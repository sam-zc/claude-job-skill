# Explicit application handoff

Use this procedure only when the user asks to apply to identified jobs. Search, status, help, schedule setup and ordinary nightly runs do not authorize submission or account creation. Skill maintenance is not a live application request.

## Responsibilities and input

`job-skill` calls the bundled [ai-apply](../../ai-apply/SKILL.md). Execute in the same agent, one job at a time. Pass company, role, requisition, canonical URL/aliases, complete captured JD, exact existing job folder, verified final PDF path/hash, intended text, analysis and QA/provenance locations, and any existing cover letter. Include the requested application scope; do not select additional jobs implicitly. Missing bundled skill/helpers block application, not trigger an improvised submission flow.

ai-apply owns the application claim, portal session, upload checks, submission, confirmation and local job state. job-skill owns Sheet updates and the batch report. All job artifacts stay in the existing `workflows/<company>/<job>/` folder. Never put credentials, OTPs, session tokens or signed verification links in artifacts, Sheet cells, logs, command arguments or commits.

## Reuse the prepared resume

1. Resolve job identity against the supplied JD/URL, manifest and previous application evidence. Confirm the current posting still describes this job and the user's current preferences still fit. An APPLIED record or confirmed portal submission returns DUPLICATE without submitting again. An uncertain prior submit must be reconciled before any retry.
2. Reacquire the existing folder through ai-tailor's coordination helper after its standalone claim was released. Never reuse an expired token, steal an active lock, create another folder or recopy the BASE merely to apply. Preserve TAILORED evidence/history while the new attempt is IN_PROGRESS.
3. Verify current BASE/source binding, protected source hashes, intended text, working/final PDF bytes, candidate-bound mechanical QA and recorded page/evidence review. Keep the exact final PDF filename/bytes and existing cover letter when current. Validation is not a request to rewrite the resume.
4. A search-era provenance token has expired. Under the newly acquired claim, save a **new** `application/<attempt>/provenance.json` copied from the original provenance with only the ownership token rebound and nonsecret reuse metadata added (original provenance path, reuse time). Preserve original capture/generation times and every content hash; never overwrite prior provenance or claim fresh visual review. Run the existing `validate_pdf.py` with this new provenance, original QA directory and verified candidate hash. The guard must pass; changing a token never excuses changed sources or missing QA.
5. If current evidence is complete and the guard passes, skip tailoring and proceed directly to application. Recheck upload integrity immediately before upload and Submit, with distinct receipt files. If checks fail, identify the specific stale/missing evidence. Revalidation may inspect the same PDF without rewriting it. Never refresh hashes/attestations solely to conceal drift. For an existing tailored PDF, BLOCK and report when substantive re-tailoring is needed; obtain an explicit re-tailor instruction before changing its content. If the user supplies a genuinely new, unprepared job and asks to apply, the normal ai-tailor caller workflow prepares its first PDF.

## Login, account creation and verification

The user authorizes the following as necessary steps of an explicit application request. This covers normal email/password, email OTP, verification-link and existing-session routes on the intended employer/ATS domain; it is not a guarantee that every portal can be completed.

| Portal state | Action |
|---|---|
| Already signed in | Verify the account is the candidate's and continue. Do not switch another person's account. |
| Existing account, email/password | Use the confirmed application email from contexts/personal.md and the user-supplied password available transiently in the active conversation or an authorized credential source. Do not assume it is correct for every portal. |
| New account required | Create the candidate account using the confirmed email, truthful profile details and the supplied transient password if the portal accepts it. Complete required verification. Optional marketing/alerts remain off unless requested. Account registration is not an application submission. |
| Email already registered | Switch to sign-in for that email; do not create a duplicate account. |
| Password rejected or portal password rules reject it | Do not guess variations or repeatedly retry. Use an offered email OTP/magic-link route when available; otherwise ask for the needed credential or a user-handled login. Do not reset/change an existing password without authorization. |
| Email OTP, verification link or magic link | Request through the current portal, then use connected Gmail scoped to that portal/sender, candidate email and request time. Read the matching newest message and use the code/link transiently on the expected portal. Verify successful authentication; never treat login success as application success. |
| OTP expired or rejected | Recheck the matching message and current challenge. Request at most one fresh code after a failed/expired attempt; stop if rate limited or still unsuccessful. Do not reuse unrelated/older codes or keep resending. |
| OAuth/SSO | Use an already authorized candidate session when available. If consent or another account credential is needed, surface that exact step; do not grant unrelated access. |
| CAPTCHA, anti-bot, identity check, authenticator/SMS/push MFA or recovery challenge | Pause for the user's completion. Do not solve, bypass, outsource or evade the challenge. Resume only after the portal shows it completed. Email access does not authorize bypassing another factor. |
| Required credential/email access unavailable | Save a nonsecret BLOCKED reason and the next action. The password itself is deliberately not stored in this skill, so a future session may need credential input. |

Use a browser/service's credential-entry mechanism; do not place secrets in shell commands or screenshots retained as evidence. Do not reveal passwords or OTPs in responses. Keep only nonsecret account metadata (portal domain, email used, registration/verification outcome) when needed to resume. Preserve application state on interruptions and release owned shared browser/job locks when pausing; reacquire safely and verify the live page/account before resuming.

## Form completion and result

For a job-skill caller, always reuse the existing current cover letter; if absent, execute job-skill’s cover-letter procedure after resume verification and before Submit, in this same job folder and active claim. The same agent performs this caller-owned step without a second worker or claim.

Follow ai-apply's upload guard, PDF-only rule and truthful-answer requirements. Resolve required unknowns only when encountered. Do not invent salary, authorization or personal answers. Ordinary application fields may be filled from confirmed facts; never claim corrected fields prove automatic PDF parsing. If required parser validation fails or PDF is refused, record the exact blocker.

Submit only within the user's requested job scope. APPLIED requires a success page, employer application ID, submitted state or matching confirmation email. Return outcome, company/requisition, folder, final PDF hash, confirmation type/reference/time or exact blocker, and a nonsecret evidence path. Never retry an uncertain submission without checking prior state.

job-skill rereads the relevant Google Sheet rows and validation, matches company/requisition or canonical URL, and updates only that job's row with the confirmed outcome and verified artifact links. Preserve existing Applied records on duplicates. If tracking fails after submission, retain local APPLIED evidence and report “applied; tracker update pending”; retry the Sheet update only, never the application. Honor the existing sheet's allowed status values and keep detailed blockers in the job folder/report when no matching cell exists.

On confirmed agent submission, set Status = Applied, Applied By = `🤖 Agent`, Applied On = the actual confirmation date, Last Update = actual verification date, and fill the nonsecret Confirmation / Application ID plus exact Workflow Folder. Use the existing cover-letter/resume artifact paths in their columns. On a pre-submit block, set Blocked and explain the exact next step; leave submission-only fields blank. Later employer outcomes may change Status, but preserve who/when/confirmation of the submission. Follow-up dates never authorize outreach. Read the current A:S schema and full tracker rules in job-skill before writing; never restore the former Auto Applied/Done labels.
