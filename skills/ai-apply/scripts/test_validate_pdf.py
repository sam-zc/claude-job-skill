"""Upload guard behavior using isolated company/job locks and real BASE bytes."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from pypdf import PdfWriter
from validate_pdf import validate, write_receipt
from coordination import BASE, bind, claim, finish, sha, update

FIXTURE = Path(__file__).resolve().parents[3] / 'assets/frontend-base.pdf'


class UploadGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        (self.root / 'main-resume').mkdir()
        shutil.copy2(FIXTURE, self.root / BASE)
        self.folder = 'sample/frontend-123'
        result = claim(self.root, self.folder, ['company:sample:123'], 'synthetic-test', 'Sample', 'Frontend', '123')
        self.token = result['token']
        self.job = Path(result['jobDir'])
        (self.job / 'source').mkdir()
        copy = self.job / 'source/frontend-base.pdf'
        shutil.copy2(FIXTURE, copy)
        bind(self.root, self.folder, self.token, copy)
        shutil.copy2(self.root / BASE, self.job / 'resume.pdf')
        (self.job / 'expected.txt').write_text('Independently planned synthetic final wording')
        (self.job / 'source/protected-hashes.json').write_text(json.dumps({BASE: sha(self.root / BASE)}))
        self.pdf = self.job / 'sample-frontend-123-resume.pdf'
        shutil.copyfile(FIXTURE, self.pdf)
        self.expected = sha(self.pdf)
        self.provenance = self.job / 'provenance.json'
        self.proof = dict(sourceBasePath=str(self.root / BASE), sourceBaseSha256=sha(FIXTURE),
            sourceCopyPath=str(copy), sourceCopySha256=sha(copy),
            workingPdfPath=str(self.job / 'resume.pdf'), workingPdfSha256=sha(self.job / 'resume.pdf'),
            expectedTextSha256=sha(self.job / 'expected.txt'),
            capturedAt='2026-11-23T10:00:00+05:30', generatedAt='2026-11-23T10:01:00+05:30', ownershipToken=self.token)
        self.provenance.write_text(json.dumps(self.proof))
        # Synthetic attestation fixtures exercise the upload handoff, not visual QA itself.
        self.qa = self.job / 'qa/iteration-01'
        (self.qa / 'inputs').mkdir(parents=True)
        (self.qa / 'qa/final').mkdir(parents=True)
        shutil.copy2(self.pdf, self.qa / 'candidate.pdf')
        shutil.copy2(self.job / 'resume.pdf', self.qa / 'inputs/direct.pdf')
        shutil.copy2(self.job / 'expected.txt', self.qa / 'inputs/expected.txt')
        (self.qa / 'status.json').write_text(json.dumps(dict(
            status='MECHANICAL_PASS_AGENT_VISUAL_REVIEW_REQUIRED', candidate_pdf=str(self.qa / 'candidate.pdf'),
            candidate_sha256=self.expected, direct_sha256=self.proof['workingPdfSha256'],
            expected_text_sha256=self.proof['expectedTextSha256'])))
        (self.qa / 'qa/final/checks.json').write_text(json.dumps(dict(
            mechanical_checks_passed=True, checks={'synthetic_unit_fixture': True},
            base_sha256=self.proof['sourceBaseSha256'])))
        (self.qa / 'provenance.json').write_text(json.dumps({
            **{k: v for k, v in self.proof.items() if k != 'ownershipToken'}, 'workingPdfMatchesIteration': True}))
        self.review = dict(candidateSha256=self.expected, expectedTextSha256=self.proof['expectedTextSha256'],
            reviewedAt='2026-11-23T10:03:00+05:30', evidenceReviewed=True, jdReconciled=True,
            protectedInputsVerified=True, pages=[{'page': page, 'observations': 'Synthetic unit review fixture'} for page in (1, 2)])
        (self.qa / 'review.json').write_text(json.dumps(self.review))

    def check(self, pdf=None):
        return validate(self.root, pdf or self.pdf, self.provenance, self.expected, self.qa)

    def tearDown(self):
        self.temp.cleanup()

    def test_owned_reviewed_two_page_copy_passes(self):
        result = self.check()
        self.assertEqual(result['page_count'], 2)
        self.assertEqual(result['sha256'], self.expected)
        self.assertTrue(result['mechanical_QA_verified'])
        self.assertTrue(result['visual_review_recorded'])
        self.assertTrue(result['agent_review_is_attestation'])

    def test_unreviewed_hash_alone_cannot_pass(self):
        with self.assertRaisesRegex(ValueError, 'QA directory is required'):
            validate(self.root, self.pdf, self.provenance, self.expected)

    def test_missing_visual_review_blocks_upload(self):
        (self.qa / 'review.json').unlink()
        with self.assertRaisesRegex(ValueError, 'Required QA evidence missing'):
            self.check()

    def test_stale_review_or_missing_page_blocks_upload(self):
        for mutation in ({'candidateSha256': '0'*64}, {'pages': self.review['pages'][:1]},
                         {'evidenceReviewed': False}):
            (self.qa / 'review.json').write_text(json.dumps({**self.review, **mutation}))
            with self.assertRaisesRegex(ValueError, 'complete recorded'):
                self.check()

    def test_failed_mechanical_QA_blocks_upload(self):
        (self.qa / 'qa/final/checks.json').write_text(json.dumps(dict(
            mechanical_checks_passed=False, checks={'reading_order': False})))
        with self.assertRaisesRegex(ValueError, 'Mechanical QA did not pass'):
            self.check()

    def test_nonboolean_mechanical_pass_does_not_authorize_upload(self):
        evidence = self.qa / 'qa/final/checks.json'
        original = json.loads(evidence.read_text())
        for invalid in ('false', 'true', 1):
            evidence.write_text(json.dumps({**original, 'mechanical_checks_passed': invalid}))
            with self.assertRaisesRegex(ValueError, 'Mechanical QA did not pass'):
                self.check()

    def test_altered_QA_candidate_blocks_upload(self):
        (self.qa / 'candidate.pdf').write_bytes(b'changed candidate')
        with self.assertRaisesRegex(ValueError, 'checked QA candidate'):
            self.check()

    def test_changed_QA_intended_text_blocks_upload(self):
        (self.qa / 'inputs/expected.txt').write_text('changed after verification')
        with self.assertRaisesRegex(ValueError, 'QA provenance or intended-text'):
            self.check()

    def test_wrong_source_lineage_rejected(self):
        self.provenance.write_text(json.dumps({**self.proof, 'sourceBasePath': str(self.root / 'reference.pdf')}))
        with self.assertRaisesRegex(ValueError, 'Provenance'):
            self.check()

    def test_changed_upload_rejected(self):
        self.pdf.write_bytes(self.pdf.read_bytes() + b'\n% changed since review\n')
        with self.assertRaisesRegex(ValueError, 'SHA256 differs'):
            self.check()

    def test_finished_owner_rejected(self):
        finish(self.root, self.folder, self.token)
        with self.assertRaisesRegex(ValueError, 'not owned'):
            self.check()

    def test_prepared_resume_reused_under_new_claim_without_rewriting(self):
        before = {p: p.read_bytes() for p in (self.pdf, self.job / 'resume.pdf',
                  self.job / 'expected.txt', self.provenance, self.qa / 'review.json')}
        update(self.root, self.folder, self.token, 'TAILORED', 'Synthetic preparation complete')
        finish(self.root, self.folder, self.token)
        result = claim(self.root, self.folder, ['company:sample:123'], 'synthetic-apply', 'Sample', 'Frontend', '123')
        with self.assertRaisesRegex(ValueError, 'not owned'):
            self.check()
        attempt = self.job / 'application/attempt-01/provenance.json'
        attempt.parent.mkdir(parents=True)
        attempt.write_text(json.dumps({**self.proof, 'ownershipToken': result['token'],
                                     'reusedFrom': str(self.provenance)}))
        checked = validate(self.root, self.pdf, attempt, self.expected, self.qa)
        self.assertEqual(checked['sha256'], self.expected)
        for path, content in before.items():
            self.assertEqual(path.read_bytes(), content)
        history = json.loads((self.job / 'job.json').read_text())['history']
        self.assertIn('TAILORED', [item['status'] for item in history])
        (self.qa / 'review.json').unlink()
        with self.assertRaisesRegex(ValueError, 'Required QA evidence missing'):
            validate(self.root, self.pdf, attempt, self.expected, self.qa)

    def test_wrong_job_and_symlink_rejected(self):
        other = self.root / 'workflows/sample/other-456'
        other.mkdir()
        other_pdf = other / 'sample-other-456-resume.pdf'
        shutil.copyfile(self.pdf, other_pdf)
        with self.assertRaisesRegex(ValueError, 'Provenance must stay'):
            self.check(pdf=other_pdf)
        original = self.job / 'original.pdf'
        self.pdf.rename(original)
        self.pdf.symlink_to(original)
        with self.assertRaisesRegex(ValueError, 'Symlinked'):
            self.check()

    def test_old_flat_folder_rejected(self):
        old = self.root / 'workflows/flat-123'
        old.mkdir()
        pdf = old / 'flat-123-resume.pdf'
        shutil.copyfile(self.pdf, pdf)
        with self.assertRaisesRegex(ValueError, 'workflows/company/job'):
            self.check(pdf=pdf)

    def test_final_filename_requires_company_prefix(self):
        wrong = self.job / 'frontend-123-resume.pdf'
        shutil.copyfile(self.pdf, wrong)
        with self.assertRaisesRegex(ValueError, 'PDF name must be'):
            self.check(pdf=wrong)

    def test_nested_iteration_cannot_be_uploaded_as_final(self):
        nested = self.job / 'exports/01/direct.pdf'
        nested.parent.mkdir(parents=True)
        shutil.copyfile(self.pdf, nested)
        with self.assertRaisesRegex(ValueError, 'workflows/company/job'):
            self.check(pdf=nested)

    def test_receipt_saved_in_same_job_and_not_overwritten(self):
        receipt = self.job / 'qa/upload/before-submit.json'
        result = self.check()
        write_receipt(self.root, self.pdf, receipt, result, self.provenance)
        self.assertEqual(json.loads(receipt.read_text())['sha256'], self.expected)
        with self.assertRaises(FileExistsError):
            write_receipt(self.root, self.pdf, receipt, result, self.provenance)

    def test_receipt_cannot_escape_job_or_overwrite_a_source(self):
        for target in (self.root / 'result.json', self.job / 'source/result.json',
                       self.root / 'workflows/other/job/qa/upload/result.json'):
            with self.assertRaisesRegex(ValueError, 'inside this job/qa/upload'):
                write_receipt(self.root, self.pdf, target, self.check(), self.provenance)
            self.assertFalse(target.exists())

    def test_receipt_rejects_symlinked_directory(self):
        (self.job / 'qa').mkdir(exist_ok=True)
        (self.job / 'qa/upload').symlink_to(self.root, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'inside this job/qa/upload'):
            write_receipt(self.root, self.pdf, self.job / 'qa/upload/result.json', self.check(), self.provenance)

    def test_blocked_receipt_records_failure_inside_job(self):
        receipt = self.job / 'qa/upload/failed-upload.json'
        result = {'structural_gate': 'BLOCKED', 'reason': 'Synthetic changed upload'}
        write_receipt(self.root, self.pdf, receipt, result, self.provenance)
        self.assertEqual(json.loads(receipt.read_text()), result)

    def test_receipt_requires_current_job_ownership(self):
        receipt = self.job / 'qa/upload/stale-owner.json'
        finish(self.root, self.folder, self.token)
        with self.assertRaisesRegex(ValueError, 'not owned'):
            write_receipt(self.root, self.pdf, receipt, {'structural_gate': 'BLOCKED'}, self.provenance)
        self.assertFalse(receipt.exists())

    def test_cli_saves_same_job_receipt(self):
        receipt = self.job / 'qa/upload/cli-before-submit.json'
        result = subprocess.run([sys.executable, str(Path(__file__).with_name('validate_pdf.py')),
            '--workspace', str(self.root), '--pdf', str(self.pdf),
            '--provenance', str(self.provenance), '--expected-sha256', self.expected,
            '--qa-dir', str(self.qa),
            '--receipt-out', str(receipt)], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        stdout = json.loads(result.stdout)
        self.assertEqual(json.loads(receipt.read_text()), stdout)
        self.assertEqual(stdout['sha256'], self.expected)
        self.assertIn('checkedAt', stdout)

    def test_one_three_and_encrypted_pdfs_rejected(self):
        for pages, encrypted in [(1, False), (3, False), (2, True)]:
            writer = PdfWriter()
            for _ in range(pages):
                writer.add_blank_page(width=612, height=792)
            if encrypted:
                writer.encrypt('fixture-only')
            writer.write(self.pdf)
            self.expected = sha(self.pdf)
            with self.assertRaisesRegex(ValueError, 'Encrypted|exactly 2'):
                self.check()


if __name__ == '__main__':
    unittest.main()
