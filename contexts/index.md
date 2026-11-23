# Resume Tailoring Context Router

## Current local resume routing — 2026-11-23

The user confirmed `../main-resume/frontend-base.pdf` as the correct active resume. Use it for every suitable frontend/full-stack JD. Read [resume-baseline.md](resume-baseline.md) for all current approved statements. Read the seven flat reference Markdown files through `../main-resume/references/index.md` and relevant current context. No separate Full Stack BASE, remote manifest, Google Docs/Drive flow or Rezi template is required. Historical source/layout contracts below do not override this selection.

Follow ai-tailor for local PDF-copy → direct PDF edits → independent text/mechanical/evidence/all-page visual checks. Artifacts go under `../workflows/<company>/<role-job-id>/`; coordination logic stays in the skill. The actual selected BASE controls the two-line header, RESPONSIVE.IO role headings and three-project layout. Do not restore a mandatory fourth CSVora section. The latest BASE's claims are user-confirmed, not new benchmark/code/ATS observations; preserve evidence boundaries for additions.

## Usage Order

1. Read `personal.md` for identity, preferences and application answers.
2. Read `resume-baseline.md` for the complete current user-approved resume.
3. Read this router; route scope to relevant briefs, keeping the same local BASE.
4. Start current fact lookup at CORE-039, SERVER-037 or LYRA-044; read older exact records for additional implementation detail.
5. Read only relevant briefs/anchored records, not entire evidence archives.
6. Latest confirmed BASE facts supersede older conflicts; do not turn a skills listing into an unrecorded achievement.

## Context Map

| Context | Fast file | Deep file | ID family |
|---|---|---|---|
| Frontend/application | `core-app/brief.md` | `core-app/evidence.md` | CORE-xxx |
| Java/backend | `server/brief.md` | `server/evidence.md` | SERVER-xxx |
| Design system/UI platform | `design-system/brief.md` | `design-system/evidence.md` | LYRA-xxx |

## Role Routing

### Frontend roles

- Default: Frontend BASE.
- Read: `core-app/brief.md` and `design-system/brief.md`.
- Add `server/brief.md` only for backend/API/security requirements.

### Full Stack roles

- Default: the same local Frontend BASE; emphasize supported backend/full-stack contributions.
- Read: `core-app/brief.md` and `server/brief.md`.
- Add `design-system/brief.md` when frontend architecture/component systems matter.

### Design System / UI Platform roles

- Default: Frontend BASE.
- Read: `design-system/brief.md` and `core-app/brief.md`.
- Add backend context only for a substantive backend requirement.

### AI Application / Agent UI roles

- Default: the same local Frontend BASE; scope determines relevant frontend/backend evidence.
- Read: `design-system/brief.md` and `core-app/brief.md`.
- Read `server/brief.md` selectively for retrieval, persistence or integration implementation.
- AI interface construction is not automatic evidence of model/ADK/runtime ownership.

## Application Suitability Routing

`personal.md` is authoritative for preferences and application answers; this section routes decisions without duplicating the full profile.

1. Assess role family and meaningful frontend/full-stack scope. Accept the listed frontend/UI/React, Full Stack, SWE/SDE/SWE II and senior equivalents; generic SWE is acceptable with substantial frontend/full-stack work.
2. Prefer frontend-heavy → full stack with meaningful frontend → general SWE with meaningful frontend/full-stack. Skip backend-only/pure Java/server-platform scope without that relevance, primary support and QA.
3. Allow all Indian cities and work modes; international roles must be remote and explicitly permit work from India. Relocation is within India only.
4. Full-time only. Skip internship, contract/staffing/temporary, contract-to-hire unless later approved, freelance openings and part-time. Project history is not an employment preference.
5. Target 1+, 2+, 3+, 4+ requirements; exactly 5/5+ is lower priority. Skip stated minimums or range upper bounds above 5. Senior titles, night shifts and bonds alone are not exclusions.
6. Apply the ₹15 LPA minimum and Responsive.io/Responsive/RFPIO employer exclusion from personal.md. Unknown salary or eligibility is not proof of a match or exclusion.
7. Assess skills, evidence and missing mandatory requirements. One missing keyword alone is not a skip. If a potentially suitable role needs an unavailable mandatory answer/evidence, use BLOCKED.
8. Read `personal.md` for notice, CTC, India authorization and exact unknown-answer handling. Do not infer foreign authorization, compensation splits or immediate availability.

### Base Selection

Always copy `../main-resume/frontend-base.pdf`. Read core-app/design-system context for frontend-heavy roles and core-app/server for full-stack scope. Reference Markdown contributes supported details; no archived BASE/template replaces the selected source. The user's latest confirmation governs current source wording when older context disagrees; do not infer unrecorded implementation detail.

### Application Decision Statuses

| Status | Exact decision semantics |
|---|---|
| APPLIED | Successfully submitted, with visible or otherwise verifiable submission confirmation |
| BLOCKED | `Potentially applicable, but submission could not safely be completed.` Missing mandatory information/evidence, auth/OTP, required user input/approval, ambiguous required questions, unknown compensation split/legal answers, or portal obstruction |
| SKIPPED | `Intentionally not applied due to candidate preference or role mismatch.` Explicit role/location/type conflict or clearly inappropriate scope after review |

Do not BLOCK an explicit preference mismatch. Do not SKIP merely for one missing keyword. Suitability considers role family, frontend/full-stack relevance, seniority, years, location, work mode, employment type, skills, evidence and mandatory gaps.

## Global Capability Router

| JD Capability | Read | Evidence examples |
|---|---|---|
| Current approved BASE / all printed facts | resume-baseline; relevant brief | CORE-039, SERVER-037, LYRA-044 |
| React/TypeScript | core-app; design-system | CORE-001, CORE-026, CORE-039; LYRA-001, LYRA-041, LYRA-044 |
| Frontend architecture | core-app | CORE-001, CORE-013 |
| Design systems | design-system; core-app adoption | LYRA-001, LYRA-002; CORE-029 |
| Micro-frontends / 2 / Native web components | core-app | CORE-039; CORE-002 implementation detail |
| Module Federation | core-app | CORE-002 |
| Angular migration | core-app | CORE-003, CORE-004 |
| Performance / Webpack cold builds | core-app | CORE-005 |
| Package optimization | design-system | LYRA-018, LYRA-022 |
| Testing / RTL / MSW / Playwright / Jest | core-app; design-system | CORE-006; dated CORE-026 Jest tests; LYRA-024 |
| Current component test coverage / ~95% | design-system | LYRA-044 |
| Additional historical unit-test runtime / 56% | design-system | LYRA-024; separate from coverage |
| Accessibility | design-system; core-app | LYRA-004, LYRA-010, LYRA-024; CORE-033 |
| State management | core-app; design-system | CORE-012, CORE-019, CORE-026; LYRA-041 |
| Modern frontend workflows / tool adoption | design-system; core-app boundary | LYRA-042 (user-confirmed Zustand, StyleX, Bun, Oxlint, Oxfmt); LYRA-034 (code-verified Lyra Oxlint/Oxfmt) |
| TinyMCE | core-app | CORE-009 |
| Search/filtering UX | core-app | CORE-017, CORE-018, CORE-035 |
| Java | server | SERVER-001, SERVER-002, SERVER-006 |
| Spring Boot / reporting resilience | server | SERVER-005; framework precision in server brief |
| REST | server; core-app integration | SERVER-002, SERVER-006; CORE-014 |
| MongoDB | server | SERVER-006, SERVER-007, SERVER-015, SERVER-017 |
| Solr | server | SERVER-023, SERVER-024 |
| GraphQL | server, project only | SERVER-034 |
| PostgreSQL / Neon | server, project only | SERVER-034 |
| Security | server; account UI in core-app | SERVER-001, SERVER-007, SERVER-014; CORE-011 |
| Authorization | server | SERVER-001, SERVER-002, SERVER-012 |
| RAG / vector search / 30% relevance | server | SERVER-037 for current claim; SERVER-023/024 for narrower implementation |
| AI agents / 33 Lyra AI components | core-app; design-system; selective server | LYRA-044 current scope; CORE-026; LYRA-028/029/031; SERVER-027 |
| MCP | design-system | LYRA-021 |
| CI/CD / 4 release packages / 80% less manual effort | core-app; design-system | LYRA-044 current release facts; CORE-031, LYRA-022/023 detail |
| Sonar | server reporting; design-system quality | SERVER-030; LYRA-025 |
| Jenkins / Dockerized Sonar | design-system; server user-confirmed scope | LYRA-025, LYRA-038; SERVER-033 |
| Documentation | design-system | LYRA-019, LYRA-033 |
| Figma Code Connect | design-system | LYRA-020 |
| Recharts | design-system | LYRA-016 |
| ShadCN | design-system; current compatibility wording in resume-baseline.md / LYRA-044 | LYRA-027 plus later user-attested compatibility correction |
| Payments | server, project only | SERVER-034 |
| Deployment | server project; design-system publishing/Jenkins | SERVER-034; LYRA-022, LYRA-025, LYRA-038 |
| Data migration / backfill | server | SERVER-017, SERVER-024 |
| AG Grid / pagination | core-app; server counts | CORE-023; SERVER-015 |
| Dynamic authenticated integration | core-app POC; server hackathon | CORE-027; SERVER-029 |
| SSE / Redis / OTP guest sessions | server; core-app authentication/notifications | SERVER-032; CORE-007, CORE-008; USER-CONFIRMED personal implementation |

`Read` names identify corresponding briefs, not entire archives. Examples are navigation pointers, not proof that every framework/version/metric in a JD is supported.

## Evidence Status Legend

| Fast status | Meaning |
|---|---|
| STRONG | Exact implementation/attribution supported by inspected code/PR evidence; deployment and metrics still need their own provenance |
| SUPPORTED | Finalized-base or explicit user-supported scope; do not invent missing mechanics or treat it as a fresh benchmark |
| PROJECT | Separate freelance/personal/hackathon project; retain production or demo maturity explicitly |
| POC | Implemented prototype/evaluation or branch work; not shipped adoption unless separately established |
| TOOLING | Build/test/release/docs/developer tooling; distinguish implementation from only using/reviewing it |
| SKILLS-ONLY | Knowledge/listing without attributable implementation evidence |
| LEARNING ONLY | Learning/discussion material, including friend implementation; not a personal achievement |
| DO NOT USE | Explicitly invalidated/invented/unattributed personal claim |
| UNKNOWN | Required detail is unavailable: UNKNOWN — requires user confirmation |

Keep archive labels such as CODE-VERIFIED, USER-CONFIRMED, REPORTED-VALIDATION, HISTORICAL, REVERTED, UNMERGED and UNCOMMITTED when retrieving a record. Fast statuses simplify routing; they do not erase detailed status or confidence.

## Global Do-Not-Use / Safety Overrides

The complete latest BASE was user-confirmed on 2026-11-23. CORE-039, SERVER-037 and LYRA-044 govern its current claims, metrics and role attribution. The narrower earlier confirmations below remain valid where consistent. Historical contradictory labels do not override current user confirmation; confirmation is not a new code audit or benchmark.

- **SSE/60%:** USER-CONFIRMED / PERSONAL IMPLEMENTATION; resume-safe YES, 60% client polling-overhead reduction (SERVER-032; CORE-008).
- **Redis/OTP guest sessions:** USER-CONFIRMED / PERSONAL IMPLEMENTATION; resume-safe YES (SERVER-032; CORE-007, CORE-011). Historical TOTP QR repair is a separate contribution.
- **Dockerized Sonar/Jenkins:** USER-CONFIRMED / PERSONAL IMPLEMENTATION for Dockerized Sonar validation in Jenkins CI and Lyra deployments/Sonar management (SERVER-033; LYRA-025, LYRA-038); no all-employer CI ownership.
- **Modern frontend tools:** USER-CONFIRMED / PERSONAL IMPLEMENTATION (2026-10-03) of adopting Zustand, StyleX, Bun, Oxlint and Oxfmt in frontend workflows (LYRA-042). Only the Lyra Oxlint/Oxfmt migration is separately code-verified (LYRA-034); no new metrics, named-app adoption or rollout breadth are inferred.
- **Internship backend:** USER-CONFIRMED / PERSONAL IMPLEMENTATION for Spring Boot REST APIs/Java background processing with product/QA; scoped CODE detail remains in SERVER-009/010, current broad confirmation in SERVER-033.
- **Membership/DAO/projection/tests/SBOM:** USER-CONFIRMED / PERSONAL IMPLEMENTATION plus scoped CODE evidence in SERVER-006/007. Use the combined BASE wording without 15+; no broad CVE/tooling ownership or invented latency.
- **15+ fields:** INVENTED (USER-CONFIRMED), historical wording; DO NOT USE as a verified metric. SERVER-007 proves exactly 11 exclusions in the inspected selective Mongo projection. Default tailoring uses data minimization without invented quantity.
- **Webpack metric:** current user-approved printed BASE uses 86% (10–14 minutes → ~101 seconds). The historical finer 101.45-second/~88% record remains CORE-005/rfp-app evidence, not Lyra; do not silently rewrite the latest approved figure or call it a fresh benchmark.
- **Test metric:** 174 → 76 sec / 56% belongs to design-system/LYRA-024, not core-app testing.
- No audited WCAG compliance claim, broad AWS architecture beyond project S3 and user-confirmed S3 build-cache reuse, universal API compatibility, or invented outcomes/scale.
- 50+ means engineer enablement/training, not direct mentoring or managed team size.
- Historical ShadCN source remains IMPLEMENTED PROTOTYPE / POC with third-party provenance. The later user-approved resume wording `added ShadCN compatibility through a Tailwind token bridge` is superseded for current printing by the compatibility wording in resume-baseline.md / LYRA-044; it does not establish release of the historical 11-component prototype set or universal compatibility.
- Authenticated API request EXECUTION is confirmed for the June hackathon baseline; do not reduce it to templates. Keep July personally authored branch work and uncertain production rollout separate (SERVER-029).
- No proprietary code, credentials, customer data, private internal URLs or raw PR discussions in external material.
- Preserve migration periods, project attribution and selected-base ADK chronology. Unknown required application answers block submission.

## Deep Evidence Lookup Rule

| ID | Archive |
|---|---|
| CORE-xxx | `core-app/evidence.md` |
| SERVER-xxx | `server/evidence.md` |
| LYRA-xxx | `design-system/evidence.md` |

1. Expand any range to individual IDs; validate actual headings. Examples in this router enumerate IDs to avoid ambiguous ranges.
2. Find anchored record headings such as `### CORE-002 — ...`; retrieve from that heading to the next heading of equal or higher level.
3. Some archives repeat an ID for detailed supplements. Retrieve all matching heading blocks for the requested ID when precise implementation proof is needed; do not confuse prose mentions/PR mappings with record headings.
4. Read the selected block's attribution/status/metric boundary and any safety override in this file. Current overrides control over preserved historical prose.
5. Follow only explicitly necessary linked companion records. Full appendices/commit/PR inventories are opt-in for exact provenance questions, never default JD context.

## Current BASE reconciliation

Completed by explicit user confirmation on 2026-11-23: the local selected BASE is correct. See the active personal.md section for hash, employer/roles, header, projects and source precedence. Historical October/November remote reconciliations remain provenance, not instructions to restore deleted files or required project sections.

## Latest AI Coding Practice Confirmation

LYRA-043 in `design-system/evidence.md` records regular Cursor, Codex, Claude Code and Claude chat usage for implementation, tests and generated-code review, explicitly confirmed and requested to be saved during InCommon ai-tailor (LinkedIn 4473644567). Use for general personal practice; no invented expertise rating, assistant-specific feature/metric, unfamiliar-language success or enterprise/security-policy claim. Historical unknowns are superseded only in this scope; Copilot remains unconfirmed.

## Recent confirmed evidence routing — 2026-10-24

Before marking a capability unsupported, check current personal facts, brief updates and the latest dated evidence supplement. If a known recent job record contains an explicit user correction absent from central context, read that final correction rather than relying on an earlier gap assessment. An old tailored sentence alone is not new confirmation. The selected BASE has the separate explicit 2026-11-23 confirmation recorded above.

| Capability | Authoritative route | Boundary |
|---|---|---|
| Cavemio video player, GSAP, Shaka/HLS.js, HLS/DASH, ABR, DRM, buffering/recovery | personal.md, Current printed projects / Cavemio; resume-baseline.md | User-confirmed project implementation/testing; no inferred production scale or expert depth |
| S3 build-cache reuse | CORE-005 dated supplement; core-app brief | Distinct from project image storage and cold-build benchmark |
| Easy Peasy authoring; Redux conversations; authored Jest tests | CORE-026 dated supplement | September 2025 versus October/November 2025 role attribution; no full backend ownership |
| Style Dictionary, token aliases, light/dark/brand themes, scoped portals | LYRA-002/003; design-system brief | Existing code-backed evidence; no new adoption metric |
| Branch code splitting/lazy loading | CORE-032 | Optional branch-level work; never imply shipped runtime gains |
