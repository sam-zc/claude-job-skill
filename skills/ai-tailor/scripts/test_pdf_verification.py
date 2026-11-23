"""Real PDF regression cases; all generated files stay in a temporary workspace."""
from pathlib import Path
import re
import subprocess
import tempfile
import unittest

import pikepdf
import pymupdf
import verify_export as v


BASE = Path(__file__).resolve().parents[3] / 'assets/frontend-base.pdf'


class PDFVerificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='pdf-verification-regression-')
        cls.root = Path(cls.temp.name).resolve()
        cls.base_text = subprocess.check_output(
            ['rtk', 'proxy', 'pdftotext', '-layout', str(BASE), '-'], text=True)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def check_pdf(self, pdf, expected, label):
        text = self.root / (label + '.txt')
        text.write_text(expected)
        return v.check(pdf, text, self.root / (label + '-qa'), BASE)

    def test_real_in_place_edit_preserves_all_parser_orders(self):
        candidate = self.root / 'in-place.pdf'
        replacements = 0
        with pikepdf.open(BASE) as doc:
            for page in doc.pages:
                streams = list(page.Contents) if isinstance(page.Contents, pikepdf.Array) else [page.Contents]
                for stream in streams:
                    data = stream.read_bytes()
                    replacements += data.count(b'product and design')
                    if b'product and design' in data:
                        # Same source-encoded glyphs/total advance, in the original draw operation.
                        stream.write(data.replace(b'product and design', b'design and product'))
            self.assertEqual(replacements, 1)
            doc.save(candidate)
        result = self.check_pdf(candidate, self.base_text.replace('product and design', 'design and product', 1), 'in-place')
        self.assertTrue(result['mechanical_checks_passed'], result['checks'])
        self.assertEqual(len(result['baseline_reliable_extractor_modes']), 8)
        self.assertTrue(all(item['source_word_order_equal'] for item in result['extractor_order_diagnostics_require_agent_review'].values()))

    def test_swapped_link_targets_rejected_even_with_same_URI_set(self):
        candidate = self.root / 'swapped-links.pdf'
        with pymupdf.open(BASE) as doc:
            page = doc[0]
            links = page.get_links()
            github = next(link for link in links if link.get('uri') == 'https://github.com/sam-zc')
            portfolio = next(link for link in links if link.get('uri') == 'https://sanjeev.quest')
            github['uri'], portfolio['uri'] = portfolio['uri'], github['uri']
            page.update_link(github)
            page.update_link(portfolio)
            doc.save(candidate)
        result = self.check_pdf(candidate, self.base_text, 'swapped-links')
        self.assertTrue(result['checks']['base_hyperlink_destinations_preserved'])
        self.assertFalse(result['checks']['base_hyperlink_anchors_preserved'])
        self.assertFalse(result['mechanical_checks_passed'])

    def test_visual_order_does_not_hide_content_stream_order_regression(self):
        candidate = self.root / 'reordered-content.pdf'
        moved = None
        with pikepdf.open(BASE) as doc:
            page = doc.pages[0]
            streams = list(page.Contents) if isinstance(page.Contents, pikepdf.Array) else [page.Contents]
            for stream in streams:
                data = stream.read_bytes()
                match = re.search(rb'\(open-source UI components\. Works with product and design[^\n]*?\) Tj', data)
                if match:
                    self.assertIsNone(moved)
                    moved = match.group(0)
                    stream.write(data[:match.start()] + data[match.end():])
            self.assertIsNotNone(moved)
            # Same text/font/position, but appended after the rest of the page's content.
            page.Contents = pikepdf.Array([*streams, pikepdf.Stream(doc,
                b'q .12549 .129412 .141176 rg BT /F3+0 10 Tf 1 0 0 1 36 639 Tm ' + moved + b' ET Q')])
            doc.save(candidate)
        result = self.check_pdf(candidate, self.base_text, 'reordered-content')
        self.assertTrue(result['checks']['source_word_sequence_preserved'])
        self.assertFalse(result['checks']['reading_order_not_regressed'])
        self.assertFalse(result['mechanical_checks_passed'])


if __name__ == '__main__':
    unittest.main()
