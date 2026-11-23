## Current resume confirmation — 2026-11-23

For current printed facts, read `SERVER-037` in this file and [resume-baseline.md](../resume-baseline.md). The user confirmed the full selected BASE as correct. Its facts/counts/role attribution override older conflicting resume wording. Earlier verification headers and investigation records below are historical within that overlap; they remain evidence for additional implementation detail. This update is user confirmation, not a new code audit or benchmark.

<!-- REVERIFY-20261003:START -->
## Current Canonical Verification — 2026-10-03

LATEST USER CONFIRMATION: the candidate re-verified SSE/60%, Redis caching/OTP guest sessions, Dockerized Sonar in Jenkins CI, Lyra deployment/Sonar management, membership/DAO/projection/JUnit/Mockito/SBOM work, and internship Spring Boot/REST/background processing as personal implementation. Current status: USER-CONFIRMED / PERSONAL IMPLEMENTATION; resume-safe YES. This supersedes earlier friend/filler/do-not-use classifications for those claims. Historical investigation text, source coverage, authorship searches and earlier statements below remain preserved; those earlier attribution conclusions are not the current canonical status.

The 60% polling-overhead metric is USER-CONFIRMED, not a fresh benchmark or newly located code attribution. No uninspected implementation internals are invented. Historical 15+ remains invented and is excluded from BASE/public wording; inspected projection count remains 11. Webpack attribution remains rfp-app; Lyra unit runtime remains separate. See corresponding latest notes inside the affected records.

<!-- REVERIFY-20261003:END -->

# Server / Backend Engineering Context

Established and inspected: **2026-10-03**. This knowledge base separates the candidate's implementation, collaboration/review, existing systems, learning material, and external projects. Read the attribution and metric boundaries with each record before tailoring a resume or application answer. Detailed implementation records and the full attributable commit inventory follow.

## Sources, maintenance and attribution

- `F`: finalized `main-resume/SAM - Frontend Engineer - BASE.pdf` (two pages), read only.
- `S`: finalized `main-resume/SAM - Full Stack Software Engineer - BASE.pdf` (two pages), read only.
- `U`: direct user instructions/clarifications in this inspection, including identity confirmation and corrections on 2026-10-03.
- `CODE`: actual local commit diff, historical/current implementation, or relevant blame inspected. `HISTORY`: Git metadata, ancestry or patch identity. `PR`: authenticated GitHub title/body/commits/files/reviews/comments and merge status actually retrieved. These supplement personal.md's evidence vocabulary.
- `RESUME-SUPPORTED`: preserve the approved F/S factual baseline and metrics when implementation or measurements are unavailable. It is not independent code or deployment verification. `USER-CONFIRMED` records the user's exact scope clarification; `CONFLICT` preserves both inconsistent sources. `UNKNOWN` explicitly limits inference. `INVENTED (USER-CONFIRMED)` identifies a number the user explicitly says was made up; retain its wording/provenance without treating it as a measured engineering outcome.
- `PRODUCTION`, `TOOLING`, `PROJECT`, `HACKATHON` and `PROTOTYPE / POC` identify the source's stated context, not automatic deployment proof. A merged PR, release hook or production-named branch does not establish rollout. Attribution confidence is confirmed for the four user-confirmed Git identities; surrounding system ownership remains limited to the inspected changes.
- All repository-backed records share the source/ref/HEAD and inspection date below unless an explicit historical SHA/ref is given. The finalized PDFs, personal.md, other contexts and source repository were not edited. No confidential code, credentials, raw request headers or tenant identifiers are persisted here.

**Latest corrections control future use.** U now explicitly identifies the 15+ user-list field count as a made-up resume number and asks to retain the wording; preserve it as `INVENTED (USER-CONFIRMED)`, separately from the 11 code-verified Mongo exclusions. SSE/60% polling and Redis/OTP guest-session implementation belongs to a friend, per U. Retain it for attributed technical discussion/learning in SERVER-032; do not present it as the candidate's personal implementation or measured outcome. U describes the generic internship background-pipeline and complete Dockerized Sonar/Jenkins wording as “filler”; preserve its resume provenance in SERVER-033, with personal scope unverified. The candidate's actual project-template process extension, Java Sonar fixes, Python reporting tests and Sonar review work remain separately established. U asks to retain the June hackathon wording; it remains resume-supported, separately from the personally authored July Phase II branch code (SERVER-029).

## Backend capability map

| Area | Evidence and personal scope | Detailed record |
|---|---|---|
| Java / REST / MongoDB | Inspected JAX-RS/Jersey APIs and Spring-injected services/DAOs; Spring Boot microservice configuration also exists. Do not call every controller Spring MVC or every module Spring Boot. | SERVER-001–028; build snapshot below |
| Business-unit retrieval | One membership API response with partitions and user map; DAO projection and mocked JUnit/Mockito coverage. Original API-call count/latency unknown. | SERVER-006 |
| Disclosure / SBOM remediation | Code proves 11 Mongo exclusions in a selective query; **15+ response fields** wording remains INVENTED (USER-CONFIRMED). U confirms the same initiative as SBOM remediation; no SBOM/CVE/dependency-remediation implementation located. | SERVER-007 |
| Reporting | Per-company exception isolation, missing-data/cell validation, diagnostics. Resume calls this Spring Boot reporting; actual modules and process/service flow recorded. | SERVER-005 |
| Search / RAG retrieval | Response-header metadata, Mongo/Solr filters, AI answer-context propagation, atomic index updates and backfill tooling. Existing model/embedding infrastructure is not personal ownership. | SERVER-023–024 |
| Workflow / background activity | Discussion state, onboarding validation, activity pagination, project-template activity extension and email migrations. Broad internship pipeline claim remains unresolved. | SERVER-002,008–009,015–019,033 |
| Security / access | Super-admin username guard, permission/input checks, TOTP QR repair, activation-state and BYOK-parameter fixes. Friend guest-session claims are separate. | SERVER-001–003,007,012,014,032 |
| Integrations | HubSpot/SharePoint diagnostics, Slack text normalization, Mongo integration upsert fixes, DeepL organization glossary/no-translate handling. | SERVER-020–022,026 |
| AI / agent applications | Input/conversation/canvas persistence and V1 compatibility; July external-source discovery/index/session prototype. No personal SSE/ADK/model-runtime ownership inferred. | SERVER-027,029 |
| Quality / tooling | Java null/static-analysis fixes, JUnit/Mockito changes, Python weighted Sonar reporting with 11 tests; review and merge coordination. | SERVER-006,010,030–031,036 |
| Redis / OTP / SSE | Friend implementation; retained as learning material. Candidate hands-on implementation/proficiency and event lifecycle details unknown. | SERVER-032 |
| GraphQL / Neon PostgreSQL / payments / deployment | Freelance commerce, outside this employer repository; resume-supported personal work. | SERVER-034 |

## Metric provenance and factual boundaries

| Claim | Provenance / use | What remains unknown |
|---|---|---|
| Membership retrieval in **one Java API call** | S p1; code confirms the combined endpoint/response, SERVER-006 | Previous number of calls, latency, traffic or payload-byte savings |
| **15+ response fields removed** | Historical S p1 wording; U explicitly says the number is made up and requests retention: INVENTED (USER-CONFIRMED), SERVER-007 | Not a measured count. Code proves 11 Mongo exclusions; SBOM generator/dependency/CVE details remain unknown |
| **30% MTTR reduction** through ELK analysis/root-cause investigation | F/S p2; retained RESUME-SUPPORTED at U's request, SERVER-033; no measurement evidence supplied | Incident sample, period, calculation, underlying logs and personal actions beyond located diagnostics |
| **60% polling reduction** | F/S p1 historical provenance; U attributes the SSE implementation to a friend, SERVER-032 | Benchmark, exact system and whether the candidate contributed any separate work; not a candidate achievement |
| **5+ demonstrated services**, including Chorus and Jira | F/S p2; June 2026 hackathon baseline retained at U's request, SERVER-029 | Complete service list, individual June components and precise production rollout |
| **Two commerce OAuth providers** | F/S p2: Google and Discord, SERVER-034 | Session/library/permission internals; employer provider implementation not inferred |
| **11 Python tests passed** | Actual local read-only audit run plus inspected PR descriptions, SERVER-030 | No Java coverage percentage or employer CI-wide quality improvement inferred |

Do not invent company/user/record counts, original request counts, p95 latency, retries, coverage percentages, throughput, savings, rollout, deployment ownership or design authority. Preserve approved metrics with their exact provenance; absence of benchmark logs does not disprove them. Code constants such as 30-record batches, 10 threads, 500 visited nodes or word thresholds are configuration/logic limits, not achieved production scale.

## Repository snapshot and identity (2026-10-03)

The evidence ledger below supersedes the prior source-unavailable baseline. Resume/user provenance remains explicit where independent implementation or rollout evidence is missing. A merged PR is not proof of production deployment.

- Source: `/Users/SANJEEV.S/projects/rfpserver`; origin `https://github.com/responsive-core/rfpserver.git` (private).
- Inspected checkout: `sam/sonarqube-rfpio-app-coverage-aggregation`; HEAD `54a406b06074cec63c8be4f6de19c41febb2863d`. Source working tree initially clean and read-only throughout.
- Inventory: 154,311 commits reachable through all available refs; 9 local branches, 5,580 remote refs, 8 tags, one stash ref and one Codex ref. Author/committer date extrema 2015-01-07 through 2026-09-22. Non-shallow checkout; this does not prove deleted/unfetched branches or older hosting records are complete.
- Identity: user explicitly confirmed on 2026-10-03 that all discovered identities are theirs: `sanjeev.s@rfpio.com`, `sanjeev.s@responsive.io`, `sanjeev.s+rio@responsive.io`, `sanjeev.shoyo@gmail.com`; aliases Sam, Sanjeev, S-Sanjeev, SANJEEV S; work GitHub `sanjeev-s_rio`. Authenticated `/user` also returns that login. Personal GitHub `sam-zc` comes from finalized resumes, not historical author inference.
- Complete local candidate inventory: 589 records with confirmed identities in the author field (including generated merges/stash) plus four commits authored by collaborators but committed by the candidate. Author counts: 536 rfpio email, 39 responsive email, 11 plus-rio email, three personal-email records. 593 author-or-committer candidate records total; 270 nonmerge records reduce to 255 stable patch IDs including two stash-only patch groups; **253 distinct non-stash patches** remain. The 323 merge records include the stash merge; the four committer-only records are merges. Repeated patch IDs and branch merges are not counted as separate features.
- GitHub repository was created 2026-02-04; 13 authored PRs were verified across authored/involvement searches; 29 accessible relevant PRs total were inspected, all closed, including merged and unmerged records. The initial authored search returned 12; involvement search exposed #5320, so search results alone are not treated as exhaustive. Older merge messages explicitly reference Bitbucket `rfpioinc/rfpserver`; those are local-history PR references, not inspected PR descriptions/reviews.
- Full coverage, date ranges, PR inspection limits, deduplication and missing history are recorded at the end. No claim of complete deleted/unfetched hosting history.

### SERVER-001 — Protect super-admin username changes

Evidence `CODE; HISTORY; PRODUCTION (S p2)`; attribution confirmed for authored diffs; status historical and retained in inspected HEAD (support-aware guard blamed to `407a126c5e549a58e3183fa27002121de58c65e4`); deployment supported by resume, no independent release evidence. Problem: proxy-assisted user-name changes could target a super-admin account (RES-91611). `d35404a9d9afa878aa7fd7de958795482b0aa1f0` (2023-11-10) adds a role check in `UserService.updateUserNameToUsers`; `407a126c5e549a58e3183fa27002121de58c65e4` (2023-11-14; duplicate patch exists) passes server-derived `isSupport()` from `AdminAPI` and permits the support exception while rejecting a super-admin target for non-support callers. The check happens before subsequent target-user mutation and downstream username update work. Initial blanket protection was refined to the support-aware form. The historical diff throws generic `Exception`; do not claim a specific HTTP status, audited access-control framework or removal of all account-takeover risks. No tests or impact measurement are present in these diffs. Keywords/application material: Java, service-layer authorization, privileged-account protection; explain the trusted support flag and target-role guard. Ownership covers this control, not original user-management architecture. Older hosting PR metadata inaccessible; local merge references are inventoried below.

### SERVER-002 — User onboarding validation and selective lookup

Evidence `CODE; HISTORY; employer context; deployment UNKNOWN`; attribution confirmed; historical implementation; inspected HEAD retains onboarding validation, with later collaborative changes; production deployment independently UNKNOWN. `7ffa04162c4debc789d3471f3bd36448424ca154`; anchors `6baa7ae623fee2377dd5b9c6468905cb3a990aee`, `6a9d824add9f92bb67f3b3702c50fa9c19c34ea1`, `8745851ce8d0a821f406810f6386077670ad7da1`, `5ccf6777a963b19c2dba9892b8656397b9f3d2c9` (February 2024). `UsersAPI /get-uservo-list` evolves from GET/comma-delimited query to POST/list body, rejects an empty list with G101 and delegates to company-scoped `UserService.getUserInfoList`. `AdminAPI /get-valid-new-users` requires MANAGE_USERS, checks feature-dependent role/support/module permissions, validates nonempty input and delegates to `getValidNewUsers`. Service classifies invalid addresses, signup-restricted addresses, existing users and valid candidates, normalizes addresses and throws U110 for license limits. Follow-up returns stable UI keys and adds structured `userNameMap` to bulk-add feedback. Validation endpoint does not itself create users. Tests/latency/count metrics UNKNOWN. Keywords: REST contracts, input validation, tenant scoping, authorization, license enforcement, bulk onboarding. Do not infer throughput or original endpoint ownership.

### SERVER-003 — TOTP QR-provider repair

Evidence `CODE; HISTORY`; attribution confirmed; historical fix superseded by collaborator local QR rendering; deployment UNKNOWN. `e5c616ec749cae0be35e56da9cea583c175abe21` and `65b070c37e924b507e317083aeb529659273bf43` (2024-04-08), `rfpio-auth-pod-commons-service/.../TimeBasedOneTimePasswordUtil.qrImageUrl`: switched QR-image URL from Google Charts to QuickChart while retaining the existing OTP-auth payload builder; follow-up corrected the additional query delimiter to `&`. This is a repair to existing TOTP enrollment rendering, not authorship of the OTP algorithm or Redis guest-session subsystem. Current HEAD returns a locally generated QR via `QRCodeGenerator`; Gokulakrishnan's `7828beff9d9075b821a55e1a02b8e1f11a47bf22` / `da28a2f642969ce10e5638fcc45bf8f9f74ac0bf` (2024-04-09–10) supersede the external-provider URL. No new tests or outcome metric in candidate diffs. Keywords: authentication troubleshooting, TOTP, external-service compatibility. No secrets/OTP values retained.

### SERVER-004 — Document import default-font repair

Evidence `CODE; HISTORY`; attribution confirmed; default-font behavior retained in inspected HEAD; deployment UNKNOWN. `a9860a8160d57bca2353fddde12fbf967db4af0c` (2023-12-19; repeated patch deduplicated), `0d85eeac073f3401b59d77d3a80bb4d3bbc68479` (2023-12-20), `rfpio-import-services/.../ExtractCssStyleFromDocxUtil`: determine document-default font, initialize fallback to Calibri even when defaults are absent, pass it through paragraph/character CSS extraction and supply FONT_FAMILY when style map lacks one. Before: missing default font produced incomplete imported styles. After: explicit document font or fallback survives extraction. Existing Apache POI/XWPF conversion is a used system, not original ownership. Tests and adoption metrics UNKNOWN. Keywords: Java, document parsing, defensive defaults, import compatibility.


### SERVER-005 — Daily-report failure isolation and missing-data resilience

Evidence `CODE; HISTORY; PRODUCTION (S p1)`; confirmed authored changes, historical implementation; independent deployment and operational metrics UNKNOWN. In `rfpio-microservice-projects/rfpio-daily-report/.../DailyReportProcess`, `122da2a4f04f3da8df7b232cebc01bf9ade97a98`, `5183d9b6d30c8b8725403561f592ef5ff70785fb`, `3be2e2ec8a592db82637f49836595c36d965b579` (2025-04-29) move exception handling inside the company loop, log company-level progress and retain exception stack traces. Failure while aggregating one company no longer aborts later companies. `d7b75c2300cdfb3f7b662b2a9726bc8fd0c388f3` adds completion logging. `1d579df8cc7ae524925e72c4fa2259a827fcc472`, `6a6a9c09aff256535ca737e79ca022f7c871cb68`, `f92f21337ad10491414f7c8b347d3bbe7f04562f`, `9f93b5edc7936ae96da43da41b26d4be304a84f3`, `4243eaf01e848b0761387e37cba4f62159b702d7`, `01eef5ff089664552136febc44e48ccd3974d81a` (2025-06-30–07-06) handle missing map values/retention periods and correct Excel numeric versus string cells: explicit zero for applicable numeric values, empty strings for missing text, with follow-up fixes for add-ons, contract period and billing frequency. This is exception isolation and validation, not demonstrated retries, parallelism, transactional rollback or complete success after partial failure. No new tests in these diffs. Keywords/application material: Java background processing, per-tenant failure isolation, null safety, diagnostic logging, report generation.

### SERVER-006 — Business-unit membership API and user-directory refactor

<!-- REVERIFY-20261003:START -->
**LATEST USER CONFIRMATION — 2026-10-03:** Membership/user metadata consolidation into one permission-checked Java API response, MongoDB DAO refactoring, selective data projection and JUnit/Mockito coverage during SBOM remediation are USER-CONFIRMED / PERSONAL IMPLEMENTATION; resume-safe YES. SERVER-007 projection and SERVER-006 test mechanics remain distinct. This does not establish broad SBOM tooling/CVE ownership or performance gains. This supersedes earlier contradictory attribution for current resume/application use; retained historical text follows.
<!-- REVERIFY-20261003:END -->

Evidence `CODE; HISTORY; PR; PRODUCTION (S p1)`; confirmed personal implementation plus explicit collaboration. `027d76768c16b11d1769aec808b8245ca8afe8b1`, `20f6f61ed901fa936c863f20a897fb6f3e6b160d`, `ad655f9b5e5940fd644968aa5e95fb0171f674f5` (2026-08-05–06) implement GET `/company-bu/{buId}/membership-users` in `CompanyBusinessUnitAPI`, permission `COMPANY_SETTINGS`, blank/null BU rejection G101, session company → `UserService.getBuMembershipPartition` → `UsersDAO` company-scoped Mongo query excluding super-admin users. Partitions primary members, shared members, globally shared users, eligible primary candidates and shared candidates; skips empty usernames; sorts relevant lists. Final response includes `userVoMap` together with membership lists, enabling the client to populate cached users in this one API call. Do not invent the previous number of calls or query/latency savings. The inspected method validates a nonblank ID; existence validation of the BU is not established.

Personally changed `UsersAPI` to `/get-user-directory-meta` with optional `fetchOnly` for tags, OOO users, super-admins or company-user counts; empty selector requests all supported metadata and unknown selector returns an empty map. Added a country-of-concern true/false filter (false also permits absent values) and role-count endpoint. JUnit/Mockito changes in `UsersAPITest`, `CompanyBusinessUnitAPITest`, `UsersDAOTest`, `AdminAPITest` cover delegation, empty inputs, selecting only requested services, Mongo query arguments and synthetic membership partition cases. These are mocked unit tests, not production load/DB integration benchmarks or proof that security annotations executed in tests.

Inspected PRs [#8629](https://github.com/responsive-core/rfpserver/pull/8629), [#8735](https://github.com/responsive-core/rfpserver/pull/8735), [#8742](https://github.com/responsive-core/rfpserver/pull/8742) are merged; their titles/descriptions describe user-list revamp and on-demand directory retrieval (RES-177198). #8735/#8742 contain Akarshan's implementation as well as candidate commits; do not attribute all directory metadata, pagination and active-user-count changes to the candidate. #8629 includes candidate review comments requesting JUnit coverage. Later personally authored `d299cb3ea8886fdc0776628550b5e8ac46f62931`, `6b7d41bbfb08550898f21785d181145039fdddae`, `9e60a84c1c7f61a3c4149ab5ad7f163641b61123` (08-12–14), PRs #9205/#9221, remove eager user loading and then restore it for the legacy V1 bootstrap while retaining V2's on-demand behavior in `UserLoadRequestAPI`. PR #9077 is a broad branch synchronization, not independently attributable implementation. Merged status does not establish deployment. Keywords: Java REST API, MongoDB DAO refactoring, payload minimization, backward compatibility, JUnit, Mockito, tenant scoping.

### SERVER-007 — Selective user-list projection and disclosure remediation

<!-- REVERIFY-20261003:START -->
**LATEST USER CONFIRMATION — 2026-10-03:** Selective projection/data-minimization and the relationship to SBOM remediation are re-verified USER-CONFIRMED / PERSONAL IMPLEMENTATION. Public BASE wording omits the historical invented 15+ quantity. Exactly 11 inspected Mongo exclusions remain the code-supported count; no universal endpoint fix is inferred. This supersedes earlier contradictory attribution for current resume/application use; retained historical text follows.
<!-- REVERIFY-20261003:END -->

Evidence `CODE; HISTORY; PR; PRODUCTION (S p1 broader approved context)`; confirmed author. `2b0c9fbab8205f09b33017f69cee74a9eb73d1dd` (2026-05-22; duplicate patch deduplicated) adds `UsersDAO.getUserInfoListProjection` and applies it before mapping the company-scoped username-list query. Inspected merged PRs [#5510](https://github.com/responsive-core/rfpserver/pull/5510), [#5708](https://github.com/responsive-core/rfpserver/pull/5708), titled “fix: RES-177486 VULN-04: Mass PII Disclosure via User List Endpoint”, contain this one-file change and approvals. Exactly 11 Mongo fields are excluded in this helper: organization preferences, Teams user ID, user type/message, active timestamp, last bounce/active dates, lock, alias emails, recent agents and additional map. Existing request flow: POST `UsersAPI /get-uservo-list` validates a nonempty username list and derives session company → `UserService.getUserInfoListForSuggestion` → company/username-list `UsersDAO.getUserInfoList` → projection before VO mapping → response `users` map, with existing guest/orphan availability classification for missing usernames. The candidate disclosure patch changes projection, not original guest classification or authentication. The business-unit DAO uses this helper later. Other overloaded user-list and super-admin retrieval methods in inspected HEAD lack this projection, so do not claim universal field removal or elimination of all PII exposure.

Historical S p1 wording states **15+ response fields removed during SBOM remediation**. Latest U clarification (2026-10-03): “userlist api hiding feilds 15+ is made up number just keep as it is i can take care”. Retain the literal 15+ wording as `INVENTED (USER-CONFIRMED); HISTORICAL RESUME WORDING`, not a measured or merely unverified count. The personal action of hiding user-list fields is code-verified, with exactly 11 Mongo exclusions in this path. The earlier U answer linking this to the same SBOM initiative remains USER-CONFIRMED; SBOM generator/dependency/CVE actions remain UNKNOWN. No extra endpoints or fields are inferred to justify 15+. No tests were introduced by the disclosure commit itself; later BU/DAO tests belong to SERVER-006. Keywords: data minimization, API security, MongoDB projection, disclosure remediation. Prohibited: treating 15+ as verified/measured, overwriting historical wording without provenance, treating the initiative link as proof of SBOM tooling/dependency remediation, or claiming all endpoints were fixed. Factual achievement wording can describe selective user-list projection without using the invented quantity.


### Attribution correction received during inspection (2026-10-03)

Evidence `USER-CONFIRMED; CONFLICT` with F/S and the prior server-context baseline. User explicitly answered the combined SSE/60% polling and Redis/OTP guest-session attribution question: “not done by me, but from friend i take it as resume wording and i can manage in interview”. **Neither contribution is the candidate's implementation.** The earlier SSE implementation, 60% polling reduction and Redis/OTP secure guest-session claims are retained as historical resume provenance with corrected friend ownership, and must not be reused as personal achievements. Follow-up user instruction asks to retain these topics for interview preparation because their friend is teaching them. Keep them available as learning/discussion material with explicit friend implementation attribution; demonstrated hands-on candidate scope and current proficiency remain UNKNOWN. Repository architecture or interview familiarity cannot restore implementation attribution. The TOTP QR-provider repair in SERVER-003 is a distinct personally authored fix and remains valid. No other contexts or finalized PDFs are edited in this task; propose correction of these claims in them separately.

SERVER-007 clarification: the user answered “same” when asked whether the disclosure fix and SBOM remediation were the same initiative. Record this relationship as `USER-CONFIRMED`, not code-proven SBOM tooling or dependency remediation. The later U clarification explicitly identifies 15+ as a made-up number; preserve its historical wording with INVENTED (USER-CONFIRMED) provenance. No additional-field count remains pending from the user.


## Detailed employer contribution ledger (continued)

For SERVER-008–031 below, repository/ref/HEAD and inspection date are the common snapshot recorded in the coverage section. Attribution is **confirmed authored implementation** when anchored to personally authored patches; it does not mean sole design/ownership of the surrounding system. Unless stated otherwise, tests and measured outcomes are UNKNOWN, and independent production deployment is UNKNOWN. Local Bitbucket merge references are inventoried separately; their descriptions/reviews were not accessible. Dates are commit author dates, not role or deployment dates.

### SERVER-008 — Discussion visibility, hidden-user persistence and E-Sign compatibility

`CODE; HISTORY`; July 2023 and September 2024; employer Java REST/MongoDB work. Anchors: `5809e772dec9539a8a065346f4ffa4f0cf11a9ce`, `687009919411fed44e60f6619c175d24fd58119a`, `662759d9a5620653a8ca008477c27b2ab663f9c1`, `493438f131bb0a58125c3872a0fedcb93570946e`, `bdcfae2f1bc6a74d4a195187e4c3f9a177a2446d`, `63bac24b4701d69c90e751e18fe5c6a2cfa4574c`, `aa6f983ea5cd48a46d9d991f5a12420f1d05dfac`; follow-up `3794cedeb2784749d117c2e91fe6d04ca3ffe0d7`.

Before: discussion comments lacked this per-user hidden-state path, and E-Sign comments were subjected to answer-library lookup assumptions. Added `CommentVO.hiddenUserList` mapping and serialization in `BaseDiscussionDAO`; renamed the initial `hideuser_list` storage to `hidden_user_list`. POST `ProjectDiscussionsAPI /update-hidden-users` validates discussion ID/comments, extracts status/mention/author/date filters and delegates to `ProjectDiscussionsService`; `/update-library-hidden-users` handles the library path. `LibraryDiscussionDAO` scopes by company, discussion ObjectId and comment ID; project DAO also scopes by project. Mongo positional updates use `$addToSet` for hiding a user and `$pullAll` for unhide, returning the updated document. Reply mentions unhide the parent for mentioned users. Project service returns comments filtered by the requested search criteria; library service returns the mapped discussion. Follow-ups remove unused linked-company parameters/checks; do not claim a surviving feature gate from the first version. E-Sign bypasses answer-library lookup; answer comments still require an existing non-trash library entry. September 2024 adds hidden-user exclusion to My Work parent-comment status aggregation. Subject “Performance Improvement” does not prove latency improvement. Current system retains hidden-state handling; surrounding permissions and entity ownership predate these changes. No candidate test additions in this cohort. Application material: trace a stateful REST update through company/project-scoped DAO to filtered response; discuss mention-driven visibility. Keywords: workflow APIs, MongoDB positional operators, discussion state, backend compatibility.

### SERVER-009 — Project-template organization activity and projection repair

<!-- REVERIFY-20261003:START -->
**LATEST USER CONFIRMATION — 2026-10-03:** Internship Spring Boot REST API/backend background-processing ownership and product/QA collaboration are now USER-CONFIRMED / PERSONAL IMPLEMENTATION. This record retains CODE-supported project-template process/activity metadata detail; SERVER-010 retains null-safety/static-analysis fixes. Do not invent API count, throughput or scale. This supersedes earlier contradictory attribution for current resume/application use; retained historical text follows.
<!-- REVERIFY-20261003:END -->

`CODE; HISTORY`; January 2023 internship-period evidence. `4edf6578d10c87b17a39089d9d65b33ce4bc2733`, `ccd7bb2c9c8f570e643e26e488322cb44f8b97db`, `5bd973cc50f0d2eb8c314ec0528466c0055d9052`, `c217b40f2191b0b97736f8ff8964459fec49464b`: inside existing `ProjectTemplateCopyOverProcess`, after copying activities, add a `TEMPLATE_CREATED` organization activity when creating a template. Construct activity with project/template identity, company, date and creator, then write through `projectActivitiesDAO`. Refine activity entity classification from TEMPLATE to PROJECT; include `company_id` in a project-details projection. Before: this creation activity/company context was missing from these paths; after: the activity path has the required metadata. Historical/current mainline ancestry verified. This establishes extension of an existing background copy process, not authorship of the whole pipeline or its orchestration. No deployment log, volume or test count. Keywords: background processing, activity/audit metadata, MongoDB projection, Java workflow integration.

### SERVER-010 — Sonar critical issue and defensive user-model guards

<!-- REVERIFY-20261003:START -->
**LATEST USER CONFIRMATION — 2026-10-03:** Latest USER-CONFIRMED / PERSONAL IMPLEMENTATION covers the combined internship API/background-processing contribution. These targeted Java/null-safety/static-analysis changes remain CODE-backed detail, without invented metrics. This supersedes earlier contradictory attribution for current resume/application use; retained historical text follows.
<!-- REVERIFY-20261003:END -->

`CODE; HISTORY`; January/March 2023. `9892dc5e34642c034758623ddd7b485478b8f62d`, `33df45b8de4716340f97a7951fbed057e098405e`, `577c023977d00bb4b89164153769cd73132c4779`, `7f45a31b6b6c18b8e68482f8960ef5e3ceceee7c`: repair map/list handling in `HTMLContentParserUtils`, add null checks, refine formatting while addressing RES-64466. `9cfee9311b5c574e478191602a6a742086583ca7` adds null guards around delegated `UserCompanyInfo` access in `UserInfoVO`. Scope is targeted Java/static-analysis and null-safety fixes. They do not prove ownership of Sonar deployment, all HTML sanitization, or a pipeline-wide quality gate. Historical mainline ancestry verified; no measured outcome/new tests established. Keywords: debugging, static analysis, null safety, Java maintenance.

### SERVER-011 — Spell-check/grammar preference migration

`CODE; HISTORY`; January 2023, RES-64141. `250ff8241d1552c7708eba52d976f5cde5913746`, `7f23f26a79e6ede29665460eee644d06a70d991c`, `4f657344991ad9f2c3c717c90840960a79ff7d9d`, `4c0195499399e7d873f18cff5bf500d3db4bdd06`: Mongo scripts rename prior ProWritingAid master/feature/data preferences to spell-check-and-grammar preference names, initialize Grammarly as the default provider, preserve existing provider settings and correct a provider-name typo. Scripts are migration intent, not proof they ran successfully. Historical revisions differ; no validated idempotency, atomicity, affected-record count or rollout log. Existing grammar-provider product architecture is outside personal ownership. Keywords: MongoDB migration, preference compatibility, rollout tooling.

### SERVER-012 — BYOK API parameter validation

`CODE; HISTORY`; September 2023. `7bb75bc73338726caac1b9fc8a3170b0644be40d`: `AdminAPI.validateKMSKey` and `updateKMSKeyId` accept the `kmskey` query parameter and reject blank keys with G101 in the existing BYOK-feature-gated flow. `04efe416d91987304a516c4a429a6b3fc0eb56f6` removes a model setter rather than implementing session management. Title “Session and BYOK” must not become authorship of encryption, KMS integration, rotation or sessions. Historical mainline ancestry verified. Keywords: REST validation, BYOK integration maintenance, feature gates.

### SERVER-013 — E-Sign numeric spreadsheet import

`CODE; HISTORY`; August 2023. `0b5c3b539a9be38e9bef957d84ccf903a3e6bde3`, `EsignBulkService`: replace `String.valueOf(double)` for numeric Excel cells with Apache POI `NumberToTextConverter.toText`, preventing an unwanted numeric suffix in bulk-send labels. This is input-format normalization in an existing E-Sign flow; not a new signature engine. Historical mainline ancestry verified; test/outcome metrics UNKNOWN. Keywords: Java, Excel parsing, data normalization, import troubleshooting.

### SERVER-014 — Password-policy defaults, activation-state protection and community sign-in

`CODE; HISTORY`; August/November 2024. `58e68763c40bf74356fb883b71891356fd70dffa` updates default password-policy seed values (minimum length/history 6→8 and enabled minimum-password policy) to address new-company settings errors. `3e0e802257f8762c76330fa8b90b616dade72c0b`, `daaf7055008953ec3aab195b9c485de5b31ccd8e`, `3dee6ea65a0fa51bef5d2e456a2f7440d3970781` prevent an existing non-pending user from being moved to `PENDING_ACTIVATION`, with status-change diagnostics, in the password/reset-adjacent user-service path. `e1ebd62e7b301c49c6cccffff090788a4dd48b8c` makes community sign-in use an optional configured community URL with fallback to the primary base URL (GovCloud issue). Current code/blame retains the community URL contribution. These are targeted fixes, not ownership of the whole sign-in/reset UI/backend or universal password security. Keywords: state-transition validation, configuration fallback, authentication troubleshooting, Java services.

### SERVER-015 — Organization-activity pagination and matching counts

`CODE; HISTORY`; November 2024. `a1093db9d16d050f4060c9475798ccb1ebe7ec69`, `31e6adc024cebcb4aa1e9d84f933b5bbbf12426b`, `005370990fa3c59bd75e8eb94a8114f9143433e8`: `OrganizationActivitiesDAO` adds offset/skip to descending `_id` sorting and limit, extracts `constructQuery` shared by result retrieval and `countDocuments`, and service/`OrganizationActivityVOList` return `totalCount`. Before: list/count/pagination support was incomplete; after: matching filters supply results and total for pagination. No index addition, cursor-pagination claim or quantified performance result. Historical mainline ancestry verified. Keywords: MongoDB DAO, REST pagination, consistent list/count filters, refactoring.

### SERVER-016 — Backend email rendering and V1/V2 route compatibility

`CODE; HISTORY`; October 2024–May 2025. Anchors `02ae4165d59dc5e3677d4fe244a00541177fbb14`, `0e23df91f1b41a61c4ef5dc8150bdcf8b4367f38`, `66bcb062709d0ec27d72c7dd39753a8362ebd5ac`, plus the email rendering cohorts in the complete patch ledger. Existing workflow action → `ProjectNotificationBuilder`/other notification builders → contextual data (project/section/users/custom fields) → `VelocityEngineUtils.getEmailContent` → selected shared V2 wrapper (`mainTemplateV2.vm`) and Velocity macros → existing email delivery. Personally route notification links through mail-specific V2 base URLs and section routes, pass template names into rendering to select the wrapper, adjust project/custom-field context and guest URL generation. Restore a dedicated V1 guest URL for legacy share-response compatibility. The commit titled “PackageBilling Unit Test” changes notification routing, not a Java test; do not count it as unit testing. Workflow status/action generation and delivery infrastructure already existed. Current implementation is shared/collaborative; a list of template enum names does not establish authorship of every notification type. No email delivery volume or original SMTP ownership. Keywords: server-side rendering, workflow notifications, REST/UI contract compatibility, Java, Velocity.

### SERVER-017 — Tenant-aware email-template migration with edited-content preservation

`CODE; HISTORY`; January–September 2025; large substantive initiative absent from the finalized backend bullets. Anchors `ef97ed4da3aae1ac56f555c5536606c0afbcbafc`, `3a112610e9cfeeaeea8c2196134f0a1707b9cc2f`, `cb493b9a00d780c560b5eb2afb4d89b1ca432a7f`, `ad460d697ba1a70e52c66f72b477937c6b30f125`, `fb9bf847e68fc484dfbcefd5526f59c83dd1cd5b`, `17f87d9a7bef8284d67e85505d6135129f187c84`; revisions/helpers/release hooks exhaustively inventoried below.

Problem: moving default email templates to the V2 structure also required adapting tenant-edited HTML, headings/buttons, translated labels and non-editable fields. Personally add `EmailTemplateMigrationV2Process implements RfpBatchProcess` plus template metadata helpers and release migration scheduling. Release hook writes a PENDING `batch_process` record; process reads optional company ID list (final version null-safe), snapshots previous global header/button/subject metadata from `email_template_metadata`, enumerates selected/dedicated databases, validates company IDs, migrates company-scoped overrides in `email_template`, handles shared-database tenant overrides, then updates global defaults. Even with a selected dedicated-company list, the inspected process subsequently handles shared-company templates/global defaults: do not claim perfectly restricted company targeting.

Within each edited template: resolve enum/new metadata; parse old HTML with Jsoup; retain editable content/text nodes; remove obsolete non-editable blocks and structural wrappers, append the new numbered placeholders; compare old translated labels/buttons with the tenant's edits; replace default values with new/translated defaults while retaining changed values; batch `UpdateOneModel`/`$set` writes. Translation lookup searches labels/email/message/actions/tooltip with null fallback. Logs report matched/modified counts and template/company failures. Company/template catches permit continued processing, but some exceptions are swallowed and outer completion logs can still occur: do not call this transactional, exactly-once or a verified successful migration. Null/index assumptions remain in historic/current code; intention to preserve edits is stronger evidence than proof that every edit survived.

Follow-ups fix the mistaken metadata collection, replace a JSON snapshot with Mongo metadata projection, preserve text nodes with `childNodes`, fix blank-content guards and Velocity end markers, skip special follower-table structures, and consolidate/delete older dated helper/process versions into `EmailTemplateMigrationHelperNew`. April PENDING-job guard checks for an existing pending migration; later release hooks delete/reinsert pending jobs. This is duplicate-pending-job handling, not an end-to-end idempotency guarantee. `c768536de199fb5597d0b44de2af34e77e09c469` explicitly reverts helper selection for dev-test deployment; later helpers supersede it. Current HEAD/blame retains candidate-created process/helper selection. Release-name strings and instructions do not prove rollout. No automated migration test additions found; migration safety, actual tenant/template counts and rollout validation UNKNOWN. Keywords/application material: Java background jobs, MongoDB bulk writes, data migration, compatibility, preservation of customization, troubleshooting, operational diagnostics.

### SERVER-018 — Gmail/Outlook HTML compatibility and workflow-template fixes

`CODE; HISTORY`; December 2024–September 2025. The patch ledger includes every template/helper revision under RES-132448/133748/144083/153742 and related bugs. Personally move wrapper styles inline, correct Velocity conditional placement and closing tags, use email-compatible table structures/spacer rows rather than relying on margins/div layout, adapt shared macro arguments (`addMarginTop`, button/table rendering), correct white-header text visibility and refine nested tables for Gmail/Outlook. Examples: `679468d097b59cfe979bf29850fd1796ed221a37`, `6a2b3916d5fd37f4dd6b058cfd37126bb554f6ca`, `3110b8527b48e8f0627ebd4f02d365dbeff21e97`, `0be642ff0e59de2ff3d8d0df192b8ec1e82b1179`, `73d88bf3c1d8bb1aeb70dcedb7d902fac1f19425`, `e0bbfd24141804ee76f120982d5849c838bde4f9`.

Repair context/templates for intake comment mentions, project-note mentions/followers, section assignment/review, bulk-review due dates, guest section names, custom fields, digest/task/clarification/Jira/GSheet/source-file notifications; these are template payload and migration maintenance inside pre-existing product workflows. Shared helpers consolidate repeated project/custom-field markup. A red-header style experiment and “Email testing” commit subjects are development iterations, not automated test evidence. French translation-label updates are small localization support, not ownership of multilingual translation architecture. Current templates are collaborative and later revised. Tests rendered by this audit: none; no cross-client screenshot/QA artifacts or quantified rendering success. Keywords: backend-generated HTML, Velocity, cross-client compatibility, workflow data/context, migration maintenance.

### SERVER-019 — Template-linked email URL tracking and HTML wrapping

`CODE; HISTORY`; February 2025. `EmailTemplateService.getConfiguredURLContent` uses Jsoup to add `emailTemplateId` query metadata to anchor URLs, selecting `?` or `&`, and returns original content if no anchors exist. `parseHtmlAndWrapContent` applies existing cleanup/replacement helpers and V2 wrapper handling; unwraps table-body content for PROFILE, DISCUSSIONS, PROACTIVE_PROPOSALS and AUTOPILOT compatibility. Anchors: `9fc0b2ff37c32c34c1f1bb869870748d8abdc639`, `5d08f27fb6d3db9a2c19f6cd6dcc02ab2a341899`, `448fc9702c4ae73435b4937babb763539880b4b1`, `1a7d315eb80f0f8224f67857a50f6ee562e054b7`. This is link metadata generation and HTML transformation, not proof of an analytics collector, click rates, deliverability improvement or complete XSS protection. Keywords: URL handling, HTML parsing, backend template contracts.

### SERVER-020 — Integration and request diagnostics

`CODE; HISTORY`; February–May 2025. `664abd710ef7e018ad7bd66d73e65bf8b00ef72d`, `39f89db67957fa507b3147b01bb81584c881708c`, `6b7c128cfeb2e2bdd402ce8feae7437cb5859282`, `3a36580c367f76f2a6892561898d3ea4523f7544`, `c87408f73744635bc8c74df971f071b0faf4ce3c`, `814d35f090b215a7ef007f2bfe09d0dd31e56b6e`: add HubSpot fetch-start, auth/company integration path, SharePoint empty-response/error and request-header diagnostics. Follow-ups replace full company/user-map logging with narrower username/pod context and adjust DEBUG/WARN levels. Historical `ExternalRequestInterceptors` change logged all request headers at INFO; do not generalize this to sanitized or secure logging. No raw headers, tokens or confidential values retained here. The approved ELK/30% MTTR fact is resume-supported separately; these logger changes do not measure or reproduce 30%. Keywords: troubleshooting, structured context, production diagnostics, external API debugging. Ownership is diagnostic instrumentation, not whole integrations or ELK platform.

### SERVER-021 — Slack Markdown normalization for search

`CODE; HISTORY`; May 2025, RES-144565. `53b0d8fc609ac06e1de9b64f09c2708e4ab62af1`, `4ac6f0cbd34b2a9dd0d539b298ce3b52993dc7ff`, `f0c26e6afc32bb5aa1b75ee97d0dbc1034958ba0`, `2b6cdec2525d4928d8fe0cdf38ff62e3e6106851`: initially strip markup with a regex loop, then replace it with `SlackMarkdownFactory.parseMarkupString(markup, returnPlainText)` using existing CommonMark HTML rendering plus Jsoup body text. `SlackIntegrationService.slackSearch` sends normalized text to the existing search flow; response/comment rendering requests HTML instead. Follow-up removes unnecessary checked-exception declarations. Before: Slack markup polluted search terms; after: the search path receives plain text while display retains markup support. Historical mainline ancestry verified. No candidate tests/result quality metric. Keywords: API integration, parsing, search-query normalization, refactoring.

### SERVER-022 — SharePoint and company-integration configuration repairs

`CODE; HISTORY`; May/August 2025. `cf45c19545cb4e57fac09948ab3e4dfd141898ba`, `d16791867e0d713bc8bbc343358ead7c19c5959a` refine missing individual integration behavior and SharePoint diagnostics; a temporary G101 throw for company-access information is removed in the follow-up. `cdc068e48a6750ae9ac2a8635018142ab48dcf16` preserves a Seismic-specific exception to account lookup. `f5df349c166b56ab8b7223c2080ab059b5f66dc5` changes SharePoint search sort from last-modified time to `Rank`, addressing wrong-document relevance ordering, without a quantified relevance improvement.

`5547f1fd589daed7d598d9b7fb589d6663bc6a1d`, `3225f12d24999c63df21fdd1090e2a3cc7822ee1`, `45309a298a196fd9c0196204076ca5fadca051d6`: `CompanyIntegrationDetailsDAO` validates an optional ObjectId before constructing it, otherwise filters by company/type, logs missing-ID context and enables upsert where appropriate. Before: invalid/missing ID caused edit errors; after: the existing integration update path can match/insert by its alternate scope. Do not claim immutable uniqueness or general concurrency safety. Keywords: MongoDB validation/upsert, external integration troubleshooting, query scoping, production error repair.

### SERVER-023 — Response-header filtering throughout retrieval and AI answer context

`CODE; HISTORY; PRODUCTION (S p1)`; June–July 2025. Anchors `b8ee06bc230e2ea38282a48af00a0a649d7fd7f1`, `a86c22f242eb81a26efe53db028f31f40be6003d`, `e197183bc1e5f2e42dda21c7a7518ad6bc249c2c`, `bc80269f862b864e391724f769b0032a988e668f`, `bc3958b119519601fd5374d2f4a0e1117ad14d63`, `94377985324ed45f1eac92c3e3343d4630ffaa3c`; related repeated branches are grouped in the ledger.

Problem: content response headers were missing from embedding/index metadata or not propagated through retrieval/filter/context paths. Existing create/update workflow → `AnswerLibraryService`/`ContentLibraryCreateUpdateService` collect response-header keys → `AnswerLibraryUtils`/`IndexContentVO`/`BaseFilterVO` carry `response_headers` (wire filter `responseHeaders`) → existing search abstraction → Mongo or Solr index. `ContentLibraryAISyncProcess` requests Solr numbered answer-header fields alongside answer content. `AbstractSearchService` assigns the matching header to content chunks based on the embedding ID's response index; title/other documents keep appropriate aggregate headers. This relies on existing ID conventions; do not promise robust handling of every malformed ID.

Personally add Mongo index/update mapping and filters (`$in` in vector filter and keyword query), Solr header filtering and stored/multivalued schema field, change search/vector index naming to v3, propagate selected headers through `AiSearchService`, `AiAutoRespondProcess` and allowed dataset filter keys, persist dataset changes/audit old vs new values, filter answer content when constructing AI context, and fix granular response VO/header mapping. Existing OpenAI/model calls and embedding generation are consumers, not personally authored model infrastructure. A historical version mistakenly maps response headers into tags; current mapper `setResponseHeaders` is blamed to collaborator `cbcf763b8726c638170d989188138018d9fb9d3e`, so credit the correction separately rather than treating the intermediate bug as the final behavior. Tests: `AiSearchServiceTest` mock-call signatures adjusted for the new argument; no new retrieval accuracy benchmark. APIs/DAO/query routes retain existing company scoping and feature checks; no new universal authorization claim. Application material: metadata must travel through ingest, retrieval filters and the answer context to produce consistent behavior. Keywords: RAG retrieval, MongoDB vector search, Solr, filtering, embeddings metadata, Java data flow, schema migration. No latency, corpus size, recall or model-quality metric.

### SERVER-024 — Bulk response-header synchronization and operational backfill

`CODE; HISTORY; PRODUCTION (S p1)`; June–July 2025. Anchors `b100f3eac5af19d503bc3721935b424fafaa20db`, `22964112abb293e453cb46c67dbd281345553490`, `97af6693cd37ceec3d1680c338aec32b205977db`, `d505b5205c0ec79f4b3a62e1d0c437b1d6275485`, `1a86be431c570805035c5723a91ccb4ef16b4442`, `299a3d8adec3b50c27da5ae6d9d727fb1def1352`, `f10aa39b24cbb26e48db442a494c465584747cbf`, `bcd5a5fae6a31446bb05c54a1cea1e0b1c0e0c4a`, `fef7ad7e8dc7aec674bd899ef54f7cab034dd017`, `bd03ec6f6e17058adff10e8102fb3dcbf62cec12`, `2828561572067da4c50f3db5a7e4128f10c416a0`.

After library bulk edits, `ContentLibraryBulkUpdateProcess` constructs changed IDs/header data → `RfpioSearchService` resolves the backend/property VO → `ISearchService.updateResponseHeaders`/`storeResponseHeaders`. Mongo updates content chunks and title metadata using company-scoped write models; Solr groups embedding IDs by original `doc_id`, builds atomic SET update documents and maps the proper header by content-chunk index. Follow-ups replace per-document Solr ID queries with grouped retrieval, remove an early stub/duplicate query path and fix full-header handling for non-content IDs. OpenSearch methods added in this cohort remain TODO stubs; no OpenSearch feature implementation claim.

Personally add `AiResponseHeaderSyncProcess` CLI: optional deduplicated company include/exclude lists, bounded configured thread count (1–10; default/fallback 10), ACTIVE/AI or AI-trial eligibility, company tasks and batch tasks, diagnostics and correlated MDC span IDs. Early source was Solr cursor queries; final candidate revisions read company-scoped ACTIVE ANSWER records directly through `AnswerLibraryDAO.getResponseHeaderMap`, projecting IDs/answers, deterministic `_id` sorting and skip/limit batches (30 records per batch in inspected HEAD). Mongo reads choose primary for regular bulk-update selection and secondary for the backfill selection in the inspected revision; do not claim strong cross-store consistency. Bulk writes log matched/modified counts, and timings/counts are instrumentation, not measured outcomes supplied by this audit. Release instructions enable the response-header flag and run explicit staged company cycles; instructions do not prove execution or customer scale. No raw tenant IDs retained.

Failure behavior: task exceptions logged; wrappers catch errors, some return success-shaped/logged completion despite internal failures; CLI finally exits zero after processing errors. No demonstrated retry policy, transaction across Mongo/Solr, rollback or exactly-once guarantee. Current HEAD retains the migration class and DAO-source change. Application material: explain why an existing indexed dataset needed backfill and how normal updates and backfill converge on the same metadata contract. Keywords: search consistency, Java CLI, migration tooling, MongoDB bulk writes, Solr atomic updates, thread pools, logging. No indexed-record count, elapsed runtime or production benchmark.

### SERVER-025 — Support portal administrator and pod lookup contracts

`CODE; HISTORY`; July 2025. `b18396600a3dff0b68bdecfeea4cfe1c32054e5c`, `e5d0dd4eee73e9ea05622a249a79040b3297f5e7`, `9f93b5edc7936ae96da43da41b26d4be304a84f3`: `CompanyAuthService` separates distinct administrators from `CompanyDAO` and pod names from `PODDetailsDAO`; passes current pod property/display selector and filters displayable records. Follow-up returns pod identifiers instead of display names. This is a support dropdown/lookup response-contract change inside existing authentication infrastructure, not auth-system or multi-region architecture ownership. Some commits also contain daily-report cell fixes (SERVER-005); deduplicate overlap. Keywords: DAO refactoring, lightweight lookup APIs, backend/UI contract, configuration.

### SERVER-026 — Organization glossary and DeepL no-translate behavior

`CODE; HISTORY; PROTOTYPE / POC (initial subject)`; August 5–22, 2025 (verified commit author dates). `4ee7412e44b301854f2f8937256e22c75809601d`, `1af68435b9f8e7b866191524c54a41a19e27b207`, `cd07e04973bfa229e5b19b2b9eb7f0afd7822d30`, `e372f47613f5bef6e9d48f9aa04b9f8eb4a0b1bf`, `32e1dbfc981de08047807296cc4a63ca0bc03661`, `ecd85254e5805d4a79fe4c176ef337afd13f23c0`, `ddcbdad7ba577605bacdcf5a6af054f8a8c1b683`.

Initial POC uses hardcoded glossary phrases; replace with organization-specific Mongo `responsive_glossary`. `ResponsiveGlossaryApi` POST `/glossary/update` and GET `/glossary/get` derive company/user from session → `ResponsiveGlossaryService` → DAO scoped by company `_id`; upsert glossary plus creator/update timestamp and return the stored list. Follow-ups add TRANSLATION feature gate and COMPANY_SETTINGS permission. Initial DAO dereferences missing document; later null/empty guard prevents glossary 503 error and returns an empty list.

Translation service recursively wraps eligible HTML text nodes with stable translate IDs, skips `rfpio-no-translate` subtrees, tracks trailing-space marker and collects texts. DeepL service loads the company's glossary, matches phrases case-insensitively, wraps them in `rfpglossary` tags, submits existing translation request with XML tag handling/ignored tag setting, and strips wrappers in the response. Service sorts longer multi-word glossary entries before short entries; regex builder handles whitespace, zero-width/nonbreaking characters and the marker so phrase protection survives formatting. `AtomicInteger` supports counter sharing through recursion; not evidence of parallel execution. Current HEAD/blame retains candidate DAO/service additions and null guard, but original DeepL HTTP client, credentials and translation product existed. Production status remains UNKNOWN despite mainline inclusion. No new unit tests or translated-document accuracy metric. Keywords: REST, MongoDB upsert, external API integration, HTML parsing, Unicode/regex, defensive validation, tenant customization.

### SERVER-027 — Agent Studio conversation persistence and reopenable canvases

`CODE; HISTORY`; September–November 2025. `02bb233c00220ac307c676647c713808b1c274b4`, `b2fe1b225c86f9ac31b873e7274e580b7996ea34`, `59c043222741735d17adb63ec9c5b808843a9fbc`, `1f64b545dd2fb4779919a12543e62b7d59e93b0b`, `84990c26cd3ea8e306c7c7305c568f848d450f90`, `47df6c7700d0c6edb00f7bf4da2a38a879d4e0a1`, `40bf0841788a6cf58e183e578c1e98afb46f67c1`, `11d22667a82c416538b701db658d5e8d73866b3e`, `1ee942deb1f57a1465f00c4c9e15cc80b37a268f`.

Existing Agent Studio request/controller → `AgentsStudioService`/`ResearchAgentStudioService` → `ConversationManager` → `ResponsiveAskConversationDAO`/`ResponsiveAskPromptDAO` Mongo persistence → response VO/document-section data used by the UI canvas. Personally introduce ASK_AGENT_V2 enum, experiment with named multipart file mapping then remove that mapping in the next revision; do not present removed mapping as the final contract. Persist/map configured input fields (name, required flag, help, instructions, value, type) and entity/agent IDs into conversation/message response structures so they survive reopening. Agent response paths populate canvas data for longer answers (historical >400 and >300 word conditions are logic thresholds, not output-quality metrics); preserve research Markdown and persist sections rather than relying only on an in-memory response. `extractSections` splits first-level title and second-level Markdown sections into an ordered map with generated ObjectIds for section rewrite. Fix nullable V1 agent request access. Word-threshold fallback in research service is later removed as persistence/section handling evolves.

Auth/model runtime, original agent execution and ADK architecture are used systems, not ownership demonstrated by these diffs. Invalid input-field enum strings can throw in historical mapping; no unverified graceful-recovery claim. Candidate `@Ignore` disables research API/service test classes in November: explicitly record this instead of claiming all agent tests were passing or expanded. No backend model/agent accuracy, request volume or SSE implementation claim. Source dates extend beyond the resume's September 2024–September 2025 role placement for the platform bullet; dates are not silently reassigned. Keywords: AI application integration, Java, MongoDB persistence, backward compatibility, DTO contracts, Markdown parsing, conversational state.

### SERVER-028 — Region-restriction preference release migration

`CODE; HISTORY`; October 2025. `20d24d43a9fabe94a23f0d2697331531876d6e7c`, `98596b86b0da777728faadf07287a681b3e7d712`: move/correct auth-database release hooks that set missing `master_settings.region_restriction` to `0`, using `$exists:false`; follow-up restores the earlier hook as well. This is preference migration/release sequencing, not implementation of geolocation enforcement, country-policy logic or compliance guarantees. Existing values are protected by the missing-field filter. Current mainline ancestry verified; actual execution UNKNOWN. Keywords: release migration, MongoDB preferences, compatibility.

### SERVER-029 — Hackathon Phase II external-source discovery, indexing and connection state

`CODE; HISTORY; HACKATHON; PROTOTYPE / POC`; personally authored July 2–12, 2026 branch work: `f74aa089d8085f835bca4bcd0d0251a5014a5867`, `d86b9aecd859fd1ddc3e1732a8cd968197607aa0`, `2b86f1bcbcd3891dc7fa9e82f46020f5e2bf21ca`, `34141e59772133a608211e0e743ecf69550c8a2e`; merge collaboration `9c01cb9058e5950a538a4ff3bb3d708df2711bde`, `791ed062c75c474864f7115a7006ab15b8470255`. These commits are absent from inspected HEAD/cached staging/master; visible feature-branch code does not prove production.

Personally connect `ResponsiveAskController` discovery/indexing contracts and DTOs with `ExternalSourceIndexingService` and `connectors-base`; distinguish AI_EXTERNAL_SOURCE from normal cloud connectors, persist provider/documentation metadata and group providers separately. Initial index method counts folders without doing indexing (stub); later work uses discovery and existing external-indexing calls with PROCESSING → ACTIVE on no failures / ERROR on failures and catches/rethrows while recording error state. DAO lookup/update is company/source/selection scoped, with last sync time and update flag handling; Mongo status-update failures are logged/return false. It is not proven end-to-end transactional or successful against every provider.

Personally replace one-level child discovery with bounded recursive traversal through `RootNodeDiscoveryService`, optional parent node ID/path and context-specific LLM discovery prompts; preserve the deprecated child endpoint for compatibility. File/document/page nodes become selected file IDs; folder nodes trigger authenticated discovery through the existing root service. Limits in this branch are maximum depth 10 and 500 visited nodes, not production scale achieved. Errors listing children are logged and the code treats the node as a leaf. The prompt requests a single largest-page call and explicitly excludes pagination follow-ups, so exhaustive provider listing is not guaranteed. Replace hardcoded examples with general discovery instructions. Add resource category/reason to auth schema; this Phase II indexing scope is file/document-shaped resources, and classifies ticket/CRM/chat-only APIs as unsupported. That narrower indexing boundary does not contradict the resume's earlier broad API-execution demonstrations.

Add POST `/extsource/session`, GET `/extsource/sessions`: validate provider key, overwrite request company/user with trusted session identity → `AiSourceConnectionSessionService` → Mongo `ai_source_connection_sessions` keyed by company/user/provider; upsert and return latest sessions sorted by update timestamp. Known states progress PENDING_AUTH → AUTHENTICATED → FOLDERS_FETCHED → INDEXED; ordinal check rejects backward transitions, but blank/unknown states are accepted and read-before-write is not a compare-and-set. Persist credentials-schema fields/auth URLs/discovered folders; code does not establish encrypted token storage, safe refresh or universal validation. No secret values are retained in this context.

Collaboration boundary: inspected PR [#7074](https://github.com/responsive-core/rfpserver/pull/7074), “Elk mavericks hackfest”, is by Elakkiya and contains earlier API-documentation authorization service/model work; no candidate-authored commits there. Candidate was involved/requested in the record, with no candidate review/comment text. The generic root request executor, original token/auth schema and June implementation are not proven personally authored by these July patches.

Resume-only project baseline remains **June 2026–June 2026**, Java-backed multi-turn documentation discovery and authenticated request generation AND execution, lazy-loaded/shared logic, **5+ demonstrated services including Chorus and Jira**, later production evolution (F/S p2). User explicitly requested on 2026-10-03 to keep this content unchanged; no extra implementation/rollout detail supplied. Preserve as `RESUME-SUPPORTED; HACKATHON`, later production claim from resume only. Do not substitute July for the hackathon dates, add unsupported providers or assign all prototype backend classes to the candidate. Keywords: AI-assisted API integration, API documentation, OAuth/API tokens, external request execution, recursive discovery, connector metadata, MongoDB state.

### SERVER-030 — Correct Sonar coverage aggregation and module reporting

<!-- REVERIFY-20261003:START -->
**LATEST USER CONFIRMATION — 2026-10-03:** Dockerized Sonar validation/Jenkins CI and Lyra deployment/Sonar management are now USER-CONFIRMED / PERSONAL IMPLEMENTATION through the latest confirmation (SERVER-033; LYRA-025). Existing Python aggregation/tests remain this record’s code-backed scope; confirmation does not turn every employer CI job into candidate ownership. This supersedes earlier contradictory attribution for current resume/application use; retained historical text follows.
<!-- REVERIFY-20261003:END -->

`CODE; HISTORY; PR; TOOLING`; September 2026. `54a406b06074cec63c8be4f6de19c41febb2863d`, authored and present at inspected HEAD. Merged PRs [#10163](https://github.com/responsive-core/rfpserver/pull/10163), [#10164](https://github.com/responsive-core/rfpserver/pull/10164), both “feat: aggregate RFPIO app coverage paths”, integrate the same patch into development/staging, with approvals; [#10156](https://github.com/responsive-core/rfpserver/pull/10156) closed unmerged with a broad base diff. Deduplicate these as one initiative.

Personally change Python `sonarqube_components.jsonc`/`sonarqube_utils.py` to support grouped arrays of RFPIO_APP paths, remove overlapping ancestor paths to avoid double counting recursive Sonar counters, request raw covered/uncovered line/condition metrics and sum those counts before computing percentages. Combined coverage uses covered lines plus covered conditions divided by their total; it is not a simple mean of component percentages. Normalize display groups and attach all underlying component links. Missing/invalid counters or failed paths produce warnings, partial/error state and N/A totals rather than publishing a misleading aggregate. Update HTML reporting with grouped path popovers and Slack-report payload generation; no Slack message sent by this audit. Other projects retain their existing metric retrieval/trend behavior.

Added 11 Python `unittest` tests covering weighted counters, grouping, overlap filtering and missing/failed metrics. Audit executed `python3 -B -m unittest sonarqube.test_sonarqube_utils` on 2026-10-03: **11 passed**, 0.019s locally (verification timing is not a resume speedup metric). PR descriptions also report 11 passing tests/compile checks; distinguish those reported checks from this actual run. This is reporting/tooling for frontend coverage stored in the server repo, not proof of Java coverage increase or ownership of the entire Sonar/Jenkins infrastructure. Stash/index/untracked test scaffolding is excluded from feature credit. Keywords: Python, SonarQube, coverage mathematics, test tooling, failure visibility, CI reporting.

### SERVER-031 — Backend review, collaboration and merge coordination

<!-- REVERIFY-20261003:START -->
**LATEST USER CONFIRMATION — 2026-10-03:** The latest Dockerized Sonar/Jenkins ownership confirmation is USER-CONFIRMED / PERSONAL IMPLEMENTATION (SERVER-033; LYRA-025). The collaborator review described below remains a review; it is not retroactively reclassified as personally authored code. This supersedes earlier contradictory attribution for current resume/application use; retained historical text follows.
<!-- REVERIFY-20261003:END -->

`PR; HISTORY; TOOLING`; confirmed hosting-account review activity, not personal implementation of reviewed systems. Inspected reviews: #9427 and #9983 (Akarshan user-load-details encryption) approved; #8211 user-list revamp has approved and dismissed reviews; #4638 (Keerthana response-header import indexing repair) approved; #11177 (Akarshan local Docker/Sonar scan setup) approved but PR closed unmerged; #11225 later local Sonar setup has a dismissed candidate review and is also unmerged; #946 public-profile ASK fixes has dismissed reviews, not final approval. Most candidate review bodies are blank, so no inferred design guidance, security assessment depth or mentoring. #8629 contains three candidate inline comments “Junit” requesting test coverage on API/DAO paths.

Encryption diffs use a feature-gated V2 response wrapper with AES-GCM/session-derived key utilities and tests, but those are Akarshan's changes. Local Sonar setup contains Docker Compose, startup/profile restore scripts and documentation, but those are Akarshan's changes and unmerged records. They do not independently verify the candidate's original Dockerized Sonar/Jenkins implementation bullet. PR #10102, “arthi_dev_ofc_online into development”, was opened by the candidate and merged, but all five implementation commits inspected are Arthi's; record merge coordination only. PR #9077 is broad synchronization; 1,625 file entries were retrieved, commit endpoint returns only 250 of 1,270 reported commits. No blanket implementation claim from these PRs. Four collaborator-authored/local candidate-committer records are excluded from personal implementation attribution. Keywords: code review, test review, integration coordination; no leadership/ownership or reviewer-quality metric.

### SERVER-032 — SSE and Redis/OTP: retained friend-implemented learning material

<!-- REVERIFY-20261003:START -->
**LATEST USER CONFIRMATION — 2026-10-03:** SSE implementation and 60% client polling-overhead reduction, plus Redis caching and OTP verification for secure guest access/session management, are now USER-CONFIRMED / PERSONAL IMPLEMENTATION; resume-safe YES. Earlier friend/learning statements and negative code-search findings are historical and superseded for attribution. No new code evidence, benchmark run, TTL/reconnect details or production internals are inferred. This supersedes earlier contradictory attribution for current resume/application use; retained historical text follows.
<!-- REVERIFY-20261003:END -->

`RESUME-SUPPORTED (historical); USER-CONFIRMED; CONFLICT; LEARNING`. F/S previously state SSE real-time notifications with **60% polling reduction**, and Redis caching/OTP verification for secure guest access/session management. U explicitly says these were **not done by the candidate**, but implemented by a friend who is teaching them; follow-up asks to retain the topics for interview preparation. Preserve the topics and old metric with this attribution. They can support a factual answer about what the candidate is learning or how a known system works, with friend ownership stated. They do not support “I built/implemented SSE”, “I reduced polling 60%”, or “I implemented Redis/OTP guest sessions”. The candidate's actual TOTP QR-provider repair is SERVER-003 and does not establish guest OTP or Redis ownership.

All candidate nonmerge patches were searched for SSE/event-stream and Redis additions/deletions; no attributable SSE/Redis implementation was found. Historical/deleted-path searches include SSE/guest/OTP/Redis code across available refs; these show system presence, not authorship. Missing details are **UNKNOWN — requires user confirmation**: event producers, emitter/subscriber modules, authentication, reconnect IDs, heartbeats, lifecycle cleanup, disconnect/error handling, polling benchmark provenance, Redis key/TTL/invalidation, OTP verification lifetime/rate limits and session security. No such internals are invented from architecture. Deployment status and learning proficiency are unknown. JD topics: SSE, streaming, lifecycle, Redis, OTP, sessions; use only as attributed learning material until personal scope is established.

### SERVER-033 — Resume-only operations and broad internship/CI claims

<!-- REVERIFY-20261003:START -->
**LATEST USER CONFIRMATION — 2026-10-03:** Dockerized Sonar validation integrated into Jenkins CI, Lyra deployment/Sonar management, and internship Spring Boot REST APIs/backend background processing with product/QA are now USER-CONFIRMED / PERSONAL IMPLEMENTATION; resume-safe YES. Earlier filler/scope-unresolved classifications are historical. SERVER-009/010 retain the narrower code-backed internship mechanics. 30% MTTR remains unchanged with its existing provenance. This supersedes earlier contradictory attribution for current resume/application use; retained historical text follows.
<!-- REVERIFY-20261003:END -->

`RESUME-SUPPORTED; USER-CONFIRMED (scope limitation); UNKNOWN`. F/S state internship Spring Boot REST APIs with product/QA teams and background data pipelines (September 2022–July 2023), Dockerized Sonar validation integrated into Jenkins, and employer ELK root-cause investigation with **30% MTTR reduction**. U answers the combined pipeline/Dockerized Sonar-Jenkins scope question: “thats just filler i can manage it”. This supplies no confirmed implementation scope for those two broad claims. Retain their historical F/S wording and this clarification as a conflict/unresolved attribution record; do not upgrade them to verified personal achievements. The clarification did not answer the separate ELK metric provenance, so preserve the 30% metric as resume-supported rather than applying the filler statement to it. In the latest follow-up, U explicitly asks to keep 30% unchanged and supplies no measurement evidence; the figure retains F/S provenance and its measurement question is closed.

Personally attributable narrower evidence: January 2023 project-template copy-process activity extension (SERVER-009), Java static-analysis/null fixes (SERVER-010), extensive 2025 migration/backfill processes (SERVER-017/024), September 2026 Python Sonar aggregation and 11 tests (SERVER-030), and review of collaborator Docker/Sonar setup (SERVER-031). No personally authored Jenkins/Docker/SBOM dependency/CVE implementation was located in the full candidate patch inventory. Current CI/build configuration is a used system; its existence is not attribution. Java/backend production incident diagnostics are CODE in SERVER-020, but they do not calculate 30%. Internship history before January 2023, specific QA collaboration, exact ELK incidents, original Jenkins pipeline/image/quality gates and deployment status remain unknown. Application material: explain the verified scoped extensions/diagnostics/reporting; preserve the broader claims' evidence limitation.

### SERVER-034 — Freelance commerce backend, separate from employer systems

`PROJECT; PRODUCTION; RESUME-SUPPORTED`, F/S p2, **May 2026–June 2026**. Freelance E-Commerce Payments Platform at `https://foulware.com/`; owned design, development, release and production updates of a Next.js/Neon PostgreSQL platform. PostgreSQL-backed GraphQL schemas/resolvers support catalog and order queries; product flows include catalog, cart, checkout and order dashboard/management. Integrated PayRam payments and automated license-key assignment after payment. Google/Discord OAuth (**two providers**) and RBAC protect commerce workflows. S supports Amazon S3 image storage, Vercel application deployment, PayRam separately self-hosted on an Ubuntu VPS, and SMTP notifications. SMTP delivery is separate from OAuth/OTP authentication. Source code is outside this repository and was not inspected here; original resume-supported ownership is preserved.

Unknown: GraphQL library/types, transactions/indexes/batching/pagination, role matrix/session library, webhook verification/idempotency/refunds, payment/customer/order/revenue figures, SMTP provider, runbooks and current live availability. No employer GraphQL/PostgreSQL/Neon/PayRam/S3/Vercel/VPS ownership inferred. S3 establishes image-storage scope, not broad AWS, EC2/EKS/Lambda/VPC/multi-region architecture. Resume-supported production updates do not supply frequency/dates beyond the project range. Keywords: GraphQL, PostgreSQL, Neon, OAuth, RBAC, payments, full-stack ownership, S3, Vercel, Linux/VPS, SMTP. Deployment provenance is resume-only; no live-site check or payment operations performed.

### SERVER-035 — Targeted release cleanup and SMB guide asset support

`CODE; HISTORY`; confirmed personally authored, historical; deployment/execution unknown. `1f644c1add7513cf280a6a702f8cbf7209bb13cc` (2024-11-04, RES-125844) adds `deleteCustomFields` to existing dedicated/shared post-release hooks in `DBMigrationProcess241107`. Query filters `type=DATE_AND_TIME` and selected entity types (ANSWER_LIBRARY, ALL, SECTION_TEMPLATE, DOCUMENT_LIBRARY, CATALOG); `company_custom_fields.deleteMany` removes matching definitions. This is an explicitly destructive release-cleanup intent in existing migration infrastructure, not proof of execution or a reversible rollout. The helper has no explicit company predicate; tenancy derives from the passed database/hook context, and the shared hook runs only when the passed database name is RFP_DB. No candidate tests, deleted-record count, backup/rollback or downstream data cleanup established. Keywords: MongoDB filters, release migration, targeted maintenance.

`8d5cfb1f283e3123a959e2bf8cb229c6e1bd3e1a` (2025-06-25, RES-148953) adds the SMB Emerging Edition guide PDF and clarifies an existing S3 upload instruction's assets-folder source. Binary content was not treated as authored software or proof of personal document authorship; no upload/deployment was verified. This is asset/release-support activity, not employer S3 architecture ownership. No raw guide content is reproduced.

### SERVER-036 — Merge-resolution work and imported-code limits

`HISTORY; CODE (combined diffs); collaboration attribution`. All 323 author-or-committer identity-matched merge records were inventoried, including 322 ordinary integration merges and one stash merge; 105 records have combined-diff paths including the stash. Combined diff lines were compared with the candidate's nonmerge patch corpus and remaining substantive differences inspected. Integration of other authors' work is not blanket implementation credit. Bitbucket-generated merge records often name the candidate as author but another person as committer; these do not prove the candidate performed the merge or resolved conflicts. The inventory distinguishes both identities.

`9c01cb9058e5950a538a4ff3bb3d708df2711bde` (July 2026 hackathon merge) combines external indexing/discovery revisions, adds null-safe discovered/indexed/failed file lists and response file IDs/count, plus `nodeId`/`nodeID` serialization alias handling. Credit this as attributable merge-resolution/contract repair around SERVER-029, not original ownership of the request executor/auth system. `24922a00178c87a324290b4d6bd6cbae3c53f124` combines Agent Studio request maps/files DTO fields around SERVER-027; these fields have overlapping collaborator history, so merge presence alone does not prove sole design.

Email branch merges reconcile V2 template allowlists, wrapping/Profile behavior, release hooks and dated helper variants (SERVER-016–019); `5f310e3423b35b011637bf586ffa67bc591773b2` includes an empty V2 allowlist on a test-revert branch and is not the final product contract. Release-sync merges such as `fa8fe1aad14fb7a56a18ef2062e71524d6a743dd` carry unrelated preference/index code from others; no new personal feature credit. Four collaborator-authored candidate-committer records are listed separately below. No contribution count is derived from merge volume. Keywords: integration coordination, compatibility, conflict resolution; not sole architecture ownership.

## Java/Maven/build/test context actually inspected

The root is a multi-module Maven repository. In inspected HEAD, root `pom.xml` declares Java 21, Spring 7.0.8, Jersey 5.0.0-M1, JUnit 4.13.2 plus Jupiter/Vintage 5.12.2, Surefire 3.5.5 and JaCoCo 0.8.13. `rfpio-microservice-projects/pom.xml` supplies Spring Boot 4.1.0, Java/test/plugin settings; reporting is a microservice module. Historical snapshot `9892dc5e34642c034758623ddd7b485478b8f62d` (January 2023) used Java 8/Spring 5.3.22/Jersey 2.35/Spring Boot 2.7.2; `122da2a4f04f3da8df7b232cebc01bf9ade97a98` (April 2025) used Java 17/Spring 6.0.23/Jersey 3.1.9/Spring Boot 3.2.2. These are configuration snapshots, not personally authored version upgrades or verified production runtime versions.

Common REST APIs inspected use JAX-RS `@Path`/GET/POST/QueryParam and permission annotations on Spring-managed components, with injected service/DAO dependencies. Authentication/session/access helpers and exception translation often predate candidate changes. Mongo DAOs use company/database scoping, `Document`/Bson filters, cursors/projections and bulk/update operations; no ORM or transaction framework is invented. Solr/OpenSearch/Mongo search abstraction existed; candidate-added OpenSearch methods in the response-header cohort are stubs.

JUnit/Mockito additions use mocked delegation, argument capture and synthetic data (including Mongo cursor mocks); historical API test classes use `MockitoJUnitRunner`. `UsersDAOTest` extends shared `RfpioJUnit`, whose broader legacy suite includes DB-backed tests: added mocked cases do not turn the entire suite into isolated unit tests. Relevant root/module POMs, test resources and shared test base were inspected. Java/Maven suites were **not executed** in this read-only audit, so no passing Java suite or coverage percentage is claimed. Research API/service classes were marked `@Ignore` in candidate history (SERVER-027). Python Sonar tests were actually executed once and passed (SERVER-030). Existing CI/Docker/Jenkins files are context; no candidate dependency-security upgrade was found in the authored patch corpus. Framework upgrades, vulnerability inventory and organization-wide CI ownership remain outside attribution. F/S separately support owned Lyra GitHub Actions publishing/releases with build, package-size, lint/type checks; that frontend/tooling scope is outside this backend source audit, not ownership of all employer infrastructure.

## Flow/status clarifications from final verification

- SERVER-001's support-aware guard is retained at HEAD; the initial blanket guard was refined. Collaborator `923d18d33b488628a1636faa743e11fcf59e2395` adds coded error/logging behavior later, so its HTTP/error details are not candidate credit.
- SERVER-003's external QR-provider URL repair is superseded by collaborator local rendering. SERVER-004's document default/fallback-font behavior survives in current `rfp-import-export/rfpio-import-services/.../ExtractCssStyleFromDocxUtil`.
- SERVER-005 has two layers: `DailyReportProcess` fetches/aggregates per-company data, including POD/internal daily-report REST requests; core `rfp-webapp/.../DailyReportService` obtains DAO/storage/project metrics for the internal response; microservice `.../daily/report/process/service/DailyReportService` produces Excel cells and persists user metrics. Missing-cell/default repairs are in the latter service, not all in the loop process. Missing/zero retention uses an existing 365-day reporting fallback in that service; the process's initialized zero is an intermediate value, not a claim that final reported retention is always zero. Company-loop isolation does not cover failures outside that loop or guarantee a complete report after partial failure.
- SERVER-006's membership endpoint/partition code is absent from this older checkout HEAD but retained in cached `origin/staging`; merged August PRs establish integration, not production rollout. Targeted API/V1 compatibility behavior is historical mainline code. Avoid describing all endpoints as current in every ref.
- SERVER-007's current projection excludes the 11 constants `ORG_PREFERENCE`, `MS_TEAMS_USER_ID`, `USER_TYPE`, `USER_MESSAGE`, `ACTIVE_TS`, `LAST_BOUNCE_EMAIL_DATE`, `LAST_ACTIVE_DATE`, `LOCK`, `ALIAS_EMAILS`, `RECENT_AGENTS`, `ADDITIONAL_MAP`. Mongo field exclusion can differ from final serialized response fields; U explicitly says 15+ is a made-up resume number; retain it with that provenance and do not reconstruct a total by adding guessed DTO fields.
- SERVER-024's current 30-record batching and configured maximum 10 threads are code limits; no achieved volume/time is asserted. SERVER-029's July feature-branch prototype is absent from inspected HEAD/cached staging/master, while the June hackathon dates/5+ demonstration remain unchanged as requested, with resume-only provenance.
- Agent persistence revisions span September–November 2025; this extends beyond the resume bullet's September 2024–September 2025 role range. Preserve commit dates alongside role provenance rather than silently revising employment dates or claiming ADK ownership.

## Inspection coverage and limitations

Coverage is the **full available attributable local inventory**, not a recent-commit or PR sample. The repository is non-shallow; all reachable refs were enumerated, author aliases were searched across history, and every candidate nonmerge patch group was classified and inspected for substantive logic. Related changes were traced through implementations, deleted/historical versions, tests, consumers and relevant blame. Combined merge diffs were checked separately; imported and repeated work does not receive blanket feature credit. Repeated template literal revisions were compared for changed conditions, variables, placeholders and markup; no rendered cross-client email QA was performed. Other authors' complete repository history was used when needed to explain before/after behavior and ownership, not exhaustively audited as the candidate's work.

| Coverage dimension | Actual scope / result |
|---|---|
| Requested period | Approximately four years through inspection date 2026-10-03; all reachable history considered, including earlier baseline code |
| All-ref repository history | 154,311 reachable commits; date extrema across author/committer metadata 2015-01-07–2026-09-22; 106,026 commits reachable with Git --since=2022-01-01 traversal |
| Candidate dates | Earliest author-or-committer inventory author date 2023-01-04T14:35:19+05:30; latest 2026-09-02T14:39:36+05:30; no matched 2022 authored work found |
| Candidate year inventory | 2023: 50; 2024: 61; 2025: 456; 2026: 26; includes author/committer matches, merge and stash records, not feature counts |
| Authorship | 589 authored records; 4 collaborator-authored candidate-committer records; 593 identity-matched records total |
| Nonmerge coverage | 270 records → 255 stable patch groups, including two stash-only groups → 253 distinct non-stash groups; 15 repeat/cherry-pick records deduplicated; 172 distinct changed paths including templates/assets/stash scaffolding |
| Merge coverage | 323 records, including one stash merge; 105 have combined-diff paths including stash. Every record inventoried; distinct substantive combined-diff changes and ownership limits investigated |
| Current/historical status | Current implementations and selected blame checked; representative-SHA HEAD ancestry recorded per patch. Ancestry is history, not proof that code survived later reverts or is deployed |
| GitHub PRs | 29 inspected: 13 opened by candidate, 16 other authors; 22 merged / 7 closed unmerged. Metadata, bodies, all file-entry pages, reviews, inline comments, issue comments and available commit pages retrieved |
| PR history dates | Inspected merged records span 2026-02-10–2026-09-03; candidate review records include 2026-02-25–2026-09-21; July prototype commits separately inspected locally |
| Authenticated identity | GitHub /user confirms sanjeev-s_rio; user confirmed all four Git emails and aliases |
| Hosting commit search | All pages retrieved for confirmed emails: rfpio 432, responsive 18, plus-rio 1, personal 3 indexed results; incomplete_results=false; no unknown SHA outside local identity inventory found. Search is indexed hosting scope, not every historical/deleted branch |
| Test verification | Java/JUnit/Mockito changes inspected; no Java suites executed. Sonar Python suite actually ran: 11 passed. No deployment/migration/benchmark performed |

The inspected local snapshot has cached `origin/HEAD`/`origin/staging` = `c01cfe575eb5edfff9a6c67d2e5760b4502ea81b`; cached `origin/master` = `018c29192551d854a55a14b62678f22f76469705`. Read-only GitHub API reports live staging `007ae1307fa79b3b91831101154f5dd705439dee`, repository pushed 2026-10-03T04:16:19Z. No fetch was performed, so the cached local refs do not include every latest remote change. Repository creation on GitHub is 2026-02-04; older Git history/Bitbucket merge references were imported, but their old hosting review/issue history is not automatically available on GitHub.

**Missing/inaccessible coverage:** U confirms Bitbucket is no longer available. A read-only Bitbucket repository API/browser check returned unavailable/not-found/login context before that clarification; no usable authenticated historical Bitbucket PR access was found, and no further Bitbucket attempt was made. Old PR numbers/branch labels below come solely from actual Git merge subjects; their true PR titles/descriptions/reviews/status/participants remain inaccessible. Jira issue API returned 404 for RES-177198; linked ticket IDs/subjects are preserved, but no private issue contents/status invented. A PR merge commit is local integration evidence, not the original hosting review record.

GitHub #9077 reports **1,270 commits**, but the PR commits REST endpoint supplies only **250** even after paging; all **1,625 file entries** were retrieved. This is an explicit 1,020-commit-list gap, not a claim to have inspected every commit in that broad PR through its API. Other inspected PR commit/file lists were retrieved to their reported totals. File patch fields can be absent/truncated for binaries/large diffs; local full diffs were used for attributable patches and relevant historical code. Complete broad collaborator PR file listings do not mean personal ownership or line-by-line inspection of unrelated systems. GitHub search is not a guarantee against unindexed/deleted PRs, commits under other identities or unavailable repositories.

Missing 2022 matched authorship does not disprove internship work. Deleted/unfetched branches, old review threads, manual changes, squashed commits under other authors, work in other repositories, migration execution, customer rollout and performance/incident logs remain incomplete. No present code absence is treated as disproving an approved resume fact. The two known friend-attributed claims and filler clarification are explicit user corrections, not conclusions from absence.

## Authenticated PR evidence register

All links below are actually inspected GitHub PRs. Titles are hosting titles; description summaries identify empty/template-only bodies and distinguish body statements from diff-derived facts. Counts are retrieved commit/file entries; merge date is hosting UTC date. Reviewer status is recorded as returned, including dismissed reviews; no substantive guidance inferred from a blank body. Merged deployment remains UNKNOWN.

| PR / actual title | Opened by | Merge status/date; merge SHA | Commits / files retrieved | Candidate review / description and attribution |
|---|---|---|---|---|
| [#306 — staging-dev conflict](https://github.com/responsive-core/rfpserver/pull/306) | preethi-singaram_rio | MERGED 2026-02-10; `3a9b26e7a00e132dcd8b69338a60d426e3b6ba5b` | 9 / 3 | none recorded; Body empty; collaborator staging/dev conflict synchronization. Involvement only; no personal implementation attribution. |
| [#946 — RES-168433 - TKT-211249: Profile Center – ASK Issues on Public Profile](https://github.com/responsive-core/rfpserver/pull/946) | santhiya-thangavel_rio | CLOSED UNMERGED | 6 / 4 | DISMISSED; Body empty; collaborator public-profile ASK repair. Candidate reviews dismissed, unmerged; SERVER-031. |
| [#1467 — Agentic qbuilder](https://github.com/responsive-core/rfpserver/pull/1467) | hari_rio | MERGED 2026-03-06; `b170119510ca3d7072247f8f4c79e6a9bf708dc2` | 5 / 10 | none recorded; Body empty; collaborator agentic query-builder work. Involvement only; no candidate implementation/review text established. |
| [#4635 — fix: RES-175211 TKT-215596 Response headers not indexed](https://github.com/responsive-core/rfpserver/pull/4635) | keerthana-s_rio | CLOSED UNMERGED | 1 / 1 | none recorded; Body empty; earlier unmerged collaborator response-header import patch. No personal implementation credit; SERVER-023. |
| [#4638 — fix: RES-175211 TKT-215596 Response headers in AI not indexed in ccl standard template file import](https://github.com/responsive-core/rfpserver/pull/4638) | keerthana-s_rio | MERGED 2026-05-11; `f8a5877bdc693752f29c54cf33f978741a5d5938` | 1 / 1 | APPROVED; Body empty; collaborator import path sets response-header VO/index metadata. Candidate approval only; SERVER-023/031. |
| [#5320 — fix: RES-177486 VULN-04: Mass PII Disclosure via User List Endpoint](https://github.com/responsive-core/rfpserver/pull/5320) | sanjeev-s_rio | CLOSED UNMERGED | 138 / 93 | none recorded; Body empty; broad 138-commit/93-file base, candidate projection is one patch; closed unmerged, later narrow PRs merged. SERVER-007. |
| [#5325 — feat: improve NPS search component in manage projects (RES-176114)](https://github.com/responsive-core/rfpserver/pull/5325) | akarshan-s_rio | MERGED 2026-05-29; `86551fe73f435e758196cce8c8cd141fd757df27` | 2 / 2 | none recorded; Body empty; collaborator NPS-search change. Involvement only; not personal implementation. |
| [#5510 — fix: RES-177486 VULN-04: Mass PII Disclosure via User List Endpoint](https://github.com/responsive-core/rfpserver/pull/5510) | sanjeev-s_rio | MERGED 2026-06-01; `8212bd2bbed9e1241d36a7fec78a0df231967e08` | 1 / 1 | none recorded; Body empty; one-file 11-field Mongo exclusion. SERVER-007. |
| [#5516 — RES-176916 - custom field is not fetching team values based on the project/intake business units](https://github.com/responsive-core/rfpserver/pull/5516) | akarshan-s_rio | MERGED 2026-05-27; `195f95f688f7d8207153ee88b477cab62c8defe9` | 1 / 1 | none recorded; Body repeats custom-field team-value/BU issue. Collaborator implementation, no candidate review text; not a personal feature. |
| [#5708 — fix: RES-177486 VULN-04: Mass PII Disclosure via User List Endpoint](https://github.com/responsive-core/rfpserver/pull/5708) | sanjeev-s_rio | MERGED 2026-06-10; `9ebb0f5dba0c8c2ba0d6b67370704c7bab18c108` | 1 / 1 | none recorded; Body empty; one-file selective projection; same patch as #5510. SERVER-007. |
| [#7074 — Elk mavericks hackfest](https://github.com/responsive-core/rfpserver/pull/7074) | elakkiya_rio | MERGED 2026-07-01; `cac47ceaa4dfc9b9ebed78c27c91aee480297f6d` | 3 / 7 | none recorded; Body empty; collaborator API-documentation authorization service/models. Involvement/requested context, no candidate-authored commits/review comments; SERVER-029. |
| [#7851 — feat: userList revamp - RES-177198](https://github.com/responsive-core/rfpserver/pull/7851) | akarshan-s_rio | CLOSED UNMERGED | 4 / 22 | none recorded; Body empty; collaborator earlier user-list branch, unmerged. Ownership baseline only; SERVER-006. |
| [#8211 — RES-177198 - userList revamp](https://github.com/responsive-core/rfpserver/pull/8211) | akarshan-s_rio | MERGED 2026-07-30; `908616d2e79ab6728cb3f7059480e978bbf393e6` | 9 / 7 | APPROVED,DISMISSED; Body: remove upfront user list; build screenshots referenced. Collaborator API/DAO/tests, candidate approved and dismissed reviews; SERVER-006/031. |
| [#8629 — Sam company user load details removal](https://github.com/responsive-core/rfpserver/pull/8629) | sanjeev-s_rio | MERGED 2026-08-06; `1059b3e00c76a55ca4f9c1bfe34f4213816cadd7` | 3 / 10 | COMMENTED; Body empty; candidate BU/directory changes plus three inline Junit comments. SERVER-006/031. |
| [#8660 — feat: userList revamp - RES-177198](https://github.com/responsive-core/rfpserver/pull/8660) | akarshan-s_rio | MERGED 2026-08-05; `25d118bfde32f5342325f49df6c9d3340f88b93d` | 1 / 2 | none recorded; Body empty; collaborator user-list revamp follow-up. Baseline/ownership comparison, no personal implementation credit; SERVER-006. |
| [#8735 — Company user load details removal](https://github.com/responsive-core/rfpserver/pull/8735) | sanjeev-s_rio | MERGED 2026-08-07; `02ac3c364ce00a717a4dc83265d0da6d65fcaa54` | 8 / 12 | none recorded; Body: on-demand metadata, role counts, BU partitions, lightweight OOO/tags/count services and tests. Mixed candidate/Akarshan ownership; SERVER-006. |
| [#8742 — Company user load details removal](https://github.com/responsive-core/rfpserver/pull/8742) | sanjeev-s_rio | MERGED 2026-08-07; `02ac3c364ce00a717a4dc83265d0da6d65fcaa54` | 10 / 12 | none recorded; Body: supersedes/dev-sync #8735; selective directory/role-count/BU membership APIs and tests. Mixed candidate/Akarshan implementation; SERVER-006. |
| [#9077 — Sam company user load details removal](https://github.com/responsive-core/rfpserver/pull/9077) | sanjeev-s_rio | MERGED 2026-08-12; `5077ecb8f06b63e38eac4759caf97baf887f032c` | 250/1270 reported / 1625 | none recorded; Body empty; broad branch sync, not 1,625 personally implemented files. SERVER-006/031. |
| [#9205 — feat: userList revamp review comments - RES-177198](https://github.com/responsive-core/rfpserver/pull/9205) | sanjeev-s_rio | MERGED 2026-08-14; `0aff1d7d74e55cf9321be58549b1c07e7bd7d777` | 1 / 1 | none recorded; Body empty; personal user-load V1/V2 review follow-up; SERVER-006. |
| [#9221 — feat: userList revamp review comments - RES-177198](https://github.com/responsive-core/rfpserver/pull/9221) | sanjeev-s_rio | MERGED 2026-08-14; `c78b1c8286507063fc98e67b7595dca595ef4292` | 1 / 1 | none recorded; Body empty; personal legacy V1 preload compatibility follow-up; SERVER-006. |
| [#9427 — RES-184750 - user-load-details API encryption ETISALAT](https://github.com/responsive-core/rfpserver/pull/9427) | akarshan-s_rio | MERGED 2026-08-19; `e498b915cf7ed6ac0ac643e7d71c15fe0edb327c` | 4 / 6 | APPROVED; Body: feature-gated AES-256-GCM V2 response, session-derived key and tenant feature migration. Collaborator implementation; candidate approval. SERVER-031. |
| [#9983 — RES-184750 etisalat userload details encryption](https://github.com/responsive-core/rfpserver/pull/9983) | akarshan-s_rio | MERGED 2026-08-31; `1d8df855d19e5d19a576cdde22c69749b4828f29` | 20 / 7 | APPROVED; Body empty; collaborator encryption/migration/tests; candidate approval. SERVER-031. |
| [#9993 — RES-184750 etisalat userload details encryption](https://github.com/responsive-core/rfpserver/pull/9993) | akarshan-s_rio | MERGED 2026-08-31; `2d1272ad69d64b4135fc74a4d9217018689660f3` | 10 / 7 | none recorded; Body empty; collaborator encrypted user-load response rollout updates. No candidate implementation/review text; SERVER-031. |
| [#10102 — arthi_dev_ofc_online into development](https://github.com/responsive-core/rfpserver/pull/10102) | sanjeev-s_rio | MERGED 2026-09-01; `e067ab1fb4409ad0d07e3f6cda28bad59ec4fc1b` | 5 / 3 | none recorded; Body empty; five implementation commits are Arthi's. Candidate opening/merge coordination only; SERVER-031. |
| [#10156 — Sam/sonarqube rfpio app coverage aggregation](https://github.com/responsive-core/rfpserver/pull/10156) | sanjeev-s_rio | CLOSED UNMERGED | 24 / 116 | none recorded; Same reporting body; broad base includes unrelated changes; closed unmerged. SERVER-030. |
| [#10163 — feat: aggregate RFPIO app coverage paths](https://github.com/responsive-core/rfpserver/pull/10163) | sanjeev-s_rio | MERGED 2026-09-03; `cf8e5386c9a6b756893bc9f098b0ea223b423607` | 1 / 6 | none recorded; Same body/implementation as #10164; separate target branch, deduplicated. SERVER-030. |
| [#10164 — feat: aggregate RFPIO app coverage paths](https://github.com/responsive-core/rfpserver/pull/10164) | sanjeev-s_rio | MERGED 2026-09-03; `4fb8c5f9d960ae0719fa0df8fb0b1f3cce3f71ef` | 1 / 6 | none recorded; Body: weighted raw counters, grouped paths, overlap filtering, partial/N/A failures and 11 tests. Personal same patch as #10163; SERVER-030. |
| [#11177 — Local Sonar scan setup for rfp-server](https://github.com/responsive-core/rfpserver/pull/11177) | akarshan-s_rio | CLOSED UNMERGED | 2 / 17 | APPROVED; Body is unfilled generic PR template. Collaborator local Docker/Sonar setup; candidate approval, unmerged. SERVER-031. |
| [#11225 — RES-188368 - local sonar scan for rfp-server](https://github.com/responsive-core/rfpserver/pull/11225) | akarshan-s_rio | CLOSED UNMERGED | 2 / 15 | DISMISSED; Body is unfilled generic PR template, not substantive design evidence. Collaborator Docker/Sonar setup; candidate dismissed review. SERVER-031. |

Candidate inline comments retrieved: #8629, three “Junit” requests on API/DAO paths. No issue comments were returned for these 29 PRs. This establishes specific review activity, not implementation of the reviewed code. Review bodies are predominantly blank; no inferred mentoring, architecture authority or measurable review outcome.

## Complete nonmerge patch inventory

Each P-ID is an audit inventory entry, not a feature count. SERVER IDs identify grouped contribution records; a patch can touch more than one initiative. Maintain existing P-IDs on future updates and append new entries rather than renumbering. Full SHA anchors allow reinspection without repeating broad discovery. “HEAD ancestor” refers to the representative SHA only; an equivalent cherry-pick can exist at HEAD even when the representative is absent. “No” does not mean reverted or never deployed. Current/superseded/reverted status is explained in the initiative narratives. Stash-only entries are explicitly excluded. HTML template/asset changes remain categorized with their actual scope.

| Patch ID | Author date | Representative commit SHA | SERVER record | HEAD ancestor | Commit subject |
|---|---|---|---|---|---|
| P001 | 2023-01-04 | `9892dc5e34642c034758623ddd7b485478b8f62d` | SERVER-010 | yes | RES-64466 - SonarQube critical issue |
| P002 | 2023-01-04 | `33df45b8de4716340f97a7951fbed057e098405e` | SERVER-010 | yes | RES-64466 - SonarQube critical issue |
| P003 | 2023-01-04 | `577c023977d00bb4b89164153769cd73132c4779` | SERVER-010 | yes | RES-64466 - SonarQube critical issue |
| P004 | 2023-01-05 | `7f45a31b6b6c18b8e68482f8960ef5e3ceceee7c` | SERVER-010 | yes | RES-64466 - SonarQube critical issue |
| P005 | 2023-01-13 | `250ff8241d1552c7708eba52d976f5cde5913746` | SERVER-011 | yes | RES-64141 |
| P006 | 2023-01-13 | `7f23f26a79e6ede29665460eee644d06a70d991c` | SERVER-011 | yes | no message |
| P007 | 2023-01-13 | `4f657344991ad9f2c3c717c90840960a79ff7d9d` | SERVER-011 | yes | no message |
| P008 | 2023-01-13 | `4c0195499399e7d873f18cff5bf500d3db4bdd06` | SERVER-011 | yes | no message |
| P009 | 2023-01-20 | `4edf6578d10c87b17a39089d9d65b33ce4bc2733` | SERVER-009 | yes | RES-54415 - Project Template - Org level Activities |
| P010 | 2023-01-20 | `5bd973cc50f0d2eb8c314ec0528466c0055d9052` | SERVER-009 | yes | no message |
| P011 | 2023-01-20 | `ccd7bb2c9c8f570e643e26e488322cb44f8b97db` | SERVER-009 | yes | no message |
| P012 | 2023-01-23 | `c217b40f2191b0b97736f8ff8964459fec49464b` | SERVER-009 | yes | RES-54415 - Project Template |
| P013 | 2023-03-09 | `9cfee9311b5c574e478191602a6a742086583ca7` | SERVER-010 | yes | RES-68430 |
| P014 | 2023-07-04 | `5809e772dec9539a8a065346f4ffa4f0cf11a9ce` | SERVER-008 | yes | feat: RES-78346 Discussion 2.O |
| P015 | 2023-07-06 | `687009919411fed44e60f6619c175d24fd58119a` | SERVER-008 | yes | feat: RES-79223 Discussion 2.O |
| P016 | 2023-07-10 | `662759d9a5620653a8ca008477c27b2ab663f9c1` | SERVER-008 | yes | feat: RES-79223 Discussion 2.O |
| P017 | 2023-07-10 | `493438f131bb0a58125c3872a0fedcb93570946e` | SERVER-008 | yes | feat: RES-79223 Discussion 2.O |
| P018 | 2023-07-10 | `bdcfae2f1bc6a74d4a195187e4c3f9a177a2446d` | SERVER-008 | yes | feat: RES-79223 Discussion 2.O |
| P019 | 2023-07-10 | `63bac24b4701d69c90e751e18fe5c6a2cfa4574c` | SERVER-008 | yes | fix: compilation error |
| P020 | 2023-07-12 | `aa6f983ea5cd48a46d9d991f5a12420f1d05dfac` | SERVER-008 | yes | fix: RES-75193 E-sign comments not shown in my work |
| P021 | 2023-08-22 | `0b5c3b539a9be38e9bef957d84ccf903a3e6bde3` | SERVER-013 | yes | fix: RES-83234  Bulk Send numeric label values are displayed with a suffix |
| P022 | 2023-09-14 | `7bb75bc73338726caac1b9fc8a3170b0644be40d` | SERVER-012 | yes | feat: RES-83750 Session and BYOK |
| P023 | 2023-09-14 | `04efe416d91987304a516c4a429a6b3fc0eb56f6` | SERVER-012 | no | feat: RES-83750 Session and BYOK |
| P024 | 2023-11-10 | `d35404a9d9afa878aa7fd7de958795482b0aa1f0` | SERVER-001 | no | fix: RES-91611 user able to take over super admin account using proxy |
| P025 | 2023-11-14 | `407a126c5e549a58e3183fa27002121de58c65e4` | SERVER-001 | yes | fix: RES-91611 Super admin account takeover bug fix |
| P026 | 2023-12-19 | `a9860a8160d57bca2353fddde12fbf967db4af0c` | SERVER-004 | yes | fix: RES-89107 default font support in uploading Custom styles in org settings. |
| P027 | 2023-12-20 | `0d85eeac073f3401b59d77d3a80bb4d3bbc68479` | SERVER-004 | yes | fix: RES-89107 default font support in uploading Custom styles in org settings. |
| P028 | 2024-02-06 | `7ffa04162c4debc789d3471f3bd36448424ca154` | SERVER-002 | yes | feat: RES-98484 Org Settings - 2.0 UX - User Management - Add user |
| P029 | 2024-02-06 | `f1319a22739e4511b9e4d881da11cddaf69098d1` | SERVER-002 | yes | feat: RES-98484 Org Settings - 2.0 UX - User Management - Add user(Single) |
| P030 | 2024-02-06 | `6baa7ae623fee2377dd5b9c6468905cb3a990aee` | SERVER-002 | yes | feat: RES-98484 Org Settings - 2.0 UX - User Management - Add user(Single) |
| P031 | 2024-02-12 | `6a9d824add9f92bb67f3b3702c50fa9c19c34ea1` | SERVER-002 | yes | feat: RES-96960 - 2.0 UX - Org Settings - User Management - Add user(Multi user) |
| P032 | 2024-02-12 | `8745851ce8d0a821f406810f6386077670ad7da1` | SERVER-002 | yes | feat: RES-96960 - 2.0 UX - Org Settings - User Management - Add user(Multi user) |
| P033 | 2024-02-20 | `5ccf6777a963b19c2dba9892b8656397b9f3d2c9` | SERVER-002 | yes | fix: RES-99980 Org V2 - Add Multi User bugs |
| P034 | 2024-04-08 | `e5c616ec749cae0be35e56da9cea583c175abe21` | SERVER-003 | no | fix: RES-107284 QR code generator bug fix |
| P035 | 2024-04-08 | `65b070c37e924b507e317083aeb529659273bf43` | SERVER-003 | no | fix: RES-107284 QR code generator bug fix |
| P036 | 2024-08-12 | `58e68763c40bf74356fb883b71891356fd70dffa` | SERVER-014 | yes | fix: RES-119487 - For a new company, security - error messgae shouldn't be shown |
| P037 | 2024-09-16 | `3794cedeb2784749d117c2e91fe6d04ca3ffe0d7` | SERVER-008 | no | perf: RES-120063 - My Work - Performance Improvement |
| P038 | 2024-10-15 | `02ae4165d59dc5e3677d4fe244a00541177fbb14` | SERVER-016 | yes | feat: RES-125859 - Email redirection from V1 to V2 (Phase IV) |
| P039 | 2024-10-15 | `0e23df91f1b41a61c4ef5dc8150bdcf8b4367f38` | SERVER-016 | yes | feat: RES-122166 - 2.0 UX - Package & Billing Unit Test |
| P040 | 2024-11-04 | `1f644c1add7513cf280a6a702f8cbf7209bb13cc` | SERVER-035 | yes | fix: RES-125844 Deleting CCL Date and Time CFs |
| P041 | 2024-11-05 | `e1ebd62e7b301c49c6cccffff090788a4dd48b8c` | SERVER-014 | yes | fix: RES-128273 - Unable to sign into community (GovCloud) |
| P042 | 2024-11-06 | `3e0e802257f8762c76330fa8b90b616dade72c0b` | SERVER-014 | yes | fix: RES-127850 Reset password email not received by the user |
| P043 | 2024-11-06 | `daaf7055008953ec3aab195b9c485de5b31ccd8e` | SERVER-014 | yes | fix: RES-127850 Reset password email not received by the user |
| P044 | 2024-11-06 | `3dee6ea65a0fa51bef5d2e456a2f7440d3970781` | SERVER-014 | yes | fix: RES-127850 Reset password email not received by the user |
| P045 | 2024-11-13 | `a1093db9d16d050f4060c9475798ccb1ebe7ec69` | SERVER-015 | yes | perf: RES-128400 - Activities revamp |
| P046 | 2024-11-13 | `31e6adc024cebcb4aa1e9d84f933b5bbbf12426b` | SERVER-015 | yes | perf: RES-128400 - Activities revamp |
| P047 | 2024-11-13 | `005370990fa3c59bd75e8eb94a8114f9143433e8` | SERVER-015 | yes | perf: RES-128400 - Activities revamp |
| P048 | 2024-12-17 | `5c341643336379bc1c8798738db60b91f4d5c155` | SERVER-016 | yes | feat: RES-130235 - 2.0 UX - Email Template - Section Bulk Submit for Review |
| P049 | 2024-12-18 | `ed3ec552387f148443b786124934eea64a3f40b1` | SERVER-018 | yes | feat: RES-130235 - 2.0 UX - Email Template - Section Bulk Submit for Review |
| P050 | 2024-12-18 | `540bd8c89cfccbe2dd6b29dfe1df4a7136a3b095` | SERVER-018 | yes | feat: RES-130235 - 2.0 UX - Email Template - Section Bulk Submit for Review |
| P051 | 2024-12-18 | `025648312c368f49bbaded2768b2bc792031b78e` | SERVER-018 | yes | feat: RES-130235 - 2.0 UX - Email Template - Section Bulk Submit for Review |
| P052 | 2024-12-19 | `d095cabb708520552fddc5103c1476fa0c2cc1e9` | SERVER-018 | yes | feat: RES-130235 - 2.0 UX - Email Template - Section Bulk Submit for Review |
| P053 | 2024-12-20 | `66bcb062709d0ec27d72c7dd39753a8362ebd5ac` | SERVER-016 | yes | fix: RES-132954 - Project Guest share response v1 redirection |
| P054 | 2025-01-08 | `6237e5ca2f0a4e59d1223b29953a768a02f1dd80` | SERVER-018 | yes | fix: RES-132459 - Email Redirection 2.0 |
| P055 | 2025-01-08 | `8763458c28597a6ce9f2ef9e5cdce55c7dd36a21` | SERVER-018 | yes | fix: RES-132459 - Email Redirection 2.0 Test |
| P056 | 2025-01-09 | `b1fb50859130819a3ae8c6a1a4ea9d24a4b5574f` | SERVER-018 | no | mainTemplateV2.vm edited online with Bitbucket |
| P057 | 2025-01-09 | `0b2ba87673f92e9587de6b95ae6329aaf79b8d03` | SERVER-017 | yes | feat: RES-133744 - Dedicated DB email template migration |
| P058 | 2025-01-09 | `bff64f682ba7b20003a8dcb54ff3ee73ba3d4f99` | SERVER-017 | yes | feat: RES-133744 - Dedicated DB email template migration |
| P059 | 2025-01-10 | `8557d90521eef8833abafb040f12bfd252247038` | SERVER-017 | yes | feat: RES-133744 - Dedicated DB email template migration |
| P060 | 2025-01-10 | `0a2817444fb40793f356d4049f9a2ab45774fe0f` | SERVER-017 | yes | feat: RES-133744 - Dedicated DB email template migration |
| P061 | 2025-01-13 | `4ab7cf731d9c64a47c1bbfca1ad938e2c87d5de5` | SERVER-017 | yes | feat: RES-133744 - Dedicated DB email template migration |
| P062 | 2025-01-13 | `78022970030ab0e6070edf6b934027172f984ae0` | SERVER-017 | yes | feat: RES-133744 - Email Redirection 2.0 |
| P063 | 2025-01-17 | `b3dd26fdadcb06cd73914b2ed19f9f819b533d75` | SERVER-016 | yes | ProjectNotificationBuilder.java edited online with Bitbucket |
| P064 | 2025-01-22 | `ef97ed4da3aae1ac56f555c5536606c0afbcbafc` | SERVER-017 | yes | feat: RES-133748 - Overall all Edited mail templates content migration |
| P065 | 2025-01-22 | `146485545817958e4c59f6bc2e17319e82997816` | SERVER-017 | yes | feat: RES-133748 - Overall all Edited mail templates content migration |
| P066 | 2025-01-22 | `82b74a8564dd221ef5e20f1a4326d434c558e87f` | SERVER-017 | yes | feat: RES-133748 - Overall all Edited mail templates content migration |
| P067 | 2025-01-22 | `09af44e1cf827ee957cfa959fe4b0b0bd026f08e` | SERVER-017 | yes | feat: RES-133748 - Overall all Edited mail templates content migration |
| P068 | 2025-01-23 | `3a112610e9cfeeaeea8c2196134f0a1707b9cc2f` | SERVER-017 | yes | feat: RES-133748 - Overall all Edited mail templates content migration |
| P069 | 2025-01-23 | `cb493b9a00d780c560b5eb2afb4d89b1ca432a7f` | SERVER-017 | yes | feat: RES-133748 - Overall all Edited mail templates content migration |
| P070 | 2025-01-30 | `a0fd2a3ebfa8ac4861246bfa72c1035dae714704` | SERVER-017, SERVER-018 | yes | feat: RES-135369 - Gmail client issues |
| P071 | 2025-01-30 | `4f791539e06125fca077906c787aacba80fb8f46` | SERVER-017, SERVER-018 | yes | feat: RES-135369 - Gmail client issues |
| P072 | 2025-02-04 | `9fc0b2ff37c32c34c1f1bb869870748d8abdc639` | SERVER-019 | yes | feat: RES-134791 - Email Template Source gainsight tracking |
| P073 | 2025-02-04 | `5d08f27fb6d3db9a2c19f6cd6dcc02ab2a341899` | SERVER-019 | yes | feat: RES-134791 - Email Template Source gainsight tracking |
| P074 | 2025-02-04 | `448fc9702c4ae73435b4937babb763539880b4b1` | SERVER-019 | yes | feat: RES-134791 - Email Template Source gainsight tracking |
| P075 | 2025-02-05 | `1b4edfda49cb8a87d5e8ddb9c1d3c55c4e97ea65` | SERVER-018 | yes | french.js edited online with Bitbucket |
| P076 | 2025-02-05 | `29074df197bd9617e85d9db78b66b4c2c461ac9a` | SERVER-018 | yes | french.js edited online with Bitbucket |
| P077 | 2025-02-05 | `6a20a4981d30e722b81b3e42d15d453742446c03` | SERVER-016, SERVER-017 | yes | feat: RES-134351 - 2.0 UX - Email Template - Create Project |
| P078 | 2025-02-06 | `1a7d315eb80f0f8224f67857a50f6ee562e054b7` | SERVER-019 | yes | fix: RES-136840 - Unwrapped Emails Alignment Issue |
| P079 | 2025-02-06 | `466a263a8a58a2752ae67704f5412c6c04bc4ea8` | SERVER-017 | yes | feat: RES-134351 - 2.0 UX - Email Template - Create Project |
| P080 | 2025-02-24 | `664abd710ef7e018ad7bd66d73e65bf8b00ef72d` | SERVER-020 | yes | Added Loggers |
| P081 | 2025-02-28 | `39f89db67957fa507b3147b01bb81584c881708c` | SERVER-020 | yes | ExternalRequestInterceptors.java edited online with Bitbucket |
| P082 | 2025-03-07 | `6b7c128cfeb2e2bdd402ce8feae7437cb5859282` | SERVER-020 | yes | fix: Added Loggers for debugging purposes |
| P083 | 2025-03-07 | `3a36580c367f76f2a6892561898d3ea4523f7544` | SERVER-020 | yes | fix: Added Loggers for debugging purposes |
| P084 | 2025-03-11 | `8189b150655c15d015ecf1e8b873dd8cc46ec552` | SERVER-017 | yes | fix: Email Template review comments |
| P085 | 2025-03-12 | `8e42699cea42ec6b37b23894b6e7f1ee96cde7c4` | SERVER-017 | yes | fix: RES-140131 - Issue while migrating textnodes |
| P086 | 2025-03-13 | `e86135797c0dd33b81e7e0b5e2575f9be1f62f92` | SERVER-017 | yes | fix: RES-140131 - Issue while migrating textnodes |
| P087 | 2025-03-13 | `8222c0e1e5f7bf8fbcf799ae91492997d6bd9c2c` | SERVER-017 | yes | fix: RES-140131 - Issue while migrating textnodes |
| P088 | 2025-03-13 | `5bb6ff1fc69f5506dc30d8e696be8446a23d043a` | SERVER-017 | yes | fix: RES-140131 - Issue while migrating textnodes |
| P089 | 2025-03-14 | `59f115cbc9202399c9ac23686f1b2a03592465d7` | SERVER-018 | yes | fix: RES-140432 - Mail visibility Issue |
| P090 | 2025-03-14 | `f68df62626c872800a9efa632f1d3558ba3a4810` | SERVER-018 | yes | fix: RES-140432 - Mail visibility Issue |
| P091 | 2025-03-24 | `f7b7a54de047aeb09a8879828b52f737e2370c49` | SERVER-016, SERVER-018 | yes | feat: RES-139212 - 2.0 UX - Email Templates - Intake Comment Mention |
| P092 | 2025-03-25 | `0a4ecfd66bdbb3529af89db8620cd69d9b8a2364` | SERVER-016, SERVER-018 | yes | feat: RES-139212 - 2.0 UX - Email Templates - Intake Comment Mention |
| P093 | 2025-03-27 | `b5c28c823ad6b33ba1fb459ac25bd5d15f470149` | SERVER-016, SERVER-018 | yes | feat: RES-139184 - 2.0 UX - Email Templates - Project Notes Comment Mentions |
| P094 | 2025-03-27 | `883f592054a9cdb9b256dc28d807ca8f2ed8032a` | SERVER-016, SERVER-018 | yes | feat: RES-139184 - 2.0 UX - Email Templates - Project Notes Comment Mentions |
| P095 | 2025-04-02 | `2e20dfdb51c8dda9690d23bf72d8b6760f626fed` | SERVER-016, SERVER-018 | yes | feat: RES-139183 - 2.0 UX - Email Templates - Project Notes Comment Followup |
| P096 | 2025-04-02 | `3852e0f7c96459d71186f27a0e92979a5c9429b6` | SERVER-016, SERVER-018 | yes | feat: RES-139183 - 2.0 UX - Email Templates - Project Notes Comment Followup |
| P097 | 2025-04-03 | `c768536de199fb5597d0b44de2af34e77e09c469` | SERVER-017 | yes | fix: revert for devtest deployment |
| P098 | 2025-04-03 | `4df4b7e12b0df02b31283eb414065d5a02812bb9` | SERVER-018 | yes | fix: RES-142568 - Outlook Email css bug fix |
| P099 | 2025-04-03 | `6046abbb7abd0c9f2fca25729bd959b67b7dbe2b` | SERVER-018 | yes | fix: RES-142568 - Outlook Email css bug fix |
| P100 | 2025-04-16 | `dee9d6994af51b7d8e222d95cc3a088f3ecd7026` | SERVER-018 | yes | fix: RES-142470 - Outlook Rendering issue |
| P101 | 2025-04-16 | `f97a09ad73bd542a03a8f1ac2195c1e91da49f14` | SERVER-018 | yes | fix: RES-142470 - Outlook Rendering issue |
| P102 | 2025-04-16 | `a147924afa6eb928bf9f58961a694aa7d3d47dd0` | SERVER-018 | yes | fix: RES-142470 - Outlook Rendering issue |
| P103 | 2025-04-21 | `930281c229a49aa7ce21ec32a86479326ac8b452` | SERVER-018 | yes | fix: RES-142470 - Outlook Rendering issue |
| P104 | 2025-04-22 | `ccc675bf09c2947252e6557623e5360b357acb25` | SERVER-018 | yes | fix: RES-142470 - Outlook Rendering issue |
| P105 | 2025-04-22 | `0d1f7bca5327899e37e151da30f79e1310d70468` | SERVER-018 | yes | fix: RES-142470 - Outlook Rendering issue |
| P106 | 2025-04-22 | `5010bf48eadc6c1f46008d118982824eb8aa4e10` | SERVER-018 | yes | fix: RES-142470 - Outlook Rendering issue |
| P107 | 2025-04-22 | `eeb01a4467948a2095da05f88f5e0a58c7d9d475` | SERVER-018 | yes | fix: RES-142470 - Outlook Rendering issue |
| P108 | 2025-04-22 | `59ceba21f02cf97a08030be4b99f14b4a3b964bc` | SERVER-018 | yes | fix: RES-142470 - Outlook Rendering issue |
| P109 | 2025-04-22 | `ad460d697ba1a70e52c66f72b477937c6b30f125` | SERVER-017 | yes | fix: RES-144199 - mailTemplateMigrationV2Process batch processes in PENDING state |
| P110 | 2025-04-25 | `679468d097b59cfe979bf29850fd1796ed221a37` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P111 | 2025-04-28 | `5377ec5433c765e5ec2077680fc367406ae4a38c` | SERVER-018 | yes | mainTemplateV2.vm edited online with Bitbucket |
| P112 | 2025-04-28 | `3185676f049f465f2861d01b8b2bd9e03821a4a9` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P113 | 2025-04-28 | `6580b4636ca79e111dc1fd2e804c3a97da1b762d` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P114 | 2025-04-28 | `262caf9c7aeac157a48c23c1f9ae592c312de446` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P115 | 2025-04-28 | `fea662146f2600fc6a68ec4d491e0ac4fbe70499` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P116 | 2025-04-28 | `61415865a96c9182c811356a0c41515e9232436b` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P117 | 2025-04-28 | `9d5079174f41fd108717c3476a36a8b08dee67ad` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P118 | 2025-04-29 | `eb12a0743cdfbfa5bd9f8c3115634f36748de95c` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P119 | 2025-04-29 | `122da2a4f04f3da8df7b232cebc01bf9ade97a98` | SERVER-005 | yes | fix: RES-144932 - Daily report Exception Handling |
| P120 | 2025-04-29 | `5183d9b6d30c8b8725403561f592ef5ff70785fb` | SERVER-005 | yes | fix: RES-144932 - Daily report Exception Handling |
| P121 | 2025-04-29 | `3be2e2ec8a592db82637f49836595c36d965b579` | SERVER-005 | yes | fix: RES-144932 - Daily report Exception Handling |
| P122 | 2025-04-29 | `2d97089505635029c1550666a0144ab662545178` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P123 | 2025-04-30 | `6a2b3916d5fd37f4dd6b058cfd37126bb554f6ca` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P124 | 2025-04-30 | `88caf2d2a9bf07597fa0002476c2c1c7d0558fa6` | SERVER-018 | no | fix: RES-144083 - Formatting issues in Outlook |
| P125 | 2025-05-02 | `115b9927a3f457b438a136aae83245576bb1568e` | SERVER-018 | no | fix: RES-144083 - Formatting issues in Outlook |
| P126 | 2025-05-02 | `c500f32473aacbb16a8eb6893cf3602047386a90` | SERVER-018 | no | fix: RES-144083 - Formatting issues in Outlook |
| P127 | 2025-05-05 | `78491597c42a5c29d9f6038b8dd31c9bed0d4913` | SERVER-018 | no | fix: RES-144083 - Formatting issues in Outlook |
| P128 | 2025-05-05 | `e629aa4235b8bd275b04261ccb0a8d03c78d5d43` | SERVER-018 | no | fix: RES-144083 - Formatting issues in Outlook |
| P129 | 2025-05-05 | `32104cce07c82abe6ad42e98415718773792945d` | SERVER-018 | no | fix: RES-144083 - Formatting issues in Outlook |
| P130 | 2025-05-05 | `8aa72deef153b406ec2773135086bdc509a685d7` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P131 | 2025-05-06 | `32409d1885b839487ba960b323592c112a88d2f7` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P132 | 2025-05-06 | `3110b8527b48e8f0627ebd4f02d365dbeff21e97` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P133 | 2025-05-06 | `8753a31c4f7504a43e34bd5cb11ba08c81c3bc5e` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P134 | 2025-05-07 | `0be642ff0e59de2ff3d8d0df192b8ec1e82b1179` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P135 | 2025-05-08 | `83501cf1defc1611527d4e528e9af6c0e6975706` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P136 | 2025-05-08 | `e8107f8e8261973c15576124a5dfb2b4b491c911` | SERVER-018 | yes | fix: RES-144083 - Formatting issues in Outlook |
| P137 | 2025-05-08 | `c87408f73744635bc8c74df971f071b0faf4ce3c` | SERVER-020 | no | fix: added loggers |
| P138 | 2025-05-08 | `814d35f090b215a7ef007f2bfe09d0dd31e56b6e` | SERVER-020 | yes | fix: added loggers |
| P139 | 2025-05-08 | `cf45c19545cb4e57fac09948ab3e4dfd141898ba` | SERVER-022 | yes | fix: RES-144011 Unable to save sharepoint details |
| P140 | 2025-05-08 | `d16791867e0d713bc8bbc343358ead7c19c5959a` | SERVER-022 | yes | fix: RES-144011 Unable to save sharepoint details |
| P141 | 2025-05-20 | `53b0d8fc609ac06e1de9b64f09c2708e4ab62af1` | SERVER-021 | yes | fix: RES-144565 - Slack Markdown formats search issue |
| P142 | 2025-05-20 | `4ac6f0cbd34b2a9dd0d539b298ce3b52993dc7ff` | SERVER-021 | yes | fix: RES-144565 - Slack Markdown formats search issue |
| P143 | 2025-05-20 | `f0c26e6afc32bb5aa1b75ee97d0dbc1034958ba0` | SERVER-021 | yes | fix: RES-144565 - Slack Markdown formats search issue |
| P144 | 2025-05-20 | `2b6cdec2525d4928d8fe0cdf38ff62e3e6106851` | SERVER-021 | yes | fix: RES-144565 - Slack Markdown formats search issue |
| P145 | 2025-05-21 | `cdc068e48a6750ae9ac2a8635018142ab48dcf16` | SERVER-016, SERVER-022 | yes | fix: RES-146686, RES-146638 - e2e bugs |
| P146 | 2025-05-22 | `3edd81e639b6ddbeaacd795ab23bcdc2354debf1` | SERVER-016, SERVER-018 | yes | fix: RES-144968, RES-144968 e2e bugs |
| P147 | 2025-05-22 | `b7b7b76fd663fcf0b1275ca87ba3506b2aa56c00` | SERVER-016, SERVER-018 | yes | fix: RES-144968, RES-144968 e2e bugs |
| P148 | 2025-05-26 | `f5df349c166b56ab8b7223c2080ab059b5f66dc5` | SERVER-022 | yes | fix: RES-144802 - Sharepoint search does not pull in the right document. |
| P149 | 2025-05-29 | `d7b75c2300cdfb3f7b662b2a9726bc8fd0c388f3` | SERVER-005, SERVER-017 | yes | fix: RES-145860, RES-146683, RES-146735 backlog bugs |
| P150 | 2025-06-04 | `b8ee06bc230e2ea38282a48af00a0a649d7fd7f1` | SERVER-023 | no | feat: RES-147803 - Include Response header in Mongo db and solar index |
| P151 | 2025-06-09 | `d4ac4a75a6da2176d853aa5495384c567ab951e0` | SERVER-023 | no | feat: RES-147803 - Include Response header in Mongo db and solar index |
| P152 | 2025-06-12 | `a86c22f242eb81a26efe53db028f31f40be6003d` | SERVER-023 | no | feat: RES-147812 - Search embeddings based on response header |
| P153 | 2025-06-13 | `3c3d2429bdbcd3227e4e8f4755746e30664a9c13` | SERVER-023 | no | feat: RES-147812 - Search embeddings based on response header |
| P154 | 2025-06-14 | `ee55fbd1cd59b300b45adb2f5c57526e2c3db388` | SERVER-023 | no | feat: RES-147812 - Search embeddings based on response header |
| P155 | 2025-06-15 | `25918330c6aba59a1bf752cc35e70017ca9f3a20` | SERVER-023 | no | feat: RES-147812 - Search embeddings based on response header |
| P156 | 2025-06-16 | `15655e082556f09787714b6984402b64b2351163` | SERVER-023 | no | feat: RES-147812 - Search embeddings based on response header |
| P157 | 2025-06-16 | `8574f4291e44e9d7be4051656426427711ad9adc` | SERVER-023 | no | feat: RES-147812 - Search embeddings based on response header |
| P158 | 2025-06-17 | `bc80269f862b864e391724f769b0032a988e668f` | SERVER-023 | no | feat: RES-147812 - Search embeddings based on response header |
| P159 | 2025-06-17 | `217c4f9c169aed172d55807e7a7320e97e2a5b1e` | SERVER-023 | no | feat: RES-147812 - Search embeddings based on response header |
| P160 | 2025-06-19 | `bc3958b119519601fd5374d2f4a0e1117ad14d63` | SERVER-023 | no | fix: RES-149361 - AI response header bug fix |
| P161 | 2025-06-19 | `b100f3eac5af19d503bc3721935b424fafaa20db` | SERVER-023, SERVER-024 | no | fix: RES-149361 - AI response header bug fix |
| P162 | 2025-06-19 | `e197183bc1e5f2e42dda21c7a7518ad6bc249c2c` | SERVER-023 | yes | fix: RES-149361 - AI response header |
| P163 | 2025-06-19 | `22964112abb293e453cb46c67dbd281345553490` | SERVER-023, SERVER-024 | yes | fix: RES-149361 - AI response header |
| P164 | 2025-06-19 | `97af6693cd37ceec3d1680c338aec32b205977db` | SERVER-023, SERVER-024 | yes | fix: RES-149361 - AI response header |
| P165 | 2025-06-19 | `5448308a68fb9899382f33e18bd6b6d96568275d` | SERVER-023 | yes | fix: RES-149361 - AI response header |
| P166 | 2025-06-19 | `9428880d3c4d70865412118b83e5a7ce518a8b3c` | SERVER-023 | no | fix: RES-149361 - AI response header |
| P167 | 2025-06-19 | `5289aab55e5347da10ff54a08ca1643e68b648f3` | SERVER-023 | yes | fix: RES-149361 - AI response header |
| P168 | 2025-06-20 | `54eae5a2736643e5e3d5b9868391b9f911f7820b` | SERVER-023 | yes | fix: RES-149361 - AI response header |
| P169 | 2025-06-20 | `43f7c0f087441a812ec601085044967c414cca35` | SERVER-023 | yes | fix: RES-149361 - AI response header |
| P170 | 2025-06-20 | `f74a73e0373dd8cc3e2e071543cad51ab798ed6c` | SERVER-023 | yes | fix: RES-149361 - AI response header |
| P171 | 2025-06-20 | `649cb1f3922b4e09a3836092404bf0987412330d` | SERVER-023 | yes | fix: RES-149361 - AI response header |
| P172 | 2025-06-20 | `cee376ec8f082fd0198a0bcd8b7fc7176b9d5504` | SERVER-023 | yes | fix: RES-149361 - AI response header |
| P173 | 2025-06-25 | `f99870dcb27f53b42de91b495ee5451222c8eb46` | SERVER-023 | yes | feat: RES-147807 - AI response header |
| P174 | 2025-06-25 | `8fa270db702e51b623cae347cab2eebbbe8d1360` | SERVER-023, SERVER-024 | yes | feat: RES-147807 - AI response header |
| P175 | 2025-06-25 | `89d55496bc895c5eca427a3205f33a668cb1b58c` | SERVER-023, SERVER-024 | yes | feat: RES-147807 - AI response header |
| P176 | 2025-06-25 | `6fabb50fd7956b9e4647e090c5f3e37aec170934` | SERVER-023, SERVER-024 | yes | feat: RES-147807 - AI response header |
| P177 | 2025-06-25 | `db62d8a64e49e0ac094cb1c5e7c326c19dae46a8` | SERVER-023, SERVER-024 | yes | feat: RES-147807 - AI response header |
| P178 | 2025-06-25 | `8d5cfb1f283e3123a959e2bf8cb229c6e1bd3e1a` | SERVER-035 | yes | feat: RES-148953 - SMB Feedback |
| P179 | 2025-06-30 | `94377985324ed45f1eac92c3e3343d4630ffaa3c` | SERVER-023 | yes | fix: RES-150279 - Response header granular api bug fix |
| P180 | 2025-06-30 | `1d579df8cc7ae524925e72c4fa2259a827fcc472` | SERVER-005 | yes | fix: RES-150398 - Daily report process logger |
| P181 | 2025-06-30 | `6a6a9c09aff256535ca737e79ca022f7c871cb68` | SERVER-005 | yes | fix: RES-150398 - Daily report process error handling |
| P182 | 2025-06-30 | `67a45bd4a8225d3f1a2fcecfd7d32594bf07d6a6` | SERVER-005 | yes | fix: RES-150398 - Daily report process error handling |
| P183 | 2025-06-30 | `f92f21337ad10491414f7c8b347d3bbe7f04562f` | SERVER-005 | yes | fix: RES-150398 - Daily report process error handling |
| P184 | 2025-07-02 | `b18396600a3dff0b68bdecfeea4cfe1c32054e5c` | SERVER-025 | yes | feat: RES-150714 - Support Portal Pod name handling |
| P185 | 2025-07-02 | `e5d0dd4eee73e9ea05622a249a79040b3297f5e7` | SERVER-025 | yes | feat: RES-150714 - Support Portal Pod name handling |
| P186 | 2025-07-06 | `9f93b5edc7936ae96da43da41b26d4be304a84f3` | SERVER-005, SERVER-025 | yes | fix: RES-150398 - Daily report process error handling |
| P187 | 2025-07-06 | `4243eaf01e848b0761387e37cba4f62159b702d7` | SERVER-005 | yes | fix: RES-150398 - Daily report process error handling |
| P188 | 2025-07-06 | `01eef5ff089664552136febc44e48ccd3974d81a` | SERVER-005 | yes | fix: RES-150398 - Daily report process error handling |
| P189 | 2025-07-16 | `d505b5205c0ec79f4b3a62e1d0c437b1d6275485` | SERVER-024 | yes | feat: RES-151073 - Overall Response Header Index Migration |
| P190 | 2025-07-17 | `1a86be431c570805035c5723a91ccb4ef16b4442` | SERVER-024 | yes | feat: RES-151073 - Overall Response Header Index Migration |
| P191 | 2025-07-17 | `d875c3b2050d7600d6af15a7fb4bcaf53a3004e3` | SERVER-024 | yes | feat: RES-151073 - Overall Response Header Index Migration |
| P192 | 2025-07-17 | `7f36c8e7227ea3c0815074541be27e8876021d2a` | SERVER-024 | yes | feat: RES-151073 - Overall Response Header Index Migration |
| P193 | 2025-07-17 | `93c9d36543de5a1a206f6c0a17c5963f3ba06f83` | SERVER-024 | yes | feat: RES-151073 - Overall Response Header Index Migration |
| P194 | 2025-07-17 | `299a3d8adec3b50c27da5ae6d9d727fb1def1352` | SERVER-024 | yes | feat: RES-151077 - Solr Bulk Update Indexing |
| P195 | 2025-07-17 | `f10aa39b24cbb26e48db442a494c465584747cbf` | SERVER-024 | yes | feat: RES-151077 - Solr Bulk Update Indexing |
| P196 | 2025-07-18 | `638b640442e36b6c8e03172c91515d84da142b84` | SERVER-024 | yes | feat: RES-151077 - Solr Bulk Update Indexing |
| P197 | 2025-07-18 | `bcd5a5fae6a31446bb05c54a1cea1e0b1c0e0c4a` | SERVER-024 | yes | feat: RES-151077 - Solr Bulk Update Indexing |
| P198 | 2025-07-18 | `dad02f1b1ba395963d2594892a06e756ba0daf29` | SERVER-024 | yes | feat: RES-151077 - Solr Bulk Update Indexing |
| P199 | 2025-07-22 | `a38e5d80a6394a010ff99222ca95de3f7cee2f9c` | SERVER-024 | yes | feat: RES-151073 - Overall Response Header Index Migration |
| P200 | 2025-07-22 | `2828561572067da4c50f3db5a7e4128f10c416a0` | SERVER-024 | yes | feat: RES-151073 - Overall Response Header Index Migration |
| P201 | 2025-07-23 | `fef7ad7e8dc7aec674bd899ef54f7cab034dd017` | SERVER-024 | yes | feat: RES-151073 - Overall Response Header Index Migration |
| P202 | 2025-07-28 | `bd03ec6f6e17058adff10e8102fb3dcbf62cec12` | SERVER-024 | yes | feat: RES-151073 - Overall Response Header Index Migration |
| P203 | 2025-08-05 | `4ee7412e44b301854f2f8937256e22c75809601d` | SERVER-026 | yes | feat: RES-152665 - POC for deepl no translate implementation |
| P204 | 2025-08-05 | `5d47ac80bbb2a40b780f94c2ee12a6d5a17f51ed` | SERVER-026 | yes | feat: RES-152665 - POC for deepl no translate implementation |
| P205 | 2025-08-06 | `5845db76502f91e51116ea18a8eb1b676d3f64a1` | SERVER-026 | yes | feat: RES-152665 - POC for deepl no translate implementation |
| P206 | 2025-08-06 | `4acfd2914595e0dd00b73cd5703aa10265b28e29` | SERVER-026 | yes | feat: RES-152665 - POC for deepl no translate implementation |
| P207 | 2025-08-08 | `1af68435b9f8e7b866191524c54a41a19e27b207` | SERVER-026 | yes | feat: RES-152665 - POC for deepl no translate implementation |
| P208 | 2025-08-08 | `1221cb3aee129db04b4031149a579a7bb905ba63` | SERVER-026 | yes | feat: RES-152665 - POC for deepl no translate implementation |
| P209 | 2025-08-08 | `cd07e04973bfa229e5b19b2b9eb7f0afd7822d30` | SERVER-026 | yes | feat: RES-152665 - POC for deepl no translate implementation |
| P210 | 2025-08-11 | `e372f47613f5bef6e9d48f9aa04b9f8eb4a0b1bf` | SERVER-026 | yes | feat: RES-152665 - POC for deepl no translate implementation |
| P211 | 2025-08-12 | `32e1dbfc981de08047807296cc4a63ca0bc03661` | SERVER-026 | yes | fix: RES-154045 - Org glossaries bug fix |
| P212 | 2025-08-13 | `ecd85254e5805d4a79fe4c176ef337afd13f23c0` | SERVER-026 | yes | fix: RES-154045 - Org glossaries bug fix |
| P213 | 2025-08-21 | `5547f1fd589daed7d598d9b7fb589d6663bc6a1d` | SERVER-022 | yes | Prod error : company-integrations/edit |
| P214 | 2025-08-21 | `3225f12d24999c63df21fdd1090e2a3cc7822ee1` | SERVER-022 | yes | Prod error : company-integrations/edit |
| P215 | 2025-08-21 | `45309a298a196fd9c0196204076ca5fadca051d6` | SERVER-022 | yes | Prod error : company-integrations/edit |
| P216 | 2025-08-22 | `ddcbdad7ba577605bacdcf5a6af054f8a8c1b683` | SERVER-026 | yes | fix: RES-155154 - translate glossary 503 error |
| P217 | 2025-09-01 | `fb9bf847e68fc484dfbcefd5526f59c83dd1cd5b` | SERVER-017, SERVER-018 | yes | feat: RES-153742 - Overall Individual Migration of Email Templates to 2.0 |
| P218 | 2025-09-05 | `a5cfbed836f0ad5e399f9ebca5fbb454bbe13006` | SERVER-017, SERVER-018 | yes | feat: RES-153742 - Overall Individual Migration of Email Templates to 2.0 |
| P219 | 2025-09-10 | `b8d728bc0399f20e2c62191598263c9c6af4dda2` | SERVER-017, SERVER-018 | yes | feat: RES-153742 - Overall Individual Migration of Email Templates to 2.0 |
| P220 | 2025-09-10 | `9a1a987b6f551cc2ac617c79d808bcd9a34c94ba` | SERVER-017, SERVER-018 | yes | feat: RES-153742 - Overall Individual Migration of Email Templates to 2.0 |
| P221 | 2025-09-10 | `a33452e861c0195e91b54cd33844bb31556a5a7f` | SERVER-017, SERVER-018 | yes | feat: RES-153742 - Overall Individual Migration of Email Templates to 2.0 |
| P222 | 2025-09-10 | `776ac31a54c72df9e05c84e52558cf7b2fedd4bf` | SERVER-017, SERVER-018 | yes | feat: RES-153742 - Overall Individual Migration of Email Templates to 2.0 |
| P223 | 2025-09-10 | `5796dba89703a3932ae19132fb74480f0b1e05c4` | SERVER-017, SERVER-018 | yes | feat: RES-153742 - Overall Individual Migration of Email Templates to 2.0 |
| P224 | 2025-09-11 | `73d88bf3c1d8bb1aeb70dcedb7d902fac1f19425` | SERVER-018 | yes | fix: RES-156468 - Section name is missing on the Guest user Email Template. |
| P225 | 2025-09-11 | `1a5d59cb6becf990ba5c532a7c449f9357c62d38` | SERVER-017 | yes | feat: RES-153742 - Overall Individual Migration of Email Templates to 2.0 |
| P226 | 2025-09-11 | `17f87d9a7bef8284d67e85505d6135129f187c84` | SERVER-017 | yes | feat: RES-153742 - Overall Individual Migration of Email Templates to 2.0 |
| P227 | 2025-09-12 | `e0bbfd24141804ee76f120982d5849c838bde4f9` | SERVER-017, SERVER-018 | yes | feat: RES-153742 - Overall Individual Migration of Email Templates to 2.0 |
| P228 | 2025-09-29 | `02bb233c00220ac307c676647c713808b1c274b4` | SERVER-027 | yes | feat: ai-agent base setup |
| P229 | 2025-09-30 | `b2fe1b225c86f9ac31b873e7274e580b7996ea34` | SERVER-027 | yes | feat: ai-agent base setup |
| P230 | 2025-10-02 | `59c043222741735d17adb63ec9c5b808843a9fbc` | SERVER-027 | yes | feat: ai-agent base setup |
| P231 | 2025-10-02 | `e722d10aee3b6728116691f3dee98cabc0bdd7c4` | SERVER-027 | yes | feat: ai-agent base setup |
| P232 | 2025-10-03 | `5d13f98e03e42280af896fdf61af14e76504b66c` | SERVER-027 | yes | feat: ai-agent base setup |
| P233 | 2025-10-07 | `1f64b545dd2fb4779919a12543e62b7d59e93b0b` | SERVER-027 | yes | feat: ai-agent base setup |
| P234 | 2025-10-16 | `84990c26cd3ea8e306c7c7305c568f848d450f90` | SERVER-027 | yes | fix: RES-159202 agent studio bugs |
| P235 | 2025-10-17 | `47df6c7700d0c6edb00f7bf4da2a38a879d4e0a1` | SERVER-027 | yes | feat: RES-159389 - canvas Missing on Reopened Conversations |
| P236 | 2025-10-17 | `d869a887c50e6444649e71cb6c1131f0f64b6244` | SERVER-027 | yes | feat: RES-159389 - canvas Missing on Reopened Conversations |
| P237 | 2025-10-22 | `40bf0841788a6cf58e183e578c1e98afb46f67c1` | SERVER-027 | yes | fix: RES-159566 - unable to run v1 ai agent |
| P238 | 2025-10-23 | `20d24d43a9fabe94a23f0d2697331531876d6e7c` | SERVER-028 | yes | feat: RES-151382 - Region Restriction Migration |
| P239 | 2025-10-23 | `98596b86b0da777728faadf07287a681b3e7d712` | SERVER-028 | yes | feat: RES-151382 - Region Restriction Migration |
| P240 | 2025-11-05 | `11d22667a82c416538b701db658d5e8d73866b3e` | SERVER-027 | yes | feat: RES-160161 - Section level ask rewrite |
| P241 | 2025-11-07 | `1ee942deb1f57a1465f00c4c9e15cc80b37a268f` | SERVER-027 | yes | fix: ignore test |
| P242 | 2026-05-22 | `2b0c9fbab8205f09b33017f69cee74a9eb73d1dd` | SERVER-007 | yes | fix: RES-177486 VULN-04: Mass PII Disclosure via User List Endpoint |
| P243 | 2026-07-02 | `f74aa089d8085f835bca4bcd0d0251a5014a5867` | SERVER-029 | no | feat: Maverick hackcathon - Phase II |
| P244 | 2026-07-02 | `d86b9aecd859fd1ddc3e1732a8cd968197607aa0` | SERVER-029 | no | feat: Maverick hackcathon - Phase II |
| P245 | 2026-07-11 | `2b86f1bcbcd3891dc7fa9e82f46020f5e2bf21ca` | SERVER-029 | no | feat: Maverick hackcathon - Phase II |
| P246 | 2026-07-12 | `34141e59772133a608211e0e743ecf69550c8a2e` | SERVER-029 | no | feat: AI hack feat mavericks |
| P247 | 2026-08-05 | `027d76768c16b11d1769aec808b8245ca8afe8b1` | SERVER-006 | no | feat: userList rewamp getCompanyUserName REMOVAL - RES-177198 |
| P248 | 2026-08-05 | `20f6f61ed901fa936c863f20a897fb6f3e6b160d` | SERVER-006 | no | feat: userList rewamp getCompanyUserName REMOVAL - RES-177198 |
| P249 | 2026-08-06 | `ad655f9b5e5940fd644968aa5e95fb0171f674f5` | SERVER-006 | no | feat: userList revamp ActiveUsers revamp - RES-177198 |
| P250 | 2026-08-12 | `d299cb3ea8886fdc0776628550b5e8ac46f62931` | SERVER-006 | no | feat: userList revamp ActiveUsers revamp - RES-177198 |
| P251 | 2026-08-14 | `6b7d41bbfb08550898f21785d181145039fdddae` | SERVER-006 | no | feat: userList revamp review comments - RES-177198 |
| P252 | 2026-08-14 | `9e60a84c1c7f61a3c4149ab5ad7f163641b61123` | SERVER-006 | no | feat: userList revamp review comments - RES-177198 |
| P253 | 2026-09-02 | `7f7324f737e91bc0dba64f83bd20fac5b430cbfe` | STASH-EXCLUDED | no | index on sam-company-user-load-details-removal: 9e60a84c1c7 feat: userList revamp review comments - RES-177198 |
| P254 | 2026-09-02 | `be9d4e6fcd849aef12ee82fa0e3054ed74de10c5` | STASH-EXCLUDED | no | untracked files on sam-company-user-load-details-removal: 9e60a84c1c7 feat: userList revamp review comments - RES-177198 |
| P255 | 2026-09-02 | `54a406b06074cec63c8be4f6de19c41febb2863d` | SERVER-030 | yes | feat: aggregate RFPIO app coverage paths |

### Repeated patches / cherry-pick deduplication

These pairs have equal stable patch IDs in the inspected inventory; they count once for implementation scope, regardless of target branch or merge count. Equal patch identity is not proof of equal deployment.

| Inventory group | Equivalent commit SHAs |
|---|---|
| P025 | `407a126c5e549a58e3183fa27002121de58c65e4`; `abbdc2e87632905ad77ac7586700464b549b3fdd` |
| P026 | `a9860a8160d57bca2353fddde12fbf967db4af0c`; `5d544bd17340c40d0ff1055068bff2a362a106a0` |
| P082 | `52e9825516a7d03911a47c17486292ed7693c097`; `6b7c128cfeb2e2bdd402ce8feae7437cb5859282` |
| P083 | `8f2ced34a63a04b303e759d5cd5c217d1cda6a9b`; `3a36580c367f76f2a6892561898d3ea4523f7544` |
| P138 | `814d35f090b215a7ef007f2bfe09d0dd31e56b6e`; `8909c7b4e2466c5b186d2ed2ee4d7beed5c302be` |
| P139 | `cf45c19545cb4e57fac09948ab3e4dfd141898ba`; `8b22c905d0d0d85a416606ea43536e84f2932d6d` |
| P140 | `d16791867e0d713bc8bbc343358ead7c19c5959a`; `ae066fe427bd4dbf8713e42663f101532aadf0ea` |
| P158 | `c68982dc1c656fc9c91e93db9374c3021e03b866`; `bc80269f862b864e391724f769b0032a988e668f` |
| P161 | `2081a35b49ec89683c75b8f115b492dddadc64d5`; `b100f3eac5af19d503bc3721935b424fafaa20db` |
| P216 | `360544927a9ddda5e6d0e6a4a11c74b6004e1cc3`; `ddcbdad7ba577605bacdcf5a6af054f8a8c1b683` |
| P224 | `73d88bf3c1d8bb1aeb70dcedb7d902fac1f19425`; `40dc322c98a4f511af3202b07152ef3cadcdae06` |
| P225 | `1a5d59cb6becf990ba5c532a7c449f9357c62d38`; `ba07ad26208339f2f2f2e3557dd63f22b7f3b2ca` |
| P226 | `17f87d9a7bef8284d67e85505d6135129f187c84`; `1decaf64b54c256923918a075c72f51c0ad129c9` |
| P227 | `e0bbfd24141804ee76f120982d5849c838bde4f9`; `a78c63de3ea6c0b9483a08240659c59c458bb09a` |
| P242 | `2b0c9fbab8205f09b33017f69cee74a9eb73d1dd`; `8de6c929f52282a6aa5f0554fb9e3b709f0a6758` |

### Collaborator-authored / candidate-committer records

These four identities match the committer, not the implementation author. They are merge/integration records and are excluded from personal implementation attribution; the recorded Bitbucket number does not supply inaccessible reviews/title/description.

| SHA | Author/date | Local merge subject |
|---|---|---|
| `fc3c4a275eb40e64c0db3b5887586028f19e11a5` | abishek.k; 2025-04-28 | Merged in abishek_v2_emailTemplate (pull request #32026) |
| `a0b023ab17ea7591bb3f970d86d705d5afd3c11b` | abishek.k; 2025-04-28 | Merged in abishek_v2_emailTemplate (pull request #32025) |
| `5bd3c1864e5f368677d51e490af0632213e0c41d` | abishek.k; 2025-04-22 | Merged in abishek_v2_emailTemplate (pull request #31836) |
| `32e61d0c775264ef9eed8d35c40ac0662ac619b5` | Preethi Singaram; 2024-12-19 | Merged in preethi_Email_template (pull request #29057) |

## Complete identity-matched merge inventory

M-ID rows preserve every merge, including the stash. “A” means the user-confirmed identity is author; “C” means committer; “A+C” means both. Generated Bitbucket merge authors often differ from the actual committer. A/C status is not personal implementation ownership or proof of conflict resolution. Local subjects below are Git subjects, **not inspected hosting PR titles**. Old Bitbucket URLs are intentionally not presented as inspected evidence. Combined-diff path counts identify where merged changes were inspected; zero does not prove no integration effort. Ordinary branch merges and PR integrations do not count as new features.

| Merge ID | Author date | Full commit SHA | Identity match | Local PR/branch integration subject | Combined-diff paths |
|---|---|---|---|---|---|
| M001 | 2023-01-09 | `57614ffdd6136583da783494cea67113657a2126` | A | Merged in Sanjeev_dev (pull request #17479) | 1 |
| M002 | 2023-01-13 | `8612ae83a7639812d127d50f7d8069aafc386348` | A | Merged in Sanjeev_server (pull request #17570) | 0 |
| M003 | 2023-01-20 | `f1ca8d228c6f79e09a8fe318a8b3189dc8001778` | A | Merged in Sanjeev_server (pull request #17657) | 0 |
| M004 | 2023-01-27 | `95426f0564552b7a45413abf9bcafe2d10fb5f03` | A | Merged in Sanjeev_dev_server (pull request #17658) | 2 |
| M005 | 2023-03-13 | `503f55a610261f9deac94ba6f27eaec7eef07bb7` | A | Merged in Sanjeev_stg (pull request #18242) | 0 |
| M006 | 2023-07-10 | `c9ff28e6d12e1533fa6161afb0dfa9da23791d9d` | A | Merged in Sanjeev_my_work (pull request #19900) | 0 |
| M007 | 2023-07-10 | `4da106f52d22ccaa119184afc381bd1c5d69ce80` | A+C | Merged in my_work_dev3 (pull request #19987) | 0 |
| M008 | 2023-07-10 | `30a05625a5cb19f40ba4a84b28bde05d1d411e38` | A+C | Merged in Sanjeev_my_work (pull request #19993) | 0 |
| M009 | 2023-07-10 | `6b0327c4a01880a80339ad6d7a462073633d2806` | A+C | Merged in my_work_dev3 (pull request #19994) | 0 |
| M010 | 2023-07-17 | `09be34f8a793579076a475f858db7d0430978c4e` | A | Merged in Sanjeev_stg (pull request #20029) | 0 |
| M011 | 2023-08-23 | `5a5c442029c9a6040f4d326c76e48bd6306e4f66` | A | Merged in Sanjeev_stg (pull request #20566) | 0 |
| M012 | 2023-09-14 | `dcf85ab96e31326bd43596bda4a380f41146c25f` | A | Merged in sanjeev_org (pull request #21004) | 0 |
| M013 | 2023-09-14 | `2bcca4f4f978d5f68b7cdb20bd39731ed55dd7ac` | A+C | Merged in dev3_conflict (pull request #21006) | 0 |
| M014 | 2023-09-14 | `4b033463a1c729c85899737aca61c0cb9a5e4c88` | A | Merged in dev3_conflict (pull request #21019) | 0 |
| M015 | 2023-09-14 | `cb56d10244206f99e78c39e252dea3f44700f88e` | A+C | Merge branch 'org_settings_dev3' into dev3_conflict | 2 |
| M016 | 2023-11-14 | `448c18f7e1f8b2aadefae0290661ecf83aedf2ca` | A | Merged in sanjeev_pre (pull request #21898) | 0 |
| M017 | 2023-11-14 | `f522aecfcd7a28f36eaf5c4cae99e1df0e7623ed` | A | Merged in sanjeev_mr (pull request #21903) | 0 |
| M018 | 2023-11-14 | `c8bd828b291f1a1d6ef68c136c253d0ffe2718b7` | A+C | Merge branch 'master' into sanjeev_pre | 1 |
| M019 | 2023-11-23 | `6c80926140ea51eb15e0e691629def630738d9aa` | A+C | Merge branch 'qrelease' into sanjeev_qr | 1 |
| M020 | 2023-12-20 | `f678551c4a9fdd0bc3dec67a0abced4492aa3bad` | A | Merged in sanjeev_customfont (pull request #22384) | 0 |
| M021 | 2023-12-21 | `014c60f4592e61fbc112667a74d50cf73311152f` | A | Merged in sanjeev_customfont (pull request #22414) | 0 |
| M022 | 2024-02-08 | `dc4450d69b9df55acf0284ea8f80b1f42d19bbfa` | A | Merged in sanjeev_org_settings (pull request #22905) | 0 |
| M023 | 2024-02-12 | `6dc2acaa85577c7355d6680f322d37d86a6f5ce4` | A | Merged in sanjeev_org_settings (pull request #23049) | 1 |
| M024 | 2024-02-21 | `7d71ae20dd3de636f04eede6c06ff1ae53c60fb6` | A | Merged in sanjeev_org_settings (pull request #23221) | 0 |
| M025 | 2024-04-15 | `f88cbc27cecde2ef608982b82901365347b2200c` | A+C | Merge branch 'staging' into sanjeev_stg2 | 0 |
| M026 | 2024-04-15 | `3da2d2aa3559523d3c41363752d1761f384d5ecc` | A+C | Merge branch 'staging' into sanjeev_stg2 | 0 |
| M027 | 2024-04-17 | `b14ef547c5cb0e50f11f3cbe5ffbd1bae47c1897` | A+C | Merge branch 'staging' into sanjeev_stg2 | 0 |
| M028 | 2024-04-20 | `28c3d12ffe21e6c3125b729e0be0b0fd9078c058` | A+C | Merge branch 'staging' into sanjeev_stg2 | 0 |
| M029 | 2024-04-24 | `0aa59349bdc8afa68078ff056df13126fe6899ea` | A+C | Merge branch 'sri_userload_revamp_server' into sam_org | 5 |
| M030 | 2024-07-02 | `8310c705af45335001b1bbe47603420884a1de60` | A+C | Merge branch 'staging' into sam_org | 0 |
| M031 | 2024-07-10 | `1c579f07711faf81c15a2e1ff0e487ed155ede38` | A+C | Merge branch 'abishek_server_org_settings' into sam_org | 0 |
| M032 | 2024-08-06 | `4346a6df1e8a5e2b7d71f90d1a6beea29579f5a3` | A+C | Merge branch 'Logapriya_server' into sam_org | 0 |
| M033 | 2024-08-12 | `5390e918526857be3834382390691ecca57c84e6` | A | Merged in sam_org (pull request #26561) | 1 |
| M034 | 2024-08-12 | `027fe7d3443f96c4f9c93fd200fab7152391a21d` | A+C | Merge branch 'sam_org' into sam_org | 0 |
| M035 | 2024-09-16 | `71a3268117ac5c34a8c7d65ed1f526a161141696` | A | Merged in sam_org (pull request #27102) | 2 |
| M036 | 2024-09-29 | `97a2713ff02b90c2ff7f79c38faea603fa82b3ef` | A+C | Merge branch 'staging' into sam_org | 2 |
| M037 | 2024-10-15 | `35c241919acd041cb3000086702a06a69e638974` | A | Merged in sam_email (pull request #27737) | 0 |
| M038 | 2024-11-04 | `92b6b33ab160be7c43acbf60a6b09fd9e1263cf2` | A | Merged in sam_prl (pull request #28103) | 1 |
| M039 | 2024-11-05 | `43c4483cdd9d9d37820aeb290a90bbd66a56f6cb` | A | Merged in sam_prl (pull request #28104) | 0 |
| M040 | 2024-11-06 | `09bb4eee7dd7cc75615e54d2f1c5a57ab0df4092` | A | Merged in sam_mr (pull request #28123) | 1 |
| M041 | 2024-11-06 | `8b7a180920a293db4e5f30d61cbc2e1be1519e56` | A | Merged in sam_mr (pull request #28124) | 1 |
| M042 | 2024-11-06 | `da319249e5fe5fe1e245591212b02ae5298d7d6d` | A | Merged in sam_mr (pull request #28149) | 1 |
| M043 | 2024-11-06 | `8d8e95c82b282b984e66dcfb5b70dbf5990d9777` | A | Merged in abishek_server_org_settings (pull request #28156) | 1 |
| M044 | 2024-11-06 | `7d9e8a26f3fb2ff09c223d5bd7d967328f3aefab` | A | Merged in abishek_server_org_settings (pull request #28157) | 1 |
| M045 | 2024-11-08 | `17d3f7f4237bc46c792ee30e1216ba83a72670b0` | A | Merged in sam_mr (pull request #28183) | 1 |
| M046 | 2024-11-08 | `7070bb32289e860644dc075fadec3c8750e23c36` | A | Merged in sam_mr (pull request #28192) | 1 |
| M047 | 2024-11-08 | `f9bfdfea5a7fd05e945f1009ffc992215ce81f56` | A+C | Merge branch 'master' into sam_mr | 0 |
| M048 | 2024-11-13 | `ce3b89535b825e96ae54d47f2c7954272722b86c` | A | Merged in sam_mr (pull request #28266) | 0 |
| M049 | 2024-11-14 | `1e599f3a4eb40bc3bf9f97fef40a016d38cacc2c` | A | Merged in sam_mr (pull request #28267) | 0 |
| M050 | 2024-11-14 | `187f52cf3fcee42a1723b23686e2a4c4b1c73b65` | A | Merged in sam_mr (pull request #28287) | 0 |
| M051 | 2024-12-17 | `7235899081f3150a18c300357bf9d56ca534b3cd` | A+C | Merge branch 'staging' into sam_mr | 3 |
| M052 | 2024-12-18 | `566ad278de60e4740df3059538efc87b8d193d08` | A | Merged in sam_mr (pull request #28991) | 0 |
| M053 | 2024-12-18 | `aaac26a6b6093fd288510bf830b1e4b3fe631c98` | A+C | Merged in sam_mr (pull request #29026) | 0 |
| M054 | 2024-12-19 | `fdec0b4b2d653654581943be257a7b7a1c0de30f` | A+C | Merged in sam_mr (pull request #29051) | 0 |
| M055 | 2024-12-19 | `32e61d0c775264ef9eed8d35c40ac0662ac619b5` | C | Merged in preethi_Email_template (pull request #29057) | 0 |
| M056 | 2024-12-20 | `65b16927ddceb763c8385ef4f60a869576f6f237` | A | Merged in sam_guest_email (pull request #29086) | 0 |
| M057 | 2025-01-08 | `06eb34115ceb1d3265a2780b867dcfb273681c54` | A | Merged in email_test_revert (pull request #29246) | 1 |
| M058 | 2025-01-08 | `9300a1b99be288d0ed41e45aad8c5f3db530e0d7` | A+C | Merged in staging (pull request #29255) | 0 |
| M059 | 2025-01-08 | `c5bbf71786c05ced73400e7d04648cdc1731efff` | A | Merged in email_test_revert (pull request #29259) | 0 |
| M060 | 2025-01-08 | `8f1809c642385997846f6dd33a0aed4316910ffd` | A+C | Merge branch 'Emailtemplates-v2' into email_test_revert | 0 |
| M061 | 2025-01-09 | `e24835577c1865303384a9882b5311af7fce3ae5` | A | Merged in email_test_revert (pull request #29267) | 0 |
| M062 | 2025-01-09 | `33c300a84544b721ed82c9fd94551a4badaec7ea` | A | Merged in email_test_revert (pull request #29268) | 0 |
| M063 | 2025-01-09 | `0b3e3567926fd0a2be2fce728c13c26c75447020` | A+C | Merge branch 'Emailtemplates-v2' into email_test_revert | 0 |
| M064 | 2025-01-10 | `d3fe286531be6e171a2cec6cd18573e75ea495cb` | A | Merged in email_test_revert (pull request #29298) | 0 |
| M065 | 2025-01-10 | `8b98349b72c6ef4df28369bdbb6ff33c3b42a854` | A+C | Merge branch 'Emailtemplates-v2' into email_test_revert | 0 |
| M066 | 2025-01-13 | `d6736f6800793a7d138900068e048f13eaeadd7d` | A+C | Merged in email_test_revert (pull request #29355) | 0 |
| M067 | 2025-01-13 | `87fd8b64ec9c3303b1ea63d9c601f40232cc4fa7` | A+C | Merge branch 'Emailtemplates-v2' into email_test_revert | 1 |
| M068 | 2025-01-13 | `5f310e3423b35b011637bf586ffa67bc591773b2` | A+C | Merge branch 'staging' into email_test_revert | 3 |
| M069 | 2025-01-20 | `5ca67a6c3ebea5946aa091701cd0793276e0b53e` | A | Merged in email_test_revert (pull request #29356) | 1 |
| M070 | 2025-01-22 | `e29e34f35726424bfd6f49bd9e5f081eb973d1cb` | A+C | Merge branch 'Emailtemplates-v2' into sam_mail_template | 0 |
| M071 | 2025-01-22 | `5841aebc492f8a9b293af17fd87d09bf4c95a60b` | A+C | Merge branch 'Emailtemplates-v2' into sam_mail_template | 0 |
| M072 | 2025-01-23 | `c4187103e115f62bea473711c5a2d69798a88f8e` | A | Merged in sam_mail_template (pull request #29571) | 0 |
| M073 | 2025-01-28 | `1524887dfcae67727ded1e2f5bbcea94f613ebbe` | A | Merged in sam_mail_template (pull request #29717) | 0 |
| M074 | 2025-01-28 | `5a9b01593461dffe66b75e707147c196b6cc3698` | A+C | Merge branch 'Emailtemplates-v2' into sam_mail_template | 0 |
| M075 | 2025-01-28 | `139d845085316d64da3a2b5a66f1548aaa3a1579` | A+C | STAGING SYNC | 6 |
| M076 | 2025-01-30 | `c45dde206f61d3319724f403278354659d30e5b4` | A+C | Merge branch 'Emailtemplates-v2' into sam_mail_template | 0 |
| M077 | 2025-01-31 | `9510d4566f6eba7be83cc12ebb7014b8b2828c9d` | A | Merged in sam_mail_template (pull request #29810) | 0 |
| M078 | 2025-02-04 | `71da2c022989001cb48dbeb589dd2769749690d6` | A+C | Merge branch 'Emailtemplates-v2' into sam_mail_template | 0 |
| M079 | 2025-02-05 | `c60953558a4a9b522be6e0034795d1445f2357b0` | A | Merged in sam_email_tracking (pull request #29886) | 1 |
| M080 | 2025-02-05 | `4838522a454bb2aec561471c9da492a1f2b1c641` | A | Merged in sam_french (pull request #29904) | 0 |
| M081 | 2025-02-05 | `390cc3f291974af62113a6cc470e41a9ac37f585` | A+C | Merge branch 'Emailtemplates-v2' into sam_mail_template | 4 |
| M082 | 2025-02-06 | `72e2449bc659f65d2351aafdb85fa077ce1adbaa` | A | Merged in sam_mail_template (pull request #29937) | 3 |
| M083 | 2025-02-06 | `48a3174384767fa0f14724b8869322eb837500c1` | A | Merged in sam_email_tracking (pull request #29940) | 0 |
| M084 | 2025-02-06 | `c7060d7fc6946117b4021026300a6b19fe37a2e7` | A+C | Merged in sam_email_base (pull request #29958) | 0 |
| M085 | 2025-02-06 | `484e3233a733d6b926ba9ef0296e2460f9026f8c` | A | Merged in sam_email_base (pull request #29959) | 1 |
| M086 | 2025-02-06 | `7e1e835e7d34bbad7a7bf9e4fa77d0a0faed378b` | A+C | Merge branch 'staging' into sam_email_tracking | 1 |
| M087 | 2025-02-06 | `6509f85d7076489338a0d746652d1f6e4e0ef772` | A+C | Merge branch 'staging' into sam_email_base | 5 |
| M088 | 2025-02-24 | `f6bdfafa2f11b2bc6cc6217637ac04d530dbb163` | A | Merged in sam_hubspot (pull request #30337) | 0 |
| M089 | 2025-02-28 | `0f437cce223e1206e4d87a75e638b48c90397a0e` | A | Merged in sam_hubspt (pull request #30439) | 0 |
| M090 | 2025-03-07 | `b0c0c1ef2ad22159127dcec06e566fac0bbd0682` | A | Merged in sam_seismic_sync (pull request #30604) | 0 |
| M091 | 2025-03-07 | `14483f5a7aee33a40914379ca1600188a27f2bf7` | A | Merged in sam_seismic (pull request #30603) | 0 |
| M092 | 2025-03-12 | `568eb701e9f9311675474c907b387f85264a04b0` | A+C | Merge branch 'feature/email-template-v2-stg' into feature/email-template-v2-stg | 1 |
| M093 | 2025-03-13 | `25aef97ce4d235b283b70ff59e537ffd192b1c23` | A | Merged in feature/email-template-v2-stg (pull request #30711) | 2 |
| M094 | 2025-03-13 | `3f359e7f12817e2b8f1da106f10e6fe420a06f9d` | A+C | Merge branch 'feature/email-template-v2-stg' into feature/email-template-v2-stg | 0 |
| M095 | 2025-03-13 | `aca7c1e18eba1a48eab17bbf7423f3c3ae828bd2` | A+C | Merge branch 'feature/email-template-v2-stg' into feature/email-template-v2-stg | 0 |
| M096 | 2025-03-14 | `a7950b075f07f6742b7eea8c45dc3596b1dcc24d` | A | Merged in feature/email-template-v2-stg (pull request #30811) | 0 |
| M097 | 2025-03-14 | `0ddc37fd58e8c43c40f734a213117b5fae9ebc89` | A | Merged in feature/email-template-v2-stg (pull request #30812) | 0 |
| M098 | 2025-03-25 | `8d955a4c5f9020d59108c2b7eb15953d4f3928d9` | A | Merged in sam_email_v2 (pull request #31107) | 0 |
| M099 | 2025-03-27 | `ac0354ecd56b1b414abc5e8d1f1da4293b95243a` | A+C | Merge branch 'staging' into sam_email_v2 | 4 |
| M100 | 2025-03-28 | `6791d1ddfc43da3307d34498bbcbc1e3f0abc595` | A | Merged in sam_email_v2 (pull request #31194) | 3 |
| M101 | 2025-03-28 | `9430e5d337f135bc88e1fafa85cf677b412166f1` | A+C | Merge branch 'staging' into sam_email_v2 | 4 |
| M102 | 2025-03-31 | `30152d954ca2cc14068f6935c9bc60d045760284` | A | Merged in preethi_mst_april (pull request #31267) | 0 |
| M103 | 2025-04-01 | `7cc0ab37f92608ed94900127916a322837a85778` | A | Merged in preethi_mst_april (pull request #31285) | 0 |
| M104 | 2025-04-01 | `7d8a5a30e710c1df8c07184d36c668184b579ad0` | A | Merged in preethi_mst_april (pull request #31286) | 0 |
| M105 | 2025-04-02 | `3d9632ac2b50b7256748e432028af269ebab2661` | A | Merged in sam_email_v2 (pull request #31346) | 0 |
| M106 | 2025-04-02 | `8b1fc0a35e3ebc28551bad64d3e607b04790af9b` | A+C | Merge branch 'staging' into sam_email_v2 | 4 |
| M107 | 2025-04-03 | `a3143192ea1841b1cf37ca64b1749316648f9998` | A | Merged in sam_email_v2 (pull request #31403) | 0 |
| M108 | 2025-04-03 | `69c9f863886f7690ca422fd8d9de716694e216a2` | A+C | Merge branch 'staging' into sam_email_v2 | 1 |
| M109 | 2025-04-04 | `e89e711b5f521cea9360b6429db02e94f8100d01` | A | Merged in sam_email_v2 (pull request #31412) | 0 |
| M110 | 2025-04-16 | `c44854450741ffce9f5e4839f39a0be31fb7ff83` | A+C | Merge branch 'prerelease' into sam_email_v2 | 1 |
| M111 | 2025-04-17 | `310019e047d19b2184048c7cd86f26081ac553c9` | A | Merged in sam_email_v2 (pull request #31726) | 0 |
| M112 | 2025-04-21 | `f1f77c49124c4d5461510af8fe15ba04718d5e99` | A | Merged in sam_email_v2 (pull request #31801) | 1 |
| M113 | 2025-04-22 | `eaa83a17e3c468c4aad693e0abdff53babcc77d2` | A | Merged in sam_email_v2 (pull request #31834) | 0 |
| M114 | 2025-04-22 | `5bd3c1864e5f368677d51e490af0632213e0c41d` | C | Merged in abishek_v2_emailTemplate (pull request #31836) | 2 |
| M115 | 2025-04-22 | `e7922d8f59c0ee1670af185212e27f3859f64380` | A | Merged in sam_email_v2 (pull request #31841) | 1 |
| M116 | 2025-04-22 | `717555c3f085590d73de829b8441ccdd3886ec26` | A+C | Merge branch 'outlook_email' into sam_email_v2 | 0 |
| M117 | 2025-04-23 | `cb384ef6ec31c3fa6e406715c2df8fdf43230eb7` | A | Merged in outlook_email (pull request #31858) | 0 |
| M118 | 2025-04-23 | `7d0205a328737f1c84c30caa9d21c0e5f3ac2b77` | A+C | Merge branch 'outlook_email' into sam_email_v2 | 0 |
| M119 | 2025-04-23 | `13e39b1354dda0476117a7a082d14f9c9dc091df` | A+C | Merge branch 'outlook_email' into sam_email_v2 | 0 |
| M120 | 2025-04-24 | `d29f8829f4012cfe26dcc375a2923d1303a81274` | A+C | Merge branch 'outlook_email' into sam_email_v2 | 0 |
| M121 | 2025-04-25 | `18c6f08b9b081ffc52fdcacfad1cc2ee2f2129cf` | A | Merged in sam_email_v2 (pull request #31937) | 1 |
| M122 | 2025-04-28 | `70f90720e5a5ec4d5c157a768769599039bc6d0e` | A | Merged in email_addrs (pull request #31987) | 0 |
| M123 | 2025-04-28 | `444845a13cb2c08555d491e6b01c3a337dd67e22` | A+C | Merged in sam_email_v2 (pull request #31996) | 0 |
| M124 | 2025-04-28 | `2e54cc5ccf956f07992674036787189f73a418a5` | A | Merged in email_addrs (pull request #31991) | 0 |
| M125 | 2025-04-28 | `53ade47968956ae4809f247f0e534e6b85c8c24f` | A+C | Merged in sam_email_v2 (pull request #32002) | 1 |
| M126 | 2025-04-28 | `da3111f231b433a3cc756adf595ff6dea70f8c41` | A+C | Merged in sam_email_v2 (pull request #32004) | 2 |
| M127 | 2025-04-28 | `271479ff081802b653b28087107a969cb1ba05d3` | A | Merged in outlook_email (pull request #31998) | 2 |
| M128 | 2025-04-28 | `e6374f90a8160b2b708f3089210d6afce22c6d00` | A | Merged in email_addrs (pull request #32010) | 0 |
| M129 | 2025-04-28 | `89c67cc006a3325f415b679861e3a79b3483d722` | A | Merged in sam_email_v2 (pull request #32014) | 2 |
| M130 | 2025-04-28 | `bf58e50d50f6cf6007b4973b60d4abadebf48095` | A+C | Merge branch 'outlook_email' into sam_email_v2 | 3 |
| M131 | 2025-04-28 | `a0b023ab17ea7591bb3f970d86d705d5afd3c11b` | C | Merged in abishek_v2_emailTemplate (pull request #32025) | 0 |
| M132 | 2025-04-28 | `fc3c4a275eb40e64c0db3b5887586028f19e11a5` | C | Merged in abishek_v2_emailTemplate (pull request #32026) | 1 |
| M133 | 2025-04-28 | `c07b5d4bd9e163ef18b3f94bf0d86a7afef495d1` | A | Merged in outlook_email_copy (pull request #32024) | 0 |
| M134 | 2025-04-28 | `4bd4567b44b8dbf0b25360dfd31d503f30ac1f52` | A | Merged in outlook_email (pull request #32015) | 1 |
| M135 | 2025-04-28 | `7b908bcccca0a5b0063f16368f69f23533df73b6` | A+C | Merge branch 'outlook_email' into sam_email_v2 | 2 |
| M136 | 2025-04-28 | `6dd8d2d48163c3921d527d73d2f208391a2acb49` | A+C | Merge branch 'staging' into outlook_email_copy | 5 |
| M137 | 2025-04-29 | `2b1804f62d48070b11e53f30930e1ad0889f282b` | A | Merged in outlook_email (pull request #32035) | 0 |
| M138 | 2025-04-29 | `54a9c6d1f8552a60fdcff01464be72efd6f9659b` | A+C | Merged in sam_email_v2 (pull request #32019) | 2 |
| M139 | 2025-04-29 | `f200b4f145c54d9989dca37154770131400b9e01` | A+C | Merged in sam_email_v2 (pull request #32071) | 0 |
| M140 | 2025-04-29 | `117088e5cfe34568df13e412d24c12da8ed011f0` | A | Merged in outlook_email_copy (pull request #32065) | 0 |
| M141 | 2025-04-29 | `0e863669ef6ed83dd4b9add4290a162f79045921` | A | Merged in outlook_email (pull request #32060) | 1 |
| M142 | 2025-04-29 | `81f73a56d02791a441d80cd1b682189969629aaf` | A+C | Merge branch 'outlook_email_copy' into outlook_email_copy | 0 |
| M143 | 2025-04-29 | `f8f3b99a730fb8f936e600fe21b96222a40313ef` | A+C | Merge branch 'outlook_email' into sam_email_v2 | 0 |
| M144 | 2025-04-30 | `ef827975f044f57456653916070cb28fdf76d3af` | A+C | Merged in sam_email_v2 (pull request #32105) | 0 |
| M145 | 2025-04-30 | `7d08ce5bad222fa2b92cc4b7e8e47461baa56885` | A | Merged in outlook_email (pull request #32106) | 1 |
| M146 | 2025-05-02 | `a513ec82827c5e703945c4fca6b5acab9c2c55ba` | A+C | Merge branch 'outlook_email' into sam_email_v2 | 1 |
| M147 | 2025-05-05 | `e101a2e240fbcc99d79caf47d9c0e813e52fbc94` | A | Merged in outlook_pr (pull request #32194) | 0 |
| M148 | 2025-05-05 | `49c75c37da0cf3e645e936dc039197fd6edb00d0` | A+C | Merge branch 'outlook_email_mst' into sam_email_v2 | 3 |
| M149 | 2025-05-05 | `1a39f241bc23b045e5fac2a87ec7c472a3c8c712` | A+C | Merge branch 'prerelease' into outlook_pr | 0 |
| M150 | 2025-05-06 | `090a9ca460b4d308f85499e1fc2d2388132facaf` | A | Merged in sam_email_mst (pull request #32193) | 0 |
| M151 | 2025-05-06 | `ec1e3acf9db5a4586abda66f38bb0aaf99bc37bb` | A | Merged in sam_email_mst (pull request #32240) | 0 |
| M152 | 2025-05-06 | `a779dfcc9a4f32786c9560cdd38734278b586f6b` | A+C | Merge branch 'master' into sam_email_mst | 0 |
| M153 | 2025-05-06 | `993237cf823c3951dca7b4cc7bf8ebb12bf91a69` | A+C | Merge branch 'outlook_email_mst' into outlook_pr | 2 |
| M154 | 2025-05-07 | `0f277f27bbef34a67769bc31040c767f67cc3779` | A+C | Merged in prerelease (pull request #32252) | 0 |
| M155 | 2025-05-07 | `c0858886f65f9f4f9d3065f422998c5e2b3536df` | A+C | Merged in sam_email_mst (pull request #32256) | 0 |
| M156 | 2025-05-07 | `f5b99a6232d102736c97cc77e50748848fe58db7` | A+C | Merged in sam_email_mst (pull request #32257) | 0 |
| M157 | 2025-05-07 | `e9186c080e1d41935f42807d059a3b1da289f294` | A | Merged in outlook_pr (pull request #32247) | 0 |
| M158 | 2025-05-08 | `fc090c5c6b644b00d5e1898fb2b90917615b91d6` | A+C | Merged in sam_email_mst (pull request #32289) | 0 |
| M159 | 2025-05-08 | `2163db364b73c6888bd94b954300b2ee9a6b16d2` | A+C | Merged in sam_email_mst (pull request #32291) | 0 |
| M160 | 2025-05-08 | `6b5ec6bcf503e35b4d97820f794ef285bd64805a` | A+C | Merged in sam_email_mst (pull request #32293) | 0 |
| M161 | 2025-05-08 | `0eee80b0e955865a6dbe8069b644236dbb05fe32` | A | Merged in outlook_email_mst (pull request #32288) | 0 |
| M162 | 2025-05-08 | `804069ecd94f0bee1dcaee3ee92894aed1bbd0de` | A+C | Merge branch 'master' into sam_email_mst | 1 |
| M163 | 2025-05-08 | `5c9c1b1ea4a7c3214399a4d1a9ae2f9b630cb068` | A | Merged in sam_zendkk (pull request #32298) | 0 |
| M164 | 2025-05-08 | `0b35db499db581632850f165af08e20e8c56d893` | A+C | Merge branch 'prerelease' into sam_zendkk | 1 |
| M165 | 2025-05-09 | `26b873cf2b22d7498c1af6f2ec7b38f1269d6ec7` | A | Merged in sam_shrpt (pull request #32326) | 0 |
| M166 | 2025-05-09 | `e7af271b036026f4d2559f93c0c6f554b893ed7d` | A | Merged in sam_shrpt (pull request #32332) | 0 |
| M167 | 2025-05-20 | `5eabd0fd25ac1adb1b234a4a16b8d24854f92839` | A | Merged in sam_shrpt (pull request #32562) | 1 |
| M168 | 2025-05-21 | `40132c2bdfa8fb8cbf4ee004c511bc34de32cc18` | A | Merged in sam_e2e_bugs (pull request #32599) | 0 |
| M169 | 2025-05-21 | `3f263e6bcc7a1cab7bcf8e0ad0f6863135e63ba4` | A | Merged in sam_e2e_bugs (pull request #32600) | 2 |
| M170 | 2025-05-22 | `dcd230d4ba692237a5a6d298e33ac2f7b7c4db47` | A | Merged in sam_shrpt (pull request #32585) | 0 |
| M171 | 2025-05-22 | `2309912467c69cecef1ec66b67fc166edf446ac9` | A | Merged in sam_e2e_bugs (pull request #32637) | 1 |
| M172 | 2025-05-22 | `55105bc6b9369168255f59326488af3688435d7a` | A | Merged in sam_e2e_bugs (pull request #32638) | 1 |
| M173 | 2025-05-26 | `a201c0b45f0031605bec2d34c1be286315474337` | A | Merged in sam_shrpt (pull request #32714) | 1 |
| M174 | 2025-05-27 | `5c911a651300af054be82aaaf4300c8f4c91f7ae` | A | Merged in sam_shrpt (pull request #32745) | 0 |
| M175 | 2025-05-29 | `a132cfea7a0b8b992ebfce77de36f7c7fb25ab4a` | A | Merged in sam-mail-pre (pull request #32810) | 0 |
| M176 | 2025-05-30 | `9ce351adbae5211cd3bd667b24c82b07c1aaed02` | A | Merged in sam-mail-pre (pull request #32816) | 0 |
| M177 | 2025-05-30 | `b4d77f1f8ac6be19970d74c2e5ee0d584c3eed49` | A+C | Merge branch 'prerelease' into sam-mail-pre | 0 |
| M178 | 2025-06-03 | `34f1370e267f653a50c5bbf59b0fc110428a8638` | A+C | Merge branch 'prerelease' into sam-mail-pre | 0 |
| M179 | 2025-06-14 | `3dd3a680b401633139cc542757c1248c3111a5c7` | A+C | Merge branch 'sam-mail-pre' into sam-mail-pre | 0 |
| M180 | 2025-06-16 | `452cbbec6141a15947305cb91fdfeea83d76c4b2` | A | Merged in sam-mail-pre (pull request #32935) | 0 |
| M181 | 2025-06-16 | `7208f2c021bf43f3b58b7bae6e7628ca45907224` | A | Merged in sam_ai_dev (pull request #33291) | 0 |
| M182 | 2025-06-16 | `49df70c35041c90a7355729a83e515a304f7707f` | A+C | Merge branch 'staging' into sam_ai_stg | 7 |
| M183 | 2025-06-17 | `d00389e1e9d8fd05df509c08d4dde569ce17d5e5` | A | Merged in sam_ai_dev (pull request #33295) | 0 |
| M184 | 2025-06-17 | `39a2523569cd42c89cd6ceb8dc39fd73cfea7562` | A | Merged in sam_ai_dev (pull request #33309) | 0 |
| M185 | 2025-06-19 | `29651b72a6fdf5f926809b8254123dbc31f0646e` | A | Merged in sam_ai_dev (pull request #33412) | 1 |
| M186 | 2025-06-19 | `cd0e1070d7d45e2add9055d49b0eb90d52054e4e` | A+C | Merge branch 'sam_ai_dev' into sam_ai_dev | 0 |
| M187 | 2025-06-19 | `d1a35c982779b7e63121d141be777747ac1ca8f8` | A | Merged in sam_dev-t (pull request #33465) | 0 |
| M188 | 2025-06-19 | `5aa8e8a6144a4745bf73c39a28e59812f757006c` | A+C | Merge branch 'sam_header_stg' into sam_header_stg | 0 |
| M189 | 2025-06-19 | `ee8615634e0a6769c84b2faa341f8b33a94a7e8e` | A+C | Merge branch 'sam_header_stg' into sam_header_stg | 0 |
| M190 | 2025-06-19 | `b4ddd71d3c204336cf8a5f2d6b2be559fb4eee2f` | A | Merged in sam_header_stg (pull request #33485) | 3 |
| M191 | 2025-06-19 | `915296229e07cd15c82e9213a85f4c63f396e209` | A | Merged in sam_header_stg (pull request #33487) | 0 |
| M192 | 2025-06-19 | `b4568145b2ebbe7d949fe91c3cfdbe129909f42e` | A | Merged in sam_header_stg (pull request #33488) | 0 |
| M193 | 2025-06-20 | `a2aa75ed95a4f6bdf6d1fc8fdd2dd570a1085efe` | A+C | Merge branch 'sam_header_stg' into sam_header_stg | 1 |
| M194 | 2025-06-20 | `8cba42e8fa24278641419075dcca7ba1242bafa0` | A | Merged in sam_header_stg (pull request #33452) | 0 |
| M195 | 2025-06-20 | `02cb29bbad8fe792e6cb67fdabf37803d33e1cba` | A+C | Merge branch 'sam_header_stg' into sam_header_stg | 0 |
| M196 | 2025-06-20 | `5869a1738e51e593f3a93a13d9e0cdbd54dd0b74` | A+C | Merge branch 'sam_header_stg' into sam_header_stg | 0 |
| M197 | 2025-06-25 | `bb63564e393bd2be657d228f7766b1401096f648` | A | Merged in sam_header_stg (pull request #33696) | 1 |
| M198 | 2025-06-25 | `e982421b0b688ab7954e9505837c756b24f75286` | A | Merged in sam_header_stg (pull request #33695) | 0 |
| M199 | 2025-06-25 | `e41964398e315e6476b9cc11a28ee3d43c923a81` | A | Merged in sam_header_stg (pull request #33741) | 0 |
| M200 | 2025-06-25 | `f48267aba73b4a1367e82ab934b7ad652a4f24cb` | A | Merged in sam_header_stg (pull request #33748) | 0 |
| M201 | 2025-06-25 | `5ab42d511bebf5559992055fc2b00a830f901246` | A+C | Merge branch 'release-RES-25.06.04' into sam_header_stg | 2 |
| M202 | 2025-06-25 | `8a1bef36d211a57099473cde8662a19f3b7c1883` | A+C | Merge branch 'release-RES-25.06.04' into sam_header_stg | 1 |
| M203 | 2025-06-30 | `71b349cb067c9c57ef6c7693b4fff6fa789eb37d` | A | Merged in sam_header_stg (pull request #33793) | 0 |
| M204 | 2025-06-30 | `f2f27fa0fb8ff8e5857cacac04e1597e91a7d638` | A | Merged in sam_header_stg (pull request #33813) | 0 |
| M205 | 2025-06-30 | `e0f55fcb85d615607a054e68fe8613abc05af799` | A | Merged in sam_header_stg (pull request #33810) | 0 |
| M206 | 2025-06-30 | `b2a7df4a678f66e09feaab092002c6dfd979dc09` | A+C | Merge branch 'sam_header_stg' into sam_header_stg | 0 |
| M207 | 2025-06-30 | `077d57181db7c462e426a7cd58779d594a2b760a` | A | Merged in sam_header_stg (pull request #33820) | 0 |
| M208 | 2025-07-02 | `4213c9f24c96d14794ee26cdc0ee159c36555829` | A | Merged in sam_header_stg (pull request #33874) | 2 |
| M209 | 2025-07-02 | `e6573dc31912fa0502b3b8a229e47eec1a84bf0f` | A | Merged in sam_header_stg (pull request #33877) | 2 |
| M210 | 2025-07-03 | `e48128235199e4eaa0ecacf5056306d22861b909` | A | Merged in sam_header_stg (pull request #33897) | 2 |
| M211 | 2025-07-03 | `53d50d4083d85d84525281f7981f1cdd3ed0b092` | A | Merged in sam_header_stg (pull request #33896) | 2 |
| M212 | 2025-07-03 | `c9839a377860b84d6b05079b1d51201aed467961` | A | Merged in sam_header_stg (pull request #33914) | 2 |
| M213 | 2025-07-06 | `7d56b4fd119ea60d1b19e68eb227fe51d66034d3` | A | Merged in sam_header_stg (pull request #33981) | 0 |
| M214 | 2025-07-06 | `f38fe553cb8c8594a7f6925755e9f3d1451f982e` | A | Merged in sam_header_stg (pull request #33980) | 0 |
| M215 | 2025-07-07 | `29b1eed270e22752acde212898ed3c87a840816f` | A | Merged in sam_header_stg (pull request #33993) | 0 |
| M216 | 2025-07-07 | `fbaa4a0456ac86a19a4a52f05b114f85b2dfb30b` | A | Merged in sam_header_stg (pull request #33994) | 0 |
| M217 | 2025-07-07 | `919bfdeb4bd49aa12fd652a493e80ed1bd2a0890` | A | Merged in sam_header_stg (pull request #34006) | 0 |
| M218 | 2025-07-16 | `bc25c243a062eea2dadee13ff5806e93cc88f466` | A | Merged in sam_header_stg (pull request #34373) | 4 |
| M219 | 2025-07-17 | `417e9326ec37b00c7b2d3bc253728cae9c5f3e41` | A | Merged in sam_header_stg (pull request #34374) | 3 |
| M220 | 2025-07-17 | `11c6d1e8cd384dba06cd7265cd5536692cce2a00` | A | Merged in sam_header_stg (pull request #34452) | 2 |
| M221 | 2025-07-17 | `a736fe04e40b917885eedccdf4f96dbe207e11e9` | A | Merged in sam_header_stg (pull request #34451) | 4 |
| M222 | 2025-07-18 | `9108eff092027c5de52f7693904bb50c9b69ba90` | A | Merged in sam_header_stg (pull request #34467) | 2 |
| M223 | 2025-07-18 | `db33b0d2932f01dcde149de241195b1f5547ab4a` | A | Merged in sam_header_stg (pull request #34466) | 3 |
| M224 | 2025-07-18 | `fe536b32c7236a9819cd5c61f5725d1f00991959` | A | Merged in sam_header_stg (pull request #34538) | 1 |
| M225 | 2025-07-18 | `0390a7398edd791fbd76b960774c2823b6a5c244` | A | Merged in sam_header_stg (pull request #34540) | 1 |
| M226 | 2025-07-18 | `9bf273cf0fb5fcaf1bf1a2ba751b80f2cf704c76` | A | Merged in sam_header_stg (pull request #34558) | 2 |
| M227 | 2025-07-22 | `0d7f47f4880def517429e0cc828f9a690c73e9fe` | A | Merged in sam_header_stg (pull request #34682) | 0 |
| M228 | 2025-07-22 | `4ea8688b0906c8556fe7c1fbb145a2fea8f6f5bc` | A | Merged in sam_header_stg (pull request #34683) | 0 |
| M229 | 2025-07-22 | `aa7d1d691a09746ab8ff647b9c0b68e58d3f43be` | A | Merged in sam_header_stg (pull request #34684) | 0 |
| M230 | 2025-07-22 | `ff664b4cf64171a328e5d1b4b4038ad43236be73` | A+C | Merge branch 'pre-release' into sam_header_stg | 0 |
| M231 | 2025-07-23 | `fd54e5f468c06e6fc7a3164c0425ca2f83be45cb` | A | Merged in sam_header_stg (pull request #34716) | 0 |
| M232 | 2025-07-23 | `f960d42a351564b514013a914035e2ae561f29f4` | A | Merged in sam_header_stg (pull request #34685) | 1 |
| M233 | 2025-07-28 | `4367ad9f44634ff96cce1ea25cef1b5ca0d010d4` | A | Merged in sam_header_stg (pull request #34766) | 0 |
| M234 | 2025-07-28 | `98a74b5db469dcad147ba38e7dbd3e9b12e4379b` | A | Merged in sam_header_stg (pull request #34767) | 0 |
| M235 | 2025-07-29 | `52dfcbd9afa7fb3ac40eab95d37bc6be738701e3` | A | Merged in sam_header_stg (pull request #34791) | 0 |
| M236 | 2025-07-29 | `104fc6361cf6d41aa8142217099f0de49fa3a641` | A | Merged in sam_header_stg (pull request #34792) | 0 |
| M237 | 2025-08-06 | `5c40d435fe1958970c5545de18c1afa21ce6f4ce` | A | Merged in sam_header_stg (pull request #35097) | 0 |
| M238 | 2025-08-06 | `4381fb374d9fdb23de3c02fb094cf4ff03052432` | A | Merged in sam_header_stg (pull request #35098) | 0 |
| M239 | 2025-08-06 | `63a21ed7e4c79ac779c70a469205853a51b6fd47` | A+C | Merge branch 'staging' into sam_header_stg | 0 |
| M240 | 2025-08-08 | `3b72916df316d7899bff6037a5e00bb2df59bf85` | A+C | Merged in staging (pull request #35256) | 0 |
| M241 | 2025-08-11 | `88458a4c63f2d213acc21989472e2e32c11a61d0` | A | Merged in sam_header_stg (pull request #35237) | 0 |
| M242 | 2025-08-11 | `1043bdb35be401734e2dcb3ae15cf5ac19cd86a5` | A | Merged in sam_header_stg (pull request #35238) | 0 |
| M243 | 2025-08-11 | `8515858c4117cb76a5a020e0a4d0b078b48015df` | A+C | Merge branch 'sam_header_stg' into sam_header_stg | 0 |
| M244 | 2025-08-12 | `8114464c4491f9f704bc7d747e0bdded95f1be3a` | A+C | Merged in staging (pull request #35449) | 0 |
| M245 | 2025-08-12 | `fa54713221a8f07b0b757d9f04396bc4d3c54028` | A | Merged in sam_header_stg (pull request #35447) | 0 |
| M246 | 2025-08-12 | `c8f2210c713d16b69bb22cf3b607d8554144e55b` | A | Merged in sam_header_stg (pull request #35448) | 0 |
| M247 | 2025-08-13 | `f81ee16d85aba0fece5c25f8e71083a64a7f469e` | A | Merged in sam_header_stg (pull request #35546) | 0 |
| M248 | 2025-08-13 | `1f0b2fdbd15274553c57c84cd640df3a49bf7050` | A+C | Merge branch 'sam_header_stg' into sam_header_stg | 0 |
| M249 | 2025-08-14 | `989b2a726d2c76dddba2d4d8ffc1f17e80ed733b` | A | Merged in sam_header_stg (pull request #35547) | 0 |
| M250 | 2025-08-14 | `a998f33dc338dfa5da23b1cfe8cedbcda57bdfd3` | A | Merged in sam_header_stg (pull request #35628) | 1 |
| M251 | 2025-08-21 | `a22cb1d958e98a0c7bd98eee0ee35eddde2036ac` | A+C | Merged in staging (pull request #35909) | 1 |
| M252 | 2025-08-21 | `89cfaa9bea87769cb650f36b91008e428de549e7` | A | Merged in sam_header_stg (pull request #35895) | 0 |
| M253 | 2025-08-21 | `bd6ca96310e2559b64a10c7b41daafb677286d31` | A | Merged in sam_header_stg (pull request #35896) | 0 |
| M254 | 2025-08-22 | `34a5802f80651fc206b16873ceae6433d7120393` | A | Merged in sam_header_stg (pull request #35965) | 0 |
| M255 | 2025-08-22 | `1a56c58012d01678bd22770fa836546b51457ece` | A | Merged in sam_header_stg (pull request #35966) | 0 |
| M256 | 2025-08-22 | `20854a090a2319a57e6b437f50a2820fad25bf5d` | A+C | Merge branch 'sam_header_stg' into sam_header_stg | 0 |
| M257 | 2025-08-26 | `f27717bb925a27749063dba4cf7beada1b7548f4` | A+C | Merged in pre-release (pull request #36127) | 0 |
| M258 | 2025-08-26 | `cedfe94ea9c8c75c9d9012ee0eed1772041114bb` | A | Merged in sam_glossary (pull request #36093) | 0 |
| M259 | 2025-09-01 | `99562d37519b0d3ec6115b70b30905e1ead0c984` | A+C | Merged in staging (pull request #36288) | 0 |
| M260 | 2025-09-01 | `84b1a3c0bd31664e88ec0e9aa6694c9c24c7d053` | A | Merged in sam_header_stg (pull request #36289) | 0 |
| M261 | 2025-09-01 | `56b0a16b6c7529e812748f81fb18f0a69a78a22d` | A+C | Merge branch 'sam_header_stg' into sam_header_stg | 0 |
| M262 | 2025-09-02 | `4dfe2efa3fb801111cfcd8d0ab0fd352cbdd4147` | A | Merged in sam_header_stg (pull request #36290) | 0 |
| M263 | 2025-09-05 | `09a4703d3bbe1c0a18f77f910d79eb45879140d7` | A+C | Merge branch 'staging' into sam_header_stg | 1 |
| M264 | 2025-09-08 | `6611cddd09227766c4613a14d0a1cda5f5682bee` | A+C | Merge branch 'staging' into sam_header_stg | 8 |
| M265 | 2025-09-10 | `c59d7fc40f21934b7dcae0d017ed8f4923ea1ace` | A | Merged in email-dev-conf (pull request #36724) | 0 |
| M266 | 2025-09-10 | `d9210ceb6c2c20d7338381744bad9135179a6ee2` | A | Merged in email-q4-conf (pull request #36725) | 0 |
| M267 | 2025-09-10 | `9d70b9db7d483b5e8e99ad877fea5e93c3425548` | A+C | Merge branch 'staging' into sam_header_stg | 0 |
| M268 | 2025-09-10 | `fa8fe1aad14fb7a56a18ef2062e71524d6a743dd` | A+C | Merge branch 'sam_header_stg' into email-dev-conf | 2 |
| M269 | 2025-09-10 | `2b319ffa7c3d73292c050a94dbe7b30c48642d01` | A+C | Merge branch 'sam_header_stg' into email-q4-conf | 1 |
| M270 | 2025-09-11 | `860081dbb4b08230338674e49cd9179ff9465422` | A | Merged in sam_header_stg (pull request #36760) | 0 |
| M271 | 2025-09-11 | `842fac5c12c77fd8ce97f911aca72454eca07f30` | A | Merged in sam_header_stg (pull request #36761) | 0 |
| M272 | 2025-09-11 | `72d599da10eceb559f0578c81ed02a66f22c420b` | A | Merged in sam_header_stg (pull request #36784) | 0 |
| M273 | 2025-09-11 | `b77458dfb191987e5fe9c8f8a1ffe08966c9b644` | A | Merged in sam_header_stg (pull request #36785) | 0 |
| M274 | 2025-09-12 | `49df80f63dbe99aeb8393e91548badc54c928c5c` | A | Merged in sam_header_stg (pull request #36842) | 0 |
| M275 | 2025-09-12 | `e0be9473f741eb1128a3fece438e112a5e762663` | A | Merged in sam_header_stg (pull request #36843) | 0 |
| M276 | 2025-09-12 | `f7db2cbe48a6205f0f1f94bdd4dd460528abdb7c` | A | Merged in sam_header_stg (pull request #36739) | 0 |
| M277 | 2025-09-12 | `8f112320f5ce336217f90ef7ba66103180a55457` | A+C | Merge branch 'sam_header_stg' into sam_header_stg | 0 |
| M278 | 2025-09-12 | `a7ce780df7a44c9986ab77b52eedd1d776b55cee` | A+C | Merge branch 'staging' into sam_header_stg | 1 |
| M279 | 2025-09-24 | `35ed1c505fe81a85b21237c880198688ca38cd40` | A+C | Merge branch 'feature/agent-studio-global-server' into feature/agent-studio-global-server | 0 |
| M280 | 2025-09-29 | `e14c8bd37a7a305d63e80eba60c2725be507b42a` | A+C | Merge branch 'feature/agent-studio-global-server' into feature/agent-studio-global-server | 0 |
| M281 | 2025-09-30 | `963f062824eca6af2c586461ac63c8d5e2cd931a` | A | Merged in feature/agent-studio-global-server (pull request #37446) | 0 |
| M282 | 2025-09-30 | `24922a00178c87a324290b4d6bd6cbae3c53f124` | A+C | Merge branch 'feature/agent-studio-global-server' into feature/agent-studio-global-server | 2 |
| M283 | 2025-09-30 | `f493ada1ff4d7a76b693cb729e6e56475f4d14a9` | A+C | Merge branch 'feature/agent-studio-global-server' into feature/agent-studio-global-server | 0 |
| M284 | 2025-09-30 | `46829cda11449ebfadd3c4cdc6a72cc6e6372059` | A+C | Merge branch 'feature/agent-studio-global-server' into feature/agent-studio-global-server | 0 |
| M285 | 2025-10-02 | `e0ea72a9bb3d49b9c7e45fd8cbcf53e4ae374307` | A+C | Merge branch 'feature/agent-studio-global-server' into feature/agent-studio-global-server | 0 |
| M286 | 2025-10-02 | `efa7eec3b1935d55035d0c564f2ca95565627942` | A | Merged in feature/agent-studio-global-server (pull request #37534) | 0 |
| M287 | 2025-10-03 | `bc177601a9d27ea393f84f2a0a2208c01e4cf3cf` | A | Merged in feature/agent-studio-global-server (pull request #37573) | 0 |
| M288 | 2025-10-03 | `86d40d235c0c01a11c8f18ba9733bf7ccafb7de8` | A | Merged in feature/agent-studio-global-server (pull request #37574) | 0 |
| M289 | 2025-10-03 | `13682f49a896b8246e6c240b2bdb3415dd9fd5c0` | A+C | Merge branch 'feature/agent-studio-global-server' into feature/agent-studio-global-server | 0 |
| M290 | 2025-10-07 | `833cce36b8bfb8a35a43586e42b1bd1c7f18a8f8` | A | Merged in feature/agent-studio-global-server (pull request #37698) | 0 |
| M291 | 2025-10-07 | `0b3344c8dca2ceb99c5e6aa326e19444a98463bf` | A+C | Merge branch 'feature/agent-studio-global-server' into feature/agent-studio-global-server | 2 |
| M292 | 2025-10-15 | `1fd272743e417e9c16b1240fc7c4f48e0d552879` | A+C | Merge branch 'feature/agent-studio-global-server' into feature/agent-studio-global-server | 0 |
| M293 | 2025-10-16 | `7f8b9be15bf4153e149c90d8f03d1d16fa9519d7` | A+C | Merged in sam_agent_pre (pull request #38132) | 0 |
| M294 | 2025-10-17 | `a9cd081bab067a5d0747d51941f3a10020199b91` | A | Merged in sam_agent_pre (pull request #38123) | 0 |
| M295 | 2025-10-17 | `3ea4af1fa63a8b0b6981f0adb10ebd877e768ef0` | A | Merged in sam_agent_pre (pull request #38124) | 0 |
| M296 | 2025-10-17 | `028cdb193b723caa952fa422d0d0cad807f47bc5` | A | Merged in sam_agent_pre (pull request #38150) | 0 |
| M297 | 2025-10-17 | `e245c61968e3dfa63ffc72178a0c5851167988c5` | A | Merged in sam_agent_pre (pull request #38149) | 0 |
| M298 | 2025-10-22 | `2609716823394e9b7ae29ddcc2bcd03878d77315` | A | Merged in sam_agent_pre (pull request #38186) | 0 |
| M299 | 2025-10-22 | `f8427b3e5b01a7b55592490de53ccc15c69ee028` | A | Merged in sam_agent_pre (pull request #38185) | 0 |
| M300 | 2025-10-22 | `54579cf350cd74714d7537d82326242bd163e75d` | A | Merged in sam_agent_pre (pull request #38188) | 0 |
| M301 | 2025-10-22 | `df635cfb68273e76e223debfb31ba26a872091f4` | A | Merged in sam_agent_pre (pull request #38189) | 0 |
| M302 | 2025-10-23 | `8a7381ea64c92f9a4139891cc815eebeb9ff8631` | A | Merged in sam_agent_pre (pull request #38262) | 0 |
| M303 | 2025-10-23 | `9d3a27ce9cb76d45a9cf65f3a3f36123098b91d1` | A | Merged in sam_agent_pre (pull request #38263) | 0 |
| M304 | 2025-10-23 | `7271c6837dd7442e3ce5ea6cfa6a2457fe77c21f` | A | Merged in sam_agent_pre (pull request #38264) | 0 |
| M305 | 2025-10-23 | `11989d3c542b593a8911299fe73c14a1963480d1` | A | Merged in sam_agent_pre (pull request #38265) | 0 |
| M306 | 2025-11-04 | `7f210dc65a29a6eef2e6c82b2aea74422b885ea4` | A+C | Merge branch 'gk_ag_st_prls' into feature/RES-160161 | 0 |
| M307 | 2025-11-05 | `3db5e57ae88733fd962d0a4a1d2508f5c55327c6` | A | Merged in feature/RES-160161 (pull request #38694) | 1 |
| M308 | 2025-11-05 | `50b223317e407a4b3c4e85db0974c495ea6e24e5` | A+C | Merge branch 'staging' into feature/RES-160161 | 0 |
| M309 | 2025-11-07 | `e7727ec733d0aff445f34b9b11438a82b67d0ecf` | A | Merged in preethi_agent_pre (pull request #38839) | 0 |
| M310 | 2025-11-19 | `d532d33f203557d664a7c0ef92f8526d6a858bbd` | A | Merged in feature/RES-160161 (pull request #38693) | 1 |
| M311 | 2025-11-19 | `7eb89254540f0ebf0d5f4b0ada36109005db96fe` | A | Merged in feature/RES-160161 (pull request #39238) | 1 |
| M312 | 2025-11-20 | `1f8f36c667edceb1ed9fcedbe1265f95c952f063` | A | Merged in pre-release (pull request #39301) | 0 |
| M313 | 2026-05-27 | `fa974acac536dddea3e9cd635f0efcfcad9bf4f9` | A+C | Merge branch 'staging' into RES-177486 | 1 |
| M314 | 2026-07-02 | `9c01cb9058e5950a538a4ff3bb3d708df2711bde` | A+C | Merge branch 'mavericks_hackfest' into mavericks_hackfest | 4 |
| M315 | 2026-07-02 | `c7fd2add8818850bf0e8d6de314fbf1005a25e3a` | A+C | Merge branch 'mavericks_hackfest' into mavericks_hackfest | 1 |
| M316 | 2026-07-11 | `791ed062c75c474864f7115a7006ab15b8470255` | A+C | Merge branch 'mavericks_hackfest' into mavericks-copy | 2 |
| M317 | 2026-07-12 | `68e563fa17497f004df31d3102140da730fdf0bf` | A+C | Merge branch 'mavericks-copy' into mavericks-copy | 0 |
| M318 | 2026-08-06 | `3f37a9f87f00014c7861d8cbdfa78ecb4750e187` | A+C | Merge branch 'development' into company-user-load-details-removal | 5 |
| M319 | 2026-08-06 | `809b58eff23ae4b91865801e4773eb4c421b0122` | A+C | Merge remote-tracking branch 'origin/development' into company-user-load-details-removal-dev-sync | 0 |
| M320 | 2026-08-12 | `32e6400ff5989248d69254dc10334ac7a88392bb` | A+C | Merge branch 'pre-release' into sam-company-user-load-details-removal | 5 |
| M321 | 2026-08-12 | `5077ecb8f06b63e38eac4759caf97baf887f032c` | A | Merge pull request #9077 from responsive-core/sam-company-user-load-details-removal | 0 |
| M322 | 2026-08-14 | `0aff1d7d74e55cf9321be58549b1c07e7bd7d777` | A | Merge pull request #9205 from responsive-core/sam-company-user-load-details-removal | 0 |
| M323 | 2026-09-02 | `4da2187dd5171baa8d86d74dec2abe0ba9336377` | A+C | On sam-company-user-load-details-removal: sonarqube coverage aggregation changes | 4 |

## Changed-module/path index for future investigation

Repository-relative paths below are the actual historical changed paths in the classified nonmerge corpus; some modules later moved under `rfp-response-project`, `rfp-content-library`, `rfp-import-export` or `rfp-release`. Paths and class names locate evidence; presence in a grouped patch does not imply original ownership of the complete file. Refer to SHA-specific trees when a current path is absent. Only filenames/module identifiers are persisted, not confidential code.

### SERVER-001 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/users/rest/AdminAPI.java`
- `rfp-commons/src/main/java/com/rfpio/server/users/services/UserService.java`

### SERVER-002 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/users/rest/AdminAPI.java`
- `rfp-commons/src/main/java/com/rfpio/server/users/rest/UsersAPI.java`
- `rfp-commons/src/main/java/com/rfpio/server/users/services/UserService.java`

### SERVER-003 — changed paths

- `rfpio-auth-pod-commons-service/src/main/java/com/rfpio/server/auth/security/util/TimeBasedOneTimePasswordUtil.java`

### SERVER-004 — changed paths

- `rfpio-import-services/src/main/java/com/rfpio/server/importservice/util/ExtractCssStyleFromDocxUtil.java`

### SERVER-005 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper250502.java`
- `rfpio-auth-service-base/src/main/java/com/rfpio/server/company/dao/PODDetailsDAO.java`
- `rfpio-microservice-projects/rfpio-daily-report/src/main/java/com/rfpio/server/daily/report/process/service/DailyReportProcess.java`
- `rfpio-microservice-projects/rfpio-daily-report/src/main/java/com/rfpio/server/daily/report/process/service/DailyReportService.java`

### SERVER-006 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/company/bu/rest/CompanyBusinessUnitAPI.java`
- `rfp-commons/src/main/java/com/rfpio/server/users/dao/UsersDAO.java`
- `rfp-commons/src/main/java/com/rfpio/server/users/rest/AdminAPI.java`
- `rfp-commons/src/main/java/com/rfpio/server/users/rest/UsersAPI.java`
- `rfp-commons/src/main/java/com/rfpio/server/users/services/UserService.java`
- `rfp-commons/src/main/java/com/rfpio/server/users/vo/UserInfoSearchVO.java`
- `rfp-commons/src/test/java/com/rfpio/server/company/bu/rest/CompanyBusinessUnitAPITest.java`
- `rfp-commons/src/test/java/com/rfpio/server/users/dao/UsersDAOTest.java`
- `rfp-commons/src/test/java/com/rfpio/server/users/rest/AdminAPITest.java`
- `rfp-commons/src/test/java/com/rfpio/server/users/rest/UsersAPITest.java`
- `rfp-response-project/rfp-projects-impl/src/main/java/com/rfpio/server/company/rest/UserLoadRequestAPI.java`

### SERVER-007 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/users/dao/UsersDAO.java`

### SERVER-008 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/commons/dao/BaseDiscussionDAO.java`
- `rfp-projects-impl/src/main/java/com/rfpio/server/discussions/dao/LibraryDiscussionDAO.java`
- `rfp-projects-impl/src/main/java/com/rfpio/server/discussions/dao/ProjectDiscussionsDAO.java`
- `rfp-projects-impl/src/main/java/com/rfpio/server/discussions/rest/ProjectDiscussionsAPI.java`
- `rfp-projects-impl/src/main/java/com/rfpio/server/discussions/service/LibraryDiscussionService.java`
- `rfp-projects-impl/src/main/java/com/rfpio/server/discussions/service/ProjectDiscussionsService.java`
- `rfpio-commons-base/src/main/java/com/rfpio/server/projects/base/discussions/vo/CommentVO.java`

### SERVER-009 — changed paths

- `rfp-projects-impl/src/main/java/com/rfpio/server/projects/process/ProjectTemplateCopyOverProcess.java`
- `rfp-projects-impl/src/main/java/com/rfpio/server/projects/service/ProjectsService.java`
- `rfpio-external-pod-commons-base/src/main/java/com/rfpio/server/projects/vo/activity/ProjectActivityType.java`
- `rfpio-external-pod-commons-base/src/main/java/com/rfpio/server/projects/vo/activity/ProjectEntity.java`

### SERVER-010 — changed paths

- `rfpio-commons-base/src/main/java/com/rfpio/server/users/vo/UserInfoVO.java`
- `rfpio-utils/src/main/java/com/rfpio/server/utils/HTMLContentParserUtils.java`

### SERVER-011 — changed paths

- `scripts/db_index/auth_service/metadata.js`
- `scripts/migration/2023/23_01_01/db/rfpio_authentication.js`
- `scripts/migration/2023/23_01_04/db/rfpio_authentication.js`

### SERVER-012 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/users/rest/AdminAPI.java`
- `rfpio-commons-base/src/main/java/com/rfpio/server/company/model/CompanyInfoVO.java`

### SERVER-013 — changed paths

- `rfpio-electronic-signature/src/main/java/com/rfpio/server/esign/bulk/service/EsignBulkService.java`

### SERVER-014 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/users/services/UserService.java`
- `rfpio-commons-db/src/main/java/com/rfpio/server/properties/constants/PropertiesConstants.java`
- `scripts/db_index/auth_service/metadata.js`

### SERVER-015 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/commons/vo/CompanyActivitiesSearchVO.java`
- `rfp-commons/src/main/java/com/rfpio/server/master/dao/OrganizationActivitiesDAO.java`
- `rfp-commons/src/main/java/com/rfpio/server/master/service/OrganizationActivityService.java`
- `rfpio-external-pod-commons-base/src/main/java/com/rfpio/server/master/vo/OrganizationActivityVOList.java`

### SERVER-016 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/commons/utils/VelocityEngineUtils.java`
- `rfp-commons/src/main/java/com/rfpio/server/emailtemplate/service/EmailTemplateService.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper250404.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationV2Process.java`
- `rfp-commons/src/main/java/com/rfpio/server/users/services/UserService.java`
- `rfp-commons/src/main/resources/emailTemplates/VM_global_library.vm`
- `rfp-commons/src/main/resources/emailTemplates/newMainTemplateV2.vm`
- `rfp-projects-impl/src/main/java/com/rfpio/server/projects/mail/NotificationBuilder.java`
- `rfp-projects-impl/src/main/java/com/rfpio/server/projects/mail/ProjectNotificationBuilder.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250327.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250529.java`
- `scripts/db_index/pod/email_template_intake.js`
- `scripts/db_index/pod/email_template_project.js`
- `scripts/db_index/pod/email_template_section.js`

### SERVER-017 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/commons/utils/VelocityEngineUtils.java`
- `rfp-commons/src/main/java/com/rfpio/server/emailtemplate/service/EmailTemplateService.java`
- `rfp-commons/src/main/java/com/rfpio/server/master/vo/TranslateVO.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper250424.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper250429.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper250502.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper250508.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper250828.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelperNew.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationV2Process.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationV2Process250313.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationV2Process250424.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationV2Process250429.java`
- `rfp-commons/src/main/resources/EmailTemplateMetadata.json`
- `rfp-commons/src/main/resources/emailTemplates/mainTemplateV2.vm`
- `rfp-projects-impl/src/main/java/com/rfpio/server/projects/mail/NotificationBuilder.java`
- `rfp-projects-impl/src/main/java/com/rfpio/server/projects/mail/ProjectNotificationBuilder.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/constants/DBMigrationHelper.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/constants/EmailTemplateEnum.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250130.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250327.java`
- `rfp-release/rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250925.java`
- `rfpio-microservice-projects/rfpio-daily-report/src/main/java/com/rfpio/server/daily/report/process/service/DailyReportProcess.java`
- `scripts/db_index/pod/email_template_project.js`

### SERVER-018 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/commons/utils/VelocityEngineUtils.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper250404.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper250424.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper250429.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper250502.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper250506.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper250508.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelper250828.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationHelperNew.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationV2Process.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationV2Process250313.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationV2Process250424.java`
- `rfp-commons/src/main/java/com/rfpio/server/process/EmailTemplateMigrationV2Process250429.java`
- `rfp-commons/src/main/resources/emailTemplates/VM_global_library.vm`
- `rfp-commons/src/main/resources/emailTemplates/mainTemplateV2.vm`
- `rfp-projects-impl/src/main/java/com/rfpio/server/projects/mail/NotificationBuilder.java`
- `rfp-projects-impl/src/main/java/com/rfpio/server/projects/mail/ProjectNotificationBuilder.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/constants/DBMigrationHelper.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/constants/EmailTemplateEnum.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250327.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250429.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250502.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250506.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250508.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250529.java`
- `rfp-release/rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250925.java`
- `rfp-webapp/src/main/resources/translate/french.js`
- `scripts/db_index/pod/email_template_company.js`
- `scripts/db_index/pod/email_template_intake.js`
- `scripts/db_index/pod/email_template_issue_tracking.js`
- `scripts/db_index/pod/email_template_project.js`
- `scripts/db_index/pod/email_template_question.js`
- `scripts/db_index/pod/email_template_section.js`
- `scripts/db_index/pod/email_template_team.js`

### SERVER-019 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/emailtemplate/service/EmailTemplateService.java`

### SERVER-020 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/users/services/UserService.java`
- `rfpio-auth-pod-commons-service/src/main/java/com/rfpio/server/integration/service/RfpioExternalIntegrationService.java`
- `rfpio-auth-service-wrapper/src/main/java/com/rfpio/server/external/service/verification/call/ExternalIntegrationServiceBeanCall.java`
- `rfpio-auth-service-wrapper/src/main/java/com/rfpio/server/external/service/verification/call/ExternalIntegrationServiceRestCall.java`
- `rfpio-external-controller/src/main/java/com/rfpio/server/external/integration/crm/controller/HubspotController.java`
- `rfpio-external-controller/src/main/java/com/rfpio/server/external/security/interceptors/ExternalRequestInterceptors.java`
- `rfpio-integration-sharepoint/src/main/java/com/rfpio/server/integration/sharepoint/SharePointAuthorization.java`
- `rfpio-integration-sharepoint/src/main/java/com/rfpio/server/integration/sharepoint/SharePointService.java`

### SERVER-021 — changed paths

- `rfpio-integration-bot/src/main/java/com/rfpio/server/integration/bot/SlackIntegrationService.java`
- `rfpio-integration-bot/src/main/java/com/rfpio/server/integration/slack/markdown/SlackMarkdownFactory.java`

### SERVER-022 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/commons/utils/RFPConstants.java`
- `rfp-commons/src/main/java/com/rfpio/server/company/integrations/dao/CompanyIntegrationDetailsDAO.java`
- `rfp-commons/src/main/java/com/rfpio/server/users/services/UserService.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250529.java`
- `rfpio-integration-sharepoint/src/main/java/com/rfpio/server/integration/sharepoint/SharePointAuthorization.java`
- `rfpio-integration-sharepoint/src/main/java/com/rfpio/server/integration/sharepoint/SharePointService.java`

### SERVER-023 — changed paths

- `ask-responsive/src/main/java/com/rfpio/server/ask/constants/AskConstants.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/service/ResponsiveAskService.java`
- `configs/solr 9/configsets/knn_conf_v3/conf/managed-schema.xml`
- `rfp-commons/src/main/java/com/rfpio/server/content/library/vo/HistoricalSearchResponseVO.java`
- `rfp-projects-impl/src/main/java/com/rfpio/server/ai/process/AiAutoRespondProcess.java`
- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250626.java`
- `rfpio-answerlibrary/src/main/java/com/rfpio/server/answerlibrary/dao/AnswerLibraryDAO.java`
- `rfpio-answerlibrary/src/main/java/com/rfpio/server/answerlibrary/process/ContentLibraryBulkUpdateProcess.java`
- `rfpio-answerlibrary/src/main/java/com/rfpio/server/answerlibrary/service/AnswerLibraryService.java`
- `rfpio-answerlibrary/src/main/java/com/rfpio/server/answerlibrary/utils/AnswerLibraryUtils.java`
- `rfpio-answerlibrary/src/main/java/com/rfpio/server/content/library/constants/AiConstants.java`
- `rfpio-answerlibrary/src/main/java/com/rfpio/server/content/library/dao/AIDatasetDAO.java`
- `rfpio-answerlibrary/src/main/java/com/rfpio/server/content/library/rest/BaseAIDatasetAPI.java`
- `rfpio-answerlibrary/src/main/java/com/rfpio/server/content/library/services/AIDatasetService.java`
- `rfpio-answerlibrary/src/main/java/com/rfpio/server/content/library/services/AiSearchService.java`
- `rfpio-answerlibrary/src/main/java/com/rfpio/server/content/library/services/ContentLibraryBaseService.java`
- `rfpio-answerlibrary/src/main/java/com/rfpio/server/content/library/services/ContentLibraryCreateUpdateService.java`
- `rfpio-answerlibrary/src/main/java/com/rfpio/server/search/service/ContentLibraryAISyncProcess.java`
- `rfpio-answerlibrary/src/test/java/com/rfpio/server/content/library/services/AiSearchServiceTest.java`
- `rfpio-commons-base/src/main/java/com/rfpio/server/company/model/VectorDimension.java`
- `rfpio-commons-db/src/main/java/com/rfpio/server/commonsdb/constants/MongoDBConstants.java`
- `rfpio-mongo-search/src/main/java/com/rfpio/server/dao/MongoSearchDAO.java`
- `rfpio-mongo-search/src/main/java/com/rfpio/server/service/MongoSearchService.java`
- `rfpio-search-service/src/main/java/com/rfpio/server/search/constants/SearchConstants.java`
- `rfpio-search-service/src/main/java/com/rfpio/server/search/engine/ISearchService.java`
- `rfpio-search-service/src/main/java/com/rfpio/server/search/service/AbstractSearchService.java`
- `rfpio-search-service/src/main/java/com/rfpio/server/search/service/RfpioSearchService.java`
- `rfpio-search-service/src/main/java/com/rfpio/server/search/vo/base/BaseFilterVO.java`
- `rfpio-search-service/src/main/java/com/rfpio/server/search/vo/request/IndexContentVO.java`
- `rfpio-solr-search/src/main/java/com/rfpio/server/search/engine/service/SolrConnectionService.java`
- `rfpio-solr-search/src/main/java/com/rfpio/server/search/engines/SolrSearchEngine.java`
- `scripts/migration/2025/25_06_04/db/rfp.js`
- `scripts/migration/2025/25_06_26/db/rfp.js`

### SERVER-024 — changed paths

- `rfp-webapp/src/main/java/com/rfpio/server/core/process/AiResponseHeaderSyncProcess.java`
- `rfpio-answerlibrary/src/main/java/com/rfpio/server/answerlibrary/dao/AnswerLibraryDAO.java`
- `rfpio-answerlibrary/src/main/java/com/rfpio/server/answerlibrary/process/ContentLibraryBulkUpdateProcess.java`
- `rfpio-mongo-search/src/main/java/com/rfpio/server/dao/MongoSearchDAO.java`
- `rfpio-mongo-search/src/main/java/com/rfpio/server/service/MongoSearchService.java`
- `rfpio-search-service/src/main/java/com/rfpio/server/search/engine/ISearchService.java`
- `rfpio-search-service/src/main/java/com/rfpio/server/search/service/RfpioSearchService.java`
- `rfpio-solr-search/src/main/java/com/rfpio/server/search/engine/service/SolrConnectionService.java`
- `rfpio-solr-search/src/main/java/com/rfpio/server/search/engines/OpenSearchEngine.java`
- `rfpio-solr-search/src/main/java/com/rfpio/server/search/engines/SolrSearchEngine.java`
- `scripts/migration/2025/25_06_04/db/rfp.js`
- `scripts/migration/2025/25_06_26/db/rfp.js`
- `scripts/migration/2025/25_07_05/db/rfp.js`


### SERVER-025 — changed paths

- `rfpio-auth-pod-commons-service/src/main/java/com/rfpio/server/company/service/CompanyAuthService.java`
- `rfpio-auth-service-base/src/main/java/com/rfpio/server/company/dao/CompanyDAO.java`
- `rfpio-auth-service-base/src/main/java/com/rfpio/server/company/dao/PODDetailsDAO.java`
- `rfpio-microservice-projects/rfpio-daily-report/src/main/java/com/rfpio/server/daily/report/process/service/DailyReportService.java`

### SERVER-026 — changed paths

- `rfp-commons/src/main/java/com/rfpio/server/company/glossary/dao/ResponsiveGlossaryDAO.java`
- `rfp-commons/src/main/java/com/rfpio/server/company/glossary/rest/ResponsiveGlossaryApi.java`
- `rfp-commons/src/main/java/com/rfpio/server/company/glossary/service/ResponsiveGlossaryService.java`
- `translation-service/src/main/java/com/rfpio/server/translation/service/RfpioDeepLTranslateService.java`
- `translation-service/src/main/java/com/rfpio/server/translation/service/RfpioTranslationService.java`

### SERVER-027 — changed paths

- `ask-responsive/src/main/java/com/rfpio/server/ask/dao/ResponsiveAskConversationDAO.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/dao/ResponsiveAskPromptDAO.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/vo/ConversationVO.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/vo/PromptResponseSetVO.java`
- `rfpio-agent-studio/src/main/java/com/rfpio/server/agent/studio/controller/AgentStudioAPI.java`
- `rfpio-agent-studio/src/main/java/com/rfpio/server/agent/studio/service/AgentsStudioService.java`
- `rfpio-agent-studio/src/main/java/com/rfpio/server/agent/studio/service/ResearchAgentStudioService.java`
- `rfpio-agent-studio/src/test/java/com/rfpio/server/agent/studio/controller/ResearchAgentStudioAPITest.java`
- `rfpio-agent-studio/src/test/java/com/rfpio/server/agent/studio/service/ResearchAgentStudioServiceTest.java`
- `rfpio-ai-agent/src/main/java/com/rfpio/server/ai/agent/dto/AgentQueryRequestVO.java`
- `rfpio-ai-agent/src/main/java/com/rfpio/server/ai/agent/service/ConversationManager.java`

### SERVER-028 — changed paths

- `rfp-release/rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess250925.java`
- `rfp-release/rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess251030.java`

### SERVER-029 — changed paths

- `ask-responsive/pom.xml`
- `ask-responsive/src/main/java/com/rfpio/server/ask/controller/ResponsiveAskController.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/dao/AiSourceConnectionSessionDAO.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/service/AiSourceConnectionSessionService.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/service/ChildItemDiscoveryService.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/service/ExternalSourceAuthSchemaService.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/service/ExternalSourceIndexingService.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/service/ResponsiveAskLLMService.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/service/RootNodeDiscoveryService.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/vo/AiSourceConnectionSessionVO.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/vo/ChildItemDiscoveryResponse.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/vo/ExternalSourceAuthSchemaVO.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/vo/ExternalSourceFolderItem.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/vo/ExternalSourceIndexRequest.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/vo/ExternalSourceIndexResponse.java`
- `ask-responsive/src/main/java/com/rfpio/server/ask/vo/SelectedChildSourceItem.java`
- `connectors-base/src/main/java/com/responsive/connectors/core/api/ExternalSourceConnectorApi.java`
- `connectors-base/src/main/java/com/responsive/connectors/core/db/ConnectorConfigDAO.java`
- `connectors-base/src/main/java/com/responsive/connectors/service/ResponsiveExternalService.java`

### SERVER-030 — changed paths

- `sonarqube/__init__.py`
- `sonarqube/sonarqube_components.jsonc`
- `sonarqube/sonarqube_report.py`
- `sonarqube/sonarqube_slack.py`
- `sonarqube/sonarqube_utils.py`
- `sonarqube/test_sonarqube_utils.py`

### SERVER-035 — changed paths

- `rfp-release-migrations/src/main/java/com/rfpio/server/release/migration/db/DBMigrationProcess241107.java`
- `scripts/migration/2025/25_06_04/assests/SMB-Emerging-Edition-User-Guide.pdf`
- `scripts/migration/2025/25_06_04/db/rfp.js`


## Updated backend resume-ready evidence table

Use the factual action and ownership boundary together. CODE/PR rows support personal implementation only for the candidate's anchored changes. Resume-supported claims remain available with their provenance; friend implementations and unresolved filler wording are retained for attributed learning/history rather than rewritten as personal achievements. These are building blocks for tailoring, not a claim that every row belongs in one resume.

| ID | Factual contribution / application-ready material | Outcome, evidence and ownership boundary | JD keywords |
|---|---|---|---|
| SERVER-001 | Added support-aware service validation blocking non-support username changes to super-admin targets. | CODE; S production context; current guard retained. No universal account-takeover or security metric. | Java, API authorization, privileged access |
| SERVER-002 | Evolved selective-user lookup contract and bulk onboarding validation, permission checks, license errors and stable response keys. | CODE; historical/current collaborative user management. No throughput claim or original system ownership. | REST contracts, validation, MongoDB, tenant scoping |
| SERVER-003 | Repaired an existing TOTP enrollment QR URL/provider and query delimiter. | CODE; historical compatibility fix later superseded by colleague's local QR. Not OTP/Redis engine authorship. | authentication debugging, TOTP, integration maintenance |
| SERVER-004 | Preserved DOCX default/fallback font through paragraph/character style extraction. | CODE; current behavior retained; POI/XWPF system already existed. | Java, document parsing, defensive defaults |
| SERVER-005 | Isolated daily-report company failures, logged exception context and validated missing numeric/text/retention data. | CODE; S reporting baseline; later companies continue after a company failure. No retries/SLA/success-rate metric. | Spring Boot context, resilience, reporting, logging |
| SERVER-006 | Consolidated BU membership lists/user metadata into one permission-checked API; refactored targeted directory/DAO contracts and mocked tests. | CODE/PR/S: **one Java API call**; merged, deployment unverified. Collaborator parts separately credited. | Java, REST, MongoDB, DAO, JUnit, Mockito |
| SERVER-007 | Added selective Mongo user-list projection to reduce disclosure. | CODE: 11 excluded Mongo fields in one query path; Historical S **15+ response fields** wording retained as INVENTED (USER-CONFIRMED); same SBOM initiative per earlier U answer. | API security, data minimization, MongoDB projection |
| SERVER-008 | Added persistent per-user discussion hiding/unhiding, mention-driven visibility and E-Sign/My Work compatibility. | CODE; company/project-scoped Mongo positional updates; no quantified performance gain. | workflow APIs, MongoDB, state handling |
| SERVER-009 | Extended the project-template copy process to emit organization activity with company/creator/entity metadata. | CODE; internship-period existing-pipeline extension, not whole pipeline implementation. | background processing, activity metadata, Java |
| SERVER-010 | Fixed Java map/list/null static-analysis issues and guarded delegated user-model access. | CODE; narrow Sonar/null-safety work. No full CI ownership. | Java, static analysis, troubleshooting |
| SERVER-011 | Added/refined Mongo grammar-preference renaming/default-provider migration scripts. | CODE; migration intent; execution/record count/idempotency unknown. | MongoDB, migrations, compatibility |
| SERVER-012 | Validated blank KMS key parameters in existing feature-gated BYOK API paths. | CODE; parameter handling, not KMS/encryption/session architecture. | REST validation, BYOK maintenance |
| SERVER-013 | Normalized numeric Excel cell text for E-Sign bulk-send labels using POI conversion. | CODE; unwanted suffix repair, no broader signature-system ownership. | Java, Excel import, data normalization |
| SERVER-014 | Repaired default password settings, protected activation status and added community URL fallback. | CODE; targeted authentication/settings behavior, not a complete rebuilt backend auth system. | state validation, configuration, auth debugging |
| SERVER-015 | Added offset pagination and matching filtered total counts to organization-activity retrieval. | CODE; shared DAO query/list-count consistency. No index or measured latency gain. | MongoDB, pagination, DAO refactoring |
| SERVER-016 | Updated backend email data/routing and shared Velocity rendering for V2 workflows while preserving legacy guest links. | CODE; notification/delivery infrastructure pre-existed. | Java, Velocity, compatibility, API/UI contracts |
| SERVER-017 | Built/refined tenant-aware email-template migration preserving edited content through metadata/HTML transformation and Mongo writes. | CODE; shared/dedicated databases, release job scheduling, null/error diagnostics. No exactly-once/verified rollout guarantee. | Java jobs, MongoDB bulk writes, data migration |
| SERVER-018 | Repaired shared server-generated HTML templates/macros for Gmail/Outlook and workflow context errors. | CODE; repeated revisions consolidated, no rendered QA metric. | server rendering, HTML compatibility, Velocity |
| SERVER-019 | Added template IDs to email anchor URLs and corrected wrapping for module-specific email content. | CODE; link metadata, not ownership of tracking analytics. | URL handling, Jsoup, rendering contracts |
| SERVER-020 | Instrumented integration requests and narrowed debugging context for HubSpot/auth/SharePoint troubleshooting. | CODE; logs do not prove the separate resume **30% MTTR** measurement. Historical header logging not established sanitized. | diagnostics, production debugging, integrations |
| SERVER-021 | Normalized Slack Markdown to plain-text search terms while retaining HTML for display paths. | CODE; parser/refactoring repair, no relevance benchmark. | Slack integration, parsing, search |
| SERVER-022 | Repaired SharePoint relevance sorting and Mongo integration ID/upsert handling. | CODE; Rank sort, ObjectId validation and alternate scoped updates. No general uniqueness/concurrency guarantee. | external APIs, MongoDB, validation, troubleshooting |
| SERVER-023 | Propagated response headers through Mongo/Solr ingest/index filters and AI answer context. | CODE/S; RAG metadata/retrieval scope; collaborator final mapper/import fixes credited separately. | Solr, MongoDB, vector search, RAG, Java |
| SERVER-024 | Added bulk header-index updates and bounded, logged backfill tooling reading source answer records. | CODE/S; atomic Solr field updates/Mongo bulk writes, no cross-store transaction/retry/volume guarantee. | migration tooling, search consistency, thread pools |
| SERVER-025 | Split administrator/pod lookups and corrected pod ID versus display-name response contracts. | CODE; support/API response maintenance, not regional platform architecture. | DAO refactoring, support tooling, API contracts |
| SERVER-026 | Added tenant glossary REST/DAO and DeepL no-translate HTML/phrase handling, including absent-document repair. | CODE; prototype evolves into current code, production rollout unknown; original translation client already existed. | REST, MongoDB, DeepL, Unicode, Jsoup |
| SERVER-027 | Persisted agent inputs/conversation/canvas sections for reopen and repaired V1 compatibility. | CODE; existing runtime used; removed iterations/@Ignore tests explicit; no personal ADK/SSE/model architecture claim. | AI applications, MongoDB persistence, DTOs, Markdown |
| SERVER-028 | Corrected region-restriction preference initialization in auth release hooks. | CODE; missing-value migration, not geolocation policy enforcement. | MongoDB, release tooling, compatibility |
| SERVER-029 | Implemented July prototype external-resource discovery/index/session contracts; retain June hackathon authenticated execution baseline separately. | CODE July feature branch; F/S June **5+ services** including Chorus/Jira, later production evolution resume-only. No universal provider/token-refresh claim. | AI integrations, OAuth/API tokens, discovery, connector state |
| SERVER-030 | Corrected Sonar module coverage by summing raw counters, filtering overlapping paths and reporting partial data. | CODE/PR; **11 Python tests passed** in audit; same patch across merged PRs counted once. Not Java coverage improvement. | Python, SonarQube, testing, reporting |
| SERVER-031 | Reviewed backend encryption/import/Sonar changes and requested JUnit coverage; coordinated an Arthi integration PR. | PR; collaborator implementation; blank/dismissed reviews preserved. No inferred leadership/design quality. | code review, test review, integration coordination |
| SERVER-032 | Learning/discussion topics: friend's SSE real-time and Redis/OTP guest-session systems. | U explicitly friend-implemented; historical **60% polling** metric retained with friend/resume provenance, not personal outcome. | SSE, Redis, OTP, sessions (learning) |
| SERVER-033 | Preserve resume-only ELK incident analysis/30% MTTR; record broad internship pipeline and Docker/Sonar-Jenkins wording plus U's filler clarification. | F/S/U; broad personal implementation unverified; use narrower verified work above. | ELK, root-cause analysis; pipeline/CI scope unresolved |
| SERVER-034 | Freelance GraphQL/Neon commerce backend, PayRam/license assignment, two OAuth providers, RBAC, S3/Vercel/VPS/SMTP. | F/S PROJECT/PRODUCTION; source outside employer repo, no employer attribution. | GraphQL, PostgreSQL, payments, OAuth, deployment |
| SERVER-035 | Added targeted custom-field release cleanup and SMB guide asset/upload-instruction support. | CODE; execution, deletion count, PDF authorship and S3 upload unknown. | release migration, MongoDB, maintenance |
| SERVER-036 | Reconciled integration contracts and null-safe file-list/serialization behavior in merge resolutions. | Combined-diff CODE; merge metadata alone does not prove implementation ownership. | compatibility, conflict resolution, collaboration |

## Factual application-answer building blocks

- **BU/data minimization:** describe the permissions/session-company check, Mongo scope/projection, server-side membership partition and combined lists/user map. Explain collaborator directory changes and legacy V1 compatibility. State one resulting API call; original call count and timing are unknown.
- **Reporting resilience:** explain why an exception around a whole company loop prevented later processing, how moving the catch inside isolates that company, and how diagnostics/missing-cell guards avoid misleading report values. A partial report can still be incomplete; no retry or complete recovery claim.
- **Search consistency:** trace response-header keys from answer records to stored/index metadata, query filters and AI context, then normal bulk updates and historical backfill. Distinguish atomic index field updates from cross-store transactions. Existing embedding/model generation is outside personal scope.
- **Migration maintenance:** explain customized HTML/default-label comparisons, shared/dedicated database handling, metadata snapshots, text-node preservation, batching and logged partial failures. Scheduling a PENDING job does not prove rollout; pending-job guards are not global idempotency.
- **Authorization:** explain the trusted support flag and target super-admin role check before mutation. Other user-management validators, lock/batch code and error translation pre-existed or were changed by collaborators.
- **Translation integration:** describe tenant glossary API authorization, Mongo upsert, recursive eligible text-node handling, longer-phrase matching and DeepL ignored XML tags, with absent-glossary handling. Do not claim the original HTTP/credential implementation or accuracy improvement.
- **Agent application state:** describe input/DTO fields, conversation/prompt persistence and Markdown sections that allow reopening a canvas. Distinguish application integration from model/ADK runtime ownership and disclose historical disabled tests when relevant.
- **Tooling:** explain raw covered/uncovered counters and why averaging module percentages is wrong, ancestor-path overlap removal, missing-metric N/A behavior and the 11 actual tests. Keep this separate from unresolved Jenkins/Docker implementation wording.

## Conflicts and proposed cross-context corrections — not edited here

1. **SSE/Redis personal attribution:** F/S and prior contexts describe candidate implementation; U explicitly identifies friend implementation and asks to retain learning material. Propose copying SERVER-032's attribution into personal.md/other relevant contexts and any future resume revision. Preserve the old 60% statement as friend/resume provenance, not a personal metric. No PDFs/contexts were changed in this task.
2. **Broad pipelines and Dockerized Sonar/Jenkins:** F/S broad wording conflicts with U's filler clarification and narrower code. Propose replacing unsupported personal ownership in future tailoring with SERVER-009/010/017/024/030 and verified review scope. Preserve historical wording/clarification for traceability. ELK/30% remains separately resume-supported; it was not disavowed by the specific pipeline/CI answer.
3. **11 Mongo fields versus 15+ resume wording:** CODE proves 11 exclusions; latest U explicitly says 15+ is a made-up number and asks to retain it. Preserve 15+ as INVENTED (USER-CONFIRMED), alongside the earlier same-SBOM-initiative confirmation. Proposed cross-context updates should carry the invented-number provenance rather than presenting 15+ as measured. No extra fields, dependency/CVE or SBOM steps are invented.
4. **Framework and chronology precision:** common APIs are inspected JAX-RS/Jersey Spring-managed code; microservices use Spring Boot. Some Agent Studio work is dated September–November 2025, beyond its resume role-bullet placement. Propose referencing actual implementation dates/frameworks without silently altering employer role dates. ADK/model-runtime and overall AI-platform ownership are not established by these server patches.
5. **Hackathon versus Phase II:** retain approved June 2026/5+ demonstrated-service wording exactly as requested. Add July branch prototype evidence and deployment limits alongside it rather than replacing project dates or attributing collaborator authorization work. Actual production components/provider list are unknown.
6. **Source availability / tooling placement:** personal.md's original uninspected-source baseline is now stale for this repository; propose linking this 2026-10-03 audit and coverage limits on its next authorized update. Sonar's Python reporting is server-repository evidence for frontend coverage tooling, not Java test speed/coverage. Commerce GraphQL/Neon/payments/hosting facts remain solely freelance-project scope; Lyra release tooling remains a separate context.

## Implementation chronology from Git author dates

U says deployment dates are unknown and asks to check commit dates. The dates below come from the personally attributable patch inventory and SHA-specific Git author metadata. They date implementation/revision activity, not rollout, release, merge or customer availability. Duplicate/cherry-pick and merge dates do not create additional implementation milestones. Deployment status remains UNKNOWN; no further deployment-date question is pending for this audit.

| Initiative | Personally attributable implementation dates | Source / boundary |
|---|---|---|
| SERVER-006 — BU membership/directory refactor | 2026-08-05–2026-08-14 | P inventory/SHA-specific author dates; shipment unverified |
| SERVER-017 — Email-template migration and release hooks | 2025-01-09–2025-09-12 | P inventory/SHA-specific author dates; shipment unverified |
| SERVER-018 — Email rendering/compatibility revisions | 2024-12-18–2025-09-12 | P inventory/SHA-specific author dates; shipment unverified |
| SERVER-023 — Response-header retrieval/index metadata | 2025-06-04–2025-06-30 | P inventory/SHA-specific author dates; shipment unverified |
| SERVER-024 — Bulk header synchronization and backfill initiative | 2025-06-19–2025-07-28 | P inventory/SHA-specific author dates; shipment unverified |
| SERVER-026 — DeepL glossary/no-translate | 2025-08-05–2025-08-22 | P inventory/SHA-specific author dates; shipment unverified |
| SERVER-029 — July Phase II discovery/index/session prototype | 2026-07-02–2026-07-12 | P inventory/SHA-specific author dates; shipment unverified |

The backfill CLI/migration-specific RES-151073/151077 patches are dated **2025-07-16–2025-07-28**; the wider SERVER-024 initiative includes June 19 bulk-update work and June 25 release instructions. The June 2026 hackathon resume date is preserved separately from July Phase II code. DeepL's former July–August narrative was too broad for these attributable patches and is corrected to August 5–22.

## Closed manual follow-ups — user clarifications (2026-10-03)

No user input remains required for this completed audit. The four follow-up questions were answered with the instructions below; retain the gaps/provenance and do not repeat these questions without new evidence or a user request to revisit them.

1. **User-list 15+:** U explicitly says the quantity is made up and asks to keep it. Literal wording remains in SERVER-007 with INVENTED (USER-CONFIRMED) provenance; the actual field-hiding contribution and 11 Mongo exclusions remain CODE. The earlier same-SBOM-initiative answer is preserved, without claiming generator/dependency/CVE work.
2. **Shipment dates:** U does not know them and asks to use commit dates. The implementation chronology above supplies Git author dates. Deployment dates/status remain UNKNOWN; commit dates are not substituted for proof of shipment.
3. **ELK/30% MTTR:** U asks to keep it unchanged and supplies no measurement data. Preserve F/S resume provenance and the original 30% wording; this preference is not verification of the period/sample/calculation. No measurement question remains pending.
4. **September–December 2022 history:** U asks to keep existing content unchanged and supplies no alternate identity/repository/export. Preserve internship dates/wording with F/S provenance, alongside the recorded lack of matched 2022 commits. No alternate authorship, repository or work is inferred. No coverage question remains pending.

## Maintenance completion note

2026-10-03: full updated text re-read and inventory/attribution/metric/ownership boundaries checked. Latest user annotations reconciled: invented 15+ provenance, commit-based implementation chronology, retained 30%/internship wording and closed manual follow-ups. All 255 nonmerge groups and 323 merge records are persisted, with duplicates/stash/collaborator work distinguished; 29 accessible PRs are registered. Evidence is prose, identifiers and paths rather than raw confidential code. Only server.md was persistently edited; no source edits, application submissions, messages, workflow implementations, commits, pushes or deployments. This is a complete audit of the available attributable inventory with the explicitly recorded hosting/ref/rollout/measurement gaps; it is not a claim that unavailable history is complete.


### SERVER-037 — Current approved BASE: retrieval, commerce and external connector

Status: USER-CONFIRMED / CURRENT RESUME, 2026-11-23.
Source: `main-resume/frontend-base.pdf` (workspace-relative), SHA256 `baf4ed23b5878de7c5ae208387d60828962b606c09aaa467d2ebb28235f9cc93`; complete exact-wording reading copy in `contexts/resume-baseline.md`. User explicitly confirmed the latest resume as correct and requested context synchronization. This record supersedes conflicting older resume counts/wording/attribution only within the statements below.

- Software Engineer, September 2024–September 2025: **30% search-relevance improvement**, replacing keyword retrieval with MongoDB Atlas Vector Search/OpenAI embeddings through Java/Spring Boot APIs. The result and contribution are user-confirmed; inspected response-header/filter data-flow records SERVER-023/024 supply narrower implementation detail, not a reason to erase the current claim.
- **Freelance E-Commerce Platform**, independent freelance project: maintained a released Next.js/Vercel app with products/cart/checkout/order dashboard; Google and Discord as **2 OAuth providers**, RBAC, GraphQL schemas/resolvers; license-key delivery after PayRam payment; Ubuntu-hosted PayRam, Neon PostgreSQL and Amazon S3 product data/images. This is project work, not employer backend ownership (supplementary record SERVER-034).
- **AI-Powered External Source Connector**, internal hackathon: Java/LLM prototype interpreted API documentation, identified endpoints/required parameters and executed authenticated requests using OAuth/API tokens; demonstrations across **5+ services**, including Chorus/Jira. The concept later evolved into a production Automated External Source Connector for AI Search/content ingestion/indexing. Preserve the prototype-versus-later-production distinction and do not infer sole production ownership (supplementary record SERVER-029).
- BASE skills also include Java, Spring Boot, REST, GraphQL, MongoDB, PostgreSQL, Redis, Solr, Node.js/Fastify, Google ADK/RAG and OpenAI/Atlas. A skills listing alone does not prove additional employer implementation scope, years or proficiency.

Evidence boundary: current user-confirmed resume facts, not a new source-code audit, freshly measured benchmark, test execution or live employer-parsing result. Consult existing anchored records for extra implementation detail; do not invent facts absent from either source. The selected PDF remains unchanged.
