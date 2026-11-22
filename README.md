# Sanjeev's job assistant

Personal configuration and instructions for **SANJEEV S**, based on the supplied Frontend BASE and fresh preferences confirmed on 2026-11-23.

This repo is being prepared first. The original search/materials/tracking/nightly-report/weekly-review capabilities are retained. Workflow defaults, limits, scheduling activation and Codex integration are explicitly **TODO**; nothing is installed or scheduled by this change.

## Personal sources

| File | Purpose |
|---|---|
| [profile.json](profile.json) | Resume-derived identity/career information, notice period and immutable source paths/hash |
| [preferences.json](preferences.json) | Fresh role/experience/location/pay/employment/company preferences and pending workflow decisions |
| [tracker.json](tracker.json) | The designated Google Sheets tracker and its existing column mapping |
| [assets/frontend-base.pdf](assets/frontend-base.pdf) | Byte-identical copy of the supplied resume |
| [profile/resume.md](profile/resume.md) | Complete approved resume text for fast reading |
| [SKILL.md](SKILL.md) | Personal assistant instructions; no generic onboarding or foreign-market templates |

The tracker is the existing [Google Sheet, Assignments tab](https://docs.google.com/spreadsheets/d/105thf_TByGIJF1WuEfDbzA_PNDOrN39iMNNQ6-r5TTw/edit?gid=891834841#gid=891834841). It replaces the old local Excel-tracker requirement. Its metadata/header mapping was read, and no rows or formatting were changed.

The source resume and adjacent workspace skills/contexts remain unchanged. Fresh preferences here govern this repo; old ₹17 LPA, four-city and six-year settings are not imported. Current CTC and offer information remain unspecified.

## Evaluate a normalized job

The evaluator is a standard-library Python filter for supplied listing facts, not a scraper, live application bot or ATS prediction model. It never searches, writes to the Sheet, edits a resume or submits an application.

```bash
rtk proxy python3 scripts/evaluate_job.py /absolute/path/job.json
rtk proxy python3 -m unittest discover -s tests -v
```

Input is one JSON job object or a list of objects. See the test fixtures for field shapes. Output is ELIGIBLE, NEEDS_DETAIL or SKIP with explicit reasons. Unknown salary/experience/India eligibility is preserved as missing detail; known hard exclusions cause SKIP. Exactly 5/5+ is the documented boundary, while the user's priority targets are 1+/2+/3+/4+.

## Retained features

- Multi-platform job discovery, verified links, deduplication and fit/gap assessment.
- A tailored PDF resume plus cover letter for every job selected for materials, with downloadable bundles.
- The designated Google Sheets tracker, Gmail-based status reconciliation and manual updates.
- Automatic nightly searches/materials and a morning report when a schedule is configured.
- Weekly performance review, rejection-pattern analysis and evidence-backed search/material improvements.

The document flow is the change: edit a PDF copy directly and verify it, rather than create DOCX files. The spreadsheet destination is your existing Google Sheet. Personal filters come from your fresh answers. Deferring workflow configuration does not remove the nightly capability.

## Still TODO

The user requested deciding workflow later. Leave default search/tailor/apply mode, run limits, posting recency, scheduling, Gmail status-check policy, material hosting and host integration unset until then. Application materials always include a cover letter when a material-generation mode is eventually chosen. No DOCX resume flow or score-chasing rewrite loop is included.

Before integration, align the installed ai-tailor/ai-apply/orchestrator with these fresh settings and the designated Google Sheet. Do not activate their older preferences as a fallback.

License: MIT, retained from the original project.
