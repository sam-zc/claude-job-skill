#!/usr/bin/env python3
"""Guard and check a directly edited PDF for one owned company/job folder."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
from coordination import BASE, SELECTED_BASE_SHA256, owned, sha


def inside(path, parent):
    path = Path(path)
    resolved = path.resolve()
    if not resolved.is_relative_to(parent) or resolved == parent or resolved != path.absolute():
        raise ValueError('All exports, evidence and output must stay inside the job without symlinks')
    return resolved


def guard(workspace, job_dir, provenance):
    workspace, job_dir = Path(workspace).resolve(), Path(job_dir).absolute()
    try:
        folder = job_dir.relative_to(workspace / 'workflows').as_posix()
    except ValueError:
        raise ValueError('Job must be under workflows/company/job') from None
    job, data = owned(workspace, folder, provenance.get('ownershipToken'))
    base = workspace / BASE
    copy = job / 'source/frontend-base.pdf'
    expected = {'sourceBasePath': str(base), 'sourceBaseSha256': sha(base),
                'sourceCopyPath': str(copy), 'sourceCopySha256': sha(copy)}
    if base.resolve() != base or sha(base) != SELECTED_BASE_SHA256:
        raise ValueError('Selected local BASE changed; reconcile an authorized refresh')
    if any(provenance.get(k) != v for k, v in expected.items()):
        raise ValueError('Provenance must identify the selected local BASE and identical job copy')
    if sha(copy) != sha(base) or data.get('sourceBasePath') != BASE or data.get('sourceCopyPath') != 'source/frontend-base.pdf':
        raise ValueError('Wrong BASE lineage or unbound job source')
    if data.get('sourceBaseSha256') != sha(base) or data.get('sourceCopySha256') != sha(copy):
        raise ValueError('Bound source hash changed')
    inside(copy, job)
    if not provenance.get('capturedAt') or not provenance.get('generatedAt'):
        raise ValueError('Capture and generation times are required')
    working = inside(provenance.get('workingPdfPath', ''), job)
    if working != job / 'resume.pdf' or sha(working) != provenance.get('workingPdfSha256'):
        raise ValueError('Working PDF identity/hash changed')
    expected = job / 'expected.txt'
    inside(expected, job)
    if sha(expected) != provenance.get('expectedTextSha256'):
        raise ValueError('Independently prepared expected text changed')
    snapshot = inside(job / 'source/protected-hashes.json', job)
    protected = json.loads(snapshot.read_text())
    if protected.get(BASE) != sha(base):
        raise ValueError('Protected input snapshot must include the selected BASE')
    for relative, digest in protected.items():
        path = workspace / relative
        if not path.resolve().is_relative_to(workspace) or path.resolve() != path or not relative.startswith(('main-resume/', 'contexts/')):
            raise ValueError('Invalid protected input path')
        if sha(path) != digest:
            raise ValueError('Protected input changed: ' + relative)
    return job


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--workspace', type=Path, required=True)
    p.add_argument('--job-dir', type=Path, required=True)
    for name in ('provenance', 'expected-text', 'pdf', 'out'):
        p.add_argument('--' + name, type=Path, required=True)
    a = p.parse_args()
    job = a.job_dir.absolute()
    # Reject unsafe paths before reading provenance or creating any output.
    for path in (a.pdf, a.out, a.provenance, a.expected_text):
        inside(path, job)
    provenance = json.loads(a.provenance.read_text())
    job = guard(a.workspace, a.job_dir, provenance)
    if sha(a.pdf) != provenance['workingPdfSha256']:
        raise ValueError('Iteration PDF differs from the saved working PDF')
    if sha(a.expected_text) != provenance['expectedTextSha256']:
        raise ValueError('Iteration expected text differs from the independent edit plan')
    result = subprocess.run(['rtk', 'proxy', sys.executable,
        str(Path(__file__).with_name('run_export_check.py')),
        str(a.pdf), str(a.expected_text), str(a.out), '--base-pdf', str(a.workspace.resolve() / BASE)], check=False)
    if result.returncode:
        raise SystemExit(result.returncode)
    guard(a.workspace, a.job_dir, provenance)
    if sha(a.pdf) != provenance['workingPdfSha256'] or sha(a.expected_text) != provenance['expectedTextSha256']:
        raise ValueError('Iteration PDF or intended text changed during verification')
    import verify_export as v
    v.save_json(a.out / 'provenance.json', {
        **{k: value for k, value in provenance.items() if k != 'ownershipToken'},
        'workingPdfMatchesIteration': True,
        'liveATS': 'NOT_TESTED', 'visualReview': 'REQUIRED_FROM_AGENT',
    })



if __name__ == '__main__':
    main()
