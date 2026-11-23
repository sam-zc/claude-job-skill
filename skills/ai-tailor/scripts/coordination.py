#!/usr/bin/env python3
"""Own local company/job folders, bind the BASE copy, and update the workflow log.

No remote services. Bookkeeping is created only by claim, never by --help.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import secrets
import shutil
from zoneinfo import ZoneInfo

BASE = 'main-resume/frontend-base.pdf'
SELECTED_BASE_SHA256 = 'baf4ed23b5878de7c5ae208387d60828962b606c09aaa467d2ebb28235f9cc93'
STATUSES = ('IN_PROGRESS', 'TAILORED', 'APPLIED', 'BLOCKED', 'SKIPPED')


def now():
    return datetime.now(ZoneInfo('Asia/Kolkata')).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, data):
    path = Path(path)
    temp = path.with_name(path.name + '.' + secrets.token_hex(8) + '.tmp')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    temp.replace(path)


def job_path(workspace, folder):
    workspace = Path(workspace).resolve()
    parts = Path(folder).parts
    if len(parts) != 2 or any(not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', x) for x in parts):
        raise ValueError('Folder must be company-slug/role-job-slug')
    job = workspace / 'workflows' / folder
    if job.resolve() != job:
        raise ValueError('Symlinked workflow paths are not permitted')
    return job


@contextmanager
def serial(workspace):
    state = Path(workspace).resolve() / 'workflows/.coordination'
    if state.resolve() != state:
        raise ValueError('Symlinked coordination path')
    state.mkdir(parents=True, exist_ok=True)
    lock = state / 'write.lock'
    try:
        lock.mkdir()
    except FileExistsError:
        raise ValueError('Workflow bookkeeping is busy; inspect before retrying') from None
    try:
        yield
    finally:
        lock.rmdir()


def owned(workspace, folder, token):
    job = job_path(workspace, folder)
    owner = job / '.lock/owner.json'
    if not token or not owner.is_file() or json.loads(owner.read_text()).get('token') != token:
        raise ValueError('Job is not owned by this token')
    data = json.loads((job / 'job.json').read_text())
    if data.get('folder') != folder:
        raise ValueError('Job identity does not match its folder')
    return job, data


def claim(workspace, folder, aliases, task, company, role, job_id, retailor_applied=False):
    job = job_path(workspace, folder)
    aliases = sorted(set(x.strip() for x in aliases if x.strip()))
    if not aliases:
        raise ValueError('At least one verified job alias is required')
    requisition = str(job_id).strip().casefold()
    if not requisition:
        raise ValueError('A stable job identity is required')
    with serial(workspace):
        for path in (Path(workspace).resolve() / 'workflows').glob('*/*/job.json'):
            existing = json.loads(path.read_text())
            if set(aliases) & set(existing.get('aliases', [])) and path.parent != job:
                raise ValueError(f'Existing alias belongs to {existing["folder"]}; reconcile that job')
            if (path.parent != job and path.parent.parent.name == job.parent.name
                    and str(existing.get('jobId', '')).strip().casefold() == requisition):
                raise ValueError(f'Existing company/requisition belongs to {existing["folder"]}; reconcile that job')
        previous = json.loads((job / 'job.json').read_text()) if (job / 'job.json').exists() else None
        if previous:
            if str(previous.get('jobId', '')).strip().casefold() != requisition:
                raise ValueError('Existing folder has a different job identity; reconcile before reuse')
            if not set(aliases) & set(previous.get('aliases', [])):
                raise ValueError('Slug collision: existing job has different aliases')
            if previous.get('status') == 'APPLIED' and not retailor_applied:
                raise ValueError('APPLIED duplicate; preserve history (explicit re-tailor requires --retailor-applied)')
        job.mkdir(parents=True, exist_ok=True)
        lock = job / '.lock'
        try:
            lock.mkdir()
        except FileExistsError:
            raise ValueError('Job already has an active owner; reuse its valid token or reconcile it') from None
        token = secrets.token_hex(24)
        save(lock / 'owner.json', dict(token=token, task=task, claimedAt=now()))
        data = previous or dict(folder=folder, company=company, role=role, jobId=job_id,
                                createdAt=now(), history=[])
        data['aliases'] = sorted(set(data.get('aliases', [])) | set(aliases))
        # An authorized re-tailor never erases the application state/history.
        if data.get('status') != 'APPLIED':
            data['status'] = 'IN_PROGRESS'
        data['updatedAt'] = now()
        save(job / 'job.json', data)
        log = Path(workspace).resolve() / 'workflows/log.md'
        if not log.exists():
            log.write_text('# Job workflow log\n\nLocal records start with this workflow. Missing earlier records do not establish application history.\n\n')
        return dict(token=token, folder=folder, jobDir=str(job), status=data['status'])


def bind(workspace, folder, token, source_copy):
    with serial(workspace):
        job, data = owned(workspace, folder, token)
        source = Path(workspace).resolve() / BASE
        copy = Path(source_copy).resolve()
        if copy != job / 'source/frontend-base.pdf':
            raise ValueError('Source copy must be this job/source/frontend-base.pdf')
        if source.resolve() != source or sha(source) != SELECTED_BASE_SHA256:
            raise ValueError('Selected local BASE changed; reconcile an authorized refresh')
        if sha(copy) != sha(source):
            raise ValueError('Source copy differs from the selected BASE')
        data.update(sourceBasePath=BASE, sourceBaseSha256=sha(source),
                    sourceCopyPath='source/frontend-base.pdf', sourceCopySha256=sha(copy), updatedAt=now())
        save(job / 'job.json', data)
        return data


def update(workspace, folder, token, status, note):
    if status not in STATUSES:
        raise ValueError('Unsupported job status')
    with serial(workspace):
        job, data = owned(workspace, folder, token)
        record = dict(status=status, at=now(), note=note)
        data.setdefault('history', []).append(record)
        if data.get('status') == 'APPLIED' and status != 'APPLIED':
            data['tailoringStatus'] = status
        else:
            data['status'] = status
        data['updatedAt'] = record['at']
        save(job / 'job.json', data)
        # Rebuild the index under the global write lock; manifests retain full histories.
        def cell(value):
            return str(value).replace('|', '\\|').replace('\n', ' ')
        rows = ['# Job workflow log', '',
                'Local index; prior deleted records are not proof of no application. See each job.json for history.', '',
                '| Updated (Asia/Kolkata) | Company | Role | Job ID | Status | Folder |',
                '|---|---|---|---|---|---|']
        for path in sorted((Path(workspace).resolve() / 'workflows').glob('*/*/job.json')):
            item = json.loads(path.read_text())
            values = [item.get(k, '') for k in ('updatedAt', 'company', 'role', 'jobId', 'status', 'folder')]
            rows.append('| ' + ' | '.join(map(cell, values)) + ' |')
        log = Path(workspace).resolve() / 'workflows/log.md'
        temp = log.with_name('log.' + secrets.token_hex(8) + '.tmp')
        temp.write_text('\n'.join(rows) + '\n')
        temp.replace(log)
        return data


def finish(workspace, folder, token):
    with serial(workspace):
        job, _ = owned(workspace, folder, token)
        shutil.rmtree(job / '.lock')
        return dict(folder=folder, released=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--workspace', type=Path, required=True)
    sub = p.add_subparsers(dest='command', required=True)
    c = sub.add_parser('claim')
    c.add_argument('--folder', required=True, help='company-slug/role-job-slug')
    c.add_argument('--alias', action='append', required=True)
    c.add_argument('--task', required=True)
    c.add_argument('--company', required=True)
    c.add_argument('--role', required=True)
    c.add_argument('--job-id', required=True)
    c.add_argument('--retailor-applied', action='store_true', help='Only after explicit user instruction')
    for name in ('bind-source', 'status', 'finish'):
        c = sub.add_parser(name)
        c.add_argument('--folder', required=True)
        c.add_argument('--token', required=True)
        if name == 'bind-source':
            c.add_argument('--source-copy', type=Path, required=True)
        elif name == 'status':
            c.add_argument('--status', choices=STATUSES, required=True)
            c.add_argument('--note', default='')
    a = p.parse_args()
    if a.command == 'claim':
        result = claim(a.workspace, a.folder, a.alias, a.task, a.company, a.role, a.job_id, a.retailor_applied)
    elif a.command == 'bind-source':
        result = bind(a.workspace, a.folder, a.token, a.source_copy)
    elif a.command == 'status':
        result = update(a.workspace, a.folder, a.token, a.status, a.note)
    else:
        result = finish(a.workspace, a.folder, a.token)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
