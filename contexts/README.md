# Context System

## Purpose

This directory is the factual source for resume tailoring, job suitability checks and future application answers. It preserves implementation evidence while keeping routine JD matching concise. It does not implement or authorize job search, submission or Rezi changes.

## Files

| File | Purpose | Default retrieval |
|---|---|---|
| `personal.md` | Identity, timeline, preferences, application answers and immutable bases | Every run |
| `resume-baseline.md` | Exact latest approved resume text, source hash and links | Every run |
| `index.md` | Role/capability router, statuses and safety overrides | Every run |
| `core-app/brief.md` | Application/frontend tailoring facts | Relevant frontend/application JDs |
| `server/brief.md` | Personally supported backend/full-stack facts | Relevant backend/API/security JDs |
| `design-system/brief.md` | Lyra/component/platform tailoring facts | Relevant UI platform/design-system JDs |
| `core-app/evidence.md` | Complete CORE investigation archive | Exact requested records only |
| `server/evidence.md` | Complete SERVER investigation archive | Exact requested records only |
| `design-system/evidence.md` | Complete LYRA investigation archive | Exact requested records only |

## Retrieval Strategy

Fast path: **personal → resume-baseline → index → relevant brief → exact evidence IDs**. Personal preferences/application answers are authoritative in `personal.md`; briefs and evidence establish engineering scope and attribution.

- Start with identity/preferences and use the single local BASE and route the JD to relevant briefs.
- Use the briefs for initial fit, keywords and factual achievement selection.
- Open individual evidence records only for attribution, precise wording, implementation detail, chronology, testing, tradeoffs or unresolved conflicts.
- Never load all archives by default. Retrieval mechanics are documented in `index.md`.
- Record references are stable IDs, not mutable line numbers. Multiple same-ID headings can be supplements to one contribution.
- Earlier investigation records remain historical evidence; new dated confirmations are added without rewriting their original text. Old `contexts/core-app.md`, `contexts/server.md` and `contexts/design-system.md` paths inside historical prose mean their corresponding new `*/evidence.md` archives.
- Historical references to personal.md's former engineering metrics/maintenance contract are dated provenance. Current safety overrides and corrected evidence records control reuse.
- Old appendices and archived guidance can contain invalidated claims. Read `index.md` overrides before retrieving or tailoring any record.

## Evidence Precedence

1. Latest explicit user confirmation/correction, including the complete current BASE confirmed on 2026-11-23.
2. Code/PR evidence for exact implementation and attribution.
3. Older finalized resume-supported fact; the explicitly confirmed current BASE is covered by rule 1.
4. Older resume wording.
5. Skills-only evidence.

Record conflicts with both versions and their sources; do not silently combine them. Latest corrections can invalidate old resume bullets. A user-confirmed invented number remains invented; retention in an archive never makes it verified. Code proves mechanics, not automatically production rollout, personal preferences, adoption scale or benchmark outcomes.

Design-system repository-level contribution attribution is user-confirmed and includes all recorded identities. Preserve actual actors and third-party provenance; this does not apply blanket ownership to core/server collaborators' work. A PR author, current file, committer or merge alone is not proof of surrounding system authorship.

## Confidentiality

Never copy proprietary code, credentials, customer data, private internal URLs or raw PR discussions into external resumes/applications. Use public-safe behavioral summaries. Evidence archives remain internal factual references; their IDs may be used for internal traceability, not as substitutes for public portfolio links.

## Updating Context

- Update the relevant `evidence.md` first; preserve existing IDs, ledgers, source coverage and provenance appendices.
- Then update the corresponding `brief.md` to reflect the new fact/status/boundary.
- Update `index.md` only when routing, safety status or reconciliation changes.
- Update `personal.md` only for personal/application facts; do not restore an engineering dump there.
- Each record should preserve problem/action, personal scope, implementation flow, symbols/paths, tests/tradeoffs, source repo/ref/HEAD/date, commits/PR evidence, current/historical maturity, metrics, confidence and prohibited claims.
- Inspect exact diffs/tests and accessible hosting metadata when new research is authorized. Distinguish personal implementation, collaboration, review, merge transport, generated artifacts and existing architecture.
- Keep historical/reverted/unmerged/uncommitted work explicit. Commit/merge dates are not automatically role or deployment dates.
- Preserve source-coverage/access limitations; do not present partial research as exhaustive.
- Retain supported baseline facts without inventing mechanisms or metrics. Benchmark claims require recorded provenance; reported measurements are not fresh runs.
- Use `UNKNOWN — requires user confirmation` for gaps. Do not repeat questions already answered unless there is a conflict or a freshness concern.
- Validate every brief/router ID against an actual record heading and verify protected source/PDF/skill files remain unchanged during maintenance.

## Current Reconciliation Contract

The user's 2026-11-23 confirmation of `../main-resume/frontend-base.pdf` governs current resume facts. `resume-baseline.md` preserves its full wording; personal.md holds identity/preferences; the briefs reflect its current metrics/scope directly; CORE-039, SERVER-037 and LYRA-044 record the confirmation with role boundaries. Existing evidence remains available for additional mechanisms and historical provenance.

Preserve the BASE and use flat reference Markdown plus relevant contexts during tailoring. Actual authoring/output/verification mechanics are maintained in ai-tailor, with jobs under `workflows/<company>/<job>/`. Retired remote source/template instructions are not active context. Context synchronization creates no tailored resume, application or new measurement.

## Repository workspace

These records and the resume inputs now live in this repository. Normal tailoring reads this checked-in evidence directly; historical source-repository paths, refs and URLs document provenance and do not require external source checkouts. Do not manufacture new verification when a historical source is unavailable. Current workflow instructions are in `../skills/job-skill/`, `../skills/ai-tailor/` and `../skills/ai-apply/`.
