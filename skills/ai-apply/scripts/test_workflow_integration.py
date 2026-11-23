"""Exercise real PDF QA, claim release/reuse and pre-upload validation locally.

Review records here are explicitly synthetic test fixtures, not agent visual signoff.
No browser, Sheet, email, submission or real job artifact is touched.
"""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import pikepdf
from validate_pdf import validate, write_receipt
from coordination import BASE, bind, claim, finish, now, sha, update

REPO = Path(__file__).resolve().parents[3]


class WorkflowIntegrationTests(unittest.TestCase):
    def test_direct_pdf_through_released_claim_and_application_reuse(self):
        with tempfile.TemporaryDirectory(prefix='synthetic-application-') as temp:
            root = Path(temp).resolve()
            (root / 'main-resume').mkdir()
            shutil.copy2(REPO / BASE, root / BASE)
            (root / 'contexts').mkdir()
            (root / 'contexts/personal.md').write_text('Synthetic evidence fixture only')
            folder = 'sample/frontend-123'
            aliases = ['company:sample:123', 'https://example.com/jobs/123']
            first = claim(root, folder, aliases, 'synthetic-tailor', 'Sample', 'Frontend', '123')
            job = Path(first['jobDir'])
            (job / 'source').mkdir()
            source = job / 'source/frontend-base.pdf'
            shutil.copy2(root / BASE, source)
            bind(root, folder, first['token'], source)
            # Prepare intended text from the unchanged source, before editing.
            text = subprocess.check_output(['rtk', 'proxy', 'pdftotext', '-layout', str(source), '-'], text=True)
            (job / 'expected.txt').write_text(text.replace('product and design', 'design and product', 1))
            with pikepdf.open(source) as document:
                count = 0
                for page in document.pages:
                    streams = list(page.Contents) if isinstance(page.Contents, pikepdf.Array) else [page.Contents]
                    for stream in streams:
                        data = stream.read_bytes()
                        count += data.count(b'product and design')
                        if b'product and design' in data:
                            stream.write(data.replace(b'product and design', b'design and product'))
                self.assertEqual(count, 1)
                document.save(job / 'resume.pdf')
            protected = {name: sha(root / name) for name in (BASE, 'contexts/personal.md')}
            (job / 'source/protected-hashes.json').write_text(json.dumps(protected))
            iteration = job / 'exports/01'
            iteration.mkdir(parents=True)
            shutil.copyfile(job / 'resume.pdf', iteration / 'direct.pdf')
            shutil.copyfile(job / 'expected.txt', iteration / 'expected.txt')
            proof = dict(sourceBasePath=str(root / BASE), sourceBaseSha256=sha(root / BASE),
                         sourceCopyPath=str(source), sourceCopySha256=sha(source),
                         workingPdfPath=str(job / 'resume.pdf'), workingPdfSha256=sha(job / 'resume.pdf'),
                         expectedTextSha256=sha(job / 'expected.txt'), capturedAt=now(), generatedAt=now(),
                         ownershipToken=first['token'])
            original_proof = iteration / 'provenance.json'
            original_proof.write_text(json.dumps(proof))
            qa = job / 'qa/01'
            result = subprocess.run(['rtk', 'proxy', sys.executable,
                str(REPO / 'skills/ai-tailor/scripts/verify_job.py'), '--workspace', str(root),
                '--job-dir', str(job), '--provenance', str(original_proof),
                '--expected-text', str(iteration / 'expected.txt'), '--pdf', str(iteration / 'direct.pdf'),
                '--out', str(qa)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            candidate_hash = sha(qa / 'candidate.pdf')
            final = job / 'sample-frontend-123-resume.pdf'
            shutil.copyfile(qa / 'candidate.pdf', final)
            with self.assertRaisesRegex(ValueError, 'review.json'):
                validate(root, final, original_proof, candidate_hash, qa)
            # Synthetic review attestation to test handoff plumbing only.
            (qa / 'review.json').write_text(json.dumps(dict(candidateSha256=candidate_hash,
                expectedTextSha256=proof['expectedTextSha256'], reviewedAt=now(), evidenceReviewed=True,
                jdReconciled=True, protectedInputsVerified=True, pages=[
                    dict(page=i, observations='Synthetic integration review fixture; not a real visual signoff')
                    for i in (1, 2)])))
            validate(root, final, original_proof, candidate_hash, qa)
            update(root, folder, first['token'], 'TAILORED', 'Synthetic QA complete')
            finish(root, folder, first['token'])
            with self.assertRaisesRegex(ValueError, 'not owned'):
                validate(root, final, original_proof, candidate_hash, qa)
            attempt = claim(root, folder, aliases, 'synthetic-apply', 'Sample', 'Frontend', '123')
            reused = job / 'application/01/provenance.json'
            reused.parent.mkdir(parents=True)
            reused.write_text(json.dumps({**proof, 'ownershipToken': attempt['token'],
                                         'reusedFrom': str(original_proof)}))
            checked = validate(root, final, reused, candidate_hash, qa)
            write_receipt(root, final, job / 'qa/upload/before-upload.json', checked, reused)
            self.assertEqual(sha(final), candidate_hash)
            self.assertEqual(json.loads(original_proof.read_text()), proof)
            self.assertTrue(all(sha(root / name) == digest for name, digest in protected.items()))
            # A fake confirmed outcome exercises local duplicate prevention, never a live submission.
            update(root, folder, attempt['token'], 'APPLIED', 'Synthetic confirmation fixture only')
            finish(root, folder, attempt['token'])
            with self.assertRaisesRegex(ValueError, 'APPLIED duplicate'):
                claim(root, folder, aliases, 'synthetic-retry', 'Sample', 'Frontend', '123')


if __name__ == '__main__':
    unittest.main()
