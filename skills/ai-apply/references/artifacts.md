# Job artifacts and log schema

All data/output paths are relative to the repository root. Every job-specific file belongs under `workflows/<company-slug>/<role-slug>-<job-id>/`. Only create a real job folder once company, role and stable identity are resolved. `job.json` is the durable job identity/state/source manifest; JD/analysis/application evidence holds the detailed job facts and outcome. Only shared index/coordination bookkeeping lives outside the job directory. Escape `|` and newlines in Markdown table cells. Preserve unrelated rows/artifacts. Never store passwords, OTPs, government identifiers, customer data, signed/private URLs or raw source discussions.

The only resume format is PDF. `source/frontend-base.pdf` is an unchanged source copy, `resume.pdf` is the directly edited working copy, `expected.txt` is independently prepared intended final text, and `<company-slug>-<job-folder>-resume.pdf` is copied from the checked QA candidate. A company prefix is required in the final filename even though the job is already inside the company directory.

## JD.md

```markdown
# Job Description

## Metadata
Company:
Role:
Job ID:
URL:
Source:
Posted:
Captured: (Asia/Kolkata)
Location:
Work Mode:
Employment Type:
Experience:
Domain:
Application Route:
Compensation: (when visible; otherwise Not disclosed)
Capture Complete: Yes / No (reason)

## Responsibilities

## Required Qualifications

## Preferred Qualifications

## Technologies / Keywords

## Original Job Description
(Complete relevant original text, not just an extract or generated summary.)
```

## analysis.md

```markdown
# Resume / Job Analysis

## Job Summary

## Suitability
Decision: PROCEED / BLOCKED / SKIPPED
Application Status: IN_PROGRESS / TAILORED / APPLIED / BLOCKED / SKIPPED / DUPLICATE
Reason:

## Selected Resume Template
Local Frontend BASE (or Not selected — early gate)
BASE path / SHA256:
Job source-copy path / SHA256:
Working PDF path / SHA256; independently planned expected text hash:
Supporting Markdown reference paths/current hashes:
Whole-library selection table (BASE/reference path and current hash, JD relevance, used/not-used reason):
Reason:
Local job PDF path: (only after verified copying)

## Initial Resume Review
ATS Score: optional /100 (heuristic, not hiring probability or an acceptance gate)
Detected Level:
Target Market: India
Recruiter Verdict: (simulation)
Supporting review findings; explain any score's limits if one was produced.

## Highlights ✓

## Lowlights ✗

## The 7 Deadly Sins
(All seven; ✓ committed / ✗ clean; do not silently invert the legend.)

## Keywords Missing or Not Demonstrated
| Priority | JD Requirement | Resume Coverage | Context Evidence | Evidence ID | Action |
|---|---|---|---|---|---|
(Include A/B/C/D/E classification, mandatory/preferred distinction and ranked importance.)

## Exact JD Keyword Reconciliation
| Exact JD phrase | Current local BASE PDF literal / supported alias | Evidence class + ID | Final PDF literal / alias | Disposition / omission reason |
|---|---|---|---|---|
(Use the final saved/checked PDF text for the last two columns; explain unsupported terms without adding them.)

## Priority Fixes (Ranked by Impact)

## Bullet Rewrites (Before → After)
(Exact before, truthful proposed after, evidence, JD reason; mark proposals.)

## Context Evidence Used
(Exact IDs/status/attribution and necessary boundaries; public-safe paraphrases only.)

## Gaps We Cannot Truthfully Fill

## Final Recommendation
PROCEED / BLOCKED / SKIPPED
(Recommendation and exact next action, separate from actual submission status.)
```

For early skips or pre-review blockers, keep relevant headings and mark unperformed stages explicitly rather than inventing scores, evidence or rewrites. For a confirmed duplicate, report the existing APPLIED record/folder without recreating artifacts.

After actual tailoring append:

```markdown
# Changes Made
| Section | Before | After | JD Reason | Evidence |
|---|---|---|---|---|

Note distinct verified achievements condensed into another bullet or omitted. For an omission, state why a concise version could not fit and whether the final PDF still shows that workstream through another hands-on example; a skills-only mention is not equivalent.

## Local Export Verification
BASE / source-copy / working PDF paths and hashes:
Source capture and PDF save times; working/iteration PDF identity:
Iteration / provenance / raw export paths:
Final PDF path / SHA256; independent expected-text path / SHA256:
Exactly two PDF pages:
Poppler default/raw/layout; pypdf plain/layout; pdfplumber default; PyMuPDF sorted/unsorted versions and raw differences:
ActualText / ToUnicode / font / link / bullet checks:
Guarded metadata repair, catalog graph and pixel comparison (if needed):
Copied BASE → intended before/after ledger → edited PDF wording / order:
Professional Summary plain paragraph (no list markers or duplicate title):
Three title / RESPONSIVE.IO / date / Coimbatore associations; no internship or false project jobs:
Selected BASE’s projects / centered contact header / right-aligned dates and locations:
Page-by-page PDF visual observations; actual font/glyph coverage and any limitations:
Checked QA directory / candidate-bound review.json (all pages and evidence/JD/protection checks):
Final PDF exact JD phrase / alias ledger:
Protected local BASE/reference/context hash comparisons:
Final upload guard / unchanged upload hash:
Live portal parsing: PASS / FAIL / NOT_TESTED / NOT_OBSERVABLE (observations for this exact file only):
Validated: (Asia/Kolkata)

## Application Result
Status:
Route:
Confirmation type / nonsecret reference / time:
Blocker or uncertainty / exact user action if any:
```

Default folder lifecycle:

```text
workflows/company/role-jobid/
├── job.json                        # aliases, state/history and BASE-copy binding
├── JD.md
├── analysis.md
├── source/
│   ├── frontend-base.pdf            # unchanged BASE copy
│   └── protected-hashes.json
├── resume.pdf                      # directly edited working PDF
├── expected.txt                    # independent intended wording
├── company-role-jobid-resume.pdf    # only after shared verification
├── exports/<iteration>/            # saved PDF, independent expected text and provenance
├── qa/<iteration>/                 # raw checks, renders and evidence
├── qa/upload/<attempt>.json         # pre-upload / pre-submit guard receipts
└── application/                    # nonsecret portal screenshots / confirmation evidence
```

`application.md` is optional inside this same job folder when analysis.md cannot concisely capture the result. Application evidence records company/requisition, route/URL, nonsecret confirmation type/reference/time and uploaded PDF hash; never persist an entire unrelated inbox or secrets. Skipped/pre-tailoring blocked jobs have job metadata plus JD/analysis, without a copied/tailored resume. Post-tailoring blockers retain completed work with failed/pending validation clearly marked; artifacts alone do not imply success.

Upload receipts are newly created by `validate_pdf.py --qa-dir <checked-iteration> --receipt-out <new-receipt>`. They must be JSON files under this exact job's `qa/upload/` and cannot overwrite earlier receipts. The gate requires successful candidate-bound mechanical QA, unchanged raw/intended-text artifacts and a complete `review.json` from actual all-page visual/evidence review. Recorded agent judgment is an attestation; the receipt is not independent proof of appearance, an ATS certificate or submission confirmation.

## workflows/log.md

```markdown
| Updated (Asia/Kolkata) | Company | Role | Job ID | Status | Folder |
|---|---|---|---|---|---|
```

- The shared helper generates this index from company/job `job.json` manifests; do not hand-write an incompatible expanded table. Updated is the helper's Asia/Kolkata timestamp. Folder is `company-slug/job-slug` relative to workflows.
- Store location/work mode, canonical job URL, fit summary, BASE/working/final paths and hashes, reason and confirmation details in the job's JD/analysis/application evidence. The helper's status note preserves a concise outcome in that manifest's history. A match heuristic is never hiring odds; use Not assessed when review was not performed.
- TAILORED: standalone ai-tailor completed verification; no application submitted. ai-apply keeps IN_PROGRESS until its terminal application outcome.
- APPLIED: confirmed submission only; durable duplicate-suppression record.
- BLOCKED: potentially applicable but missing mandatory facts/evidence, access, validation, verification or confirmed submission outcome. State the exact blocker.
- SKIPPED: deliberate preference/role mismatch, with exact reason.
- IN_PROGRESS: active incomplete attempt; not success and not permission to retry submission.
- DUPLICATE: returned because already APPLIED. It is not a `coordination.py status --status` value; leave the original APPLIED manifest/index row intact and report the existing folder. Never downgrade success or recreate the job just to log a duplicate.
- Update the same active attempt as it progresses; retain prior successful/uncertain submission evidence. On resume, recheck reality before another Submit.
- Do not create manifests/index rows for unresolved company/job identity. Capture a complete pasted JD as “Pasted JD — no URL” in the job metadata after identity is resolved; never fabricate a URL.
