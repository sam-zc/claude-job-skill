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
Resume generation now calls the bundled [ai-tailor skill](skills/ai-tailor/SKILL.md).
It owns one job’s evidence review, PDF editing and verification; this skill keeps search, ranking,
cover letters, bundles and tracking. Blocked jobs are reported without stopping the rest of the batch.
Explicit application requests use [the ai-apply handoff](references/apply.md), including prepared-PDF reuse,
account/login/email verification and confirmed tracking. Search and nightly runs remain preparation-only.
The authoritative BASE is `../main-resume/frontend-base.pdf`; the bundled PDF must match its hash.

## Commands

- `/job-skill help` — usage guide
- `/job-skill search` — search all platforms for roles matching your profile
- `/job-skill apply <job URL or selected result>` — apply on request using the current verified PDF through bundled ai-apply
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

Both skills, their review/PDF procedures, helper scripts, upload guards and tests are versioned here:

```text
SKILL.md
references/apply.md
skills/
  ai-tailor/SKILL.md, references/, scripts/
  ai-apply/SKILL.md, references/, scripts/
assets/frontend-base.pdf
```

No separately installed PDF, resume-review, tech-resume-optimizer, ai-tailor or ai-apply skill is
required. Run commands from this repository root. Browser/search/email/Sheets access is supplied
by the running agent's tools; no account credentials are bundled.

The data workspace remains `/Users/SANJEEV.S/projects/misc`: its `main-resume/` and `contexts/`
are private source inputs, and `workflows/` contains job outputs. Pass that location as `--workspace`.
These data folders are not skills and are not copied into Git. The BASE in `main-resume/` remains
authoritative; `assets/frontend-base.pdf` is its checked reference copy and the test fixture.
Tests run from the repository without those external data folders, using temporary workspaces.

For this checkout, the former `.agents/skills/ai-tailor` and `.agents/skills/ai-apply` directories
are discovery symlinks pointing into `skills/`. They contain no independent copies. When cloning
elsewhere, register these skill directories with the host if direct skill discovery is desired;
job-skill itself reads them through repository-relative links.

Use Python 3.10+ and install Poppler with the platform package manager (`brew install poppler`
on macOS). Prepare an isolated Python environment and run the checks:

```sh
rtk proxy python3 -m venv .venv
rtk proxy .venv/bin/python -m pip install -r skills/ai-tailor/scripts/requirements.txt
rtk proxy .venv/bin/python -m unittest discover -s skills/ai-tailor/scripts -p 'test_*.py'
rtk proxy .venv/bin/python -m unittest discover -s skills/ai-apply/scripts -p 'test_*.py'
```

For actual runs, set `PDF_PYTHON` to the absolute path of the prepared Python executable and use
the helper commands in each skill. Poppler and the pinned Python packages are runtime dependencies,
not skill dependencies. No schedule or application is started by installation or testing.

## Privacy

Job artifacts are local; tracking uses the configured Google Sheet. Gmail status checks are scoped
to tracked companies, and explicit applications may read active-portal verification messages.
Apply requests can create required accounts and use transient credentials/email OTPs. Passwords,
OTPs and signed verification links are never saved in skills, artifacts or Git. Human security
challenges require the user's completion. No applications are submitted during ordinary searches.

## License

MIT — use and adapt freely.
