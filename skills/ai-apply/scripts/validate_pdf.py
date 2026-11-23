#!/usr/bin/env python3
"""Validate an owned company/job PDF without editing it; optionally save a receipt."""

import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import sys


MAX_PAGES = 2


# Share the same BASE lineage and coordination checks as the edited-PDF guard.
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "ai-tailor/scripts"))
from verify_job import guard, inside
from coordination import job_path, owned, now


def write_receipt(workspace, pdf, destination, result, provenance_path):
    """Keep a new validation receipt under this same job's qa/upload directory."""
    root = Path(workspace).resolve(strict=True)
    raw = Path(pdf)
    candidate = raw if raw.is_absolute() else root / raw
    if '..' in candidate.parts:
        raise ValueError('PDF path traversal is forbidden')
    try:
        company, slug, filename = candidate.relative_to(root / 'workflows').parts
    except ValueError:
        raise ValueError('Receipt requires a workflows/company/job PDF path') from None
    job = job_path(root, company + '/' + slug)
    if filename != company + '-' + slug + '-resume.pdf' or not job.is_dir():
        raise ValueError('Receipt requires the canonical final PDF path and an existing job')
    raw_proof = Path(provenance_path)
    proof_file = raw_proof if raw_proof.is_absolute() else root / raw_proof
    inside(proof_file, job)
    proof = json.loads(proof_file.read_text())
    owned(root, company + '/' + slug, proof.get('ownershipToken'))
    raw = Path(destination)
    target = raw if raw.is_absolute() else root / raw
    if ('..' in target.parts or target.resolve() != target
            or not target.is_relative_to(job / 'qa/upload') or target.suffix != '.json'):
        raise ValueError('Receipt must be a new JSON file inside this job/qa/upload')
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('x') as stream:
        stream.write(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return target


def verify_qa(job, qa_dir, provenance, expected_sha256, page_count):
    """Bind the final bytes to actual mechanical QA and a recorded agent review."""
    if qa_dir is None:
        raise ValueError('The checked QA directory is required; a caller hash alone is insufficient')
    qa = inside(qa_dir, job)
    def read(relative):
        path = inside(qa / relative, job)
        if not path.is_file():
            raise ValueError('Required QA evidence missing: ' + relative)
        value = json.loads(path.read_text())
        if not isinstance(value, dict):
            raise ValueError('QA evidence must be a JSON object: ' + relative)
        return value
    status = read('status.json')
    checks = read('qa/final/checks.json')
    proof = read('provenance.json')
    review = read('review.json')
    candidate = inside(qa / 'candidate.pdf', job)
    if (status.get('status') != 'MECHANICAL_PASS_AGENT_VISUAL_REVIEW_REQUIRED'
            or checks.get('mechanical_checks_passed') is not True or not isinstance(checks.get('checks'), dict)
            or not checks['checks']
            or not all(value is True for value in checks['checks'].values())):
        raise ValueError('Mechanical QA did not pass')
    if (status.get('candidate_pdf') != str(candidate)
            or status.get('candidate_sha256') != expected_sha256 or sha_file(candidate) != expected_sha256):
        raise ValueError('Final PDF does not match the checked QA candidate')
    keys = ('sourceBasePath', 'sourceBaseSha256', 'sourceCopyPath', 'sourceCopySha256',
            'workingPdfPath', 'workingPdfSha256', 'expectedTextSha256')
    if (proof.get('workingPdfMatchesIteration') is not True
            or any(proof.get(key) != provenance.get(key) for key in keys)
            or checks.get('base_sha256') != provenance['sourceBaseSha256']
            or status.get('direct_sha256') != provenance['workingPdfSha256']
            or status.get('expected_text_sha256') != provenance['expectedTextSha256']
            or sha_file(inside(qa / 'inputs/direct.pdf', job)) != provenance['workingPdfSha256']
            or sha_file(inside(qa / 'inputs/expected.txt', job)) != provenance['expectedTextSha256']):
        raise ValueError('QA provenance or intended-text evidence is stale or belongs to another revision')
    pages = review.get('pages', [])
    if (review.get('candidateSha256') != expected_sha256
            or review.get('expectedTextSha256') != provenance['expectedTextSha256']
            or not review.get('reviewedAt')
            or any(review.get(key) is not True for key in ('evidenceReviewed', 'jdReconciled', 'protectedInputsVerified'))
            or not isinstance(pages, list) or len(pages) != page_count
            or any(not isinstance(page, dict) or type(page.get('page')) is not int
                   or not isinstance(page.get('observations'), str)
                   or not page['observations'].strip() for page in pages)
            or {page.get('page') for page in pages} != set(range(1, page_count + 1))):
        raise ValueError('Current candidate needs a complete recorded all-page visual and evidence review')
    return qa


def sha_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate(workspace, pdf, provenance_path, expected_sha256, qa_dir=None):
    """Return facts about exact PDF bytes, or raise ValueError on gate failure."""
    root = Path(workspace).resolve(strict=True)
    workflows = root / "workflows"
    if not workflows.is_dir() or workflows.is_symlink():
        raise ValueError("Workspace must contain a real workflows directory")
    raw = Path(pdf)
    if ".." in raw.parts:
        raise ValueError("PDF path traversal is forbidden")
    candidate = raw if raw.is_absolute() else root / raw
    try:
        relative = candidate.relative_to(workflows)
    except ValueError:
        raise ValueError("PDF must be inside workspace/workflows") from None
    if len(relative.parts) != 3:
        raise ValueError("PDF must be inside workflows/company/job")
    company, slug, filename = relative.parts
    if not all(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", x) for x in (company, slug)):
        raise ValueError("Company/job folders must use lowercase ASCII letters/digits/hyphens")
    if filename != company + "-" + slug + "-resume.pdf":
        raise ValueError("PDF name must be <company>-<job-folder>-resume.pdf")
    if candidate.parent.is_symlink() or candidate.is_symlink():
        raise ValueError("Symlinked job folders/PDFs are forbidden")
    resolved = candidate.resolve(strict=True)
    if resolved != candidate or not resolved.is_file():
        raise ValueError("PDF must be a regular file at the declared job path")
    if resolved.stat().st_nlink != 1:
        raise ValueError("Hard-linked PDFs are forbidden")
    provenance_file = Path(provenance_path)
    if not provenance_file.is_absolute():
        provenance_file = root / provenance_file
    if not provenance_file.resolve(strict=True).is_relative_to(candidate.parent):
        raise ValueError("Provenance must stay inside this job folder")
    provenance = json.loads(provenance_file.read_text())
    guard(root, candidate.parent, provenance)
    if not re.fullmatch(r"[0-9a-f]{64}", expected_sha256):
        raise ValueError("Expected SHA256 must come from the verified QA candidate")
    # Parse and hash the same bytes so the validation receipt identifies the upload.
    data = resolved.read_bytes()
    actual_sha256 = hashlib.sha256(data).hexdigest()
    if actual_sha256 != expected_sha256:
        raise ValueError("Final PDF SHA256 differs from the verified candidate")
    if not data.startswith(b"%PDF-"):
        raise ValueError("File is not a PDF export")
    try:
        from pypdf import PdfReader
    except ImportError:
        raise ValueError("pypdf unavailable; install the repository requirements into the selected Python environment") from None
    try:
        reader = PdfReader(io.BytesIO(data), strict=True)
        if reader.is_encrypted:
            raise ValueError("Encrypted PDFs cannot pass application validation")
        count = len(reader.pages)
    except ValueError:
        raise
    except Exception:
        raise ValueError("PDF cannot be reliably parsed") from None
    if count != MAX_PAGES:
        raise ValueError(f"HARD STOP: page_count={count}; require exactly {MAX_PAGES}")
    qa_path = Path(qa_dir) if qa_dir is not None else None
    if qa_path is not None and not qa_path.is_absolute():
        qa_path = root / qa_path
    qa = verify_qa(candidate.parent, qa_path, provenance, expected_sha256, count)
    return {
        "structural_gate": "PASS", "page_count": count, "max_pages": MAX_PAGES,
        "pdf": str(resolved), "source_base": provenance["sourceBasePath"],
        "sha256": actual_sha256,
        "qa_directory": str(qa), "mechanical_QA_verified": True,
        "visual_review_recorded": True, "agent_review_is_attestation": True,
        "live_ATS_verified": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--pdf", required=True)
    parser.add_argument("--provenance", required=True)
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--qa-dir", required=True, help="This job's checked iteration including review.json")
    parser.add_argument("--receipt-out", help="New JSON receipt under this job's qa/upload directory")
    args = parser.parse_args()
    try:
        result = validate(args.workspace, args.pdf, args.provenance, args.expected_sha256, args.qa_dir)
    except (ValueError, OSError, KeyError, TypeError) as error:
        result = {"structural_gate": "BLOCKED", "reason": str(error)}
    result['checkedAt'] = now()
    if args.receipt_out:
        try:
            write_receipt(args.workspace, args.pdf, args.receipt_out, result, args.provenance)
        except (ValueError, OSError) as error:
            print(json.dumps({**result, "structural_gate": "BLOCKED", "receipt_error": str(error)}))
            return 1
    print(json.dumps(result))
    return 0 if result['structural_gate'] == 'PASS' else 1


if __name__ == "__main__":
    sys.exit(main())
