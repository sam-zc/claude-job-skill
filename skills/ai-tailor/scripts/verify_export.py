#!/usr/bin/env python3
"""Evidence-first PDF audit; narrowly guarded legacy spacing repair.

Run with Python and the packages pinned in requirements.txt.
No input is overwritten. No extraction output is normalized in saved evidence.
"""
import argparse
import collections
import difflib
import hashlib
import importlib.metadata
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import unicodedata

sys.path.insert(0, str(Path(__file__).resolve().parent / '.deps'))
import pikepdf
import pypdf
import pdfplumber
import pymupdf

SPAN = re.compile(rb'/Span\s*<<\s*/ActualText\s*<FEFF200B>\s*>>\s*BDC(.*?)EMC', re.S)
OLD = b'/ActualText <FEFF200B>'
NEW = b'/ActualText <FEFF0020>'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def save_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def run(*args):
    command = ['rtk', 'proxy', *args] if shutil.which('rtk') else list(args)
    return subprocess.check_output(command, stderr=subprocess.STDOUT).decode('utf-8')


def text_stats(text):
    return {'characters': len(text), 'nonempty_lines': sum(bool(s.strip()) for s in text.splitlines()),
            'U+200B': text.count('\u200b'), 'U+FFFD': text.count('\ufffd'),
            'bullets': {f'U+{ord(c):04X}': text.count(c) for c in '●•·'},
            'format_characters': dict(collections.Counter(f'U+{ord(c):04X}' for c in text if unicodedata.category(c) == 'Cf'))}


def logical_graph(root, canonicalize_repair=False):
    """Object-number-independent graph, retaining links/cycles and stream bytes."""
    seen = {}
    def walk(o):
        ref = getattr(o, 'objgen', (0, 0))
        tag = None
        if ref != (0, 0):
            if ref in seen:
                return {'ref': seen[ref]}
            tag = len(seen)
            seen[ref] = tag
        if isinstance(o, pikepdf.Stream):
            data = o.read_bytes()
            if canonicalize_repair:
                data = data.replace(NEW, OLD)
            val = {'stream_sha256': sha(data), 'dict': {str(k): walk(v) for k, v in sorted(o.items()) if str(k) not in ['/Length', '/Filter', '/DecodeParms']}}
        elif isinstance(o, pikepdf.Dictionary):
            val = {str(k): walk(v) for k, v in sorted(o.items())}
        elif isinstance(o, pikepdf.Array):
            val = [walk(v) for v in o]
        elif isinstance(o, pikepdf.String):
            val = {'string_hex': bytes(o).hex()}
        elif isinstance(o, (bool, int, float, type(None))):
            val = o
        else:
            val = str(o)
        return {'id': tag, 'value': val} if tag is not None else val
    return walk(root)


def audit(pdf, out, render=False):
    pdf, out = Path(pdf).resolve(), Path(out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    r = pypdf.PdfReader(pdf)
    evidence = {'input': str(pdf), 'sha256': sha(pdf.read_bytes()), 'pages': len(r.pages),
                'versions': {n: importlib.metadata.version(n) for n in ['pypdf', 'pdfplumber', 'pdfminer.six', 'PyMuPDF', 'pikepdf']},
                'pdftotext_version': run('pdftotext', '-v').splitlines()[0], 'modes': {}}
    modes = {
        'poppler-raw': run('pdftotext', '-enc', 'UTF-8', '-raw', str(pdf), '-'),
        'poppler-layout': run('pdftotext', '-enc', 'UTF-8', '-layout', str(pdf), '-'),
        'poppler-default': run('pdftotext', '-enc', 'UTF-8', str(pdf), '-'),
        'pypdf-plain': '\n'.join(p.extract_text(extraction_mode='plain') or '' for p in r.pages),
        'pypdf-layout': '\n'.join(p.extract_text(extraction_mode='layout') or '' for p in r.pages),
    }
    with pdfplumber.open(pdf) as pl:
        modes['pdfplumber-default'] = '\n'.join(p.extract_text() or '' for p in pl.pages)
        fonts = collections.defaultdict(collections.Counter)
        geometry = []
        for i, p in enumerate(pl.pages):
            for c in p.chars:
                fonts[c['fontname']].update(c['text'])
            for line in p.extract_text_lines():
                geometry.append({'page': i + 1, **{k: line[k] for k in ['text', 'x0', 'x1', 'top', 'bottom']}})
        evidence['used_font_characters'] = {f: dict(c) for f, c in fonts.items()}
        save_json(out / 'line-geometry.json', geometry)
    with pymupdf.open(pdf) as mu:
        modes['pymupdf-text-unsorted'] = '\n'.join(p.get_text('text', sort=False) for p in mu)
        modes['pymupdf-text-sorted'] = '\n'.join(p.get_text('text', sort=True) for p in mu)
        evidence['links'] = [{'page': i + 1, 'uri': l.get('uri'), 'rect': list(l['from']),
                             'text': ' '.join(p.get_textbox(l['from']).split())}
                            for i, p in enumerate(mu) for l in p.get_links()]
        evidence['page_boxes'] = [list(p.rect) for p in mu]
    for name, text in modes.items():
        (out / (name + '.txt')).write_text(text)
        evidence['modes'][name] = text_stats(text)
    (out / 'pdffonts.txt').write_text(run('pdffonts', str(pdf)))
    (out / 'pdfinfo.txt').write_text(run('pdfinfo', str(pdf)))
    actual = []
    cmaps = []
    with pikepdf.open(pdf) as q:
        evidence['tagged'] = '/StructTreeRoot' in q.Root
        evidence['mark_info'] = str(q.Root.get('/MarkInfo', ''))
        evidence['pdf_syntax_warnings'] = q.check_pdf_syntax()
        for obj in q.objects:
            if isinstance(obj, pikepdf.Dictionary) and '/ActualText' in obj:
                actual.append({'object': list(obj.objgen), 'dictionary_value': str(obj.ActualText)})
            if not isinstance(obj, pikepdf.Stream):
                continue
            data = obj.read_bytes()
            for m in re.finditer(rb'/ActualText\s*(<([0-9a-fA-F\s]+)>|\(([^)]*)\))', data):
                raw = bytes.fromhex(m[2].decode()) if m[2] else m[3]
                value = raw[2:].decode('utf-16-be') if raw.startswith(b'\xfe\xff') else raw.decode('latin1')
                actual.append({'object': list(obj.objgen), 'offset': m.start(), 'value': value,
                               'context': data[max(0, m.start()-20):m.end()+120].decode('latin1')})
        for i, page in enumerate(q.pages):
            for key, font in page.Resources.Font.items():
                data = font.ToUnicode.read_bytes() if '/ToUnicode' in font else b''
                filename = f'page-{i+1}-{str(key)[1:]}-ToUnicode.txt'
                (out / filename).write_bytes(data)
                cmaps.append({'page': i+1, 'resource': str(key), 'base_font': str(font.BaseFont), 'cmap_sha256': sha(data), 'file': filename})
        evidence['actual_text_U+200B'] = sum(x.get('value', x.get('dictionary_value', '')).count('\u200b') for x in actual)
        evidence['actual_text_count'] = len(actual)
        evidence['cmaps'] = cmaps
    save_json(out / 'actual-text.json', actual)
    save_json(out / 'audit.json', evidence)
    if render:
        run('pdftoppm', '-r', '144', '-png', str(pdf), str(out / 'page'))
    return evidence


def clean(src, dst, out):
    """Replace only exporter U+200B over a confirmed space glyph with U+0020."""
    src, dst, out = Path(src).resolve(), Path(dst).resolve(), Path(out).resolve()
    if dst.exists() or src == dst:
        raise ValueError('Destination must be new; input is never overwritten')
    dst.parent.mkdir(parents=True, exist_ok=True)
    out.mkdir(parents=True, exist_ok=True)
    total = 0
    with pikepdf.open(src) as q:
        before = logical_graph(q.Root)
        before_info = logical_graph(q.docinfo)
        for page in q.pages:
            contents = page.Contents
            streams = list(contents) if isinstance(contents, pikepdf.Array) else [contents]
            for stream in streams:
                data = stream.read_bytes()
                spans = list(SPAN.finditer(data))
                if data.count(b'FEFF200B') != len(spans):
                    raise ValueError('Unexpected U+200B encoding/context; manual analysis required')
                for m in spans:
                    body = m[1]
                    names = re.findall(rb'(/F\d+)\s+[\d.]+\s+Tf', body)
                    glyphs = re.findall(rb'<([0-9A-Fa-f]+)>\s*Tj', body)
                    if len(names) != 1 or glyphs != [b'0003'] or b'TJ' in body or b"'" in body or b'"' in body:
                        raise ValueError('ActualText does not wrap exactly the expected spacing glyph')
                    font = page.Resources.Font[names[0].decode()]
                    if not re.search(rb'<0003>\s*<0020>', font.ToUnicode.read_bytes()):
                        raise ValueError('Unicode mapping does not confirm U+0020')
                    # Reject any additional drawing/text operations in this narrowly supported pattern.
                    if not re.fullmatch(rb'\s*/F\d+\s+[\d.]+\s+Tf\s+(?:[-\d.]+\s+){6}Tm\s+(?:[-\d.]+\s+){2}Td\s+<0003>\s+Tj\s*', body):
                        raise ValueError('Unrecognized marked-content operation sequence')
                total += len(spans)
                # Change only the replacement-string code point; retain BDC/EMC and glyph drawing.
                patched = SPAN.sub(lambda m: m[0].replace(OLD, NEW), data)
                if len(spans) != data.count(OLD):
                    raise ValueError('Noncanonical spacing metadata; refusing broad replacement')
                if patched != data:
                    stream.write(patched)
        if not total:
            raise ValueError('No matching defect; do not modify a clean or different export')
        if logical_graph(q.Root, True) != before or logical_graph(q.docinfo) != before_info:
            raise ValueError('Unexpected in-memory document change')
        q.save(dst)
    with pikepdf.open(dst) as q:
        if logical_graph(q.Root, True) != before or logical_graph(q.docinfo) != before_info:
            dst.unlink()
            raise ValueError('Reopened document failed full logical graph preservation')
    report = {'input_sha256': sha(src.read_bytes()), 'output_sha256': sha(dst.read_bytes()),
              'replacements': total, 'change': 'ActualText U+200B -> U+0020 only',
              'full_catalog_graph_equal_except_allowed_replacement': True,
              'info_dictionary_equal': True, 'tags_links_fonts_unicode_maps_and_drawing_preserved': True}
    save_json(out / 'cleanup.json', report)
    return report


def compare(a, b, out):
    out = Path(out).resolve(); out.mkdir(parents=True, exist_ok=True)
    from PIL import Image, ImageChops
    reports = {}
    for name, pdf in [('a', a), ('b', b)]:
        audit(pdf, out/name, render=True)
    am, bm = pymupdf.open(a), pymupdf.open(b)
    reports['page_count_equal'] = len(am) == len(bm)
    reports['render_comparison'] = []
    for i in range(min(len(am), len(bm))):
        ai = Image.open(out/'a'/f'page-{i+1}.png').convert('RGB')
        bi = Image.open(out/'b'/f'page-{i+1}.png').convert('RGB')
        same = ai.size == bi.size and ImageChops.difference(ai, bi).getbbox() is None
        reports['render_comparison'].append({'page':i+1,'poppler_144dpi_pixel_identical':same})
    for f in (out/'a').glob('*.txt'):
        other = out/'b'/f.name
        if not other.exists(): continue
        x, y = f.read_text(), other.read_text()
        (out/(f.stem+'.diff')).write_text(''.join(difflib.unified_diff(x.splitlines(True),y.splitlines(True),fromfile=str(a),tofile=str(b))))
        if f.stem.startswith(('poppler-', 'pypdf-', 'pdfplumber-', 'pymupdf-')):
            reports[f.stem] = {'byte_identical_text': x == y,
                'equal_after_only_documented_U200B_to_space': x.replace('\u200b',' ') == y,
                'equal_after_U200B_to_space_and_whitespace_collapse': ' '.join(x.replace('\u200b',' ').split()) == ' '.join(y.split())}
    save_json(out/'comparison.json', reports)
    return reports


def baseline_expectations(pdf):
    """Read header, employment and project-heading geometry from the selected PDF."""
    with pdfplumber.open(pdf) as document:
        lines = [dict(page=i + 1, **line) for i, page in enumerate(document.pages)
                 for line in page.extract_text_lines()]
        boxes = [[float(page.width), float(page.height)] for page in document.pages]
    summary = next(i for i, line in enumerate(lines) if line['text'] == 'PROFESSIONAL SUMMARY')
    headers = lines[:summary]
    roles = [line for line in lines if ' | RESPONSIVE.IO ' in line['text']
             and any(line['text'].startswith(title + ' |') for title in
                     ('Frontend Platform Engineer', 'Software Engineer', 'Associate Software Engineer'))]
    start = next(i for i, line in enumerate(lines) if line['text'] == 'PROJECTS & OPEN SOURCE')
    end = next(i for i, line in enumerate(lines[start + 1:], start + 1) if line['text'] == 'EDUCATION')
    projects = [line['text'] for line in lines[start + 1:end]
                if line['text'][0].isalnum() and line.get('chars')
                and 'bold' in line['chars'][0]['fontname'].lower()]
    if len(headers) != 2 or len(roles) != 3 or len(projects) != 3:
        raise ValueError('Selected BASE structure changed; reconcile its actual layout before verification')
    with pymupdf.open(pdf) as document:
        anchors = [{'uri': link['uri'], 'text': ' '.join(page.get_textbox(link['from']).split())}
                   for page in document for link in page.get_links() if link.get('uri')]
        links = sorted({link['uri'] for link in anchors})
    return {'headers': [{k: line[k] for k in ('text', 'page', 'x0', 'x1')} for line in headers],
            'roles': [{k: line[k] for k in ('text', 'page', 'x0', 'x1')} for line in roles],
            'project_headers': projects, 'links': links, 'link_anchors': anchors, 'page_boxes': boxes,
            'tagged': '/StructTreeRoot' in pypdf.PdfReader(pdf).trailer['/Root']}


def check(pdf, expected_text, out, base_pdf):
    """Local BASE-relative mechanical gates; agent visual/evidence review is required."""
    expected = baseline_expectations(base_pdf)
    out = Path(out).resolve()
    a = audit(pdf, out/'pdf', render=True)
    baseline = audit(base_pdf, out/'baseline-pdf')
    source = Path(expected_text).read_text()
    expected_bullets = sum(source.count(glyph) for glyph in '●•')
    source = re.sub(r'(?m)^\s*[●•] ?', '', source)
    text = (out/'pdf/pdfplumber-default.txt').read_text()
    unbulleted = re.sub(r'(?m)^\s*[●•] ?', '', text)
    source_words, pdf_words = source.split(), unbulleted.split()
    (out/'source-vs-pdf-words.diff').write_text('\n'.join(difflib.unified_diff(source_words,pdf_words,fromfile='Independent intended text',tofile='PDF pdfplumber')))
    extractor_order = {}
    for mode in a['modes']:
        extracted = (out/'pdf'/f'{mode}.txt').read_text()
        words = re.sub(r'(?m)^\s*[●•] ?', '', extracted).split()
        differences = list(difflib.unified_diff(source_words, words, fromfile='Independent intended text words', tofile=mode))
        (out/f'source-vs-{mode}.diff').write_text('\n'.join(differences))
        extractor_order[mode] = {'source_word_order_equal': source_words == words, 'diff_lines': len(differences)}
    def words_only(value):
        return re.sub(r'(?m)^\s*[●•] ?', '', value).split()
    baseline_words = words_only((out/'baseline-pdf/pdfplumber-default.txt').read_text())
    reliable_modes = [mode for mode in baseline['modes']
                      if words_only((out/'baseline-pdf'/f'{mode}.txt').read_text()) == baseline_words]
    actual_links = sorted({link['uri'] for link in a['links'] if link.get('uri')})
    expected_anchors = collections.Counter((link['uri'], link['text']) for link in expected['link_anchors'])
    actual_anchors = collections.Counter((link['uri'], link['text']) for link in a['links'] if link.get('uri'))
    norm = lambda value: ' '.join(value.split())
    normalized_source = norm(source)
    source_lines = [norm(line) for line in source.splitlines()]
    geometry = json.loads((out/'pdf/line-geometry.json').read_text())
    employment = [line for line in geometry if any(norm(line['text']) == norm(role['text']) for role in expected['roles'])]
    header = geometry[:len(expected['headers'])]
    work_start = next((i for i, line in enumerate(geometry) if line['text'] == 'WORK EXPERIENCE'), -1)
    work_end = next((i for i, line in enumerate(geometry) if i > work_start and line['text'] == 'SKILLS'), -1)
    work_geometry = geometry[work_start+1:work_end] if work_end > work_start >= 0 else []
    checks = {
        'two_pages': a['pages'] == 2,
        'page_size_preserved': len(a['page_boxes']) == len(expected['page_boxes']) and all(
            abs(box[2]-ref[0]) < .2 and abs(box[3]-ref[1]) < .2
            for box, ref in zip(a['page_boxes'], expected['page_boxes'])),
        'no_U200B_in_ActualText_or_any_extractor': a['actual_text_U+200B'] == 0 and all(m['U+200B'] == 0 for m in a['modes'].values()),
        'no_replacement_characters': all(m['U+FFFD'] == 0 for m in a['modes'].values()),
        'source_word_sequence_preserved': source_words == pdf_words,
        'reading_order_not_regressed': bool(reliable_modes) and all(
            extractor_order[mode]['source_word_order_equal'] for mode in reliable_modes),
        'base_hyperlink_destinations_preserved': set(expected['links']).issubset(actual_links),
        'base_hyperlink_anchors_preserved': not (expected_anchors - actual_anchors),
        'intended_bullets_preserved': expected_bullets > 0 and all(
            m['bullets']['U+25CF'] + m['bullets']['U+2022'] == expected_bullets for m in a['modes'].values()),
        'visible_wording_Calibri': bool(a['used_font_characters']) and all(
            'Calibri' in font for font, chars in a['used_font_characters'].items() if any(c.isalnum() for c in chars)),
        'has_Calibri_bold': any('Calibri' in font and 'bold' in font.lower() for font in a['used_font_characters']),
        'existing_tagging_preserved': not expected['tagged'] or a['tagged'],
        'no_pdf_syntax_warnings': not a['pdf_syntax_warnings'],
        'employment_associations_preserved': all(source_lines.count(norm(role['text'])) == 1 for role in expected['roles']),
        'three_employment_rows': len(employment) == 3 and sum(' | RESPONSIVE.IO ' in line['text'] for line in work_geometry) == 3,
        'employment_rows_right_aligned': len(employment) == 3 and all(
            abs(next(row['x1'] for row in employment if norm(row['text']) == norm(ref['text'])) - ref['x1']) < .5
            for ref in expected['roles']),
        'selected_header_preserved': len(header) == len(expected['headers']) and all(
            norm(row['text']) == norm(ref['text']) and abs((row['x0']+row['x1'])/2-(ref['x0']+ref['x1'])/2) < .5
            for row, ref in zip(header, expected['headers'])),
        'no_internship': not re.search(r'(?i)engineering intern|software engineer intern', source),
        'required_projects': all(norm(title) in normalized_source for title in expected['project_headers']),
    }
    lines = source.splitlines()
    sections = [line.strip() for line in lines]
    if 'PROJECTS & OPEN SOURCE' in sections and 'EDUCATION' in sections:
        start, end = sections.index('PROJECTS & OPEN SOURCE'), sections.index('EDUCATION')
        projects = '\n'.join(lines[start+1:end])
        checks['no_project_date_ranges'] = end > start and not re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+20\d\d\s*[-–]', projects)
    else:
        checks['no_project_date_ranges'] = False
    report = {'mechanical_checks_passed': all(checks.values()), 'checks': checks,
              'base_pdf': str(Path(base_pdf).resolve()), 'base_sha256': sha(Path(base_pdf).read_bytes()),
              'base_expectations': expected,
              'baseline_reliable_extractor_modes': reliable_modes,
              'extractor_order_diagnostics_require_agent_review': extractor_order,
              'employment_geometry': employment, 'header_geometry': header,
              'required_manual_gates': ['Inspect every PDF page; compare changes with the independent edit ledger', 'Reconcile content/JD evidence and protected hashes',
                  'Live parser test only when separately authorized; otherwise NOT_TESTED'],
              'not_an_ATS_score_or_cross_tenant_guarantee': True}
    save_json(out/'checks.json', report)
    return report


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    a = sub.add_parser('audit'); a.add_argument('pdf'); a.add_argument('out'); a.add_argument('--render',action='store_true')
    a = sub.add_parser('clean'); a.add_argument('src'); a.add_argument('dst'); a.add_argument('out')
    a = sub.add_parser('compare'); a.add_argument('a'); a.add_argument('b'); a.add_argument('out')
    a = sub.add_parser('check'); a.add_argument('pdf'); a.add_argument('expected_text'); a.add_argument('out')
    a.add_argument('--base-pdf', required=True)
    args = vars(p.parse_args()); cmd = args.pop('command')
    result = {'audit':audit,'clean':clean,'compare':compare,'check':check}[cmd](**args)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if cmd == 'check' and not result['mechanical_checks_passed']:
        sys.exit(2)
