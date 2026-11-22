import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from evaluate_job import evaluate_job


class EligibilityTests(unittest.TestCase):
    def setUp(self):
        self.job = {
            'company': 'Example Product Company', 'title': 'Frontend Engineer',
            'role_family': 'frontend', 'required_experience': {'minimum': 1, 'maximum': 5},
            'location': {'country': 'India', 'mode': 'hybrid', 'city': 'Pune'},
            'employment_type': 'full_time', 'is_contract': False,
            'salary': {'currency': 'INR', 'minimum_annual_inr': 1500000, 'maximum_annual_inr': 2000000},
        }

    def test_matching_role_in_any_indian_city(self):
        self.assertEqual(evaluate_job(self.job)['decision'], 'ELIGIBLE')

    def test_one_through_five_year_minimums(self):
        for years in (1, 2, 3, 4, 5):
            self.job['required_experience'] = {'minimum': years}
            self.assertEqual(evaluate_job(self.job)['decision'], 'ELIGIBLE')

    def test_one_plus_role_is_eligible_for_three_year_candidate(self):
        self.job['required_experience'] = {'minimum': 1, 'maximum': None}
        result = evaluate_job(self.job)
        self.assertEqual(result['decision'], 'ELIGIBLE')
        self.assertFalse(result['exclusion_reasons'])

    def test_above_five_minimum_or_range_maximum_excluded(self):
        for requirement in ({'minimum': 6}, {'minimum': 2, 'maximum': 7}):
            self.job['required_experience'] = requirement
            self.assertEqual(evaluate_job(self.job)['decision'], 'SKIP')

    def test_unknown_experience_is_missing_detail(self):
        self.job.pop('required_experience')
        self.assertEqual(evaluate_job(self.job)['decision'], 'NEEDS_DETAIL')

    def test_frontend_focused_full_stack_only(self):
        self.job['role_family'] = 'full_stack'
        self.job['frontend_focus'] = True
        self.assertEqual(evaluate_job(self.job)['decision'], 'ELIGIBLE')
        self.job['frontend_focus'] = False
        self.assertEqual(evaluate_job(self.job)['decision'], 'SKIP')
        self.job['frontend_focus'] = None
        self.assertEqual(evaluate_job(self.job)['decision'], 'NEEDS_DETAIL')

    def test_backend_excluded(self):
        self.job['role_family'] = 'backend'
        self.assertEqual(evaluate_job(self.job)['decision'], 'SKIP')

    def test_international_remote_requires_india_permission(self):
        self.job['location'] = {'country': 'United States', 'mode': 'remote', 'can_work_from_india': True}
        self.assertEqual(evaluate_job(self.job)['decision'], 'ELIGIBLE')
        self.job['location']['can_work_from_india'] = False
        self.assertEqual(evaluate_job(self.job)['decision'], 'SKIP')
        self.job['location']['can_work_from_india'] = None
        self.assertEqual(evaluate_job(self.job)['decision'], 'NEEDS_DETAIL')

    def test_remote_role_explicitly_located_in_india_is_allowed(self):
        self.job['location'] = {'country': 'India', 'mode': 'remote'}
        self.assertEqual(evaluate_job(self.job)['decision'], 'ELIGIBLE')

    def test_foreign_hybrid_or_onsite_excluded(self):
        for mode in ('onsite', 'hybrid'):
            self.job['location'] = {'country': 'Germany', 'mode': mode}
            self.assertEqual(evaluate_job(self.job)['decision'], 'SKIP')

    def test_contracts_and_internships_excluded(self):
        for employment in ('contract', 'internship', 'part_time', 'fixed_term', 'full_time_contract'):
            self.job['employment_type'] = employment
            self.assertEqual(evaluate_job(self.job)['decision'], 'SKIP')
        self.job['employment_type'] = 'full_time'
        self.job['is_contract'] = True
        self.assertEqual(evaluate_job(self.job)['decision'], 'SKIP')

    def test_shifts_bonds_and_service_companies_are_allowed(self):
        self.job.update(company='Example Services', night_shift=True, bond_required=True)
        self.assertEqual(evaluate_job(self.job)['decision'], 'ELIGIBLE')

    def test_responsive_aliases_and_domain_are_excluded(self):
        for employer in ('Responsive.io', 'RESPONSIVE', 'RFPIO Inc.'):
            self.job['company'] = employer
            self.assertEqual(evaluate_job(self.job)['decision'], 'SKIP')
        self.job.update(company='Unclear employer', employer_domain='https://careers.responsive.io')
        self.assertEqual(evaluate_job(self.job)['decision'], 'SKIP')

    def test_responsive_design_is_not_an_employer_match(self):
        self.job.update(company='Responsive Design Studio', jd='Build responsive design; candidate worked at RFPIO.')
        self.assertEqual(evaluate_job(self.job)['decision'], 'ELIGIBLE')

    def test_below_floor_salary_excluded(self):
        self.job['salary'].update(minimum_annual_inr=1000000, maximum_annual_inr=1400000)
        self.assertEqual(evaluate_job(self.job)['decision'], 'SKIP')

    def test_undisclosed_or_crossing_salary_needs_detail(self):
        self.job.pop('salary')
        self.assertEqual(evaluate_job(self.job)['decision'], 'NEEDS_DETAIL')
        self.job['salary'] = {'currency': 'INR', 'minimum_annual_inr': 1200000, 'maximum_annual_inr': 2000000}
        self.assertEqual(evaluate_job(self.job)['decision'], 'NEEDS_DETAIL')

    def test_foreign_salary_requires_conversion_evidence(self):
        self.job['salary']['currency'] = 'USD'
        self.assertEqual(evaluate_job(self.job)['decision'], 'NEEDS_DETAIL')
        self.job['salary']['conversion'] = {'source_url': 'https://example.com/verified-test-rate', 'rate_date': '2026-11-23'}
        self.assertEqual(evaluate_job(self.job)['decision'], 'ELIGIBLE')

    def test_contradictory_or_invalid_numbers_are_not_accepted(self):
        for requirement in ({'minimum': 5, 'maximum': 2}, {'minimum': True}, {'minimum': float('nan')}):
            self.job['required_experience'] = requirement
            self.assertEqual(evaluate_job(self.job)['decision'], 'NEEDS_DETAIL')

    def test_confirmed_exclusion_wins_over_unknown_salary(self):
        self.job.update(company='Responsive.io')
        self.job.pop('salary')
        self.assertEqual(evaluate_job(self.job)['decision'], 'SKIP')

    def test_cli_batch_does_not_mutate_supplied_jobs(self):
        jobs = [self.job, {**copy.deepcopy(self.job), 'company': 'Responsive.io'}]
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'jobs.json'
            path.write_text(json.dumps(jobs))
            before = path.read_bytes()
            result = subprocess.run([sys.executable, str(ROOT/'scripts/evaluate_job.py'), str(path)],
                                    capture_output=True, text=True, check=True)
            self.assertEqual([job['decision'] for job in json.loads(result.stdout)], ['ELIGIBLE', 'SKIP'])
            self.assertEqual(path.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
