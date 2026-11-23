# Sanjeev’s job-search skills

AI-powered job search assistant for Indian professionals — built as a Claude Skill.

Searches 12+ Indian and global job platforms (Naukri, LinkedIn, Instahyre, Cutshort, Hirist,
Indeed India, Foundit, Shine, TimesJobs, Glassdoor, WeWorkRemotely, AngelList) plus direct
company career pages, generates ATS-optimized, human-sounding resumes and cover letters
tailored to each job posting, scores keyword match, tracks applications, and can automate
nightly searches with a morning report.

## Personal configuration

This copy uses Sanjeev's confirmed profile and job preferences in [job-skill](skills/job-skill/SKILL.md), with the approved
[BASE PDF](main-resume/frontend-base.pdf) and [resume reading copy](contexts/resume-baseline.md).
The original commands, search/scoring, cover letters, bundles, Gmail tracking, nightly pipeline
and weekly reviews are retained. Resume editing is PDF-only, outputs go under
`workflows/<company>/<job>/`, and tracking uses the existing
[Google Sheet, Assignments tab](https://docs.google.com/spreadsheets/d/105thf_TByGIJF1WuEfDbzA_PNDOrN39iMNNQ6-r5TTw/edit?gid=891834841#gid=891834841).
Execution preferences, schedule activation and broader Codex installation remain TODO.
Resume generation now calls the bundled [ai-tailor skill](skills/ai-tailor/SKILL.md).
It owns one job’s evidence review, PDF editing and verification; this skill keeps search, ranking,
cover letters, bundles and tracking. Blocked jobs are reported without stopping the rest of the batch.
Explicit application requests use [the ai-apply handoff](skills/job-skill/references/apply.md), including prepared-PDF reuse,
account/login/email verification and confirmed tracking. Search and nightly runs remain preparation-only.
The authoritative BASE is `main-resume/frontend-base.pdf`; the reference copy in `assets/` must match its hash. The separately preserved `main-resume/sanjeev-frontend-base.pdf` is not an active BASE.

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
  the skill reviews observed patterns, supported keywords and role fit, without treating rejection
  timing as proof of an ATS filter, and adjusts search emphasis within confirmed preferences — and always tells
  you what changed and why
- Clean output only: no tool/JS/code-block narration, no "let me check X" pauses — just job
  listings, fitness scores, apply links, and status updates
- Weekly self-correction review of response/interview/ghosted rates

## Installation

This is a three-skill repository, with each entry point under `skills/<name>/SKILL.md`:

| Skill | Responsibility |
|---|---|
| [job-skill](skills/job-skill/SKILL.md) | Search, ranking, cover letters, tracking, reports and requested application routing |
| [ai-tailor](skills/ai-tailor/SKILL.md) | Evidence-backed PDF tailoring and verification |
| [ai-apply](skills/ai-apply/SKILL.md) | Reuse the verified PDF, complete a requested application and confirm its outcome |

```text
skills/
  job-skill/SKILL.md, references/apply.md
  ai-tailor/SKILL.md, references/, scripts/
  ai-apply/SKILL.md, references/, scripts/
contexts/                       # confirmed facts, preferences and evidence
main-resume/
  frontend-base.pdf             # authoritative BASE
  references/                   # flat Markdown reference library
assets/frontend-base.pdf        # matching reference/test copy
profile/resume.md               # readable bundled snapshot
.agents/skills/                 # relative discovery links to all three skills
workflows/                      # generated job artifacts; ignored by Git
```

The clone itself is the workspace. Resolve its real directory, run helper commands from there,
and pass `--workspace .`. Skills, contexts, resume sources, references and tests are all included;
no parent data folders or external skill installation is required. Historical external source-repo
paths in evidence records are citations, not runtime dependencies. Tests use temporary workspaces.

The checked-in `.agents/skills/` symlinks point into this repository's `skills/` collection for
local discovery. Existing discovery links in the parent workspace also point to these same copies;
they are optional compatibility links, not required inputs. Keep the full repository together when
installing: copying a single SKILL.md without its sibling skills and data is insufficient.

Browser/search/email/Sheets access comes from the running agent's tools. Runtime packages and
account access are still required; credentials are never bundled. Search and nightly commands
prepare materials; explicit apply requests authorize the separate application flow.

Use Python 3.10+ and RTK (the helper subprocesses follow the repository RTK convention), and install Poppler with the platform package manager (`brew install poppler`
on macOS). Prepare an isolated Python environment and run the checks:

```sh
rtk proxy python3 -m venv .venv
rtk proxy .venv/bin/python -m pip install -r skills/ai-tailor/scripts/requirements.txt
rtk proxy .venv/bin/python -m unittest discover -s skills/ai-tailor/scripts -p 'test_*.py'
rtk proxy .venv/bin/python -m unittest discover -s skills/ai-apply/scripts -p 'test_*.py'
```

The application suite includes a local integration test using a real edited PDF and the
verification CLI, then claim release/reacquisition, unchanged-PDF upload validation and duplicate
prevention. Its review/confirmation records are explicitly synthetic fixtures; it does not certify
an agent visual review, employer ATS parsing or live portal submission.

For actual runs, set `PDF_PYTHON` to the absolute path of the prepared Python executable and use
the helper commands in each skill. Poppler and the pinned Python packages are runtime dependencies,
not skill dependencies. No schedule or application is started by installation or testing.

## Data and credentials

The confirmed contexts and resume library are versioned with this personal repository. Generated
job artifacts stay under the ignored `workflows/` directory; tracking uses the configured Google Sheet. Gmail status checks are scoped
to tracked companies, and explicit applications may read active-portal verification messages.
Apply requests can create required accounts and use transient credentials/email OTPs. Passwords,
OTPs and signed verification links are never saved in skills, artifacts or Git. Human security
challenges require the user's completion. No applications are submitted during ordinary searches.

## License

MIT — use and adapt freely.
