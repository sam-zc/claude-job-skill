#!/usr/bin/env python3
"""Check a saved edited PDF against independent intended text in a NEW output directory.

Does not submit applications or certify an ATS result.
"""
import argparse
from pathlib import Path
import shutil
import verify_export as v

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('pdf', type=Path)
p.add_argument('expected_text', type=Path)
p.add_argument('output_directory', type=Path)
p.add_argument('--base-pdf', type=Path, required=True)
args = p.parse_args()
pdf, expected = args.pdf.resolve(), args.expected_text.resolve()
if not pdf.is_file() or not expected.is_file():
    p.error('Edited PDF and independent expected text must exist')
out = args.output_directory.resolve()
out.mkdir(parents=True, exist_ok=False)
(out/'inputs').mkdir()
shutil.copy2(pdf, out/'inputs/direct.pdf')
shutil.copy2(expected, out/'inputs/expected.txt')
source = out/'inputs/direct.pdf'
candidate = out/'candidate.pdf'
a = v.audit(source, out/'qa/direct')
if a['actual_text_U+200B']:
    v.clean(source, candidate, out/'qa/cleanup')
else:
    shutil.copy2(source, candidate)
c = v.compare(source, candidate, out/'qa/comparison')
if not c['page_count_equal'] or not all(x['poppler_144dpi_pixel_identical'] for x in c['render_comparison']):
    raise SystemExit('FAIL: rendered candidate differs from direct export; inspect evidence')
r = v.check(candidate, out/'inputs/expected.txt', out/'qa/final', base_pdf=args.base_pdf)
status = {'status': 'MECHANICAL_PASS_AGENT_VISUAL_REVIEW_REQUIRED' if r['mechanical_checks_passed'] else 'FAIL',
          'candidate_pdf': str(candidate), 'expected_text_sha256': v.sha(expected.read_bytes()),
          'direct_sha256': a['sha256'], 'candidate_sha256': v.sha(candidate.read_bytes()),
          'manual_steps': r['required_manual_gates'],
          'live_ATS_verified': False, 'submitted': False}
v.save_json(out/'status.json', status)
print(status['status'])
print('Inspect every page PNG in', out/'qa/final/pdf')
print('Agent: inspect every page; record live ATS as NOT_TESTED unless separately authorized and observed.')
if not r['mechanical_checks_passed']:
    raise SystemExit(2)
