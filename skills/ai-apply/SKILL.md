---
name: ai-apply
description: "Process one supplied job URL or complete JD for Sanjeev: review fit, reuse a verified job PDF or prepare the first copy when absent, apply, and record confirmed results. Recognize /ai-apply and $ai-apply. Use job-skill for integrated discovery and explicit application requests."
---

# One-job local resume application workflow

Invocation: `/ai-apply <job URL or complete JD>` or `$ai-apply <input>`. This is a textual convention, not a registered slash alias. Process one job; do not start discovery, schedules or unrelated outreach. Resolve a selected LinkedIn result to its actual job URL and complete expanded JD, not a card or search page.

Run helper commands from the repository root (`/Users/SANJEEV.S/projects/misc/claude-job-skill`); pass `--workspace /Users/SANJEEV.S/projects/misc`. Candidate source and output paths below are workspace-relative; links are relative to this file’s physical repository location. Follow AGENTS/RTK rules. Read [artifact schemas](references/artifacts.md) before writing. A live request to apply authorizes this workflow through submission and active-job verification/application email when required by that route, subject to actual tool permissions. Honor review-only, tailor-only and dry-run limits. Skill maintenance/testing does not authorize any application, portal interaction, email or remote resume experiment. Dry tests use synthetic inputs in a temporary workspace with no live services or real workflow records.

Use [ai-tailor](../ai-tailor/SKILL.md) as the authoritative local resume-preparation workflow. The only BASE is `main-resume/frontend-base.pdf`; content inputs are the flat reference Markdown and current contexts. Historical remote resumes stay read-only and are not copy sources. `main-resume/`, `contexts/`, source repositories, skills and configs remain protected during normal runs.

## job-skill caller and authentication

Read [explicit application handoff](../../references/apply.md) for prepared-PDF reuse, new ownership/provenance, account creation, login, email OTP/verification, challenge handoff and Sheet ownership. These instructions also govern authentication during direct ai-apply requests. They authorize account creation/login only while carrying out an explicit live application request. Keep passwords and OTPs transient; no credential value belongs in a skill or repository.

When called by job-skill, use the supplied existing job folder and verified PDF. Follow the reuse procedure before considering new preparation; return a confirmed outcome for job-skill to update the Sheet. Do not run discovery or independently update the Sheet.

## Job folder and PDF-only contract

Resolve `COMPANY_SLUG` and `JOB_SLUG` using ai-tailor's stable identity rules. `JOB_SLUG` is the role plus requisition/local identity, without repeating the company. Set `JOB_FOLDER` to `<company-slug>/<job-slug>`, `JOB_DIR` to the absolute `workflows/<company-slug>/<job-slug>/`, and `FINAL_PDF` to `$JOB_DIR/<company-slug>-<job-slug>-resume.pdf`. For example: `workflows/amazon/front-end-engineer-ii-10575321/amazon-front-end-engineer-ii-10575321-resume.pdf`.

Keep **every job-specific artifact** inside this same `JOB_DIR`: JD, analysis, job manifest, copied BASE, working PDF, independent intended text, edit/evidence ledger, iterations, raw extracts, page renders, upload-check receipts, retained portal screenshots and submission confirmation. Use `application/` for nonsecret portal/confirmation evidence. Do not write job files directly under `workflows/`, the company directory, `output/`, or another job. Only the shared index `workflows/log.md` and shared coordination locks live outside job directories.

The resume flow is **copy BASE PDF → edit `resume.pdf` directly → verify against independently prepared `expected.txt` and all-page visual/evidence checks → upload the unchanged checked final PDF**. Do not create DOCX files, convert through Word, or use a separate resume-authoring flow. Save only the final PDF as the application resume.

## 1. Reuse verified material or prepare a new job

For an existing tailored job, first follow the prepared-resume reuse procedure in the handoff reference. Reacquire its claim, validate the same PDF with new attempt provenance and existing QA, then proceed to upload/form completion. Do not recopy, rewrite or repeat tailoring solely because the job is now being applied to. If a substantive content change is needed, BLOCK and explain it unless the user explicitly authorized re-tailoring.

For a new job with no prepared resume, execute ai-tailor in its **ai-apply caller mode**, within this one owned `JOB_DIR`. Use [skills/ai-tailor/scripts/coordination.py](../ai-tailor/scripts/coordination.py) with `--workspace /Users/SANJEEV.S/projects/misc` and `--folder "$JOB_FOLDER"` for claims, source binding, status/logging and release; run the relevant subcommand's `--help` for its remaining arguments. Reuse caller-owned tokens rather than acquiring a competing claim. APPLIED stops as DUPLICATE unless re-tailoring is explicitly requested; re-tailoring does not authorize a duplicate submission or erase prior application history.

For new preparation, follow ai-tailor's complete JD capture, current preference gate, the bundled initial resume review, exact phrase/evidence ledger, all-reference comparison, relevant context supplements, evidence-backed technical optimization, protected local copy, direct PDF editing and PDF-only verification against independent intended text. Its actual BASE layout governs employer, header and projects. Inspect mandatory application questions and accepted upload formats early where observable; discoverable mandatory unknowns or a portal that refuses PDF block before copying. Scores remain labeled heuristics, never acceptance targets.

Keep one JD/analysis/folder/token and IN_PROGRESS through application. After all evidence, mechanical, protection and all-page visual gates pass, record final PDF path and hashes in analysis and return control here. Do not release the caller's claim or write terminal TAILORED during shared preparation. Reuse prior artifacts only after local BASE lineage, current inputs/hashes, working PDF revision, QA and visual observations are reconciled; reverify unchanged content when needed; do not regenerate a prepared resume without explicit re-tailoring authorization.

## 2. Verified artifacts and final upload guard

For new or explicitly revised material, follow [the direct-PDF verification procedure](../ai-tailor/references/local-export.md), including `verify_job.py` and its ownership/protected-input guards. Retain saved PDF/rejected iterations under `JOB_DIR/exports/` and `JOB_DIR/qa/`. Copy only the checked candidate to `FINAL_PDF`. Record local BASE/copy/working-PDF paths and hashes, independent intended-text hash, input protection, parser modes/versions, metadata/fonts/links, role associations, phrase/evidence dispositions and page-by-page visual observations.

The PDF must be exactly two readable pages. A mechanical pass does not establish visual quality, factual accuracy or live ATS behavior. Failed required checks block upload/submission. Fix the working PDF, save a fresh iteration and repeat the full shared verification after changes. No silent font substitution.

Before uploading the reused verified `FINAL_PDF` (or after copying a newly checked candidate), and again immediately before Submit, run the upload guard with actual values. `QA_ITERATION` is the absolute checked directory produced by `verify_job.py`, with actual mechanical QA, bound provenance and the completed `review.json` specified in the shared procedure. `ITERATION` is that run's raw saved-PDF/provenance directory; for a reused resume, use the new application-attempt provenance directory from the handoff reference instead. The upload gate requires all of this evidence to match the same PDF/intended-text revision. Set `ATTEMPT_ID` to a new stage/attempt name, such as `before-upload-01` or `before-submit-01`; never overwrite earlier receipts:

```sh
rtk proxy "$PDF_PYTHON" skills/ai-apply/scripts/validate_pdf.py \
  --workspace /Users/SANJEEV.S/projects/misc \
  --provenance "$ITERATION/provenance.json" \
  --qa-dir "$QA_ITERATION" \
  --pdf "$FINAL_PDF" --expected-sha256 "$VERIFIED_PDF_SHA256" \
  --receipt-out "$JOB_DIR/qa/upload/$ATTEMPT_ID.json"
```

Use the repository’s prepared Python environment with pypdf. The expected hash must come from the successfully reviewed shared QA candidate, not an unreviewed upload. The guard checks local BASE lineage, current company/job ownership, final path, exact page count, unchanged bytes, successful mechanical QA and current candidate-bound review evidence. The visual/evidence record is an agent attestation, not independent automated certification or a live ATS result. The uploaded artifact must have these exact bytes; unknown identity, missing QA or a stale/incomplete review blocks submission.

## 3. Apply and confirm

For a browser-based application, use this job's dedicated tab. Serialize shared UI access with an atomic directory lock at `workflows/.coordination/browser-shared.lock`; record the existing job token, `JOB_FOLDER` and exact tab ID in its `owner.json`. This is a directory-lock protocol, not a nonexistent coordination-helper subcommand. Reuse only a matching valid caller-owned lock; never steal another owner's lock. Keep it through Submit and confirmation read-back, verifying tab URL, company and requisition before final action. Release only the matching invocation-owned browser lock after confirmation or a safe pause, before releasing the job claim; caller-owned locks remain with the caller. Connector-only actions do not require a browser lock. Retain any necessary nonsecret UI evidence under `JOB_DIR/application/`.

Continue through LinkedIn Easy Apply, external employer portals reached from LinkedIn, and employer careers sites; an external redirect is not itself a blocker. Use the validated PDF from this job folder. If the portal refuses PDF and requires another format, record that exact requirement as BLOCKED; do not silently introduce a conversion or claim an upload succeeded. Resolve required questions from `contexts/personal.md`; current defaults are:

| Field | Answer |
|---|---|
| Current CTC | UNKNOWN; resolve only when required |
| Expected CTC | Exact target UNKNOWN; minimum ₹15 LPA is not an exact expected-CTC answer |
| Notice | 30 days |
| Citizenship / authorization | India / authorized in India |
| Sponsorship in India | No |
| Relocation | Any city in India; no international relocation |
| Remote | India-wide, or international remote explicitly allowing work from India |

Convert units correctly (LPA vs rupees, annual vs monthly); never invent a compensation breakdown, exact legal identity, dates/GPA or sensitive legal/self-identification answer. Optional fields can be left unanswered or use an offered “prefer not to say” only when truthful/permitted. Mandatory unknowns mean BLOCKED with the exact field/action needed; do not guess.

Use connected Gmail **only for this active job**: portal verification, application/recruiter email required by the active route, OTP or submission confirmation. Narrow searches to this portal/company and relevant time window. Retrieve OTP transiently, use it, and **never write it or passwords to disk, context, log, artifacts or summaries**. Do not dump unrelated email. No unsolicited recruiter outreach or follow-up scheduling; those require a separate user request. Unavailable required OTP/login is BLOCKED.

Never bypass CAPTCHA, anti-bot verification, identity checks or security challenges. If human intervention is required, BLOCKED; surface the exact portal/action and resume after the user completes it.

After upload, inspect the actual parsed employment fields when the portal exposes them. Require exactly three jobs with the correct title/employer/date/location associations from ai-tailor: all RESPONSIVE.IO and Coimbatore, no internship and no project converted into a job. Do not manually correct parsed fields to make a parser test pass. If parsing fails, BLOCK with the observed mismatch. Revise only with explicit re-tailoring authorization, then save/reverify and re-upload; do not silently rewrite a prepared PDF. If the portal exposes no parsed employment, record NOT_OBSERVABLE, never claim live ATS verification; this alone does not block a portal that only accepts an attachment. An explicitly required live parser test that cannot be observed does block. Ordinary truthful application questions remain separate from a parser test.

Immediately before final Submit, re-read log and verify correct company/job; correct recorded job duplicate; correct **unchanged SHA256** of the actual uploaded artifact (the verified PDF); freshly passed exactly-two-page and SHA256 guard; the completed exact-JD-keyword ledger against that same PDF with unresolved mismatches explicitly reported; correct salary/notice/location/relocation; all answers truthful; visual/link/date checks complete; and protected local resources unchanged. A local checker pass or a semantic alias does not resolve an unsupported requirement. If upload/form/resume changed, repeat affected checks. Submit when these gates pass and the live request authorizes it; obey any actual permission prompt.

**APPLIED only with confirmed success**: success page, LinkedIn submitted state, employer application ID or matching confirmation email. Record nonsecret confirmation type/reference/time, company/requisition and uploaded PDF hash in `JOB_DIR/analysis.md`; retain supporting evidence under `JOB_DIR/application/` (an optional job-local application.md may summarize it). If submit outcome is uncertain, record BLOCKED “submission outcome unconfirmed”; inspect submitted state/email before any retry. Never blindly resubmit or mark APPLIED after an intermediate click.

## 4. Persist result and return

Save detailed application URL, location/work mode, fit, blocker or confirmation and final PDF hash inside the job's JD/analysis/application evidence. Use `skills/ai-tailor/scripts/coordination.py --workspace /Users/SANJEEV.S/projects/misc status --folder "$JOB_FOLDER" --token "$TOKEN" --status <status> --note <nonsecret-outcome-summary>` to update the existing `job.json` history and shared `workflows/log.md` index. The command accepts IN_PROGRESS, APPLIED, BLOCKED, SKIPPED and TAILORED; ai-apply uses TAILORED only for an explicitly tailor-only request that ends before application. DUPLICATE is a returned outcome, not a status argument: preserve the existing APPLIED record and do not acquire a new claim or downgrade it. Keep IN_PROGRESS during ordinary shared preparation.

Preserve completed artifacts and prior outcome evidence on blocks; identify pending/failed validation. Release only invocation-owned UI/job locks. Use the same helper's `finish --folder "$JOB_FOLDER" --token "$TOKEN"` on completion/block; caller-owned ownership remains with its caller. A fresh invocation must re-check actual portal state and the existing job history before retrying submission.

Return company, role, status, local BASE, folder, page count if exported, confirmation if APPLIED, or exact blocker/skip reason. Keep credentials/OTP and proprietary evidence out of the response. Stop after this job; the orchestrator controls further candidates.
