# job-skill

AI-powered job search assistant for Indian professionals — built as a Claude Skill.

Searches 12+ Indian and global job platforms (Naukri, LinkedIn, Instahyre, Cutshort, Hirist,
Indeed India, Foundit, Shine, TimesJobs, Glassdoor, WeWorkRemotely, AngelList) plus direct
company career pages, generates ATS-optimized, human-sounding resumes and cover letters
tailored to each job posting, scores keyword match, tracks applications, and can automate
nightly searches with a morning report.

## Personal configuration

This copy uses Sanjeev's confirmed profile and job preferences in `SKILL.md`, with the approved
[BASE PDF](assets/frontend-base.pdf) and [resume reading copy](profile/resume.md).
The original commands, search/scoring, cover letters, bundles, Gmail tracking, nightly pipeline
and weekly reviews are retained. Resume editing is PDF-only, outputs go under
`../workflows/<company>/<job>/`, and tracking uses the existing
[Google Sheet, Assignments tab](https://docs.google.com/spreadsheets/d/105thf_TByGIJF1WuEfDbzA_PNDOrN39iMNNQ6-r5TTw/edit?gid=891834841#gid=891834841).
Execution preferences, schedule activation and broader Codex installation remain TODO.
Resume generation now calls the existing [local ai-tailor skill](../.agents/skills/ai-tailor/SKILL.md).
It owns one job’s evidence review, PDF editing and verification; this skill keeps search, ranking,
cover letters, bundles and tracking. Blocked jobs are reported without stopping the rest of the batch.
The authoritative BASE is `../main-resume/frontend-base.pdf`; the bundled PDF must match its hash.

## Commands

- `/job-skill help` — usage guide
- `/job-skill search` — search all platforms for roles matching your profile
- `/job-skill automate` — set up a nightly automated search with a morning report
- `/job-skill status` — check application status (auto-detects rejections/interviews via Gmail if connected)

Natural language also works — e.g. "Find me React jobs in Bangalore", "Apply to this job: [URL]",
"What's the status of my applications?"

## Key features

- 13-channel search (12+ job boards + direct company career pages)
- Tailored resume + cover letter generated per job, written to sound human (no AI clichés,
  no templated bullet rhythm) rather than obviously AI-generated
- Internal evidence-backed keyword optimization (70% coverage guide, not a completion gate) — never shown as a raw score to the user
- Application tracker (existing Google Sheet) with status flow from Found → Applied → Offer/Rejected
- Gmail-based auto-detection of rejections, interview invites, and assessments
- **Auto-improvement on rejection patterns**: when Gmail shows repeated or same-day rejections,
  the skill diagnoses the likely cause (ATS filter vs. targeting vs. seniority mismatch) and
  automatically tightens keyword matching or search targeting going forward — and always tells
  you what changed and why
- Clean output only: no tool/JS/code-block narration, no "let me check X" pauses — just job
  listings, fitness scores, apply links, and status updates
- Weekly self-correction review of response/interview/ghosted rates

## Installation

This personal integration runs from `/Users/SANJEEV.S/projects/misc`, with this repository at
`claude-job-skill/`. It requires the existing sibling `.agents/skills/ai-tailor/` (including its
scripts and `references/local-export.md`), `contexts/`, and `main-resume/`. Those local dependencies
are maintained in the workspace, not bundled in this repository. ai-tailor uses the installed
PDF, resume-review and tech-resume-optimizer skills. Read its dependency requirements before a run.
Copying this repository alone does not install those dependencies or activate a nightly schedule.

## Privacy

All data stays within the session. Optional Gmail integration only reads emails from companies
you've applied to — nothing else. The skill never submits applications, creates accounts, or
handles CAPTCHAs/OTPs/logins on your behalf; you review the morning report and apply manually.

## License

MIT — use and adapt freely.
