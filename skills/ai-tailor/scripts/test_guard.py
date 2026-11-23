"""Exercise local lineage/ownership, duplicate handling and protected-input guards."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from coordination import BASE, claim, bind, finish, update, sha
from verify_job import guard, inside

REAL_BASE = Path(__file__).resolve().parents[3] / 'assets/frontend-base.pdf'


class GuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        (self.root / 'main-resume').mkdir()
        shutil.copy2(REAL_BASE, self.root / BASE)
        (self.root / 'contexts').mkdir()
        (self.root / 'contexts/personal.md').write_text('Confirmed candidate facts')
        self.folder = 'sample/frontend-engineer-123'
        result = self.claim(self.folder, 'company:sample:123')
        self.token = result['token']
        self.job = Path(result['jobDir'])
        (self.job / 'source').mkdir()
        copy = self.job / 'source/frontend-base.pdf'
        shutil.copy2(self.root / BASE, copy)
        bind(self.root, self.folder, self.token, copy)
        shutil.copy2(self.root / BASE, self.job / 'resume.pdf')
        (self.job / 'expected.txt').write_text('Independently planned synthetic final wording')
        (self.job / 'source/protected-hashes.json').write_text(json.dumps({
            BASE: sha(self.root / BASE), 'contexts/personal.md': sha(self.root / 'contexts/personal.md')}))
        self.provenance = dict(sourceBasePath=str(self.root / BASE), sourceBaseSha256=sha(self.root / BASE),
            sourceCopyPath=str(copy), sourceCopySha256=sha(copy),
            workingPdfPath=str(self.job / 'resume.pdf'), workingPdfSha256=sha(self.job / 'resume.pdf'),
            expectedTextSha256=sha(self.job / 'expected.txt'),
            capturedAt='2026-11-23T10:00:00+05:30', generatedAt='2026-11-23T10:01:00+05:30', ownershipToken=self.token)

    def claim(self, folder, alias, retailor=False):
        return claim(self.root, folder, [alias], 'synthetic-test', 'Sample', 'Frontend Engineer', alias.rsplit(':', 1)[-1], retailor)

    def tearDown(self):
        self.temp.cleanup()

    def test_owned_local_copy_accepted(self):
        self.assertEqual(guard(self.root, self.job, self.provenance), self.job)

    def test_token_cannot_access_another_job(self):
        other = self.claim('sample/other-456', 'company:sample:456')
        with self.assertRaisesRegex(ValueError, 'not owned'):
            guard(self.root, other['jobDir'], self.provenance)

    def test_released_copy_cannot_be_verified(self):
        finish(self.root, self.folder, self.token)
        with self.assertRaisesRegex(ValueError, 'not owned'):
            guard(self.root, self.job, self.provenance)

    def test_wrong_lineage_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Provenance'):
            guard(self.root, self.job, {**self.provenance, 'sourceBasePath': str(self.root / 'reference.pdf')})

    def test_old_flat_folder_rejected(self):
        with self.assertRaisesRegex(ValueError, 'company-slug/role-job-slug'):
            guard(self.root, self.root / 'workflows/old-flat-job', self.provenance)

    def test_changed_base_rejected(self):
        (self.root / BASE).write_bytes(b'changed source')
        with self.assertRaisesRegex(ValueError, 'BASE changed'):
            guard(self.root, self.job, self.provenance)

    def test_changed_copy_rejected(self):
        (self.job / 'source/frontend-base.pdf').write_bytes(b'changed copy')
        with self.assertRaisesRegex(ValueError, 'Provenance'):
            guard(self.root, self.job, self.provenance)

    def test_changed_context_rejected(self):
        (self.root / 'contexts/personal.md').write_text('unexpected mutation')
        with self.assertRaisesRegex(ValueError, 'Protected input changed'):
            guard(self.root, self.job, self.provenance)

    def test_changed_working_pdf_rejected(self):
        (self.job / 'resume.pdf').write_bytes(b'new revision')
        with self.assertRaisesRegex(ValueError, 'Working PDF'):
            guard(self.root, self.job, self.provenance)

    def test_changed_independent_expected_text_rejected(self):
        (self.job / 'expected.txt').write_text('changed intended wording')
        with self.assertRaisesRegex(ValueError, 'expected text changed'):
            guard(self.root, self.job, self.provenance)

    def test_alias_cannot_claim_a_second_folder(self):
        with self.assertRaisesRegex(ValueError, 'Existing alias'):
            self.claim('other/frontend-999', 'company:sample:123')

    def test_same_requisition_rejected_even_with_different_board_aliases(self):
        with self.assertRaisesRegex(ValueError, 'company/requisition'):
            claim(self.root, 'sample/different-title-123', ['board:new-alias'], 'test', 'Sample', 'New Title', '123')

    def test_existing_folder_cannot_change_requisition(self):
        with self.assertRaisesRegex(ValueError, 'different job identity'):
            claim(self.root, self.folder, ['company:sample:123'], 'test', 'Sample', 'Frontend', '456')

    def test_unknown_status_does_not_change_job(self):
        before = (self.job / 'job.json').read_bytes()
        with self.assertRaisesRegex(ValueError, 'Unsupported job status'):
            update(self.root, self.folder, self.token, 'DUPLICATE', 'Do not downgrade')
        self.assertEqual((self.job / 'job.json').read_bytes(), before)

    def test_protected_snapshot_cannot_be_a_symlink_outside_job(self):
        snapshot = self.job / 'source/protected-hashes.json'
        external = self.root / 'snapshot.json'
        snapshot.rename(external)
        snapshot.symlink_to(external)
        with self.assertRaisesRegex(ValueError, 'inside the job'):
            guard(self.root, self.job, self.provenance)

    def test_active_claim_cannot_be_stolen(self):
        with self.assertRaisesRegex(ValueError, 'active owner'):
            self.claim(self.folder, 'company:sample:123')

    def test_applied_retailor_keeps_application_history(self):
        update(self.root, self.folder, self.token, 'APPLIED', 'Synthetic confirmed success')
        finish(self.root, self.folder, self.token)
        with self.assertRaisesRegex(ValueError, 'APPLIED duplicate'):
            self.claim(self.folder, 'company:sample:123')
        token = self.claim(self.folder, 'company:sample:123', retailor=True)['token']
        data = update(self.root, self.folder, token, 'TAILORED', 'Explicit synthetic re-tailor')
        self.assertEqual(data['status'], 'APPLIED')
        self.assertEqual(data['tailoringStatus'], 'TAILORED')
        self.assertIn('APPLIED', (self.root / 'workflows/log.md').read_text())
        self.assertEqual(data['history'][0]['note'], 'Synthetic confirmed success')

    def test_external_and_symlinked_outputs_rejected(self):
        with self.assertRaisesRegex(ValueError, 'inside the job'):
            inside(self.root / 'main-resume/output.pdf', self.job)
        (self.job / 'escape').symlink_to(self.root / 'main-resume', target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'inside the job'):
            inside(self.job / 'escape/output.pdf', self.job)


if __name__ == '__main__':
    unittest.main()
