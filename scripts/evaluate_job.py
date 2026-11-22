#!/usr/bin/env python3
"""Evaluate supplied job facts against Sanjeev's confirmed personal preferences.

No network, spreadsheet writes, resume mutations, scheduling or applications.
"""
import argparse
import json
import math
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


def normalized(value):
    return re.sub(r'[^a-z0-9]+', '_', value.strip().casefold()).strip('_') if isinstance(value, str) else ''


def number(value):
    return value if type(value) in (int, float) and math.isfinite(value) and value >= 0 else None


def company_key(value):
    if not isinstance(value, str):
        return ''
    value = value.strip().casefold().strip(' .,\t\n')
    value = re.sub(r'(?:[\s,.]+(?:incorporated|inc|limited|ltd|llc|private|pvt))+$', '', value).strip()
    return re.sub(r'[^a-z0-9]', '', value)


def domain_key(value):
    if not isinstance(value, str) or not value.strip():
        return ''
    parsed = urlparse(value.strip() if '://' in value else 'https://' + value.strip())
    return (parsed.hostname or '').casefold().removeprefix('www.')


def evaluate_job(job):
    """Return personal-filter eligibility; missing facts are not invented."""
    if not isinstance(job, dict):
        raise ValueError('Each job must be a JSON object')
    preferences = json.loads((ROOT / 'preferences.json').read_text())
    skipped, missing = [], []

    company = company_key(job.get('company'))
    domain = domain_key(job.get('employer_domain'))
    excluded = {company_key(name) for name in preferences['companies']['excluded_names']}
    excluded_domains = preferences['companies']['excluded_domains']
    if company in excluded or any(domain == name or domain.endswith('.' + name) for name in excluded_domains):
        skipped.append('Target employer is Responsive.io/RFPIO, which is excluded.')
    elif not company and not domain:
        missing.append('Verify the target employer.')

    family = normalized(job.get('role_family'))
    if not family or family == 'unknown':
        missing.append('Verify role scope from the full JD.')
    elif family not in preferences['roles']['allowed_families']:
        skipped.append('Role is outside frontend-focused engineering scope.')
    elif family != 'frontend':
        focus = job.get('frontend_focus')
        if focus is False:
            skipped.append('Full-stack/generic engineering role is not frontend-focused.')
        elif focus is not True:
            missing.append('Verify frontend focus; the title alone is insufficient.')

    experience = job.get('required_experience')
    experience = experience if isinstance(experience, dict) else {}
    minimum = number(experience.get('minimum'))
    maximum = number(experience.get('maximum'))
    cap = preferences['roles']['maximum_stated_required_years']
    if minimum is not None and maximum is not None and maximum < minimum:
        missing.append('Experience range is contradictory; verify the JD.')
    elif (minimum is not None and minimum > cap) or (maximum is not None and maximum > cap):
        skipped.append(f'Stated required experience exceeds {cap} years.')
    elif minimum is None:
        missing.append('Verify the stated minimum experience requirement.')

    location = job.get('location')
    location = location if isinstance(location, dict) else {}
    mode = normalized(location.get('mode'))
    mode = 'onsite' if mode == 'on_site' else mode
    country = normalized(location.get('country'))
    india = country in ('india', 'in', 'ind')
    if mode == 'remote':
        eligibility = location.get('can_work_from_india')
        if eligibility is False:
            skipped.append('Remote job excludes working from India.')
        elif eligibility is not True and not india:
            missing.append('Verify that the remote job permits working from India.')
    elif mode in ('hybrid', 'onsite'):
        if not country or country == 'unknown':
            missing.append('Verify the country for onsite/hybrid work.')
        elif not india:
            skipped.append('Outside-India work is allowed only when remote from India.')
    else:
        missing.append('Verify whether work is remote, hybrid or onsite.')

    employment = normalized(job.get('employment_type'))
    if employment in ('contract', 'full_time_contract', 'fixed_term', 'internship', 'intern', 'part_time', 'freelance', 'temporary'):
        skipped.append('Only non-contract full-time employment is allowed.')
    elif employment not in ('full_time', 'permanent_full_time'):
        missing.append('Verify full-time employment type.')
    elif job.get('is_contract') is True:
        skipped.append('Full-time contract work is still excluded.')
    elif employment != 'permanent_full_time' and job.get('is_contract') is not False:
        missing.append('Verify that this full-time opening is not a contract.')

    salary = job.get('salary')
    salary = salary if isinstance(salary, dict) else {}
    currency = normalized(salary.get('currency'))
    conversion = salary.get('conversion')
    conversion = conversion if isinstance(conversion, dict) else {}
    if not currency:
        missing.append('Salary is undisclosed or its currency is unknown.')
    elif currency != 'inr' and not (str(conversion.get('source_url', '')).startswith('https://')
                                    and re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(conversion.get('rate_date', '')))):
        missing.append('Foreign pay requires verified, dated INR normalization.')
    else:
        low = number(salary.get('minimum_annual_inr'))
        high = number(salary.get('maximum_annual_inr'))
        floor = preferences['compensation']['minimum_annual_ctc']
        if low is not None and high is not None and high < low:
            missing.append('Salary range is contradictory; verify the listing.')
        elif high is not None and high < floor:
            skipped.append('Advertised annual compensation is entirely below ₹15 LPA.')
        elif low is not None and low >= floor:
            pass
        else:
            missing.append('Confirm an offer at or above ₹15 LPA; salary is unknown or crosses the floor.')

    decision = 'SKIP' if skipped else 'NEEDS_DETAIL' if missing else 'ELIGIBLE'
    return {
        'company': job.get('company'), 'title': job.get('title'), 'decision': decision,
        'exclusion_reasons': skipped, 'missing_details': missing,
        'scope': 'Personal filters only; complete-JD evidence review still required.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('job_json', type=Path, help='One normalized job object or a list of jobs')
    args = parser.parse_args()
    jobs = json.loads(args.job_json.read_text())
    result = [evaluate_job(job) for job in jobs] if isinstance(jobs, list) else evaluate_job(jobs)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
