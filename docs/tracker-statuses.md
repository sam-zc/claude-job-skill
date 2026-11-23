# Tracker status guide

The `Assignments` tab's Status chip shows the latest evidenced application stage. It is separate from the local workflow manifest and from Applied By. Stages can branch or be skipped; not every application receives an acknowledgement or assessment.

| Status | Meaning / when to use |
|---|---|
| Found | A job was discovered and recorded; review and application materials are not complete. |
| Preparing | Capturing/reviewing the JD, checking fit/evidence, tailoring the resume, writing the cover letter or verifying the PDFs. Nothing has been submitted. |
| Ready to apply | The resume and cover letter are complete and verified for this exact job. Submission has not started. A resume alone is insufficient. |
| Applying | An explicitly requested application is actively being completed: sign-in, account verification, forms or upload. Success is not yet confirmed. |
| Applied | Submission is confirmed by a success page, submitted state, employer reference, matching confirmation email or explicit user report. Finding a job, making a PDF or clicking an intermediate button is insufficient. |
| Acknowledged | The employer confirms receipt or that the application is under review. This does not mean shortlisted. |
| Assessment | An assessment/test invitation or stage is confirmed. Record the deadline, progress and result when known in Next Action / Notes. Do not assume passing or failing. |
| Interview | An interview invitation, scheduled interview or interview round is confirmed. Put the round, date and next step in the notes. |
| Offer | An offer is explicitly received for this application. It does not mean the offer was accepted or that employment started; record those details when confirmed. |
| Rejected | An explicit rejection or unsuccessful outcome is confirmed for this exact job. Silence, a low fit score or a closed posting is not rejection evidence. |
| Withdrawn | The candidate's application has actually been withdrawn, confirmed by the portal or the user. Deciding not to apply in the first place is Skipped. |
| Blocked | A pre-submission step cannot proceed: mandatory missing information, unavailable login/OTP, user-handled CAPTCHA, refused PDF, failed QA or uncertain submission outcome. State the exact blocker and next action. Resume when resolved. |
| Skipped | Intentionally not applying because of a confirmed preference mismatch or a decision not to pursue the job. It is not a technical failure and is not an employer rejection. |
| Closed | A not-yet-submitted posting is verified closed/filled/removed. If already submitted, preserve the application stage and note the posting closure unless the employer explicitly confirms an application outcome. |

## Typical flow

Found → Preparing → Ready to apply → Applying → Applied → Acknowledged → Assessment / Interview → Offer or Rejected.

- An employer may move directly from Applied to Interview, Offer or Rejected.
- Preparing or Applying can become Blocked, then resume the last applicable stage. A pre-application preference conflict becomes Skipped; a closed posting becomes Closed.
- After submission, do not downgrade the stage merely because a later check fails. Keep the latest confirmed stage and put the new issue in Next Action / Notes. If submission itself is uncertain, use Blocked and reconcile the portal/email before any retry.
- No response stays at the last confirmed stage with a dated pending note. Elapsed time alone does not justify Rejected, Closed or a repeat submission.

## Applied By and evidence columns

- `👤 Manual`: the user completed the confirmed submission.
- `🤖 Agent`: the agent completed an explicitly authorized, confirmed submission.
- Leave Applied By and Applied On blank until submission is established. Preserve who/when after the status later changes to Interview, Offer, Rejected or Withdrawn.
- Applied On records the actual submission date; Last Update records the actual substantive verification date. Use the workbook's India timezone.
- Confirmation / Application ID holds the nonsecret employer reference/evidence link. Next Action / Notes holds deadlines, exact blockers and pending details. Workflow Folder identifies the existing job folder.
- A Follow-up On date is a reminder, not permission to send a message.

## Local workflow status is different

The local `job.json` uses IN_PROGRESS, TAILORED, APPLIED, BLOCKED and SKIPPED for preparation/submission bookkeeping. Map IN_PROGRESS to Preparing or Applying according to the actual stage. TAILORED becomes Ready to apply only after the cover letter is checked too. APPLIED remains preserved in local history even if the Sheet later records an employer rejection; this prevents duplicate submissions. DUPLICATE is a returned outcome and does not replace an existing successful application.

Always read current live headers and dropdown validation before writing; preserve native chip colors and historical submission evidence. Never store credentials or OTPs in the tracker.
