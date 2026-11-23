## Current resume confirmation — 2026-11-23

For current printed facts, read `CORE-039` in this file and [resume-baseline.md](../resume-baseline.md). The user confirmed the full selected BASE as correct. Its facts/counts/role attribution override older conflicting resume wording. Earlier verification headers and investigation records below are historical within that overlap; they remain evidence for additional implementation detail. This update is user confirmation, not a new code audit or benchmark.

<!-- REVERIFY-20261003:START -->
## Current Canonical Verification — 2026-10-03

LATEST USER CONFIRMATION: the candidate re-verified SSE/60%, Redis caching/OTP guest sessions, Dockerized Sonar in Jenkins CI, Lyra deployment/Sonar management, membership/DAO/projection/JUnit/Mockito/SBOM work, and internship Spring Boot/REST/background processing as personal implementation. Current status: USER-CONFIRMED / PERSONAL IMPLEMENTATION; resume-safe YES. This supersedes earlier friend/filler/do-not-use classifications for those claims. Historical investigation text, source coverage, authorship searches and earlier statements below remain preserved; those earlier attribution conclusions are not the current canonical status.

The 60% polling-overhead metric is USER-CONFIRMED, not a fresh benchmark or newly located code attribution. No uninspected implementation internals are invented. Historical 15+ remains invented and is excluded from BASE/public wording; inspected projection count remains 11. Webpack attribution remains rfp-app; Lyra unit runtime remains separate. See corresponding latest notes inside the affected records.

<!-- REVERIFY-20261003:END -->

# Core Application Engineering Knowledge Base

Established and inspected: **2026-10-03**. This is a factual contribution register for resume tailoring, JD matching and application answers. It preserves implementation detail and ownership boundaries; it is not a resume.

Employer scope: enterprise SaaS work at **Responsive (formerly RFPIO)** from the September 2022 internship onward. Source modules establish response/project, content, administration and AI application work. Customer counts, traffic, concurrency, commercial adoption, team size and formal on-call/management responsibilities remain UNKNOWN; application/commit/training counts cannot substitute for those facts.

## Provenance, attribution and safe reuse

Source aliases:

- **F** — `/Users/SANJEEV.S/projects/misc/claude-job-skill/main-resume/SAM - Frontend Engineer - BASE.pdf`, both finalized pages read as a read-only factual reference.
- **S** — `/Users/SANJEEV.S/projects/misc/claude-job-skill/main-resume/SAM - Full Stack Software Engineer - BASE.pdf`, both finalized pages read as a read-only factual reference.
- **P** — `/Users/SANJEEV.S/projects/misc/claude-job-skill/contexts/personal.md`, canonical career/metric/evidence-maintenance contract, read in full.
- **C0** — the existing `core-app.md` before this investigation; preserves previously approved resume/context facts even when originating code is missing.
- **U** — user instructions and explicit identity confirmation (“all me” for the listed identities); user also confirmed Bitbucket is now closed.
- **U2** — user annotation follow-up on 2026-10-03: confirmed personal implementation of Document Library faceted-search UI (“yes”); confirmed rollout of the build changes associated with PR-9515 and companion S3 pipeline (“yes rolled out”); confirmed the 174→76-second metric and Storybook/Chromatic/interaction work belong to design-system, not this repository. Other requested clarifications were explicitly left as-is for the user to handle. This updates only the answered fields; it does not supply missing SHAs, measurement conditions, release dates or implementation details.
- **G-20261003** — read-only local Git/source inspection of `/Users/SANJEEV.S/projects/rfp-app`, branch `lyra-ux`, HEAD `93e20e29670c887d47231a47255884330dd2fe33`. Remote `https://github.com/responsive-core/rfp-app.git`; inspection date 2026-10-03. Unless a record names another SHA/ref, this is its repository/ref/inspection metadata.
- **PR-N** — authenticated read-only GitHub inspection at `https://github.com/responsive-core/rfp-app/pull/N`; titles, description summaries, states, commits, reviews and file-diff boundaries are retained in the PR register below. Historical Bitbucket numbers are a separate namespace.

Evidence labels follow P: `PRODUCTION`, `PROJECT`, `PROTOTYPE/POC`, `HACKATHON`, `TOOLING`, `SKILLS-ONLY`, `USER-CONFIRMED`, `UNKNOWN`, `CONFLICT`. Here **PRODUCTION describes employer application work supported by F/S or application code; it does not independently prove production deployment**. Deployment is **UNKNOWN** unless a record explicitly cites user confirmation or a PR author's environment report. **CORE-005 rollout is USER-CONFIRMED (U2)**; its exact release/environment and independent deployment evidence remain unspecified. A merge proves integration into its named base at that time, not a release, adoption, traffic or deployment.

Authorship confidence is **high for the exact authored diff**, **medium for broader resume-only ownership/impact**, and **unknown for missing implementation details**. A current file, PR author, merge author or committer is never sufficient to attribute all surrounding architecture to me. Interpretations are labeled; endpoint names establish frontend integration, not server implementation.

Confirmed historical identities: `sanjeev.s@rfpio.com` (Sanjeev / S-Sanjeev); `sanjeev.s@responsive.io` (Sanjeev / S-Sanjeev / SANJEEV S); `sanjeev.s+rio@responsive.io` (SANJEEV S); `sanjeev.shoyo@gmail.com` (Sam). U confirmed all belong to me, including the historical S-Sanjeev alias/login. Authenticated work GitHub account: **`sanjeev-s_rio` / SANJEEV S**. The public resume profile **`sam-zc`** remains distinct. Current Git configuration was not used to establish historical identity.

Canonical role dates remain: Engineering Intern **September 2022–July 2023**; Associate Software Engineer **July 2023–August 2024**; Software Engineer **September 2024–September 2025**; UI Architecture & Design Systems **October 2025–present**. Commit dates describe observed implementation phases, not HR dates. Some initiatives span these boundaries.

## Canonical facts and metrics

| Fact/metric | Provenance and reuse boundary | Related IDs |
|---|---|---|
| Shared layouts/navigation across **5+ applications**, with product/design/backend collaboration; responsive UI patterns in F | F/S p1; leadership is approved resume evidence. Exact app membership and sole ownership are not established by code counts. | CORE-001 |
| **Two React micro-frontends** with Webpack Module Federation for viewer reuse across **Trust Center and Builder** | Personal scope from the user's November 13, 2026 Frontend BASE update. Earlier F/S resumes listed three. Exact package mapping is unknown. | CORE-002 |
| Internship **Response Template and Billings** Angular→React/TypeScript migrations | F/S p2; two distinct modules in internship. Later Billing 2.0 code is a separate phase. | CORE-003, CORE-020 |
| **Four additional later migrations**, **45% page-load improvement**, cross-browser compatibility | F/S p2; Associate period. Redux and Easy Peasy use for state management is user-confirmed November 13, 2026. Four module names, timings and measurement method remain unknown. | CORE-004 |
| Full-monorepo cold build **10–14+ minutes →101.45 seconds (~88%)** | F/S p1/P; repository verified as rfp-app for the inspected build initiative. U2 confirms rollout of the build changes and companion S3 pipeline. PR-9515 also uses 15+ minutes and separately 720.0 seconds/85.9%; the baseline conflict remains unresolved. | CORE-005 |
| Unit tests **174→76 seconds (56%)** | F/S p1/P; U2 explicitly confirms this is design-system work, not rfp-app. Do not apply the metric to the app_v2 Vitest rollout. | CORE-006 |
| SSE notifications **60% less client polling overhead** | F/S p1/C0. Retained despite missing attributable stream implementation. Not API latency, infrastructure cost or server-load reduction. | CORE-008 |
| Production troubleshooting **30% MTTR reduction** using ELK/root-cause analysis | F/S p2/C0; incident/log/measurement evidence not available in this checkout. Use MTTR wording. | CORE-010 |
| Enablement/training for **50+ engineers** | F/S/P, docs/live demos; group enablement, not “mentored 50 engineers” or people management. | CORE-006, CORE-029 |
| Hackathon **5+ services**, including Chorus and Jira; later production evolution | F/S/P; demo/service count is approved. July branch contains mock-enabled flows; service-by-service production status and dates remain unknown. | CORE-027 |

The 70+ Lyra components, >90% published Lyra package-size reduction and 11 ShadCN prototypes belong to their design-system/prototype contexts. Application import changes here do not prove I implemented those components or prototypes. Java MongoDB/Solr synchronization, Atlas/OpenAI RAG and ADK backend execution belong to server/agent evidence; this file records the attributable frontend side.

## Technology and architecture boundaries

| Technology | Verified use and ownership boundary |
|---|---|
| React / TypeScript / Angular | Authored React/TS modules, typed models, forms, stores, shared components and legacy Angular fixes are evidenced across 2022–2026. Six approved migrations retain distinct periods and unresolved originating commits. |
| Redux / Easy Peasy | **Implementation verified**, superseding C0's skills-only uncertainty. I authored Easy Peasy action/thunk/context-store models in account/security, business units, org search, custom fields, My Work and Agent Studio, and changed Redux Toolkit-driven Ask UI flows. Existing global store infrastructure predates many changes. |
| Zustand / StyleX | **USER-CONFIRMED personal adoption on 2026-10-03**, routed to design-system supplement LYRA-042. The inspected core-application source/history still does not establish adoption in this specific app; AgentStore here uses Easy Peasy, not Zustand. Do not infer component-level use or rollout breadth. |
| Bun / Oxlint / Oxfmt | **USER-CONFIRMED personal adoption on 2026-10-03** in frontend modernization work (LYRA-042). Oxlint/Oxfmt's Lyra migration is separately code-verified (LYRA-034). No attributable configuration/source adoption for these tools was found in this inspected core app; the local `oxc` branch with other authors is not evidence of this work. |
| Webpack / Module Federation / Turbo / pnpm | Authored build/cache/concurrency and federation compatibility work verified. The initial pnpm/Turbo monorepo conversion in PR-6421 is Gowrishankar's work; I optimized and maintained it. |
| Vitest / Testing Library / MSW / Playwright | Authored test foundation, HTTP-boundary fixtures, reference module tests, smoke support and scoped quality tooling verified in CORE-006. Historical Jest tests are separate evidence. |
| Vite | Verified **test-runner integration**: shared Vitest factory imports `@vitejs/plugin-react`, Vite aliases/types and dependency optimization. Main app production compilation remains Webpack. This is not proof of a Vite application migration. |
| Storybook / Chromatic | F/S/P support design-system testing; U2 confirms the Storybook/Chromatic/interaction work belongs to design-system, not this repository. No attributable core-app setup was located; maintain that scope. |
| Next.js / Rspack / Rsbuild | Existing satellite builds/configuration are inspected dependencies of build work; changing their build settings does not establish full application implementation. Freelance Next.js implementation remains separate. |
| REST / Axios / i18next / MUI / AG Grid / TinyMCE | Actual integration, rendering, forms and fixes evidenced below. Use version-specific claims only where a record supplies provenance. |

## Contribution records

Each record inherits **G-20261003** repository/ref/date metadata. Commit identifiers in the detailed records resolve to full SHAs; the exhaustive authored-patch index below preserves additional fixes and duplicate transports. “Current module” means it exists at the inspected snapshot, not that every historical line or design survives. Historical test files may have been removed by the 2026 Jest cleanup. No builds/tests were rerun during this read-only audit.

### CORE-001 — Shared application shell, layouts, headers and navigation

**Evidence:** PRODUCTION (F/S p1 + Git); high attribution for authored changes, medium for 5+ scope/leadership. **Status:** historical 2023–2024 framework phases with current descendants; deployment UNKNOWN.

**Attribution confidence:** HIGH for authored shell changes; MEDIUM for F/S leadership and 5+ scope. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

**Context/action:** Page-specific headers and launcher/sidebar implementations were being modernized across the React application. I implemented common shell pieces, moved multiple page headers into shared layout/portal contracts and adjusted responsive navigation. This is collaborative framework work, not ownership of every application.

**Execution:** `HeaderLayout` derives module/home-page appearance from route data, wraps the AppBar/toolbar and selects `HeaderAdornmentRenderer` content. The common header portal allows page-specific controls to render inside the shell; header loading is gated on user-details readiness. Page wrappers for My Account, My Work, Response Templates, intake, projects, e-sign, content analysis and reports were adapted. Launcher items use feature/permission checks and responsive presentation. Side-navigation changes centralize selected page/title state; expanded hamburger sections persist through localStorage with fallback handling. This replaces repeated header assembly with shared rendering plus page-specific adornments. Existing routing, permission services, store hooks and some framework components were reused.

**Evidence anchors/paths:** `231eabe4ef59b9ed6f678c37eca835ec5f367aa9`, `9f65d0438d2dd03413deaeef949e0faf3398387b`, `9285e64bfd4928cfcef8922c2b3d85289efa091a`, `e8989496dc3a0603d4be08e694ef354b32055d65`, `6b7278732f2550fa06e81fdd352a6237c2e078ff`, `5c74e66de39d5af736392759ce6c8b546314a338`; `app_v2/src/components/header-wrapper/`, `layouts/LoggedInHeaderLayout.tsx`, `rfp-components/RfpHamBurgerMenu.tsx`, `store/header-store/`. Historical `HeaderLayout` tests added in `72899b1e8737f106c153f3bc7b666906e076234c`; launcher/header/avatar tests and browser fixes are in the change index. Original Bitbucket PR descriptions/reviews are unavailable; commit-message references survive. No measured layout-performance outcome beyond F/S application scope.

**Reuse:** “I implemented shared React header/layout/navigation contracts and adapted multiple product modules, coordinating with product, design and backend teams.” **JD keywords:** frontend architecture, React, TypeScript, responsive design, component reuse, navigation, permissions. **Avoid:** sole architecture owner, built all 5+ applications, people management, or inventing a routing-hook origin/rollout date.

### CORE-002 — Micro-frontends, viewer reuse and federation compatibility

**Evidence:** PRODUCTION (F/S p1) + Git/PR-8784 for compatibility; medium attribution for the original three-MFE claim, high for inspected fixes. **Status:** original viewer-reuse period September 2024–September 2025; 2026 compatibility fixes merged; deployment UNKNOWN.

**Attribution confidence:** HIGH for verified compatibility fixes; MEDIUM for the original three-MFE/viewer claim. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

The user's November 13, 2026 Frontend BASE update records two React micro-frontends built with Webpack Module Federation to enable viewer reuse across Trust Center and Builder. Use two for personal resume scope. Earlier F/S resumes listed three. The exact package names, original authored interfaces and deployment boundaries remain **UNKNOWN — requires user confirmation**.

Current configuration provides context: app_v2 consumes remotes such as profileBuilder, pursuitIntelligence and commons; Builder/guest configuration separates viewer exposure from a full designer runtime. However, founding configs inspected in `a00c2c600a0bf2d8e365b155b0b1cd1285855e2e` (commons, Boopathi), `8d253c759ac14b75aa1d13fdade794e27c5ae162` (Builder, Madhanbabu) and `3578e7b50c2d1a5649097dbf852c3e62e187f2ce` (guest architecture, Kumaresh) are **other authors' implementation**. They neither disprove F/S nor prove I authored those foundations.

My verified federation repair `e32c0cdf70bfb609b258788ae66fd1069ed85cf1` / PR-8784 drops `eager` consumption for i18next/react-i18next while retaining singleton sharing. The PR explains a host Webpack 5.76 / remote 5.108 and react-i18next 11.18.6 / 15.7.4 mismatch: a remote expected an eagerly loaded shared entry, producing an undefined `loaded` failure and hosted spinner after the Lyra upgrade. Async bootstrap/non-eager consumption permits the share scope to initialize. The remote entry must be rebuilt as well as the host. PR-author checks cover Lite build, hosted Guided project-list load, standalone and federated translation; dev-environment verification is reported, not independently replayed. Related build-plugin compatibility is CORE-005; scoped remote theming is CORE-029.

**Paths:** `app_v2/webpack.config.js`, `responsive-lite/webpack.config.js`, `app_profile_builder/webpack.config.js`, `app_profile_guest/webpack.config.js`. **Reuse:** “I worked on Module Federation viewer reuse and later diagnosed and fixed host/remote shared-dependency initialization.” **Keywords:** micro-frontends, Module Federation, singleton dependencies, async bootstrap, integration debugging. **Avoid:** deriving three from today's remotes, claiming the other authors' founding configs, or claiming independent deployment ownership.

### CORE-003 — Internship migrations: Response Template and Billings

**Evidence:** PRODUCTION, F/S p2/C0; medium attribution, implementation details UNKNOWN. **Status:** historical internship, September 2022–July 2023; deployment UNKNOWN.

**Attribution confidence:** MEDIUM for F/S facts; UNKNOWN for missing originating implementation. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

Approved fact: I migrated **Response Template and Billings** from Angular to React/TypeScript using reusable components. Their originating migration commits/PRs were not identified in the available attributed history. The first attributable local commit is November 2022; that gap does not disprove earlier internship implementation.

Response Template follow-up evidence includes header/layout adjustments and `TemplateMenuRenderer` error/filter fixes, e.g. `60844f69b824816f3879a3ecd446951a35eb96a8`; template duplication/processing work appears in CORE-037. These demonstrate related maintenance, not the complete original migration. The substantial October 2024 Billing 2.0 implementation in CORE-020 must not be substituted for the internship migration. Exact Angular controllers, new React entry points, data/store flows, tests, rollout and relative collaborator ownership remain unknown.

**Reuse:** “During my internship I migrated Response Template and Billings to React/TypeScript.” **Keywords:** Angular modernization, React, TypeScript, reusable components. **Avoid:** attaching 45% performance to these two modules, inventing coverage/module size, or re-dating the internship using later billing code.

### CORE-004 — Four later Angular-to-React migrations

**Evidence:** PRODUCTION, F/S p2/P/C0; medium attribution; measured implementation mapping UNKNOWN. **Status:** Associate period July 2023–August 2024; deployment UNKNOWN.

**Attribution confidence:** MEDIUM for F/S facts; UNKNOWN for module/measurement mapping. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

Approved fact: I modernized **four additional modules** using React/TypeScript, improving page-load speed **45%** while maintaining cross-browser compatibility. The full history contains substantial My Account, business-unit, organization/security, user-management and framework work, but code alone does not identify which four count as the approved migrations. Do not select four plausible folders and call that verified.

**USER-CONFIRMED — November 13, 2026:** I used Redux and Easy Peasy for state management in the four AngularJS-to-React/TypeScript migrations. The per-module allocation of the two libraries remains unknown.

Concrete implementations are recorded separately in CORE-007/011/012/013/021 and browser fixes in CORE-033. **UNKNOWN — requires user confirmation:** four module names, their Angular/React entry points, original migration SHAs, measured pages, baseline/final timings, browser matrix and measurement method. Six total remains two internship plus four additional later modules.

**Reuse:** approved four-module/45% wording may be used with F/S provenance; detailed examples must reference verified initiative records without asserting they are the four. **Keywords:** modernization, frontend performance, cross-browser compatibility. **Avoid:** treating 45% as a repository-wide average, inventing measured Core Web Vitals, or collapsing periods.

### CORE-005 — Monorepo cold-build optimization, bounded concurrency and compiler caches

**Evidence:** TOOLING + USER-CONFIRMED rollout (U2), F/S p1 + authored code + PRs; high attribution for changes; PR benchmarks author-reported. **Status:** September 2026 development changes merged; staging PR-9515 was OPEN in the inspected GitHub snapshot. U2 confirms the build changes and companion S3 pipeline were rolled out. **Deployment/rollout: USER-CONFIRMED**; environment, release date and independently verified deployment checks UNKNOWN. PR merge status was not reinspected in this follow-up.

**Attribution confidence:** HIGH for authored code; rollout user-confirmed in U2; benchmark outcomes author-reported/F/S, not independently rerun. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

**Problem/action:** Serial builds and overly aggressive parallel compilation consumed excessive memory; the PR records an exit-137 baseline. I tuned build orchestration, compiler/minifier parallelism, output splitting and persistent caches on the existing pnpm/Turbo monorepo. The original monorepo conversion is Gowrishankar's PR-6421, not my implementation.

**Flow:** Root build uses two waves: smaller satellite tasks with Turbo concurrency four, then the large Lite/rfpio builds with concurrency one. Shared `packages/build-utils/index.cjs` supplies memory-aware/compiler/minifier helpers. Webpack filesystem caches have a seven-day retention and live in each app's `.webpack-cache` (or explicit `WEBPACK_CACHE_DIR`), avoiding the node_modules/mount cross-device problem. Cache invalidation includes build configuration dependencies. App_v2 Babel work is scoped to src through thread-loader; worker count is capped at four/CPU−1, watch pools stay alive, non-watch timeout is bounded and static warmup is avoided because it interfered with filesystem cache replay. Minimizer caps evolved during the initiative; current CI cap is four. Next satellite CI CPU settings are limited separately. Lite's ProvidePlugin dependency was removed with explicit React imports/automatic JSX so cache serialization and federation work correctly. Turbo inputs exclude tests/fixtures/docs from production builds. Vendor splitting and optional source maps reduce output size. Sonar source-path follow-ups avoid double-indexing root/module sources.

**Anchors:** `161d9ba8068dbd2a40844742fd090a2ebd2217d4`, `ae0cca354c398462007140b44fbc06b9ab277eef`, `5374d37d7b39b0c535b7de86b1eed4aa7cba3d2e`, `c9ba40b9729c9ad398b79c1c9ddc47ccea70396b`, `dfeb53373a3685bb348d9fa0c40dfbc415489478`, `7c7df975d2a9e534ce1a17ebf8e779bcc96c528e`, `0bced9664b427bc9a5c1c995cf2a55dcc5ba3269`, `8a544fda9fd803364873e882a4eaa072fd2d4e36`. **Paths:** root `package.json`/`turbo.json`, `packages/build-utils/`, `app_v2/webpack.{config,prod}.js`, Lite/satellite configs and build-performance docs. **PRs:** 8968, 8988, 9012, 9055, 9114, 9128, 9179 merged into development; 8966/9178 closed unmerged alternatives; 9515 staging open in the original inspection snapshot. U2 subsequently confirms rollout; this is not a new GitHub merge-status observation. Titles and description summaries retain their inspected provenance in the PR register.

**Validation/outcomes:** Canonical F/S metric remains **10–14+ minutes →101.45 seconds (~88%)**. PR-9515 checked build, warm-cache, watch, coverage and Sonar test-plan items; no commands were rerun here. Its summary says 15+ minutes/~88%/8.5×, while detailed baseline is 720.0 seconds/85.9%/7.1×. The PR's S3 tar-cache/pipeline narrative and additional metrics are author-reported; a post-deploy job check was unchecked in that inspected description. U2 confirms the build changes and companion S3 pipeline were rolled out. This resolves the rollout question by user evidence; exact deployment timing/environment and Job1/Job2/Sonar results are not independently established by this checkout. See benchmark register below before using additional numbers.

**Reuse:** “I optimized a frontend monorepo's cold builds with bounded concurrency, Webpack disk caching and compiler/minifier tuning, reducing the approved baseline to 101.45 seconds.” **Keywords:** build performance, monorepo, Webpack, Turborepo, caching, memory profiling, developer experience. **Avoid:** presenting rollout as independently verified, inferring PR-9515 merged from the rollout confirmation, sole monorepo creation, zero future OOMs, or silently reconciling conflicting baseline percentages. Rollout may be stated with U2 user-confirmed provenance.

### CORE-006 — Vitest/MSW foundation, scoped coverage and Playwright smoke contracts

**Evidence:** TOOLING, authored Git + PR-8279/8281; high attribution for my infra/reference tests; collaborative Sonar scope. **Status:** August–September 2026 merged foundation at current snapshot; deployment UNKNOWN / developer tooling integration verified.

**Attribution confidence:** HIGH for authored infrastructure/reference tests; collaborative Sonar ownership explicitly bounded. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

I introduced a shared `@rfp/vitest` package and app-local testing foundation for the Webpack application, replacing the Jest setup in a distinct deletion phase and building My Work/Plans & Billings reference suites. The shared factory translates Webpack-aware aliases/assets into Vitest configuration, separates node pure-logic and jsdom component projects, integrates React/Vite transforms, normalizes CJS/ESM dependencies and prebundles expensive test dependencies. DOM setup supplies browser/observer shims; MSW helpers and fetch/SSE test infrastructure support HTTP-facing tests. These are test utilities, not production notification implementation.

**Flow:** Captured JSON fixtures feed MSW HTTP handlers, a registry and module route maps; common bootstrap covers login/user-load/translate data. Tests render real components using React Testing Library rather than mocking Axios/service functions. `test:resolve-targets` derives scoped production targets from folder/file or local/PR diffs (local includes unstaged, staged and untracked files). `run-scoped.mts` evaluates lines, branches, functions and statements at **≥85% per in-scope production set**, with documented exclusions. Quality docs also require state-matrix/pure-logic scenarios; the percentage alone is insufficient. PR validation posts a persistent gatecheck comment. Playwright support intercepts routes with the same fixture JSON and adds My Work/Billings ready+interactive smoke flows; assertions use actual translated fixture copy inside data-qa and a before/after UI delta. Loading/error/bootstrap-empty scenarios stay in Vitest; the documented smoke floor is ~5%, minimum two flows per migrated routable feature.

**Anchors/paths:** `c30af003fb1ec7742bc1eef8c4bfadae9c14b906`, `8718aff634aca1f65d99631c1c79e2390a1e8f7f`, `9693de9785e4ac5c52550fdf52a9da561338705c`, `510f5d7f14089e79728f5927527a2580c20a7b7e`, `e84f8b3e2a54bf5e437fbd7b47b26227a3a98bd3`, `1295fc3823a4087c4e320a5915df529cd866bc96`; `packages/vitest/`, `app_v2/src/test/`, `app_v2/src/containers/{my-work,plans-billings}/tests/`, `app_v2/e2e/`, `scripts/pr-validation/`, testing docs. `.cursor/skills/vitest/ATTRIBUTION.md` explicitly credits adapted open-source layouts/testing patterns; my repository integration/contract adaptation is distinct from inventing those upstream ideas.

**Ownership/testing boundary:** PR-8279/8281 include Akarshan's local Docker/Sonar setup from PR-8282 (`7aa3c23ff9269bd434199b6e165813c30b0ca08a` and follow-ups). I integrated it and fixed coverage paths/root source composition; I did not author the entire Sonar environment. Historical PR checks report full Vitest, infra smoke, scoped My Work/Billings coverage and Playwright validation. Those are author-reported, not rerun audit results. `cf0c8866ebdbd357c54e7524379bfd91016c60d6` removes a broad legacy Jest suite; removal does not prove complete conversion or retention of every old test. **174→76 seconds/56%, Storybook accessibility, interaction tests and Chromatic belong to design-system, not rfp-app, explicitly confirmed by U2**. Application Vitest/MSW/RTL/Playwright implementation above retains its separate Git evidence and no borrowed runtime metric.

**Earlier saved iterations:** the deleted/unreachable object audit recovered `9027e02ab24081112a0527c7b8c1e38570d58429`, an August 19 untracked-tree snapshot containing a node/jsdom smoke split, RTL data-qa setup, MemoryRouter render helper, asset stub, Lyra AI mock and an initially empty MSW server factory. This documents the scaffold before captured HTTP fixtures and shared-package extraction; a stash capture does not by itself prove original authorship or adoption. `c49af5468fee3f5c227e7a20e565648420f72c0e` saves a later jsdom-noise experiment: a window.open stub and a virtualConsole handler filtering “not implemented” errors while forwarding others. `3bcd4a7ca2d6c3c246b82024d04c190f6df37f36` saves coverage.reportOnFailure=true. These drafts add no independently verified tests-passing result or new delivered-feature count; current policy and reference suites above supersede the initial empty-handler scaffold.

**Reuse:** “I established a reusable frontend test foundation with HTTP-boundary MSW fixtures, component/logic tests, scoped coverage enforcement and fixture-backed E2E smoke flows.” **Keywords:** Vitest, React Testing Library, MSW, Playwright, coverage, test architecture, CI validation, developer tooling. **Avoid:** 85% whole-repository coverage, all modules migrated, deleting tests as quality improvement, independently verified historical runs, or applying the Lyra runtime metric to app_v2.

### CORE-007 — Sign-in, password reset, guest access and authentication integration

<!-- REVERIFY-20261003:START -->
**LATEST USER CONFIRMATION — 2026-10-03:** Redis caching and OTP verification for secure guest access/session management are now USER-CONFIRMED / PERSONAL IMPLEMENTATION; resume-safe YES via SERVER-032. Existing sign-in/password-reset frontend mechanics remain code-backed. Earlier guest-session attribution exclusions are superseded. This supersedes earlier contradictory attribution for current resume/application use; retained historical text follows.
<!-- REVERIFY-20261003:END -->

**Evidence:** PRODUCTION, F/S p2 plus exact follow-up diffs; high for specific fixes, medium for complete rebuilt-flow claim. **Status:** historical 2023–2024 workflows with later descendants; deployment UNKNOWN.

**Attribution confidence:** HIGH for verified fixes; MEDIUM for complete-flow/Redis resume claims. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

F/S establish responsive sign-in/password-reset UI with validation, REST/error states and Redis/OTP guest/session work. I authored legacy Google sign-in/provider-visibility/Lite OAuth restrictions, company-activation and My Account password integrations. Examples `6e5c516d34ef0fe5dcc545f9e33b61e47dadab4c`, `a6d74c4849e11beda0fc9d7f4c3863df24c6ed3d`, `803b1f2e46ca3c5802a624bcc0c1ebd9ef8cd845` affect Angular login/controller/bootstrap paths; these must not be described as the entire original React login creation. Inspected founding React Login commits `995ee5e66236d3efd95311c4e2e2349cc72fefea` / `09957fea8519c2108e77a87ff87f9b9c88a7d8cb` are Kumaresh's work; an older skeleton predates my tenure.

My Account service wiring (CORE-011) lowercases the reset username, posts `login/forgot-password`, handles response/error logging and closes its dialog; change-password uses urlencoded old/new-password data and success callbacks. Guest preview/route/pod handling appears in historical fixes; e.g. `a6ae3a470e2df81c4a122861351bef817b8b8679` has a subsequent revert and must retain that status. One guest pod fix `b2eeaab44506bffd3956b03878cc0e4cbd892200` is Dinesh-authored/committed by me, not my authored implementation.

**Paths:** `app/app/js/controller/pages/{loginCtrl,googleCtrl}.js`, `app_v2/src/containers/login/`, My Account service/settings, guest components. **UNKNOWN:** original rebuilt-flow SHAs, Redis keys/TTL, OTP resend/expiry/rate limits, token storage and session lifecycle; backend implementation belongs to server evidence. No inspected test proves the complete auth flow/security posture.

**Reuse:** “I implemented authentication UI integrations and corrected provider/activation/guest-flow behavior; approved resume evidence also records sign-in/reset modernization and Redis/OTP guest access.” **Keywords:** authentication UI, REST, validation, sessions, guest access, error handling. **Avoid:** sole React-login authorship, password hashing/provider architecture, secure-by-audit claims or inventing Redis internals.

### CORE-008 — SSE notification delivery and polling reduction

<!-- REVERIFY-20261003:START -->
**LATEST USER CONFIRMATION — 2026-10-03:** SSE implementation and 60% client polling-overhead reduction are now USER-CONFIRMED / PERSONAL IMPLEMENTATION; resume-safe YES via SERVER-032. Preserve UI/test-helper code evidence separately; no new transport internals or independently measured benchmark are inferred. This supersedes earlier contradictory attribution for current resume/application use; retained historical text follows.
<!-- REVERIFY-20261003:END -->

**Evidence:** PRODUCTION, F/S p1/C0; medium attribution for approved claim, implementation UNKNOWN. **Status:** historical Software Engineer period; deployment UNKNOWN.

**Attribution confidence:** MEDIUM for F/S fact; UNKNOWN for stream/measurement details. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

Retain: delivered real-time notifications with **Server-Sent Events**, reducing client polling overhead **60%**. Exact user-authored stream code was not located in the all-ref attributed history search for EventSource/text-event-stream/fetch-event-source/server-sent-event symbols. The matching owned commits were dependency-lock changes, not notification implementations.

Current `app_v2/src/services/agenticChatSse.ts` uses fetch/readConnection, auth headers, event IDs and abort/response handling, but its inspected history/blame originates with Thiyagarajan and Hari (`e912241fe9d6ee7ee34dc287af08acd4cd77d80d`, `59e9b05943a6f20ee6172307a7c2c307d657d8e7`). Do not borrow its reconnection/data flow as mine. Pending-mail queue UI changes in CORE-037 are also not proof of SSE transport. Test SSE helpers in CORE-006 do not establish production notification ownership.

**UNKNOWN — requires user confirmation:** repo/branch/SHAs, stream endpoint and event types, state/store updates, reconnect/backoff/Last-Event-ID/heartbeat/error/cleanup behavior, tests, rollout and measurement basis for 60%. **Reuse:** approved SSE/60% sentence with F/S provenance. **Keywords:** SSE, real-time notifications, event-driven UI. **Avoid:** cost/latency/server-load percentages or inferred reconnect behavior.

### CORE-009 — TinyMCE composition, comments, plugins and rich-text correctness

**Evidence:** PRODUCTION (F p2 + authored diffs); high attribution for custom changes. **Status:** historical 2022–2025 implementation/fixes; current editor descendants, some explicit reverts; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

I customized the React editor integration and vendored plugins for enterprise document composition and annotations/inline-comment behavior. Earliest attributable change `6a72d6bb339dce72291d388cbdfc75c6bff0cf10` concerns selected-style visibility in November 2022; 2023 work includes editor upgrade/customization and guest/annotation rendering, e.g. `28f1c03446b019e23227a45e1a5293170093a6aa`, `c87752c3ef793a606a39e909c609e2f9a5f208d4`. Upstream TinyMCE distributions, minified bundles, skins and icons are generated/vendor artifacts; changing or importing them does not mean I wrote the editor engine.

**Implementation areas:** React wrapper `vendors/tinymce/components/Editor.tsx` and `TinyMCEUtils.ts` coordinate HTML, comment/annotation presentation and guest editor behavior. Custom paste/format-painter/style handling deals with plain-text/Word clipboard formatting, company content defaults, line height, fonts and preservation of inline styles. Promise/error handling around paste/image processing was corrected in `14a4b3f65c8bdaaabea17e57e89fb7b1ca90c1df` / `d84109327fcdc6f1bc3792328247037fe7147606`; image/blob paths have additional fixes. The table plugin preserves inherited styling when inserting new rows (`2de4afd8dd3431d0f18f83746d46d2f267e45a4b`). Image editing switched through `bdesk_photo`/image plugin changes (`59c2f40b35325fbb463cc215e7c21c7f1d8665b9`). Word/character-count limits were integrated with response/import/edit-answer UI (`3afbe30015e557ba718c526bb1c06cb247a994e7`, `d523e91e86e509520c35b04359b6457d6a0150a4`); they are application validation, not a server storage-limit claim. Merge-tag popovers, dialog focus, menu overflow, grammar icons and customer styles have distinct follow-up fixes recorded in the index.

**Paths/tests:** `app/vendor/tinymce-editor-react/plugins/`, `app_v2/src/vendors/tinymce/`, `utils/TinyMCEUtils.ts`, project answer/editor/import components and `library_fixes.txt` custom patch notes. Several theme/menu fixes were explicitly reverted (`3872c112b13fb650e172e2158a268d5a090e3d18`, `18a5baf240618aedc5edd6d9ac6e753055c567b2`); do not claim they remain current. Historical test-related changes exist, but comprehensive editor end-to-end coverage/performance was not established. Comment persistence/backend collaboration schema, real-time multi-user editing and usage scale remain unknown.

**Reuse:** “I customized TinyMCE's React integration and rich-text plugins, fixing clipboard/styles, annotations, images, tables and response validation.” **Keywords:** rich-text editor, TinyMCE, document workflows, DOM/HTML, async handling, browser compatibility. **Avoid:** editor-engine authorship, Google-Docs-style real-time collaboration, or treating bundled upstream code as original implementation.

### CORE-010 — Production troubleshooting and ELK root-cause investigation

**Evidence:** PRODUCTION, F/S p2/C0; medium attribution, incident details UNKNOWN. **Status:** Associate period production-support experience; deployment/incident rollout UNKNOWN.

**Attribution confidence:** MEDIUM for F/S fact; UNKNOWN for incident/measurement details. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

Approved fact: resolved production issues through ELK log analysis and root-cause investigation, reducing **MTTR 30%**. Repository fixes/errorLogger updates demonstrate troubleshooting activity, but do not expose incident timelines, Kibana queries, dashboards, customer impact or the measurement population. Diagnostic-only logs and speculative/rolled-back fixes are not all permanent product improvements.

Related concrete examples: accent-color bootstrap fallback (CORE-033), OAuth/company activation (CORE-007), TinyMCE async failures (CORE-009), company-user migration regressions (CORE-028), federation hosted spinner (CORE-002) and compiler/cache/Sonar failures (CORE-005). They illustrate code-level diagnosis; none is automatically the incident behind the canonical MTTR metric.

**UNKNOWN:** incident IDs/categories, before/after resolution times, measurement window/count, exact ELK evidence and my role in triage versus implementation/release. **Reuse:** approved ELK/root-cause/30% MTTR sentence, with concrete repository examples separately qualified. **Keywords:** production support, troubleshooting, observability, root-cause analysis, ELK. **Avoid:** uptime/SLO guarantees, formal SRE/on-call ownership, staffing claims or attributing the metric to a chosen bug without evidence.

### CORE-011 — My Account security and organization security administration

<!-- REVERIFY-20261003:START -->
**LATEST USER CONFIRMATION — 2026-10-03:** Latest confirmation establishes candidate-owned Redis/OTP guest-session work via SERVER-032, alongside this code-backed account/security UI. This does not extend the UI record into blanket cryptography/auth-engine ownership. This supersedes earlier contradictory attribution for current resume/application use; retained historical text follows.
<!-- REVERIFY-20261003:END -->

**Evidence:** PRODUCTION-context + authored Git; high for UI/service/store changes. **Status:** 2023 forms, 2024 performance refactor and later maintenance; current module descendants; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

I authored My Account password/2FA/API-account UI and organization login-method, password-policy, domain/IP, timeout, BYOK and SSO configuration work. `504a059eb8b2c0aa2d7f80284bd2b883a8b20599`, `a69fe8c8c8bec8303df051e64443daf4782fb2a1`, `d7c236689ab0f31d11241645b6eaacb1316a32e2`, `94e47e8cacf603730d628b86b44c3b5032ed4de6` create/extend typed Easy Peasy state with temporary password, keyed verification codes, validity flags and user-account map. `MyAccountService.ts` integrates user preferences, account removal, reset/change password, `generate-2fa` and `validate-code-2fa`, returning data/callbacks and reporting errors. Forms validate required/confirmation inputs and six-character code readiness, with password visibility controls and success/snackbar/dialog transitions.

Organization forms (`16697a6d821ddbabf762eb3023e94e03918ac97b`, `a0cf6a792c02e5582b38d19e95fe6329557606da`, `271dc68e3c596790e7b93c5f3466488a527a5278`, `5b5dfafbf8ea42548e231fe3d847346d76a8882b`) hold initial/temp company preferences and save/cancel dirty state. Domain/IP chips and allowed sign-in/password-policy toggles map to configuration payloads; session UI edits idle/reminder settings. BYOK `63eec99cb7e1640db7fa6a3ee3c1278e1043187c` loads KMS key identity, validates it through `users/admin/validate-kms-key` and updates via `users/admin/update-kms-key`; early placeholder scaffolding is superseded by that wiring. SSO `5c848058cc18c94d9d81d9116d419a39fb76e93f` handles certificate FileReader input, metadata/provider fields and save integration; existing SSO scaffolding was reused. Historical SAML tests/mock data were added in RES-83777 changes.

My Account performance refactor `e9ec3d353c98cabb010e2e46177212fe67a7e8b1` lazily loads tab bodies through existing retry/loader components, replaces repeated makeStyles/header composition with responsive styled components, centralizes integration/API permission checks and removes an unused saved-banner timer/subscription. This supports reduced eager work and cleanup; the commit title's LCP/INP/CLS intent is not a measured score. `6579ac3185474b9598b18b9d80974b4d7c4cb94a` alone adds a CSS minimizer dependency and must not stand for the entire refactor.

**Paths/tests:** `containers/my-account/`, account stores, historical organization security/login-settings stores/renderers/services and SAML test files; later security/password-policy bug fixes in index. **Reuse:** “I implemented stateful account/security administration forms with validation, REST integration, dirty-state save/cancel behavior and follow-up performance improvements.” **Keywords:** React forms, typed state, MFA UI, SSO/SAML, API integration, lazy loading. **Avoid:** backend authentication/cryptography/authorization-engine ownership or measured Web Vitals improvement without timings.

### CORE-012 — Business-unit creation, editing and primary/shared membership

**Evidence:** PRODUCTION-context + authored Git; high attribution. **Status:** July–August 2023 implementation with later user-directory adaptation; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

I implemented Business Unit administration UI/store behavior, including edit/create fields, custom colors and primary/shared user selection. `7535077afc6dd58276d38fe4624b6991d2620330` establishes management components and adjusts service/layout paths; `ea980d6b4db1118785b69f266e087c2a025c9691` expands typed edit state to initial/temp BU data, all/primary/shared member collections, current list page and select-all origin flags. Member selection updates the temporary BU representation, dirty state and save/cancel flow, while list/filter changes distinguish membership types. Additional filters/feedback are in `ec0b6218e843931203bff725c4f311bd0b62058f` and later fixes.

The existing company/backend BU model and user APIs are dependencies, not sole authored backend architecture. The historical preload-era user collections were later superseded by the targeted user-resolution initiative (CORE-028).

**Paths/tests:** historical `containers/organization-settings/my-organization/company-info/business-units/`, business-unit services and Easy Peasy store/interfaces; current `organization-settings/.../business-units/`. `d92f8ba6aabaae19669688064bfc238dbfce2177` adds BuFrameWork tests and mock data; subsequent cleanup/fixture changes are distinct. Historical test existence does not prove current coverage or production release.

**Reuse:** “I built business-unit administration with primary/shared membership, selection state, validation and save/cancel workflows.” **Keywords:** enterprise administration, React/TS, state management, business units, testing. **Avoid:** server-side tenancy enforcement or treating the whole user/BU system as mine.

### CORE-013 — Organization settings framework, typed shared state and navigation

**Evidence:** PRODUCTION-context + authored Git; high for changes, collaborative overall architecture. **Status:** 2023–2025 framework evolution; current descendants; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

I helped build organization-settings 2.0 navigation/framework and consolidate section state. RES-94862 left-nav initial/new-UI phases (`d5964ab2c67637d287a7f77bab4e49b68b364ae4`, `3cd417dfc6befe18d5a4b398f130961cb397b945`, `053377d2a7aa818e99127637566a433584260c87`) derive navigation lists, active section and availability from feature/permission data, render category/sidebar entries and coordinate section URLs. Shared organization store updates (`540ba0ab47c8a94fce12cc0dcb618c92d461b1c1`, `7c80087115c6ae0f74433ead3c62bfd2af35499e`, `95c4166b6df351ff4fc3e09068d035009948fe36`) centralize company preference snapshots/actions and avoid each section independently rebuilding shared state. Individual module stores remain scoped.

Later feedback fixes address accordion toggles, selected menu/favourite handling, direct-URL access for Responsive AI (`1576b136e627c737e80436ce4c8e3eb91925ae78`), circular imports (`e74afb7eb487085c80d78147f7f99052aff5a1ce`) and discarded/unsaved changes. Global search (CORE-017) consumes this framework's navigation/permission contract. Shared state/hooks, feature-preference services and routing primitives are existing dependencies; collaborators authored other framework portions and numerous merged changes.

**Paths:** `organization-settings/containers/{Organization*,org-side-nav}/`, `store/OrganizationGeneralStoreImpl.ts`, `utils/{OrganizationUtils,org-sidebar,OrgSideNavUtils}.*`. Historical paths moved from `containers/organization-settings`; record snapshots matter. Tests appear across module suites; no audit run or whole-framework coverage claim. **Reuse:** “I implemented organization-settings navigation and shared typed state while preserving feature/permission and unsaved-change behavior.” **Keywords:** application framework, Redux/Easy Peasy, routing, state boundaries, permissions, refactoring. **Avoid:** sole ownership of organization settings or claiming backend URL access enforcement from UI route guards.

### CORE-014 — Integration setup, connection state and connector configuration

**Evidence:** PRODUCTION-context + authored Git; high for exact integration UI changes. **Status:** 2023–2025 implementation/fixes; current descendants; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

Highspot setup `183fc901aca2730226b1fd8f5ca5348714040c24` creates a configuration flow with initial/temp parameters, required connection fields and connect/disconnect state. `HighspotContainer` loads existing integration parameters, compares dirty values, posts configuration/feature preference changes and applies returned company preferences to shared state. Connection validation controls readiness; disconnect transitions status and the connected-app list; error paths log rather than treating every attempted request as success. This uses the existing integration service/backend.

Other attributable work spans Salesforce/Dynamics/Zoho/HubSpot/Pipedrive field mapping and connection/save validation, CRM branding/layout fixes and SharePoint integration-site listing. `2ecf55892726799e6e4e66a6ac93fcff31f35186` changes SharePoint site discovery/listing handling and related types/utils to address missing main sites; `664f812bf1ef8e85ee1bb16033ad29cc4853baf8` is a save-validation follow-up. Financial field conversion/currency formatting is separate UI correctness work, not connector/backend ownership. OAuth credentials/schema shape may be described; no credential values are stored here.

**Paths:** `organization-settings/containers/platform/integrations/`, integration services/utils/interfaces, My Account integration renderers and CRM components. Historical unit tests/mock changes exist where indexed; provider end-to-end validation/production enablement is not independently established. **Reuse:** “I implemented integration configuration UI with validation, persisted preferences, connection feedback and connector-specific fixes.” **Keywords:** third-party integrations, REST, OAuth UI, configuration workflows, error handling. **Avoid:** implementing entire provider SDKs/APIs, deployment ownership or claiming every connector was authored by me.

### CORE-015 — Response-project preferences, metadata and project import workflows

**Evidence:** PRODUCTION-context + authored Git; high attribution for listed changes. **Status:** 2024 configuration implementation with later maintenance; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

`6239357966fe52630fae6fbab93cbe4cfd1d7b31` builds Response Project preference layout/component mappings and state transitions: feature sections render configurable accordion content, track edited preference values and enabled counts, then serialize changes into the existing organization save contract. Project metadata and custom-option handling have additional reusable selector/checkbox fixes (`a531ae7faded3024a69f4b72433590c6925afd69`).

`ee9baa26e5c08226a54fb3575e8646e831f5c1e2` implements project import/download-template UI and service integration. Users select a metadata/template file, prepare multipart data and call `projects/respond/import-project-file`; metadata generation uses `users/admin/generate-project-metadata`. Batch details are observed using existing asynchronous process utilities; UI readiness/progress/error/notification callbacks tie import results to the configuration screen. That polling/batch infrastructure is not proof of my SSE transport implementation.

**Paths/tests:** `organization-settings/containers/response_projects/project-configuration/preferences/`, metadata/import mappings, ResponseProjectsService and related stores/utils. Historical tests and import/error fixes are indexed; no import throughput/coverage metric established. Server parsing/generation and job infrastructure are dependencies. **Reuse:** “I built project-preference and metadata/import UI with typed state, file/API integration and asynchronous job feedback.” **Keywords:** configuration, forms, file upload, REST, asynchronous workflows, TypeScript. **Avoid:** backend import engine or speculative measured performance.

### CORE-016 — Reusable custom-field management and content-library configuration

**Evidence:** PRODUCTION-context + authored Git; high attribution. **Status:** June–July 2024 implementation plus 2025 fixes; current descendants; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

I built/extended common custom-field CRUD drawers, renderers, search/reorder and import/export behavior across project/intake/content categories. `42f74b306d8ae8caa786ef8566dbe0e0c6c4e613`, `fa15454969ab34fe1acc424793c886385c4b254e`, `538d77619114702279ac304a0ff3ed594d03cdc5`, `f7872ad766570a3d995408d5b9541629224d3ec1`, `75b0e9c8f08e1785a863a3e5a93ba0c12f95e7f3`, `3fe280a5f292c95cd8b58e6d1086c5dd30d9d4b9`, `b453ba1dc72738e5df19893c3b2e3121a39bd7e8` show distinct phases rather than repeated single-feature deliveries.

**Flow:** A typed replica of a selected field is edited separately from persisted state. Required name/display/value/project-type checks control action readiness; duplicate/invalid identifier handling prevents invalid saves. Easy Peasy updates trim/deduplicate option values, toggle selected project types and adjust searchability/mandatory flags by field type. Category switching selects allowed types, preserves previous edit type where appropriate, sets category-specific auto-increment defaults and disables unsupported facets/mandatory options. Payload construction includes group/entity/category/CRM mappings; async initialization loads Salesforce/other CRM metadata before choices are exposed. Dirty drawer state supports warning/save/cancel. Reorder, advanced filters, CCL categories and import/export upload are reusable configuration operations; they are not independent backend-schema ownership.

**Paths/tests:** `organization-settings/org-common-components/custom-fields/`, `utils/custom-fields/`, `store/custom-fields/`, platform library-setup configuration, historical custom-field tests/mock data. Subsequent backlog fixes address category/option validation, group names, import translations, CRM mapping and search/reorder behavior; see index. **Reuse:** “I implemented reusable custom-field configuration with category-aware validation, state isolation, CRM mapping and import/export.” **Keywords:** reusable UI, schema-driven forms, TypeScript, state management, CRUD, enterprise configuration. **Avoid:** dynamic database/schema engine ownership or calling every affected screen a separate migration.

### CORE-017 — Permission-aware organization settings global search

**Evidence:** PRODUCTION-context + authored Git; high attribution. **Status:** August 2024 initial/phase-II implementation with later fixes; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

I implemented organization-settings search across settings categories. `bb4ef8d11ae6ac41a24eda913ffec41a4b5376f9` starts text/word matching; `ef8549454f33fd0c3cfd6dad1fbf425d6b37c64b` introduces `searchConfigMap`, `searchPermissionMap`, typed search store and results/recommendation/quick-filter components. Search configuration combines translated labels, feature availability and user permissions; results group/label matching settings and omit inaccessible targets.

`5834ead5ca6fd02d762db2557c3c231a4a25f462` maps selected result identifiers to destination sections, parent accordion expansion and query parameters. `a806e84da0dfb5873c9bfb96f4c383cc624982dc` extends phase-II coverage/dynamic labels, so selecting a result both navigates and reveals the correct nested setting. State tracks search text/focus/identifier and returns to appropriate framework content when cleared. This is client-side settings discovery over known configuration, **not Solr/Document Library full-text search**. Voice search experiments are separately CORE-036.

**Paths:** `organization-settings/containers/org-global-search/`, `utils/org-search-utils/{OrgSearchHelper,OrgSearchUtils,OrgSearchLabelUtils}.*`, `store/org-search-store/`, OrganizationHeader. Later duplicate-word, permission and navigation fixes are preserved. Exhaustive standalone search tests/latency metrics were not established in this audit. **Reuse:** “I built permission-aware settings search with grouped results and deep navigation to nested configuration.” **Keywords:** search UX, permissions, routing, i18n, state management. **Avoid:** backend search/index authorship or measured search-scale claims.

### CORE-018 — Content-library search UX, Document Library facets and reporting integration

**Evidence:** PRODUCTION-context + authored Git for listed CCL/report fixes; USER-CONFIRMED (U2) for personal implementation of Document Library faceted-search UI. **Status:** 2023 document fixes and 2024 CCL redesign; the faceted-search implementation period/current version is unspecified; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed Git-authored changes; personal faceted-search UI implementation confirmed by U2. Exact faceting mechanics and collaborator boundaries beyond that statement remain unresolved. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

I changed CCL search input/recent-search behavior, placement and shared-header integration across RES-107917/108345/109053. `ace4713ecb4b44e233b4f750f6302dd7a733e5cb` and its follow-ups adjust `ContentLibraryInputSearch`, recent-search presentation, focus/close/empty behavior and framework location. `fd5f242c22ecac7882d9e0d94a072ee7b6b7c54b` corrects empty recent-search behavior. Related small document/download/display and subscribed-content popover fixes are indexed; do not treat them as an entire Document Library feature.

Organization search-configuration fixes prevent duplicate custom stop/related words (`35ff6d74eefc4243efc40418f2751e715608cd11`). The 2026 Content Search Terms Report crash correction reads company plan in the component rather than invoking a hook from a helper (CORE-028). These are frontend configuration/reporting repairs; endpoint usage does not establish Solr indexing/query internals.

U2 explicitly confirms: **I implemented Document Library faceted-search UI.** This is user-confirmed frontend contribution evidence, not a located originating diff. **Exact paths/SHAs, facet/filter payloads, API/error states, tests, dates and collaborator boundaries remain UNKNOWN**. No numeric outcome is supplied. S p1 separately establishes Java MongoDB/Solr response-header synchronization; server.md is the backend scope. The UI confirmation does not establish authorship of Solr indexing/query internals or the backend search engine.

**Paths:** `containers/content-library/ContentLibraryInputSearch*`, search/header components, library configuration stop/related words and reporting. Tests/metrics beyond listed historical changes not established. **Reuse:** “I implemented Document Library faceted-search UI, improved content-library search UX and corrected document/search-report integrations.” Faceting uses U2 provenance; the listed CCL/report changes use Git provenance. **Keywords:** faceted search, Document Library, search UI, filtering, recent searches, React, reporting. **Avoid:** inventing facet/API/test mechanics, backend search construction, sole feature ownership or measured search outcomes.

### CORE-019 — My Work discussion workflows and rendering/state refactor

**Evidence:** PRODUCTION-context + authored Git; high attribution. **Status:** 2023 discussion 2.0, September 2024 performance/state refactor, 2026 test migration; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

I implemented/extended discussion/thread/comment UI, mentions, attachments, entity-name navigation, counts and resolve/dismiss/edit behavior in My Work (`7534b6ee86efdb4ed3dcf5ae1ad631676cf30fa8`). Historical tests/mock changes include `803c36931e7b9620b7b1c413b364a5d78c084c5e`; some early tests rely on mocked store/timer behavior and should not be overstated as comprehensive end-to-end validation.

`115c883628c4f1d49792537112500ca851f9bffd` introduces dedicated discussion components and an injectable Easy Peasy context store: `initDiscussions` fetches IDs/data; selectors render keyed cards/child comments; store actions handle status, current comment/entity, attachment preview and mention/add-to-team confirmation. The page shows skeleton until initialization completes, then count/content or empty state. MyWorkService normalizes successful Axios responses to data and returns false/logs on unsupported/error cases. `9363f2bef02b00acae9304f5cf275de8991e205d` refines store behavior; `e014399a67c35235dabd2a9d641c3b6554afc3b7` removes a redundant discussion provider. Moving mutable discussion/preview state into scoped selectors and removing duplicate providers supports reduced redundant work; no numeric rerender/latency improvement was measured in this audit.

**Paths/tests:** `containers/my-work/{MyWorkDiscussion,discussions}/`, `store/my-work-store/MyWorkDiscussionStore{Impl,Model}.ts`, MyWorkService and discussion components. 2026 Vitest suites cover task/dashboard/calendar/filter/discussion paths and share HTTP fixtures (CORE-006); historical Jest deletion is not full test preservation. **Reuse:** “I built My Work discussion workflows and refactored their scoped state/rendering, including comments, mentions and attachment feedback.” **Keywords:** state architecture, React performance, discussions, async UI, testing. **Avoid:** quantified render reduction or original ownership of every My Work feature.

### CORE-020 — Plans & Billings 2.0, usage rendering and tests

**Evidence:** PRODUCTION-context + authored Git; high attribution. **Status:** October 2024 implementation, 2026 Vitest/E2E reference module; deployment UNKNOWN. Separate from CORE-003 internship migration.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

`dd03ac62c4684ff4b7d5507d42f9bb48894f79a3` introduces the React Billing 2.0 container, typed billing props, plan/update cards, usage/progress charts and BillingService/BillingUtils. `PlansAndBillingsInitiator` sets the shell title, loads payment then space/usage data and replaces a loader with plan content. BillingService GETs `users/payments/get` and `space/get-company-spaceinfo`; non-success/error paths return false or log. The initial container does not demonstrate a robust full-screen error UX, so do not invent one.

`initBillingInfo` derives monthly/category/current subscription/custom cost and feature-based plan type from payment and company preferences. `initChartData` normalizes space units and active-project/user quotas into chart ranges; the original small-usage floor is presentation logic, not changed storage consumption. Online/offline renderers use different amount/date shapes (online cents/currentEnd; offline cost/renewal), display renewal/year/month copy and free/enterprise exceptions. Responsive cards, preferred subscriptions and dismissible banner adapt to plan context.

**Paths/tests:** `containers/plans-billings/{billing-card,service,utils,props-type}/`; `ffbb4baf422051ea7e7838e7f76f25804e2fc32c` adds historical Billing tests/fixtures; follow-up implementation/legacy sunset fixes are indexed. CORE-006 migrates/extends it with Vitest HTTP fixtures and ready+interactive Playwright smoke. Backend billing/payment processor/entitlements are existing dependencies, not my sole architecture. **Reuse:** “I implemented plan/billing presentation with payment and quota APIs, online/offline plan rules, responsive usage cards and tests.” **Keywords:** React/TS, billing UI, REST, charts, responsive design, testability. **Avoid:** payment-system ownership, production revenue outcomes, or re-dating this to internship.

### CORE-021 — Single/multiple user administration and reusable user pickers

**Evidence:** PRODUCTION-context + authored Git; high attribution. **Status:** 2024 administration implementation, 2025 user-chip refactor, later targeted-hydration adaptation; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

I implemented add-user/multi-user UI and related user-management fixes: `eb35102ee54c88bd3261fdd129071dbe1ade24e6`, `4c32d5bccf25760d97430b359ce488473d1b8c61`, `6b85885ee606ef0bffd5524c3f8fedd731238318`. Forms collect recipients/roles/BU fields, manage invalid-user maps and readiness, apply existing eligibility/plan/permission rules and send payloads through user services; returned state updates drive list/drawer feedback. Multi-recipient handling preserves validation rather than treating all entered addresses as accepted. Exact backend invitation/authorization logic is not attributed here. `7e4faea00b9ace8a9655ed8d13a61007dc21e3c7` reverts a specific MultiUserInitiator change, not proof the entire administration feature was removed.

2025 `user chips revamp` (`8fdf7aee248dded2465c7b6a928ebdbf9d1e3ed1`, `4847dfc1c4a823817df2258aef126c8d6948d9e0`) adapts shared picker props/rendering across BU selection, project-task templates, CRM and report/configuration surfaces. Follow-up fixes restore display/eligibility and target-audience/search criteria behavior. CORE-028 subsequently replaces full-directory assumptions with targeted cache/discovery APIs; do not claim historical preload logic is the current model.

**Paths/tests:** `organization-settings/.../user-management/manage-users/add-users/`, user-list/details utils/services and `rfp-components/user-chips/`. Historical tests/mock edits are indexed; no invitation success-rate/scale metric. **Reuse:** “I implemented single/bulk user administration and reusable user-picker flows with validation and permission-aware configuration.” **Keywords:** user management, forms, enterprise UX, validation, component reuse. **Avoid:** backend RBAC/invitation engine ownership or claiming all picker primitives originated with me.

### CORE-022 — Role/permission comparison view and interaction tests

**Evidence:** PRODUCTION-context + authored Git; high attribution. **Status:** November–December 2024 implementation/test follow-ups; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

`84e394956b1255c362ed16fe7274b09ad2a4d7f3` adds list/compare view switching through `rolesStore.currentToggleView`, an exclusive accessible toggle group and comparison UI. The comparison view organizes role columns against permission/module rows, with a pinned reference column, drag/reorder behavior, nested module expansion/search and responsive presentation. It consumes existing role/resource-policy data; it does not implement server-side permission evaluation.

`532c11ba6b26f428c41716cf0297bb92a1810a76` and follow-ups add historical tests for view defaults/transitions, pinned/drag behavior and nested permission presentation. These are concrete interaction-test contributions; no test execution or current suite completeness is asserted from source existence. **Paths:** `organization-settings/containers/my-organization/user-management/manage-roles/`, role-store/framework helpers and tests/mocks.

**Reuse:** “I implemented an interactive role comparison view with sortable columns, nested permission rows and regression tests.” **Keywords:** complex data UI, permissions UX, drag-and-drop, interaction testing, accessibility. **Avoid:** building the authorization engine or a measured admin-productivity result.

### CORE-023 — Organization activity browsing, server paging and detail views

**Evidence:** PRODUCTION-context + authored Git; high attribution. **Status:** November 2024 implementation with later dependency fixes; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

`1e8aa548bc9db605b6fefee7bc4978e792298602` builds organization activity browsing with AG Grid, filters and detail drawers. Requests use row offset/limited batches and transformed filter data rather than loading every activity at once. `1950e901462f74e3d95970bf6806be60087525a0` passes backend `result.totalCount` into the grid instead of unknown −1 and adjusts initial row counts, allowing the grid to reason about available pages and stop correctly. Backend audit generation/storage is existing infrastructure.

Later org circular-dependency cleanup (CORE-013) includes activity-related imports. **Paths:** `organization-settings/.../my-organization/activities/`, service/filter/framework helpers. **Tests/outcome:** historical test-related changes are indexed; qualitative paging correctness is supported, no latency or record-count improvement measured. **Reuse:** “I built paged organization activity browsing and corrected grid total-count/filter behavior.” **Keywords:** AG Grid, server-side pagination, audit UI, filters, REST. **Avoid:** audit pipeline ownership or invented scalability numbers.

### CORE-024 — Support portal home, billing administration and pod selection

**Evidence:** PRODUCTION-context + authored Git; high for listed portions. **Status:** October–December 2024 and July 2025 changes; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

`4a93e2022f54638b47112e0fd4b0a05c8a83c1b6` implements support home/tile/navigation behavior, using support login/role state and setting page title/navigation to support routes. `9db4da693531d4a9124833fe03f9035f024cd3d5` extends support company-billing/preferences editing, counts/entitlements and copy/help feedback. Existing support authentication/admin APIs are reused, not an entirely authored portal.

`c101760a7580441b99ad0449c27301bdee81a6a8` corrects support pod-name selection/fallback and related company suggestion types; other commits address support style isolation and request/save validation. This is application configuration/routing for support workflows, not pod provisioning or infrastructure deployment ownership.

**Paths/tests:** `app_v2/src/support-portal/`, support company services/models, org/company wrappers; historical tests or manual validation details beyond indexed changes unknown. **Reuse:** “I implemented support-portal navigation/configuration features and fixed company/pod and billing-administration behavior.” **Keywords:** internal tooling, administration UI, troubleshooting, REST, feature permissions. **Avoid:** entire portal ownership, infrastructure management or production incident metrics tied to this feature.

### CORE-025 — Email-template rendering, client compatibility and deep links

**Evidence:** PRODUCTION-context + authored Git; high for fixes, broader builder ownership not established. **Status:** December 2024–February 2025 changes, some explicit reverts; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

RES-130235 changes modify preview/delete/dialog/email rendering and common email styles rather than proving original authorship of the full template builder. `0f5b1ba3f3c92d673a72f954b1e9830acf188103` and follow-ups adapt preview/style handling; Gmail (`24f2b2343d6ebf834fef34b08c2525566ca04da8`) and Outlook fixes address mail-client rendering. `58da0e14f3be5911a6ad673e71baf8e5d8909f6b` changes template styling for the dedicated-DB migration context; it is not evidence I built the DB migration engine.

Email redirection `6da2e2afda2cb76a390267847e30aacd77a1efe8` is followed by explicit revert `f14ea1be25aaff37c26686f46107ef958499d540`; later routing changes must be distinguished from that reverted attempt. Gainsight source tracking `740fa973b49c91986ba8bdcde7fbc42c38b6b66f` / RES-134791 parses template/source query context in login/base layout to route/track the correct source; this supports instrumentation integration, not a measured conversion/adoption result.

**Paths/tests:** `app/app/css/email/main-style-sheet.css`, email-preview/org email components, `containers/login/LoginUtils.ts`, BaseLayoutInitiator; historical regression test changes indexed. **Reuse:** “I fixed enterprise email-template rendering across clients and application deep-link/source routing.” **Keywords:** HTML email, client compatibility, i18n, routing, instrumentation. **Avoid:** full email-platform authorship, database migration ownership or inferring analytics impact.

### CORE-026 — Agent Studio authoring, Ask execution UI, history and Markdown

**Evidence:** PRODUCTION-context + authored Git; high for frontend implementation; S broader ADK-platform evidence medium. **Status:** September–November 2025 phases with current descendants, specific reverts; deployment UNKNOWN.

**Attribution confidence:** HIGH for frontend code; MEDIUM for broader S platform claim. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

I implemented substantial Agent Studio frontend foundations and Ask agent experience. `bce81162c6c0a099fa74b87fdf5a692651c859f8` creates `AgentStore.ts` and filter-service integration; `b4623b6dc28c481d48f214141c8131103fddbc01`, `401a15aba24ba10f8803a170fec108da675035a4` and subsequent commits expand create/list/view/preview and agent-run UI. **The store uses Easy Peasy, not Zustand.** It maintains agents keyed by ID plus ordered IDs/current draft, input fields, knowledge-source filters, saving/error and add/update/remove/reorder actions. Filter initialization GETs `/answer-lib/get-used-filters-AI`, conditionally includes response headers, constructs filter state and falls back to default filter options on caught errors. Early `saveCurrent` upserts locally; later API/publish behavior is collaborative—do not describe that first draft thunk as a completed backend persistence API.

The Ask side builds v2 chat/cards/agent details/selection/history, loading/run-state controls, attachments and document-canvas/citation/export views. `triggerAgentRun` serializes `agentQueryRequest` plus keyed file fields into multipart FormData and POSTs `/agents1/scoped/trigger-agent`, logging errors; UI updates Redux-backed conversation/agent/run state around the request. `14c144b865350f18741676d56abc7222d7b8f150` introduces research-agent behavior; `25256ee94aaeeda05308fba87315817812230857` develops the later UI. `64f337b9b33ef8e258b0bfaf3cfdab48070da2d1` adds Markdown math support with remark/rehype/KaTeX, currency-dollar escaping and rendering integration; `7ad8761b5be69e92364c0bf9bd09621ae4146b0a` fixes HTML display for older conversations. Some chat-history/new-UI changes were reverted (`00ee18a73d40c80ed014feba6cce9631b8aefaf7`); not a full platform rollback.

**Paths/tests:** `app_v2/src/ai-agents/{components,store,services,steps,utils}/`, `app_ask/src/{components-v2,containers-v2,service,store,utils}/`. `1662e26d80f7e0726fc2d5ed827acd81f2adfb6f` adds Jest suites for create-flow, inputs/purpose/knowledge/list/view/preview and utilities, with wrappers/fixtures; 2026 legacy cleanup changes availability. Gokula/Subash and others have visible foundation/follow-up commits: my initial store/flows do not imply sole platform ownership. S places the ADK/custom React platform in Sep2024–Sep2025; visible code continues into Oct/Nov2025, which is a phase/role-placement reconciliation gap, not permission to redate canonical roles.

**Reuse:** “I implemented typed agent-authoring state and a custom React agent/Ask UI with file inputs, run feedback, history, citations/canvas and test coverage.” **Keywords:** AI application UI, agents, React/TS, Redux, async workflows, multipart APIs, Markdown, testing. **Avoid:** ADK/RAG engine authorship solely from frontend code, sole platform ownership, or claiming every run/stream service is mine.

### CORE-027 — AI-assisted external-source integration prototype and hackathon evolution

**Evidence:** HACKATHON (F/S/P) + PROTOTYPE/POC Git; high for UI branch changes, medium for approved 5+ demo services. **Status:** July 2026 prototype branches; later production evolution approved but mapping/rollout UNKNOWN; deployment UNKNOWN.

**Attribution confidence:** HIGH for branch UI changes; MEDIUM for demo/service/evolution narrative. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

`6c75ca697cdbd7de2f547752656fe01cb4d929e8`, `944dc362a36d85bcca71ffc62dc24bc28ac9230e`, `de7c83b245e82bab21ce1e8559531ed3757a8d06`, `ca132bcd6f20a838a8c53aff86beddcfd95206af`, `29ece93dc58ddfe0a72a62c2af9f756f3f589cbc` implement AI-assisted Add Source UI/auth-schema/folder-discovery flows. A prompt requests integration metadata; `normalizeExternalSourceAuthSchema` handles clarification, token/OAuth schemas, required fields, snake_case→camelCase names, defaults and documentation/provider data. Redirect URI is app-controlled and excluded from visible credential fields. Values are trimmed/mapped into authorization payloads, with nonstandard fields carried as additional token parameters. URL/token result normalization accepts several response shapes; successful token-stored/authorization-required flags drive connected state. Popup callback/code handling and folder-root/child discovery support an interactive configuration wizard.

Service paths include `ask/authorize-api` and `ask/discover-root-nodes`; failures log, authorization errors rethrow and discovery returns undefined for unsupported/error results. At inspected July SHA, **`USE_ADD_AI_SOURCE_MOCK_API = true`**, with delayed mock auth and nodes. This is explicit prototype evidence; schemas/provider labels or mocked success do not prove live provider execution. UI/resource categories and clarification prevent treating every prompted source as supported. No real credentials are reproduced.

**Folder-selection execution:** at `29ece93dc58ddfe0a72a62c2af9f756f3f589cbc`, `FolderPickerCard` maintains selected IDs, expanded/loading sets and a childrenMap. `getFolderSelectionState` computes checked/indeterminate/unchecked from the node and its **loaded** descendants; `syncAncestorSelection` walks parent relationships, adding an ancestor only when all known descendants are selected. Toggling affects the node/subtree and updates ancestors. Expansion reuses cached children or calls discovery, propagates an already-selected parent to newly loaded descendants and clears the loading flag in finally. A later empty-child result disables expansion; search matches node names/known subtrees. This is consistency over the loaded client tree, not proof of exhaustive server-side hierarchy traversal.

`IOSFolderGroup` adds a compact/full source preview and a React portal into the drawer. The source palette uses labels/images or fallback initials; expanding opens a labeled dialog, Escape/backdrop starts a 220ms close transition, and internal clicks do not dismiss it. The later version shows source-session statuses and invokes onSourceSelect to reopen a saved session. Labels such as Dropbox/Drive/Box/SharePoint/OneDrive/Confluence/Jira are UI metadata, not evidence of live integrations. `71b51c794a2e6c42eb4c8dbafe31284f2c51dc5f` is an unreachable July 12 alternate iteration with these folder/preview foundations, preceding additional session/service behavior in the ref-reachable version. Its stable patch differs; it remains part of this same prototype initiative, with merge/deployment UNKNOWN. Keyboard labels/Escape handling do not establish a complete accessibility audit, focus trapping or reduced-motion support.

**Paths/tests:** `organization-settings/.../platform/ai-assistance/external-source/AddAISource{Drawer,AuthSchemaService}.*`, external-source framework/utils/folder components; no complete live-provider/E2E test record established. F/S/P approve **5+ services including Chorus/Jira** and later production evolution. June hackathon narrative versus July commit dates requires phase clarification; preserve both. Backend agent/tool execution and production connector deployment require separate server/manual evidence.

**Reuse:** “I built the React UI for AI-assisted integration discovery, clarification, dynamic auth forms and folder selection during hackathon/prototype development.” **Keywords:** AI integrations, schema-driven forms, OAuth UI, prototypes, API orchestration. **Avoid:** claiming every mocked provider was live, five production integrations from these files, secure audited credential storage or sole backend execution ownership.

### CORE-028 — Removing full-company-user preload: targeted hydration, discovery and regression fixes

**Evidence:** PRODUCTION-context + authored Git/PRs; high for my migration/fixes, collaborative architecture. **Status:** May–September 2026 phases, merged integration/fixes, current reference contract; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

The v2 boot contract no longer includes all company users. I inventoried affected reads, migrated broad surfaces and fixed regressions from removing preload-era maps/utilities. Planning `08c2b5f45bc57d759e87ef17654edd284f6de02c` is distinct from implementation `d9e73b563f2fc9f57faa4509f927fa7ea3ec50c1`; `66d66457e64d3d71270f3956e8c75e410606e8ce`, `587b364bd91442464b96d5fa5f3d4ad1c731b3ce`, `60ab7267943002240bdb2dc46e44bbdf3549883a`, `74318edb2392164c572324b3603205d92e7d103b`, `e0068069be8fa24a2b6ad8a2e7c5f3d87e75fc98`, `f70dd50c8c5ee82feddfb0341d94a49b379f0934` show active-user/display/other-method phases. Do not count per-branch transports as new features.

**Current flow, used/adapted by my changes:** boot seeds logged-in user in cachedUsers. Known usernames resolve through shared UserName/UserRole/UserAvatar or batched `get-uservo-list`, queued/debounced by store/cache helpers; guest/orphan negative caching prevents repeated unresolved lookups. Discovery/autocomplete/mentions use `suggest-users-by-keyword` with role/BU/module/tag/permission-related request fields; the partial cache cannot represent the eligible-user universe. Directory aggregates use `get-user-directory-meta` with optional slice refresh for tags/OOO/super-admin/count rather than reloading profiles. Updates use logged-in userInfoVO when only current-user facts are needed. The API default suggestion limit is 25 unless skipLimit; it is not a paginated load-everyone API. This flow is described in the inspected `docs/user-resolution-reference.md`; current shared transports/cache infrastructure includes other authors' work.

My follow-ups fix agent-run-history lazy user display (`c8030fa1890fde21efdfc03d22ec35b091164f77`); mention display and suggested-user seeding, team-name dedupe, `PROJECT_DISCUSSION`→`PROJECT` endpoint module mapping, duplicate-answer edit access and Content Search Terms Report hook/max-update-depth crash (`3af64d1119634d68e3dd69e78b034e8a05a61516`, `f6020cbfebb59cd8ff5a8b6e1da0835175704005`, PR-7831); Axios company-switch exemption for directory metadata (`f314727aa4b26afd500d3ff5cb3908ceff713d8e`, PR-8927/8925). The PR includes linked Jira IDs RES-185195/185164/185193/185186/185179, whose issue bodies were not accessible.

**Paths/tests:** `utils/user-cache/`, `utils/user-load-details/`, UserDataStoreImpl, authContext, user-chip transport/components and many migrated modules; no-user-list bootstrap fixture in CORE-006. PR-5147 initial proposal closed unmerged; 7411/7512/7708/7831/7897 and follow-ups merged into differing feature/integration bases—see exact register. Hari's boot change and Akarshan's follow-ups are collaborators' work. PR-7826 is a closed unmerged 532-commit aggregate with only five local author-matched commits; its entire diff is not mine. No measured boot payload/latency reduction is established.

**Reuse:** “I migrated frontend consumers from a full user-directory preload to targeted hydration/discovery/metadata APIs and repaired mention/report/history regressions.” **Keywords:** payload optimization, caching, lazy data, API contracts, permissions, refactoring, migration. **Avoid:** sole backend/cache architecture, full-directory completeness from partial cache, or invented payload/performance percentages.

### CORE-029 — Lyra application adoption, brand themes and hosted theme isolation

**Evidence:** PRODUCTION-context/TOOLING + authored Git/PRs; high attribution for app integration. **Status:** May unmerged i18n POC; September 2026 scope/theme migration merged; deployment UNKNOWN.

**Attribution confidence:** HIGH for application adoption changes; enablement/component metrics retain F/S/P scope. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

I migrated application imports/dependencies from `@lyra` to `@responsive-lyra`, adapted peers/registry configuration, initialized brand/material themes and updated test mocks (`4d6ea78f206a85c8324db01f8211bf72d83f6af8`, PR-8662/8762/8694). This changes application consumption across hundreds of files; mechanical scope replacements are not hundreds of new features or proof I wrote all those components. Package component development/70+/>90% metrics remain in the design-system context.

`packages/utils-shared/src/ColorUtils.ts` maps brand hex/names to the supported material/Lyra theme palettes; BaseLayoutInitiator derives company branding and wraps content with the provider/rem-14px bootstrap. `3e45e258ec5f4a048215ba4c1b5621386bd3742a` changes `responsive-lite/src/components/AppWrapper.tsx`: standalone retains document ThemeProvider; hosted mode wraps content in `LyraScopedThemeProvider` because the document provider writes/deletes body data-theme/data-mode and could overwrite/remove the host company theme when the remote unmounts. I preserved auth/i18n/snackbar/store/router composition while isolating theme scope. Federation translation initialization is CORE-002.

May internationalization `6eb94f4faff4d96d9f906644ddfc0f82e4296148`, PR-4476 (“[DON'T MERGE] DS-469: Internationalization for Lyra (Requires Lyra AI Publish)”), is **closed unmerged**. Its bootstrap/i18n/preview experiment and my exploratory review comment are not a shipped rollout. March PR-1271 similarly closed unmerged; later package bumps are separate successful integration changes.

**Validation/review:** PR-8762 author reports build/UI/theme checks; review on PR-8694 requests removing unwanted whitespace, demonstrating integration review rather than original feature authorship. Credential rotation/config files were inspected only as non-secret metadata; no values are retained. Group enablement for 50+ engineers is F/S/P, not proven by import counts. **Reuse:** “I integrated a shared design system into multiple applications, mapped company branding and isolated hosted micro-frontend themes.” **Keywords:** design-system adoption, theming, integration, Module Federation, developer enablement. **Avoid:** component-library authorship from imports or calling the unmerged i18n POC current.

### CORE-030 — Repository graph tooling, opt-in GitNexus hooks and safe removal

**Evidence:** TOOLING, authored Git/PRs; high attribution for integration/maintenance. **Status:** June–July 2026 setup, removed September 2026; historical/superseded; deployment N/A to product.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

Graphify per-package artifacts/graph setup (`7739f3417a2cb9028c5e21aa67857d2fbb1ecd74`) and GitNexus integration (`9ccfe2363c442bd22ff3231a4800fd7174d04aa1`, `9f8522a91e3dd9435443a7c97a835cdf2fd5934c`) are tooling work, not product features or authorship of the underlying graph/embedding algorithms. PR-7005 describes per-clone opt-in `.gitnexus.env`, manual init/sync/status/clean/UI and post-commit/merge/checkout/rewrite background index hooks. Path gating skips irrelevant changes/modules; atomic mkdir locks plus stale-TTL recovery/traps protect concurrency; failure markers allow diagnosis/recovery. Windows scripts locate Git Bash through a Node runner and force LF for shell files. Hooks are a no-op without opt-in and background indexing does not block commits.

`scripts/gitnexus-hooks.test.sh` covers locks, skip paths, traps/crash recovery and gating; PR-author screenshots/test narrative report fresh clone/no-op, init, full sync, cleanup and automatic reindex. Screenshots were referenced, not independently visually verified or rerun. Turbo graph/input configuration follow-ups are distinct.

Removal `01456bc7a974eae211f231a3f67c98fe88463e92`, `347f7cf504b3982cd47a4193c7fb0966f54f71f1`, PR-8869/related cleanup PRs removes hooks/config/scripts and obsolete generated artifacts. A reviewer identified standalone `app_pursuit_intelligence/tools/host-smoke/package-lock.json` as still needed because that tool is outside workspace/pnpm; I restored it (`3c645cbf5c0611e58ad1a22daa1f89d327365dcd`) and reverted accidental merge formatting (`598814c78bcb2ae62ce8b2d98799b39b2a4ffb48`). This is evidence of review response and scoped cleanup, not current GitNexus adoption. **Reuse:** “I integrated opt-in repository graph tooling with safe background hooks/cross-platform runners and later removed it while preserving standalone tooling.” **Keywords:** developer tooling, Git hooks, concurrency, failure recovery, cross-platform. **Avoid:** product deployment, current use, proprietary graph-engine authorship or treating generated graph files as implementation.

### CORE-031 — Reliable backport workflow and conflict reporting

**Evidence:** TOOLING, authored Git + PR-8354/8358; high attribution. **Status:** August 2026 merged workflow; deployment N/A to product, CI use not comprehensively replayed.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

The old workflow walked all PR commits, including merge history, and could continue after conflicts, yielding repeated/nested conflict markers and incorrect backport scope. `5d1922b7e357126f9743a87c948589e62f7762cb` replaces this with one cherry-pick of the merged result (`-x -m 1` for merge commits; plain `-x` for squash/rebase), drops empty/already-applied work, checks for an existing backport PR and preserves promotion/skip rules. Clean changes may auto-merge; a conflict stops at one marker state and creates a draft PR without auto-merge; unexpected failures abort and preserve manual retry guidance.

**Path:** `.github/workflows/backport-to-lower-branch.yml`. PR-8354 body contrasts a problematic broad backport with a smaller manual result; those counts are case-specific, not aggregate productivity metrics. Its test plan is unchecked. Later bot discussion on PR-8762 reports creating draft backport #8802; this is an observed bot report, not independent validation of every path. **PR-8358 also targets staging**, despite its name/history suggesting a sync variant; use inspected base metadata, not assumed development destination.

**Reuse:** “I corrected automated backport semantics to cherry-pick the final merge result once and surface a single actionable conflict draft.” **Keywords:** GitHub Actions, Git, CI/CD tooling, cherry-pick, failure handling. **Avoid:** all scenarios tested/passed, deployment ownership or claiming new CI algorithms beyond the authored workflow.

### CORE-032 — Runtime loading and dependency isolation on ux-opt

**Evidence:** authored Git, branch implementation/TOOLING; high attribution, production adoption UNKNOWN. **Status:** `f812f111a15458dc2e324c3677650352345ff2b4` on `ux-opt`, `origin/ux-opt`, `origin/akarshan-ux-opt`; absent from inspected HEAD/staging/development/master ancestry; branch-only evidence, deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

I reduced eager dependency work in Ask/API/export/date/bundle paths. Markdown math removes the static rehype-katex import, detects math after currency-dollar escaping, shares one load Promise and conditionally supplies the plugin; `useMarkdownMath` triggers a rerender after load, while canvas/history conversion awaits math before rendering non-HTML text. The inspected code lacks an explicit import-rejection retry path; do not invent one. XLSX loads only during Excel export; SwaggerWrapper uses React.lazy/Suspense when API schema is available. These are code-level loading changes, not measured page-load results.

Date/time helpers consolidate Dayjs operations while retaining Moment-compatible date-picker return contracts; tests cover New York DST boundaries, instant serialization and from/to day bounds. `listUtils` isolates an in-place add/remove helper so importers avoid the large GeneralUtils module. Split-chunk package naming handles normal/scoped/pnpm/nested/Windows paths and misc fallback. Vendor/sourcemap/font cleanup spans multiple app configs. Existing date/Markdown behavior is preserved where tested; a complete Moment elimination is not established.

**Paths/tests:** `app_ask/src/utils/{Markdown,GeneralUtils}.ts*`, APIExplorerContainer, `utils/{DayjsUtils,listUtils}.ts`, `utils/tests/DayjsUtils.timezone.test.tsx`, `listUtils.test.ts`, `packages/build-utils/__tests__/getSplitChunkPackageName.test.cjs`, shared DateUtils/configs. Tests were read, not run. No associated live PR found in the authored-PR inventory. **Reuse:** “I implemented branch-level lazy loading and dependency isolation for math rendering, export and API explorer, with timezone/package-path regression tests.” **Keywords:** code splitting, lazy loading, bundle optimization, compatibility tests. **Avoid:** shipped performance claims, an invented percentage, successful import recovery or removing Moment entirely.

### CORE-033 — Shared UI correctness, accessibility details and cross-browser fixes

**Evidence:** authored Git/PRODUCTION-context; high for individual fixes. **Status:** 2023–2025 changes with current descendants; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

Meaningful small work is retained rather than absorbed into architecture claims: shared button/theme color fixes; help/footer/feedback/tour behavior; keyboard/dialog focus; image alt and toggle labels; scroll/overlay/layout adjustments; account/profile/header navigation consistency; fonts/Inter anti-aliasing and Mac/Safari/Firefox fixes. These are specific accessibility/compatibility improvements, not proof of a WCAG audit or full browser certification.

Concrete before/after examples: `97f57c685049fab69439325b6a156f5917313f84` makes accent-color lookup tolerate an unknown color with a fallback instead of throwing during instance load; `88c7bd0dc720f6fd8e8acbb501354e21d7bd1eda` rereads window.location/current query parameters inside `setSearchParamsState` to avoid stale search state during Mac back navigation; `09613847e977aec3aa3a636ce8013ccc10dee560` / `8eccf1618603225eca97026b3581b943a6e7dc22` correct translation-wrapper behavior; `780d1784e1dd3760a75f38953c2d67d41e1050a4` restores dialog focus; `a3b42520fe3e2b13e1448a8fc5cf8af5face3cf4` changes decimal text-input handling after an earlier per-screen attempt was reverted. These use existing design/routing primitives.

**Paths/tests:** shared `rfp-components/`, header/footer/help components, URL/search hooks, ColorUtils/translation wrapper, App.css/fonts and affected feature screens. Historical header/avatar tests are implementation evidence; “E2E bugs” in commit titles means bugs discovered through testing, not necessarily an authored Playwright suite. The exhaustive index retains individual issue IDs/changed paths. **Reuse:** “I fixed shared UI/browser regressions and accessibility details, including theme fallbacks, focus and navigation state.” **Keywords:** troubleshooting, accessibility, cross-browser, i18n, React, polish. **Avoid:** blanket compliance, a defect-reduction metric or equating every style change with architecture/performance leadership.

### CORE-034 — Company preferences, locale/currency and content-format controls

**Evidence:** authored Git/PRODUCTION-context; high attribution. **Status:** 2024–2025 improvements; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

`31ed0693e191803c767d68d787f9b23cd79fda09` uses `Intl.NumberFormat`-derived currency symbols for company locale configuration instead of hardcoded symbols, including an explicit currency-code argument for dropdown previews; `22fe9707917ae222e1f8861060aa1af000adfd2b` fixes currency mapping follow-ups. `ae89e3f558656340c15637ef97b37c98959c00c1` / `106c0eab4602bf08619301a6770ab0ccce0d7ee5` add/configure Dayjs language mappings and centralize supported translation-language lists so locale rendering follows user/company settings.

Content-format work handles Word paste/default style application and validates custom line spacing. `5109508648a3833be0090957a7d61daf53695710` replaces fixed line-height selection with free-form Autocomplete/input state, valid numeric/default checks, error helper feedback and disabled save when invalid; follow-ups preserve decimal precision and reduce save flicker. Glossary fixes trim/deduplicate edited values and correct missing field/selection behavior (`5112b21f23085b11f815009d759528e8a08a656a`, `6c59a59540461f7545c3782a931e3fd9cc01543b`, `204fbe9fd0622649733d77d251466a17fb35b2c9`). Announcement timezone/create/style-dialog fixes are separate application behavior, not translation-engine ownership.

**Paths/tests:** CurrencyConfigUtils, DayjsUtils/GeneralUtils, company locale-preference/company-features renderers, TranslateGlossaries, TinyMCECustomStyles and announcement utils. No measured translation accuracy/locale performance or comprehensive suite result. **Reuse:** “I improved locale/currency presentation and company content-format controls with validation, precision and glossary fixes.” **Keywords:** internationalization, localization, Intl, date/time, form validation, content formatting. **Avoid:** translation backend authorship or promoting DeepL POC (CORE-036) into a live capability.

### CORE-035 — AI response-header filters and linked-company criteria

**Evidence:** authored Git/PRODUCTION-context + PRs; high for frontend changes, collaborative backend. **Status:** June 2025 response-header phase; July 2026 linked-company phase merged; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

`e790ace2f9ab6f5bc14bfaa73f6e922abd7daf4c` / RES-147812 extends Ask/AI filter state and request payloads to include response headers conditionally under the feature flag. Utilities refine selections, map displayed header names and omit disallowed/disabled filter data; re-ask/prompt rendering is adjusted when filters are applied. `c131a6ae5f4bb644b0a71df1f27a5b72e819f43c` / `fa5e1f81a1a03a8aa0b7cddb2a59a5d7a30965b9` fixes response-header behavior in Ask utilities/dataset UI. This is frontend selection/payload integration; Java MongoDB/Solr synchronization and embedding/RAG internals remain server scope.

`ee20e4207f5947fc49cd08dd704af3f2ad478d31` and follow-ups add per-linked-company tag/collection criteria in AI Draft/Ask. `LinkedCompanyAiFilters` loads partner-company details and filter options, guards feature/project readiness, uses cancellation to avoid stale effect updates, maps company IDs/names/options and exposes typed criteria. Changes update only that company's entry, mark filters/reset state and honor disabled/empty/loading conditions. Existing partner/filter services and backend matching are dependencies. PR-6760/6779/6852 include **Ranjith's backend commit** `3d267aa92c829ca066861cd77b9d65522566d997`, sometimes committed/cherry-picked by me; that is not my backend authorship. PR-6727 is closed unmerged; other promotion PRs merged.

**Recovered historical variants:** `68950d12aa6b0a8da209b99b82b80043831ee196` only reorders an import in ResponsiveAIUtils despite its feature title; it is maintenance, not another filter implementation. `5b48ce617447349f5d23b6f39d34bea8e47a741d` moves linked-company criteria mapping earlier in applyFilters, guarded by linked_companies && agentic_ask and adding only nonempty mapped criteria. Both are July 17 unreachable variants outside refs/reflogs, with no established merge/release. Their differing patches are preserved without duplicating this feature.

**Paths/tests:** Ask filter components/context/actions, AiDatasetUtils, `components/dialogModels/RespondProject/LinkedCompanyAiFilters*`, bulkAiService/partner-service integration. No independently rerun model/search quality or endpoint tests. **Reuse:** “I integrated response-header and per-company AI search criteria into React filter state and request flows.” **Keywords:** AI UI, filters, TypeScript contracts, API integration, async effects. **Avoid:** embedding/search algorithm ownership, backend authorship from committer identity or search-accuracy metrics.

### CORE-036 — Exploratory voice-search and DeepL no-translate UI

**Evidence:** PROTOTYPE/POC, authored Git; high for code, product adoption UNKNOWN. **Status:** 2025 exploratory branches/historical experiments; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

`83a2d02bee18067ed75e9a3f57f7ad0eb6243493` and `9c0b0c281a1769f9b5c856e6d92f5875665869a4` explore voice-driven organization search through speech-input state/dependencies and search-result integration. `c8500430e308b4f57bf17fb612680e48c777051a` explicitly labels a DeepL “no translate” POC, adding translate-engine/glossary UI/options and props. These are distinct experiments, not verified broad production rollouts or one of the 11 ShadCN prototypes in other context.

**Paths/tests:** org search results/props and translate-engine/glossary configuration. Browser support, speech service behavior, privacy, provider execution, test results and rollout are unknown. **Reuse:** “I explored voice-driven settings search and no-translate configuration in frontend prototypes.” **Keywords:** prototyping, speech UI, translation configuration, experimentation. **Avoid:** shipped voice search, live DeepL behavior or combining prototype counts across contexts.

### CORE-037 — Project/template/document/e-sign workflows and small troubleshooting changes

**Evidence:** authored Git/PRODUCTION-context; high for exact changes; feature ownership bounded. **Status:** 2023–2024 historical fixes and UI improvements; deployment UNKNOWN.

**Attribution confidence:** HIGH for listed authored changes; surrounding architecture and outcomes bounded by the record. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

Early internship work includes document-type filter maps, template-only exclusion of author/reviewer/source properties, removal of inappropriate guest-email team options, template duplication/processing banners and additional metadata handling (`891451a5c5a63f93a248af47af4efcbe8d59bd20`, `65b77ecee31bbf6ee22fb884bb7c768095ec6b6e`, `216b7c194a63b261de2dbe723cc2352eea507de6`, `f1456d6716aa3895d657908d7ea597792bfd311a`). Numerous “no message” commits were traced to their actual changed functions/paths rather than discarded; they are in the index with structural context. E-sign lifecycle/review/bulk-recipient UI and expiration sorting (`965d4776635f7678bf0181ac36125026791b3a68`, `5e9dc3cd053304087ac8f13304c8d294269afab8`) are follow-up contributions, not proof of sole e-sign implementation.

Project/template filter/export/errorLogger fixes (`60844f69b824816f3879a3ecd446951a35eb96a8`, `059afb49df7a1cac19eca59ca120dd5c76460327`), proposal basic-info changes, request/intake/profile corrections and MS Teams project-back navigation (`648f785274601dc8fb271aad6b365f943043338d`) preserve narrow boundaries. Pending notification queue UI (`39b92a15b36f070069a3bd575a87f102068a8fb0`, `b953c53b727cbef2ef03f92c6fd88b8008964e3a`) changes display/queue interaction; it does not establish SSE transport. Legacy Angular organization grid row-height/reorder and NPS-note clearing fixes show maintenance of the old app during modernization. Debugging/log suppression and conflict-only changes remain classified as such, with no invented feature or metric.

**Paths/tests:** project/template/import/export/e-sign/intake/request/proposal/profile components, legacy controllers and ErrorLogging utilities. Some changed historical tests exist; no audit test run or full feature certification. **Reuse:** “I delivered focused document/project workflow fixes while maintaining legacy and modern application paths.” **Keywords:** application maintenance, troubleshooting, document workflows, validation, cross-framework migration. **Avoid:** attributing whole modules from a few bug fixes or translating pending-mail UI into SSE ownership.

### CORE-038 — Dependency maintenance, generated artifacts, merge transport and review response

**Evidence:** TOOLING / collaborative transport, exact Git/PR metadata. **Status:** historical/current maintenance; product deployment UNKNOWN.

**Attribution confidence:** HIGH for author/transport metadata; UNKNOWN for original authorship of imported/generated artifacts. **Inspection:** G-20261003 (repository/ref/HEAD/date above).

Dependency bumps, lockfile churn, generated editor bundles/fonts/graphs, imported upstream skills and merge/stash snapshots are retained as inventory evidence but not counted as original product features. Token/registry updates (PR-8066/8068) are recorded only as credential-distribution maintenance; values/raw config are intentionally excluded. Package/editor peer/version fixes have narrow scope, not library authorship.

Example maintenance anchors: `19004ff4a16f54a16c05d7132d2a5dcf6cc3ac8b` (registry credential distribution; metadata only) and `6262df958c4128ee00c918b32ff9ba451453f942` (editor package/peer update). These identify exactly which changes support this record without retaining sensitive configuration.

Of 2,358 author-matched commits, 1,136 are actual multi-parent merges. The 1,222 non-merge inventory also includes three merge-titled single-parent transports and two stash companion records; author name does not prove their imported code is mine. Twenty committer-only records have other authors and are excluded from authored implementation totals. PRs such as 8754 sync (143 returned commits) and 7826 (532) contain many collaborators' changes; the full PR diff is not my implementation. Akarshan's Sonar, Gowrishankar's monorepo, Ranjith's linked-company backend and other founding architecture remain explicitly attributed.

The read-only unreachable-object audit adds 53 exact-identity captures outside refs and reflogs: three ordinary July commits and 50 stash/index/untracked snapshots from July–September 2026. Their metadata and non-secret diff structure are retained in a separate register. Broad synchronization/conflict snapshots can contain hundreds of collaborators' changes; capture ownership does not transfer implementation authorship. The extra snapshots are not included in the 1,222 ref-reachable non-merge count or the 1,180 deduplicated groups and do not imply shipped work. Git fsck returned no diagnostics in this connectivity-only audit; this is not a content-integrity or release certification.

Specific review-response evidence: PR-8869 lockfile restoration/formatting cleanup, PR-8694 whitespace feedback and PR-4476 my exploratory i18n comment. These support collaboration/review response, not a quantified review program, formal review ownership or mentoring. **Reuse:** “I maintained application tooling/dependencies and responded to integration review while keeping changes scoped.” **Keywords:** collaboration, code review response, maintenance, dependency management. **Avoid:** counting merges/cherry-picks/generated files as independent delivered features or claiming others' authored code.

## Build benchmark provenance register

All additional numbers below are **PR-9515 description reports, not independently reproduced measurements**. PR links/recorded checks were inspected; attached screenshots/dashboard were not independently validated. Baseline conditions vary. Canonical F/S cold-build wording remains authoritative for reuse.

| Measurement | Recorded before → after | Conditions/limitations |
|---|---|---|
| Full cold monorepo, canonical | 10–14+ min →101.45 sec (~88%) | F/S/P. Preserve range/approximate percentage. |
| Full cold monorepo, PR detailed | 720.0 sec →101.45 sec; 85.9%, 7.1× | PR detail vs PR summary 15+ min/~88%/8.5× is CONFLICT. PR describes 8-vCPU/16-GB CI and macOS experiments; exact run series unavailable. |
| Single rfpio cold | 122.64 →90.73 sec total; core compile 80.18 sec | Different scope from full monorepo; PR-reported 26% total reduction. |
| Incremental source edit | 122.64 →9.60 sec total /6.03 Webpack | Cache-assisted source edit, not cold build; PR reports 92.2% total reduction. |
| Turbo replay after test/doc edits | 263 ms, FULL TURBO | Cache replay, not compilation. No inferred user latency. |
| Peak RSS | >22 GB / c=6 exit137 →4.16 GB full two-wave | Different concurrency/cache conditions; “permanent fix” PR rhetoric is not a guarantee. Single-app 6.01→3.63 GB is separately reported. |
| Output | 208→59 MB; common vendor 12.3→5.84 MiB; <5KB chunks 374→183 | 71.6%, 52.5%, 51.1% respectively, author-reported build artifacts, not package publication or network transfer. |
| Cache transport | 10,000+ loose files →one tarball; ~78% payload cut, 2–4s restore /3–5s upload | Companion S3/pipeline figures are PR-author reports. U2 confirms rollout; the inspected post-deploy Job1/Job2/Sonar checklist was unchecked, and its results are not independently verified. Rollout confirmation does not resolve these measurement/check details. |

## Conflicts, cross-context reconciliation and claims to reserve

1. **Build baseline:** F/S/P canonical 10–14+ minutes/~88%; PR-9515 15+ minutes and 720.0 seconds/85.9% coexist. No canonical metric changed. Confirm which command/run should support future precise variants.
2. **Testing scope:** application Vitest/MSW/RTL/Playwright is now Git-verified. U2 explicitly resolves the 174→76-second metric and Storybook/Chromatic/interaction scope as design-system, not rfp-app. Update future interpretations of C0's testing unknowns, not the metric or other files.
3. **Redux vs Zustand:** Redux/Easy Peasy implementation is verified here. AgentStore is Easy Peasy. Zustand/StyleX remain skills-only; Bun/Oxlint/Oxfmt unknown. Do not silently promote them in personal/design contexts.
4. **Architecture dates:** visible shared-shell work starts in 2023 and evolves through 2024, earlier than the F/S Sep2024–Sep2025 architecture bullet placement. Preserve role dates; clarify early implementation vs later leadership/reuse phase. Original three-MFE mapping remains unknown while founding configs show collaborators.
5. **Migration periods:** internship two + later four remain canonical; 2024 Billing 2.0 is distinct. Missing founding commits do not remove approved earlier work or identify the four by inference.
6. **Agent dates:** S places ADK/custom React platform in Sep2024–Sep2025; attributed UI phases continue Sep–Nov2025. Preserve that timeline distinction until clarified, without rewriting personal.md/server.md.
7. **Hackathon dates/status:** June narrative versus July 2026 code; prototype mock flag versus approved later production evolution. Keep demo, follow-up and production phases distinct; Chorus/Jira evidence cannot be supplied by unrelated mocked file providers.
8. **SSE/ELK/Search gaps:** preserve SSE60% and ELK30% MTTR with F/S provenance. Current other-author agent SSE and Java Solr work must not fill missing frontend ownership/implementation details. Document Library faceted-search UI implementation is now USER-CONFIRMED (U2); exact paths, APIs, tests and ownership detail remain unknown.
9. **Merge vs release:** development merges/current ancestry, the originally open staging build PR and removed/unmerged prototypes have separate status. U2 confirms CORE-005 build/S3 rollout, without establishing a new PR merge observation or deployment of other initiatives. Do not silently convert all repository work to deployed product outcomes.

Only core-app.md was updated. These reconciliation notes are proposals for future context maintenance; personal.md, server.md, design-system contexts, base PDFs, Rezi, skills and workflows were left unchanged.

## Missing facts — precise manual questions

U2 requests items 1–7 and 11–14 be left as-is for the user to handle; they are preserved below, not newly requested in this follow-up. Items 8–10 are narrowed or resolved using the specific confirmations. Do not ask again whether Document Library UI was implemented, whether the build/S3 rollout happened, or whether the design-system metric belongs to this repository.

1. **Internship origins:** Which Angular controllers/routes and React components did you migrate for Response Template and Billings? Can you identify branch names/SHAs, the approximate implementation months and your portion versus collaborators?
2. **Four later modules/45%:** What are the four module names and their originating branches/SHAs? Which pages and before/after timings produced 45%, using which tool, browser/cache conditions and measurement window?
3. **Two micro-frontends/5+ apps:** Which two packages count toward your personal viewer-reuse scope, and which five-plus applications shared your shell? What did you implement for Trust Center/Builder viewer reuse, and which pieces were initially built by others? Which commits show your viewer interfaces/host-remote integration?
4. **Architecture timeline:** How do 2023–2024 shell/framework implementations relate to the Sep2024–Sep2025 leadership/reuse phase in the resume? What responsibilities did “led” cover?
5. **SSE60%:** In which repo/branch/SHAs is your notification stream? What endpoint/events/store updates/reconnection/error/cleanup logic and tests did you implement, and how was the polling reduction measured?
6. **Authentication/guest sessions:** Which SHAs show your original responsive sign-in/reset rewrite and Redis/OTP work? What was your frontend/backend boundary, and what expiry/resend/session/error behavior did you implement?
7. **ELK30% MTTR:** Which incidents/root causes and ELK queries or dashboards were involved? What baseline/final resolution times, incident population/window and your triage/fix/release responsibilities support 30%?
8. **Document Library/Solr:** Personal faceted-search UI implementation is confirmed (U2). Remaining details: which paths/SHAs, facet/filter payloads, API/error states, tests, implementation period and collaborator boundaries apply? Backend indexing ownership is not inferred.
9. **Build rollout/metrics:** Rollout of the build changes and companion S3 pipeline is confirmed (U2). The canonical baseline question remains unresolved: which command/machine/cache conditions reconcile 10–14+, 15+ and 720s? Exact rollout environment/date/release and post-deploy checks were not supplied; no new PR merge observation is recorded.
10. **Testing174→76 — scope resolved:** U2 confirms the metric and Storybook/Chromatic/interaction implementations are in design-system, not this repository. Detailed suite/command/measurement evidence belongs in the design-system context; no further core-app scope confirmation is needed.
11. **Agent/ADK ownership:** What platform work happened before Sep2025 versus the Sep–Nov UI phases? Which ADK/backend parts did you implement, what did teammates own, and what was released?
12. **Hackathon evolution:** Was the July code follow-up to the June demo? Which five-plus services were live in the demo, which later reached production, and when/where did mock flags get removed and live execution get tested?
13. **Reserve technologies/runtime branch:** Where did you implement Zustand, StyleX, Bun, Oxlint or Oxfmt (repo/branch/SHAs and purpose)? Was ux-opt runtime work merged/released elsewhere, and are there measured loading/bundle outcomes?
14. **Review/enablement:** What review standards, docs/live-demo sessions and adoption outcomes were specifically your work? Confirm the 50+ figure denotes enabled/trained engineers, and supply any factual examples without converting it to mentoring.

## Updated resume-ready evidence table

Wording is factual reusable material, not a request to include every row. Git-only qualitative contributions need no invented metric. “Verified” means the stated provenance supports the bounded claim, not production deployment.

| IDs | Reusable factual material | Metric/provenance | JD keywords and limits |
|---|---|---|---|
| 001 | Implemented shared React layouts/header/navigation with product/design/backend collaboration | 5+ apps F/S; Git mechanisms verified | architecture, responsive UI; collaborative scope |
| 002 | Built two React micro-frontends enabling Trust Center/Builder viewer reuse; repaired federation i18n initialization | Two per current user-edited Frontend BASE; fix PR-8784 | Module Federation; original mapping unknown |
| 003/004 | Migrated two internship modules and four additional later modules, using Redux and Easy Peasy for the later work | 2+4; later45% F/S; state management user-confirmed | AngularJS to React/TypeScript; preserve periods/measurement gap |
| 005 | Optimized full-monorepo cold builds with concurrency, disk cache and compiler tuning | 10–14+min→101.45s/~88% F/S | Webpack, Turbo, performance; rollout USER-CONFIRMED (U2); original PR status retained |
| 006 | Established Vitest/RTL/MSW scoped tests and fixture-backed Playwright smoke | ≥85% scoped policy; runtime56% is design-system F/S/U2 | test architecture; not whole-repo coverage |
| 007/011 | Implemented auth/account/security forms, REST validation/error/dirty-state flows | F/S plus Git; no new numeric result | authentication UI, SSO/MFA, APIs; backend boundary |
| 008 | Delivered SSE notifications reducing polling overhead | 60% F/S/C0 | real-time; missing implementation detail |
| 009 | Customized TinyMCE document/comment/paste/style/image/table workflows | F + Git | rich text, browser/async correctness |
| 010 | Resolved production issues through ELK/root-cause investigation | 30% MTTR F/S | observability; incident details unknown |
| 012/013/021/022 | Built enterprise administration flows, typed shared state, membership/user/role comparison UI | Git, qualitative | complex forms, permissions UX, Redux |
| 014/015/016 | Implemented connector configuration, project imports and reusable custom-field management | Git, qualitative | REST, workflows, schema-driven UI |
| 017/018/035 | Built settings search, implemented Document Library faceted-search UI, improved CCL search and integrated AI header/company criteria | Git for listed fixes/filters; U2 for Document Library facets; qualitative | search UX/filtering; no inferred backend indexing ownership |
| 019/032 | Refactored scoped discussion state and implemented lazy loading/dependency isolation | Git; 032 branch-only | React performance, code splitting; no measured % |
| 020/023/024/025/034/037 | Implemented billing/activity/support/configuration workflows and focused app fixes | Git, qualitative | enterprise UI, pagination, localization, maintenance |
| 026 | Built custom React agent-authoring/run/history/citation/canvas UI and tests | Git + S platform scope | AI interfaces; ADK/backend boundary |
| 027 | Built AI-assisted integration discovery/auth/folder UI during hackathon/prototype evolution | 5+ services F/S/P; mock-enabled branch | agents/integrations; live rollout unknown |
| 028 | Migrated consumers from full user preload to targeted hydration/discovery/metadata APIs | Git, qualitative | caching, payload optimization, API contracts |
| 029 | Integrated shared design-system themes and isolated hosted remote theme scope | Git; enablement50+ F/S/P | design systems, adoption; not package authorship |
| 030/031/038 | Built/maintained safe graph hooks, backport automation and scoped tooling changes | Git/PR; GitNexus removed | developer experience, CI, Git, collaboration |
| 033/036 | Fixed browser/accessibility/i18n details; explored voice/no-translate prototypes | Git; experiments labeledPOC | compatibility, accessibility, prototyping |
## Inspection-coverage register

**Completed coverage:** all available ref-reachable author/committer identities and author-matched history were inventoried across the full period, not only recent commits/HEAD. Every deduplicated authored record was processed for actual non-generated diff structure (paths, added/removed declarations, API strings, test/hunk metadata), then grouped into initiatives and investigated with focused diffs/historical source, current descendants, selected blame/origin checks and PR evidence. This is not a claim that every line of third-party/generated code or every collaborator's commit received manual review.

| Source/range | What was covered | Boundary/remaining gap |
|---|---|---|
| Available local refs | Non-shallow; **247,494** reachable commits across all contributors, author dates **2015-01-07–2026-09-30**; 53 local branches, 5,578 remote-tracking refs, 10 tags, six Codex refs, one stash ref | Counts are repository history, not my delivery count. No fetch; remote-tracking refs are the saved snapshot. Objects outside refs/reflogs received a separate connectivity-only audit; see supplemental row/register. No other clone or unavailable remote history was inferred. |
| My ref-reachable history | **2,358** author matches: **1,222 non-merge**, **1,136 actual multi-parent merge** commits; **2022-11-09–2026-09-30**. Twenty committer-only/other-author records separately inventoried | Exact confirmed identities, not every name match or Git config. Earliest local attributed commit is later than internship start. Merge-titled single-parent transports/stash companions are separately qualified. |
| Authored non-merge census by year | 2022:1; 2023:450; 2024:483; 2025:196; 2026:92 | Author dates, not role or deployment dates. All years included. |
| Stable patch deduplication | **1,178 unique nonempty patch IDs +2 no-patch records =1,180 groups**, with **42 repeated-patch groups**; all 1,222 SHAs retained in group/copy register | Identical patch removal avoids double-counting cherry-picks. Similar but nonidentical iterations remain separate evidence within one initiative, not new features. |
| Actual diff inventory | **9,317 non-generated path-change scans** across all 1,180 records; large initiatives received focused implementation/source reads | Binary/minified/upstream generated assets, dependency-lock bodies, credential config and captured fixture bodies are not persisted. Structural scan is not line-by-line manual verification of every patch. |
| Local reflogs supplement | **247,519** all-ref+reflog reachable commits, **25** beyond refs. **18** additional own author records:12 non-merge +6 stash-root merges; dates May–September 2026 | One substantive federation commit duplicates the published patch; stash/draft versions are not separate shipped work. Supplemental register below preserves relevant WIP and generated/draft status. |
| Unreachable-object supplement | Read-only git fsck --unreachable --no-reflogs --no-progress --connectivity-only:114 unreachable commits, of which89 are outside refs+reflogs; **53 exact own author matches**, July 12–September 30 2026 (3 ordinary commits,24 stash roots,24 index companions,2 untracked trees). All 53 non-secret tracked/untracked diff structures processed; ordinary diffs and relevant scaffold/folder variants inspected | No diagnostic errors returned. Remaining36 other-author objects are not attributed. 13,142 eligible path-change scans largely repeat deletion/sync snapshots; not unique work or added to main census. Ordinary variants remain historical; broad stash capture proves capture ownership only. |
| Current vs historical | HEAD `93e20e29670c887d47231a47255884330dd2fe33`; staging `f1ad60ecf4bd79f9ebdb3e171ff6e1197a44bf01`; development `1193a0ab9f434b9ccaf353860a8d770de14c273c`; master `16814a94f7c0923fcbb9b41b2754bd2682b5e9c5` | Ancestry tracked per group. Inclusion does not establish active lines after reverts/superseding changes, release or deployment. ux-opt explicitly separate. |
| Older architectural context | Selected 2021 login skeleton/history plus 2024–2025 other-author MFE foundations, 2026 monorepo/Sonar origins and current SSE blame | Older all-contributor history census is complete for available refs; unrelated pre-tenure engineering is not attributed/reviewed as my work. |
| GitHub authored PRs | **83** search results, all states, created **2026-03-06–2026-09-30**; **60 merged /22 closed unmerged /1 open**. Titles/bodies/states, paginated file diffs, commit lists, reviews, inline/discussion comments inspected | Search incomplete=false. Current work account found 83; S-Sanjeev and sam-zc searches found 0 in this repo. Empty descriptions stay empty; no fabricated historic metadata. |
| Large PR commit cap | PR-7826 reports532 commits; GitHub commits API returns at most250. Local exact base `00377528b974afdb2078a325234fc1144c73a971`..head `c44121cc99b983b574fc2a5295394d1400270a19` yielded all532, only5 exact author matches | Local metadata supplements missing API tail; aggregate PR code is overwhelmingly collaborative. Full file endpoint has616 entries, scoped non-secret diff scan615. |
| Additional collaboration PRs | PR-6421 (Gowrishankar monorepo) and PR-8282 (Akarshan Sonar) metadata/descriptions/commit authors/reviews inspected | **85 distinct GitHub PR records total**; these two are attribution references, not my authored contributions. Their complete per-file diffs were not fetched in the second pass; local relevant origins were inspected. |
| PR diff/review boundary | All 83 authored PRs' file patches were processed into non-secret hunk/symbol summaries; principal PR descriptions and relevant feedback examined in detail | GitHub may omit binary/large patches; omitted/generated/credential bodies intentionally excluded. Review state is snapshot evidence; attachments/screenshots/dashboard not independently validated. Four unmerged PR API merge_commit_sha values (7826/8826/8916/8923) are not present as local objects and are recorded only as API metadata, never completed merges. |
| Historical Bitbucket | Git messages retain branch/PR IDs and some titles/summaries; user confirms hosting closed | Original descriptions, reviews, linked issue bodies and historical merge UI unavailable. Never reinterpret a Bitbucket number as the same GitHub number. |
| Jira/production sources | Linked RES/DS IDs and PR references inventoried | Jira issue bodies, ELK logs, telemetry, release/deploy evidence, benchmark run logs and the companion S3 pipeline not directly retrieved. No authenticated Jira source available in this inspection. |
| F/S/P/C0/U2 | Both finalized PDFs, personal contract and original core context read as factual references; approved facts preserved. User confirmations on 2026-10-03 update Document Library ownership, build/S3 rollout and design-system test scope | No other contexts/PDFs/Rezi/skills/workflows edited. Design-system/server repos not inspected as source repos in this task. |
| Validation | Final complete file read/audited for record/source IDs, SHA resolution, duplicate coverage, PR status/ownership and canonical metrics; source working tree checked unchanged | No tests/builds/installations/checkouts/fetch/commits/push/deployment. Historical test checks explicitly author-reported. |

## Inspected GitHub PR register

All URLs below are actual inspected PRs; titles are preserved. `c` is returned commit count, `f` file endpoint count. Descriptions are summarized, not inferred when empty. Review counts include dismissed/commented history; approvals do not prove release. PR records preserve deployment evidence from the original inspection (UNKNOWN/N/A to product tooling); later U2 user confirmation of CORE-005 rollout is recorded separately above. No PR state was freshly checked or changed by that confirmation. Authored PRs can contain other authors' code. The API merge_commit_sha field may be a test merge for an unmerged PR; only the explicit MERGED state establishes a completed merge.

### PR-1271 — DS-390 feat: Lyra version upgrade and theme cleanup

- URL: [1271](https://github.com/responsive-core/rfp-app/pull/1271); author `sanjeev-s_rio`; created 2026-03-06; **CLOSED UNMERGED 2026-03-06**; base `development`; head `sam-lyra-bugfix` / `a13cac6753ef9a2dba89e86ddc111201566517e4`; API merge_commit_sha `None`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=15/15; reviews {'APPROVED': 3}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-029.

### PR-1844 — Update package.json for lyra version

- URL: [1844](https://github.com/responsive-core/rfp-app/pull/1844); author `sanjeev-s_rio`; created 2026-03-16; **MERGED 2026-03-16**; base `development`; head `sanjeev-s_rio-patch-1` / `0dae7586367b8eb0cf38ad7d030f527592295958`; API merge_commit_sha `ace06b90aa8d81f63f064c18df5d32c441cabb88`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=1/1; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-029.

### PR-3681 — Update package.json

- URL: [3681](https://github.com/responsive-core/rfp-app/pull/3681); author `sanjeev-s_rio`; created 2026-04-27; **MERGED 2026-04-27**; base `hotfix_patch`; head `lyra-bug-fix` / `2d480aa7b09b06a1f39eaeb13accdb8e9b1ed9ba`; API merge_commit_sha `666a2506945f4200aeaa17fad12e35106c927baa`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=1/1; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-038.

### PR-3707 — fix: RES-174071 Resolving conflicts on base-unscoped @layer

- URL: [3707](https://github.com/responsive-core/rfp-app/pull/3707); author `sanjeev-s_rio`; created 2026-04-28; **MERGED 2026-04-28**; base `RES-26.03.04_28_Apr_2026_Hotfix`; head `lyra-bug-fix` / `2d480aa7b09b06a1f39eaeb13accdb8e9b1ed9ba`; API merge_commit_sha `fb839ad531dbb58ba9495c9c8c4f6bd2e85ec76d`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=1/1; reviews {'APPROVED': 2}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-038.

### PR-4228 — fix: RES-175591 Update package.json for lyra latest version

- URL: [4228](https://github.com/responsive-core/rfp-app/pull/4228); author `sanjeev-s_rio`; created 2026-05-11; **MERGED 2026-05-12**; base `hotfix_patch`; head `lyra-2.1.9-bump` / `07da96fb64d0e93708388103098c07154fe9abca`; API merge_commit_sha `b3d48af3d5e6a8ab57af5b49e9f51547fa84b421`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=1/1; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-029.

### PR-4256 — fix: RES-175591 Update package.json for lyra latest version

- URL: [4256](https://github.com/responsive-core/rfp-app/pull/4256); author `sanjeev-s_rio`; created 2026-05-12; **MERGED 2026-05-12**; base `RES_26.04.05_12_May_2026_Hotfix`; head `lyra-2.1.9-bump` / `07da96fb64d0e93708388103098c07154fe9abca`; API merge_commit_sha `a8a9eb75c6e21c800129891db715f71de255e683`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=1/1; reviews {'APPROVED': 2}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-029.

### PR-4357 — Sam lyra bugfix

- URL: [4357](https://github.com/responsive-core/rfp-app/pull/4357); author `sanjeev-s_rio`; created 2026-05-13; **CLOSED UNMERGED 2026-06-15**; base `development`; head `sam-lyra-bugfix` / `1488b90dc725e7c783b368c88f2a5922f5d33655`; API merge_commit_sha `None`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=2; f=20/20; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-029.

### PR-4476 — [DON'T MERGE] DS-469: Internationalization for Lyra (Requires Lyra AI Publish)

- URL: [4476](https://github.com/responsive-core/rfp-app/pull/4476); author `sanjeev-s_rio`; created 2026-05-15; **CLOSED UNMERGED 2026-06-15**; base `development`; head `sam-lyra-i18n` / `6eb94f4faff4d96d9f906644ddfc0f82e4296148`; API merge_commit_sha `None`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=11/11; reviews {'COMMENTED': 1}; inline comments=1; discussions=0; other-author commit records=0. Related primary IDs: CORE-029.
- Inspected inline feedback: `sanjeev-s_rio` on `app_v2/src/i18n.shared.ts` — explore if this can be removed for base app_v2 app with usesuspense

### PR-5147 — Company user load details removal

- URL: [5147](https://github.com/responsive-core/rfp-app/pull/5147); author `sanjeev-s_rio`; created 2026-06-03; **CLOSED UNMERGED 2026-07-08**; base `staging`; head `company-user-load-details-removal` / `d9e73b563f2fc9f57faa4509f927fa7ea3ec50c1`; API merge_commit_sha `None`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=5; f=194/194; reviews ; inline comments=0; discussions=0; other-author commit records=1; collaborators Hari Hara Sudan. Related primary IDs: CORE-028.

### PR-6325 — feat: RES-179299 Git Nexus Setup

- URL: [6325](https://github.com/responsive-core/rfp-app/pull/6325); author `sanjeev-s_rio`; created 2026-07-07; **CLOSED UNMERGED 2026-07-08**; base `development`; head `k-graph` / `9ccfe2363c442bd22ff3231a4800fd7174d04aa1`; API merge_commit_sha `None`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=2; f=64/64; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-030.

### PR-6358 — feat: RES-179299 Git Nexus Setup

- URL: [6358](https://github.com/responsive-core/rfp-app/pull/6358); author `sanjeev-s_rio`; created 2026-07-08; **MERGED 2026-07-09**; base `development`; head `k-graph-sync-dev` / `4d1fe9e1b75acd2809132c77a10202244f09c436`; API merge_commit_sha `12e81605f0a8daea4ba55705fb76762355ff042f`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=4; f=92/92; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-030.

### PR-6418 — feat: RES-179299 Lyra Peer dependency fix

- URL: [6418](https://github.com/responsive-core/rfp-app/pull/6418); author `sanjeev-s_rio`; created 2026-07-09; **MERGED 2026-07-09**; base `development`; head `k-graph-sync-dev` / `c53d85c7f4bc7d9e2f70297b051ade793f29b6cc`; API merge_commit_sha `b60053f71f26b5be32ed4b7e803b49fb28c52918`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=2/2; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-029.

### PR-6727 — Res 182294 linked company filters

- URL: [6727](https://github.com/responsive-core/rfp-app/pull/6727); author `sanjeev-s_rio`; created 2026-07-16; **CLOSED UNMERGED 2026-07-22**; base `development`; head `RES-182294-linked-company-filters` / `82b8bfb15a89ea4bbcd0d68dad58ba317bba9480`; API merge_commit_sha `None`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=3; f=18/18; reviews ; inline comments=0; discussions=0; other-author commit records=1; collaborators Ranjith R. Related primary IDs: CORE-035.

### PR-6756 — Master

- URL: [6756](https://github.com/responsive-core/rfp-app/pull/6756); author `sanjeev-s_rio`; created 2026-07-16; **CLOSED UNMERGED 2026-07-16**; base `development`; head `master` / `5af4b8f508d80929f844f4d101bfe3453f29cb57`; API merge_commit_sha `None`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=13; f=88/88; reviews ; inline comments=0; discussions=0; other-author commit records=13; collaborators IN000542-PRAVEE\praveenkumar.selvam_, Tamilselvan Kandasamy, Gobinath N, Mukesh Kumar Pathak, Gowthaman R, sourabh, Sathish Kumar V, DineshKumar N, Gowrishankar S. Related primary IDs: transport/dependency context; no independent feature attribution.

### PR-6760 — feat: RES-182292 - AI Linked Company Filters

- URL: [6760](https://github.com/responsive-core/rfp-app/pull/6760); author `sanjeev-s_rio`; created 2026-07-16; **MERGED 2026-07-17**; base `development`; head `RES-182294-linked-company-filters-stg` / `ca96197289a7519721fda45e39d06da9e889c02e`; API merge_commit_sha `82785305b7b459c4e0b8110e91230fb4727bd47a`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=4; f=20/20; reviews ; inline comments=0; discussions=0; other-author commit records=1; collaborators Ranjith R. Related primary IDs: CORE-035.

### PR-6779 — feat: RES-182292 - AI Linked Company Filters - dev sync

- URL: [6779](https://github.com/responsive-core/rfp-app/pull/6779); author `sanjeev-s_rio`; created 2026-07-17; **MERGED 2026-07-17**; base `development`; head `linked-company-filters` / `148761f8b0c2f8f44c545e4fdeb6baa509d812c4`; API merge_commit_sha `82785305b7b459c4e0b8110e91230fb4727bd47a`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=5; f=20/20; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=1; collaborators Ranjith R. Related primary IDs: CORE-035.

### PR-6852 — Res 182294 linked company filters stg

- URL: [6852](https://github.com/responsive-core/rfp-app/pull/6852); author `sanjeev-s_rio`; created 2026-07-20; **MERGED 2026-07-21**; base `staging`; head `RES-182294-linked-company-filters-stg` / `31b6a87557bbc84930af69ce9822bd44e9318a9d`; API merge_commit_sha `d4f6d420e960406fe836c1e94fd85f215c70731a`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=9; f=21/21; reviews {'APPROVED': 2}; inline comments=0; discussions=0; other-author commit records=5; collaborators Ranjith R. Related primary IDs: CORE-035.

### PR-7005 — feat: RES-179299 Add GitNexus configuration and setup scripts

- URL: [7005](https://github.com/responsive-core/rfp-app/pull/7005); author `sanjeev-s_rio`; created 2026-07-23; **MERGED 2026-07-23**; base `monorepo_v2`; head `nexus-monorepo` / `816b3337a6dbe0b93f42b79c14c74281b105ceaf`; API merge_commit_sha `44d83932e91ec78e95a1b630dcdf518227ac2b2b`.
- Description summary: Opt-in GitNexus init/sync/background hooks; safe locks/path gating/stale recovery; Windows runner; helper tests and author-reported screenshot examples.
- Evidence/ownership: c=2; f=26/26; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-030.

### PR-7014 — feat: RES-179299 Add GitNexus configuration and setup scripts

- URL: [7014](https://github.com/responsive-core/rfp-app/pull/7014); author `sanjeev-s_rio`; created 2026-07-23; **MERGED 2026-07-23**; base `monorepo_v2`; head `nexus-monorepo` / `f96d54c85c5f4ec5f0f3e288d2ec5f8c8a64c64d`; API merge_commit_sha `c962052221875a79b1141c0cf6e06f1f82070fce`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=4/4; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-030.

### PR-7019 — feat: RES-179299 Turbo Config updates

- URL: [7019](https://github.com/responsive-core/rfp-app/pull/7019); author `sanjeev-s_rio`; created 2026-07-23; **MERGED 2026-07-23**; base `staging`; head `nexus-monorepo` / `2d042993b0efcf012e3d55c19bad1fa06da392ae`; API merge_commit_sha `e744c718d174dd60dd64a0e24c4c42a8f938237d`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=4; f=5/5; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=1; collaborators Gowrishankar S. Related primary IDs: CORE-030.

### PR-7411 — Sam company user load details removal

- URL: [7411](https://github.com/responsive-core/rfp-app/pull/7411); author `sanjeev-s_rio`; created 2026-08-05; **MERGED 2026-08-06**; base `company-user-load-details-removal`; head `sam-company-user-load-details-removal` / `5338c74b9d88e611fa7b54aac40f54acb8fb3d63`; API merge_commit_sha `a809654f2a63a8f0b8f9f894220b53169b875950`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=3; f=67/67; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-028.

### PR-7512 — feat: userList revamp ActiveUsers revamp - RES-177198

- URL: [7512](https://github.com/responsive-core/rfp-app/pull/7512); author `sanjeev-s_rio`; created 2026-08-07; **MERGED 2026-08-07**; base `company-user-load-details-removal`; head `sam-company-user-load-details-removal` / `5c050ab4d43bf170c29cc14929b2d1c5d4495b4c`; API merge_commit_sha `f951929575b2a7f9ec1a34fa6352e15c2699cb9d`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=67/67; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-028.

### PR-7700 — feat: userList rewamp OTHER METHODS AUG11 - RES-177198

- URL: [7700](https://github.com/responsive-core/rfp-app/pull/7700); author `sanjeev-s_rio`; created 2026-08-12; **MERGED 2026-08-12**; base `akarshanNEW-company-user-load-details-removal`; head `sam-company-user-load-details-removal` / `036f8107d20976605d889c4a0106a5a21debf987`; API merge_commit_sha `9d70b6918b65bf50451e38eadd88689e64f7886c`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=20/20; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-028.

### PR-7706 — Sam company user load details removal

- URL: [7706](https://github.com/responsive-core/rfp-app/pull/7706); author `sanjeev-s_rio`; created 2026-08-12; **MERGED 2026-08-12**; base `akarshanNEW-company-user-load-details-removal`; head `sam-company-user-load-details-removal` / `1e68f27264e645078d7a3f33d8442e0ad78df332`; API merge_commit_sha `79339339d653914f19743572b0a2f43c207fbc56`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=3; f=1/1; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-028.

### PR-7708 — Company user load details removal

- URL: [7708](https://github.com/responsive-core/rfp-app/pull/7708); author `sanjeev-s_rio`; created 2026-08-12; **MERGED 2026-08-12**; base `clone-company-user-load-details-removal`; head `company-user-load-details-removal` / `79339339d653914f19743572b0a2f43c207fbc56`; API merge_commit_sha `8d92ea0db19131336c2220dfae35472dde0a5476`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=19; f=369/369; reviews ; inline comments=0; discussions=0; other-author commit records=11; collaborators Akarshan S. Related primary IDs: CORE-028.

### PR-7817 — fix: ULD-14-08-2026 mention display, audit edit, and content search report

- URL: [7817](https://github.com/responsive-core/rfp-app/pull/7817); author `sanjeev-s_rio`; created 2026-08-14; **MERGED 2026-08-20**; base `development`; head `company-user-load-details-dev` / `5a1ab5ec857cd3e289b6611ec294c54887414411`; API merge_commit_sha `d8aa75568bd5de1719515ed00069ccbeed2d3611`.
- Description summary: ULD regressions: duplicate-answer edit access, project mention endpoint mapping/team dedupe, display/cache fixes and content-search-report hook crash; Jira bodies not retrieved.
- Evidence/ownership: c=14; f=21/21; reviews {'DISMISSED': 6, 'APPROVED': 8}; inline comments=0; discussions=0; other-author commit records=4; collaborators Akarshan S. Related primary IDs: CORE-026, CORE-028.

### PR-7826 — Sam company user load details removal

- URL: [7826](https://github.com/responsive-core/rfp-app/pull/7826); author `sanjeev-s_rio`; created 2026-08-14; **CLOSED UNMERGED 2026-08-14**; base `company-user-load-details-removal`; head `sam-company-user-load-details-removal` / `c44121cc99b983b574fc2a5295394d1400270a19`; API merge_commit_sha `08133e1ee62e4bfddd194b7091630982c602d8a5`.
- Description summary: ULD regressions: duplicate-answer edit access, project mention endpoint mapping/team dedupe, display/cache fixes and content-search-report hook crash; Jira bodies not retrieved. Closed/unmerged variant: no successful merge inferred.
- API-only object boundary: merge_commit_sha is absent from available local objects; PR is closed unmerged. No completed merge or attributable implementation is inferred from that field.
- Evidence/ownership: c=250 (API cap;532 verified via local base..head); f=616/616; reviews ; inline comments=0; discussions=0; other-author commit records=247; collaborators Gowrishankar S, Frinozil Xavier, Kaliraj Balakrishnan, Siranjivi J, Soundarakumar Ponnusami, Ramya Ganesh, sathishkumarm-rio, Hari Hara Sudan, IN000542-PRAVEE\praveenkumar.selvam_, Subash_RFPIO, Tamilselvan Kandasamy, SRIMATHI RADHAKRISHNAN, DineshKumar N, yerranagu Jawahar reddy, Keerthana S, Yogesh A, Sathish Kumar V, Gunalan P, Navaneethan C, Uttam Gupta S, RamKumar, Yerranagu Jawahar Reddy, Kalaiyarasan A, Pracheth M H, Santhiya Thangavel, Lavanyaa Deivasigamani, Pavithra Devi, pavithravelusamy, Ranjith R, RANJITH R, Nivedha Viswamani, Preethi singaram, Mehavarthini K, Gobinath N, Megapathi R, Akash A, Stefy Grace P, Sownther, Dharunkumar Rangarajan, Sownther M, abarnaduraisamy. Related primary IDs: CORE-028.

### PR-7830 — fix: ULD-14-08-2026 mention display, audit edit, and content search r…

- URL: [7830](https://github.com/responsive-core/rfp-app/pull/7830); author `sanjeev-s_rio`; created 2026-08-14; **MERGED 2026-08-14**; base `company-user-load-details-removal`; head `ULD-14-08-2026` / `3af64d1119634d68e3dd69e78b034e8a05a61516`; API merge_commit_sha `3903a413d682c54d4f713f8a729dfbd0fb5cfc32`.
- Description summary: …eport
- Evidence/ownership: c=1; f=6/6; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-028.

### PR-7831 — fix: ULD-14-08-2026 mention display, audit edit, and content search report

- URL: [7831](https://github.com/responsive-core/rfp-app/pull/7831); author `sanjeev-s_rio`; created 2026-08-14; **MERGED 2026-08-14**; base `company-user-load-details-dev`; head `company-user-load-details-removal` / `3903a413d682c54d4f713f8a729dfbd0fb5cfc32`; API merge_commit_sha `21f6f8e1d9133e0627b04d81296bebd291131b74`.
- Description summary: ULD regressions: duplicate-answer edit access, project mention endpoint mapping/team dedupe, display/cache fixes and content-search-report hook crash; Jira bodies not retrieved.
- Evidence/ownership: c=2; f=6/6; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-028.

### PR-7896 — fix: ULD-14-08-2026 mention display, audit edit, and content search r…

- URL: [7896](https://github.com/responsive-core/rfp-app/pull/7896); author `sanjeev-s_rio`; created 2026-08-17; **MERGED 2026-08-17**; base `company-user-load-details-removal`; head `ULD-14-08-2026` / `f6020cbfebb59cd8ff5a8b6e1da0835175704005`; API merge_commit_sha `4021bba04dcaa6e451752b54c86120a117c8ec42`.
- Description summary: ULD regressions: duplicate-answer edit access, project mention endpoint mapping/team dedupe, display/cache fixes and content-search-report hook crash; Jira bodies not retrieved.
- Evidence/ownership: c=1; f=11/11; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-028.

### PR-7897 — Company user load details removal

- URL: [7897](https://github.com/responsive-core/rfp-app/pull/7897); author `sanjeev-s_rio`; created 2026-08-17; **MERGED 2026-08-17**; base `company-user-load-details-dev`; head `company-user-load-details-removal` / `4021bba04dcaa6e451752b54c86120a117c8ec42`; API merge_commit_sha `b1c0bac9896753019dc791041614a86feda8dcf8`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=2; f=11/11; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-028.

### PR-7900 — fix: enhance AgentRunHistoryTable with user cache integration for imp…

- URL: [7900](https://github.com/responsive-core/rfp-app/pull/7900); author `sanjeev-s_rio`; created 2026-08-17; **MERGED 2026-08-17**; base `company-user-load-details-removal`; head `ULD-14-08-2026` / `c8030fa1890fde21efdfc03d22ec35b091164f77`; API merge_commit_sha `3d2a843628a999d0f1d438445be7b136fb451412`.
- Description summary: …roved display and performance
- Evidence/ownership: c=1; f=1/1; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-028.

### PR-7901 — Company user load details removal

- URL: [7901](https://github.com/responsive-core/rfp-app/pull/7901); author `sanjeev-s_rio`; created 2026-08-17; **MERGED 2026-08-17**; base `company-user-load-details-dev`; head `company-user-load-details-removal` / `3d2a843628a999d0f1d438445be7b136fb451412`; API merge_commit_sha `5a1ab5ec857cd3e289b6611ec294c54887414411`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=2; f=1/1; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-028.

### PR-8001 — feat: RES-185427 jest code removal.

- URL: [8001](https://github.com/responsive-core/rfp-app/pull/8001); author `sanjeev-s_rio`; created 2026-08-19; **CLOSED UNMERGED 2026-08-19**; base `development`; head `RES-185427-jest-removal` / `cf0c8866ebdbd357c54e7524379bfd91016c60d6`; API merge_commit_sha `None`.
- Description summary: Delete legacy Jest code/config as preparation for a new test foundation; does not establish full test migration. Closed/unmerged variant: no successful merge inferred.
- Evidence/ownership: c=3; f=777/777; reviews ; inline comments=0; discussions=0; other-author commit records=2; collaborators Akarshan S, Gowrishankar S. Related primary IDs: CORE-006.

### PR-8002 — feat: RES-185427 jest code removal

- URL: [8002](https://github.com/responsive-core/rfp-app/pull/8002); author `sanjeev-s_rio`; created 2026-08-19; **CLOSED UNMERGED 2026-08-20**; base `development`; head `RES-185427-jest-removal-staging` / `424779e0f00698574a893095145897bf0cae475f`; API merge_commit_sha `None`.
- Description summary: Delete legacy Jest code/config as preparation for a new test foundation; does not establish full test migration. Closed/unmerged variant: no successful merge inferred.
- Evidence/ownership: c=5; f=783/783; reviews ; inline comments=0; discussions=0; other-author commit records=4; collaborators Akarshan S, Gowrishankar S, Kaliraj Balakrishnan. Related primary IDs: CORE-006.

### PR-8053 — feat: RES-185427 jest code removal - dev sync

- URL: [8053](https://github.com/responsive-core/rfp-app/pull/8053); author `sanjeev-s_rio`; created 2026-08-20; **MERGED 2026-08-20**; base `development`; head `RES-185427-jest-removal-staging-dev` / `06d544af193c71d5f766028a23ec0f1fa519effb`; API merge_commit_sha `56422ff8df6e039f1ef555b50fef9a4636e79042`.
- Description summary: Delete legacy Jest code/config as preparation for a new test foundation; does not establish full test migration.
- Evidence/ownership: c=4; f=785/785; reviews {'DISMISSED': 13, 'APPROVED': 2}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-006.

### PR-8056 — feat: RES-185427 jest code removal

- URL: [8056](https://github.com/responsive-core/rfp-app/pull/8056); author `sanjeev-s_rio`; created 2026-08-20; **MERGED 2026-08-20**; base `staging`; head `RES-185427-jest-removal-staging` / `6ffd126b90c6ab69c3d57bd8e98dc173f7e2b81c`; API merge_commit_sha `46ca1baf6a75ee3e8b23c634ed84332a6135ede8`.
- Description summary: Delete legacy Jest code/config as preparation for a new test foundation; does not establish full test migration.
- Evidence/ownership: c=2; f=774/774; reviews {'APPROVED': 2}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-006.

### PR-8066 — Update .npmrc files with new authentication tokens

- URL: [8066](https://github.com/responsive-core/rfp-app/pull/8066); author `sanjeev-s_rio`; created 2026-08-20; **MERGED 2026-08-20**; base `staging`; head `jfrog-token-update` / `19004ff4a16f54a16c05d7132d2a5dcf6cc3ac8b`; API merge_commit_sha `82c2861437747e251631dae047a1c6ece7a631de`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=2/2; reviews {'DISMISSED': 3, 'APPROVED': 2}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-038.
- Credential config omitted from diff-content retention; no token values or secret-shaped bodies copied.

### PR-8068 — Jfrog token update dev

- URL: [8068](https://github.com/responsive-core/rfp-app/pull/8068); author `sanjeev-s_rio`; created 2026-08-20; **MERGED 2026-08-20**; base `development`; head `jfrog-token-update-dev` / `2595121e01622c662bec307c6e41fefcec9c6753`; API merge_commit_sha `70d04ab38114a360ac58d99e7e87caa6161dcebc`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=2; f=3/3; reviews {'APPROVED': 2}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-038.
- Credential config omitted from diff-content retention; no token values or secret-shaped bodies copied.

### PR-8279 — feat: RES-185427 Vitest/MSW/E2E testing foundation, PR validation gatecheck, and SonarQube local setup

- URL: [8279](https://github.com/responsive-core/rfp-app/pull/8279); author `sanjeev-s_rio`; created 2026-08-26; **MERGED 2026-08-27**; base `staging`; head `RES-185427-vitest-setup` / `d99694bb0091c443e8500a7df598c4befdac9bcc`; API merge_commit_sha `4d32ac00d420dd14b464f8a20e6ef39c87b4323f`.
- Description summary: Shared Vitest foundation, captured MSW fixtures/route registry, scoped ≥85% gates, target resolution, My Work/Billings suites, Playwright fixture-backed smoke, PR validation and collaborative Sonar setup; author-reported checks.
- Evidence/ownership: c=20; f=240/240; reviews {'DISMISSED': 2, 'APPROVED': 4}; inline comments=0; discussions=2; other-author commit records=12; collaborators Akarshan S. Related primary IDs: CORE-006.

### PR-8280 — Res 185427 vitest setup

- URL: [8280](https://github.com/responsive-core/rfp-app/pull/8280); author `sanjeev-s_rio`; created 2026-08-26; **CLOSED UNMERGED 2026-08-26**; base `development`; head `RES-185427-vitest-setup` / `98d99cdad269f1569ba0249facc6970d3e447abf`; API merge_commit_sha `None`.
- Description summary: Shared Vitest foundation, captured MSW fixtures/route registry, scoped ≥85% gates, target resolution, My Work/Billings suites, Playwright fixture-backed smoke, PR validation and collaborative Sonar setup; author-reported checks. Closed/unmerged variant: no successful merge inferred.
- Evidence/ownership: c=2; f=196/196; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-006.

### PR-8281 — feat: RES-185427 Vitest/MSW/E2E testing foundation, PR validation gatecheck, and SonarQube local setup

- URL: [8281](https://github.com/responsive-core/rfp-app/pull/8281); author `sanjeev-s_rio`; created 2026-08-26; **MERGED 2026-08-27**; base `development`; head `RES-185427-vitest-setup-dev-sync` / `fb06deb55a16172ea095dca47b4300e0627667c5`; API merge_commit_sha `10d1d533e6a9ee5b338564f49020f59c1b99be76`.
- Description summary: Shared Vitest foundation, captured MSW fixtures/route registry, scoped ≥85% gates, target resolution, My Work/Billings suites, Playwright fixture-backed smoke, PR validation and collaborative Sonar setup; author-reported checks.
- Evidence/ownership: c=19; f=230/230; reviews {'APPROVED': 5}; inline comments=0; discussions=0; other-author commit records=11; collaborators Akarshan S. Related primary IDs: CORE-006.

### PR-8310 — Res 185427 vitest setup

- URL: [8310](https://github.com/responsive-core/rfp-app/pull/8310); author `sanjeev-s_rio`; created 2026-08-27; **CLOSED UNMERGED 2026-08-27**; base `RES-185427-vitest-setup-dev-sync`; head `RES-185427-vitest-setup` / `af1e611ceca44ed125b3a876daa7272ed1e95a6d`; API merge_commit_sha `None`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=15; f=112/112; reviews ; inline comments=0; discussions=0; other-author commit records=11; collaborators Akarshan S. Related primary IDs: CORE-006.

### PR-8348 — Res 185427 vitest setup

- URL: [8348](https://github.com/responsive-core/rfp-app/pull/8348); author `sanjeev-s_rio`; created 2026-08-28; **CLOSED UNMERGED 2026-08-28**; base `development`; head `RES-185427-vitest-setup` / `d99694bb0091c443e8500a7df598c4befdac9bcc`; API merge_commit_sha `None`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=3; f=9/9; reviews ; inline comments=0; discussions=0; other-author commit records=1; collaborators Akarshan S. Related primary IDs: CORE-006.

### PR-8349 — Vitest dev sync

- URL: [8349](https://github.com/responsive-core/rfp-app/pull/8349); author `sanjeev-s_rio`; created 2026-08-28; **MERGED 2026-08-28**; base `development`; head `vitest-dev-sync` / `648295bdc2f146b19949a57105e295cdca5098ab`; API merge_commit_sha `4d74f8ff80e218193031928472108269358c5809`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=4; f=9/9; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=1; collaborators Akarshan S. Related primary IDs: CORE-006.

### PR-8354 — fix: backport merged PRs with single merge-commit cherry-pick and correct conflict markers

- URL: [8354](https://github.com/responsive-core/rfp-app/pull/8354); author `sanjeev-s_rio`; created 2026-08-28; **MERGED 2026-08-28**; base `staging`; head `RES-185427-vitest-setup` / `5d1922b7e357126f9743a87c948589e62f7762cb`; API merge_commit_sha `f0dc86d2dd8c0371a2740b439ad71f1a02aa1b67`.
- Description summary: Replace iterative PR-commit cherry-picks with one merged-result cherry-pick; handle existing/empty/clean/conflict cases; described broken-backport example; test plan unchecked.
- Evidence/ownership: c=1; f=1/1; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-031.

### PR-8358 — fix: backport merged PRs with single merge-commit cherry-pick and correct conflict markers

- URL: [8358](https://github.com/responsive-core/rfp-app/pull/8358); author `sanjeev-s_rio`; created 2026-08-28; **MERGED 2026-08-28**; base `staging`; head `RES-185427-vitest-setup` / `bff331a21a6d77a0f6f20801ac2e8ba095019f6e`; API merge_commit_sha `6c0ae26e556b51586e391ab4f170e295ac5d5aac`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=1/1; reviews {'APPROVED': 1}; inline comments=0; discussions=1; other-author commit records=0. Related primary IDs: CORE-031.

### PR-8662 — feat: DS-940: migrate design system packages to @responsive-lyra and enable material themes

- URL: [8662](https://github.com/responsive-core/rfp-app/pull/8662); author `sanjeev-s_rio`; created 2026-09-08; **MERGED 2026-09-09**; base `development`; head `lyra-package-update` / `b582ed87ea22a40bfcc178d0c83811c82a99d8df`; API merge_commit_sha `cf6bd5cd6a8112d152369477c4fc7ce4b59f86c5`.
- Description summary: Migrate @lyra to @responsive-lyra and newer UI/icons/AI peers/registry, rem bootstrap/material palettes/company theme, test mocks and author-reported verification.
- Evidence/ownership: c=2; f=409/409; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-029.

### PR-8665 — feat: DS-940: migrate design system packages to @responsive-lyra scope and enable material themes

- URL: [8665](https://github.com/responsive-core/rfp-app/pull/8665); author `sanjeev-s_rio`; created 2026-09-08; **CLOSED UNMERGED 2026-09-09**; base `development`; head `lyra-package-update-dev` / `6262df958c4128ee00c918b32ff9ba451453f942`; API merge_commit_sha `None`.
- Description summary: Migrate @lyra to @responsive-lyra and newer UI/icons/AI peers/registry, rem bootstrap/material palettes/company theme, test mocks and author-reported verification. Closed/unmerged variant: no successful merge inferred.
- Evidence/ownership: c=6; f=574/574; reviews {'DISMISSED': 5}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-029, CORE-038.

### PR-8694 — Lyra package update dev

- URL: [8694](https://github.com/responsive-core/rfp-app/pull/8694); author `sanjeev-s_rio`; created 2026-09-09; **MERGED 2026-09-09**; base `development`; head `lyra-package-update-dev` / `9cb120212f7e7aac8ebad9987d4b81a3363cd571`; API merge_commit_sha `cf6bd5cd6a8112d152369477c4fc7ce4b59f86c5`.
- Description summary: Migrate @lyra to @responsive-lyra and newer UI/icons/AI peers/registry, rem bootstrap/material palettes/company theme, test mocks and author-reported verification.
- Evidence/ownership: c=7; f=574/574; reviews {'APPROVED': 11, 'COMMENTED': 1}; inline comments=1; discussions=0; other-author commit records=0. Related primary IDs: CORE-029, CORE-038.
- Inspected inline feedback: `hari_rio` on `app_pursuit_intelligence/src/features/my-company/components/RiskComplianceTab.tsx` — Please check these unwanted linespaces @sanjeev-s_rio

### PR-8754 — sync

- URL: [8754](https://github.com/responsive-core/rfp-app/pull/8754); author `sanjeev-s_rio`; created 2026-09-10; **MERGED 2026-09-10**; base `lyra-package-update`; head `staging` / `d4142fdb4e3ad481d65acd5348962e6e727491aa`; API merge_commit_sha `607476382585300a796c3d80ad2e0971a373dc26`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=143; f=419/419; reviews ; inline comments=0; discussions=0; other-author commit records=143; collaborators Keerthana S, sampathkumar_rio, Sampathkumar M, Arthi G, Sownther, Akash A, Jagadeeshwaran V, Thiyagarajan Parthasarathy, Siranjivi J, Mehavarthini K, Vasukidevi P, Santhiya, Gunalan P, DineshKumar N, Dharunkumar Rangarajan, vikashvar.r, Aditya L Sriivatsalan, Tamilselvan Kandasamy, MukeshP, Hari Hara Sudan, Kalaiyarasan A, Kaliraj Balakrishnan, Gokula krishnan N, Mounika Sri, Gowrishankar S, Sathish Kumar V, Stefy Grace P, Mukesh Kumar Pathak, Pravin Udayakumar, Kumaresh R. Related primary IDs: transport/dependency context; no independent feature attribution.

### PR-8762 — feat: DS-940: migrate design system packages to @responsive-lyra scope and enable material theme

- URL: [8762](https://github.com/responsive-core/rfp-app/pull/8762); author `sanjeev-s_rio`; created 2026-09-10; **MERGED 2026-09-10**; base `staging`; head `lyra-package-update` / `f55a0bc6f6cfd94adf43b514c3153ee793aed85c`; API merge_commit_sha `d1d5b7f7d1bb35f7c05761f113252a3105757d98`.
- Description summary: Migrate @lyra to @responsive-lyra and newer UI/icons/AI peers/registry, rem bootstrap/material palettes/company theme, test mocks and author-reported verification.
- Evidence/ownership: c=5; f=452/452; reviews {'DISMISSED': 1, 'APPROVED': 10}; inline comments=0; discussions=1; other-author commit records=0. Related primary IDs: CORE-002, CORE-029.
- Discussion evidence: backport bot reported draft #8802 due to conflict; not an independently replayed workflow test.

### PR-8784 — DS-940 refactor: update webpack config for i18next and react-i18next to non-eager loading

- URL: [8784](https://github.com/responsive-core/rfp-app/pull/8784); author `sanjeev-s_rio`; created 2026-09-10; **MERGED 2026-09-10**; base `development`; head `lyra-package-update-dev` / `e32c0cdf70bfb609b258788ae66fd1069ed85cf1`; API merge_commit_sha `10e95eada04aec77934e61201ae6ece1cc2004ca`.
- Description summary: Explain hosted Lite i18n share-scope/eager initialization failure across package/Webpack versions; remove eager flags, preserve singletons, rebuild remote; author-reported hosted/standalone/dev checks.
- Evidence/ownership: c=1; f=1/1; reviews {'APPROVED': 3}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-002.

### PR-8814 — Lyra package update

- URL: [8814](https://github.com/responsive-core/rfp-app/pull/8814); author `sanjeev-s_rio`; created 2026-09-10; **MERGED 2026-09-10**; base `development`; head `lyra-package-update` / `a4eb933e34805cb120a6c69a834f1e3b84e16a99`; API merge_commit_sha `6f6b1a0182b3df9d122d90d134e4b1a5ba66a9e9`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=4; f=5/5; reviews {'APPROVED': 4}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-002.

### PR-8826 — fix: DS-940 scoped Lyra theme for hosted responsive-lite

- URL: [8826](https://github.com/responsive-core/rfp-app/pull/8826); author `sanjeev-s_rio`; created 2026-09-10; **CLOSED UNMERGED 2026-09-10**; base `staging`; head `theme-leak-fix` / `3e45e258ec5f4a048215ba4c1b5621386bd3742a`; API merge_commit_sha `cffce1d774f2fd1bd86298016d641069b737bc33`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- API-only object boundary: merge_commit_sha is absent from available local objects; PR is closed unmerged. No completed merge or attributable implementation is inferred from that field.
- Evidence/ownership: c=1; f=1/1; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-029.

### PR-8827 — fix: DS-940 scoped Lyra theme for hosted responsive-lite

- URL: [8827](https://github.com/responsive-core/rfp-app/pull/8827); author `sanjeev-s_rio`; created 2026-09-10; **MERGED 2026-09-10**; base `development`; head `theme-leak-fix` / `3e45e258ec5f4a048215ba4c1b5621386bd3742a`; API merge_commit_sha `d807799d941fa01b4994156eaba51ecb832d4e72`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=1/1; reviews {'APPROVED': 2}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-029.

### PR-8828 — fix: DS-940 scoped Lyra theme for hosted responsive-lite

- URL: [8828](https://github.com/responsive-core/rfp-app/pull/8828); author `sanjeev-s_rio`; created 2026-09-10; **MERGED 2026-09-10**; base `staging`; head `theme-leak-fix` / `3e45e258ec5f4a048215ba4c1b5621386bd3742a`; API merge_commit_sha `600bc451e67df98c8d5154c83b7c7932cbb33d6a`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=1/1; reviews {'APPROVED': 2}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-029.

### PR-8867 — chore: RES-187398 remove GitNexus integration and clean up repository artifacts

- URL: [8867](https://github.com/responsive-core/rfp-app/pull/8867); author `sanjeev-s_rio`; created 2026-09-11; **CLOSED UNMERGED 2026-09-15**; base `development`; head `gitnexus-cleanup` / `014315540f36c8b7e626eac014ddd74ba5eb1322`; API merge_commit_sha `None`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=4; f=37/37; reviews ; inline comments=0; discussions=0; other-author commit records=2; collaborators Gowrishankar S, Kaliraj Balakrishnan. Related primary IDs: CORE-030.

### PR-8869 — chore: RES-187398 remove GitNexus integration and clean up repository artifacts

- URL: [8869](https://github.com/responsive-core/rfp-app/pull/8869); author `sanjeev-s_rio`; created 2026-09-11; **MERGED 2026-09-11**; base `development`; head `gitnexus-cleanup-dev` / `598814c78bcb2ae62ce8b2d98799b39b2a4ffb48`; API merge_commit_sha `0e4aca63d2e08a8898f2d188cb9fb4745ba40c56`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=4; f=24/24; reviews {'DISMISSED': 10, 'COMMENTED': 2, 'APPROVED': 5}; inline comments=2; discussions=0; other-author commit records=0. Related primary IDs: CORE-030, CORE-037.
- Inspected inline feedback: `gowrishankar_rio` on `app_pursuit_intelligence/tools/host-smoke/package-lock.json` — app_pursuit_intelligence/tools/host-smoke/package-lock.json is different: host-smoke is not included as a workspace package, and its documentation still uses npm install. Keep it unless that standalone tool is also migrated to pnpm.
- Inspected inline feedback: `sanjeev-s_rio` on `app_pursuit_intelligence/tools/host-smoke/package-lock.json` — restored lock file

### PR-8890 — fix: RES-185427 - fix sonar coverage path and root test script

- URL: [8890](https://github.com/responsive-core/rfp-app/pull/8890); author `sanjeev-s_rio`; created 2026-09-11; **CLOSED UNMERGED 2026-09-15**; base `development`; head `sonar-fix` / `1295fc3823a4087c4e320a5915df529cd866bc96`; API merge_commit_sha `None`.
- Description summary: Correct coverage path/root test command and local Sonar composition; related validation documented. Closed/unmerged variant: no successful merge inferred.
- Evidence/ownership: c=1; f=8/8; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-006.

### PR-8916 — Gitnexus cleanup

- URL: [8916](https://github.com/responsive-core/rfp-app/pull/8916); author `sanjeev-s_rio`; created 2026-09-15; **CLOSED UNMERGED 2026-09-15**; base `staging`; head `gitnexus-cleanup` / `014315540f36c8b7e626eac014ddd74ba5eb1322`; API merge_commit_sha `e93ca7b9d2b433d230ae352f8448ffae4f035e1a`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- API-only object boundary: merge_commit_sha is absent from available local objects; PR is closed unmerged. No completed merge or attributable implementation is inferred from that field.
- Evidence/ownership: c=2; f=35/35; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-030.

### PR-8918 — fix: RES-185427 - fix sonar coverage path and root test script

- URL: [8918](https://github.com/responsive-core/rfp-app/pull/8918); author `sanjeev-s_rio`; created 2026-09-15; **MERGED 2026-09-15**; base `development`; head `sonar-fix-dev` / `a6153e4b9a830fa2ba34bf2f66250ef46550d82b`; API merge_commit_sha `399d7fc93358afcd28739e96e4d4e931bae9890e`.
- Description summary: Correct coverage path/root test command and local Sonar composition; related validation documented.
- Evidence/ownership: c=2; f=8/8; reviews {'APPROVED': 4}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-006.

### PR-8919 — chore: RES-187398 remove GitNexus integration and clean up repository artifacts

- URL: [8919](https://github.com/responsive-core/rfp-app/pull/8919); author `sanjeev-s_rio`; created 2026-09-15; **CLOSED UNMERGED 2026-09-15**; base `development`; head `gitnexus-cleanup` / `014315540f36c8b7e626eac014ddd74ba5eb1322`; API merge_commit_sha `None`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=2; f=35/35; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-030.

### PR-8921 — Gitnexus cleanup

- URL: [8921](https://github.com/responsive-core/rfp-app/pull/8921); author `sanjeev-s_rio`; created 2026-09-15; **MERGED 2026-09-15**; base `development`; head `gitnexus-cleanup-dev2` / `0381a70f53771dc0f8a08353ab2c17265b2c9ac7`; API merge_commit_sha `e656f6ab019ecdc91236b23febc16a3d40cc33cf`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=3; f=1/1; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-030.

### PR-8923 — User load fix

- URL: [8923](https://github.com/responsive-core/rfp-app/pull/8923); author `sanjeev-s_rio`; created 2026-09-15; **CLOSED UNMERGED 2026-09-15**; base `staging`; head `user-load-fix` / `f314727aa4b26afd500d3ff5cb3908ceff713d8e`; API merge_commit_sha `3cf56ae753da0bbd3a6c25381af9e3f2239d6bba`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- API-only object boundary: merge_commit_sha is absent from available local objects; PR is closed unmerged. No completed merge or attributable implementation is inferred from that field.
- Evidence/ownership: c=1; f=1/1; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-028.

### PR-8925 — feat: Add '/users/get-user-directory-meta' to skipCompanySwitchUrl in…

- URL: [8925](https://github.com/responsive-core/rfp-app/pull/8925); author `sanjeev-s_rio`; created 2026-09-15; **MERGED 2026-09-15**; base `staging`; head `user-load-fix` / `f314727aa4b26afd500d3ff5cb3908ceff713d8e`; API merge_commit_sha `a2692904240ea708b1f6d8de80b87486a5038e8e`.
- Description summary: … Axios helper
- Evidence/ownership: c=1; f=1/1; reviews {'APPROVED': 1}; inline comments=0; discussions=1; other-author commit records=0. Related primary IDs: CORE-028.

### PR-8927 — feat: Add '/users/get-user-directory-meta' to skipCompanySwitchUrl in…

- URL: [8927](https://github.com/responsive-core/rfp-app/pull/8927); author `sanjeev-s_rio`; created 2026-09-15; **MERGED 2026-09-15**; base `pre-release`; head `userload-fix` / `16f8b956a3af36d3181dab7f8a7c329b69e27501`; API merge_commit_sha `8fd0263eee6e43032dd61113b26830ed2e8e8c30`.
- Description summary: … Axios helper
- Evidence/ownership: c=1; f=1/1; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-028.

### PR-8928 — Userload fix

- URL: [8928](https://github.com/responsive-core/rfp-app/pull/8928); author `sanjeev-s_rio`; created 2026-09-15; **MERGED 2026-09-15**; base `staging`; head `userload-fix` / `16f8b956a3af36d3181dab7f8a7c329b69e27501`; API merge_commit_sha `21ba3d195000265d31aee2f0d39c899e9b894630`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=8; f=1/1; reviews {'APPROVED': 1}; inline comments=0; discussions=1; other-author commit records=7; collaborators Sampathkumar M, Yogesh A, Gowrishankar S, Gowthaman R, Kaliraj Balakrishnan. Related primary IDs: CORE-028.

### PR-8929 — chore: RES-187398 remove GitNexus integration and clean up repository

- URL: [8929](https://github.com/responsive-core/rfp-app/pull/8929); author `sanjeev-s_rio`; created 2026-09-15; **MERGED 2026-09-15**; base `staging`; head `gitnexus-cleanup` / `014315540f36c8b7e626eac014ddd74ba5eb1322`; API merge_commit_sha `8ef52036bd3f38e2d12f5a8205dac113faa60bca`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=2; f=35/35; reviews {'APPROVED': 5}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-030.

### PR-8931 — Gitnexus cleanup rebase to pre-release

- URL: [8931](https://github.com/responsive-core/rfp-app/pull/8931); author `sanjeev-s_rio`; created 2026-09-15; **MERGED 2026-09-15**; base `pre-release`; head `gitnexus-cleanup-pr` / `10e588311e34ccf7128ff0ebfe9642ca0c06a867`; API merge_commit_sha `721309823df72ec95de5f983e8e7e5c9e0ba1945`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=2; f=35/35; reviews {'APPROVED': 4}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-030.

### PR-8932 — fix: RES-185427 - fix sonar coverage path and root test script

- URL: [8932](https://github.com/responsive-core/rfp-app/pull/8932); author `sanjeev-s_rio`; created 2026-09-15; **MERGED 2026-09-15**; base `staging`; head `sonar-fix` / `081e4b811124e74691a9bb1e4728a9d4fd1499cb`; API merge_commit_sha `5d655a161422d4f88b0152ee034b38a11742795b`.
- Description summary: Correct coverage path/root test command and local Sonar composition; related validation documented.
- Evidence/ownership: c=2; f=8/8; reviews {'APPROVED': 2}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-006.

### PR-8959 — chore: RES-187398 keep host-smoke package-lock.json

- URL: [8959](https://github.com/responsive-core/rfp-app/pull/8959); author `sanjeev-s_rio`; created 2026-09-16; **MERGED 2026-09-16**; base `staging`; head `gitnexus-cleanup-pr` / `24b02a6c937ed5c23f2a9ba94d4d4c921921a72a`; API merge_commit_sha `9a6693220bd1fc7851147250ab76eb5ef4493dbe`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=4; f=0/0; reviews {'APPROVED': 4}; inline comments=0; discussions=1; other-author commit records=1; collaborators Gowrishankar S. Related primary IDs: CORE-030.

### PR-8960 — pre-release/staging Rebase

- URL: [8960](https://github.com/responsive-core/rfp-app/pull/8960); author `sanjeev-s_rio`; created 2026-09-16; **MERGED 2026-09-16**; base `development`; head `gitnexus-cleanup-pr` / `24b02a6c937ed5c23f2a9ba94d4d4c921921a72a`; API merge_commit_sha `7c408d7bcdd5d28837bf71b2e55d09c8a08614aa`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=10; f=33/33; reviews {'APPROVED': 5}; inline comments=0; discussions=0; other-author commit records=7; collaborators Gowrishankar S, Jacob Motes, Kaliraj Balakrishnan. Related primary IDs: CORE-030.

### PR-8966 — RES-187387 perf: optimize CI build pipeline, memory headroom, and persistent caching

- URL: [8966](https://github.com/responsive-core/rfp-app/pull/8966); author `sanjeev-s_rio`; created 2026-09-16; **CLOSED UNMERGED 2026-09-16**; base `development`; head `ui-opt` / `ee8cd4824c8eef7b97cbdb762c00d483c9454b76`; API merge_commit_sha `None`.
- Description summary: Two-wave monorepo builds, disk/Turbo caches, output/concurrency tuning and reported benchmarks; later follow-ups refine compatibility. Closed/unmerged variant: no successful merge inferred.
- Evidence/ownership: c=5; f=10/10; reviews ; inline comments=0; discussions=0; other-author commit records=1; collaborators Preethi S. Related primary IDs: CORE-005.

### PR-8968 — RES-187387 perf: optimize CI build pipeline, memory headroom, and persistent caching

- URL: [8968](https://github.com/responsive-core/rfp-app/pull/8968); author `sanjeev-s_rio`; created 2026-09-16; **MERGED 2026-09-16**; base `development`; head `ui-opt-dev` / `1a49de6e6b683bfafa0ee0d3a4e864d34a29f0f7`; API merge_commit_sha `4efff0df209372e369476cf5503a442960a6a2ef`.
- Description summary: Two-wave monorepo builds, disk/Turbo caches, output/concurrency tuning and reported benchmarks; later follow-ups refine compatibility.
- Evidence/ownership: c=6; f=10/10; reviews {'APPROVED': 4}; inline comments=0; discussions=0; other-author commit records=1; collaborators Preethi S. Related primary IDs: CORE-005.

### PR-8988 — fix: update webpack configuration for Module Federation compatibility

- URL: [8988](https://github.com/responsive-core/rfp-app/pull/8988); author `sanjeev-s_rio`; created 2026-09-16; **MERGED 2026-09-16**; base `development`; head `ui-opt-dev` / `5374d37d7b39b0c535b7de86b1eed4aa7cba3d2e`; API merge_commit_sha `7ce3f0f21997e639ad77614b58f1497d55fd4b48`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=2; f=4/4; reviews {'APPROVED': 2}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-005.

### PR-9012 — chore: update package.json and pnpm-lock.yaml for build configuration…

- URL: [9012](https://github.com/responsive-core/rfp-app/pull/9012); author `sanjeev-s_rio`; created 2026-09-17; **MERGED 2026-09-17**; base `development`; head `ui-opt-dev` / `5d087e5d976cbc126a4c9fa63f7c68354b218243`; API merge_commit_sha `0bbcb8fc42970f30a711e2c70a55cc6f1fb18e9d`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=3/3; reviews {'APPROVED': 1}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-005.

### PR-9055 — RES-187387 perf: parallelize Babel via thread-loader & tune worker concurrency

- URL: [9055](https://github.com/responsive-core/rfp-app/pull/9055); author `sanjeev-s_rio`; created 2026-09-17; **MERGED 2026-09-17**; base `development`; head `ui-opt-dev` / `c9ba40b9729c9ad398b79c1c9ddc47ccea70396b`; API merge_commit_sha `fdf24d23a0c76f2886397673909042d34503e41e`.
- Description summary: Scoped Babel thread-loader parallelism, bounded worker/minimizer concurrency, watch-pool lifecycle and Next CI worker settings.
- Evidence/ownership: c=1; f=5/5; reviews {'APPROVED': 2}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-005.

### PR-9114 — fix: adjust parallel minimizer settings for CI environments to optimize performance

- URL: [9114](https://github.com/responsive-core/rfp-app/pull/9114); author `sanjeev-s_rio`; created 2026-09-18; **MERGED 2026-09-18**; base `development`; head `ui-opt-dev` / `dfeb53373a3685bb348d9fa0c40dfbc415489478`; API merge_commit_sha `d8ffb8508dfa40cbbc2dbc36fc9888e22f1d6042`.
- Description summary: Description empty; implementation purpose/status is limited to title, actual changed files/commits and linked initiative.
- Evidence/ownership: c=1; f=1/1; reviews {'APPROVED': 3}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-005.

### PR-9128 — RES-187387 fix: relocate Webpack FS cache & restore Sonar root sources

- URL: [9128](https://github.com/responsive-core/rfp-app/pull/9128); author `sanjeev-s_rio`; created 2026-09-18; **MERGED 2026-09-21**; base `development`; head `ui-opt-dev` / `7c7df975d2a9e534ce1a17ebf8e779bcc96c528e`; API merge_commit_sha `cdbb5bcc614512825e732803f90d9875eecc4e75`.
- Description summary: Move Webpack cache out of node_modules across app configs; correct EXDEV/mount cache placement and Sonar root-source composition.
- Evidence/ownership: c=1; f=6/6; reviews {'APPROVED': 3}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-005.

### PR-9178 — RES-187387 perf: optimize CI build pipeline, memory headroom, and persistent caching

- URL: [9178](https://github.com/responsive-core/rfp-app/pull/9178); author `sanjeev-s_rio`; created 2026-09-21; **CLOSED UNMERGED 2026-09-21**; base `development`; head `ui-opt` / `0bced9664b427bc9a5c1c995cf2a55dcc5ba3269`; API merge_commit_sha `None`.
- Description summary: Cold-build/memory/cache optimization plus benchmark tables, two-wave/Turbo/FS-cache/thread-loader rationale; checked local/build plans, unchecked post-S3-deploy job verification. Baseline variants conflict. Closed/unmerged variant: no successful merge inferred.
- Evidence/ownership: c=2; f=46/46; reviews ; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-005.

### PR-9179 — chore: RES-187387 relocate Webpack FS cache & update build configurations

- URL: [9179](https://github.com/responsive-core/rfp-app/pull/9179); author `sanjeev-s_rio`; created 2026-09-21; **MERGED 2026-09-22**; base `development`; head `ui-opt-conflict` / `b775888f01c805e7b45178ee59dc94a010f90e44`; API merge_commit_sha `def2d492b9ec2411614d6f3803e004a33ff3fe48`.
- Description summary: Relocate compiler caches and synchronize package/build configurations; follow-up to RES-187387.
- Evidence/ownership: c=5; f=35/35; reviews {'DISMISSED': 3, 'APPROVED': 4}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-005.

### PR-9515 — RES-187387 perf: optimize CI build pipeline, memory headroom, and persistent caching

- URL: [9515](https://github.com/responsive-core/rfp-app/pull/9515); author `sanjeev-s_rio`; created 2026-09-30; **OPEN**; base `staging`; head `ui-opt` / `93e20e29670c887d47231a47255884330dd2fe33`; API merge_commit_sha `None`.
- Description summary: Cold-build/memory/cache optimization plus benchmark tables, two-wave/Turbo/FS-cache/thread-loader rationale; checked local/build plans, unchecked post-S3-deploy job verification. Baseline variants conflict.
- Evidence/ownership: c=8; f=46/46; reviews {'APPROVED': 2}; inline comments=0; discussions=0; other-author commit records=0. Related primary IDs: CORE-005.

### PR-8282 — RES-186230 - sonarqube-local-rfp-app

- URL: [8282](https://github.com/responsive-core/rfp-app/pull/8282); author `akarshan-s_rio`; merged 2026-08-27; base `RES-185427-vitest-setup`. **Other-author reference.**
- Description empty. Original local Sonar environment/setup commits are Akarshan-authored; integration into my testing PR does not transfer authorship.
- Returned commit list=9; review states=; principal SHA `7aa3c23ff9269bd434199b6e165813c30b0ca08a`. Complete file endpoint not fetched in this reference pass. Deployment UNKNOWN.

### PR-6421 — Monorepo changes

- URL: [6421](https://github.com/responsive-core/rfp-app/pull/6421); author `gowrishankar_rio`; merged 2026-07-20; base `development`. **Other-author reference.**
- Description documents pnpm/Turbo workspace, shared packages/configs and migration/build/development conventions. Original conversion commits are Gowrishankar-authored; my later optimization builds on it.
- Returned commit list=35; review states=[('hari_rio', 'DISMISSED'), ('dinesh_rio', 'DISMISSED'), ('hari_rio', 'APPROVED')]; principal SHA `2243abcf3270328084c70c95419092185861087f`. Complete file endpoint not fetched in this reference pass. Deployment UNKNOWN.

## Complete deduplicated authored-patch register

This register inventories **every one of the 1,222 ref-reachable author-matched non-merge SHAs**, represented by 1,180 stable-patch groups; identical copies remain listed. Primary ID is an organizational mapping, not exclusive ownership of every path in a broad commit. Generic/no-message records carry changed-path and structural symbol context so small work is not silently dropped. Use the detailed initiative's boundary before generating claims.

Ancestry flags: **H** inspected HEAD, **S** saved origin/staging, **D** saved origin/development, **M** saved origin/master; **branch** means absent from all four. A flag indicates the SHA or an identical patch copy is an ancestor, not current line behavior or deployment. Reverts/superseding implementations remain historical. Full paths and exact diffs can be recovered read-only with the listed SHA in the source repository. Full SHA is the durable key; GitHub commit URLs use `https://github.com/responsive-core/rfp-app/commit/<SHA>` if remote access survives.

### 2022 — 1 patch groups

- 2022-11-09 | CORE-009 | `6a72d6bb339dce72291d388cbdfc75c6bff0cf10` | HSDM | RES-60640 - Style not shown when choosed.. Files/symbols: tinymce.js; tinymce.js.

### 2023 — 444 patch groups

- 2023-01-05 | CORE-037 | `891451a5c5a63f93a248af47af4efcbe8d59bd20` | HSDM | RES-64499. Files/symbols: app_v2/src/containers/project/ProjectAdvancedFilterHelper.ts; app_v2/src/containers/project/documents/ProjectDocumentProperty.tsx; symbols tempDocTypeMap, FinaldocTypeMap.
- 2023-01-05 | CORE-037 | `cc931c2fa19eef6941a69779f4d4d4da77186fe0` | HSDM | RES-64499. Files/symbols: app_v2/src/containers/project/ProjectAdvancedFilterHelper.ts; symbols FinaldocTypeMap.
- 2023-01-05 | CORE-037 | `226c62abb1f0fcc920b46874d02a091658c1c65e` | HSDM | RES-64499. Files/symbols: app_v2/src/containers/project/ProjectAdvancedFilterHelper.ts; symbols finalDocTypeMap.
- 2023-01-06 | CORE-037 | `65b77ecee31bbf6ee22fb884bb7c768095ec6b6e` | HSDM | RES-64398- Author/Reviewer progress and source file options can be removed from section properties of the template. Files/symbols: app_v2/src/containers/project/sections/SectionProperties.tsx; symbols templateExclededProperties.
- 2023-01-06 | CORE-037 | `216b7c194a63b261de2dbe723cc2352eea507de6` | HSDM | RES-64407 - Grid view- need to remove the enter guest mail in team. Files/symbols: app_v2/src/containers/project/ProjectAdvancedFilterHelper.ts; app_v2/src/containers/project/section-questions/grid-view/GridViewHeaderFilter.tsx.
- 2023-01-06 | CORE-037 | `c278cd08c3f12de0833f03fccfeb7e77eab0a8f0` | HSDM | no message. Files/symbols: app_v2/src/containers/project/section-questions/grid-view/GridViewHeaderFilter.tsx; changed symbol GridViewHeaderFilter.
- 2023-01-06 | CORE-037 | `be22ad0940a28c0e57cc7bf1e7acf1905c2280ec` | HSDM | no message. Files/symbols: app_v2/src/containers/project/sections/SectionProperties.tsx; symbols templateExcludedProperties.
- 2023-01-09 | CORE-037 | `f1456d6716aa3895d657908d7ea597792bfd311a` | HSDM | RES-64353. Files/symbols: app_v2/src/containers/project/create/create-project-form/DuplicateProjectBanner.tsx; app_v2/src/containers/project/project-template-process/ProjectTemplateProcessingDialog.tsx; symbols additional.
- 2023-01-09 | CORE-037 | `4040067dcb3180f46cf3205079571ac707c91178` | HSDM | no message. Files/symbols: app_v2/src/containers/project/create/create-project-form/DuplicateProjectBanner.tsx; app_v2/src/containers/project/project-template-process/ProjectTemplateProcessingDialog.tsx; symbols additionalAttributes.
- 2023-01-10 | CORE-033 | `cfee53a730c03bc868eaa3ae91f23fb39e7c4e12` | HSDM | RES-64633 , RES-64629. Files/symbols: app_v2/src/components/dialogModels/RespondProject/DuplicateProjectProcessing.tsx; app_v2/src/containers/project/ManageProjects/ProjectCustomizeMetadata.tsx; symbols additionalAttributes, indexOfNotification.
- 2023-01-10 | CORE-037 | `6be18a57828ec9f0ddb03a4ca8072c070360a194` | HSDM | no message. Files/symbols: app_v2/src/containers/project/create/create-project-form/DuplicateProjectBanner.tsx; symbols isTemplate.
- 2023-01-10 | CORE-033 | `5d3123ee4a2a6063245feaede571f22c0683ae3d` | HSDM | no message. Files/symbols: app_v2/src/components/dialogModels/RespondProject/DuplicateProjectProcessing.tsx; app_v2/src/containers/project/project-template-process/ProjectTemplateProcessingDialog.tsx; changed symbol DuplicateProjectProcessing.
- 2023-01-18 | CORE-009 | `7235072d016171a398772c1c66a0b07fcf30c12d` | HSDM | RES-64180. Files/symbols: app/vendor/tinymce-editor-react/tinymce.js; app/vendor/tinymce-editor/tinymce.js.
- 2023-01-19 | CORE-033 | `10c7dd733e3f4c0efea6655d92adb6cf18a0ec4a` | HSDM | RES-65121 - Dark Mode Changes. Files/symbols: app_v2/src/containers/project/manage-templates/ManageTemplateStyles.tsx; app_v2/src/containers/project/manage-templates/template-components/UsedCountDialog.tsx.
- 2023-01-19 | CORE-033 | `593e2d713127b08055e27d7ca9f7daf3d42caa40` | HSDM | no message. Files/symbols: app_v2/src/containers/project/project-template-process/CreateProjectFromTemplateWrapper.tsx; app_v2/src/containers/project/project-template-process/TemplatePropertiesContainer.tsx; changed symbol CreateProjectFromTemplateWrapper.
- 2023-01-20 | CORE-037 | `5fb541bb0649d4d7770b1905a43decc1f7056e8c` | HSDM | no message. Files/symbols: app_v2/src/containers/project/manage-templates/ManageTemplateStyles.tsx; changed symbol ProjectTemplateProcessingDialogStyles.
- 2023-01-23 | CORE-009 | `c87752c3ef793a606a39e909c609e2f9a5f208d4` | HSDM | RES-61922 - Annotation not copied over. Files/symbols: Editor.tsx.
- 2023-02-07 | CORE-009 | `d67c1332be1841bc12a28e7340f16f43d1e3ff3b` | HSDM | RES-65572 - Tinymce Version Upgrade from 5 to 6 (V2). Files/symbols: icons.js; model.js; symbols e, s, a.
- 2023-02-07 | CORE-009 | `c293dfe1a7f1cfb3e0f284a7e8b3fd2c1fba9eca` | HSDM | no message. Files/symbols: app/vendor/tinymce-editor-react/plugins/code/plugin.js; app/vendor/tinymce-editor-react/plugins/lists/plugin.js; symbols o, hasProto, typeOf.
- 2023-02-07 | CORE-009 | `3fdec25dee2885f9b41e5027fe49af94493e9770` | HSDM | no message. Files/symbols: app/vendor/tinymce-editor-react/plugins/ice/plugin.js; app/vendor/tinymce-editor-react/tinymce.js; symbols spellCheckClickEvent, replaceTextByRange, range.
- 2023-02-07 | CORE-007 | `28f1c03446b019e23227a45e1a5293170093a6aa` | HSDM | no message. Files/symbols: app/vendor/tinymce-editor-react/plugins/ice/plugin.js; app/vendor/tinymce-editor-react/plugins/lists/plugin.js; symbols spellCheckClickEvent, replaceTextByRange, range.
- 2023-02-07 | CORE-007 | `e46860d0aa27d2f92125b53367e80117939f5773` | HSDM | no message. Files/symbols: app/vendor/tinymce-editor-react/plugins/paste/plugin.js; app_v2/src/containers/guest/question/GuestResponseView.tsx; symbols basicTinymceOptions.
- 2023-02-08 | CORE-007 | `ca68083e0612308d16bbb1886eba2e910b33881f` | HSDM | no message. Files/symbols: app_v2/src/containers/guest/question/GuestResponseView.tsx; style/scaffold change (diff inspected).
- 2023-02-08 | CORE-009 | `3402cb65090998c56efa60b7f539451354d05338` | HSDM | no message. Files/symbols: app_v2/src/rfp-components/RfpRichText.tsx; app_v2/src/utils/TinyMCEUtils.ts; changed symbol RfpRichText.
- 2023-02-10 | CORE-009 | `58d73ab91c96555e86df221fddc70a744134bb8a` | HSDM | RES-66530, RES-66558, RES-66550. Files/symbols: plugin.js; plugin.js.
- 2023-02-10 | CORE-009 | `bafe1a7187d545741437dbf8062f9211d76799df` | HSDM | no message. Files/symbols: app/vendor/tinymce-editor-react/tinymce.js.
- 2023-02-10 | CORE-007 | `4202b1e16add3be57d43410aa146c069ad55a860` | HSDM | RES-66549. Files/symbols: app/app/js/controller/AppController.js; app/app/js/controller/pages/guestAlCtrl.js.
- 2023-02-13 | CORE-007 | `f5c7d3db7852ebb5611e049151b2b6c69acb05ca` | HSDM | RES-66820 ,RES-66549. Files/symbols: rfpio.css; AppController.js; symbols hasProto, typeOf, t.
- 2023-02-13 | CORE-037 | `4521f709750502a1a0273d5916bbcafc1d325efc` | HSDM | no message. Files/symbols: app/app/css/rfpio.css; style/scaffold change (diff inspected).
- 2023-02-13 | CORE-009 | `58a2023475e91eb02af4ce07af17fa4e5a1fd033` | HSDM | no message. Files/symbols: app/vendor/tinymce-editor-react/plugins/lists/plugin.js; app/vendor/tinymce-editor/plugins/lists/plugin.js; style/scaffold change (diff inspected).
- 2023-02-13 | CORE-009 | `91e14f38b824a7e6feea861c9e2d881eadf4d19b` | HSDM | no message. Files/symbols: app/vendor/tinymce-editor-react/plugins/lists/plugin.js; app/vendor/tinymce-editor/plugins/lists/plugin.js; style/scaffold change (diff inspected).
- 2023-02-13 | CORE-009 | `fccd1cbaf3699e01673adbe872435d7e1769ba7d` | HSDM | Fixes. Files/symbols: plugin.js; plugin.js; symbols __webpack_require__, originUrl, buttonState.
- 2023-02-14 | CORE-009 | `e59d806911f6a739e1fe08e5085625cf5cc70358` | HSDM | RES-47210. Files/symbols: app_v2/src/components/DocumentLibFiles/DlFilesList.tsx; app_v2/src/components/DocumentLibFiles/ListViewComponent.tsx; symbols ThumbnailViewComponent, newList, file.
- 2023-02-15 | CORE-009 | `8646f27629637a34367f014f92dea3b8d0550041` | HSDM | RES-66933. Files/symbols: app/vendor/tinymce-editor-react/skins/ui/oxide/skin.min.css.
- 2023-02-15 | CORE-009 | `e63af937ee0d9e8fc0d3e31864c155858fcbe50b` | HSDM | RES-62009. Files/symbols: app/vendor/tinymce-editor-react/themes/silver/theme.js; app/vendor/tinymce-editor/themes/silver/theme.js.
- 2023-02-15 | CORE-009 | `df63d01dbb2a0a254d609b5018b5cc98c23b83ef` | HSDM | no message. Files/symbols: app/vendor/tinymce-editor-react/skins/ui/oxide/skin.min.css.
- 2023-02-15 | CORE-009 | `704531baaed630c2d58d2a61030821c85a8dcdbf` | HSDM | RES-67126 Bullet issues. Files/symbols: plugin.js; plugin.js; symbols startNode.
- 2023-02-16 | CORE-009 | `d6194b5d0cf57d008a6671eeeb015759f5e03e2f` | HSDM | RES-66915. Files/symbols: app/app/js/controller/respond/ansLibCtrl.js; app/app/js/controller/respond/contentLibraryCtrl.js; symbols tinyExtraOptForDialog, customTinyExtra, processShapes.
- 2023-02-20 | CORE-009 | `86790eee2842b2a5596cc4adc7f88019bae69ffb` | HSDM | Library Fixes. Files/symbols: model.js; model.js.
- 2023-02-27 | CORE-033 | `3d2557d982f7bf6e6acb885682c101aa7250cf37` | branch | Application font update. Files/symbols: app_v2/src/components/App.tsx; app_v2/src/components/ComponentStyles.tsx.
- 2023-02-27 | CORE-033 | `36cab2b4224e4e8121329079789b2c80eceeeae9` | branch | Application font update. Files/symbols: app_v2/src/components/Footer.tsx; app_v2/src/components/FooterLoggedIn.tsx.
- 2023-02-28 | CORE-033 | `37e5cf5531c813c40ae21c84a6f6d4d84d760839` | branch | Application font update. Files/symbols: app_v2/src/components/MailNotificationPopover.tsx; app_v2/src/containers/e-sign/ESignBulkListTable.tsx.
- 2023-02-28 | CORE-023 | `584b543a75cf8a0531ef0d5399d1ee48582c3b1c` | branch | no message. Files/symbols: app_v2/src/containers/project/about-project/AboutHeader.tsx; app_v2/src/containers/project/activities/ActivityDetailsDialog.tsx; changed symbol AboutHeader.
- 2023-02-28 | CORE-033 | `c8ed8d49b31eafac15b67f8a5f0fed872be205d0` | branch | no message. Files/symbols: app_v2/src/components/FooterLoggedIn.tsx; app_v2/src/components/dialogModels/RespondProject/ProjectViewOptions.tsx; changed symbol footerStyles.
- 2023-03-01 | CORE-033 | `c4a7afa744ad87f2caa60e1ad92f9fb408a27023` | branch | Application font update. Files/symbols: app_v2/src/containers/e-sign/ESignBulkListTable.tsx; app_v2/src/containers/e-sign/ESignDocumentList.tsx.
- 2023-03-01 | CORE-033 | `ea41cd34e94fc0c86b99b8bb7a109db8d1bbce94` | branch | no message. Files/symbols: app_v2/src/components/Footer.tsx; app_v2/src/components/FooterLoggedIn.tsx; changed symbol footerStyles.
- 2023-03-02 | CORE-033 | `fe517e4309e7f347618a049124dc8ec9479da879` | branch | Font Changes. Files/symbols: app_v2/src/components/project-intake-components/Discussions/DiscussionCreateEditName.tsx; app_v2/src/components/project-intake-components/Discussions/DiscussionListPane.tsx; symbols cellCssClass.
- 2023-03-02 | CORE-033 | `6b2b9e01def794401f56a8f4a37e31c2491e91a1` | branch | no message. Files/symbols: app_v2/src/components/App.tsx; changed symbol App.
- 2023-03-03 | CORE-033 | `1adf565d273c53ba3435280fd12c620233d2b94e` | branch | Font update. Files/symbols: app_v2/src/containers/project/ManageProjects/ColumnFilter.tsx; app_v2/src/containers/project/ManageProjects/ProjectQuestionProgressStatus.tsx.
- 2023-03-07 | CORE-009 | `09488b160b8798f0b2917e04d5454f653be12b36` | HSDM | RES-68152. Files/symbols: app/app/js/controller/AppController.js; app/vendor/tinymce-editor-react/skins/ui/oxide/skin.min.css. Identical patch copies: `92f22e43517e30f4f41b5c1e710ede3e28abc574`.
- 2023-03-09 | CORE-033 | `90e06e2fa36234d382eaab5621d641899a00c4d4` | branch | Font update. Files/symbols: app_v2/src/components/LeftNavBar.tsx; app_v2/src/components/NavBar.tsx.
- 2023-03-10 | CORE-009 | `e7a4597c240ac1e744a20815cecd88bd402d1fd4` | HSDM | RES-66615. Files/symbols: app/vendor/tinymce-editor/skins/ui/oxide/skin.min.css.
- 2023-03-10 | CORE-009 | `2860ca28dfb77674833d755ffed7007dc4326dcd` | HSDM | RES-66567 , RES-66533. Files/symbols: skin.min.css.
- 2023-03-14 | CORE-009 | `a70f63f0a4d7987e5088cf00ff9b8e953e0bf361` | HSDM | no message. Files/symbols: app/vendor/tinymce-editor/skins/ui/oxide/skin.min.css.
- 2023-03-15 | CORE-009 | `7760c307cd214b154e0fa0533559a54860d13d2d` | HSDM | RES-66597. Files/symbols: app/library-search/controller/rfpio_controllers.js; app/library-search/resource/create_al_content.html; symbols tinyExtra.
- 2023-03-16 | CORE-009 | `4f76b4cab9d591b984f15fe23f52be82325fdd32` | HSDM | RES-68987. Files/symbols: app/vendor/tinymce-editor-react/plugins/mergetagpopover/plugin.js; app/vendor/tinymce-editor-react/plugins/rfpPaste/plugin.js; symbols paste_cursor.
- 2023-03-17 | CORE-009 | `c620cc25e7b4aa7c1e16fc126d3c8d6f5cb56360` | HSDM | RES-68987 - V1. Files/symbols: tinymce.js.
- 2023-03-20 | CORE-009 | `921499aae37502de3f70795fb98a2766ed04cae2` | HSDM | RES-68987 - extra code added in source code. Files/symbols: plugin.js; plugin.js; symbols paste_cursor.
- 2023-03-22 | CORE-037 | `965d4776635f7678bf0181ac36125026791b3a68` | HSDM | RES-69269 , RES-69285. Files/symbols: app_v2/src/containers/e-sign/ESignLifeCycle.tsx; app_v2/src/containers/e-sign/life-cycle-components/ESignReview.tsx.
- 2023-03-22 | CORE-037 | `26c7f175c3e7da47a2e901efab0bf0daceda27dd` | HSDM | no message. Files/symbols: app_v2/src/containers/e-sign/life-cycle-components/ESignReview.tsx; changed symbol EsignReview.
- 2023-03-22 | CORE-037 | `98bb2acc697b5b5def96e48061b5af977033a58f` | HSDM | no message. Files/symbols: app_v2/src/containers/e-sign/ESignLifeCycle.tsx; app_v2/src/containers/e-sign/life-cycle-components/ESignReview.tsx; symbols keys, size.
- 2023-03-22 | CORE-033 | `e40f9804feea62a07f17db2e43bddeb5c5b209b2` | HSDM | no message. Files/symbols: app_v2/src/containers/e-sign/life-cycle-components/ESignReview.tsx; app_v2/src/containers/project/create/create-project-form/DuplicateProjectBanner.tsx; changed symbol EsignReview.
- 2023-03-22 | CORE-037 | `82b49f34d4e978725a112d801d1260091151b990` | HSDM | no message. Files/symbols: app_v2/src/containers/e-sign/life-cycle-components/ESignReview.tsx; changed symbol EsignReview.
- 2023-03-22 | CORE-037 | `bd40a79785ecfd436f106374f2789860de064ba4` | HSDM | no message. Files/symbols: app_v2/src/containers/project/create/create-project-form/DuplicateProjectBanner.tsx; changed symbol DuplicateProjectBanner.
- 2023-03-22 | CORE-037 | `f67c74c4ad863fe5705d694135f5c1007814f7b6` | HSDM | no message. Files/symbols: app_v2/src/containers/e-sign/life-cycle-components/ESignReview.tsx; changed symbol EsignReview.
- 2023-03-22 | CORE-037 | `bf2df20096c510ab72f45cfb07ea3b22121ef29c` | HSDM | no message. Files/symbols: app_v2/src/containers/project/create/create-project-form/DuplicateProjectBanner.tsx; symbols size.
- 2023-03-22 | CORE-033 | `f31d96f08fc547d3b6fcbb790581a14e496fc3cd` | HSDM | no message. Files/symbols: app_v2/src/styles/App.css; style/scaffold change (diff inspected).
- 2023-03-22 | CORE-033 | `82055eb3602bd29d3c8454db53a2674a99f53074` | HSDM | RES-69379. Files/symbols: app_v2/src/components/DraggableToolBar.tsx.
- 2023-03-23 | CORE-009 | `2ab0ec7ac34136210182e5ed2f8908ac57fa2aba` | HSDM | RES-66564. Files/symbols: app/vendor/tinymce-editor-react/skins/ui/oxide/skin.min.css; app/vendor/tinymce-editor-react/tinymce.js.
- 2023-03-27 | CORE-009 | `66403b72ad9cb54e567bf33e9a31e5f9ae8f6338` | HSDM | RES-69205. Files/symbols: app/vendor/tinymce-editor-react/plugins/mergetagpopover/plugin.js; app/vendor/tinymce-editor/tinymce.js; symbols $tempcrntNode, elmRng, isCollapsed.
- 2023-03-27 | CORE-009 | `790cf56467c44733a1a96006655cb6d77442c981` | HSDM | RES-69205. Files/symbols: app/vendor/tinymce-editor-react/plugins/mergetagpopover/plugin.js; app/vendor/tinymce-editor/tinymce.js.
- 2023-03-28 | CORE-009 | `005aaec22bbb9e1ffcd6b37b3a72a0b17e6aacf7` | HSDM | RES-69205. Files/symbols: app/vendor/tinymce-editor-react/plugins/mergetagpopover/plugin.js; app/vendor/tinymce-editor/tinymce.js.
- 2023-03-28 | CORE-009 | `09d782833092b401cddf017d351ae2743f7a1673` | HSDM | RES-69205 , RES-67443. Files/symbols: plugin.js; plugin.js.
- 2023-03-30 | CORE-009 | `fb44f5b0c2fa8cc787f1fec81eb6566451cc2889` | HSDM | RES-69205 , RES-67443 , RES-65551. Files/symbols: plugin.js; plugin.js; symbols $tempcrntNode, elmRng, isCollapsed.
- 2023-04-11 | CORE-001 | `231eabe4ef59b9ed6f678c37eca835ec5f367aa9` | HSDM | RES-70018. Files/symbols: app_v2/src/assets/fonts/rfpio-font-icon/icons-reference.html; app_v2/src/assets/fonts/rfpio-font-icon/rfpio.eot; symbols AppLauncherMenu, setTheme, theme.
- 2023-04-11 | CORE-033 | `5543fe598327e9d85678194e4a66c1c8cdfa63b3` | HSDM | Welcome Banner bug fix. Files/symbols: app_v2/src/rfp-components/RfpTour.tsx.
- 2023-04-12 | CORE-001 | `a8f9206d360e04f961f81c8f0233bdbfb7441e5b` | HSDM | RES-70018. Files/symbols: app_v2/src/components/AppLauncherMenu.tsx; app_v2/src/components/AvatarMenu.tsx; symbols UI_V2_STRICT.
- 2023-04-12 | CORE-001 | `bee468dc9e6b9c3f007f5e40273cc2cea754484c` | HSDM | RES-70018. Files/symbols: app_v2/src/components/AvatarMenu.tsx; app_v2/src/components/{AppLauncherMenu.tsx =&gt; HeaderWrapper.tsx}; symbols projectVO.
- 2023-04-12 | CORE-033 | `f95ce94fdb123ee55e6b4febeadc056e6b387f38` | HSDM | RES-70018. Files/symbols: app_v2/src/components/AvatarMenu.tsx; symbols finalV1Url.
- 2023-04-12 | CORE-037 | `2cf927747452a9f2483cc84ec216937255e6c9a3` | HSDM | RES-70018. Files/symbols: app_v2/src/containers/project/PageHeader.tsx; symbols QuestionPageHeaderWrapper, projectVO, hasUpdateSectionPermission.
- 2023-04-12 | CORE-033 | `00ec2e0ae7f72a85b8785c601a5124811d026aea` | HSDM | RES-70018. Files/symbols: app_v2/src/components/AvatarMenu.tsx; symbols UI_V2_STRICT, module, companyId.
- 2023-04-13 | CORE-033 | `20ee84f19ad50db95a0a422339eaf73cae43e42b` | HSDM | RES-70018 - Unit Test Cases. Files/symbols: app_v2/src/containers/project/about-project/AboutHeader.tsx; app_v2/src/containers/project/project-template-process/CreateProjectFromTemplateWrapper.tsx; symbols MockAvatarMenuDetails, url, origin.
- 2023-04-13 | CORE-033 | `6509c00f1615dafdf4c197bce324278d8d1b22e0` | HSDM | RES-70018 - Unit Test Cases. Files/symbols: app_v2/tests/containers/components/AvatarMenu.test.tsx; symbols theme, prevColor, currentColor.
- 2023-04-17 | CORE-001 | `1ce3c7c5be0ef851e4cd729bca1b477ef40f4a4c` | HSDM | RES-71312 , RES-71314 , RES-71315 , RES-71316 , RES-71317 , RES-71318 , RES-71319 , RES-71320 , RES-71321 , RES-71322 , RES-71325 , RES-71326 , RES-71327 , RES-71366. Files/symbols: AvatarMenu.tsx; FooterLoggedIn.tsx; symbols UI_V2_STRICT, classes, module.
- 2023-04-17 | CORE-001 | `e4a8a1a38800336e696cffc76c0c514feb809f65` | HSDM | no message. Files/symbols: app_v2/src/components/HeaderWrapper.tsx; changed symbol HeaderWrapper.
- 2023-04-17 | CORE-037 | `7b3e2622123ec8750e424db53704a8aacc4af233` | HSDM | conflict resolve. Files/symbols: app_v2/src/containers/project-request/request/PublishedRequestHeader.tsx.
- 2023-04-17 | CORE-019 | `2769990f9cfc94d9a41beccf688079d2fc5409f0` | HSDM | My Work redirection. Files/symbols: AvatarMenu.tsx; symbols myWorkVersion.
- 2023-04-17 | CORE-001 | `e91485e32d73b2ecfca1befabfed60c55fbfab55` | HSDM | RES-71323. Files/symbols: app_v2/src/components/AppLauncher.tsx; app_v2/src/components/AvatarMenu.tsx; symbols myWorkVersion, currentUserInfo, urlPrefix.
- 2023-04-17 | CORE-033 | `3d1ff9af158caff3c8c74318c2863d53aade6153` | HSDM | RES-71323. Files/symbols: app_v2/src/components/AvatarMenu.tsx; app_v2/src/styles/App.css.
- 2023-04-17 | CORE-018 | `f89a73b4f697122f7cb982e87853609850314561` | HSDM | RES-71480 , RES-71486. Files/symbols: AvatarMenu.tsx; FooterLoggedIn.tsx.
- 2023-04-18 | CORE-009 | `2b7ae8d8a3468158fba6de52ed9c96feb405e9e4` | HSDM | RES-66902. Files/symbols: app/vendor/tinymce-editor-react/plugins/rfpPaste/plugin.js; app/vendor/tinymce-editor/tinymce.js; symbols tempStyle, finalTempStyle, styleName.
- 2023-04-18 | CORE-001 | `66ba195659c856769a9628d80b78b39ff5061c74` | HSDM | RES-71372. Files/symbols: app_v2/src/components/AvatarMenu.tsx; app_v2/src/components/HeaderWrapper.tsx; symbols UI_V2_STRICT, filterModules, darkEnabled.
- 2023-04-18 | CORE-009 | `a50d89109dbcc8b2f3beb542845ccfaca9fd9917` | HSDM | RES-71549. Files/symbols: app_v2/src/utils/TinyMCEUtils.ts; symbols draggable.
- 2023-04-19 | CORE-033 | `740499cc33c79c0f15813c7938582def46f21a40` | HSDM | Bug fixes. Files/symbols: app_v2/src/components/AvatarMenu.tsx.
- 2023-04-19 | CORE-037 | `2eda67038d3d0d0a8a52ffad91726fcd44eb25ca` | HSDM | RES-71715. Files/symbols: app/app/js/controller/settings/organizationCtrl.js; symbols updateRowHeight, sme_height.
- 2023-04-19 | CORE-037 | `c599a24bdac6eebf6690a2fe0f61b7fc98f9bc18` | HSDM | RES-71715. Files/symbols: app/app/js/controller/settings/organizationCtrl.js; symbols updateRowHeight.
- 2023-04-19 | CORE-037 | `cd842eea7bb9ee3e9ca4ae41f9fbeb602997dec5` | HSDM | no message. Files/symbols: app/app/js/controller/settings/organizationCtrl.js; style/scaffold change (diff inspected).
- 2023-04-20 | CORE-001 | `70f04fa382b55ad7e08429f06719daabdee56c22` | HSDM | bug fix. Files/symbols: HeaderWrapper.tsx.
- 2023-04-20 | CORE-037 | `1371ab82e8c381f8394891ac863201c304eb3dd8` | HSDM | RES-71715. Files/symbols: app/app/js/controller/settings/organizationCtrl.js.
- 2023-04-20 | CORE-001 | `f99d290937c4e79533e9df0052959bfdb006320b` | HSDM | no message. Files/symbols: app_v2/src/components/AppLauncher.tsx; changed symbol menuItems.
- 2023-04-20 | CORE-009 | `78ffbaf06d3160c0b2a4af1105241f23ecea03ae` | HSDM | RES-71830. Files/symbols: app/vendor/tinymce-editor-react/skins/ui/oxide/skin.min.css; app_v2/src/rfp-components/RfpRichText.tsx. Identical patch copies: `5d0126595ddc11b4cbb743426750027982c5eb7c`.
- 2023-04-24 | CORE-001 | `42e47585d000d52d38b0f4bbfa1637c7b9b57c77` | HSDM | RES-70018. Files/symbols: app_v2/src/components/AvatarMenu.tsx; app_v2/src/components/HeaderWrapper.tsx; symbols isManageProject, sectionsNotification, projectNotification.
- 2023-04-24 | CORE-001 | `3484d4e4e0ac40f7b95cb763bc07da5b62fcd496` | HSDM | RES-70018. Files/symbols: app_v2/src/components/HeaderWrapper.tsx.
- 2023-04-25 | CORE-001 | `5714d43af4e8b16348b4b8331a77dbf9854d1415` | HSDM | RES-70018. Files/symbols: app_v2/src/components/AvatarMenu.tsx; app_v2/src/components/HeaderWrapper.tsx; symbols hasProjectNotification, hasSectionsNotification, finalSectionsNotification.
- 2023-04-25 | CORE-037 | `76fc14c79d221ce3d48caebc5bfbe0a4800d5c45` | HSDM | RES-70018. Files/symbols: app_v2/src/containers/project/ManageProjects/ProjectHeader.tsx; app_v2/src/containers/project/PageHeader.tsx; symbols obj, getAllPendingMail, response.
- 2023-04-26 | CORE-001 | `02d8a142df4c07b40972e9f37a6c9a3dc4f17c38` | HSDM | RES-70018. Files/symbols: app_v2/src/components/AvatarMenu.tsx; app_v2/src/containers/project/ManageProjects/ProjectHeader.tsx; symbols badgeCount, setNotificationBadgePage, finalSectionsNotification.
- 2023-04-26 | CORE-038 | `e012750b61ead7410e6eaa84c7582bd94e60b1b9` | HSDM | no message. Files/symbols: app/version.txt; app_v2/package.json; style/scaffold change (diff inspected).
- 2023-04-26 | CORE-033 | `df61e2146e34f5048e524a7da7497767b7c18805` | HSDM | RES-70018. Files/symbols: app_v2/src/components/AvatarMenu.tsx; app_v2/src/containers/project/ManageProjects/ProjectHeader.tsx; symbols getPendingMail, resultCount, obj.
- 2023-05-02 | CORE-001 | `3e9f9fe2ce7ce276e0292d5a08023eeccd3ab3d9` | HSDM | RES-72192. Files/symbols: app_v2/src/components/DummyFootter.tsx; app_v2/src/components/HeaderWrapper.tsx; symbols DummyFooter, classes, footerStyles.
- 2023-05-02 | CORE-033 | `f5c09be0a1bc15ce37d7713f429b15f9c261f65c` | HSDM | no message. Files/symbols: app_v2/src/components/HelpCenter.tsx; changed symbol HelpCenter.
- 2023-05-03 | CORE-033 | `8dd4048b29ccfddcc2665a2a050508170b662e53` | HSDM | RES-72192. Files/symbols: app_v2/src/components/DummyFootter.tsx; app_v2/src/components/HelpAndContact.tsx; symbols classes, activeUsersMap, routeInfo.
- 2023-05-03 | CORE-007 | `c3f2896562fba6f56200c1fb3ef1a074bd8b6e60` | HSDM | RES-70016. Files/symbols: app/app/js/controller/AppController.js; app/app/js/controller/pages/guestAlCtrl.js.
- 2023-05-04 | CORE-007 | `de1afe7d59352f13bebba18fc66f54af070b5ab7` | HSDM | RES-70016. Files/symbols: app/app/js/controller/AppController.js; app/app/js/controller/pages/guestAlCtrl.js.
- 2023-05-04 | CORE-033 | `39bfc317e06ec0b837cba7e044a28458590f5432` | HSDM | RES-72192. Files/symbols: app_v2/src/components/HelpCenter.tsx; symbols xl.
- 2023-05-04 | CORE-007 | `7679f9d99f0a673040ce435aeac48a704830416a` | HSDM | RES-70016. Files/symbols: app/app/js/controller/AppController.js; app/app/js/controller/pages/guestAlCtrl.js.
- 2023-05-04 | CORE-023 | `c4fa153f533f79815c9bb9789cfd4c4bb9b342ec` | HSDM | RES-72193. Files/symbols: app_v2/src/components/DocumentLibFiles/ListViewComponent.tsx; app_v2/src/components/DummyFootter.tsx; symbols FooterWrapper, classes, history.
- 2023-05-08 | CORE-001 | `507d493957738d0efe6220e9f7d2c279f9a450e7` | HSDM | RES-72193. Files/symbols: app_v2/src/components/FooterComponents/FooterWrapper.tsx; app_v2/src/components/{ =&gt; FooterComponents}/HelpAndContact.tsx; symbols FooterWrapper, classes, history.
- 2023-05-08 | CORE-038 | `25a611b1e7200da1e8770eafa796ed368d3e52e7` | HSDM | no message. Files/symbols: app_v2/tests/__mocks__/resize.js; style/scaffold change (diff inspected).
- 2023-05-09 | CORE-033 | `22210ac3d6dfd66d419dc39d68cde37edf6b68da` | HSDM | RES-72193. Files/symbols: app_v2/src/components/FooterComponents/FooterWrapper.tsx; app_v2/src/components/FooterComponents/SubmitIdeaDialog.tsx; symbols FooterWrapper, module, isIntakePage.
- 2023-05-09 | CORE-001 | `89097b969afb3ef65b078ac99a7074dec2e563a6` | HSDM | RES-73539 , RES-72318. Files/symbols: HelpCenter.tsx; HeaderWrapper.tsx.
- 2023-05-10 | CORE-018 | `f2a52a72560cc7d5a50e7074d91f780557673083` | HSDM | RES-73626 , RES-73629 , RES-73635. Files/symbols: HelpCenter.tsx; DocumentViewPage.tsx; symbols tableStyle.
- 2023-05-12 | CORE-018 | `a23bfa00848fb9c4af618979a531ad4afaefa9df` | HSDM | RES-73419. Files/symbols: app_v2/src/containers/content-library/ALStandardFieldRender.tsx.
- 2023-05-15 | CORE-009 | `635f0c411cb19179d60794a2fd09d2ec53faa530` | HSDM | RES-72505. Files/symbols: app_v2/src/rfp-components/RfpRichText.tsx.
- 2023-05-15 | CORE-011 | `8ede5a35dfe4e7f2078bab139dce5ea9e2f0adad` | HSDM | My account profile bug fix. Files/symbols: DateTimeFormat.tsx; ProfileInformationContainer.tsx.
- 2023-05-16 | CORE-011 | `1c7fa2461e59f8832aabf4889063fc8b94c34c8d` | HSDM | no message. Files/symbols: app_v2/src/containers/my-account/profile/ImageUpload.tsx; changed symbol ImageUpload.
- 2023-05-16 | CORE-011 | `1fdae0a2e84f6c0a188e1e7d930c51188fdededb` | HSDM | no message. Files/symbols: app_v2/src/containers/my-account/profile/ProfileStyles.tsx; changed symbol InputsContainerStyles.
- 2023-05-17 | CORE-009 | `26ef7250bec7ab00ff94ab98bd867a53d4efb854` | HSDM | RES-66602. Files/symbols: app/vendor/tinymce-editor-react/plugins/rfpioApplyStyle/plugin.js; symbols skipLocalName.
- 2023-05-18 | CORE-009 | `3d8ae3b9d8eba2187c19b121a897a748716f6269` | HSDM | RES-73156 , RES-72032. Files/symbols: plugin.js.
- 2023-05-18 | CORE-009 | `44f365ad7905797d117d8f75cb9e886a46bc5091` | HSDM | RES-66602 , RES-73156 , RES-72032. Files/symbols: plugin.js; tinymce.js; symbols skipLocalName.
- 2023-05-19 | CORE-009 | `f91d3bb63e1ca509f770dbf8a23f305063f4d93d` | HSDM | RES-70969. Files/symbols: app/vendor/tinymce-editor-react/plugins/table/plugin.js; symbols hasProto, typeOf, t.
- 2023-05-19 | CORE-011 | `c3ba6f1a56dd3a10229c495606d75973ad407c31` | branch | RES-74558 , RES-74559 , RES-74560. Files/symbols: AvatarMenu.tsx; FooterWrapper.tsx; symbols UI_V2_STRICT.
- 2023-05-22 | CORE-009 | `626cce6e61c0de7b4587afd901925c4972f30f8b` | HSDM | RES-66602 , RES-73156 , RES-72032 , RES-70969. Files/symbols: plugin.js; plugin.js.
- 2023-05-22 | CORE-009 | `65e73d8222ce9539a8d4c47553ce0318867a29e1` | HSDM | RES-66602 , RES-73156 , RES-72032 , RES-70969. Files/symbols: plugin.js; tinymce.js; symbols hasProto, typeOf, t.
- 2023-05-23 | CORE-009 | `3c5d1d789f9c27f4886135af8dba0502e3065168` | HSDM | RES-66602 , RES-73156 , RES-72032 , RES-70969. Files/symbols: plugin.js; plugin.js.
- 2023-05-23 | CORE-011 | `504a059eb8b2c0aa2d7f80284bd2b883a8b20599` | HSDM | My account Security tabs. Files/symbols: MyAccountBody.tsx; MyAccountService.ts; symbols getApitoken, response, SecurityContainer.
- 2023-05-23 | CORE-011 | `a69fe8c8c8bec8303df051e64443daf4782fb2a1` | HSDM | My account security tabs. Files/symbols: MyAccountService.ts; SecurityContainer.tsx; symbols getApitoken, SecurityContainer, setUserData.
- 2023-05-23 | CORE-009 | `921a6a9013082d6373386ecf6a3d38994f7ca9b9` | HSDM | RES-66602 , RES-73156 , RES-72032 , RES-70969. Files/symbols: plugin.js; plugin.js; symbols t, s, b.
- 2023-05-23 | CORE-009 | `e015153803911508925cf63464b5f9e54b16c720` | HSDM | RES-72614. Files/symbols: app/vendor/tinymce-editor-react/plugins/rfpioApplyStyle/plugin.js; app/vendor/tinymce-editor/tinymce.js.
- 2023-05-25 | CORE-009 | `f28508c3fde465091f8e16a82657831258cf96ee` | HSDM | RES-72614. Files/symbols: library_fixes.txt; symbols o.
- 2023-05-29 | CORE-011 | `4fe4cf2751da2dba0ed22f95ce707faf645ceab1` | branch | My Account Conflict resolve. Files/symbols: IntegrationInitiator.tsx; IntegrationRenderer.tsx.
- 2023-05-30 | CORE-011 | `d7c236689ab0f31d11241645b6eaacb1316a32e2` | HSDM | RES-66296. Files/symbols: app_v2/src/containers/my-account/MyAccountService.ts; app_v2/src/containers/my-account/MyAccountStyles.tsx; symbols config, resetPassword, obj.
- 2023-05-31 | CORE-011 | `94e47e8cacf603730d628b86b44c3b5032ed4de6` | HSDM | RES-66296. Files/symbols: app_v2/src/containers/my-account/MyAccountBody.tsx; app_v2/src/containers/my-account/MyAccountService.ts; symbols resetPassword, validateCode2FA, PasswordRenderer.
- 2023-05-31 | CORE-011 | `78ec6572413c656e359b3a8d1c4542f92aaef08f` | HSDM | RES-66296. Files/symbols: app_v2/src/containers/my-account/MyAccountBody.tsx; app_v2/src/containers/my-account/MyAccountService.ts; symbols generateNewSecret.
- 2023-05-31 | CORE-009 | `a6c7786f139111d328a089ffe1355cdfba2fcc09` | HSDM | tinymce bug fix. Files/symbols: plugin.js; tinymce.js.
- 2023-05-31 | CORE-011 | `fd1cfe6f49a35c89bbd2302f6001b3bc84e551a7` | HSDM | RES-66296. Files/symbols: app_v2/src/containers/my-account/MyAccountBody.tsx; app_v2/src/containers/my-account/MyAccountService.ts; symbols myAccountTabs, PasswordRenderer, classes.
- 2023-06-01 | CORE-011 | `24fadaa5b2ef430b6ddd0b780acc247942ca9a03` | HSDM | RES-66296. Files/symbols: app_v2/src/containers/my-account/MyAccountService.ts; app_v2/src/containers/my-account/MyAccountUtils.ts; symbols SettingsMenuItems, passwordMenuItems.
- 2023-06-01 | CORE-011 | `352c7d887b908102ec87ddaddba9fa165d7b195e` | HSDM | no message. Files/symbols: app_v2/src/containers/my-account/Settings/PasswordRenderer.tsx; app_v2/src/containers/my-account/Settings/TwoFactorRenderer.tsx; style/scaffold change (diff inspected).
- 2023-06-01 | CORE-011 | `45da0c27e4c15e6f4adf90aa804868473f0b76d3` | HSDM | RES-66296. Files/symbols: app_v2/src/containers/my-account/Settings/PasswordValidator.tsx; app_v2/src/containers/my-account/Settings/UpdatePasswordRenderer.tsx.
- 2023-06-01 | CORE-011 | `48b97c3ab80071622dd3c3f72dcdbd56de43043c` | HSDM | no message. Files/symbols: app_v2/src/containers/my-account/Settings/UpdatePasswordRenderer.tsx; style/scaffold change (diff inspected).
- 2023-06-01 | CORE-011 | `6908a3c1d3b4ea18d86243c03e424ded18c62778` | HSDM | RES-66296. Files/symbols: app_v2/src/containers/my-account/Settings/SettingsContainer.tsx; app_v2/src/containers/my-account/Settings/ValidateBtnRenderer.tsx; symbols updateUserData, tempUserData.
- 2023-06-01 | CORE-011 | `16db5583bb28508865d7a02321d73aac19a5a756` | HSDM | RES-66296. Files/symbols: app_v2/src/containers/my-account/MyAccountService.ts; app_v2/src/containers/my-account/MyAccountUtils.ts; symbols settingsMenuItems.
- 2023-06-02 | CORE-011 | `33051fab47b8442eda665148ec763e35e93fb8b5` | HSDM | RES-66296. Files/symbols: app_v2/src/containers/my-account/Settings/PasswordRenderer.tsx; app_v2/src/containers/my-account/Settings/TwoFactorRenderer.tsx; symbols MyAccountSettingsTest, MyAccountSettingsRenderTest, setUserDetails.
- 2023-06-02 | CORE-011 | `0aaf144bd09d42b9a3411f13c91b9195f1d4d3bf` | HSDM | RES-66296. Files/symbols: app_v2/src/containers/my-account/Settings/PasswordValidator.tsx; app_v2/src/containers/my-account/Settings/TwoFactorRenderer.tsx; symbols getPasswordHint, testArr.
- 2023-06-07 | CORE-011 | `180c4e0bf2e7a68cf03e41b4557b06e493394289` | HSDM | RES-76017 , RES-76021 , RES-76022 , RES-76023 , RES-76025 , RES-76026 , RES-76027 , RES-76063 , RES-76064 , RES-76077 , RES-76082 , RES-76084. Files/symbols: MyAccountService.ts; MyAccountStyles.tsx; symbols HelperTextValidator, passwordValue, skipPasswordPolicy.
- 2023-06-07 | CORE-033 | `776803c6472e7a684dae7ae1a4d3e36d55c19adb` | HSDM | hide eye icon. Files/symbols: app_v2/src/styles/App.css.
- 2023-06-08 | CORE-011 | `428799fa5d5862189b822295717b52c315ddc941` | HSDM | fix: Preference bugs. Files/symbols: MyAccountStyles.tsx; MyAccountUtils.ts; symbols personalInforamtionInputs, addressInformationInputs, translateLabels.
- 2023-06-08 | CORE-009 | `af775c5fe6471d20124e984aec493f9883da9d1d` | HSDM | fix: tinymce log error. Files/symbols: plugin.js; tinymce.js.
- 2023-06-08 | CORE-011 | `53e7834a85d475873851d1f9bc0b3b403927fca1` | HSDM | fix: feedback. Files/symbols: PasswordRenderer.tsx; TwoFactorRenderer.tsx; symbols setUserData, userData, passwordValue.
- 2023-06-08 | CORE-014 | `bde539746f464995b691e1b05e5e30fa78330c57` | HSDM | fix: RES-75681, RES-75915 Myaccount Integration bugs. Files/symbols: MyAccountHeader.tsx; EmailPreferenceRenderer.tsx; symbols data, setUserData.
- 2023-06-08 | CORE-011 | `e75a4373b64f1849766bef46d646c834dcc86ac2` | HSDM | fix: settings bug fix. Files/symbols: SettingsContainer.tsx; symbols setUserData.
- 2023-06-08 | CORE-014 | `608083570af18872f54c1dc739156113858ee5c3` | HSDM | fix: integration tab. Files/symbols: MyAccountHeader.tsx.
- 2023-06-08 | CORE-011 | `c7fb6f8ab5828fb1cfc5970f6aa2c4c8a174f50a` | HSDM | fix: fix. Files/symbols: MyAccountHeader.tsx.
- 2023-06-08 | CORE-011 | `dadbd200103ed17ae87eaa745a5e37b3e0d39960` | HSDM | fix: fix. Files/symbols: MyAccountHeader.tsx.
- 2023-06-09 | CORE-011 | `02bdd227164387cd79992149ad4af253e66e1bb5` | HSDM | fix: RES-76027, RES-76082, RES-76386 setiings tab bugs. Files/symbols: MyAccountHeader.tsx; MyAccountUtils.ts; symbols getFilteredApiToken.
- 2023-06-12 | CORE-007 | `79b69da43c106f3cc43679f4bbdabc5ade1e6952` | HSDM | feat: RES-74414, RES-76562 native download app. Files/symbols: DownloadNativeAppContainer.tsx; DownloadNativeAppInitiator.tsx; symbols DownloadNativeAppContainer, myAccountStyles, smScreen.
- 2023-06-12 | CORE-007 | `a0a831813642a19fd02c111730c1a6c8a38a67d3` | HSDM | feat: RES-74414, RES-76562 native download app. Files/symbols: DownloadNativeAppContainer.tsx; DownloadNativeAppInitiator.tsx; symbols nativeMenuItems, fontFamily, macosPlatforms.
- 2023-06-12 | CORE-007 | `baaefafd6b846256883e0ca4d15286bfd70a5715` | HSDM | feat: RES-74414, RES-76562 myaccount v2 redirection. Files/symbols: app.js; v2RedirectCtrl.js; symbols init, companyId.
- 2023-06-12 | CORE-011 | `bab80d85e94866e432253ac4188d80398420a075` | HSDM | fix: My account , E-sign Code Cleanup. Files/symbols: BreadCrumbs.tsx; ESignBulkListTable.tsx; symbols setDatePreference, guestInfo, obj.
- 2023-06-13 | CORE-011 | `02216d032b3290feb8963808f6f0d32595b4064c` | HSDM | fix: RES-76386 settings bug fix. Files/symbols: v2RedirectCtrl.js; MyAccountHeader.tsx; symbols companyId.
- 2023-06-13 | CORE-011 | `0b91069c8dbc498a3f0549d865f4646faddc3bd0` | HSDM | fix: RES-76386 my-account bug fixes. Files/symbols: ValidateBtnRenderer.tsx.
- 2023-06-13 | CORE-011 | `bba56529e077738c71c44d5b5880392b0b955fd9` | HSDM | fix: RES-76769 my account bugs. Files/symbols: MyAccountStyles.tsx; SettingsContainer.tsx; symbols resetVerificationCode.
- 2023-06-14 | CORE-009 | `942125471bb6e18f31e6f31cfe8baa69b446d68b` | HSDM | fix: RES-72614, RES-66602 rfpioapplystyle bugs. Files/symbols: plugin.js; tinymce.js; symbols skipLocalName, selectedTds, styleName.
- 2023-06-14 | CORE-011 | `faf2d337dd02a60c5854f71c4d9b631587177be0` | HSDM | fix: RES-76769 uat feedbacks. Files/symbols: HelpCenter.tsx; MyAccountHeader.tsx.
- 2023-06-16 | CORE-011 | `9fa9f6d46bd9e6041bbb994af568822166d38ca5` | HSDM | fix: RES-76769 myaccount uat feedbacks. Files/symbols: DownloadNativeAppContainer.tsx; MyAccountHeader.tsx; symbols mandatoryField.
- 2023-06-16 | CORE-011 | `a7680c48c0e2c2a0881c6403dec2139c8d808d52` | HSDM | fix: bugs. Files/symbols: InputsContainer.tsx.
- 2023-06-19 | CORE-009 | `12d67d8c06d9f469857a84d6831a257ba202e19f` | HSDM | fix: RES-77211 Style not updated correctly. Files/symbols: plugin.js; tinymce.js; symbols selectedBlocksInTable, newElm.
- 2023-06-19 | CORE-009 | `ff1340e35807512927564d1e0169d55d0d0fcd44` | HSDM | fix: RES-77211 Style not updated correctly. Files/symbols: tinymce.js.
- 2023-06-20 | CORE-011 | `acbdb7b054ef317ab76d1647561d915ef7f3d573` | HSDM | fix: RES-77144, RES-77163 My-account E2E bugs. Files/symbols: PasswordValidator.tsx; UpdatePasswordRenderer.tsx.
- 2023-06-21 | CORE-009 | `d1be651a67bab443733709cebd9d03627089d1ce` | HSDM | fix: RES-74657 Mini formatting toolbar bugs. Files/symbols: skin.min.css; TinyMCEUtils.ts.
- 2023-06-21 | CORE-009 | `f8f9d80e42e714268e8111dc25e56276b0f8cd1f` | HSDM | fix: RES-74657 Mini formatting toolbar bugs. Files/symbols: skin.min.css; TinyMCEUtils.ts.
- 2023-06-21 | CORE-009 | `89a2e166269f5346863ee82492ab57ce2e6bfb5f` | HSDM | fix: bug. Files/symbols: skin.min.css; TinyMCEUtils.ts.
- 2023-06-21 | CORE-011 | `943273e5463f55888866ae86ca75201fa5c131e7` | HSDM | fix: myaccount-uat feedback. Files/symbols: DownloadNativeAppContainer.tsx; MyAccountStyles.tsx.
- 2023-06-21 | CORE-037 | `4d0563587a893c74fadc7c98803ceffa271ac452` | HSDM | fix: RES-74237 Cannot read properties. Files/symbols: app/app/js/app-config.js; app_v2/src/utils/UserLoadDetailUtil.ts.
- 2023-07-04 | CORE-019 | `7534b6ee86efdb4ed3dcf5ae1ad631676cf30fa8` | HSDM | feat: RES-78346 My work discussion 2.O. Files/symbols: CommentGrid.tsx; CommentTextBottomLayer.tsx; symbols placeholderText, getChildList, childComments.
- 2023-07-05 | CORE-007 | `e19fbd12020e3ef2a6ee275cf6f77bacd1a900af` | HSDM | fix: RES-79265 Myaccount v2 redirection. Files/symbols: app.js.
- 2023-07-05 | CORE-007 | `f074233d7bb36e4369790a8989884df11b7a3b13` | HSDM | fix: RES-79265 Myaccount v2 redirection. Files/symbols: app.js.
- 2023-07-10 | CORE-019 | `ddbae3d49e4fa5da52cc7a69a71b3a538642cda6` | HSDM | feat: RES-78346 My work discussion 2.O. Files/symbols: MyWorkContainer.tsx; Discussion.tsx; symbols getEntityDetails, response, getComments.
- 2023-07-10 | CORE-019 | `e2e7521e571a6a2df2652ec9406d456100c71dcc` | HSDM | feat: RES-78346 My work discussion 2.O. Files/symbols: EmptyCommentBox.tsx; MyWorkContainer.tsx; symbols Discussion, isBusinessUnitEnabled, projectTypes.
- 2023-07-11 | CORE-019 | `471a6fd9f7734cebbccc59ad8dc0282ab6047409` | HSDM | feat: RES-78346 My work discussion unit test cases. Files/symbols: Discussion.tsx; MyworkDiscussionWrapper.tsx; symbols discussionFollowers, MyworkDiscussionWrapper, mockUserDataVO.
- 2023-07-12 | CORE-019 | `6accdcd3c1e2ac5762589ebd26b1617051ffca0e` | HSDM | fix: RES-79603, RES-79604, RES-79621, RES-79622 Discussion Story Bugs. Files/symbols: CommentGrid.tsx; EmptyCommentBox.tsx.
- 2023-07-12 | CORE-019 | `12a4bf9f7576f39bb347b0a99a66b0f6eedcc6ea` | HSDM | feat: RES-78346 My work discussion. Files/symbols: Discussion.tsx.
- 2023-07-12 | CORE-019 | `2d6e87faa0cc12acd6fd0c502a15be8cb2e99f42` | HSDM | feat: RES-78346 My work discussion unit test cases. Files/symbols: mockUserDataVO.ts; Discussion.test.tsx; symbols usersModuleMap, discussion.
- 2023-07-12 | CORE-019 | `b1dfb76320adffbced0a1beb92dadf4fa381fe9b` | HSDM | feat: RES-78346 My work discussion unit test cases. Files/symbols: {discussionMocks.ts =&gt; mockDiscussion.ts}; Discussion.test.tsx.
- 2023-07-12 | CORE-019 | `e72a3f30142548aa57a579056d760943e083900f` | HSDM | feat: RES-78346 My work discussion unit test cases. Files/symbols: Discussion.test.tsx; symbols sampleProjectName.
- 2023-07-12 | CORE-019 | `803c36931e7b9620b7b1c413b364a5d78c084c5e` | HSDM | feat: RES-78346 My work discussion unit test cases. Files/symbols: Discussion.test.tsx.
- 2023-07-13 | CORE-011 | `dbf721b0ba74a33bdd8a555c5751f3a2bd7abf41` | HSDM | fix: Data-qa for testing. Files/symbols: DisplayPreferenceRenderer.tsx; EmailPreferenceRenderer.tsx.
- 2023-07-13 | CORE-019 | `6699f716fc126b23c2da7fc4f52e595abfa255d1` | HSDM | fix: RES-79622 discussion bugs. Files/symbols: Discussion.tsx; MyWorkStyles.tsx.
- 2023-07-13 | CORE-019 | `967f1c465e2dc6d6125368a09ebb7240307fda4d` | HSDM | fix: RES-79621 discussion loading fix. Files/symbols: Discussion.tsx; symbols timeOut.
- 2023-07-14 | CORE-011 | `17180916567a7c302aefe3926362e7b100983a11` | HSDM | fix: Data-qa for testing. Files/symbols: DisplayPreferenceRenderer.tsx; EmailPreferenceRenderer.tsx.
- 2023-07-14 | CORE-009 | `ef6654b94de1d77b5e4baeede2cb1c04a5637102` | HSDM | fix: RES-77334 Applying style in table bug fix. Files/symbols: plugin.js; tinymce.js; symbols selectedBlocksInTable, tdStyledObj, childStyleObj.
- 2023-07-19 | CORE-037 | `60844f69b824816f3879a3ecd446951a35eb96a8` | HSDM | fix: RES-79421 e2e bug. Files/symbols: app_v2/src/containers/response-template/TemplateMenuRenderer.tsx; app_v2/src/utils/ErrorLogging.ts.
- 2023-07-20 | CORE-009 | `98df2e262eaab42113947b651909b5939f50cecc` | HSDM | fix: RES-80246, RES-80256 e2e bugs. Files/symbols: app-config.js; al-tags.html; symbols tempWordArray.
- 2023-07-20 | CORE-037 | `059afb49df7a1cac19eca59ca120dd5c76460327` | HSDM | fix: Error skip & RES-80292. Files/symbols: app_v2/src/containers/export/create/template/ProjectExportStyleOverride.tsx; app_v2/src/utils/ErrorLogging.ts.
- 2023-07-20 | CORE-011 | `6a9cdd35fa1ca842ee71549944ab326c9715bcf0` | HSDM | fix: RES-80598 password validator. Files/symbols: PasswordValidator.tsx.
- 2023-07-25 | CORE-012 | `156835e5aba92885b38b892ecb0e44c417c0e975` | HSDM | feat: business units initiator. Files/symbols: OrganizationContainer.tsx; BusinessUnitService.ts; symbols getAllBusinessUnitsList, response, getBusinessUnitUsersCount.
- 2023-07-25 | CORE-012 | `346ae1dec6e468be4bd812817b88f9dd5b03baac` | HSDM | feat: business units initiator. Files/symbols: CustomOrgHeader.tsx; OrganizationContainer.tsx; symbols CustomOrgHeader, commonClass, isFullScreen.
- 2023-07-26 | CORE-012 | `7535077afc6dd58276d38fe4624b6991d2620330` | HSDM | feat: RES-80727 business units manage page. Files/symbols: OrganizationStyles.tsx; OrganizationWrapper.tsx; symbols BusinessUnitCardRenderer, classes, companyUserMap.
- 2023-07-26 | CORE-012 | `06d221b53af0b899b495596e0eb8cc4be3951491` | HSDM | feat: RES-80727 business units manage page. Files/symbols: OrganizationContainer.tsx; OrganizationUtils.ts; symbols featurePreferences, orgHeaderItems.
- 2023-07-27 | CORE-012 | `efab5d37b807754c67e000d2120360c568f37275` | HSDM | feat: RES-80727 business units manage page. Files/symbols: OrgNavBar.tsx; OrganizationStyles.tsx; symbols levelList, handleChange, isBuEnabled.
- 2023-07-27 | CORE-012 | `f22b4cc3c2af2f3f041b58a759d2ffbcc55de288` | HSDM | feat: RES-80727 business units manage page. Files/symbols: OrganizationContainer.tsx; OrganizationGeneralStore.ts.
- 2023-07-28 | CORE-012 | `30aa63e5d940d024a549c89a9b43f974061e1d0b` | HSDM | feat: RES-80727 business units manage page. Files/symbols: OrgNavBar.tsx; OrganizationStyles.tsx; symbols addNewBusinessUnit, commonClasses, classes.
- 2023-07-28 | CORE-012 | `6c5b82a4233bad0567163eb241c1caf95468ea78` | HSDM | feat: RES-80727 business units manage page. Files/symbols: BusinessUnitCardRenderer.tsx; BusinessUnitMockData.ts; symbols mockBusinessUnitsList, mockUserCountMap, mockProjectCountMap.
- 2023-08-02 | CORE-012 | `f2a80d8f538f6601fd313e4b4591af626de2be6d` | HSDM | feat: RES-80727 business units manage page. Files/symbols: BusinessUnitCardRenderer.tsx.
- 2023-08-02 | CORE-012 | `8315a3faa386b1e5a5d26cefb5afc5ab66690150` | HSDM | feat: RES-80727 business units manage page. Files/symbols: HeaderCallBackRenderer.tsx; OrgNavBar.tsx; symbols HeaderCallBackRenderer, classes, selectedMenuUrl.
- 2023-08-02 | CORE-012 | `a1d798abd36e69b446f285688d1489b27de8d294` | HSDM | feat: RES-80727 business units manage page. Files/symbols: BusinessUnitCardRenderer.tsx.
- 2023-08-03 | CORE-012 | `491f67cddfff2c7ccd0d316fc36761a95759372b` | HSDM | feat: RES-80727 business units manage page. Files/symbols: HeaderCallBackRenderer.tsx. Identical patch copies: `35284b785da19bfe19eb48d80fe44c8e5905e826`.
- 2023-08-03 | CORE-012 | `3fa34122e06cc89bf45391a603f5db0c1901c81a` | branch | Revert "feat: RES-80727 business units manage page". Files/symbols: HeaderCallBackRenderer.tsx.
- 2023-08-03 | CORE-012 | `17ead68a19da8dcf0b9754d40738db34faaa7a44` | HSDM | feat: RES-80727 business units manage page. Files/symbols: HeaderCallBackRenderer.tsx; OrganizationStyles.tsx; symbols ManageBusinessUnitsHeader, userRole, classes.
- 2023-08-03 | CORE-012 | `957849ed60bc320c777f5250f4c1aabffa0f5ed0` | HSDM | feat: RES-80727 business units manage page. Files/symbols: ManageBusinessUnitsHeader.tsx.
- 2023-08-09 | CORE-012 | `ea980d6b4db1118785b69f266e087c2a025c9691` | HSDM | feat: RES-80746 Business Units - Primary and Shared users list. Files/symbols: OrganizationStyles.tsx; OrganizationUtils.ts; symbols buViewListColumnData, constructColDef, colDef.
- 2023-08-11 | CORE-012 | `9614a571d288061d3c4ef7cc81caaff8ee702939` | HSDM | feat: RES-80746 Business Units - Primary and Shared users list. Files/symbols: OrganizationStyles.tsx; BuFrameWorkComponents.tsx; symbols updateInput, usersList, tempArray.
- 2023-08-11 | CORE-012 | `182402219c3719539e726199b3c91a70e9220ded` | HSDM | feat: RES-80746 Business Units - Primary and Shared users list. Files/symbols: OrganizationStyles.tsx; BuFrameWorkComponents.tsx; symbols NameRenderer, EmailRenderer, TableHeader.
- 2023-08-11 | CORE-012 | `775bc88991978e21bc276fe8d54556b46158c55c` | HSDM | feat: RES-80746 Business Units - Primary and Shared users list. Files/symbols: OrganizationStyles.tsx; BuFrameWorkComponents.tsx; symbols classes.
- 2023-08-11 | CORE-012 | `17cd4d7b729e186d63b3713ded8183b488ca7939` | HSDM | feat: RES-80746 Business Units - Primary and Shared users list. Files/symbols: BuFrameWorkComponents.tsx; EditBUPageInitiator.tsx; symbols getShowFooter.
- 2023-08-14 | CORE-012 | `808e97c777e63baa2d636383e83a8421986f3dd2` | HSDM | feat: RES-80746 Business Units - Primary and Shared users list. Files/symbols: OrganizationStyles.tsx; BuFrameWorkComponents.tsx.
- 2023-08-14 | CORE-019 | `a282dc78a9fc2e76d16165ed36a64f909e345a34` | HSDM | fix: bug fix. Files/symbols: MyWorkQuickFilters.tsx.
- 2023-08-14 | CORE-012 | `04ab7ee10a8960d3d848c95bf109d36396afdbfc` | HSDM | fix: RES-82694, RES-82699 story bugs. Files/symbols: BusinessUnitListPage.tsx; EditBusinessUnitsPage.tsx; symbols getAllBusinessUnits, sortObjectArraybyArray, sortedArray.
- 2023-08-14 | CORE-033 | `c4a467aebf8ab22121f3c725b529bff3890a4b36` | HSDM | fix: RES-82672 bug. Files/symbols: app_v2/src/containers/organization-settings/OrganizationStyles.tsx.
- 2023-08-14 | CORE-012 | `7957408bddaf93bd07bc3cde11a11799835caf6f` | HSDM | fix: RES-82672 bug. Files/symbols: EditBusinessUnitsPage.tsx.
- 2023-08-16 | CORE-019 | `55931b6227019603cb2c915461215c3f03543b08` | HSDM | fix: RES-82492 my-work bug fix. Files/symbols: MyWorkWrapperContainer.tsx; MyWorkTaskWrapper.tsx.
- 2023-08-16 | CORE-012 | `127c21f7694eb7d08d34406aca9cd0e2658b1c75` | HSDM | fix: bug fix. Files/symbols: BusinessUnitListPage.tsx.
- 2023-08-16 | CORE-038 | `7bbf01beaf829ea002d8283a226694e7a2a5c108` | branch | fix: dev3 package.json changes. Files/symbols: app_v2/package.json.
- 2023-08-17 | CORE-037 | `bce45267201b7576a35f82f10aa77afaf43f983e` | HSDM | fix: sync. Files/symbols: app_v2/src/utils/GeneralUtils.ts.
- 2023-08-17 | CORE-012 | `5f8f043541b5c04be1c12ac4370b81f3726dce00` | HSDM | fix: RES-82779 bu-page bugs. Files/symbols: OrganizationStyles.tsx; BuFrameWorkComponents.tsx; symbols noRowsOverlayComponent, text, gridRef.
- 2023-08-17 | CORE-009 | `8ce878f12b636ceab775d41a2d87c24eaeba3ee4` | HSDM | fix: RES-77330 tinymce bug fix. Files/symbols: skin.min.css; skin.min.css.
- 2023-08-18 | CORE-013 | `d231fa4f17f4adcca8fcf1bf74bc6a9727dadc1a` | HSDM | fix: code refactor. Files/symbols: OrganizationUtils.ts; BuFrameWorkComponents.tsx; symbols isBUEdited.
- 2023-08-18 | CORE-037 | `fe1d0610205382eb3ffcce453dca8f47bfbee890` | HSDM | fix: code refactor. Files/symbols: app_v2/src/utils/GeneralUtils.ts.
- 2023-08-18 | CORE-012 | `ec0b6218e843931203bff725c4f311bd0b62058f` | HSDM | feat: RES-80746 Business Units - Primary and Shared users list. Files/symbols: OrganizationUtils.ts; BuFrameWorkComponents.tsx; symbols currentUserName, isSuperAdmin, canEdit.
- 2023-08-18 | CORE-012 | `b80643181edeefd2299932a96cbd27fd235edfe7` | HSDM | feat: RES-80746 bu bugs. Files/symbols: EditBUPageInitiator.tsx; EditBusinessUnitsPage.tsx; symbols currentUserListPage, primaryUsers, getSharedUsers.
- 2023-08-18 | CORE-012 | `7887256abcb3341b97aa5df4b23fa9f0141b7096` | HSDM | feat: RES-80746 bu bugs. Files/symbols: BuFrameWorkComponents.tsx; EditBUPageInitiator.tsx; symbols callBack, data1.
- 2023-08-18 | CORE-012 | `7ef8b1e2df73fa4e7c07fbcff186baee5774bafb` | HSDM | feat: RES-80746 bu bugs. Files/symbols: BuFrameWorkComponents.tsx; EditBUPageInitiator.tsx; symbols response.
- 2023-08-18 | CORE-012 | `8775fbee1241c0e957656b85e57e6ee95f6e7d35` | HSDM | feat: RES-80746 bu bugs. Files/symbols: EditBUPageInitiator.tsx.
- 2023-08-21 | CORE-012 | `238a0a3162e1055198be53368af5bc475848055c` | HSDM | feat: RES-80746 bu bugs. Files/symbols: CreateBUInitiator.tsx; symbols callBack, response.
- 2023-08-21 | CORE-013 | `37c4b11f26d13021051344552e4c0cec0d769f6d` | HSDM | feat: RES-80746 bu bugs. Files/symbols: OrganizationUtils.ts; BUColors.tsx; symbols canEdit.
- 2023-08-21 | CORE-009 | `ee43f6d2b29fa93149bc0e079d9adc3c45e8dd26` | HSDM | fix: RES-81276 Tinymce Custom Style bugs. Files/symbols: QuestionResponseType.tsx. Identical patch copies: `d88717b6fa175730d6231fcc097f2bb4b72ed951`.
- 2023-08-21 | CORE-009 | `625862dba83bfb122748fedb62955b7f0eca2009` | HSDM | Revert "fix: RES-81276 Tinymce Custom Style bugs". Files/symbols: QuestionResponseType.tsx.
- 2023-08-21 | CORE-009 | `5f129a77574b52a06bfc5599dc6e1648e9b3f3d1` | HSDM | fix: RES-81276 Tinymce Custom Style bugs. Files/symbols: QuestionResponseType.tsx.
- 2023-08-21 | CORE-009 | `0fb0ec955a5a0e1c810f4bfaaa0d6074adc4bbc3` | HSDM | fix: RES-81276 Tinymce Custom Style bugs. Files/symbols: QuestionResponseType.tsx.
- 2023-08-22 | CORE-012 | `d92f8ba6aabaae19669688064bfc238dbfce2177` | HSDM | feat: RES-80746 Business Units - Primary and Shared users Test cases. Files/symbols: BuFrameWorkComponents.tsx; BusinessUnitsUserDetails.tsx; symbols mockPrimaryUsers, mockSharedUsers, mockAllUsers.
- 2023-08-22 | CORE-012 | `c0bfb3f0c4759c3ad07d51ca6c2cc7e29b1fe674` | HSDM | feat: RES-80746 Business Units - Primary and Shared users Test cases. Files/symbols: mockUserDataForListPage.ts; BuFrameWork.test.tsx.
- 2023-08-22 | CORE-009 | `fdd620ac1646602b87f6893d878ffdc0a30d669f` | HSDM | fix: RES-77334 Applying style in table bug fix. Files/symbols: plugin.js; tinymce.js.
- 2023-08-22 | CORE-011 | `08232367dc930da37c1446865c2464d9b77d9413` | HSDM | fix: RES-83279 accepting a wrong value in password policy expiration notify date. Files/symbols: organization-template.html.
- 2023-08-22 | CORE-009 | `380b8e17b9a3d74b4633b840c15b5a0cdf31fcde` | HSDM | fix: RES-83244 Word count. Files/symbols: TinyMCEUtils.ts; symbols tempWordArray.
- 2023-08-23 | CORE-037 | `804b6bb16c26d35125bb3f73126ccd5092f0a498` | HSDM | fix: RES-83212 clearing notes in nps metrics. Files/symbols: app/app/js/controller/support/npsMetricsCtrl.js.
- 2023-08-23 | CORE-034 | `9a5d012958f72feb1f4d0f2c6f353d3586e32e53` | HSDM | fix: footer. Files/symbols: CompanyDetailsInitiator.tsx; RfpAdvancedFilter.tsx.
- 2023-08-24 | CORE-033 | `edaee0406e94021116ba92a9e9ff3f10fc1dc617` | HSDM | fix: adv filter. Files/symbols: app_v2/src/rfp-components/RfpAdvancedFilter.tsx.
- 2023-08-24 | CORE-009 | `8e69e48700e1520f8486984eae4a734f729420de` | HSDM | fix: RES-76346 Format painter does not take effect when applied. Files/symbols: plugin.js; tinymce.js; symbols tempStyleMap, tempBlockStyleMap.
- 2023-08-24 | CORE-009 | `8ac3174b9da2ce6698e5e14fdc66610298a129e0` | HSDM | fix: RES-76346 Format painter does not take effect when applied. Files/symbols: plugin.js; tinymce.js.
- 2023-08-31 | CORE-011 | `16697a6d821ddbabf762eb3023e94e03918ac97b` | HSDM | fix: RES-83745 Domain and Ip restriction. Files/symbols: SecurityPropsType.ts; LoginSettingsStore.ts; symbols DomainRestriction, headerStyle, commonStyles.
- 2023-08-31 | CORE-013 | `bd7cdd0642d7c166462e5e05b9872b630cc62ccb` | HSDM | fix: RES-83745 Domain and Ip restriction. Files/symbols: OrganizationWrapper.tsx; OrganizationWrapperBodyRenderer.tsx; symbols classes, updateCompanyPreference.
- 2023-09-01 | CORE-013 | `7bc49ba5f0e31ce1c84cfab6635d66cd98331c1c` | HSDM | fix: RES-83745 Domain and Ip restriction. Files/symbols: OrganizationWrapper.tsx; IpRestrictionChipRenderer.tsx; symbols showFooter, userDetails, setUserDetails.
- 2023-09-01 | CORE-011 | `0fc21db7a613a0ad8e0f34728885745310cf69dd` | HSDM | fix: RES-83745 Domain and Ip restriction. Files/symbols: DomainRestriction.tsx; DomainRestrictionBodyRenderer.tsx; symbols DomainIPRestrictionMockData, DomainIpRestrictionTest, DomainIpPageTest.
- 2023-09-01 | CORE-011 | `2890d019f594019c5068abe3d38522a608944119` | HSDM | fix: RES-83745 Domain and Ip restriction. Files/symbols: DomainRestriction.tsx; DomainRestrictionBodyRenderer.tsx.
- 2023-09-04 | CORE-011 | `d10eabd0b551cb0cc3e1faaaeb1796f7b1ea67dc` | HSDM | fix: RES-83745 Domain and Ip restriction. Files/symbols: DomainRestriction.tsx; DomainRestrictionBodyRenderer.tsx; symbols filteredList, tempArray, addressArray.
- 2023-09-04 | CORE-011 | `827286829360340eb145ad9c546bcab9377aea39` | HSDM | fix: RES-83745 Domain and Ip restriction. Files/symbols: LoginSaveComponent.tsx; SecurityStyles.tsx; symbols theme.
- 2023-09-04 | CORE-011 | `41051564c45b0cdb9c37ff09b9a8a99b3c32a3e0` | HSDM | fix: RES-83745 Domain and Ip restriction. Files/symbols: DomainRestrictionBodyRenderer.tsx; IpRestrictionBodyRenderer.tsx; symbols chipsArray, domainChipRenderer, domainInput.
- 2023-09-04 | CORE-013 | `f53a8bee8b823cde87eaf8035dc5353ba3b2722a` | HSDM | fix: RES-83745 Domain and Ip restriction. Files/symbols: OrganizationContainer.tsx; OrganizationWrapper.tsx.
- 2023-09-05 | CORE-011 | `0e6443c10840addcab3df8439323ddfa7df34993` | HSDM | feat: RES-83745 Domain and Ip restriction. Files/symbols: LoginSettingsContainer.tsx.
- 2023-09-06 | CORE-011 | `3d5aa75a9afba18d8618c3bb6484263966b4cad7` | HSDM | fix: RES-85198, RES-85200, RES-85202, RES-85199, RES-85213, RES-85210 IP & Domain Restriction bugs. Files/symbols: DomainRestrictionBodyRenderer.tsx; IpRestrictionBodyRenderer.tsx.
- 2023-09-06 | CORE-011 | `3b124ee8ba7e21b271016079bb981fd19b965761` | HSDM | fix: RES-85198, RES-85200, RES-85202, RES-85199, RES-85213, RES-85210 IP & Domain Restriction bugs. Files/symbols: IpRestrictionBodyRenderer.tsx; IpRestrictionChipRenderer.tsx.
- 2023-09-07 | CORE-011 | `1e29f6cd9e499b486e834a50218301797633f745` | HSDM | fix: RES-85471, RES-85213 ip bugs. Files/symbols: DomainRestrictionBodyRenderer.tsx; LoginSaveComponent.tsx.
- 2023-09-07 | CORE-011 | `296e7e17f419f48c450e515938be5c5ac6fb7ad2` | HSDM | fix: RES-85471, RES-85213 ip bugs. Files/symbols: LoginSaveComponent.tsx.
- 2023-09-08 | CORE-011 | `a0cf6a792c02e5582b38d19e95fe6329557606da` | HSDM | feat: RES-83739 Login methods. Files/symbols: SecurityTabHeader.tsx; LoginSaveComponent.tsx; symbols tempSaml, updateInput, setInitSaml.
- 2023-09-08 | CORE-033 | `6ec8c1ce50136e0b014e99f680b72e221b8b4e22` | HSDM | feat: circular dependencies. Files/symbols: app_v2/src/components/dialogModels/RespondProject/SaveAsProjectTemplateDialog.tsx; app_v2/src/containers/content-analysis/compliance-matrix-requirements/MatrixGridCellRenderer.tsx; symbols toolBarStyles, ProjectDueDate, classes.
- 2023-09-08 | CORE-011 | `0be86f201e2bc1f4e47a8344b5aa4a35fea26467` | HSDM | feat: RES-83739 Login methods. Files/symbols: DomainRestrictionBodyRenderer.tsx; LoginSettings.tsx; symbols addDomainToList.
- 2023-09-08 | CORE-037 | `0d46d2b64cff2fd93ad9c86768e4471816056dd9` | HSDM | feat: RES-84089 - Proposals CR's - Basic Info. Files/symbols: app_v2/src/containers/proactive-proposal-builder/manage-proposal/ManageProposalTableView.tsx.
- 2023-09-10 | CORE-011 | `271dc68e3c596790e7b93c5f3466488a527a5278` | HSDM | feat: RES-83739 Login methods. Files/symbols: SecurityTabHeader.tsx; LoginItemRenderer.tsx; symbols ItemRenderer, classes, commonStyles.
- 2023-09-11 | CORE-011 | `ce7b10ba8beb2baf0169ab30b78cb19119a19f37` | HSDM | feat: RES-83739 Login methods. Files/symbols: IpRestrictionBodyRenderer.tsx.
- 2023-09-11 | CORE-011 | `3dd9204a0ad7388db5f349eb05a5c5959834f842` | HSDM | fix: RES-85467 added debounce in Rfptextfield for org settings. Files/symbols: DomainRestrictionBodyRenderer.tsx; RfpTextField.tsx.
- 2023-09-11 | CORE-011 | `42d9ae81f57f17e7e9f372fae28140ada4f4b42c` | HSDM | fix: RES-85628, RES-85625, RES-85626 login method bugs. Files/symbols: LoginItemRenderer.tsx; LoginPasswordPaneRenderer.tsx; symbols theme, loginMethodsMenuItems, getloginMethodsMenuItems.
- 2023-09-11 | CORE-011 | `784ea39ecdd32c3eae5db62fbe6982b5d189f5b1` | HSDM | fix: RES-85628, RES-85625, RES-85626 login method bugs. Files/symbols: LoginSaveComponent.tsx; LoginSettingsStore.ts; symbols passwordPolicy.
- 2023-09-12 | CORE-011 | `5b5dfafbf8ea42548e231fe3d847346d76a8882b` | HSDM | feat: RES-83750 Session and BYOK. Files/symbols: OtherSecurityInitiator.tsx; ByokBody.tsx; symbols ByokBody, commonStyles, classes.
- 2023-09-12 | CORE-011 | `c3d24e514d8621f53645097a9b9c4b132419412d` | HSDM | fix: RES-85702, RES-85751, RES-85747 login , sso bugs. Files/symbols: SecurityTabHeader.tsx; LoginItemRenderer.tsx; symbols toggleEnabled, companyPreferences, integrationCallBack.
- 2023-09-12 | CORE-011 | `00dd013c55ee4e2aafcc33436f13654aaa974f57` | HSDM | fix: RES-85702, RES-85751, RES-85747 login , sso bugs. Files/symbols: SCIMContainer.tsx; SSOContainer.tsx.
- 2023-09-12 | CORE-011 | `545ccb519335969a389c1645da51e35524d02ec2` | HSDM | fix: RES-85702, RES-85751, RES-85747 login , sso bugs. Files/symbols: SCIMContainer.tsx; SSOContainer.tsx.
- 2023-09-12 | CORE-011 | `c5049a41f00c20055a2ce12eff8f9402d0aeed28` | HSDM | fix: RES-85753 password policy. Files/symbols: LoginSettingsContainer.tsx.
- 2023-09-13 | CORE-011 | `63eec99cb7e1640db7fa6a3ee3c1278e1043187c` | HSDM | feat: RES-83750 Session and BYOK. Files/symbols: OtherSecurityInitiator.tsx; ByokBody.tsx; symbols byokKey, byokEditKey, isValidKMSKey.
- 2023-09-13 | CORE-011 | `f6a9fee1aad0b8dc3641fcbd299f18a998075c8e` | HSDM | feat: RES-83750 Session and BYOK. Files/symbols: organizationCtrl.js; ByokBody.tsx; symbols validateKMSKey, response, updateKMSKey.
- 2023-09-13 | CORE-011 | `9ed650bb56d816a3bc5964820453074c763c2fed` | HSDM | feat: RES-83750 Session and BYOK. Files/symbols: MyAccountUtils.ts; ByokBody.tsx; symbols skipPasswordPolicy, byokKey, showByok.
- 2023-09-14 | CORE-011 | `1655b2dc50a8a0e9a7ba325bdab7d90411a7cfa0` | HSDM | feat: sso. Files/symbols: SSOScimInitiator.tsx; SSOContainer.tsx.
- 2023-09-14 | CORE-019 | `c351e620bf16d61af112818bcde6b3f020c3336b` | HSDM | fix: RES-85984 discussion child count. Files/symbols: CommentUtils.ts; Discussion.tsx; symbols getChildList, childComments, getMyWorkChildList.
- 2023-09-14 | CORE-011 | `15ddb733f2fef7d373377c4dec2fec607c6c2bac` | HSDM | feat: RES-83750 Session and BYOK. Files/symbols: ByokBody.tsx.
- 2023-09-14 | CORE-011 | `fc4eb4b29283095a54846891fd73cf83c9946cb3` | HSDM | feat: sso. Files/symbols: SSOScimInitiator.tsx; SSOContainer.tsx; symbols classes.
- 2023-09-14 | CORE-011 | `801e58fa6fdd8fff3d2ae76ca2404a4b5d564031` | HSDM | feat: RES-83750 Session and BYOK. Files/symbols: ByokBody.tsx; OtherSecuritySaveComponent.tsx.
- 2023-09-14 | CORE-011 | `40d9ea3501c77458a1c70dcddb7096eeeebaa421` | HSDM | feat: RES-83750 Session and BYOK. Files/symbols: OtherSecuritySaveComponent.tsx; symbols updateByokKey, updateKmsKey.
- 2023-09-14 | CORE-011 | `bf90a4dbbbc6a89facdf86680c2d9759fc1ce698` | HSDM | feat: RES-83750 Session and BYOK. Files/symbols: SecurityService.tsx.
- 2023-09-15 | CORE-011 | `da7d3e1b5df18abf4600529f9cabf679012351a0` | HSDM | feat: sso. Files/symbols: OtherRenderers.tsx; SSOListItemBodyRenderer.tsx; symbols classes.
- 2023-09-15 | CORE-011 | `b9f77b414b3fe12f22a339ed9e549ddf2479b0f6` | HSDM | fix: RES-86129 byok bug. Files/symbols: OtherSecuritySaveComponent.tsx.
- 2023-09-15 | CORE-011 | `6af1398eea1b221b341f189a87fbf7f627f6d8ef` | HSDM | feat: sso. Files/symbols: BusinessunitAndRoles.tsx; SaveCancelContainer.tsx.
- 2023-09-15 | CORE-011 | `6d4e2ae3651377b05cf18803c1b2435334d48627` | HSDM | feat: sso. Files/symbols: BusinessunitAndRoles.tsx; SecurityStyles.tsx.
- 2023-09-15 | CORE-011 | `d9a005f5cf6600febc6dba3615b4c0498cbf27b2` | HSDM | feat: sso. Files/symbols: LoginSettingsContainer.tsx; OtherRenderers.tsx; symbols classes.
- 2023-09-15 | CORE-011 | `555117b51bbe3b1889be1e5386dc7a0ca8a9de9c` | HSDM | fix: RES-86164 BYOK bugs. Files/symbols: OtherSecurityContainer.tsx; OtherSecuritySaveComponent.tsx; symbols SaveCancelComponent.
- 2023-09-15 | CORE-011 | `5c848058cc18c94d9d81d9116d419a39fb76e93f` | HSDM | feat: sso. Files/symbols: TextFieldRenderer.tsx; SecurityUtils.ts; symbols handleUploadClick, file, reader.
- 2023-09-19 | CORE-009 | `c3039a886d313129f2ca03b948b1af3925a05f70` | HSDM | fix: RES-85417 tinymce clipboard content bug fix. Files/symbols: plugin.js; symbols hasTextContent.
- 2023-09-19 | CORE-009 | `1ca46c80b6844bceaf664f39d041ed812d52fd5a` | HSDM | fix: RES-85642 tinymce custom style prod error. Files/symbols: TinyMCECustomStyles.tsx; symbols result.
- 2023-09-19 | CORE-011 | `0f0284b5edbd70bcf83ab24a78cfc86ded7097aa` | HSDM | fix: RES-86363 sso multiline textarea bug fix. Files/symbols: TextFieldRenderer.tsx.
- 2023-09-21 | CORE-011 | `cab97f7f7571fbd3ed3edcb1a936385265c7a2ab` | HSDM | feat: RES-83777 SSO Unit Test Case. Files/symbols: SSOListItemBodyRenderer.tsx; SSOListItemRenderer.tsx; symbols SamlSsoMockdata, getLicenseCount, getLicenseCountHelper.
- 2023-09-21 | CORE-011 | `7b4cf6f73ccc44094a391d32b0510f8f46445353` | HSDM | feat: RES-83777 SSO Unit Test Case. Files/symbols: SamlOAuth.test.tsx; symbols ssoType, name.
- 2023-09-21 | CORE-011 | `97c0ff76916a41550954a6e11aa5f6311ef9522c` | HSDM | feat: RES-83777 SSO Unit Test Case. Files/symbols: SamlOAuth.test.tsx; symbols updateSamlSSO, updateSamlSSOHelper, saveButton.
- 2023-09-22 | CORE-011 | `eeaffce3b906fffb22ec188d0ff14bf34dad7951` | HSDM | feat: RES-83777 SSO Unit Test Case. Files/symbols: SamlOAuth.test.tsx; symbols samlCard, cardContent.
- 2023-09-25 | CORE-001 | `25fd635a58371f168b23d7837df463fbf82cf263` | HSDM | feat: app launcher cleanup. Files/symbols: AppLauncher.tsx; FooterWrapper.tsx; symbols menuItems, classes, currentUserInfo.
- 2023-09-25 | CORE-001 | `34581deb48be552c74474378b53386adbde7402d` | HSDM | feat: app launcher cleanup. Files/symbols: ManageProfileStyles.tsx; PreviewContentHeader.tsx.
- 2023-09-25 | CORE-001 | `9f65d0438d2dd03413deaeef949e0faf3398387b` | HSDM | feat: RES-87130 App Launcher. Files/symbols: HeaderWrapper.tsx; HeaderLayout.tsx; symbols HeaderWrapper.
- 2023-09-26 | CORE-019 | `eb9f943f6a7c3b6a845e3c0a0d2ee52faecfb17d` | HSDM | fix: RES-87461 My work/E sign - Circular Dependency. Files/symbols: ESignDocumentList.tsx; ESignDownloadDialogWrapper.tsx; symbols DownloadDialog, DownloadDialogWrapper, handleChange.
- 2023-09-27 | CORE-001 | `3dbf1876457d593c511b8de73069fdad87ad6adb` | HSDM | feat: RES-87130 App Launcher. Files/symbols: AppLauncher.tsx; SendFeedback.tsx; symbols AppLauncher, classes, localUXPref.
- 2023-09-29 | CORE-001 | `f2225414680f968f090a5cf20c67004adf9d91d9` | HSDM | feat: RES-87130 App Launcher. Files/symbols: AppLauncher.tsx; AvatarMenu.tsx; symbols AppLauncher, classes, localUXPref.
- 2023-09-29 | CORE-001 | `e4c1d4856ecd431543294eb1ba091df83b90d0f9` | HSDM | feat: RES-87130 App Launcher. Files/symbols: AppLauncher.tsx; AvatarMenu.tsx.
- 2023-10-03 | CORE-001 | `6e52d674183c05a79d47a9631682a9965623cfad` | HSDM | feat: RES-87130 App Launcher. Files/symbols: AppLauncher.tsx; HelpCenter.tsx; symbols customClass.
- 2023-10-03 | CORE-001 | `40b135296be461f648cc28341702be3f74d24bf2` | HSDM | feat: RES-87130 App Launcher. Files/symbols: HelpCenter.tsx.
- 2023-10-03 | CORE-001 | `2149af6e04e7a9f4b9f158643348fc6acbe31b0e` | HSDM | feat: RES-87130 App Launcher. Files/symbols: FooterWrapper.tsx; HelpAndContact.tsx; symbols params, darkModeFilterModules.
- 2023-10-03 | CORE-001 | `65621f19f46bc19afcdd98ac5e36b105e4bab76a` | HSDM | feat: RES-87130 App Launcher. Files/symbols: AppLauncher.tsx; AvatarMenu.tsx; symbols urlPrefix, userDetails, companyPolicy.
- 2023-10-04 | CORE-001 | `acca85717b59ed929643e04a13fafea6eb905380` | HSDM | feat: RES-87130 App Launcher. Files/symbols: ManageProfileHeader.tsx.
- 2023-10-04 | CORE-001 | `1bccfaf61d00fe0c73caa832749832b24957008c` | HSDM | feat: RES-87130 App Launcher. Files/symbols: AppLauncher.tsx; AvatarMenu.tsx.
- 2023-10-04 | CORE-001 | `28813b310fc14a35e3cd26289d8ab8ce4c0bfa5d` | HSDM | feat: RES-87130 App Launcher. Files/symbols: ContentLibrarySavedSearch.tsx.
- 2023-10-04 | CORE-001 | `a5805ba0a65bca3cd812e2a783ce0ad6a4e63426` | branch | fix: RES-88218, RES-88219, RES-88224 app launcher bugs. Files/symbols: AppLauncher.tsx; AvatarMenu.tsx; symbols darkModeFilterModules, UI_V2_STRICT.
- 2023-10-04 | CORE-001 | `2b4f0ca973ece4826ceeb572d31066afd248d481` | HSDM | feat: RES-87130 App Launcher. Files/symbols: HeaderWrapperUtils.ts; ReturnToClassicUI.tsx; symbols darkModeFilterModules, UI_V2_STRICT.
- 2023-10-05 | CORE-001 | `053dbad4240c64606f42fca84c68456b41061446` | HSDM | feat: RES-87130 App Launcher. Files/symbols: AvatarMenu.tsx; FooterWrapper.tsx; symbols isProjectPage, isManageProject, url.
- 2023-10-05 | CORE-001 | `630d4aab5c7f30b2d68b46bbbccfec15d9666344` | branch | fix: RES-88372 notification queue bugs. Files/symbols: AvatarMenu.tsx; symbols isManageProject, url, menuUrl.
- 2023-10-05 | CORE-001 | `e4f92438c43bd9369f85435c249676c4c0925b45` | branch | fix: App launcher for org settings. Files/symbols: OrganizationHeader.tsx.
- 2023-10-06 | CORE-001 | `b297267f99aebb200680f4cdcb9021a2e128f24a` | HSDM | feat: RES-87130 App Launcher. Files/symbols: HeaderWrapperStyles.tsx; HelpAndContact.tsx; symbols HelpCenterSupport, classes, isSupportAccessDialogOpen.
- 2023-10-06 | CORE-019 | `2260ebc485f0a1a0096f7450b7313d031cdc844a` | branch | fix: My work popper issue. Files/symbols: HeaderWrapperUtils.ts; CalendarSyncPopup.tsx; symbols UI_V2_STRICT.
- 2023-10-09 | CORE-019 | `084e00c8c5659effbe93d0009da2a98f2a312c66` | HSDM | feat: RES-87214 My work dark mode. Files/symbols: CommentGrid.tsx; CommentTextBottomLayer.tsx; symbols mModules, MyWorkCommonStyles, colorStyles.
- 2023-10-09 | CORE-019 | `b4d6c83f7e8121fc9ce00af015d58038fd9eb6fc` | HSDM | feat: RES-87214 My work dark mode. Files/symbols: CommentTextBottomLayer.tsx; NotificationCardRenderer.tsx.
- 2023-10-09 | CORE-034 | `700f411b8a3d5d109e3d41ac861adaed553c7ed1` | branch | fix: rfpio university translate change. Files/symbols: HeaderWrapperUtils.ts.
- 2023-10-09 | CORE-001 | `f02a76a73b8aff9be040d1dc67420fa6d7612559` | HSDM | feat: RES-87130 App Launcher. Files/symbols: MyAccountPermissionDrawer.tsx.
- 2023-10-09 | CORE-001 | `9bdeab36cea83b962f2ae1d499ee9369ca5c7a19` | HSDM | feat: RES-87130 App Launcher. Files/symbols: HeaderWrapperStyles.tsx; HelpCenterSupport.tsx; symbols theme.
- 2023-10-09 | CORE-001 | `dac17f51f3841e4d94f88011f43219a8bb5a3855` | HSDM | feat: RES-87130 App Launcher. Files/symbols: generated/dependency/empty metadata; no original feature inference.
- 2023-10-09 | CORE-019 | `78862c5f469a8f16e2e88568ad08de87d10e9f09` | HSDM | fix: RES-88629 My work dark mode bug fix. Files/symbols: MyWorkStyles.tsx; MyWorkQuickFilters.tsx; symbols radioStyles.
- 2023-10-10 | CORE-019 | `76e276dc8b316e180d4334e431ced8d380329eaa` | HSDM | fix: RES-88629 My work dark mode bug fix. Files/symbols: MyWorkQuickFilters.tsx; PreviewMailAndDeleteDialog.tsx.
- 2023-10-10 | CORE-019 | `93c66c3db15033f1a3d425e762031337b1d0a410` | HSDM | fix: RES-88629 My work dark mode bug fix. Files/symbols: MyWorkTaskWrapper.tsx; symbols colorStyles.
- 2023-10-10 | CORE-001 | `cade28e48951763ca2fb1fa5816f338f963c5197` | HSDM | feat: RES-87130 App Launcher. Files/symbols: AppLauncher.tsx.
- 2023-10-10 | CORE-001 | `9f27d6a45ac32abc8e8f71daacd5343018109f2b` | HSDM | feat: RES-87130 App Launcher. Files/symbols: AvatarMenu.tsx; HeaderWrapperUtils.ts; symbols UI_V2_STRICT.
- 2023-10-10 | CORE-001 | `9c6fdc3f94fc1030eb4ca8915cc9c40249cc8e59` | branch | feat: RES-87130 App Launcher. Files/symbols: AppLauncher.tsx; AvatarMenu.tsx; symbols isProjectPage, HelpCenter, classes.
- 2023-10-10 | CORE-001 | `9328a7f709f8fc953617f8b5e40d17fdd46d523e` | branch | feat: RES-87130 App Launcher. Files/symbols: IntakeContainer.tsx; AddProfileContentDrawer.tsx.
- 2023-10-10 | CORE-001 | `7161f3aabc8693fb215e54496fe76d4bacd12a36` | HSDM | feat: RES-88732 Remove Project Header link and "Return to Classic" button. Files/symbols: ContentLibraryTaskRenderer.tsx; MyWorkTaskRenderer.tsx; symbols finalList, isContentLibTask.
- 2023-10-12 | CORE-014 | `13210bb257008712360674c37465a50929ac8f59` | HSDM | fix: RES-87373 Integrations - Collaboration - Highspot. Files/symbols: OrgLoader.tsx; IntegrationListContainer.tsx; symbols OrgLoader, classes, commonStyles.
- 2023-10-12 | CORE-014 | `e1bb48647c1a5f14a761388ca34fed32fd1b9a57` | HSDM | fix: RES-87373 Integrations - Collaboration - Highspot. Files/symbols: HighspotPopper.tsx; IntegrationPropsType.ts; symbols HighspotPopper.
- 2023-10-12 | CORE-014 | `183fc901aca2730226b1fd8f5ca5348714040c24` | HSDM | feat: RES-87373 Integrations - Collaboration - Highspot. Files/symbols: IntegrationListContainer.tsx; HighspotContainer.tsx; symbols connectToHighspot.
- 2023-10-12 | CORE-014 | `e4db4eea63547bc985aca7cb297ebbecbfa3599f` | HSDM | feat: RES-87373 Integrations - Collaboration - Highspot. Files/symbols: IntegrationListContainer.tsx; MSDynamicsCRMContainer.tsx; symbols MSDynamicsCRMContainer, HighspotContainer.
- 2023-10-12 | CORE-014 | `f3c024ab54518b2941e76a93a10c11a510952a47` | HSDM | feat: RES-87373 Integrations - Collaboration - Highspot. Files/symbols: IntegrationListContainer.tsx; HighspotContainer.tsx; symbols integrationCallBack, tempObj, tempArray.
- 2023-10-12 | CORE-014 | `c2ee9ab85d332f16024921f32fe9ecc43427d682` | HSDM | feat: RES-87373 Integrations - Collaboration - Highspot. Files/symbols: IntegrationListContainer.tsx; HighspotContainer.tsx; symbols tempArr.
- 2023-10-12 | CORE-014 | `455493b7451fe119428595d76a36812a8fff4bef` | HSDM | feat: RES-87373 Integrations - Collaboration - Highspot. Files/symbols: HighspotContainer.tsx.
- 2023-10-13 | CORE-001 | `0b4e16e313bc66d89baac7d5156c389f430a565b` | HSDM | feat: RES-87130 App Launcher. Files/symbols: AppLauncher.tsx; AvatarMenu.tsx; symbols userDetails, companyPolicy, checkPinned.
- 2023-10-13 | CORE-012 | `2fdec23488cd53c67d1a8593f1d31befd17d91ab` | HSDM | fix: RES-89099, RES-89100 High Spot bugs. Files/symbols: PreferenceContainer.tsx; IntegrationListContainer.tsx.
- 2023-10-13 | CORE-011 | `0a8ea0662a0e1940453d07a4a66519a4c40c5890` | HSDM | fix: RES-89099, RES-89100 High Spot bugs. Files/symbols: SecurityTabHeader.tsx.
- 2023-10-16 | CORE-009 | `3bf5c178671b5de4e07f1f55e7715d34dece7413` | HSDM | fix: RES-89211 Rich text Image edit bug fix. Files/symbols: plugin.js.
- 2023-10-16 | CORE-009 | `051b0aea2118434ca6bcc13d426f7ca13afc8652` | HSDM | fix: RES-71163 Plain paste bug fix. Files/symbols: plugin.js; tinymce.js.
- 2023-10-16 | CORE-019 | `8f667eaf0fcfb651a62999f9600d02cfa19d6370` | HSDM | fix: Revert discussion code changes. Files/symbols: Discussion.tsx.
- 2023-10-17 | CORE-019 | `02b7fcdd09b2b22bfd4cd3b3e70a7b86e740432e` | HSDM | fix: RES-88171 discussion delete count bug fix. Files/symbols: Discussion.tsx; symbols updateDiscussionObject, tempAllDiscussions, filteredComments.
- 2023-10-20 | CORE-019 | `2d7ac0a809ab8f05c84d41abd133156a36826f5d` | branch | fix: Discussion redux fix. Files/symbols: Discussion.tsx; symbols updateDiscussionObject, tempAllDiscussions, filteredComments.
- 2023-10-20 | CORE-019 | `44af246f0d1b855f9d5c260eb21d5513af0f3824` | branch | fix: Discussion redux fix. Files/symbols: Discussion.tsx; DiscussionReducer.ts; symbols updateDiscussionObject, updateHideReplies, entry.
- 2023-10-20 | CORE-019 | `1d7eaf857fd43ea24bc95efc627f2eb5698880ca` | branch | fix: Discussion redux fix. Files/symbols: Discussion.tsx.
- 2023-10-25 | CORE-011 | `122c3f34cb791c325cebe9f4f9dd6755a2cfead1` | HSDM | feat: RES-85079 My Account - Security Empty State. Files/symbols: MyAccountHeader.tsx; SettingsContainer.tsx; symbols commonThemeClasses, SettingsEmptyState, classes.
- 2023-10-25 | CORE-011 | `0ca27b5fd9826eab65bd66fb6b7251ed51eb0234` | HSDM | feat: RES-85079 My Account - Security Empty State. Files/symbols: SettingsEmptyState.tsx.
- 2023-10-25 | CORE-011 | `d2d91d054df0c90b275823f768ccd6957d304e5d` | HSDM | feat: RES-85079 My Account - Security Empty State. Files/symbols: SettingsEmptyState.tsx.
- 2023-10-26 | CORE-001 | `b887ce5cf6d12eb10c074aff38ec921d8eabf308` | HSDM | fix: conflict resolve. Files/symbols: AvatarMenu.tsx; HeaderWrapperStyles.tsx; symbols menuStyles.
- 2023-11-01 | CORE-007 | `a6ae3a470e2df81c4a122861351bef817b8b8679` | HSDM | fix: RES-90988 profile guest login issue. Files/symbols: PreviewContentHeader.tsx; PreviewProfileHeader.tsx. Identical patch copies: `53a13c67718945838ec66c35e04d98ba8dcffe32`.
- 2023-11-01 | CORE-007 | `54dff0da0f43632b14e632ccc6fb8b790d960576` | HSDM | Revert "fix: RES-90988 profile guest login issue". Files/symbols: PreviewContentHeader.tsx; PreviewProfileHeader.tsx.
- 2023-11-01 | CORE-001 | `9285e64bfd4928cfcef8922c2b3d85289efa091a` | HSDM | fix: RES-90039 Side Nav - CCL. Files/symbols: AvatarMenu.tsx; ContentLibraryHomePage.tsx; symbols badgeCount, setNotificationBadgePage, classes.
- 2023-11-02 | CORE-001 | `cdff0b4d5b8450bcebb8248b4144b1c32b6cddd9` | HSDM | feat: RES-90039 Side Nav. Files/symbols: ContentLibraryHomePage.tsx; ContentLibraryNavigationPane.tsx; symbols isTabletView, mdScreen, CCLHamBurgerMenu.
- 2023-11-02 | CORE-001 | `9491f7b8768b06957271750107228ebe12645f28` | HSDM | feat: RES-90039 Side Nav. Files/symbols: LinkedContentSubscriptionPopover.tsx; CCLHamBurgerMenu.tsx; symbols translationQueObj, limit, isInvitedVendor.
- 2023-11-03 | CORE-001 | `7c2910a5724e1f9b69032a33d767cbe66de82993` | HSDM | fix: RES-91192 In safari browser, unable to navigate to profiles using App launcher. Files/symbols: AppLauncher.tsx.
- 2023-11-03 | CORE-001 | `5ca63f14b290c36fcfa14e192db96ff8ce4c9aa1` | HSDM | feat: RES-90039 Side Nav. Files/symbols: CCLHamBurgerMenu.tsx.
- 2023-11-03 | CORE-001 | `cf556146ea51cde2219998106f30e582d2bf4cd0` | HSDM | feat: RES-90039 Side Nav. Files/symbols: RfpHamBurgerMenu.tsx; symbols timer.
- 2023-11-03 | CORE-001 | `137b7d546ae3d5604622b8d962008d8872d92172` | HSDM | feat: RES-90039 Side Nav. Files/symbols: ContentLibraryHomePage.tsx; LinkedContentSubscriptionPopover.tsx; symbols LinkedContentSubscriptionPopover, currentTab, TranslationQueuePopup.
- 2023-11-06 | CORE-001 | `443f7b6be9634825046da7cbedea27a9ea3ecdaf` | HSDM | feat: RES-90039 Side Nav. Files/symbols: ContentLibraryNavigationPane.tsx; CCLHamBurgerMenu.tsx; symbols statusFilter.
- 2023-11-06 | CORE-011 | `b3af724de0de62f6b0916fb747b57263c040cdcc` | HSDM | feat: RES-85079 - My Account - Security tab UAT feedbacks. Files/symbols: SettingsEmptyState.tsx.
- 2023-11-06 | CORE-001 | `baf8e9e7e27d39ae5fc74aa682bf4b550ea82f42` | HSDM | feat: RES-90039 Side Nav. Files/symbols: RfpHamBurgerMenu.tsx.
- 2023-11-06 | CORE-001 | `f38020633be22acc771ffd98f3f237d5ead65f83` | HSDM | feat: RES-90039 Side Nav. Files/symbols: RfpHamBurgerMenu.tsx.
- 2023-11-06 | CORE-001 | `8da1411293f1630d8c2149f1396cee7f411c7ea2` | HSDM | feat: RES-90039 Side Nav. Files/symbols: RfpHamBurgerMenu.tsx.
- 2023-11-06 | CORE-001 | `7a7b21f630dc9def19cab7c38b36cc1e3d1da39b` | branch | feat: arabic. Files/symbols: HeaderAdornment.tsx; HeaderWrapper.tsx; symbols rightDirection, setRightDirection, changeDirection.
- 2023-11-06 | CORE-001 | `3a37c06fad379ed01c4bb29d4da479734033012d` | HSDM | feat: RES-90039 Side Nav. Files/symbols: RfpHamBurgerMenu.tsx.
- 2023-11-06 | CORE-001 | `d4c21c4829220ee8714a6adccf1a24fe74bda56e` | HSDM | feat: RES-90039 Side Nav. Files/symbols: RfpHamBurgerMenu.tsx.
- 2023-11-07 | CORE-018 | `35ee673179403ed8eb27fd9b4ce26c44d9eac2d9` | HSDM | fix: RES-91421 Subscribed content Popper issue. Files/symbols: LinkedContentSubscriptionPopover.tsx; TranslationQueuePopup.tsx.
- 2023-11-07 | CORE-018 | `d44d9c6de1b4cd58ffabb067953d62f47d515a52` | HSDM | fix: RES-91421 Subscribed content Popper issue. Files/symbols: TranslationQueuePopup.tsx.
- 2023-11-09 | CORE-014 | `e3ab6c5f92dca4109099041cbb1264c8c1261e28` | HSDM | feat: RES-90071 Google tag manager, Generic script injection 2.0 UX. Files/symbols: CommonCollabContainer.tsx; IntegrationListContainer.tsx; symbols CommonCollabContainerObject, CommonCollabContainer, commonStyles.
- 2023-11-09 | CORE-014 | `256daa04fa79cf2afbcc3256d9616dfb71787478` | HSDM | feat: RES-90071 Google tag manager, Generic script injection 2.0 UX. Files/symbols: CommonCollabContainer.tsx.
- 2023-11-09 | CORE-001 | `d590ac2b349903c839ce6b737c67847a401b7e53` | HSDM | fix: App launcher issues. Files/symbols: ManageProfileStyles.tsx; BuildProfileHeader.tsx.
- 2023-11-15 | CORE-014 | `dae22bf665372e6477d83eed1f8731d059f42f7a` | HSDM | fix: RES-91761, RES-91772, RES-91773, RES-91786 salesforce bugs. Files/symbols: CommonCollabContainer.tsx; IntegrationListContainer.tsx; symbols tempArr, obj, tempObj.
- 2023-11-15 | CORE-014 | `807eb0ff2f099988a0ac83073b9782bfeb5026c6` | HSDM | fix: RES-91761, RES-91772, RES-91773, RES-91786 salesforce bugs. Files/symbols: IntegrationListContainer.tsx; SalesForceContainer.tsx; symbols classes.
- 2023-11-16 | CORE-001 | `48591deab3aca7e22f9715d6c6fe7a30a49fff90` | HSDM | feat: RES-90039 ccl side nav UAT feedback. Files/symbols: ContentLibraryFacetPane.tsx; symbols navExpanded, setNavExpanded.
- 2023-11-16 | CORE-014 | `8db5fb0936c6f75f3353f81e1763f44c33440318` | HSDM | feat: RES-90055 zoho crm. Files/symbols: IntegrationListContainer.tsx; ZohoCrmContainer.tsx; symbols createNew, radioOpt1, tempList.
- 2023-11-17 | CORE-019 | `0f31e4e891aa0eb7177165d9fd1a4c0cda841ff7` | branch | feat: arabic support. Files/symbols: CommentGrid.tsx; CommentTextBottomLayer.tsx; symbols rightDirection, classes.
- 2023-11-17 | CORE-007 | `631358613a5a8e03c1d0e882b5098566345ad555` | HSDM | fix: RES-89415 Google login flash, rfpio lite google oauth restriction. Files/symbols: app.js; googleCtrl.js.
- 2023-11-17 | CORE-007 | `e7ec42a3a4032abecff4f216607fc208ba199ec7` | HSDM | fix: RES-89415 Google login flash, rfpio lite google oauth restriction. Files/symbols: loginCtrl.js; login.html.
- 2023-11-17 | CORE-007 | `ae2075007d101aa6f7437ed721467c07fafc9ca8` | HSDM | fix: RES-89415 Google login flash, rfpio lite google oauth restriction. Files/symbols: app.js; login.html.
- 2023-11-20 | CORE-007 | `6390d5371d553fded20e6e3d338b0c2ea1216593` | HSDM | fix: RES-89415 Google login flash, rfpio lite google oauth restriction. Files/symbols: googleCtrl.js.
- 2023-11-20 | CORE-007 | `e56d68321816f0ee7854adcaab0602838a4bb7e2` | HSDM | fix: RES-89415 Google login flash, rfpio lite google oauth restriction. Files/symbols: googleCtrl.js; loginCtrl.js.
- 2023-11-20 | CORE-007 | `6f30ab465eda7caf0e511bc0feba5f0e270f8c67` | HSDM | fix: RES-89415 Google login flash, rfpio lite google oauth restriction. Files/symbols: googleCtrl.js; symbols loginInvoke, googleLogin.
- 2023-11-20 | CORE-033 | `a831229aa8de7e4aadb00583fc08c6f2b5ba0da1` | HSDM | fix: RES-36132 Inconsistent on showing font style for "Webdings" & "Wingdings". Files/symbols: app/modal/content-format.html. Identical patch copies: `b2fd61c8e9f5a0b0771e82346f2ca711e82d329e`.
- 2023-11-21 | CORE-033 | `f1b75d4f70f8fca61f566edf6f274c4900113ac2` | HSDM | fix: RES-92270, RES-92208 Edit Styles - Tiny MCE font family. Files/symbols: app/modal/content-format.html; app_v2/src/containers/project/respond/TinyMCECustomStyles.tsx; symbols primaryFnt1.
- 2023-11-21 | CORE-007 | `2006bbaa69fa78ecd211c7bc8803d5a53cad2295` | HSDM | fix: RES-89415 Google login flash, rfpio lite google oauth restriction. Files/symbols: googleCtrl.js.
- 2023-11-21 | CORE-007 | `6a3b1c4acc71d0e36b98a9ad4a235bffdf113cce` | HSDM | fix: RES-89415 Google login flash, rfpio lite google oauth restriction. Files/symbols: googleCtrl.js.
- 2023-11-22 | CORE-033 | `df2c409c858a0e8ceb2b0398aae684070d848974` | HSDM | fix: RES-73504 Display of tooltips by default,. Files/symbols: app/templates/settings/custom-roles.html.
- 2023-11-22 | CORE-007 | `a6d74c4849e11beda0fc9d7f4c3863df24c6ed3d` | HSDM | fix: RES-89415 Adding logs for google login. Files/symbols: googleCtrl.js.
- 2023-11-22 | CORE-007 | `e7363ffc9a099f0b0a1388cfdd11cf5282a856ab` | HSDM | fix: RES-89415 Google login flash, rfpio lite google oauth restriction. Files/symbols: googleCtrl.js; loginCtrl.js; symbols isGoogleLoginEnabled.
- 2023-11-22 | CORE-007 | `6e5c516d34ef0fe5dcc545f9e33b61e47dadab4c` | HSDM | fix: RES-89415 Google login flash, rfpio lite google oauth restriction. Files/symbols: loginCtrl.js.
- 2023-11-23 | CORE-001 | `d5facf24f57382a944a3abc63784578d675e56af` | branch | feat: RES-92364 header Layout App UX. Files/symbols: AppLauncher.tsx; AvatarMenu.tsx; symbols module, menuItems, HeaderAdornmentRenderer.
- 2023-11-23 | CORE-007 | `06917826ba92ba186aaa50e3b4b20600955998ed` | HSDM | fix: RES-89415 rfpio lite google oauth restriction. Files/symbols: loginCtrl.js.
- 2023-11-27 | CORE-001 | `e8989496dc3a0603d4be08e694ef354b32055d65` | branch | feat: header common. Files/symbols: HeaderAdornment.tsx; HeaderAdornmentRenderer.tsx; symbols mdScreen, lgScreen, xsScreen.
- 2023-11-28 | CORE-001 | `6b7278732f2550fa06e81fdd352a6237c2e078ff` | HSDM | feat: RES-92791 Header LoggedIn layout. Files/symbols: AppLauncher.tsx; AvatarMenu.tsx; symbols module, menuItems, darkModeFilterModules.
- 2023-11-28 | CORE-007 | `120b6d5000f1a4372aca14b94d2cff1b71ccef15` | HSDM | fix: RES-93224 Unable to activate company. Files/symbols: loginCtrl.js.
- 2023-11-28 | CORE-001 | `eb94e57621fd424fc4aaabc4678c6346f9e7b675` | HSDM | feat: RES-92791 Header LoggedIn layout. Files/symbols: DashBoardInitiator.tsx.
- 2023-11-28 | CORE-007 | `7ceace3e0268db775382f09871f808569fd7dfb3` | HSDM | fix: RES-93224 Unable to activate company. Files/symbols: googleCtrl.js.
- 2023-11-28 | CORE-007 | `803b1f2e46ca3c5802a624bcc0c1ebd9ef8cd845` | HSDM | fix: RES-93224 Unable to activate company. Files/symbols: googleCtrl.js.
- 2023-11-30 | CORE-001 | `c3704a177528f844ad990759232cbe3d23ab71e1` | HSDM | feat: RES-92791 Header LoggedIn layout. Files/symbols: ContainerNotFound.tsx; ReportsHeader.tsx; symbols history, handleBackClick, path.
- 2023-12-05 | CORE-001 | `aac44604fa9df607cc286fe653a1dcfd977dac45` | HSDM | feat: RES-92791 Header LoggedIn layout. Files/symbols: IntakeTable.tsx; MyAccountHeader.tsx; symbols tableStyle.
- 2023-12-05 | CORE-001 | `bef68f81a42896e845a7c86ae6cb638b7bb7aac6` | HSDM | feat: RES-92791 Header LoggedIn layout. Files/symbols: PageHeader.tsx; ProjectViewInitiator.tsx; symbols setNotificationBadgePage, setBadgeCount, hasUpdateSectionPermission.
- 2023-12-05 | CORE-001 | `f58d833428e0ddab296f64b4c181abeb1250a1a8` | HSDM | feat: RES-92791 Header LoggedIn layout. Files/symbols: AvatarMenu.tsx.
- 2023-12-06 | CORE-001 | `08a77a7bdfb806da2ccd5565c9ae34140d089681` | HSDM | feat: RES-92791 Header LoggedIn layout. Files/symbols: ContentLibraryMenuOptions.tsx; headerLayout.tsx.
- 2023-12-06 | CORE-001 | `75f0860aec4cd560eeb6e844abc218872bf0a3a7` | HSDM | feat: RES-92368 app launcher UX redesign. Files/symbols: AppLauncher.tsx; HeaderWrapperStyles.tsx.
- 2023-12-06 | CORE-001 | `d558ef4df15255d7e95f33905ae603a189496645` | HSDM | feat: RES-92791 Header unique shadow changes. Files/symbols: AvatarMenu.tsx; HeaderWrapperStyles.tsx.
- 2023-12-06 | CORE-001 | `9281fda66138cea25af2b64f22ef1e0ece6713cb` | HSDM | feat: RES-92791 Header unique shadow changes. Files/symbols: ReportsHeader.tsx; AnalyzerError.tsx.
- 2023-12-07 | CORE-001 | `93f482560593874f3aa8eb53fc2bbc4a3efa6a9d` | HSDM | feat: RES-92791 Header unique shadow changes. Files/symbols: ProactiveProposalPlgDialog.tsx.
- 2023-12-07 | CORE-001 | `e16d512f0d900684f67c7833d1c7c28eff30a591` | HSDM | feat: RES-92368 app launcher UX redesign. Files/symbols: {Analysis.svg =&gt; analysis.svg}; {Content.svg =&gt; content.svg}.
- 2023-12-07 | CORE-001 | `01ec70e7511105ffed673e602c363c5ac830997b` | HSDM | feat: RES-92368 app launcher UX redesign. Files/symbols: HeaderWrapperUtils.ts.
- 2023-12-07 | CORE-001 | `72899b1e8737f106c153f3bc7b666906e076234c` | HSDM | feat: RES-92792 Header LoggedIn layout Unit Test. Files/symbols: AppLauncher.tsx; headerLayout.tsx; symbols portalId, layout, SampleRenderer.
- 2023-12-11 | CORE-001 | `1780f4deb0572ccf729f7163014b9d356c64c13b` | HSDM | feat: RES-92368 app launcher UX redesign. Files/symbols: AppLauncher.tsx; HeaderWrapperStyles.tsx; symbols theme.
- 2023-12-13 | CORE-001 | `f4bd97e4cb4b8f2db4b9f6d1c76830549a1652b7` | HSDM | feat: RES-92368 app launcher UX redesign. Files/symbols: AppLauncher.tsx; HeaderWrapperStyles.tsx.
- 2023-12-13 | CORE-001 | `f5d241f188451f8abf1b39621e918b8634359ebd` | HSDM | feat: RES-92368 app launcher UX redesign. Files/symbols: HeaderWrapperStyles.tsx.
- 2023-12-13 | CORE-001 | `96bbf317145d7cf5f910154777ff4a9c9a136e37` | HSDM | feat: RES-92368 app launcher UX redesign. Files/symbols: AppLauncher.tsx.
- 2023-12-13 | CORE-001 | `018632f68746f67fc3aed5e47de92d92ac51c8a0` | HSDM | feat: RES-92368 app launcher UX redesign. Files/symbols: HeaderWrapperStyles.tsx.
- 2023-12-13 | CORE-001 | `ba9d1d49157b41bb2266b5a0dfdb3d8839b7d998` | HSDM | feat: RES-92368 app launcher UX redesign. Files/symbols: HeaderWrapperStyles.tsx.
- 2023-12-13 | CORE-001 | `b9dcb42c37dfa227b61bf97646050c128c8a8fea` | HSDM | feat: RES-92368 app launcher UX redesign. Files/symbols: AppLauncher.tsx; HeaderWrapperStyles.tsx.
- 2023-12-13 | CORE-001 | `373c3e070a44eca03a040476bbc600fa3fa6d49d` | HSDM | feat: RES-92368 app launcher UX redesign. Files/symbols: HeaderWrapperStyles.tsx.
- 2023-12-15 | CORE-001 | `f4d583fa58544d52690d3afa47928c80115d1662` | HSDM | feat: RES-92368 app launcher UX redesign. Files/symbols: AppLauncher.tsx; HeaderWrapperStyles.tsx.
- 2023-12-15 | CORE-037 | `c4004c9ed25245bf57ffa2bc553476e9c85c680c` | HSDM | fix: daily staging sync. Files/symbols: app_v2/src/containers/project/PageHeader.tsx.
- 2023-12-15 | CORE-001 | `0a487d9bd77597803772fe63f0e258d0c1e4b5c7` | HSDM | fix: RES-94018, RES-94020 App launcher issues. Files/symbols: IntakePageHeaderComponents.tsx; ManageProposalTableView.tsx; symbols routerHistory, customClass.
- 2023-12-18 | CORE-001 | `357e3b911d7337f798f85842f6c422cca0f0722e` | HSDM | fix: App launcher issues. Files/symbols: AppLauncher.tsx; HeaderWrapperStyles.tsx.
- 2023-12-19 | CORE-001 | `58c5a3f3b98086b67f372a1836542329ff898dd6` | HSDM | fix: RES-94693 App launcher issues. Files/symbols: CreateIntakeHeader.tsx; CreateProjectHeader.tsx.
- 2023-12-19 | CORE-009 | `091e18e7953f6060ad9279e44db3ce5b74e258ae` | HSDM | fix: RES-94598 New Style Name is not update in Custom Styles. Files/symbols: TinyMCECustomStyles.tsx; symbols styleList, tinymceStyleList, tinymceStyleMap.
- 2023-12-19 | CORE-001 | `b79d875af35e2ce9beb40b0cac5540d352f1b53d` | HSDM | fix: RES-94693 App launcher issues. Files/symbols: AppLauncher.tsx; symbols showContentAnalysisBadge.
- 2023-12-20 | CORE-001 | `9ebfba6eb8c601c687896874cfbf99a12a30fd61` | HSDM | fix: RES-94693 App launcher issues. Files/symbols: AppLauncher.tsx.
- 2023-12-20 | CORE-037 | `99c90fa7fd1cc6bd6e64edfa77f8f8f075664473` | HSDM | fix: staging sync. Files/symbols: app_v2/src/containers/intake/IntakeViewPageHeader.tsx.

### 2024 — 459 patch groups

- 2024-01-02 | CORE-023 | `a7c4ee5566b389e3fc78ca62805dedcf8b529386` | HSDM | fix: remove clarification. Files/symbols: ClarificationQuestionPageHelper.ts; ClarificationUtils.ts.
- 2024-01-02 | CORE-001 | `312c75d64b74ade13029eaaf59674be2a05f2b88` | HSDM | fix: remove deleted files. Files/symbols: ExportViewDialog.tsx; CreateWorkSpaceHeader.tsx.
- 2024-01-02 | CORE-011 | `71b4216ba0715ad8457ff603f80d1d45563eb677` | HSDM | fix: remove unused import. Files/symbols: ReportsHeader.tsx; AddDocHeader.tsx; symbols ClarificationsWrapper.
- 2024-01-03 | CORE-001 | `4c3484cc550cedc5c711eef76ac57cfe758d15e4` | HSDM | feat: RES-95245 App Framework UX changes. Files/symbols: AttachmentChipsAdvanced.tsx; ContainerNotFound.tsx; symbols filtered, ContainerNotFound.
- 2024-01-03 | CORE-001 | `eda0644716f89e5a05587ef51aae33e3bf65de1d` | HSDM | feat: RES-95245 App Framework UX changes. Files/symbols: IntakeHamburgerMenu.tsx.
- 2024-01-03 | CORE-001 | `cf1fb97f718b6bb991184e677144aa4799a692bb` | HSDM | feat: RES-95245 App Framework UX changes. Files/symbols: {headerLayout.tsx =&gt; HeaderLayoutdummy.tsx}.
- 2024-01-03 | CORE-001 | `954f01e3a461d7316425fe3957f4c5fcf96a1e2b` | HSDM | feat: RES-95245 App Framework UX changes. Files/symbols: {HeaderLayoutdummy.tsx =&gt; HeaderLayout.tsx}.
- 2024-01-04 | CORE-001 | `b22df456b7e1aaa48636aaea5340153952d7a830` | HSDM | feat: RES-95245 App Framework UX changes. Files/symbols: HeaderAdornment.tsx; RAHeaderComponent.tsx; symbols classes.
- 2024-01-09 | CORE-037 | `a129f82e78cb265630070e5895a600edd8050ec5` | HSDM | feat: org v2 link for dev2. Files/symbols: app/app/js/app.js; app/app/js/controller/library/v2RedirectCtrl.js; symbols init, companyId.
- 2024-01-09 | CORE-037 | `b881d387825eba22fafd7207b9ccd333bc0330c6` | HSDM | feat: org v2 link for dev2. Files/symbols: app/app/js/controller/library/v2RedirectCtrl.js; app/app/views/partials/footer.html.
- 2024-01-10 | CORE-037 | `6b5edbb2a399bcc1c363295459dd96d1e3dc4cce` | HSDM | feat: org v2 link for dev2. Files/symbols: app/app/js/app.js.
- 2024-01-11 | CORE-033 | `b2459e3ec8d7e737bbfcbd159f34b03eae4e5005` | HSDM | feat: org v2 link for dev2. Files/symbols: app_v2/src/components/FooterLoggedIn.tsx.
- 2024-01-15 | CORE-014 | `29655210c571452d1b933875d869335627ad9b1b` | HSDM | feat: RES-94372 Org Settings - 2.0 UX - Webhook. Files/symbols: IntegrationListContainer.tsx; WebhookBody.tsx; symbols componentMapping, WebhookBody, colorStyles.
- 2024-01-16 | CORE-014 | `10c0326fb591638429ee9b531669f96dfe7dbd45` | HSDM | feat: RES-94372 Org Settings - 2.0 UX - Webhook. Files/symbols: WebhookOtherRenderers.tsx; WebhookSaveComponent.tsx; symbols isError, HeaderTextComponent, classes.
- 2024-01-16 | CORE-014 | `276dfa399809654f9d20c5df06de7e2890ae98e6` | HSDM | feat: RES-94372 Org Settings - 2.0 UX - Webhook. Files/symbols: {WebhookEdit.tsx =&gt; EditWebhookConfiguration.tsx}; WebhookBody.tsx; symbols handleClick, fieldName, removeExternalIntegration.
- 2024-01-16 | CORE-014 | `9cb174f2a8f0c087b2508f273d1f02c1a99bb1e2` | HSDM | feat: RES-94372 Org Settings - 2.0 UX - Webhook. Files/symbols: WebhookInitiator.tsx.
- 2024-01-16 | CORE-023 | `5c61d3a4ee80f17bec00fb5ae901b4e9ebc1f3e3` | HSDM | feat: RES-96780 - Staging rebase to qrelease - 16.01.24. Files/symbols: index.ts; PQActivitiesHeader.tsx.
- 2024-01-17 | CORE-014 | `9617a969877b02f1a943c1762cea393e6e16a241` | HSDM | feat: RES-94372 Org Settings - 2.0 UX - Webhook. Files/symbols: WebhookBody.tsx.
- 2024-01-17 | CORE-014 | `cfb8b173f500d8b0db45151741ef3eb29154121f` | HSDM | fix: RES-96812 BU is not displayed on clicking the primary BU field. Files/symbols: WebhookContainer.tsx; WebhookTextFields.tsx; symbols userName.
- 2024-01-18 | CORE-021 | `ef985c43d76daf62f720f0e49c6fef85fada2d7a` | HSDM | feat: RES-96330 Org Settings - 2.0 UX - User Management - Add user. Files/symbols: OrganizationWrapperBodyRenderer.tsx; ManageUsersInitiator.tsx; symbols ManageUsersInitiator, AddUserInitiator, isPermissionEnabled.
- 2024-01-22 | CORE-021 | `ea7ef6f8714685fe56be4e31747c95164212fa8d` | HSDM | feat: RES-96330 Org Settings - 2.0 UX - User Management - Add user. Files/symbols: UserVO.ts; ManageUsersListPage.tsx; symbols headerArray, AddUserContainer, classes.
- 2024-01-23 | CORE-021 | `efddd4b4547c4f7e25e1232bcf6c9caac6431c25` | HSDM | feat: RES-96330 Org Settings - 2.0 UX - User Management - Add user. Files/symbols: AddUserContainer.tsx; AddUserDrawer.tsx; symbols onExpandClick.
- 2024-01-23 | CORE-019 | `794cce1e7c56b80a3dff55a96dfa92296b293010` | HSDM | fix: RES-97183 Discussion & comments - @Mentioning of Users with special character. Files/symbols: CommentUtils.ts; CommentTextBox.tsx.
- 2024-01-23 | CORE-021 | `5f99f63d440313832452ec2b4de9ffd444ea1b02` | HSDM | feat: RES-96330 Org Settings - 2.0 UX - User Management - Add user. Files/symbols: UserDetailsRenderer.tsx; OrgCompWithLabel.tsx; symbols OrgCompWithLabel, classes.
- 2024-01-23 | CORE-012 | `c89378438d6761ed3d660c31ef2fc56ce5498e7d` | HSDM | fix: org bugs. Files/symbols: SaveAndCancelComponent.tsx; UpdateBusinessUnits.tsx.
- 2024-01-23 | CORE-013 | `108c01c5ef6ae20e06fc02352db0898571758259` | HSDM | fix: org bugs. Files/symbols: OrganizationUtils.ts; symbols currentUserBu.
- 2024-01-30 | CORE-021 | `9bd0a49fbdd625695f2eed19619c388ebab2864d` | HSDM | feat: RES-96330 Org Settings - 2.0 UX - User Management - Add user. Files/symbols: ManageUsersListPage.tsx; AddUserContainer.tsx; symbols closeDrawer, AddUserContainer, headerHeight.
- 2024-02-01 | CORE-021 | `e907b4ac2e295e8900798d010a3f8b1cb0f4c8e3` | HSDM | feat: RES-96330 Org Settings - 2.0 UX - User Management - Add user. Files/symbols: WarningToastDialog.tsx; ManageUsersInitiator.tsx; symbols ManageUsersContainer, showLoader, timeout.
- 2024-02-01 | CORE-021 | `d987bbdeeaf11cc5018a00e01697e4c8addc1d40` | HSDM | feat: RES-98484 Org Settings - 2.0 UX - User Management - Add user(Single). Files/symbols: UserVO.ts; WarningToastDialog.tsx; symbols userRole, additionalRoles, isProjectRequester.
- 2024-02-01 | CORE-021 | `a981e5249c46c9a1c9b13d966cf431446950ca44` | HSDM | feat: RES-96330 Org Settings - 2.0 UX - User Management - Add user. Files/symbols: UserVO.ts.
- 2024-02-02 | CORE-021 | `eb35102ee54c88bd3261fdd129071dbe1ade24e6` | HSDM | feat: RES-96330 Org Settings - 2.0 UX - User Management - Add user. Files/symbols: AddUserDrawer.tsx; AddUserSaveComponent.tsx; symbols headerViews, checkBoxStyles.
- 2024-02-05 | CORE-021 | `f8c203403400546f4f80501d0436669faf848112` | HSDM | feat: RES-98484 Org Settings - 2.0 UX - User Management - Add user. Files/symbols: UserVO.ts; AddUserContainer.tsx; symbols AddUserDrawer, classes, value.
- 2024-02-05 | CORE-021 | `802268751eae6532a33fbbfb3a3bf2edb7cce743` | HSDM | feat: RES-98484 Org Settings - 2.0 UX - User Management - Add user(Single). Files/symbols: UserDetailsStore.ts; AddUserSaveComponent.tsx; symbols AddUserSaveComponent, addNewUserInfo, users.
- 2024-02-05 | CORE-021 | `e0ed8982605c35975f8398a9d7cc08bc01b13105` | HSDM | feat: RES-98484 Org Settings - 2.0 UX - User Management - Add user(Single). Files/symbols: GeneralService.ts.
- 2024-02-06 | CORE-021 | `c82924b9597bb40a54736f33d19e57639e4fbd79` | HSDM | feat: RES-98484 Org Settings - 2.0 UX - User Management - Add user(Single). Files/symbols: AdditionalDetailsRenderer.tsx; OrgCompWithLabel.tsx; symbols manageuserStyles.
- 2024-02-06 | CORE-021 | `6b85885ee606ef0bffd5524c3f8fedd731238318` | HSDM | feat: RES-98484 Org Settings - 2.0 UX - User Management - Add user(Single). Files/symbols: UserDetailsStoreImpl.ts.
- 2024-02-08 | CORE-021 | `7ef66bcbb3c40ac6d09be64947f3b0eb1b223a48` | HSDM | feat: RES-96960 - 2.0 UX - Org Settings - User Management - Add user(Multi user). Files/symbols: AddUserDrawer.tsx; AddUserSaveComponent.tsx; symbols bulkSelectedUser, userList, ConstructUserData.
- 2024-02-08 | CORE-021 | `43d110dfbb40f1402b31ab568ccab64d8c5ae66f` | HSDM | feat: RES-96960 - 2.0 UX - Org Settings - User Management - Add user(Multi user). Files/symbols: MultiUserInitiator.tsx; symbols MultiUserInitiator, classes, tagStyles. Identical patch copies: `bf581fb0fab5495904c9000bc99601583a3fbfd2`.
- 2024-02-08 | CORE-021 | `7e4faea00b9ace8a9655ed8d13a61007dc21e3c7` | HSDM | Revert "feat: RES-96960 - 2.0 UX - Org Settings - User Management - Add user(Multi user)". Files/symbols: MultiUserInitiator.tsx.
- 2024-02-09 | CORE-021 | `9b4a06c5661984bdd39954d75d71a76641701c8d` | HSDM | fix: RES-99087, RES-99088, RES-99089 - Add user bugs. Files/symbols: AddUserContainer.tsx; AddUserSaveComponent.tsx; symbols masterBusinessUnitsMap, updateUserPolicies, buList.
- 2024-02-09 | CORE-021 | `dc1d85b9d0f974ab3a2d7e904c3fe06ba04fa7fb` | HSDM | fix: RES-99087, RES-99088, RES-99089 - Add user bugs. Files/symbols: AddUserSaveComponent.tsx; ManageUsersUtils.ts; symbols errorMessage.
- 2024-02-10 | CORE-021 | `45d3859bbd58af4d9a414482610a522e1866cfce` | HSDM | feat: RES-96960 - 2.0 UX - Org Settings - User Management - Add user(Multi user). Files/symbols: OrganizationService.ts; OrgManageUsersStore.ts; symbols count.
- 2024-02-12 | CORE-021 | `1c6a29c7fc0cfd3d8f95da041710da0fe7b0acae` | HSDM | feat: RES-96960 - 2.0 UX - Org Settings - User Management - Add user(Multi user). Files/symbols: AddUserContainer.tsx; AddUserDrawer.tsx; symbols AddUserContainer, inputRef, bulkSelectedUser.
- 2024-02-12 | CORE-021 | `29a1a403f833ebb3c725476e480935fb3b4064c4` | HSDM | feat: RES-96960 - 2.0 UX - Org Settings - User Management - Add user(Multi user). Files/symbols: AddUserDrawer.tsx; MultiUserInitiator.tsx; symbols constructUserData, tempBulkSelectedUser, idx.
- 2024-02-13 | CORE-021 | `a97127fc31e0ce741a165138dcd50963bfe8afba` | HSDM | feat: RES-96960 - 2.0 UX - Org Settings - User Management - Add user(Multi user). Files/symbols: AddUserContainer.tsx; AddUserDrawer.tsx; symbols userOptMap, users, userNameMap.
- 2024-02-14 | CORE-021 | `4c32d5bccf25760d97430b359ce488473d1b8c61` | HSDM | feat: RES-96960 - 2.0 UX - Org Settings - User Management - Add user(Multi user). Files/symbols: AddUserSaveComponent.tsx; MultiUserInitiator.tsx; symbols userInValidMap.
- 2024-02-15 | CORE-001 | `ce5160783e2246a224b1e722251a22c703d768ec` | HSDM | feat: RES-94779 2.0 UX - App Launcher. Files/symbols: AIAssistant9Dots.tsx; Community9dots.tsx; symbols AIAssistant9Dots, size, Community9dots.
- 2024-02-15 | CORE-001 | `132b65c5eb5d17c64b9f5c30899807ec17387110` | HSDM | feat: RES-94779 2.0 UX - App Launcher. Files/symbols: AppLauncher.tsx; HeaderWrapperStyles.tsx.
- 2024-02-15 | CORE-001 | `75556b80251859f41c0582fec7dee1e251fed9e2` | HSDM | feat: RES-94779 2.0 UX - App Launcher. Files/symbols: AppLauncher.tsx; HeaderWrapperStyles.tsx; symbols landingPage.
- 2024-02-15 | CORE-001 | `00d52654117a033f4c809a7643e613fcebbe9c8c` | HSDM | feat: RES-94779 2.0 UX - App Launcher. Files/symbols: AppLauncher.tsx.
- 2024-02-15 | CORE-001 | `0b62dc313d26c2a269ac2daabe58a01ebd59b29a` | HSDM | feat: RES-94779 2.0 UX - App Launcher. Files/symbols: HeaderLayout.tsx.
- 2024-02-16 | CORE-001 | `575a419d9acd4b7b628377908d4a0f5b01d8895c` | HSDM | feat: RES-94779 2.0 UX - App Launcher. Files/symbols: AIAssistant9Dots.tsx; AppLauncher.tsx; symbols AIAssistant9Dots, classes.
- 2024-02-16 | CORE-001 | `d649edb3993787767a7e112b36f554e0ffd01ccf` | HSDM | feat: RES-94779 2.0 UX - App Launcher. Files/symbols: AppLauncher.tsx; symbols checkUserAccess, currentRole, hasAccessItem.
- 2024-02-16 | CORE-001 | `51a2354e2d6656245cd6422b68735cdf7c636bb8` | HSDM | feat: RES-94779 2.0 UX - App Launcher. Files/symbols: HeaderWrapperStyles.tsx.
- 2024-02-16 | CORE-009 | `b229f465b99c24eba794327ef6373362f6ad8101` | HSDM | fix: RES-99768 Tinymce : Line spacing value in tiny mce is duplicating when we apply line space. Files/symbols: plugin.js; tinymce.js.
- 2024-02-16 | CORE-001 | `2a7bf6a80231023261effeb87c376e9427ccd587` | HSDM | feat: RES-94779 2.0 UX - App Launcher. Files/symbols: HeaderWrapperStyles.tsx.
- 2024-02-16 | CORE-001 | `ecc0c290d34629951af385424d9a0ae80f21afd7` | HSDM | feat: RES-94779 2.0 UX - App Launcher. Files/symbols: IconRenderer9dots.tsx; AppLauncher.tsx; symbols IconRenderer9dots, componentMapping.
- 2024-02-16 | CORE-001 | `1cf12f516ec0e8188e88552947de356b6f66058e` | HSDM | feat: RES-94779 2.0 UX - App Launcher. Files/symbols: AIAssistant9Dots.tsx; Community9dots.tsx.
- 2024-02-16 | CORE-001 | `21439c40df0e907ebe801fe94489c5bb6be5ba5c` | HSDM | feat: RES-94779 2.0 UX - App Launcher. Files/symbols: ResponisveFooterIcon9Dots.tsx; symbols ResponisveFooterIcon9Dots, fillColor.
- 2024-02-18 | CORE-021 | `277b3bab802aad1cee40cdab5e9d202b7dfe80eb` | HSDM | fix: RES-99843, RES-99844, RES-99901 Org V2 - Add Multi User bugs. Files/symbols: AddUserContainer.tsx; AddUserDrawer.tsx; symbols drawerStyles, tempUserList, currentUser.
- 2024-02-22 | CORE-001 | `b33d10f9649647675719f341e7affebf90de57c0` | HSDM | feat: RES-99128 - 2.0 UX - App Launcher - Header - Phase I. Files/symbols: icons-reference.html; rfpio.eot; symbols actionLevelTriggered, isDisabled, HeaderTitleAdornment.
- 2024-02-23 | CORE-001 | `5432057038d9e2796685b4d327ed6a63e2b1b7e8` | HSDM | feat: RES-100173 - 2.0 UX - App Launcher - Sub Navigation - Icon & Theme Color Update. Files/symbols: AppLauncherUtils.tsx; CCLHamBurgerMenu.tsx.
- 2024-02-26 | CORE-001 | `3c34b744532f627bf2d29830eaeda6d59e86c61e` | HSDM | feat: RES-99128 - 2.0 UX - App Launcher - Header - Phase I. Files/symbols: icons-reference.html; HeaderTitleAdornment.tsx; symbols levelAction, singlePageModules, skipBreadCrumbs.
- 2024-02-27 | CORE-001 | `41dfb369841ac94da162afd972f7b06404be49a9` | HSDM | feat: RES-100991 - 2.0 UX - App Launcher - Sub-Nav - Hover State. Files/symbols: IconRenderer9dots.tsx; AppLauncher.tsx; symbols percent, keys, popperRef.
- 2024-02-27 | CORE-001 | `19b740cee638cab80129eb70132b6859ba1ffcc2` | HSDM | feat: RES-100991 - 2.0 UX - App Launcher - Sub-Nav - Hover State. Files/symbols: RfpHamBurgerMenu.tsx.
- 2024-02-27 | CORE-001 | `9e02b63e32d83e66c38c2a55e163a2cea7f17b6a` | HSDM | feat: RES-100991 - 2.0 UX - App Launcher - Sub-Nav - Hover State. Files/symbols: AppLauncherUtils.tsx.
- 2024-02-28 | CORE-001 | `b547376fa875b35219478f2f9a50f9d1b5790290` | HSDM | fix: RES-101289, RES-101282 Header Bugs and staging sync removal fix. Files/symbols: AppLauncher.tsx; HeaderTitleAdornment.tsx; symbols smScreen, localData, featureList.
- 2024-02-28 | CORE-001 | `b575c45de05285162cd9345970738b795f3727d5` | HSDM | feat: RES-100173 App framework main. Files/symbols: icons-reference.html; rfpio.eot.
- 2024-02-28 | CORE-001 | `ef7451aaaaf5cd9cb5e3651c6286504dc070e50e` | HSDM | fix: RES-101289, RES-101282 Header Bugs and staging sync removal fix. Files/symbols: ESignLifeCycle.tsx; ESignDocumentSent.tsx; symbols rows, enable.
- 2024-02-28 | CORE-026 | `673c19304d6a0f0534c4f031a24e2a19de3599f5` | HSDM | feat: ask sync commit. Files/symbols: .babelrc; settings.json; symbols EmptyConversationDark, EmptyConversationLight, DOCXIcon.
- 2024-02-29 | CORE-001 | `6317dd92b2570714b6c97ae850ac9bfdd79b953b` | HSDM | feat: ask sync commit. Files/symbols: AskResponsive.tsx; AvatarMenu.tsx; symbols mdScreen, HeaderWrapper, showAsk.
- 2024-02-29 | CORE-001 | `507e6755b1ef327c12f5ab5ea8c437a59c6a84ef` | HSDM | feat: RES-101275 - 2.0 UX - App Framework- Initial Setup Commit. Files/symbols: IconRenderer9dots.tsx; ResponisveFooterIcon9Dots.tsx; symbols IconRenderer9dots, componentMapping, ResponisveFooterIcon9Dots.
- 2024-02-29 | CORE-001 | `54edaaa584f7174e5600c515aa5e89d3a5ad6568` | HSDM | feat: RES-101275 - 2.0 UX - App Framework- Initial Setup. Files/symbols: icons-reference.html; rfpio.eot; symbols actionLevelTriggered, isDisabled, footerHeight.
- 2024-02-29 | CORE-001 | `d618a210f261b9fd98aca4079e847bb52f01d836` | HSDM | feat: RES-101275 - 2.0 UX - App Framework Setup. Files/symbols: CRMManageProject.tsx; useUserData.ts; symbols unsetArchivedProjectVO, onCloseDrawer, notificationBadgePage.
- 2024-02-29 | CORE-001 | `ebe7811b255968056f65574ef7a93aa73a0ce3f4` | HSDM | feat: RES-101275 - 2.0 UX - App Framework Setup. Files/symbols: CreateProjectWrapper.tsx; CreateProjectForm.tsx; symbols tableStyle, routerHistory, isSalesForce.
- 2024-03-01 | CORE-001 | `fd33247f83f08727ee246acdadc6ff8366857ea6` | HSDM | feat: RES-101275 - 2.0 UX - App Framework Setup. Files/symbols: index.ts; RequestUtils.ts; symbols requestStatusColorMap.
- 2024-03-01 | CORE-001 | `df7d48ca870987ca39ac1eed10df6f16d66c1e61` | HSDM | feat: RES-101275 - 2.0 UX - App Framework Setup. Files/symbols: AskResponsive.tsx; IntakeHamburgerMenu.tsx; symbols actionKey.
- 2024-03-02 | CORE-001 | `abba69ad0b6c27792a95ac5071d7287a47925b5f` | HSDM | feat: RES-101275 - 2.0 UX - App Framework Setup. Files/symbols: HeaderTitleAdornment.tsx; ESignLifeCycle.tsx; symbols smScreen, isNativeAppEnabled, classes.
- 2024-03-03 | CORE-001 | `8662cdd4e4f203dae4288fe1c53823a3c7998040` | HSDM | feat: RES-101275 - 2.0 UX - App Framework. Files/symbols: AvatarMenu.tsx; HeaderTitleAdornment.tsx; symbols mdScreen, xsScreen, mModules.
- 2024-03-03 | CORE-001 | `8d7fc215dd2b1b1e4772a84be912809f58049d5f` | HSDM | feat: RES-101275 - 2.0 UX - App Framework. Files/symbols: HeaderTitleAdornment.tsx; ESignLifeCycle.tsx.
- 2024-03-04 | CORE-001 | `2474fb435825e5491fd83549fc5c732f24c14ea0` | HSDM | feat: RES-100970 - 2.0 UX - App Launcher - Feedback. Files/symbols: IconRenderer9dots.tsx; AskResponsive.tsx; symbols actionLevelTriggered.
- 2024-03-04 | CORE-001 | `dd6f0aa7640133998ac0be847b721bc570e30172` | HSDM | feat: RES-100970 - 2.0 UX - App Launcher - Feedback. Files/symbols: PreviewContentHeader.tsx; ProfileSearchResultsPage.tsx.
- 2024-03-05 | CORE-001 | `7e3fc3a4fe040001e898f823291b79131e2bd832` | HSDM | feat: RES-100970 - 2.0 UX - App Launcher - Feedback. Files/symbols: RfpHamBurgerMenu.tsx.
- 2024-03-05 | CORE-001 | `e3459c2d6c60b136e815e8ab6ada9890ab960dbf` | HSDM | feat: RES-100970 - 2.0 UX - App Launcher - Feedback. Files/symbols: RfpTour.tsx.
- 2024-03-05 | CORE-001 | `4d5b2ee1c29c949d521e0a203919eb3eea037fc7` | HSDM | feat: RES-100970 - 2.0 UX - App Launcher - Feedback. Files/symbols: HeaderTitleAdornment.tsx; ProjectHamburgerMenu.tsx.
- 2024-03-06 | CORE-001 | `36cc2b2dc9229f83f02f9fce82f9359b5bcd0bb0` | HSDM | fix: RES-10181, RES-101810, RES-101813 applauncher bugs. Files/symbols: SendFeedback.tsx; HeaderWrapperStyles.tsx; symbols UI_V2_STRICT.
- 2024-03-07 | CORE-001 | `c41384d23de2151b95818cc343686a563c09596c` | HSDM | fix: RES-102302 - Survey - NFR items on App-launcher avatar menu & 9 dot menu. Files/symbols: AppLauncherUtils.tsx; HeaderWrapperUtils.ts; symbols darkModeFilterModules, UI_V2_STRICT, navExpanded.
- 2024-03-07 | CORE-001 | `8b5de15fd356942962e97cf7c9a24f851e9734d3` | HSDM | fix: RES-102197 App framework bugs. Files/symbols: RfpHamBurgerMenu.tsx; App.css.
- 2024-03-07 | CORE-001 | `dff6761dcaf9701a1c5c948fdbba259cd9e7ee6f` | HSDM | fix: RES-102238 app bugs. Files/symbols: RfpHamBurgerMenu.tsx.
- 2024-03-07 | CORE-001 | `582a714b8b5d1fd3e681964580cb819c3f1d4e26` | HSDM | fix: RES-101983, RES-101810, RES-101844, RES-102173, RES-102340, RES-102367, RES-102323 bugs. Files/symbols: HeaderTitleAdornment.tsx; HeaderWrapperUtils.ts; symbols redirectedFrom, navExpanded.
- 2024-03-08 | CORE-001 | `06567be3f2d0683f90c59f4d5a396917ae1c5973` | HSDM | fix: RES-102234, RES-101180, RES-102080, RES-102383 App Framework bugs. Files/symbols: IconRenderer9dots.tsx; HeaderTitleAdornment.tsx.
- 2024-03-08 | CORE-001 | `b9fba0d21b999bb1edf4443bb7272ff3efcea055` | HSDM | fix: RES-102533, RES-102509, RES-101180, RES-102384, App FrameworkBugs. Files/symbols: AvatarMenu.tsx; HeaderTitleAdornment.tsx; symbols redirectedFrom, onRedirectionClick, redirectLink.
- 2024-03-08 | CORE-001 | `0e96276b71c783848692a27f51bcd8df590ccd6f` | HSDM | fix: RES-102533, RES-102509, RES-101180, RES-102384, App FrameworkBugs. Files/symbols: CclTour.tsx.
- 2024-03-09 | CORE-033 | `fba73b9426e9077c59b9afd141d28d0c96bfc74f` | HSDM | fix: Debugging purpose. Files/symbols: app_v2/src/rfp-components/RfpTour.tsx.
- 2024-03-09 | CORE-001 | `103372017f4dabebc186b7887e7d257df134b445` | HSDM | fix: RES-102181, RES-102533, RES-102634 App framework bugs. Files/symbols: AppLauncher.tsx; AvatarMenu.tsx; symbols handleOpen, currentPage, finalV1Url.
- 2024-03-09 | CORE-001 | `b303ef1b08c1ffc4e3ceba12fa86964535f413f0` | HSDM | fix: RES-102181, RES-102533, RES-102634 App framework bugs. Files/symbols: RfpTour.tsx.
- 2024-03-09 | CORE-001 | `0c4451fa20e96b40e60519f11c9db64f5544a367` | HSDM | fix: RES-102637 draggable icon can be able to drag under header. Files/symbols: ShredNavigationDragger.tsx.
- 2024-03-09 | CORE-001 | `9d2303839e4e6b64eeabafe7a6beb6d03fb82d9d` | HSDM | fix: RES-102614, RES-102614, RES-102181 App Framework bugs. Files/symbols: HeaderTitleAdornment.tsx; HeaderWrapperUtils.ts; symbols tempInternalUsers, BreadCrumbTitleSkeleton.
- 2024-03-11 | CORE-001 | `872114867c79be0aa0bda165bd111d3df6db6657` | HSDM | fix: RES-102716 Header Adornment fix. Files/symbols: HeaderTitleAdornment.tsx; ModuleNameRenderer.tsx.
- 2024-03-11 | CORE-001 | `b0693537198c20e08f204b36371585012970c76e` | HSDM | fix: RES-102716 Header Adornment fix. Files/symbols: HeaderTitleAdornment.tsx.
- 2024-03-11 | CORE-001 | `4f61914889219bb821eeceffb4835b63ee5d93f5` | HSDM | fix: RES-102716 Header Adornment fix. Files/symbols: App.css.
- 2024-03-11 | CORE-001 | `2273a429c57b89c3850fdd4546657a126d0daf43` | HSDM | fix: RES-102716 Header Adornment fix. Files/symbols: HeaderTitleAdornment.tsx.
- 2024-03-11 | CORE-001 | `73db3fb77cfaa78d4bda8d4e1a2fb3a51d39b3bf` | HSDM | fix: RES-102716 Header Adornment fix. Files/symbols: HeaderLayout.tsx; ContentLibraryInputSearch.tsx; symbols discussionContainerHeight, manageSectionTableHeight.
- 2024-03-12 | CORE-001 | `d99e33236a3a4892601430d6bff320be6e29ae84` | HSDM | fix: Static Common header. Files/symbols: AppLauncherUtils.tsx; LoggedInHeaderLayout.tsx.
- 2024-03-12 | CORE-001 | `caf1a98b33e9bcc573d165a2bf69cc66a7f9d983` | HSDM | fix: Static Common header. Files/symbols: HeaderWrapperUtils.ts; RfpHamBurgerMenu.tsx.
- 2024-03-12 | CORE-001 | `d9127cf62cac082743cfb03532ace6b34bbd72b6` | HSDM | fix: RES-102621 In Safari brower can't able to access Help Center. Files/symbols: HelpCenterDialog.tsx.
- 2024-03-13 | CORE-001 | `1d2f742fdfcdbcfa71802589ae082758402f263a` | HSDM | feat: RES-102446 - App Framework - Feedbacks. Files/symbols: HeaderTitleAdornment.tsx; HeaderWrapperUtils.ts; symbols isTabletDevice.
- 2024-03-13 | CORE-001 | `9ee68d05c358244729d11add4aac22842d505a7e` | HSDM | feat: RES-102446 - App Framework - Feedbacks , RES-103043, RES-103083. Files/symbols: HeaderTitleAdornment.tsx; MyWorkWrapperContainer.tsx.
- 2024-03-13 | CORE-001 | `c8e4ed57eedc4c9962aad5824ac02648f22549e0` | HSDM | feat: RES-102446 - App Framework - Feedbacks , RES-103043, RES-103083. Files/symbols: MyWorkTaskWrapper.tsx; ProjectViewInitiator.tsx.
- 2024-03-14 | CORE-001 | `7c1d900a81167dc95ed71885b795ef41e6239b39` | HSDM | feat: RES-102446 - App Framework - Feedbacks , RES-103043, RES-103083. Files/symbols: AvatarMenu.tsx.
- 2024-03-14 | CORE-001 | `92bc7c3ff71a9fb7d20afbee4dca319deb04cd7e` | HSDM | fix: RES-102181, RES-102722 App Framework Bugs. Files/symbols: AvatarMenu.tsx; HeaderWrapperStyles.tsx.
- 2024-03-14 | CORE-001 | `1e754c89a1edbe400de710cecb737a1e7e8de34e` | HSDM | fix: RES-102181, RES-102722 App Framework Bugs. Files/symbols: LoggedInHeaderLayout.tsx.
- 2024-03-18 | CORE-001 | `bf27b8562c50cee19f9672e44acb61aad96630c2` | HSDM | feat: RES-103675 Terminology change & HelpCenter Optimization. Files/symbols: IconRenderer9dots.tsx; AppLauncher.tsx; symbols svgMapping, IconRenderer9dots, componentMapping.
- 2024-03-19 | CORE-034 | `bcf13d40b51efdec3f169b00171eeefc9124f345` | HSDM | feat: RES-103669 Org Settings - Feedbacks. Files/symbols: OrgNavBar.tsx; OrganizationInitiator.tsx; symbols colorStyles, classes, selectedMenuUrl.
- 2024-03-19 | CORE-001 | `d6b9e30547af5b942983237ff9f0d49eceba9f64` | HSDM | fix: restricting ask. Files/symbols: HeaderWrapper.tsx; MyWorkHeader.tsx; symbols showAsk.
- 2024-03-20 | CORE-001 | `522bf25fa31f534356b33fc0c253b8d2a3b3e0eb` | HSDM | fix: RES-104042, RES-103996 App Framework E2E bugs. Files/symbols: AskResponsive.tsx; HeaderWrapperStyles.tsx.
- 2024-03-20 | CORE-001 | `d024aa8db212330b15801e8d8cfbc29c5264a34a` | HSDM | fix: RES-104042, RES-103996 App Framework E2E bugs. Files/symbols: RfpButton.tsx.
- 2024-03-20 | CORE-001 | `6ccc4d8166ccc428cd31234e0df678c1a2467847` | HSDM | fix: RES-102181, RES-103884, RES-104197 RES-104190, RES-104318 App Framework E2E bugs. Files/symbols: AvatarMenu.tsx; HeaderTitleAdornment.tsx; symbols companyShortName, selectedProjectPageNameMap, currentPage.
- 2024-03-21 | CORE-011 | `90b466c6cb5c9faeb339e90e0cfbc09e8c882a71` | HSDM | fix: RES-104479, RES-104108, RES-104273, RES-103937, RES-104480 bugs. Files/symbols: MyAccountPreferenceRenderer.tsx; RfpHamBurgerMenu.tsx.
- 2024-03-21 | CORE-001 | `d3b9990e348e7cc4d808b62440b12fd726b89f79` | HSDM | fix: RES-104585, RES-103882, RES-104545 App Framework E2E bugs. Files/symbols: AvatarMenu.tsx; RequestContainer.tsx; symbols isProjectViewPage, pathName, setBadgeCount.
- 2024-03-21 | CORE-001 | `fa2a1d1fb7581c22ffaca6685a79a3c1b1d1c3ac` | HSDM | fix: RES-104585, RES-103882, RES-104545 App Framework E2E bugs. Files/symbols: CreateProjectHeader.tsx.
- 2024-03-21 | CORE-001 | `2c0ae633761f44ab28bfd550d5ee2d85571c4bf7` | HSDM | fix: RES-104585, RES-103882, RES-104545 App Framework E2E bugs. Files/symbols: CreateProjectHeader.tsx.
- 2024-03-22 | CORE-001 | `6a64cbcdef1f2b19c7e4c09e5d49e6fdd8487327` | HSDM | fix: RES-104126 bugs. Files/symbols: SectionQuestionsView.tsx; RfpHamBurgerMenu.tsx.
- 2024-03-22 | CORE-001 | `f3aa6358eb322233b92e22a3d0bc669a11d6bedf` | HSDM | fix: RES-104480 FireFox Hamburger Scroll issue. Files/symbols: RfpHamBurgerMenu.tsx.
- 2024-03-24 | CORE-001 | `04179e1aaff773e3543b81a9c5d5c5e3a98d9150` | HSDM | fix: RES-104386, RES-104545 Able to navigate to other modules in ms-teams bot. Files/symbols: CreateProjectHeader.tsx; LoggedInHeaderLayout.tsx.
- 2024-03-25 | CORE-001 | `b105a19295743d14c33fd7e1c3577659dd964c97` | HSDM | feat: RES-103898 - Retaining HamBurger Menu on refresh. Files/symbols: ApplicationFrameWorkStoreImpl.ts.
- 2024-03-25 | CORE-001 | `f6318bc7339c4203c744baafef8ac39556e77b7d` | HSDM | feat: RES-103898 - Retaining HamBurger Menu on refresh. Files/symbols: CreateProjectHeader.tsx.
- 2024-03-25 | CORE-001 | `5c74e66de39d5af736392759ce6c8b546314a338` | HSDM | feat: RES-103898 - Retaining HamBurger Menu on refresh. Files/symbols: ApplicationFrameWorkStoreImpl.ts.
- 2024-03-25 | CORE-011 | `1ccde0b258e64f71b5dcec1c435d6f8e719dd8bd` | HSDM | fix: RES-104038, RES-103909, RES-105124 E2E bugs. Files/symbols: HelpCenterSupport.tsx; PreviewMailAndDeleteDialog.tsx.
- 2024-03-25 | CORE-033 | `34f5b9d19ee55eb888e3c24609c29f5a025310e4` | HSDM | fix: RES-104038, RES-103909, RES-105124 E2E bugs. Files/symbols: app_v2/src/containers/profile/components/ProfileHamburgerMenu.tsx; app_v2/src/containers/profile/view/list/ProfileListPageHeader.tsx; symbols setItemsPerPage.
- 2024-03-25 | CORE-037 | `ba744ba21e1884ab018f07d05e856dbab6b08bf5` | HSDM | fix: RES-103017, RES-104389 bugs. Files/symbols: app_v2/src/containers/e-sign/life-cycle-components/ESignReview.tsx; app_v2/src/containers/profile/view/manage-profile/AddProfile.tsx.
- 2024-03-25 | CORE-033 | `261dc83d5145cfa0c4a0489cc56a1f2bc7de0e4f` | HSDM | fix: RES-104038, RES-103909, RES-105124 E2E bugs. Files/symbols: app_v2/src/containers/profile/components/ProfileHamburgerMenu.tsx.
- 2024-03-26 | CORE-015 | `747685d1d505525a4bbabf2cf20b1343e3e3038b` | HSDM | fix: RES-105217 project notes custom name fix. Files/symbols: IntakePageHeaderComponents.tsx; IntakeViewPageHeader.tsx; symbols projectNotesName.
- 2024-03-26 | CORE-033 | `8d431d08efbc8ef43f04b928ed6d6a75848beb70` | HSDM | fix: RES-105296 Color fix. Files/symbols: app_v2/src/rfp-components/RfpButton.tsx; symbols classes, theme.
- 2024-03-27 | CORE-001 | `194b6811984bacd65fc88ed7f5ed21334a380696` | HSDM | feat: RES-104466 App Framework - Feedback & bugs. Files/symbols: icons-reference.html; rfpio.eot; symbols isPermissionEnabled, obj.
- 2024-03-27 | CORE-033 | `c178b77a73a9f992c019864c9e216125deb761c3` | HSDM | fix: RES-105458 CCL - AI dropdown. Files/symbols: app_v2/src/components/rfpio_ai/AiDropdown.tsx.
- 2024-03-27 | CORE-001 | `b03439578a9d73a5625acdf4972c372e4114be3d` | HSDM | fix: RES-105412, RES-105441, RES-105455, RES-105458, RES-105473 E2E bugs. Files/symbols: FooterWrapper.tsx.
- 2024-03-28 | CORE-001 | `5153823f945838c930276b9d51317cd5c9c897db` | HSDM | fix: RES-105412, RES-105441, RES-105455, RES-105458, RES-105473 E2E bugs. Files/symbols: HelpCenter.tsx.
- 2024-03-28 | CORE-033 | `b31018887085f02bef9f5a91bdfccabc014cb072` | HSDM | fix: RES-105412, RES-105441, RES-105455, RES-105458, RES-105473 E2E bugs. Files/symbols: app_v2/src/rfp-components/RfpButton.tsx; app_v2/src/store/ThemeStoreImpl.ts; symbols classes.
- 2024-03-28 | CORE-001 | `250f4e75039308280e35f6545602e790c56024f1` | HSDM | fix: RES-105412, RES-105441, RES-105455, RES-105458, RES-105473 E2E bugs. Files/symbols: HelpCenterDataListRenderer.tsx.
- 2024-03-28 | CORE-001 | `7be6341e155d74c9d94a0f6ec7125ce55c4de1a2` | HSDM | fix: RES-105479, RES-105455 AppFramework E2E bugs. Files/symbols: HeaderWrapper.tsx; NotificationIconInitiator.tsx.
- 2024-03-28 | CORE-001 | `feec0cbf8d10b6561a0f39c128dd189fc7003215` | HSDM | fix: RES-105479, RES-105455 AppFramework E2E bugs. Files/symbols: LoggedInHeaderLayout.tsx.
- 2024-04-01 | CORE-001 | `c8d4132df0b92b7ba4f576dc8779fbe89ffb13f9` | HSDM | fix: RES-106137, RES-102181, RES-105991 Safari Company Name slowness. Files/symbols: AvatarMenu.tsx; HeaderWrapperStyles.tsx. Identical patch copies: `a7df3291c2c73f2b8d2391747f8aa6406fc7da51`.
- 2024-04-01 | CORE-001 | `2c4cdc421e64cc7cf11da175049c221864df02d8` | HSDM | fix: RES-106137, RES-102181, RES-105991 Safari Company Name slowness. Files/symbols: AvatarMenu.tsx. Identical patch copies: `247fbba408c4a9d1d9542d389952588ed96c5ae2`.
- 2024-04-01 | CORE-001 | `72e70dcffe256d0f519647243d03ebf7eb2f2cef` | HSDM | fix: RES-106137, RES-102181, RES-105991 Safari Company Name slowness. Files/symbols: AvatarMenu.tsx. Identical patch copies: `c0992d39060bc22dd0268afd428609b911d83376`.
- 2024-04-01 | CORE-018 | `2cffe0b8184ec71ef80c7064d74404af67aa7e3c` | HSDM | fix: RES-106378, RES-106379 E2E bugs. Files/symbols: DedupeCompareContentHeader.tsx; CreateProjectHeader.tsx. Identical patch copies: `3a46e8f85d98dce9eb0c68b7bce1e81672699868`.
- 2024-04-02 | CORE-001 | `578ebfabcc0d66a82e2eb96e3953768c955049b2` | HSDM | fix: RES-106516 e2e bugs. Files/symbols: HeaderWrapperUtils.ts; CreateProjectHeader.tsx.
- 2024-04-02 | CORE-037 | `7c6e73db489e54f8423c7c62e54ddb0f25691ca7` | HSDM | fix: RES-106516 e2e bugs. Files/symbols: app_v2/src/containers/intake/ManageIntake/ManageIntakeInitiator.tsx.
- 2024-04-02 | CORE-001 | `5286e13ba2653814007a48c1fb81571ebe0d7b78` | HSDM | fix: RES-106541 e2e bugs. Files/symbols: LoggedInHeaderLayout.tsx; symbols isSmScreen.
- 2024-04-02 | CORE-037 | `648f785274601dc8fb271aad6b365f943043338d` | HSDM | fix: RES-106458 MS Teams - Unable to navigate back to project. Files/symbols: app_v2/src/containers/project/audit-answers/AuditAnswersPageHeader.tsx.
- 2024-04-04 | CORE-001 | `13a9546dbce128dfe21cc2dd936220225b899995` | HSDM | fix: /RES-106915, RES-106688, RES-106592, RES-106443 App framework bugs. Files/symbols: AppLauncher.tsx; HeaderWrapper.tsx; symbols for, classList, themeModeClass.
- 2024-04-04 | CORE-001 | `e43c2fa4bce215714c19a04c7eae703f884f7992` | HSDM | fix: /RES-106915, RES-106688, RES-106592, RES-106443 App framework bugs. Files/symbols: AppLauncher.tsx.
- 2024-04-04 | CORE-001 | `e59e6697faced86b5588f687f86903158d9277de` | HSDM | fix: /RES-106915, RES-106688, RES-106592, RES-106443 App framework bugs. Files/symbols: AvatarMenu.tsx; ContentLibraryInitiator.tsx.
- 2024-04-04 | CORE-019 | `a2b385725947663b42ffef313a23e99d9a09ef78` | HSDM | fix: RES-106592 - Project discussion tab overflow. Files/symbols: ProjectHamburgerMenu.tsx.
- 2024-04-05 | CORE-001 | `05c90c88857e74908375ba86c4398d04698fedb8` | HSDM | fix: RES-106919 poppers are not getting closing on iframe click. Files/symbols: AppLauncher.tsx; AvatarMenu.tsx.
- 2024-04-08 | CORE-037 | `52ea0f034521e53729b1dba42d0ca2baf239cf53` | HSDM | fix: RES-106990 Clarification icons change. Files/symbols: app_v2/src/containers/project/project-view/ProjectHamburgerMenu.tsx; app_v2/src/containers/project/section-questions/question-details/QuestionMenu.tsx.
- 2024-04-08 | CORE-001 | `25b5f6b9103e673e9dbfa62274bb17142ccad9e1` | HSDM | fix: RES-107279 My account header space issue. Files/symbols: AppLauncher.tsx; AnalysisInitiator.tsx.
- 2024-04-10 | CORE-013 | `2ac69c765bd4a88bdbcebc31fba6ecf72bb6331d` | HSDM | feat: Org Feedback comments. Files/symbols: HeaderTitleAdornment.tsx; HeaderWrapperUtils.ts; symbols singlePageModules, darkModeEnabledModules, ManageBusinessUnitsHeader.
- 2024-04-11 | CORE-001 | `c89091de4f2a951476e40210964324cf8052861c` | HSDM | fix: RES-107926 Company logo image scaling. Files/symbols: LoggedInHeaderLayout.tsx; App.css.
- 2024-04-15 | CORE-018 | `bf165c2a5ff37ad3fc0d603eaeed7b7c7e3f7204` | HSDM | fix: RES-107917- Search bar location update in CCL. Files/symbols: ContentLibraryAddContentMenu.tsx; ContentLibraryStyles.tsx; symbols classes.
- 2024-04-15 | CORE-018 | `6ce8f60cf6f3271de22bc3a548031847f78aaba2` | HSDM | fix: RES-107917- Search bar location update in CCL. Files/symbols: HeaderLayout.tsx; ESignLifeCycle.tsx.
- 2024-04-15 | CORE-018 | `296aebc7b6a7619896f5493fb0764d7e78872250` | HSDM | fix: RES-107917- Search bar location update in CCL. Files/symbols: HeaderLayout.tsx; LinkedCompanySelector.tsx; symbols mdScreen.
- 2024-04-15 | CORE-018 | `b20ccee4d7fb72063935550ac7653ddd376bf886` | HSDM | fix: RES-107917- Search bar location update in CCL. Files/symbols: ContentLibraryAddContentMenu.tsx; HeaderLayout.tsx.
- 2024-04-15 | CORE-018 | `3587aeea1b24f2cfcce38555fdb61af876a30d51` | HSDM | fix: RES-107917- Search bar location update in CCL. Files/symbols: HeaderLayout.tsx.
- 2024-04-16 | CORE-033 | `97f57c685049fab69439325b6a156f5917313f84` | HSDM | fix: RES-107913 - Unable to load the instance (Accent Color issue). Files/symbols: app_v2/src/utils/ColorUtils.ts; symbols colorName.
- 2024-04-16 | CORE-018 | `e86101d8d5aca6bf9134680cf0af9377157da632` | HSDM | fix: RES-107917- Search bar location update in CCL. Files/symbols: LibraryReportHeader.tsx; symbols mdScreen.
- 2024-04-16 | CORE-018 | `6b78ca52a5f523b5bb0265f46e5851bf45e09a0e` | HSDM | fix: RES-108246 Responsive Screen Alignment issue. Files/symbols: HeaderLayout.tsx; symbols smScreen.
- 2024-04-19 | CORE-018 | `f13bca7c56b1779069ef90f868c37342a90550ea` | HSDM | feat: RES-107390, RES-109053 - Project Notification, CCL Search redesign. Files/symbols: AvatarMenu.tsx; HeaderWrapperUtils.ts; symbols menuItems, constructAvatarMenuItem, classes.
- 2024-04-19 | CORE-001 | `18a08cc57d6f9787d170e1c57b5aef5612e0466b` | HSDM | feat: RES-107390 - Pending Notification Queue Revamp. Files/symbols: AvatarMenu.tsx; HeaderWrapperUtils.ts; symbols menuItems, constructAvatarMenuItem, classes.
- 2024-04-22 | CORE-018 | `ace4713ecb4b44e233b4f750f6302dd7a733e5cb` | HSDM | feat: RES-108345 - CCL Search redesign. Files/symbols: HeaderLayout.tsx; ContentLibraryInputSearch.tsx. Identical patch copies: `3cf5374e3f4a83364083201d1d787ee0f346a90c`.
- 2024-04-22 | CORE-018 | `3fa51366e6c705e95e0447d2565d31dccd604d0b` | HSDM | feat: RES-108345 - CCL Search redesign. Files/symbols: ContentLibraryInputSearch.tsx. Identical patch copies: `ff1c85bb99b4206111fd14f27adaf2075ac42981`.
- 2024-04-22 | CORE-037 | `39b92a15b36f070069a3bd575a87f102068a8fb0` | HSDM | feat: RES-107390 - Pending Notification Queue Revamp. Files/symbols: app_v2/src/containers/project/sections/PendingNotificationsForSections.tsx. Identical patch copies: `adb3dc49fc2e37f18df84010a78caac6acadd1b0`.
- 2024-04-22 | CORE-018 | `71ca65c73aa9c9bac592254e03ca022b4849a1e4` | HSDM | feat: RES-108345 - CCL Search redesign. Files/symbols: ContentLibraryNavigationPane.tsx; ContentLibraryInputSearch.tsx; symbols partnerCompanyDetails, selectedPartnerCompany, isFilterPopperOpen. Identical patch copies: `35b836252b66fdb9308fb1027f11a46682e0a09b`.
- 2024-04-22 | CORE-018 | `4c69adb85b34d1aeeacddc46c5af1b04f04ae7c6` | HSDM | feat: RES-108345 - CCL Search redesign. Files/symbols: ContentLibraryInputSearch.tsx. Identical patch copies: `89e53fa76155cd3f3ae6cb19217e7374e1672a95`.
- 2024-04-22 | CORE-018 | `512a0942215a778ae9c8392dbe71999da996b6a3` | HSDM | feat: RES-108345 - CCL Search redesign. Files/symbols: LibraryReportHeader.tsx. Identical patch copies: `d079ad95deb0c0a51ca5cf44bed36c61bb1f64bd`.
- 2024-04-23 | CORE-001 | `701e00922e6389caf695cf4f95e53913a7ba7843` | HSDM | feat: RES-107390 - Pending Notification Queue Color change. Files/symbols: HeaderWrapperStyles.tsx; ProjectHeader.tsx. Identical patch copies: `4da0944b91b303771e05de73e240bd8af91744b1`.
- 2024-04-23 | CORE-037 | `b953c53b727cbef2ef03f92c6fd88b8008964e3a` | HSDM | feat: RES-107390 - Pending Notification Queue Color change. Files/symbols: app_v2/src/containers/project/ManageProjects/ProjectHeader.tsx; app_v2/src/containers/project/sections/PendingNotificationsForSections.tsx. Identical patch copies: `4c636e8dcc335433b7cd8398982215d998052c2e`.
- 2024-04-23 | CORE-018 | `fd5f242c22ecac7882d9e0d94a072ee7b6b7c54b` | HSDM | fix: RES-109053 - Empty Recent Search bug fix. Files/symbols: ContentLibraryInputSearch.tsx; ContentLibraryRecentSearch.tsx; symbols username, ContentLibraryRecentSearch. Identical patch copies: `599993eeba66a8b3238681ceec70d954fb6acc0c`.
- 2024-04-23 | CORE-001 | `60b4b2810041539880db3cd339ca01ceba27a6b0` | HSDM | fix: Org v2. Files/symbols: HeaderWrapperUtils.ts.
- 2024-04-23 | CORE-001 | `6d1d7c5f8fa54c3eac532f87e3872aa557af166d` | HSDM | fix: Org v2. Files/symbols: HeaderWrapperUtils.ts.
- 2024-04-24 | CORE-013 | `540ba0ab47c8a94fce12cc0dcb618c92d461b1c1` | HSDM | feat: RES-109104 Org Settings Global Store Update - Init. Files/symbols: UserDetailsStore.ts; CreateBUInitiator.tsx; symbols isSuperAdminOrSupportUser, updateCompanyPreferencesVO, userVOMap.
- 2024-04-25 | CORE-013 | `95c4166b6df351ff4fc3e09068d035009948fe36` | HSDM | feat: RES-109104 Org Settings Global Store Update. Files/symbols: BuFrameWorkComponents.tsx; BusinessUnitsUserDetails.tsx; symbols tagData, userMapConfiguration, usersList.
- 2024-04-25 | CORE-013 | `57db3da7a8caa9bca7c28153383397349a9a68d0` | HSDM | feat: RES-109104 Org Settings Global Store Update. Files/symbols: CreateBUInitiator.tsx; OrganizationUtils.ts; symbols businessUnitIdMap, getBatchProcessStatus, buList.
- 2024-04-25 | CORE-038 | `ddcbff222d541fc06d7d1ed4f4b22e5ee18eaaf2` | HSDM | Merge branch 'global_store_org_settings_dev3' of https://bitbucket.org/rfpioinc/rfp-app into app_dev2_conflict. Files/symbols: app_v2/src/organization-settings/containers/OrgFrameworkRenderers.tsx; app_v2/src/organization-settings/containers/OrgNavBar.tsx.
- 2024-04-25 | CORE-013 | `c99bfc83b455496a09e348cc137ab1f814af7e27` | HSDM | feat: RES-109104 Translation wrapper Change for Org v2. Files/symbols: OrgFrameworkRenderers.tsx; OrgNavBar.tsx; symbols allUsers.
- 2024-04-26 | CORE-013 | `e9f70f495027659e9aa9112688111941757735af` | HSDM | feat: RES-109104 Org Settings Global Store Update. Files/symbols: LoginSaveComponent.tsx; UserListFrameWorkComponents.tsx; symbols updateCompanyPreferencesVO.
- 2024-04-26 | CORE-013 | `844e0f366fdcb5bdf4cec0d4dac1bd6544d3bfdd` | HSDM | feat: RES-109104 Org Settings Global Store Update. Files/symbols: LoginSaveComponent.tsx.
- 2024-04-26 | CORE-013 | `7c80087115c6ae0f74433ead3c62bfd2af35499e` | HSDM | feat: RES-109104 Org Settings Global Store Update. Files/symbols: EmailPreferenceHeader.tsx; BulkUpdateUsersDrawer.tsx; symbols companyUsers, buMap, buList.
- 2024-04-30 | CORE-013 | `8cc10f7d1f32f488cadefa8f1def98a4aaef1706` | HSDM | fix: RES-109679, RES-109680, RES-109733, RES-109704 - Org Bugs. Files/symbols: UserDetailsStore.ts; OrganizationWrapper.tsx; symbols allUsers, permissionMap, temp.
- 2024-04-30 | CORE-033 | `09613847e977aec3aa3a636ce8013ccc10dee560` | HSDM | fix: translation wrapper bug fix. Files/symbols: app_v2/src/utils/useTranslationWrapper.ts; symbols useTranslationWrapper.
- 2024-04-30 | CORE-033 | `8eccf1618603225eca97026b3581b943a6e7dc22` | HSDM | fix: translation wrapper bug fix. Files/symbols: app_v2/src/utils/useTranslationWrapper.ts.
- 2024-05-02 | CORE-021 | `4f5fa8cf8d859aeed9ebe488c7547bb5ee479526` | HSDM | fix: RES-109676, RES-109677 Org Manage user bugs. Files/symbols: DisplayPrefContainer.tsx; RfpImageUpload.tsx.
- 2024-05-02 | CORE-021 | `d5b3954b9199f03809f62e112b570757e499b1cc` | HSDM | fix: RES-109890 Add user bug fix. Files/symbols: OrganizationWrapper.tsx; AddUserSaveComponent.tsx.
- 2024-05-03 | CORE-001 | `713b51065cb6241b0fc74bae1907582603706da2` | HSDM | feat: RES-109020 Notification icon Behavior update & Remove back arrow in Answering page. Files/symbols: HeaderWrapperStyles.tsx; NotificationIconInitiator.tsx.
- 2024-05-06 | CORE-001 | `b0d1367af199c47b9d88f67921ee6fc9cef3b133` | HSDM | feat: RES-109020 Notification icon Feedback. Files/symbols: HeaderWrapper.tsx; QuestionsControlView.tsx.
- 2024-05-07 | CORE-015 | `6239357966fe52630fae6fbab93cbe4cfd1d7b31` | HSDM | feat: RES-101711 Project Preference - Base layout & Other items. Files/symbols: OrganizationWrapperBodyRenderer.tsx; OrganizationWrapperHeaderRenderer.tsx; symbols ProjectPreferenceInitiator, AnswerLibraryPreferenceRenderer, styles.
- 2024-05-07 | CORE-015 | `28a704efb4ed7a4c2e0d612b4d5d37deabcb4ebd` | HSDM | feat: RES-101711 Project Preference - Base layout & Other items. Files/symbols: ProjectPreferenceContainer.tsx; ProjectPreferenceInitiator.tsx; symbols handleSave, forceCollapse.
- 2024-05-07 | CORE-015 | `5f047f030ba02d508f39e23172fac47161d2c261` | HSDM | feat: RES-101711 Project Preference - Base layout & Other items. Files/symbols: ProjectPreferenceContainer.tsx; ProjectPreferenceInitiator.tsx; symbols ProjectPreferenceContainer, preferenceMenuList, initStoreCallBack.
- 2024-05-07 | CORE-015 | `872fb262ed91f318bf7d1be6f7ea3328a9bed53c` | HSDM | feat: RES-101711 Project Preference - Base layout & Other items. Files/symbols: ProjectQuestionAttachmentRenderer.tsx; ProjectTimerRenderer.tsx; symbols showFooter, setFeaturePreferenceWithData, projTimerPrefrenece.
- 2024-05-08 | CORE-015 | `a56a98c34fab725abcf10ed9528a09b340a89d46` | HSDM | feat: RES-101711 Project Preference - Base layout & Other items. Files/symbols: ProjectQuestionAttachmentRenderer.tsx; ProjectTimerRenderer.tsx; symbols questionAttatchmentPrefrenece, questionAttatchmentData, showFooter.
- 2024-05-08 | CORE-015 | `6558321314d02f60db1018b043b1d907902e7fbc` | HSDM | feat: RES-101711 Project Preference - Base layout & Other items. Files/symbols: ProjectPreferenceContainer.tsx; symbols idx.
- 2024-05-08 | CORE-015 | `104140344c86a16ffdfe0126e6b1e1abfb6e7b7f` | HSDM | feat: RES-101711 Project Preference - Base layout & Other items. Files/symbols: ProjectPreferenceContainer.tsx.
- 2024-05-08 | CORE-033 | `68e851f6561c8c09a914456451f7918fdad2e642` | HSDM | fix: removing conflicted code. Files/symbols: app_v2/src/styles/App.css.
- 2024-05-09 | CORE-001 | `391572693abd92e968d515deabb1a4ee42c81a5a` | HSDM | feat: RES-109025 - App Framework Changes for Org Settings 2.0. Files/symbols: IconRenderer9dots.tsx; HeaderTitleAdornment.tsx; symbols newFeatureModules, isLandingPage, skipBreadCrumbs.
- 2024-05-10 | CORE-015 | `ca97997e75f7cfe0e8b9aa44810d3d12afb6de0c` | HSDM | fix: RES-110759 - Project preference loader fix. Files/symbols: HeaderTitleAdornment.tsx; ProjectPreferenceInitiator.tsx; symbols OrgLoader.
- 2024-05-10 | CORE-015 | `7fd3d8b47433749661ae483d17d2ac9108e66d6d` | HSDM | feat: RES-101711 Active Accordion Initialization. Files/symbols: ProjectPreferenceContainer.tsx; ProjectPreferencePropsType.ts; symbols ProjectTimerRenderer, ProjectQuestionAttachmentRenderer, getActiveAccordion.
- 2024-05-13 | CORE-015 | `ee9baa26e5c08226a54fb3575e8646e831f5c1e2` | HSDM | feat: RES-109963 - Response Projects - Preference - Import projects. Files/symbols: OrganizationWrapper.tsx; ProjectPreferenceContainer.tsx; symbols templateFileName, ImportProjectRenderer, colorStyle.
- 2024-05-13 | CORE-015 | `c28e386c9798092b274312145b74d47fb5c722cf` | HSDM | feat: RES-109963 - Response Projects - Preference - Import projects. Files/symbols: ProjectPreferenceContainer.tsx; ImportProjectRenderer.tsx.
- 2024-05-14 | CORE-015 | `4f1159e8bf88285609ad3e3ec9ce0b6285e15d0f` | HSDM | feat: RES-109963 - Response Projects - Preference - Import projects. Files/symbols: ProjectPreferenceContainer.tsx; ImportProjectRenderer.tsx; symbols ImportProjectRenderer, dialogHandlerData, broadCastDescription.
- 2024-05-14 | CORE-015 | `287266f1c788c47a793c0ff12ef5f0a98ff8d80d` | HSDM | feat: RES-109963 - Response Projects - Preference - Import projects. Files/symbols: AddUserSaveComponent.tsx; OrgSubLevelAccordion.tsx.
- 2024-05-15 | CORE-015 | `15106ecc3fa28e17eff61448cbb65336ef51f778` | HSDM | feat: RES-109963 - Response Projects - Preference - Import projects. Files/symbols: ProjectPreferenceInitiator.tsx; ImportProjectRenderer.tsx; symbols broadCastTitle, broadCastDescription.
- 2024-05-15 | CORE-015 | `6cb4e1e88005dda9a3b1690651d7fb523dff5695` | HSDM | feat: RES-109963 - Response Projects - Preference - Import projects. Files/symbols: ProjectPreferenceContainer.tsx; ImportProjectRenderer.tsx; symbols accordionSummary.
- 2024-05-15 | CORE-015 | `77e507bdc1d0e872890e0a9b3bb77d175b2eba2d` | HSDM | feat: RES-109963 - Response Projects - Preference - Import projects. Files/symbols: ProjectPreferenceInitiator.tsx; ImportProjectRenderer.tsx.
- 2024-05-15 | CORE-015 | `4cf6217b1f1a7b946e582f06d41f430312525b32` | HSDM | feat: RES-109963 - Response Projects - Preference - Import projects. Files/symbols: ProjectPreferenceInitiator.tsx; OrgBasicStyles.ts.
- 2024-05-15 | CORE-015 | `d0f635f3cda05d63e5a3be16629a6411b72c8fe0` | HSDM | feat: RES-109963 - Response Projects - Preference - Import projects. Files/symbols: ResponseProjectsService.ts.
- 2024-05-16 | CORE-015 | `720578b476e74d2f9f05baed570c84d4ec029a9b` | HSDM | feat: RES-109963 - Response Projects - Preference - Import projects. Files/symbols: ProjectPreferencePropsType.ts; ResponseProjectsService.ts; symbols getCompanyMetadata, response.
- 2024-05-27 | CORE-015 | `311245751b8a4736c385c886e69449ef3aa7c04d` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences - Project Metadata. Files/symbols: CheckBoxIcon.tsx; CustomFieldVO.ts; symbols CheckBoxIcon, theme, fillColor.
- 2024-05-27 | CORE-015 | `a7d805ac1bfed555b2c9d243e1ca720fac1c7de9` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences - Project Metadata. Files/symbols: ImportProjectRenderer.tsx; ProjectQuestionAttachmentRenderer.tsx; symbols templateFileName, groupedCustomFeildVO.
- 2024-05-28 | CORE-015 | `72a3e6353d90ce0785811d295dc9c543137a3dc4` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences - Project Metadata. Files/symbols: MetadataFrameworkRenderers.tsx; ProjectMetadataContainer.tsx; symbols changePrimaryContact, changePrimaryBuMap, resetValue.
- 2024-05-28 | CORE-015 | `9e9c65483f80eb890433ea9a3ce3176ecf3f72bb` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences - Project Metadata. Files/symbols: {ProjectMetadataCustomFeilds.tsx =&gt; ProjectMetadataCustomFields.tsx}; ProjectMetadataDefaultSettings.tsx; symbols defaultMetadataFields, getComponentByType, getDefaultMetadataFields.
- 2024-05-29 | CORE-033 | `a531ae7faded3024a69f4b72433590c6925afd69` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences - Project Metadata. Files/symbols: app_v2/src/organization-settings/utils/response-projects/preferences/ProjectMetadataHelper.ts; app_v2/src/rfp-components/RfpSelect.tsx; symbols tempVal, defaultOptValue.
- 2024-05-29 | CORE-016 | `27cb6fab02cfe2595eb844954c0ee129f179300b` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences - Project Metadata. Files/symbols: OrgCustomFieldsActionDrawer.tsx; ProjectMetadataHelper.ts.
- 2024-05-30 | CORE-015 | `79e2089b4e401e39c1d21926763f6b4796f2b612` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences - Adv Project Configuration. Files/symbols: ProjectPreferenceContainer.tsx; AdvProjectConfiguration.tsx; symbols AdvProjectConfiguration, commonStyles, companyPreferences.
- 2024-06-03 | CORE-015 | `429f93b974b5afc8f18632d19937bbbdd93aeece` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences - Adv Project Configuration. Files/symbols: ProjectPreferencesUtils.tsx; RfpToggle.tsx.
- 2024-06-03 | CORE-015 | `bd0cee66613291ef7e85cf84c5698e0649d5fdce` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences - Adv Project Configuration. Files/symbols: AdvProjectConfiguration.tsx; symbols value.
- 2024-06-04 | CORE-015 | `fe771534a4b52696465d87378465ab82ee68c21a` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences UAT feedbacks. Files/symbols: AdvProjectConfiguration.tsx; AlSaveOptionsCustomFields.tsx.
- 2024-06-05 | CORE-015 | `80eac3dd526b947179591c218f8ce3a1034b6ece` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences UAT feedbacks. Files/symbols: AdvProjectConfiguration.tsx; OrgSaveCancelComponent.tsx.
- 2024-06-07 | CORE-016 | `42f74b306d8ae8caa786ef8566dbe0e0c6c4e613` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences - Custom Fields. Files/symbols: salesForceInstanceListVO.ts; OrgFrameworkRenderers.tsx; symbols gettext, instanceDetails, CRMIconsRenderer.
- 2024-06-10 | CORE-016 | `172e6004b75b48a3a19b6df2125f58a4e722dc5e` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences - Custom Fields. Files/symbols: OrgFrameworkRenderers.tsx; OrgCustomFieldsListPage.tsx; symbols salesforceInstanceList, configSFDetails, hasBU.
- 2024-06-10 | CORE-016 | `f6e7b673be148cd58988c657bc9ad0e7a5bc70c3` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences - Custom Fields. Files/symbols: OrgFrameworkRenderers.tsx; OrganizationWrapperBodyRenderer.tsx; symbols validateCustomFieldList, CustomFieldsNameRenderer, ProjectCustomFieldListPage.
- 2024-06-10 | CORE-016 | `baf7bfef3f8a16a45401b06576be1b5e92dfcb60` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences - Custom Fields. Files/symbols: OrgFrameworkRenderers.tsx.
- 2024-06-10 | CORE-016 | `df311b4199560dd450dd882d692df249229a898d` | HSDM | feat: RES-106543 - 2.0 UX - Org Settings - Projects Preferences - Custom Fields. Files/symbols: WidgetsUtils.ts.
- 2024-06-11 | CORE-016 | `fa15454969ab34fe1acc424793c886385c4b254e` | HSDM | feat: RES-113894 - 2.0 UX - Org Settings - Projects Preferences - Reorder Custom Fields. Files/symbols: UserDetailsVO.ts; UserDetailsStore.ts; symbols OrgReorderCustomFields, setCompanyCustomFieldList, DefaultMergeTagFields.
- 2024-06-12 | CORE-016 | `c4a445fda2713a399e723b722bed1750548ed963` | HSDM | feat: RES-113894 - 2.0 UX - Org Settings - Projects Preferences - Reorder Custom Fields. Files/symbols: OrgCustomFieldsListPage.tsx.
- 2024-06-12 | CORE-016 | `866fecb86cd5d3030edb23a57e282ee81a492a2d` | HSDM | feat: RES-113894 - 2.0 UX - Org Settings - Projects Preferences - Reorder Custom Fields. Files/symbols: ContentLibUsedDiffModel.tsx; ProposalConfigureContent.tsx; symbols companyCustomFieldList, systemDefinedMergeTagList, companyCustomFieldsInStore.
- 2024-06-13 | CORE-016 | `00dfcff7265468ddfde88b6c690a7a6fadc46623` | HSDM | feat: RES-113894 - 2.0 UX - Org Settings - Projects Preferences - Reorder Custom Fields. Files/symbols: UserDetailsVO.ts; Store.ts.
- 2024-06-13 | CORE-016 | `b56a7efe32fd6357673bbe12c6d4f1bdefea73e6` | HSDM | feat: V1 streamlined debugging. Files/symbols: app-config.js; OrgCustomFieldsActionDrawer.tsx; symbols isDebuggerNeeded, configureRootScope, getRootScope.
- 2024-06-14 | CORE-016 | `79b576ff21a63bfeb03c6bc9961081e5a4d11988` | HSDM | fix: RES-114590 Issue in rendering default custom fields. Files/symbols: OrgCustomFieldsFrameworkRenderer.tsx; OrgCustomFieldUtil.ts.
- 2024-06-18 | CORE-016 | `538d77619114702279ac304a0ff3ed594d03cdc5` | HSDM | feat: RES-113898 - 2.0 UX - Org Settings - Projects Preferences - Add Custom Field. Files/symbols: ProjectCustomFieldListPage.tsx; OrgCustomFieldType.ts; symbols configures, OrgRadioIcon, OrgRadioCheckedIcon.
- 2024-06-18 | CORE-016 | `d9bf414863f5915f20c60c875a6bacaac7c267ca` | HSDM | feat: RES-113898 - 2.0 UX - Org Settings - Projects Preferences - Add Custom Field. Files/symbols: app-config.js; symbols isDebuggerNeeded, configureRootScope, getRootScope.
- 2024-06-18 | CORE-016 | `c0b6a24c5fb1dd48faeb376b1eec560c04524a25` | HSDM | feat: RES-113898 - 2.0 UX - Org Settings - Projects Preferences - Add Custom Field. Files/symbols: OrgCustomFieldsStore.ts; OrgRadio.tsx; symbols OrgRadio, customFieldTypeList, getOptionLabel.
- 2024-06-18 | CORE-016 | `39276198c7b49e6cce9ae740c00aaf5a328583d2` | HSDM | feat: RES-113898 - 2.0 UX - Org Settings - Projects Preferences - Add Custom Field. Files/symbols: OrgCustomFieldType.ts; OrgCustomFieldsPropsType.ts; symbols initialCustomFieldVO, customFieldCategory, projectTypeCustom.
- 2024-06-18 | CORE-016 | `33a6fbcc6b0a57d848f068b5bb74108bdd5fb031` | HSDM | feat: RES-113898 - 2.0 UX - Org Settings - Projects Preferences - Add Custom Field. Files/symbols: OrgCustomFieldType.ts; OrgCustomFieldsPropsType.ts; symbols prepares, handleChange, getAutoIncWarningMessage.
- 2024-06-19 | CORE-016 | `e9051957b249e4ca9c2e7faa04db5d6227c8f442` | HSDM | feat: RES-113898 - 2.0 UX - Org Settings - Projects Preferences - Add Custom Field. Files/symbols: OrgCustomFieldsActionDrawer.tsx.
- 2024-06-19 | CORE-014 | `757d32205a96c3c90da18bdfb4f0f12e937d97c1` | HSDM | fix: RES-115406 Unable to create project/intake in salesforce and Dynamics Iframe. Files/symbols: index.ts; symbols propertiesToBeDeleted, masterData.
- 2024-06-19 | CORE-014 | `5fd40278829e1ed1b82cb47726b7be723461cec4` | HSDM | fix: RES-115406 Unable to create project/intake in salesforce and Dynamics Iframe. Files/symbols: index.ts; symbols userDetails.
- 2024-06-21 | CORE-016 | `6b9c153fa9eaa2d0df15897f6a82b7d358d9f617` | HSDM | feat: RES-113898 - 2.0 UX - Org Settings - Projects Preferences - Add Custom Field. Files/symbols: OrgCustomFieldType.ts; OrgCustomFieldsPropsType.ts; symbols isValueAvailable, isFormTypeFilled, handleCustomFieldAction.
- 2024-06-21 | CORE-016 | `177e25fd7d12b40d525ce2dfc5f5d55f2479d27c` | HSDM | feat: RES-113898 - 2.0 UX - Org Settings - Projects Preferences - Add Custom Field. Files/symbols: OrgCustomFieldsActionDrawer.tsx.
- 2024-07-01 | CORE-014 | `f7872ad766570a3d995408d5b9541629224d3ec1` | HSDM | feat: RES-115508 - 2.0 UX - Org Settings - Custom Fields - Integrations. Files/symbols: CustomFieldVO.ts; salesForceInstanceListVO.ts; symbols getToolTipText, text, salesforceCRMDetails.
- 2024-07-01 | CORE-014 | `d5096f71d5f8de9e9cd018431dadc5f2b6b5908c` | HSDM | feat: RES-115508 - 2.0 UX - Org Settings - Custom Fields - Integrations. Files/symbols: OrgCustomFieldsStore.ts; OrgCustomFieldsActionDrawer.tsx; symbols isSearchableAndReportableType, hubspot, pipedrive.
- 2024-07-02 | CORE-017 | `75b0e9c8f08e1785a863a3e5a93ba0c12f95e7f3` | HSDM | feat: RES-113888 - 2.0 UX - Org Settings - Custom Fields - Search & Adv Filter. Files/symbols: OrgCustomFieldType.ts; OrgCustomFieldsActionDrawer.tsx; symbols uniqueWithinProject, restrictAutoIncremental, restrictDefaultCustomFields.
- 2024-07-02 | CORE-017 | `bbac9765e9fe2d5a4c86d72990c30fa140d2e37c` | HSDM | feat: RES-113888 - 2.0 UX - Org Settings - Custom Fields - Search & Adv Filter. Files/symbols: OrgCustomFieldsRenderers.tsx; OrgCustomFieldUtil.ts; symbols name, dataList.
- 2024-07-02 | CORE-016 | `f66c15be09458b4d4c69b63af83851e6680bfd4b` | HSDM | feat: RES-113888 - 2.0 UX - Org Settings - Custom Fields - Review comments. Files/symbols: salesForceInstanceListVO.ts; OrgCustomFieldsStore.ts; symbols ZOHOAssociationRenderer, isSalesforceAvailable, ZohoMappingRenderer.
- 2024-07-02 | CORE-016 | `68e7b54abcc6e8b7769bd44c6737f000aba4bb8d` | HSDM | feat: RES-110037 - 2.0 UX - Org Settings - CCL - Custom Fields. Files/symbols: OrganizationWrapperBodyRenderer.tsx; CCLCustomFieldsListPage.tsx; symbols CCLCustomFieldsListPage, CCLCustomFieldListPage, getContentScoreCustomFields.
- 2024-07-03 | CORE-016 | `ee9ad16f82e33b941c1bc23c45d752d2452ab652` | HSDM | feat: RES-110037 - 2.0 UX - Org Settings - CCL - Custom Fields. Files/symbols: CCLCustomFieldsListPage.tsx; OrgCustomFieldsListPage.tsx; symbols orgCustomFieldsColumnData, entityType, SFlist.
- 2024-07-03 | CORE-037 | `640ad54baad6f697edbb5d6af1d029bc3c0c9b70` | HSDM | fix: Reorder issue. Files/symbols: app/app/js/controller/settings/organizationCtrl.js; symbols disallowedGroupNames. Identical patch copies: `c696f035c5dcd443847f6b7cfe877c1b5d5141fc`.
- 2024-07-03 | CORE-016 | `1a0ef9451daed52fa1cbfd6d3fec2538d8601fa9` | HSDM | feat: RES-110037 - 2.0 UX - Org Settings - CCL - Custom Fields. Files/symbols: OrgFrameworkRenderers.tsx; OrgCustomFieldUtil.ts; symbols translatedValue, getTranslatedValue.
- 2024-07-03 | CORE-001 | `95cd420da23d2cc2edce4175a279d765896fd9cf` | HSDM | fix: RES-117264 Global Header color fix. Files/symbols: LoggedInHeaderLayout.tsx.
- 2024-07-04 | CORE-016 | `3fe280a5f292c95cd8b58e6d1086c5dd30d9d4b9` | HSDM | feat: RES-110037 - 2.0 UX - Org Settings - CCL - Custom Fields. Files/symbols: CustomFieldsDetailsStore.ts; OrgFrameworkRenderers.tsx; symbols UserStatusRenderer, translatedValue, hideDefaultValue.
- 2024-07-04 | CORE-016 | `12346026b5596cf0a6a9d3d113aabeab210cc9c6` | HSDM | feat: RES-110037 - 2.0 UX - Org Settings - CCL - Custom Fields. Files/symbols: OrgFrameworkRenderers.tsx; CCLCustomFieldsListPage.tsx; symbols UserStatusRenderer, quickStyles, orgCustomFieldsColumnData.
- 2024-07-04 | CORE-016 | `70ef22c314241a956f63fe5974434182d324d5e7` | HSDM | feat: RES-110037 - 2.0 UX - Org Settings - CCL - Custom Fields. Files/symbols: CCLCustomFieldsListPage.tsx; OrgCompWithLabel.tsx; symbols rowData, CustomFieldsValueRenderer.
- 2024-07-04 | CORE-009 | `14a4b3f65c8bdaaabea17e57e89fb7b1ca90c1df` | HSDM | fix: RES-117240, RES-117139 Tinymce Promise Handling. Files/symbols: tinymce.js.
- 2024-07-04 | CORE-001 | `600b9941d72ce3abb85df486f5b2405e801a2240` | HSDM | fix: RES-117264 Global Header color fix. Files/symbols: LoggedInHeaderLayout.tsx.
- 2024-07-05 | CORE-016 | `a5a77dd961f61cae1d991e1f437ef5a4f4e1a5b6` | HSDM | fix: RES-117371 Error on fetching CrmData. Files/symbols: OrgCustomFieldsService.ts; symbols response.
- 2024-07-05 | CORE-016 | `765fb0ea443e72c51c44c94f07fbf6941691311c` | HSDM | fix: RES-117482, RES-117371 Custom Field bugs. Files/symbols: OrgCustomFieldsActionDrawer.tsx; OrgCustomFieldsService.ts; symbols response.
- 2024-07-08 | CORE-013 | `053377d2a7aa818e99127637566a433584260c87` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav Initial Setup. Files/symbols: OrgSideNavUtils.ts; UserLoadDetailUtil.ts; symbols checkUserOptedInCcl, userDetails, uxPreference.
- 2024-07-08 | CORE-013 | `d5c2bf9ca5f4a32d06e55a8610609515cdf819a5` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav Initial Setup. Files/symbols: OrgCustomFieldsListPage.tsx; OrgSideNavUtils.ts; symbols systemDefinedCustomFieldsMap, isSupportUser, isSuperAdmin.
- 2024-07-09 | CORE-013 | `fc8402473809a56ea0fe66137a1aacdf9c463e61` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav Initial Setup. Files/symbols: OrgNavBarPropsType.ts; OrgSideNavHelper.ts; symbols checkUserOptedInCcl, userDetails, uxPreference.
- 2024-07-09 | CORE-013 | `f87c9deac53f7aa39b56adcf7e565ba7170edb2c` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav Initial Setup. Files/symbols: OrgNavBarPropsType.ts; OrgSideNavUtils.ts; symbols orgSubMenuItems, getParentIdentifier, getOrgSubMenuPermissionMap.
- 2024-07-09 | CORE-013 | `f76662e53414f0dedbd17e06237d3ab67872d206` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav Initial Setup. Files/symbols: OrgSideNavUtils.ts; symbols isRfpioLiteEnabled, isIntakeEnabled, raRootPermission.
- 2024-07-09 | CORE-013 | `d5964ab2c67637d287a7f77bab4e49b68b364ae4` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav Initial Setup. Files/symbols: OrgSideNavHelper.ts; OrgSideNavUtils.ts.
- 2024-07-09 | CORE-013 | `b69f3e7b75038c37b534eac42d7a200b2af6a8fe` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav New UI. Files/symbols: OrgNavBar.tsx; OrganizationContainer.tsx; symbols OrgSideNav, quickStyles, navStyles.
- 2024-07-10 | CORE-013 | `0f11a35177a887732a3c75a8547e450b3c441bca` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav New UI. Files/symbols: OrgSideNav.tsx; OrgSideNavScrollContainer.tsx; symbols page, selectedMenuUrl, configureActiveUrl.
- 2024-07-10 | CORE-013 | `06f035c250660960b3dfec18a688496fdcba20aa` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav New UI. Files/symbols: OrgSideNav.tsx; OrgSideNavScrollContainer.tsx; symbols scroll.
- 2024-07-15 | CORE-013 | `91f251da7051f1dab334a1462504228e07d0dfda` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav New UI. Files/symbols: HeaderTitleAdornment.tsx; HomePageContainer.tsx; symbols OrgNavBarItemRenderer, quickStyles, navStyles.
- 2024-07-15 | CORE-013 | `11ce0294bcfdfa6eb2c21b5ec13f240f9b0ca855` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav New UI. Files/symbols: OrgNavBarItemRenderer.tsx; OrgSideNavScrollContainer.tsx.
- 2024-07-16 | CORE-013 | `b5aa561e30c1a4f5ce935b5089501c35326aceff` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav New UI. Files/symbols: OrgSubMenuItemRenderer.tsx; symbols projectNotesName.
- 2024-07-16 | CORE-013 | `26f47f721608fe6fa587f2bf9e80c30b6bca49da` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav New UI. Files/symbols: FavouriteListRenderer.tsx; HomePageContainer.tsx.
- 2024-07-16 | CORE-013 | `cc57ff075e06810cd05fe0b065422d40b5daca5e` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav New UI. Files/symbols: OrgNavBar.tsx.
- 2024-07-16 | CORE-013 | `3cd417dfc6befe18d5a4b398f130961cb397b945` | HSDM | feat: RES-94862 - 2.0 UX - Org Settings - Left Nav New UI. Files/symbols: OrgNavBarPropsType.ts; OrgSideNavUtils.ts.
- 2024-07-17 | CORE-034 | `54e25624dffb247e821d8c07857e1619144ddaca` | HSDM | fix: RES-117591, RES-117593, RES-117594, RES-117669, RES-117689 Mac Issues. Files/symbols: ImportStylesDialog.tsx; DomainRestriction.tsx.
- 2024-07-17 | CORE-033 | `876b759e2ebb73be220583db6f23c6f2bb54f28b` | HSDM | fix: RES-117591, RES-117593, RES-117594, RES-117669, RES-117689 Mac Issues. Files/symbols: app_v2/src/organization-settings/styles/OrgSideNavStyles.tsx.
- 2024-07-17 | CORE-016 | `6915bec5a0f82119f09ef0ed65052cfc72275d5e` | HSDM | feat: RES-110037 CCL Custom Fields UAT Feedbacks. Files/symbols: OrganizationWrapperBodyRenderer.tsx; OrganizationUtils.ts.
- 2024-07-17 | CORE-016 | `fe150bbd28bfceba0b7c710eb7c98026cb23cd13` | HSDM | feat: RES-110037 CCL Custom Fields UAT Feedbacks. Files/symbols: OrgCustomFieldUtil.ts; symbols groupName.
- 2024-07-18 | CORE-033 | `88c7bd0dc720f6fd8e8acbb501354e21d7bd1eda` | HSDM | fix: Mac Browser back issue. Files/symbols: app_v2/src/utils/useSearchParamsState.ts; symbols location, searchParams.
- 2024-07-19 | CORE-016 | `b453ba1dc72738e5df19893c3b2e3121a39bd7e8` | HSDM | feat: RES-117265 - 2.0 UX - Org Settings - Custom Fields Feedbacks. Files/symbols: OrgCustomFieldsStore.ts; OrgCustomFieldsActionDrawer.tsx; symbols initCustomFieldReplicaVO, isCustomFieldEdited, handleClose.
- 2024-07-24 | CORE-016 | `fc6c8703c34eac911ddafca178cadbe6dd379de3` | HSDM | feat: RES-117265 - 2.0 UX - Org Settings - Custom Fields Feedbacks. Files/symbols: OrgCustomFieldsStoreImpl.ts.
- 2024-07-24 | CORE-016 | `c3fdb790d520faa62922e673cd2a37a8155a8c38` | HSDM | feat: RES-117265 - 2.0 UX - Org Settings - Custom Fields Feedbacks. Files/symbols: OrgReorderCustomFields.tsx.
- 2024-07-25 | CORE-033 | `715e63f9c43b2bc6a6ab72cd784bd3d906410916` | HSDM | feat: RES-118695 - 2.0 UX - Inter Font Anti Aliasing. Files/symbols: app_v2/src/components/header-wrapper/AvatarMenu.tsx; app_v2/src/components/header-wrapper/notificationpopup/NotificationPoperRenderer.tsx.
- 2024-07-25 | CORE-033 | `335f78034f966efbde3c92ef81f3f4123125ad96` | HSDM | feat: RES-118695 - 2.0 UX - Inter Font Anti Aliasing. Files/symbols: app_v2/src/components/header-wrapper/notificationpopup/NotificationPoperRenderer.tsx; app_v2/src/containers/login/Styles/LoginStyles.tsx.
- 2024-07-25 | CORE-033 | `15ba06c5fa653fbf596ca9787a65c82759122ec3` | HSDM | feat: RES-118695 - 2.0 UX - Inter Font Anti Aliasing. Files/symbols: app_v2/src/containers/guest_v3/guest-questionnaire-preview/PreviewQuestionsContainer.tsx; app_v2/src/containers/intake-survey/IntakeSurveyStyles.tsx; symbols LoginButton, LoginTextField, ExpandedActionsReportButtonStyles.
- 2024-07-25 | CORE-033 | `538aab1becfe628bb179814ede3899057d77f83a` | HSDM | feat: RES-118695 - 2.0 UX - Inter Font Anti Aliasing. Files/symbols: app/app/css/profile-center/App.css.
- 2024-07-25 | CORE-033 | `6df033744d1d26b797d026c93758caa79a638551` | HSDM | feat: RES-118695 - 2.0 UX - Inter Font Anti Aliasing. Files/symbols: app/app/css/profile-center/App.css.
- 2024-07-25 | CORE-033 | `6c2a78acc7fb6d9bca253e12eef275f36dcb88e9` | HSDM | feat: RES-118695 - 2.0 UX - Inter Font Anti Aliasing. Files/symbols: responsive-lite/src/styles/icons-fonts.css; responsive-lite/src/styles/index.css.
- 2024-07-25 | CORE-033 | `d8ef673e08b6e2776cdf0200910317611c95ae47` | HSDM | feat: RES-118835 Inter Font Root Update & Custom Fields Bugs. Files/symbols: app_v2/src/components/header-wrapper/HeaderWrapper.tsx; app_v2/src/components/header-wrapper/HeaderWrapperUtils.ts; symbols interFontEnabledModules.
- 2024-07-29 | CORE-034 | `b99340a8116c5f4d1f8453a786c2813046b2346e` | HSDM | fix: RES-117265 UAT translate missed. Files/symbols: OrgImportExportCustomFields.tsx.
- 2024-07-29 | CORE-013 | `1b9cdccb7fa54d0c2303639c2462d5fa2123741b` | HSDM | fix: RES-119337 Org Left Nav Active Color Update. Files/symbols: OrgNavBarItemRenderer.tsx.
- 2024-07-29 | CORE-013 | `386e32c2e2437fe306c9cbae53f1dc48ea4756c7` | HSDM | fix: RES-117265 UAT feedbacks. Files/symbols: OrgSideNavUtils.ts.
- 2024-07-30 | CORE-033 | `6203d99ee80ca0817136185ad7aa64cdab8c14cb` | HSDM | fix: Inter font Issue. Files/symbols: app_v2/src/organization-settings/containers/my-organization/user-management/manage-teams/edit-team/EditTeamsContainer.tsx; app_v2/src/organization-settings/interfaces/props-type/my-organization/user-management/ManageTeamsPropsType.ts; symbols handleSave, editTeamsCallback, TeamsLeftNav.
- 2024-08-02 | CORE-017 | `bb4ef8d11ae6ac41a24eda913ffec41a4b5376f9` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search Initial Setup. Files/symbols: OrganizationHeader.tsx; OrgSearchPropsType.ts; symbols quickStyles, onChange, input.
- 2024-08-02 | CORE-017 | `251dc138ed2168e1982952cd5638ea5a7c812878` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search Initial Setup. Files/symbols: OrgSearchUtils.ts; symbols notificationPreference, intakePreference.
- 2024-08-02 | CORE-009 | `090bb1e74b58e5bd68970d63f913bd9e9813c2b8` | HSDM | fix: RES-119906 Tinymce promise bug fix. Files/symbols: tinymce.js. Identical patch copies: `d84109327fcdc6f1bc3792328247037fe7147606`.
- 2024-08-02 | CORE-017 | `729ba85a5593a7aef1afd17291839a7d0db660f3` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search Initial Setup. Files/symbols: OrgSearchUtils.ts.
- 2024-08-06 | CORE-017 | `7de243e31f08efb1877d2b7890d9e968c68950dd` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search Setup. Files/symbols: OrganizationHeader.tsx; ManageRoleAddPage.tsx; symbols styles, proposalPreference, intakePreference.
- 2024-08-06 | CORE-017 | `107362e47055c2378c7f7a4941fb62cf7477f406` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search Setup. Files/symbols: OrgSearchCardRenderer.tsx; OrgSearchQuickFilter.tsx; symbols OrgSearchCardRenderer, hasPermission, OrgSearchCardItem.
- 2024-08-06 | CORE-017 | `a0a3fffd7e9e3e7e0384e67c57a2e0119f0d2f95` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search Setup. Files/symbols: OrgSearchHelper.ts.
- 2024-08-07 | CORE-017 | `ef8549454f33fd0c3cfd6dad1fbf425d6b37c64b` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search Setup. Files/symbols: OrganizationHeader.tsx; OrgSearchCardRenderer.tsx; symbols setPageTitle, setSearchConfigMap, configSearchPermissionMap.
- 2024-08-07 | CORE-017 | `30effebd8cdd4146b5b73d4db933a5792eed0548` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search Setup. Files/symbols: OrganizationHeader.tsx; OrgSearchCardRenderer.tsx; symbols recentlySearchedItems, OrgGradientOverLay, updateOrgPreference.
- 2024-08-07 | CORE-017 | `e759a0f88634df8b39263f47e36aff7842920945` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search Setup. Files/symbols: OrgSearchTile.tsx; App.css.
- 2024-08-08 | CORE-017 | `bd948c148e81ecf8dc46a407aee712453ec5ab5e` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search Setup. Files/symbols: OrganizationHeader.tsx; OrganizationWrapperHeaderRenderer.tsx; symbols triggerRecentSearch, onBeforeunload, recentlySearchedItems.
- 2024-08-08 | CORE-017 | `dbf03823816fbae80905561f2377bb354f3aab12` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search Setup. Files/symbols: HomePageContainer.tsx; OrganizationHeader.tsx; symbols orgPreference.
- 2024-08-08 | CORE-017 | `5834ead5ca6fd02d762db2557c3c231a4a25f462` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search. Files/symbols: OrganizationWrapperLayout.tsx; EmailPreferenceRenderer.tsx; symbols searchParams, parentAccordionList, key.
- 2024-08-08 | CORE-017 | `238a5ba3d1ba70b40623077a5f01045663bca6bd` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search. Files/symbols: OrgSearchTile.tsx.
- 2024-08-08 | CORE-017 | `1a2e78e53e25f5516003ca99e1c497b1fb7c1005` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search. Files/symbols: OrgSearchTile.tsx.
- 2024-08-08 | CORE-017 | `7d4670608b4cf1041bbacfc157a0bf0fa1ce327a` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search. Files/symbols: OrganizationUtils.ts.
- 2024-08-08 | CORE-017 | `feb08fd0976eb1878b447bce9f4ff767b24d6fb2` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search. Files/symbols: OrganizationHeader.tsx; LoginSettingsContainer.tsx.
- 2024-08-08 | CORE-017 | `7fc7f8835b182613e98e35300ac3208312b271b9` | HSDM | feat: RES-116824 - 2.0 UX - Org Settings - Global Search. Files/symbols: OrganizationHeader.tsx; OrgSearchUtils.ts; symbols userRole, companyPreferences, permissionData.
- 2024-08-08 | CORE-017 | `b49d9b80929bad11a07033909ef234fa1f9fa66b` | HSDM | fix: RES-120431, RES-120432 - Org search Bugs. Files/symbols: OrgSearchTile.tsx; CreateOrImportRelatedWords.tsx.
- 2024-08-08 | CORE-017 | `856bb9642ae1d0d5e3f40f8f62fc3bf823ab87d4` | HSDM | fix: RES-120431, RES-120432 - Org search Bugs. Files/symbols: OrgSearchHelper.ts.
- 2024-08-11 | CORE-017 | `8c4e719165036fb0e0162c1670e86045873093d1` | HSDM | feat: RES-120285 - 2.0 UX - Org Settings - Global Search Phase II. Files/symbols: OrgRecentsAndRecommendations.tsx; OrgSearchCardItem.tsx; symbols styles, isValidFirstTile, SearchTypeIconRenderer.
- 2024-08-11 | CORE-017 | `a806e84da0dfb5873c9bfb96f4c383cc624982dc` | HSDM | feat: RES-120285 - 2.0 UX - Org Settings - Global Search Phase II. Files/symbols: OrgRecentsAndRecommendations.tsx; OrgSearchCardRenderer.tsx; symbols recommendedItems, SearchTypeIconRenderer, isValidSearchCard.
- 2024-08-11 | CORE-017 | `e77984b66907a0857f10e426f3a6d5d3a4c27064` | HSDM | feat: RES-120285 - 2.0 UX - Org Settings - Global Search Phase II. Files/symbols: OrgSearchInitiator.tsx; OrgSearchHelper.ts.
- 2024-08-11 | CORE-017 | `cd8affee1a28e476cb070ca8bb0c928272d51987` | HSDM | feat: RES-120285 - 2.0 UX - Org Settings - Global Search Phase II. Files/symbols: OrgSearchInitiator.tsx; OrgSearchTile.tsx; symbols closeCallBack, primaryIdentifier, timeOut.
- 2024-08-12 | CORE-017 | `828325037abf151788807b45cfe0b7a7c96726f3` | HSDM | feat: RES-120285 - 2.0 UX - Org Settings - Global Search Phase II. Files/symbols: OrgSearchHelper.ts; OrgSearchLabelUtils.ts.
- 2024-08-12 | CORE-011 | `2dbda931fb514df93119bc3ab1fbc366c265db15` | HSDM | fix: RES-119564 - Security Translate Fix. Files/symbols: LoginPasswordPolicy.tsx; SecurityUtils.ts.
- 2024-08-12 | CORE-016 | `8ac04edb5a2c134538dfe733cbc8d33dd77d84fe` | HSDM | fix: RES-120537 - Projects - Custom fields - console error. Files/symbols: OrgCustomFieldsActionDrawer.tsx; symbols setOrgSearchIdentifier.
- 2024-08-12 | CORE-011 | `519241961e9572f94abaa7975b8d0484198a4162` | HSDM | fix: RES-119564 - Security Translate Fix. Files/symbols: LoginPasswordPolicy.tsx; SecurityUtils.ts.
- 2024-08-12 | CORE-011 | `7ad4fbd6ecd729cf5a0af08e26c840f89893d36e` | HSDM | fix: RES-119564 - Security Translate Fix. Files/symbols: LoginPasswordPolicy.tsx; SecurityUtils.ts. Identical patch copies: `e03cab96c45e14d69fc31df11a8e85648afbf409`.
- 2024-08-12 | CORE-017 | `a051c151029edc54cfc927c40bd2824ef7355f84` | HSDM | fix: RES-120705 - Org Sanity Bugs. Files/symbols: IntegrationListContainer.tsx; OrgSearchHelper.ts; symbols tab, filterdList.
- 2024-08-12 | CORE-017 | `38d4b1d2ef3c971723d6bab08ccf610f785ea3dc` | HSDM | fix: RES-120127 - Org Sanity Bugs. Files/symbols: OrganizationHeader.tsx; OrgCustomFieldsPropsType.ts; symbols isSupportUser, recentlySearchedItems, index.
- 2024-08-13 | CORE-016 | `79d50df28c9cfe2d8bb799601fb7489aaaa6c404` | HSDM | fix: RES-120127, RES-120226, RES-120353, RES-120532, RES-120536 - Org Bugs. Files/symbols: MSDynamicsCRMContainer.tsx; WebhookContainer.tsx; symbols instanceClone, index, customFieldReplicaVO.
- 2024-08-13 | CORE-011 | `ee73979c9ea8eec73d9cf6d6cfe8151d793d40d7` | HSDM | fix: RES-120127 - Org Sanity Bugs. Files/symbols: SSOScimInitiator.tsx; DomainRestriction.tsx; symbols timer.
- 2024-08-13 | CORE-013 | `c1476864c3283c34e59ce921c2d9703874fa203e` | HSDM | fix: RES-120793, RES-120810, RES-120831 - Org v2 E2E bugs. Files/symbols: NotificationInitiator.tsx; MailPreferences.tsx; symbols params, response, proposalRootPermission.
- 2024-08-14 | CORE-016 | `36d005f4b094cc77fe6e4373c13ffa749f2c5c91` | HSDM | fix: RES-120839, RES-120846, RES-120847, RES-120858, RES-120894, RES-120900, RES-120905 - Org Bugs. Files/symbols: OrgFrameworkRenderers.tsx; SSOContainer.tsx; symbols handleToggleChange.
- 2024-08-14 | CORE-012 | `364a462a346bb8e9b499a64d166f7f87f07f21e3` | HSDM | fix: RES-120896, RES-120971, RES-120983 - Org E2E bugs. Files/symbols: CreateBUInitiator.tsx; DisclosureAgreementInitiator.tsx; symbols DoorContainer.
- 2024-08-15 | CORE-016 | `440d085c21ecd6f7612a6a7bbbe3eea651418202` | HSDM | fix: Org E2E bugs. Files/symbols: CustomDomainAddDrawer.tsx; CreateBUInitiator.tsx; symbols setRefreshData, inputRef, isInValidPasswordPolicy.
- 2024-08-16 | CORE-017 | `d958881cefea9ef66108ed93480ae858f71b92f7` | HSDM | fix: RES-120766 - Org global Search duplicates rendering issue. Files/symbols: OrgSearchCardItem.tsx; OrgSearchCardRenderer.tsx; symbols validBreadCrumbAnchor, validSupportingBreadCrumb, isValidSearchTile.
- 2024-08-16 | CORE-016 | `bf8a9ab8fbcb2162f55259e1b3a3b6e78747f368` | HSDM | fix: RES-120879, RES-120971, RES-120845 - Org bugs. Files/symbols: CreateBUInitiator.tsx; EditBUPageInitiator.tsx; symbols SaveFooter, SaveCancelComponent, nonEditable.
- 2024-08-17 | CORE-012 | `5ed71f08a7d66cbd415e9b75a94d9131b7f7a3ac` | HSDM | revert: RES-120839 Code reverted based PO comment. Files/symbols: EditBUPageInitiator.tsx; EditBusinessUnitsPage.tsx; symbols lgScreen, handleToggleChange.
- 2024-08-20 | CORE-018 | `35ff6d74eefc4243efc40418f2751e715608cd11` | HSDM | fix: RES-121288 - Custom Stop Words, Related Word Restricting Duplicate. Files/symbols: CustomStopWordsRenderer.tsx; RelatedWordsEditDrawer.tsx; symbols hasDuplicate, idx.
- 2024-08-20 | CORE-009 | `d5b7927d675999629918afad1cc1d22d34569b10` | HSDM | fix: RES-118914 - Tinymce Hyperlink Style Removal. Files/symbols: plugin.js.
- 2024-08-20 | CORE-021 | `6ac186fdec6528488493d115a33708ee2fd7604b` | HSDM | fix: RES-121333, RES-121337, RES-121339, RES-121355 - Org Bugs. Files/symbols: HeaderWrapper.tsx; AdditionalDetailsRenderer.tsx; symbols isRequest, isInvitedVendor, darkEnabled.
- 2024-08-21 | CORE-016 | `ded6b290e89c6b90344099f0a49b8a10b89d07ed` | HSDM | fix: RES-121400, RES-121411 - Org E2E bugs. Files/symbols: OrgCustomFieldsActionDrawer.tsx; OrgCustomFieldUtil.ts; symbols crmOptions, displayText.
- 2024-08-21 | CORE-021 | `7a09ce99f8521d6908eefcb6cfa128975db70722` | HSDM | fix: RES-121339 - Org E2E bugs. Files/symbols: AddUserContainer.tsx; UserDetailsRenderer.tsx.
- 2024-08-21 | CORE-014 | `f92df6703036b2b5f35065e65bc02d7fc4ef2e79` | HSDM | fix: RES-121406 - Org Settings V1 Glitch. Files/symbols: SalesForceContainer.tsx; OrganizationStyles.tsx.
- 2024-08-21 | CORE-017 | `0bc4c6faebdd309a107acdf2423ad0e9444e315d` | HSDM | fix: RES-121562 - Org Global Search Width fix. Files/symbols: RfpRoundedSearch.tsx; symbols styles.
- 2024-08-22 | CORE-017 | `49df9a9892e4436b16198e35f633f5bce9e1675e` | HSDM | fix: RES-121353 - Irregular navigation in scim by global search. Files/symbols: SecurityTabHeader.tsx; SSOScimInitiator.tsx; symbols setOrgSearchIdentifier, timerRef, timeOut.
- 2024-08-23 | CORE-017 | `685859c0561cb689a2c0500d074c19ca71bf90f8` | HSDM | fix: RES-121873 Global search for the proposal builder bug fix. Files/symbols: OrgSearchHelper.ts; OrgSearchUtils.ts; symbols proposalRootPermission.
- 2024-08-23 | CORE-034 | `41109b96b2fe9073408ab413485697a4d7d5bdfa` | HSDM | fix: RES-121860 Unable to create announcement. Files/symbols: AnnouncementsInitiator.tsx.
- 2024-08-28 | CORE-012 | `f732a358457f431d9820168748e468d10626b9c4` | HSDM | fix: RES-121864 - Org bu bug. Files/symbols: BuUsersListPage.tsx; BusinessUnitsUserDetails.tsx; symbols filteredArray, disabled. Identical patch copies: `772a163198f2076fc5436b9d4c2e19dc6907cffe`.
- 2024-08-29 | CORE-011 | `e9ec3d353c98cabb010e2e46177212fe67a7e8b1` | HSDM | fix: RES-122184 - My Account - LCP/INP/CLS Improvement. Files/symbols: package.json; MyAccountBody.tsx; symbols ProfileIntitiator, SettingsInitiator, MyAccountPreferencesWrapper.
- 2024-08-30 | CORE-011 | `c34948473e6de98cb8ef21b4db7f3917a69a11bd` | HSDM | fix: RES-122184 - My Account - LCP/INP/CLS Improvement. Files/symbols: MyAccountPermissionDrawer.tsx.
- 2024-09-04 | CORE-011 | `53b49e66371dc8af455b5d99787adaada0803acc` | HSDM | fix: RES-122184 - My Account - LCP/INP/CLS Improvement. Files/symbols: webpack.prod.js.
- 2024-09-04 | CORE-011 | `b2f35407682deefe74b6ccf36f1f3a246e2b19c9` | HSDM | fix: RES-122184 - My Account - LCP/INP/CLS Improvement. Files/symbols: webpack.prod.js; symbols TerserPlugin, CssMinimizerPlugin.
- 2024-09-04 | CORE-011 | `6579ac3185474b9598b18b9d80974b4d7c4cb94a` | HSDM | fix: RES-122184 - My Account - LCP/INP/CLS Improvement. Files/symbols: package.json.
- 2024-09-09 | CORE-005 | `2b0db01b8170b1fb26470d16f1fe72fa1a79df49` | HSDM | revert: webpack config. Files/symbols: webpack.prod.js; symbols TerserPlugin, CssMinimizerPlugin.
- 2024-09-09 | CORE-005 | `a6120c2c94a0458059d2ff4813c1865063decd5d` | HSDM | revert: webpack config. Files/symbols: webpack.prod.js.
- 2024-09-09 | CORE-005 | `58d25fd962455d592c6894cbc473996726f8429c` | HSDM | revert: webpack config. Files/symbols: webpack.prod.js.
- 2024-09-09 | CORE-005 | `370bc71f3f73c4c10960c42a75537fefd5c78484` | HSDM | revert: webpack config. Files/symbols: webpack.prod.js; symbols TerserPlugin, CssMinimizerPlugin.
- 2024-09-16 | CORE-019 | `115c883628c4f1d49792537112500ca851f9bffd` | HSDM | perf: RES-120063 - My Work - Performance Improvement. Files/symbols: CommentTextBottomLayer.tsx; CommentUtils.ts; symbols editCommentFunc, levelAction, responseData.
- 2024-09-16 | CORE-019 | `9363f2bef02b00acae9304f5cf275de8991e205d` | HSDM | perf: RES-120063 - My Work - Performance Improvement. Files/symbols: MyWorkDiscussionStore.ts; MyWorkDiscussionStoreModel.ts; symbols fileIds, filteredComments, commentIds.
- 2024-09-16 | CORE-019 | `432f08b7c8a73d24d09ace1b4df9dd8163e0884f` | HSDM | perf: RES-120063 - My Work - Performance Improvement. Files/symbols: CommentTextBottomLayer.tsx; MyWorkDiscussionHeader.tsx.
- 2024-09-17 | CORE-016 | `c20571e36899205593ec7d6334266e1c426aa3e3` | HSDM | fix: RES-123638, RES-123366 Org Custom Field bugs. Files/symbols: OrgCustomFieldsStore.ts; OrgCustomFieldsActionDrawer.tsx; symbols customFieldReplicaVO, isSalesforceEnabled, isZohoEnabled. Identical patch copies: `eec2c320e1ea0682c989055401f005b302567328`.
- 2024-09-17 | CORE-016 | `522054c1ed43e3542d3d0b40f9ff193afe315768` | HSDM | fix: RES-123638, RES-123366 Org Custom Field bugs. Files/symbols: OrgCustomFieldsActionDrawer.tsx. Identical patch copies: `482d94780f6127e01525cb26ad19ae51f7eb9c76`.
- 2024-09-18 | CORE-016 | `8f246f7c91737e90403f5cf6388c19a50024cefc` | HSDM | fix: RES-124013, RES-124095 e2e bugs. Files/symbols: TinyMCECustomStyles.tsx; OrgCustomFieldsActionDrawer.tsx; symbols handleBlur, value. Identical patch copies: `209403a4f135d49d5aef8c9ca7bab895ce9dceb2`.
- 2024-09-18 | CORE-001 | `ce5ba073d461630c29b131f87ad68300d92b2d41` | HSDM | fix: RES-124056 E2E bugs. Files/symbols: NotificationIconInitiator.tsx; symbols currentCompanyId. Identical patch copies: `00a10bc87db5b5e0788b86e9bd3eb3bb0122359b`.
- 2024-09-18 | CORE-016 | `a76c02e5a9774981b643a3c99334fc0a763acf6e` | HSDM | fix: RES-124164, RES-124089 E2E bugs. Files/symbols: OrgCustomFieldsStoreImpl.ts; ThemeStoreImpl.ts.
- 2024-09-18 | CORE-016 | `8532cdfd9b0afc7fd6338c3d26e77f12ad723cde` | HSDM | fix: RES-124164, RES-124089 E2E bugs. Files/symbols: OrgCustomFieldsStoreImpl.ts; symbols filteredValues.
- 2024-09-18 | CORE-016 | `f709a630424acb5731f0400dd3e542e2291647fe` | HSDM | fix: RES-124164, RES-124089 E2E bugs. Files/symbols: OrgCustomFieldsStoreImpl.ts; symbols filteredValues.
- 2024-09-19 | CORE-014 | `2d8deb45d85b9048d0104e2110dcc4f2630ec83f` | HSDM | fix: RES-124089, RES-124112 E2E bugs. Files/symbols: ConnectionDetails.tsx; JiraContainer.tsx; symbols isJiraEnabled.
- 2024-09-19 | CORE-016 | `f3edcf58e5fe8ae111376a6278254ffab561e364` | HSDM | fix: RES-124083 E2E bugs. Files/symbols: OrgCustomFieldsActionDrawer.tsx; OrgCustomFieldsStoreImpl.ts; symbols customFieldTypeList, getCustomFieldTypeList, showAutoInc.
- 2024-09-19 | CORE-016 | `6692b7a45ea7aa3709e2693c53d3ac6b5035cf08` | HSDM | fix: RES-124083 E2E bugs. Files/symbols: OrgCustomFieldsStoreImpl.ts.
- 2024-09-19 | CORE-023 | `bc61821a660786520d009ce4f9dca48fd45e3def` | HSDM | fix: RES-124094 E2E bugs. Files/symbols: UserActivitiesFrameWorkComp.tsx; symbols history.
- 2024-09-20 | CORE-016 | `7d0d29508f1b5dcf654097b36deb2be8bd099257` | HSDM | fix: RES-124083 e2e bugs. Files/symbols: OrgCustomFieldsStoreImpl.ts.
- 2024-09-24 | CORE-019 | `9a9bc28119225aaa82282a3f20af2cd5e77779d9` | HSDM | perf: RES-120063 - My Work - Performance Improvement. Files/symbols: CommentUtils.ts; EntityNameRenderer.tsx; symbols projectName, currentDiscussionId, onSelectedCommentChange.
- 2024-09-24 | CORE-019 | `4638a9d1d0ad9bdafebb9defab483677d3dda14f` | HSDM | perf: RES-120063 - My Work - Performance Improvement. Files/symbols: EntityNameRenderer.tsx; MyWorkTaskVO.ts; symbols projectName.
- 2024-09-24 | CORE-019 | `e014399a67c35235dabd2a9d641c3b6554afc3b7` | HSDM | perf: RES-120063 - My Work - Performance Improvement. Files/symbols: DashBoardInitiator.tsx; MyWorkDiscussionStoreModel.ts.
- 2024-09-24 | CORE-034 | `39e2b06c43189067f94b7521dd0d16cc0bb78687` | HSDM | fix: RES-101565, RES-124923, RES-124673, RES-105513 Backlog issues. Files/symbols: QuestionCardLayoutStyles.tsx; ContentGuestPage.tsx; symbols defaultContentFormat, guestContentFormat, defaultStyle.
- 2024-09-24 | CORE-007 | `b8d726627f4c802c3d94a4106a762c84b13e2d90` | HSDM | fix: RES-101565, RES-124923, RES-124673, RES-105513 Backlog issues. Files/symbols: ContentGuestPage.tsx.
- 2024-09-25 | CORE-011 | `fbcfe0a2bbaccc13cb23258e6965a493fac8aef1` | HSDM | fix: RES-101565, RES-105513 Backlog Issues. Files/symbols: plugin.js; plugin.js; symbols defaultContentFormat, defaultTinymceFormat, finalContentFormat.
- 2024-09-25 | CORE-015 | `79971d569fef1f8d930841f8e60a687a3aa0e92c` | HSDM | fix: RES-105513, RES-124920, RES-125124 Backlog Issues. Files/symbols: MsAddAndApiTokenContainer.tsx; IpRestrictionBodyRenderer.tsx; symbols filteredObjects, nameMatch, typeMatch.
- 2024-09-26 | CORE-011 | `dbdfde35ab7ed442ea6e2770c2f084583b4e0a83` | HSDM | fix: RES-105513, RES-124920, RES-125124 Backlog Issues. Files/symbols: IpRestrictionBodyRenderer.tsx; App.css.
- 2024-09-27 | CORE-015 | `afbf0850c5f083104169ab89fe67e056885964ca` | HSDM | fix: RES-124743, RES-124920, RES-125124, RES-125352 Backlog issues. Files/symbols: CreateAnnouncementsDrawer.tsx; IpRestrictionBodyRenderer.tsx.
- 2024-09-28 | CORE-009 | `6404cdb9bdb1f275370001cda8f97d492cbfe28b` | HSDM | fix: RES-125494 Tinymce preview not working for default styles. Files/symbols: ProposalQuestionAnswerRenderer.tsx; RecommendationUtils.tsx; symbols RichTextContainer, RichTextValueRender, defaultContentFormat.
- 2024-09-29 | CORE-019 | `d8c2bd8f1da5c8d3af2ee1291cc8530786890221` | HSDM | fix: RES-125481 Discussion bug fix. Files/symbols: DiscussionChildComments.tsx; MyWorkDiscussionStoreModel.ts.
- 2024-09-29 | CORE-019 | `840c1990abb929b56944da18cf692cb104134f1c` | HSDM | fix: RES-125485 Issue in @mentioning users. Files/symbols: MyWorkDiscussionStoreModel.ts.
- 2024-09-30 | CORE-016 | `faca5f3ec6f65f7c95338208493a582605cee0ff` | HSDM | fix: RES-125495 Hitting spacebar selects all users in the collection. Files/symbols: CollectionManager.tsx; OrgAdvancedFilter.tsx; symbols handleKeyDown.
- 2024-10-01 | CORE-009 | `be876952aa6f9b9f3a731b29b2b77beb2b31ca3d` | HSDM | fix: RES-125561 Tinymce Cursor jumps on image upload. Files/symbols: TinyMCEUploadImage.tsx; symbols configureSelectionRange, timeOut.
- 2024-10-01 | CORE-009 | `8f9ecaca0e44ed752056be1c80faf20adddcecc1` | HSDM | fix: RES-125561 Tinymce Cursor jumps on image upload. Files/symbols: TinyMCEUploadImage.tsx.
- 2024-10-01 | CORE-009 | `5f4276d1b6a7113fc1ac4920025195cc140f5b74` | HSDM | fix: RES-125561 Tinymce Cursor jumps on image upload. Files/symbols: TinyMCECustomStylesInitiator.tsx; TinyMCERichTextWordImport.tsx; symbols configureTinymceSelectionRange, tinyMCE, applySelectionRange.
- 2024-10-01 | CORE-019 | `104f3316cbb8ee945515abb20d00447c7ffcbb32` | HSDM | fix: RES-125665 Discussion Invalid Input Bug fix. Files/symbols: MyWorkDiscussionStoreModel.ts; symbols projectId.
- 2024-10-03 | CORE-009 | `ffaeeabcbc1211d584ad9f0b903d2136eb3ec4ab` | HSDM | fix: RES-125717 - Tinymce unable to search styles (sporadic). Files/symbols: plugin.js; symbols createStyle.
- 2024-10-04 | CORE-009 | `60c4b6b7ea7beaec8bb6313f0e7609e453d4c3b7` | HSDM | fix: RES-71118, RES-75962 Tinymce prod errors. Files/symbols: plugin.js; symbols hasNoParentElement, parentElement, parentNodeName.
- 2024-10-10 | CORE-020 | `dd03ac62c4684ff4b7d5507d42f9bb48894f79a3` | HSDM | feat: RES-122166 - 2.0 UX - Package & Billing. Files/symbols: SendMessageDrawer.tsx}; HeaderWrapperUtils.ts; symbols darkModeEnabledModules, interFontEnabledModules, PlanUpdatesBanner.
- 2024-10-10 | CORE-020 | `c7ba7cd13cb74ffc8ea39450b23a577dc77c88f8` | HSDM | feat: RES-122166 - 2.0 UX - Package & Billing. Files/symbols: BillingCardLoader.tsx; BillingChartRenderer.tsx; symbols BillingDynamicDivider, smallScreen.
- 2024-10-15 | CORE-020 | `bf8189d5467b0434d970399d6e46c57e614d28b4` | HSDM | feat: RES-122166 - 2.0 UX - Package & Billing. Files/symbols: PlanUpdatesBanner.tsx; PlansAndBillingsInitiator.tsx; symbols percentUsed.
- 2024-10-15 | CORE-020 | `2216c6634abfdd1d2f6c0908bb52334a44896bae` | HSDM | feat: RES-122166 - 2.0 UX - Package & Billing. Files/symbols: PlanUpdatesBanner.tsx; BillingCard.tsx; symbols PlanRenderer, isOnlinePlan, isFreeRespond.
- 2024-10-15 | CORE-020 | `ffbb4baf422051ea7e7838e7f76f25804e2fc32c` | HSDM | feat: RES-122166 - 2.0 UX - Package & Billing Unit Test. Files/symbols: PlansAndBillings.test.tsx; PlansAndBillingsMockData.ts; symbols renderWithOptionalWait, ensureComponentHasBeenLoaded, waitForAsyncCondition.
- 2024-10-15 | CORE-020 | `34686a31e31f42198c69a0eee607813b86ff6e7a` | HSDM | feat: RES-122166 - 2.0 UX - Package & Billing Unit Test. Files/symbols: BillingCard.tsx; PlanRenderer.tsx; symbols costAmount, renewalDate.
- 2024-10-15 | CORE-020 | `ed9c6a699dc676462c5a13b152f38bcc65f4791f` | HSDM | feat: RES-126708, RES-126711 - 2.0 UX - Package & Billing Bugs. Files/symbols: BillingCard.tsx; PlanRenderer.tsx.
- 2024-10-16 | CORE-009 | `642aaae755068c63a1494aa1f9480576528de823` | HSDM | fix: RES-126739 - Tinymce resize issue when undocked. Files/symbols: skin.min.css.
- 2024-10-16 | CORE-009 | `ec76c85b81d44c095989f0acfca7eb3174194275` | HSDM | fix: RES-126739 - Tinymce resize issue when undocked. Files/symbols: skin.min.css.
- 2024-10-17 | CORE-020 | `aa2cfce98407582bc4e69a766ba7b7911e2dbe1f` | HSDM | feat: RES-122166 - 2.0 UX - Package & Billing Feedbacks. Files/symbols: SaveAndCancelRenderer.tsx; SendMessageDrawer.tsx; symbols progressValue, getPositiveValue, value.
- 2024-10-17 | CORE-009 | `57514605011d15ef35a745eb5958870c398f688f` | HSDM | fix: RES-64640 (Tinymce) Unable to remove annotation, console error. Files/symbols: plugin.js; RfpRichText.tsx; symbols closestParentAnnotation, applySelectionRange.
- 2024-10-17 | CORE-020 | `f4b81db1df187e0a020fc2f232cc05311fb43dd4` | HSDM | feat: RES-126978 - 2.0 UX - Package & Billing V1 sunset. Files/symbols: app.js; v2RedirectCtrl.js; symbols init, companyId, history.
- 2024-10-17 | CORE-020 | `22c2a79fa6563875c4ce8e5f787f5404e8605d9b` | HSDM | feat: RES-126978 - 2.0 UX - Package & Billing V1 sunset. Files/symbols: Utils.ts.
- 2024-10-21 | CORE-009 | `bcc5d502c999aa72c1713bb7115b46266b8354a2` | HSDM | fix: RES-127022 Tinymce Style Conversion fix. Files/symbols: plugin.js; TinyMCECustomStyles.tsx; symbols convertToPt, pxToPtRatio, parsedPxLength.
- 2024-10-24 | CORE-001 | `8b793d9d48da26a79f41c0fe01d4c5217560b5c7` | HSDM | feat: RES-126191 - Org Settings Mobile View HamBurger Support. Files/symbols: HamMenuIcon.tsx; HeaderTitleAdornment.tsx; symbols HamMenuIcon, NavIcon, theme.
- 2024-10-24 | CORE-024 | `4a93e2022f54638b47112e0fd4b0a05c8a83c1b6` | HSDM | feat: RES-127341 - 2.0 UX - Support Portal home page. Files/symbols: v2RedirectCtrl.js; loginCtrl.js; symbols isSupportUser, history, SupportHomeInitiator.
- 2024-10-25 | CORE-024 | `7871f9a4b172d3ab7439386a9490ae1ebb6c0284` | HSDM | feat: RES-127341 - 2.0 UX - Support Portal home page. Files/symbols: DialogSupportPortal.tsx.
- 2024-10-28 | CORE-001 | `966a576c92a57da8bee591e7de31bf5f71f74ba7` | HSDM | fix: RES-127846 - Support Portal App launcher support. Files/symbols: AppLauncher.tsx; SupportHomeInitiator.tsx; symbols onTileClick, urlPrefix.
- 2024-10-28 | CORE-009 | `39645b0d23613fe3a64b207d1f8b9a8f97ac4270` | HSDM | fix: RES-126350, RES-126584 Tinymce spacing bug fix. Files/symbols: plugin.js; MyWorkDiscussionStoreModel.ts; symbols getIsSameSpacingStyle, currentStyle, lineHeight.
- 2024-10-28 | CORE-016 | `3b470426239a906ab521d3682ebf24a1938daaab` | HSDM | fix: RES-125844 CCL CF bug fix. Files/symbols: OrgCustomFieldUtil.ts; symbols filteredCustomFieldTypeList.
- 2024-10-28 | CORE-017 | `17fa39e1deb30ea80232fec69d82b1b41af11f17` | HSDM | fix: RES-126191 - Org Mobile View Props types and ui color fix. Files/symbols: OrgHamBurger.tsx; OrganizationContainer.tsx; symbols OrgSearchResults, OrgSideNav.
- 2024-11-07 | CORE-016 | `c44a2e673559427d55003034baf5a8cfc50eff4c` | HSDM | fix: RES-127624 Autoincremental identifier name reverts. Files/symbols: OrgCustomFieldUtil.ts.
- 2024-11-07 | CORE-014 | `8bd5b71f1a5b3b5677831c6a1a78c0f9a248a560` | HSDM | fix: RES-127802, RES-128466, RES-128452 - Salesforce sync bug fix. Files/symbols: SalesForceContainer.tsx; ZohoCrmContainer.tsx.
- 2024-11-08 | CORE-009 | `42a640266cd4d82b49d342156808a25bcd1accee` | branch | fix: RES-128624, RES-128669 - Custom Fields reorder, Tinymce image blob fix. Files/symbols: OrgReorderCustomFields.tsx; OrgCustomFieldUtil.ts; symbols groupListMap, disallowedGroupNames, getGroupNameMapList.
- 2024-11-08 | CORE-009 | `64d5daeb1803ef23fb721aff97a685fe2231fbdc` | HSDM | fix: RES-128624, RES-128669 - Custom Fields reorder, Tinymce image blob fix. Files/symbols: OrgReorderCustomFields.tsx; OrgCustomFieldUtil.ts; symbols groupListMap, disallowedGroupNames, getGroupNameMapList.
- 2024-11-11 | CORE-009 | `903eb45009eb9a249d410777175772f5936d5616` | HSDM | fix: RES-128669 - Unable to copy paste image into TinyMCE Editor. Files/symbols: Editor.tsx.
- 2024-11-11 | CORE-022 | `736e6f38b35d3bebaf9a554a81345c6a966d0754` | branch | fix: RES-128629 Save button not appearing after turning off the Responsive AI. Files/symbols: ManageRoleAllPermissionContainer.tsx; ManageRolesUtils.ts; symbols toggleEnabled, configAdditionalPermission.
- 2024-11-11 | CORE-013 | `ce7c117548f4c01b42041f67423b0ea6b234bb31` | branch | fix: RES-128691 - Linked Content Subscription options automatically toggles off. Files/symbols: OrgPreferenceAccordianSummary.tsx.
- 2024-11-11 | CORE-013 | `66b70c9f54f6af54301de0a2f8f21373d96016d7` | HSDM | fix: RES-128629, RES-128691 Responsive AI , Linked Content Subscription permission bug fix. Files/symbols: ManageRoleAllPermissionContainer.tsx; OrgPreferenceAccordianSummary.tsx; symbols toggleEnabled, configAdditionalPermission. Identical patch copies: `5b9a212959a32807dad68593376c826f03bb0973`.
- 2024-11-12 | CORE-016 | `fbcc062bae3cadfebab821b25a0aa4f8ecf492c9` | HSDM | fix: RES-127624, RES-128466, RES-128452, RES-128624 - zendesk bugs. Files/symbols: SalesForceContainer.tsx; ZohoCrmContainer.tsx; symbols groupListMap, disallowedGroupNames, getGroupNameMapList.
- 2024-11-13 | CORE-023 | `1e8aa548bc9db605b6fefee7bc4978e792298602` | HSDM | perf: RES-128400 - Activities revamp. Files/symbols: ActivityDetailsVO.ts; OrganizationWrapperBodyRenderer.tsx; symbols OrgActivitiesContainer, activitiesStyles, ViewActivityDetails.
- 2024-11-13 | CORE-023 | `1950e901462f74e3d95970bf6806be60087525a0` | HSDM | perf: RES-128400 - Activities revamp. Files/symbols: OrgActivitiesContainerNew.tsx; OrgActivitiesProps.ts; symbols getActivitiesRowsCallBack, transformedQuery, query.
- 2024-11-14 | CORE-001 | `5b24bb2a961d59eb08e595aae16c73f21a84e04d` | HSDM | feat: RES-126191 - Org Settings Mobile View HamBurger Support. Files/symbols: HeaderTitleAdornment.tsx; LoggedInHeaderLayout.tsx; symbols theme, mdScreen, isSmScreen.
- 2024-11-14 | CORE-001 | `50fcb715ec01dbeff25996e9b96944ca143a2276` | HSDM | feat: RES-126191 - Org Settings Mobile View HamBurger Support. Files/symbols: HamMenuIcon.tsx; OrgHamBurger.tsx; symbols HamMenuIcon, NavIcon, OrgHamBurger.
- 2024-11-15 | CORE-016 | `604cdc3750f0665455d19435861f44092e2365f2` | HSDM | fix: RES-128876 - Custom Field Text Area to Text box. Files/symbols: OrgUserCustomFieldsRenderer.tsx.
- 2024-11-25 | CORE-022 | `84e394956b1255c362ed16fe7274b09ad2a4d7f3` | HSDM | feat: RES-126968 - Compare view Opt for Manage Roles. Files/symbols: ManageRoleAddPage.tsx; ManageRoleToggleView.tsx; symbols ManageRoleToggleView, currentToggleView, setCurrentView.
- 2024-11-25 | CORE-022 | `85280f1a5eee5dc09a8069df00dcaf9c9350de0d` | HSDM | feat: RES-126968 - Compare view Opt for Manage Roles. Files/symbols: ManageRolesCompareTable.tsx; RolesCompareViewTableCell.tsx.
- 2024-11-25 | CORE-022 | `755b9976c118f4bbcc013c1929c612d0f0234572` | HSDM | feat: RES-126968 - Compare view Opt for Manage Roles. Files/symbols: ManageRoleToggleView.tsx; ManageRolesCompareTable.tsx; symbols companyPolicyRoleMap, companyPolicyMap, moduleTranslationMap.
- 2024-11-26 | CORE-022 | `cb54b5c0dd6a0614aedc2b6f4609d298a798d3ae` | HSDM | feat: RES-126968 - Compare view Opt for Manage Roles. Files/symbols: RolesCompareViewTableCell.tsx.
- 2024-11-26 | CORE-022 | `3852ed8aec404807056355adb6b2dd34cf14d73a` | HSDM | feat: RES-126968 - Compare view Opt for Manage Roles. Files/symbols: RolesDraggableColumn.tsx.
- 2024-11-26 | CORE-022 | `14524a288a732b2e9c16aa8a48c591833fc47e21` | HSDM | feat: RES-126968 - Compare view Opt for Manage Roles. Files/symbols: ManageRolesPropsType.ts.
- 2024-11-28 | CORE-022 | `df21e37656ba5645d17ca89ca6b83deadbb6ac9d` | HSDM | fix: RES-130396, RES-130399, RES-130410 - Manage roles bugs. Files/symbols: ManageRoleListPage.tsx; ManageRoleToggleView.tsx; symbols isTabletDevice.
- 2024-11-29 | CORE-022 | `532c11ba6b26f428c41716cf0297bb92a1810a76` | HSDM | feat: RES-126968 - Compare view Opt for Manage Roles Jest Tests. Files/symbols: ManageRoleAddPage.tsx; ManageRolesInitiator.tsx; symbols getIteratableRoleModules, permissionUI, moduleArray.
- 2024-11-29 | CORE-022 | `76c215d1a1b7ab6771ed1d7fb85e37f4b5252a9c` | HSDM | feat: RES-126968 - Compare view Opt for Manage Roles Jest Tests. Files/symbols: ManageRoles.test.tsx.
- 2024-12-02 | CORE-022 | `a625c4ae6ab01728a0af8eca6fb96642a287f5b5` | HSDM | feat: RES-126968 - Compare view Opt for Manage Roles Feedbacks. Files/symbols: ManageRolesCompareTable.tsx; ManageRolesCompareView.tsx; symbols searchInputContainer.
- 2024-12-02 | CORE-022 | `8967b182a150b45289a49fd3d7fc0643664857d6` | HSDM | feat: RES-126968 - Compare view Opt for Manage Roles Feedbacks. Files/symbols: ManageRoles.test.tsx; symbols pinnedModuleColumn.
- 2024-12-02 | CORE-009 | `ceb1244323107158bbb19df51a8d37f1e4245219` | HSDM | fix: RES-129264 Error while pasting in mac. Files/symbols: plugin.js.
- 2024-12-02 | CORE-009 | `60ec726c70f56a0875aacac8ddcb9c48ccfc1fab` | HSDM | fix: RES-129264 Error while pasting in mac. Files/symbols: plugin.js.
- 2024-12-03 | CORE-009 | `74b65f1561fcf10ec24ba26343628b9398625a7b` | HSDM | fix: RES-129264 Error while pasting in mac. Files/symbols: TinyMCEUtils.ts.
- 2024-12-03 | CORE-009 | `8c05cd26714fb407bf35bcb7f3338ba557403201` | HSDM | Revert "fix: RES-129264 Error while pasting in mac". Files/symbols: TinyMCEUtils.ts.
- 2024-12-03 | CORE-009 | `bf14cea6fab130d1f56ed0aaecd7ced4865a12d5` | HSDM | Revert "fix: RES-129264 Error while pasting in mac". Files/symbols: plugin.js.
- 2024-12-03 | CORE-009 | `5cc5814e90aa98decdec3be5241dff7eb250eec0` | HSDM | Revert "fix: RES-129264 Error while pasting in mac". Files/symbols: plugin.js.
- 2024-12-10 | CORE-013 | `14d6ddb35c40030096759e7c51195ca89b756d3a` | HSDM | feat: RES-130274 - Currency Intl Format Support. Files/symbols: CustomFieldRenderer.tsx; IntakeGridCellRenderer.tsx; symbols companyCurrency, defaultConfig, getCurrencySymbol.
- 2024-12-10 | CORE-013 | `31ed0693e191803c767d68d787f9b23cd79fda09` | HSDM | feat: RES-130274 - Currency Intl Format Support. Files/symbols: CompanyDetailsInitiator.tsx; LocalizationAndLanguage.tsx; symbols getCurrencySymbol, currency, locale.
- 2024-12-17 | CORE-019 | `2c11bb6bb3fdde7ac7e373b7120d595c863c9037` | HSDM | feat: RES-132138 - To remove the engagement for Calendar view. Files/symbols: MyWorkHeader.tsx.
- 2024-12-17 | CORE-034 | `22fe9707917ae222e1f8861060aa1af000adfd2b` | HSDM | fix: RES-132299 - Currency not as expected. Files/symbols: CurrencyConfigUtils.ts.
- 2024-12-19 | CORE-025 | `0f5b1ba3f3c92d673a72f954b1e9830acf188103` | HSDM | feat: RES-130235 - 2.0 UX - Email Template - Section Bulk Submit for Review. Files/symbols: PreviewMailAndDeleteDialog.tsx; EmailView.tsx; symbols link, getEmailStyleSheet, basePath.
- 2024-12-19 | CORE-025 | `9ff1075566a21bbeb09f357fbf579c72ed4ae9c7` | HSDM | feat: RES-130235 - 2.0 UX - Email Template - Section Bulk Submit for Review. Files/symbols: main-style-sheet.css. Identical patch copies: `b2d172f3484d63ac5df159ce7fb5cdf430264519`.
- 2024-12-19 | CORE-025 | `e0786915d381ad824c0fafb41583a548b44955d9` | HSDM | feat: RES-130235 - 2.0 UX - Email Template - Section Bulk Submit for Review. Files/symbols: PreviewMailAndDeleteDialog.tsx; EmailView.tsx; symbols addEmailStyleSheet, link, removeEmailStyleSheet.
- 2024-12-19 | CORE-025 | `60ccee0659144cafd7a97a8de23511c615400a1e` | HSDM | feat: RES-130235 - 2.0 UX - Email Template - Section Bulk Submit for Review. Files/symbols: main-style-sheet.css.
- 2024-12-20 | CORE-025 | `62639c30743f833cec069eb9e01e0f0e26df80cb` | HSDM | feat: RES-130235 - 2.0 UX - Email Template - Section Bulk Submit for Review. Files/symbols: PreviewEmailTemplatePage.tsx.
- 2024-12-20 | CORE-025 | `79b3e49742ab84fd179f1cec6bf32ed24c1c1cbb` | HSDM | feat: RES-130235 - 2.0 UX - Email Template - Section Bulk Submit for Review. Files/symbols: main-style-sheet.css.
- 2024-12-20 | CORE-024 | `9db4da693531d4a9124833fe03f9035f024cd3d5` | HSDM | feat: RES-132429 - Support Portal 2.0 - UAT feedback story 2. Files/symbols: OrgWarningDialog.tsx; CompanyDetailsSaveComponent.tsx; symbols BillingDetailsSaveComponent, EditButton, currentEditMode.
- 2024-12-20 | CORE-024 | `cc535337d77652bdb9152c0add8fc69534da1a72` | HSDM | feat: RES-132429 - Support Portal 2.0 - UAT feedback story 2. Files/symbols: CompanyDetailsSaveComponent.tsx.
- 2024-12-20 | CORE-024 | `9a5040319deca870d664c307fc78f8fb3d5ee53b` | HSDM | feat: RES-132429 - Support Portal 2.0 - UAT feedback story 2. Files/symbols: SubscriptionInfo.tsx; SupportMasterModelVO.ts.
- 2024-12-20 | CORE-024 | `e28d6e7e8de2d2ead69de50908c59b24df8f45fe` | HSDM | feat: RES-132429 - Support Portal 2.0 - UAT feedback story 2. Files/symbols: DialogSupportPortal.tsx; symbols updateSaveCancelConfig.

### 2025 — 191 patch groups

- 2025-01-06 | CORE-025 | `6bd5cc6c5f625dd7bf4a04fb9232f7088272d737` | HSDM | fix: RES-132459 - Email Redirection UAT and sonar errors. Files/symbols: main-style-sheet.css.
- 2025-01-07 | CORE-025 | `675b04a79206fe0924e4622116b16af99012ccef` | HSDM | Revert "feat: RES-130235 - 2.0 UX - Email Template - Section Bulk Submit for Review". Files/symbols: main-style-sheet.css.
- 2025-01-08 | CORE-025 | `6da2e2afda2cb76a390267847e30aacd77a1efe8` | HSDM | fix: RES-132459 - Email Redirection 2.0. Files/symbols: main-style-sheet.css; rfpconstants.js; symbols getEmailStyleSheet, basePath, addEmailStyleSheet.
- 2025-01-08 | CORE-025 | `f14ea1be25aaff37c26686f46107ef958499d540` | HSDM | Revert "fix: RES-132459 - Email Redirection 2.0". Files/symbols: main-style-sheet.css; rfpconstants.js.
- 2025-01-08 | CORE-025 | `f599b65aedbb3bbad904267a7002f00dda87ab6a` | HSDM | fix: RES-132459 - Email Redirection 2.0. Files/symbols: main-style-sheet.css; PreviewMailAndDeleteDialog.tsx; symbols getEmailStyleSheet, basePath, addEmailStyleSheet.
- 2025-01-10 | CORE-016 | `0a8b029ac4b466f4f44b3066b99e8c3dd93619f8` | HSDM | fix: data-qa update. Files/symbols: CCLTagsFrameworkComponent.tsx; OrgCCLCollectionFrameworkComps.tsx.
- 2025-01-10 | CORE-025 | `58da0e14f3be5911a6ad673e71baf8e5d8909f6b` | HSDM | feat: RES-133744 - Dedicated DB email template migration. Files/symbols: main-style-sheet.css.
- 2025-01-13 | CORE-025 | `4979a0ba202a1f99def046a45ef152cd79765e3c` | HSDM | fix: RES-132459 - Email Redirection 2.0 Test. Files/symbols: PreviewEmailTemplatePage.tsx; symbols sanitizedContent, skipStyleConfiguration.
- 2025-01-22 | CORE-009 | `780d1784e1dd3760a75f38953c2d67d41e1050a4` | HSDM | fix: RES-135043 - Dialog focus issue tinymce. Files/symbols: NewRfpRichText.tsx.
- 2025-01-23 | CORE-033 | `3928c6c2d3303b08a08895bea6ff5c4e85bb8ba1` | HSDM | fix: RES-134967 - Google drive Label Fix. Files/symbols: app_v2/src/components/cloudStorage/GoogleDriveUpload.tsx; app_v2/src/containers/project/CloudAuthenticationDialog.tsx; symbols moduleTranslateMap.
- 2025-01-23 | CORE-034 | `a96c39ddfb4c4398933b72fe303ca03076bec8fb` | HSDM | fix: RES-133332 - Cursor jumps back on editing decimal point. Files/symbols: ContentFormatRenderer.tsx.
- 2025-01-23 | CORE-034 | `11f6a71d5c474c4c30432cb9e97b52ada544932b` | HSDM | Revert "fix: RES-133332 - Cursor jumps back on editing decimal point". Files/symbols: ContentFormatRenderer.tsx.
- 2025-01-23 | CORE-034 | `a3b42520fe3e2b13e1448a8fc5cf8af5face3cf4` | HSDM | fix: RES-133332 - Cursor jumps back on editing decimal point. Files/symbols: RfpTextField.tsx; symbols value.
- 2025-01-30 | CORE-025 | `932588e9eade36a485c928cc01c1f78329888bb6` | HSDM | feat: RES-135369 - Gmail client issues. Files/symbols: main-style-sheet.css; symbols is.
- 2025-01-30 | CORE-025 | `24f2b2343d6ebf834fef34b08c2525566ca04da8` | HSDM | feat: RES-135369 - Gmail client issues. Files/symbols: main-style-sheet.css; symbols is.
- 2025-01-30 | CORE-014 | `2ecf55892726799e6e4e66a6ac93fcff31f35186` | HSDM | feat: RES-130398 - SharePoint Not Listing Some Main Sites for Integration (Client). Files/symbols: SharepointContainer.tsx; IntegrationPropsType.ts.
- 2025-01-31 | CORE-034 | `ae89e3f558656340c15637ef97b37c98959c00c1` | HSDM | feat: RES-134661 - UI revisions for French - (Locale Support DayJS). Files/symbols: ResponsiveBase.tsx; DayjsUtils.ts; symbols localeMapping, configureDayjsLocale, defaultLanguage.
- 2025-02-03 | CORE-034 | `106c0eab4602bf08619301a6770ab0ccce0d7ee5` | HSDM | feat: RES-134661 - UI revisions for French - (Locale Support DayJS). Files/symbols: MyAccountUtils.ts; DisplayPreferenceRenderer.tsx; symbols supportedTransalteLangList, dayJSLocaleMapping.
- 2025-02-04 | CORE-025 | `740fa973b49c91986ba8bdcde7fbc42c38b6b66f` | HSDM | feat: RES-134791 - Email Template Source gainsight tracking. Files/symbols: BaseLayoutInitiator.tsx; LoginUtils.ts; symbols trackEmailSource, pathname, templateId.
- 2025-02-04 | CORE-025 | `ec986e4e0b2a8b2b3831753f74767f890fb1496c` | HSDM | feat: RES-134791 - Email Template Source gainsight tracking. Files/symbols: LoginUtils.ts.
- 2025-02-05 | CORE-025 | `cb3df92ede530890edb08e31e7f55bc63c248703` | HSDM | feat: RES-134791 - Email Template Source gainsight tracking. Files/symbols: LoginUtils.ts; symbols timeOut.
- 2025-02-05 | CORE-009 | `25bbaca1c93a103e97e34ba331a61f310a43c943` | HSDM | fix: RES-136512 - Tinymce spacing value are not getting unset. Files/symbols: plugin.js.
- 2025-02-07 | CORE-009 | `7855b51c988174911bca03f075f914ed6a064ebe` | HSDM | fix: RES-137080 - Tinymce linespacing incorrect values. Files/symbols: plugin.js.
- 2025-02-07 | CORE-009 | `6c72500ff63a69ef87d7fa9f35d37aa7f4119cc2` | HSDM | fix: RES-137080 - Tinymce linespacing incorrect values. Files/symbols: plugin.js.
- 2025-02-07 | CORE-009 | `211f28cf5a5215cf5cc3c1b34380547ae90eeb1b` | HSDM | fix: RES-137080 - Tinymce linespacing incorrect values. Files/symbols: CopyClipUtils.ts.
- 2025-02-07 | CORE-009 | `bc499037483eb5a1f1f78474670ca513f56b5ac4` | HSDM | TinyMCEUtils.ts edited online with Bitbucket. Files/symbols: TinyMCEUtils.ts; symbols parentFontSize.
- 2025-02-07 | CORE-009 | `78359de474d22410ab1e00279ac36c3d0aff296d` | HSDM | UserLoadDetailUtil.ts edited online with Bitbucket. Files/symbols: UserLoadDetailUtil.ts.
- 2025-02-07 | CORE-009 | `6b58d628e4554fb705a31fe809cbb885a5432bbb` | HSDM | fix: RES-137080 - Tinymce linespacing incorrect values. Files/symbols: plugin.js; symbols tinyClassFontSize.
- 2025-02-14 | CORE-009 | `da8071c772147c8e53261671d8cc746bd3a1b450` | HSDM | feat: RES-137166 - Ability to retain styles in new rows in a table. Files/symbols: plugin.js; symbols processList, childIndex, targetList.
- 2025-02-14 | CORE-009 | `2de4afd8dd3431d0f18f83746d46d2f267e45a4b` | HSDM | feat: RES-137166 - Ability to retain styles in new rows in a table. Files/symbols: plugin.js; symbols selection, currNode, nextRowElem.
- 2025-02-16 | CORE-036 | `83a2d02bee18067ed75e9a3f57f7ad0eb6243493` | branch | feat: voice support search for org v2. Files/symbols: package.json. Identical patch copies: `9aabad8a1604377e6c836c79eacd1e9437f476ac`.
- 2025-02-18 | CORE-009 | `3afbe30015e557ba718c526bb1c06cb247a994e7` | HSDM | feat: RES-102896 - Word/Character Count Limits on Full Rich Text. Files/symbols: AnswerOptionValidation.tsx; AnswerViewDialog.tsx; symbols completeAnswerVO, newAnsVO, totalChars.
- 2025-02-19 | CORE-013 | `1576b136e627c737e80436ce4c8e3eb91925ae78` | HSDM | fix: RES-137952 - Able to access Responsive AI in OrgSettings via URL. Files/symbols: HomePageContainer.tsx; OrganizationContainer.tsx; symbols permissionMap, companyPreferences, isOrgPermissionLoaded.
- 2025-02-19 | CORE-013 | `89f43928bad2c1c32c593376c59850c6c5c64783` | HSDM | fix: RES-137952 - Able to access Responsive AI in OrgSettings via URL. Files/symbols: OrganizationContainer.tsx; symbols PermissionLoader, companyPreferences, setOrgSubMenuPermissionMap.
- 2025-02-19 | CORE-015 | `4bbdd3370ce90b35679486940377995355fe2248` | HSDM | fix: RES-137562, RES-137971 - Image Url Broken. Files/symbols: IntegrationUtil.ts; ConnectedAppsContainer.tsx.
- 2025-02-24 | CORE-036 | `9c0b0c281a1769f9b5c856e6d92f5875665869a4` | branch | feat: org voice search. Files/symbols: OrgSearchResults.tsx; OrgSearchPropsType.ts.
- 2025-02-24 | CORE-014 | `aef9068169551da3070c3e968cb0719a318b3924` | HSDM | fix: RES-138757 - Something Went Wrong on Intake Salesforce. Files/symbols: IntakeHamburgerMenu.tsx.
- 2025-02-26 | CORE-009 | `6a8f52323bf86128139601b21c12d42889cd8321` | HSDM | feat: RES-139002 - Addition of Character limit option. Files/symbols: HeaderTitleAdornment.tsx; AnswerViewDialog.tsx; symbols newFeatureModules, tempPanel.
- 2025-02-27 | CORE-009 | `3edff241506b3bf99a931dfcee433dd447f4dca0` | HSDM | feat: RES-139002 - Addition of Character limit option. Files/symbols: AnswerViewDialog.tsx; AnswerTypeTableContent.tsx.
- 2025-02-27 | CORE-009 | `d523e91e86e509520c35b04359b6457d6a0150a4` | HSDM | feat: RES-139002 - Addition of Character limit option. Files/symbols: AnswerViewDialog.tsx; AnswerTypeTableContent.tsx; symbols companyId, restrictCharacterLimit.
- 2025-03-06 | CORE-033 | `d1db9bb5f2ecccfa1220bdbfb50f281974a5e074` | HSDM | fix: RES-138902 - overlay scroll fix. Files/symbols: app_v2/src/organization-settings/styles/OrgBasicStyles.ts.
- 2025-03-06 | CORE-021 | `b8de07ce7b78d68c56a9125d94ade608f170406a` | HSDM | fix: RES-138902 - overlay scroll fix. Files/symbols: UserInfoContainer.tsx; OrgBasicStyles.ts.
- 2025-03-07 | CORE-014 | `9d92eff0a60d55f30178b7cde092d4d28872b231` | HSDM | fix: RES-139689 - Floating-point number is retrieved from Salesforce. Files/symbols: CRMutil.ts; symbols roundFloat.
- 2025-03-10 | CORE-014 | `c9619a2033e4851b093ddba8e27ce631c5902d07` | HSDM | fix: RES-139689 - Floating-point number is retrieved from Salesforce. Files/symbols: CRMutil.ts.
- 2025-03-14 | CORE-024 | `88a5fd7c1f32d89326caacd94702fa5e4ba98dc3` | HSDM | fix: RES-140187 - Support Portal style sheet conflict. Files/symbols: HeaderWrapperUtils.ts; LoggedInHeaderLayout.tsx; symbols supportPortalModules, styleSheetUrls, addSupportStyleSheet.
- 2025-03-14 | CORE-024 | `e1749ac341dbcb8176783719026e11e9f71e8350` | HSDM | fix: RES-140187 - Support Portal style sheet conflict. Files/symbols: UserActivity.css; main.css.
- 2025-03-14 | CORE-025 | `34e269231dcb816581997275fc96490188c5eb1f` | HSDM | fix: RES-140336 - notification email redirection. Files/symbols: NotificationCardRenderer.tsx; PreviewMailAndDeleteDialog.tsx; symbols commonClass.
- 2025-03-14 | CORE-025 | `fa2e2679e1a3f3359d97571f88a891aac4b755b3` | HSDM | fix: RES-140432 - Mail visibility Issue. Files/symbols: main-style-sheet.css.
- 2025-03-14 | CORE-025 | `881619d7e8de243cdda4775ef1a393fc243263f6` | HSDM | fix: RES-140432 - Mail visibility Issue. Files/symbols: main-style-sheet.css.
- 2025-03-18 | CORE-001 | `f6dd4d7cd38461b6e7a76790b7f0a3474b489891` | HSDM | fix: RES-107384 - Safari anchor tag support. Files/symbols: AppLauncher.tsx.
- 2025-03-19 | CORE-034 | `0ae30db3a7313eea81354b5b13bcd2e1adaaffb7` | HSDM | fix: RES-140294 - Announcement Timezone issue. Files/symbols: AnnouncementsUtils.ts; symbols updated_date.
- 2025-03-28 | CORE-013 | `efbb8d5ea124c112f38869cb5760fa818a15fdd3` | branch | feat: RES-141396 - Org Settings Circular dependency. Files/symbols: OrgActivitiesContainerNew.tsx; OrgActivitiesHeader.tsx; symbols viewActivityStyles, frameworkComponents, listArray.
- 2025-04-02 | CORE-013 | `e74afb7eb487085c80d78147f7f99052aff5a1ce` | branch | feat: RES-141396 - Org Settings Circular dependency. Files/symbols: EmailTemplateListPage.tsx.
- 2025-04-02 | CORE-016 | `56980cca87d5f7fa85c980139c23e8187a8144ae` | HSDM | fix: RES-141777 - Org Custom Fields Error Handling. Files/symbols: OrgCustomFieldsRenderers.tsx; symbols salesforceCRMDetails, isCRMDetailsLoaded.
- 2025-04-21 | CORE-025 | `2bd3b51082262457a7fdacc97403bcb8a7324fd4` | HSDM | fix: RES-142470 - Outlook Rendering issue. Files/symbols: generated/dependency/empty metadata; no original feature inference.
- 2025-04-23 | CORE-021 | `d037ee9ac360fe9cb581418b500bef8ed8bfb9c6` | HSDM | fix: RES-143943 remobe user not showing in manage user. Files/symbols: ManageUserListUtils.ts.
- 2025-04-23 | CORE-021 | `208fa3d9b9057980f246e927c500466126f70b73` | HSDM | fix: RES-143943 removve user not showing in manage user. Files/symbols: ManageUserListUtils.ts; symbols hasAccess.
- 2025-05-07 | CORE-014 | `e7477c7c648a55ac89ee2bc77802958d94b42d22` | HSDM | fix: RES-144011 Unable to save sharepoint details. Files/symbols: SharepointContainer.tsx.
- 2025-05-08 | CORE-014 | `664f812bf1ef8e85ee1bb16033ad29cc4853baf8` | HSDM | fix: RES-144011 Unable to save sharepoint details. Files/symbols: SharepointContainer.tsx; CRMutil.ts.
- 2025-05-22 | CORE-021 | `311d069eac17e40035af90c70e68953f56bd7e8f` | HSDM | fix: RES-144726, RES-144314 e2e bugs. Files/symbols: ManageUserListUtils.ts; SalesForceContainer.tsx.
- 2025-05-27 | CORE-016 | `d67c8b97a4ed7038f83c53dcc5e17c320032926b` | HSDM | fix: RES-145860, RES-146683, RES-146735 backlog bugs. Files/symbols: OrgCustomFieldsActionDrawer.tsx; OrgCustomFieldsAdvancedSearch.tsx; symbols timeOut, isLayoutSwitched, firstDndColumnInput.
- 2025-05-27 | CORE-016 | `112bdd5f645bcea43a9241099de63d985a765b6a` | HSDM | fix: RES-145860, RES-146683, RES-146735 backlog bugs. Files/symbols: OrgCustomFieldsActionDrawer.tsx.
- 2025-05-29 | CORE-016 | `86ccdc666eeca9f308ae790f57eede70c6a5b959` | HSDM | fix: RES-145860 backlogs bugs. Files/symbols: OrgCustomFieldsActionDrawer.tsx; symbols handleCursorFocus.
- 2025-05-30 | CORE-016 | `6f4996c8b78e08d9e81fea1d1c0f6b5a3a8c92fa` | HSDM | fix: RES-145860 backlogs bugs. Files/symbols: OrgCustomFieldsActionDrawer.tsx.
- 2025-06-12 | CORE-035 | `8a8b90bc6673037fba4acd8d433042a36580f606` | branch | feat: RES-147812 - Search embeddings based on response header. Files/symbols: FilterConstants.ts; FilterContext.tsx; symbols plainFields, plainFieldsNameMap, getOptions.
- 2025-06-15 | CORE-035 | `4700a2056b785b80d8e48f3d20d095e3cf54bce9` | branch | feat: RES-147812 - Search embeddings based on response header. Files/symbols: AgentChatRenderer.tsx; FilterContext.tsx; symbols isFiltersChanged, oldFilters, refineFilters.
- 2025-06-16 | CORE-035 | `e790ace2f9ab6f5bc14bfaa73f6e922abd7daf4c` | HSDM | feat: RES-147812 - Search embeddings based on response header. Files/symbols: AgentChatRenderer.tsx; FilterConstants.ts; symbols isFiltersChanged, oldFilters, refineFilters.
- 2025-06-17 | CORE-035 | `5f9388b4b68b9cc87aeb65674a9633f2cca29eb0` | HSDM | feat: RES-147812 - Search embeddings based on response header. Files/symbols: AiUtils.ts.
- 2025-06-19 | CORE-035 | `fa5e1f81a1a03a8aa0b7cddb2a59a5d7a30965b9` | HSDM | fix: RES-149361 - AI response header bug fix. Files/symbols: AiCreateDataset.tsx; AiDatasetUtils.tsx.
- 2025-06-24 | CORE-035 | `dd90ecd160d3a311b79322b420f347093a68d01d` | HSDM | fix: RES-149361 - AI response header. Files/symbols: FilterActions.tsx; FilterPopover.tsx; symbols isResponseHeaderFilterEnabled.
- 2025-06-24 | CORE-035 | `f3e5752e462ee3c7a39d25fcebadba388237a2b8` | HSDM | fix: RES-149361 - AI response header. Files/symbols: AutoPilotChatInputContainer.tsx; ChatInputContainer.tsx.
- 2025-06-24 | CORE-035 | `c131a6ae5f4bb644b0a71df1f27a5b72e819f43c` | HSDM | fix: RES-149361 - AI response header. Files/symbols: FilterContext.tsx; symbols isResponseHeaderFilterEnabled.
- 2025-07-02 | CORE-009 | `12548aecb42a9556af0d7b63441e7d8563535507` | HSDM | feat: RES-150696 - Changing the Image Editor Plugin for TinyMce. Files/symbols: plugin.js; plugin.js; symbols t, m, h. Identical patch copies: `5f2619628ae7586f76de7c24be39f033abdc41ee`.
- 2025-07-02 | CORE-009 | `59c2f40b35325fbb463cc215e7c21c7f1d8665b9` | HSDM | feat: RES-150696 - Changing the Image Editor Plugin for TinyMce. Files/symbols: plugin.js. Identical patch copies: `bd21bc8edc0f043c5a84aaebbb9979c321165870`.
- 2025-07-02 | CORE-024 | `42a452aaf54e3b91d415229edb640f2e2003542c` | HSDM | feat: RES-150714 - Support Portal Pod name handling. Files/symbols: CreateCompanyDialog.tsx; SuggestionListVO.ts; symbols currentPodName. Identical patch copies: `8346b8c525d490e8a8edf1fae4500f08b5258f32`.
- 2025-07-03 | CORE-024 | `4048840055f632a59c808172283f630b83574936` | HSDM | feat: RES-150714 - Support Portal Pod name handling. Files/symbols: OrganizationContainer.tsx.
- 2025-07-06 | CORE-024 | `c101760a7580441b99ad0449c27301bdee81a6a8` | HSDM | feat: RES-150714 - Support Portal Pod name handling. Files/symbols: OrganizationContainer.tsx; CreateCompanyDialog.tsx; symbols isPodNameAvailable.
- 2025-07-21 | CORE-014 | `cfc2e44ca30cba952c9d3d6d070c4aa58477c351` | HSDM | fix: RES-152230 - dynamics logo mismatch. Files/symbols: MSDynamicsViewAllProjectPageHeader.tsx; SFDCManageProjectWrapper.tsx. Identical patch copies: `412ac88e39cfad9241f34cd54ad8ca5d2d433c58`.
- 2025-08-08 | CORE-036 | `c8500430e308b4f57bf17fb612680e48c777051a` | HSDM | feat: RES-152665 - POC for deepl no translate implementation. Files/symbols: TranslateEngineRenderer.tsx; TranslateGlossaries.tsx; symbols hasEngineConfigChanged, hasGlossaryChanged, showSAPConnectBtn.
- 2025-08-08 | CORE-009 | `c9761aed87b4e5ea888eff71f24e2bb98f07dd72` | HSDM | fix: RES-151817 - merge tag hovering issue. Files/symbols: plugin.js; symbols rects, elmPosition.
- 2025-08-08 | CORE-009 | `5a442565e4dad2b159a2f22bfc6cc67c68905566` | HSDM | fix: RES-151817 - merge tag hovering issue. Files/symbols: App.css.
- 2025-08-08 | CORE-009 | `6ea7c6e7487e0c4750289dbe9f1c8043d75e130d` | HSDM | fix: RES-151817 - merge tag hovering issue. Files/symbols: plugin.js.
- 2025-08-08 | CORE-009 | `936be031d6bd28afa53bce59dd14edc3b41c68e8` | HSDM | fix: RES-153096 - Tinymce tox menu overflow bug fix. Files/symbols: theme.js; library_fixes.txt; symbols l, r.
- 2025-08-11 | CORE-009 | `18a5baf240618aedc5edd6d9ac6e753055c567b2` | HSDM | Revert "fix: RES-153096 - Tinymce tox menu overflow bug fix". Files/symbols: theme.js; library_fixes.txt.
- 2025-08-11 | CORE-034 | `77b8e4a19890d239291c762fdfdc616eff928257` | HSDM | fix: RES-142674 - Default content formating word paste bug fix. Files/symbols: QuestionCardLayout.tsx; RecommendationUtils.tsx; symbols defaultRendererValue, getRichTextOuterHTML.
- 2025-08-11 | CORE-034 | `1002edaa611286dc14655e3822927daf2fdf766d` | HSDM | fix: RES-142674 - Default content formating word paste bug fix. Files/symbols: CopyClipUtils.ts.
- 2025-08-11 | CORE-034 | `0fabc16aab8f2eed42a5ef645cbaa2985cae73e3` | HSDM | fix: RES-142674 - Default content formating word paste bug fix. Files/symbols: QuestionCardLayout.tsx; RecommendationUtils.tsx.
- 2025-08-11 | CORE-033 | `9640c0dbab3a5e0b7c53e30f9969b47c740de2c6` | HSDM | fix: RES-124076 - Visibilty assertion automation bug fix. Files/symbols: app_v2/src/organization-settings/containers/OrganizationWrapperHeaderRenderer.tsx.
- 2025-08-12 | CORE-034 | `5112b21f23085b11f815009d759528e8a08a656a` | HSDM | fix: RES-154044, RES-154043 - Org glossaries bug fix. Files/symbols: TranslateEngineRenderer.tsx; TranslateGlossaries.tsx.
- 2025-08-12 | CORE-034 | `6c59a59540461f7545c3782a931e3fd9cc01543b` | HSDM | fix: RES-154045 - Org glossaries bug fix. Files/symbols: TranslateGlossaries.tsx; symbols tempVal, hasDuplicate.
- 2025-08-12 | CORE-034 | `c26af336fc1cf129bd69ce8c81c74955ee1cad85` | HSDM | fix: RES-154045 - Org glossaries bug fix. Files/symbols: TranslateGlossaries.tsx; symbols tempVal.
- 2025-08-12 | CORE-034 | `0f21519f111555ac319e7bce25ac30fefa2a21d6` | HSDM | fix: RES-154045 - Org glossaries bug fix. Files/symbols: TranslateGlossaries.tsx; symbols tempVal.
- 2025-08-13 | CORE-034 | `204fbe9fd0622649733d77d251466a17fb35b2c9` | HSDM | fix: RES-154045 - Org glossaries bug fix. Files/symbols: TranslateGlossaries.tsx.
- 2025-08-14 | CORE-016 | `dba09d626003912ad2b0eb4dd96aa2076d2ac94b` | HSDM | fix: RES-154041, RES-153858 - backlog bugs. Files/symbols: OrganizationColumnFilter.tsx; OrgCustomFieldsHeader.tsx.
- 2025-08-18 | CORE-021 | `73d78b8ab089e4b5725e6a7f99759b697119ffb4` | HSDM | fix: RES-154370 - Org scroll auto trigger. Files/symbols: PreferencePropsType.ts; ManageUserCustomFieldRenderer.tsx; symbols refs, handleScroll, autoScrollValidation.
- 2025-08-18 | CORE-016 | `13acb02b0513475e6c1b4635a7f74886f3d4f8b5` | HSDM | fix: RES-154370 - Org scroll auto trigger. Files/symbols: OrgCustomFieldsActionDrawer.tsx.
- 2025-08-18 | CORE-016 | `e975e985056540e6746e1acfc46b906082abd98c` | HSDM | fix: RES-154370 - Org scroll auto trigger. Files/symbols: OrgCustomFieldsActionDrawer.tsx.
- 2025-08-18 | CORE-021 | `37da91c4c7c8e9247c9d5bcdf52822ce65d5811c` | HSDM | fix: RES-154370 - Org scroll auto trigger. Files/symbols: ManageUserCustomFieldRenderer.tsx; EmailPrefContainer.tsx; symbols handleAutoScrollForIndex.
- 2025-08-18 | CORE-009 | `8555958de54269e4fe001408b4dc63f8bae20f25` | HSDM | fix: RES-154364 - 💣 tinymce icon bug fix. Files/symbols: plugin.js.
- 2025-08-19 | CORE-033 | `c68412afb7fe6cf2ea0ef9b2249ae0cf0f0e9c10` | HSDM | fix: RES-143699 - Manage Styles and fonts import bug fix. Files/symbols: app_v2/src/organization-settings/containers/my-organization/company-features/ImportStylesDialog.tsx.
- 2025-08-19 | CORE-017 | `82bf4807672e832ef048aee87d2adef48e369558` | HSDM | fix: RES-154585, RES-154591 - org e2e bugs. Files/symbols: UserRoleAndTypeRenderer.tsx; OrgSearchUtils.ts.
- 2025-08-21 | CORE-009 | `0977f66bc8582a9271b12ed483c0d20e2b54f753` | HSDM | fix: RES-145780 - tinymce prod error. Files/symbols: theme.js; library_fixes.txt; symbols s, o.
- 2025-08-21 | CORE-009 | `74e5abcff60a23a9cfc70a0a02af33dad7dbc4a5` | HSDM | fix: RES-145780 - tinymce prod error. Files/symbols: theme.js; library_fixes.txt; symbols s, o.
- 2025-08-21 | CORE-037 | `5e9dc3cd053304087ac8f13304c8d294269afab8` | HSDM | fix: RES-102749 - In esign, Expiration date sorting is not working properly. Files/symbols: app_v2/src/containers/e-sign/ESignDocumentList.tsx.
- 2025-08-21 | CORE-009 | `3872c112b13fb650e172e2158a268d5a090e3d18` | HSDM | Revert "fix: RES-145780 - tinymce prod error". Files/symbols: theme.js; library_fixes.txt.
- 2025-08-22 | CORE-009 | `48bb4264b7e6771342fda4c965696c6a4c65f3f2` | HSDM | fix: RES-155080 - unable to open fee table tinymce. Files/symbols: theme.js.
- 2025-08-22 | CORE-009 | `b931d2d3292a699d874c47548b449c0b422717f5` | HSDM | fix: RES-155080 - unable to open fee table tinymce. Files/symbols: library_fixes.txt; symbols s, o.
- 2025-08-26 | CORE-034 | `5109508648a3833be0090957a7d61daf53695710` | HSDM | fix: RES-154234 - Customization under Line spacing configuration. Files/symbols: TinyMCECustomStyles.tsx; ContentFormatRenderer.tsx; symbols lineHeightList, isValidLineHeight, num.
- 2025-08-29 | CORE-034 | `0244fe0c02fc8b479311391400d546e8f49c2a88` | HSDM | fix: RES-154234 - Customization under Line spacing configuration. Files/symbols: TinyMCECustomStyles.tsx.
- 2025-08-29 | CORE-034 | `71d3739630eae008e404fb3dc74036a3caea8d5d` | HSDM | fix: RES-155751 - Save button flickers. Files/symbols: ContentFormatRenderer.tsx.
- 2025-09-02 | CORE-021 | `8fdf7aee248dded2465c7b6a928ebdbf9d1e3ed1` | HSDM | feat: user chips revamp. Files/symbols: CRMDocumentsImportRfp.tsx; CRMAddTeamMembers.tsx.
- 2025-09-02 | CORE-021 | `e63c94604b6fec428cd95da52509f1d4f2dcf97c` | HSDM | feat: user chips revamp. Files/symbols: AdditionalDetailsRenderer.tsx; UserDetailsContainer.tsx.
- 2025-09-05 | CORE-021 | `4847dfc1c4a823817df2258aef126c8d6948d9e0` | HSDM | feat: RES-155952 - user chips revamp. Files/symbols: SelectUsers.tsx; ProjectTaskTemplateEditDrawer.tsx; symbols filteredUsersList, membersCount.
- 2025-09-08 | CORE-026 | `6a15b2bbe858aad790cf248ddd1050b9122f1760` | HSDM | feat: RES-155656 - SMB Edition Feedback - To include the Home page. Files/symbols: loggedInLayout.tsx.
- 2025-09-08 | CORE-026 | `4a9607b1b649d8944640992363bdefa32b96d88b` | HSDM | feat: RES-155656 - SMB Edition Feedback - To include the Home page. Files/symbols: SupportIcon.tsx; loggedInLayout.tsx; symbols SupportIcon.
- 2025-09-08 | CORE-026 | `c663e8189e6daf22ddc7e449e7fc0c96fc5c668f` | HSDM | feat: RES-155656 - SMB Edition Feedback - To include the Home page. Files/symbols: SupportIcon.tsx.
- 2025-09-08 | CORE-026 | `a8ca7fa5d76b3957a908e60b9041f005e12a9d03` | HSDM | feat: RES-155656 - SMB Edition Feedback - To include the Home page. Files/symbols: SupportIcon.tsx.
- 2025-09-09 | CORE-021 | `021e1f9937669a9303b06ad8e3d015a04c86de44` | HSDM | fix: RES-156338 - User chips bug fix. Files/symbols: SearchCriteriaRender.tsx; TargetAudienceRenderer.tsx.
- 2025-09-10 | CORE-026 | `42938cc874e7d205188a3bdb015014de7212dfa1` | HSDM | feat: RES-155656 - SMB Edition Feedback - To include the Home page. Files/symbols: loggedInLayout.tsx.
- 2025-09-10 | CORE-026 | `f9b521651515d590ddaacc43f30895ea18bccace` | branch | feat: RES-155656 - SMB Edition Feedback - To include the Home page. Files/symbols: loggedInLayout.tsx.
- 2025-09-10 | CORE-026 | `024cf95542f279955f47f153504e8a587a1dd83e` | branch | feat: RES-155656 - SMB Edition Feedback - To include the Home page. Files/symbols: loggedInLayout.tsx.
- 2025-09-10 | CORE-026 | `caaa926f76fd220ed0821dd012deb5119f427890` | HSDM | feat: RES-155656 - SMB Edition Feedback - To include the Home page. Files/symbols: UserAndGuestDetails.tsx.
- 2025-09-11 | CORE-021 | `534489a75b91047c4c479a3a9d4abcb8672bab12` | HSDM | fix: RES-156338 - User chips bug fix. Files/symbols: WorkflowActionRenderer.tsx; CreateTeamContentRenderer.tsx.
- 2025-09-11 | CORE-021 | `ac8386417ded9707510285729d2a1687c2f7e700` | HSDM | fix: RES-156338 - User chips bug fix. Files/symbols: AlSearchFieldsRenderer.tsx; CustomFieldRenderer.tsx.
- 2025-09-12 | CORE-034 | `c15ebc923df0ed72ed925d334009f44e22986433` | HSDM | fix: RES-154234 - Line spacing UAT feedback. Files/symbols: ContentFormatRenderer.tsx.
- 2025-09-19 | CORE-026 | `bce81162c6c0a099fa74b87fdf5a692651c859f8` | HSDM | feat: ai-agent base setup. Files/symbols: AgentCard.tsx; AgentCreate.tsx; symbols AgentCard, classes, org.
- 2025-09-22 | CORE-026 | `b4623b6dc28c481d48f214141c8131103fddbc01` | HSDM | feat: ai-agent base setup. Files/symbols: AgentCard.tsx; AgentCreate.tsx; symbols org, pageLogo, companyLogo.
- 2025-09-22 | CORE-026 | `0777e6bb3174e50ef284d0eba7057ad179d3a844` | HSDM | feat: ai-agent base setup. Files/symbols: FieldConfigPanel.tsx.
- 2025-09-25 | CORE-026 | `219fe77aca530da048f9ccef9b5e49032f432b7e` | HSDM | feat: ai-agent base setup. Files/symbols: AgentFileUploadContainer.tsx; AgentDetailsPanel.tsx; symbols AgentFileUploadContainer, acceptableFileTypes, maxFilesToUpload.
- 2025-09-29 | CORE-026 | `401a15aba24ba10f8803a170fec108da675035a4` | HSDM | feat: ai-agent base setup. Files/symbols: AlertTextVerbatimRenderer.tsx; ChatAttachment.tsx; symbols AlertTextVerbatimRenderer, getIcon, StyledGrid.
- 2025-09-29 | CORE-026 | `e1a80587fbfcac677b6a28fed0e1aade9469d996` | HSDM | feat: ai-agent base setup. Files/symbols: ChatCards.tsx; AgentDetailsPanel.tsx; symbols filesList, dispatch, agentList.
- 2025-09-29 | CORE-026 | `e5ba8f90498111681c152a4f75c6cfaadc6ba89c` | HSDM | feat: ai-agent base setup. Files/symbols: AgentChatRenderer.tsx; ResponseRenderer.tsx; symbols isTriggerLoading, isV2AgentEnabled, results.
- 2025-09-30 | CORE-026 | `0c5bc53bb41d790c2cbaeb5df3a45a43053345b9` | HSDM | feat: ai-agent base setup. Files/symbols: ChatBox.tsx; SuggestedPrompts.tsx; symbols avatarURL.
- 2025-09-30 | CORE-026 | `7e1abe19b4cd7d8097a817c2af79f227a1d7a68b` | HSDM | feat: ai-agent base setup. Files/symbols: ChatCards.tsx.
- 2025-09-30 | CORE-026 | `28b1e01abd5483c002e77da023702b3db43bf48a` | HSDM | feat: ai-agent base setup. Files/symbols: AgentDetailsPanel.tsx; symbols conversationList, formValue, conversationId.
- 2025-10-02 | CORE-026 | `c163655dd635bae989d153afeb08e1df138febd5` | HSDM | feat: ai-agent base setup. Files/symbols: AgentChatRenderer.tsx; ResponseRenderer.tsx; symbols canvaTimerRef.
- 2025-10-02 | CORE-026 | `af81b137b0f1ae991bfcd23ca22440a0ce2c7a2a` | HSDM | feat: ai-agent base setup. Files/symbols: ButtonMenuRenderer.tsx; DocumentCopyAndDownload.tsx; symbols ButtonMenuRenderer, StyledMenu, downloadMenuObj.
- 2025-10-03 | CORE-026 | `0bd64094ca76d87d29bf6f0de5bc4917851e9a06` | HSDM | feat: ai-agent base setup. Files/symbols: AgentsPanel.tsx; index.css; symbols filteredAgents, q, name.
- 2025-10-03 | CORE-026 | `8336aecd2ea9959f29959f4f670b63df2a03ff32` | HSDM | feat: ai-agent base setup. Files/symbols: AgentAvatar.tsx; AgentChatRenderer.tsx; symbols getInitials, trimmed, parts.
- 2025-10-03 | CORE-026 | `b98a8bfeec52d89b932d368426eb9688b4717ff8` | HSDM | feat: ai-agent base setup. Files/symbols: ChatBox.tsx.
- 2025-10-06 | CORE-026 | `a6a591388637e3567a333bbc3af17dd8e97984eb` | HSDM | feat: ai-agent base setup. Files/symbols: ResponseRenderer.tsx; useAgentChats.ts; symbols isAgentRunning, selectedAgentId, selectedAgentName.
- 2025-10-06 | CORE-026 | `65c9dd49d5c27bfb1d8db74cee27bd28aebf85ae` | HSDM | feat: ai-agent base setup. Files/symbols: AgentsPanel.tsx; ConversationContainer.tsx.
- 2025-10-06 | CORE-026 | `92f54c43937fe1b8fda1c143debdaa8552ecc980` | HSDM | feat: ai-agent base setup. Files/symbols: DocumentViewContainer.tsx.
- 2025-10-06 | CORE-026 | `c79650becd2c30d344444245e1857f96e9099bfe` | HSDM | feat: ai-agent base setup. Files/symbols: ChatBoxV2.tsx; symbols conversationPromptIds, promptIndex.
- 2025-10-06 | CORE-026 | `b4b3731f71ba8c7e0e6f3155458ec23d2097baa0` | HSDM | feat: ai-agent base setup. Files/symbols: AgentsPanel.tsx; ConversationContainer.tsx; symbols handleAgentOpen, agentId, selectedAgent.
- 2025-10-06 | CORE-026 | `02bb2f3641b6d41d267c48c0ce7a78feff6c25e9` | HSDM | feat: ai-agent base setup. Files/symbols: DesktopDrawerPane.tsx; CustomToolbar.tsx; symbols isV2AgentEnabled, actions, isCanvaView.
- 2025-10-07 | CORE-026 | `ad5e53a29e123fc48f07e6f74f0229eff4b57e6e` | HSDM | feat: ai-agent base setup. Files/symbols: ConversationContainer.tsx; DocumentEditor.tsx.
- 2025-10-07 | CORE-026 | `ff1bdc56610e9153a30d027a58e787ba5ad1766d` | HSDM | feat: ai-agent base setup. Files/symbols: ResponseRenderer.tsx; index.css; symbols isV2AgentEnabled, HtmlContent.
- 2025-10-07 | CORE-026 | `c0833196a38b3172af0e2d014fd0a8ae266b8498` | HSDM | feat: ai-agent base setup. Files/symbols: AskContainer.tsx.
- 2025-10-07 | CORE-026 | `f7fc3d28e64546923aef7ddf2fe76bbc2b33bd29` | HSDM | feat: ai-agent base setup. Files/symbols: AgentChatRenderer.tsx; ResponseRenderer.tsx; symbols agentMap, entityId, prompts.
- 2025-10-07 | CORE-026 | `520f924b63f1d390d1291279b26eb02794f34942` | HSDM | feat: ai-agent base setup. Files/symbols: AgentChatRenderer.tsx; ChatHistory.tsx.
- 2025-10-08 | CORE-026 | `bba917d1af24b03ca093095f2584e3dd4a5b0526` | HSDM | feat: ai-agent base setup. Files/symbols: ChatHistory.tsx; DesktopDrawerPane.tsx; symbols results, isV2AiEnabled, classes.
- 2025-10-08 | CORE-026 | `2ff7f671dddb6c36122e33ed1be77803e53bbf2e` | HSDM | feat: ai-agent base setup. Files/symbols: ChatBox.tsx; AskThunk.ts; symbols agentId, conversationId, results.
- 2025-10-08 | CORE-026 | `72225b2754fe9ca73d149721ee7b059496ec74ac` | HSDM | feat: ai-agent base setupfeat: ai-agent base setup. Files/symbols: ChatHistory.tsx; AskThunk.ts; symbols isV2AiEnabled.
- 2025-10-08 | CORE-026 | `57d61e56919059add8ac65a5868da52f291152e3` | HSDM | feat: ai-agent base setup. Files/symbols: AskResponsive.tsx; symbols isV2AiEnabled.
- 2025-10-08 | CORE-026 | `a374144fac5e36910d1200ae97323a72423e37da` | HSDM | feat: ai-agent base setup. Files/symbols: ChatHistory.tsx; DesktopDrawerPane.tsx.
- 2025-10-08 | CORE-026 | `83c263057a8c8e62adb71bd994271657ca05002c` | HSDM | feat: ai-agent base setup. Files/symbols: AgentAvatar.tsx; ChatHistory.tsx; symbols AgentAvatar, resolvedFontSize, isEmpty.
- 2025-10-15 | CORE-026 | `06e8a8f38d30c35e9ef302a1922006c043e1f536` | HSDM | fix: RES-159202, RES-159152, RES-159152 agent studio bugs. Files/symbols: AgentChatRenderer.tsx; ResponseRenderer.tsx; symbols AgentFileUploadContainer.
- 2025-10-15 | CORE-026 | `4b3feb1b4d9d7146af006ad78d2e2ffe624c87ac` | HSDM | fix: RES-159202, RES-159152, RES-159152 agent studio bugs. Files/symbols: ChatHistory.tsx; ConversationVO.ts; symbols UserRecentagents, agentList, agentListTop3.
- 2025-10-16 | CORE-026 | `aea5fb33990dd1a310ead65572266df30fadfe30` | HSDM | feat: ai-agent base setup. Files/symbols: ChatRenderer.tsx; AgentChatRenderer.tsx; symbols HtmlContent.
- 2025-10-17 | CORE-026 | `14c144b865350f18741676d56abc7222d7b8f150` | HSDM | feat: RES-157149 Research Agent Studio. Files/symbols: ChatBoxV2.tsx.
- 2025-10-17 | CORE-033 | `5dc99b34a5f1e1fd569e21fea62c6d214ceb35dc` | HSDM | fix: RES-159498 - ASK - close icon is missing. Files/symbols: app_v2/src/components/AskResponsive.tsx.
- 2025-10-22 | CORE-026 | `76f815a0617dae83fa3f111f7b08b331cf999db0` | HSDM | feat: RES-159659 - ai agent feedbacks. Files/symbols: CustomToolbar.tsx; GeneralUtils.ts; symbols isV2AgentEnabled.
- 2025-10-23 | CORE-034 | `7237a7e7b1b7efe2113ce9c4df742138e8e0f4cc` | HSDM | fix: RES-158988 - Toolbar disappears when clicking on style. Files/symbols: CreateAnnouncementsDrawer.tsx.
- 2025-10-23 | CORE-026 | `7ad8761b5be69e92364c0bf9bd09621ae4146b0a` | HSDM | fix: RES-159761 - HTML code is displayed when we view older conversations in the chat. Files/symbols: Markdown.tsx; symbols isHtml.
- 2025-10-23 | CORE-026 | `dfe4ac57184cf1be656de1466bc78a0e547e3c9a` | HSDM | fix: RES-159751, RES-159750 - Ai agent bug fixes. Files/symbols: ChatHistory.tsx; ChatBoxV2.tsx; symbols isTriggerLoading, micStatus, isAgentProcessing.
- 2025-10-23 | CORE-026 | `4fffb041c63a2497cd2d44ea0a94aae466b86a34` | HSDM | fix: RES-159751, RES-159750 - Ai agent bug fixes. Files/symbols: ChatBoxV2.tsx; symbols todayList, existingConversationIndex, updatedHistory.
- 2025-10-24 | CORE-026 | `999aa3b4636e27b7eef6a251dfe605a1d661088d` | HSDM | fix: RES-159887 - latext support for markdown. Files/symbols: AgentChatRenderer.tsx; Markdown.tsx; symbols reactObj, formattedCodeBlock.
- 2025-10-24 | CORE-026 | `64f337b9b33ef8e258b0bfaf3cfdab48070da2d1` | HSDM | fix: RES-159887 - latext support for markdown. Files/symbols: package.json.
- 2025-10-27 | CORE-034 | `561e1d94eff7707ccd319ab83f97d9abf8c28973` | HSDM | fix: RES-158245 Line spacing in Manage Styles rounds to nearest value. Files/symbols: TinyMCECustomStyles.tsx.
- 2025-10-28 | CORE-026 | `414e5b73ed46417229dc23d44941946f168766aa` | HSDM | feat: RES-159329 - Ai agent Nice-to-Have Improvements. Files/symbols: ChatHistory.tsx; DesktopDrawerPane.tsx; symbols getFileMap, agentId, id.
- 2025-10-28 | CORE-026 | `8c516689b35637d1bafa7ad0f7af04e2476f8661` | HSDM | feat: RES-159329 - Ai agent Nice-to-Have Improvements. Files/symbols: IntervalContext.tsx; symbols IntervalContext, IntervalProvider, intervalRef.
- 2025-10-28 | CORE-026 | `51df3a5f29482eef93f818888f49dfba963fe20b` | HSDM | feat: RES-159329 - Ai agent Nice-to-Have Improvements. Files/symbols: ChatBoxV2.tsx; AgentDetailsPanel.tsx; symbols id.
- 2025-11-04 | CORE-026 | `1662e26d80f7e0726fc2d5ed827acd81f2adfb6f` | HSDM | feat: RES-160134 - AI Agents Unit Testing - Jest. Files/symbols: AgentCard.tsx; AgentCreateStepContent.tsx; symbols customFields, frameworkStyles, pushMock.
- 2025-11-04 | CORE-026 | `b0e5eb3ca07d0a1483aa67f64e402433934f2cca` | HSDM | feat: RES-160134 - AI Agents Unit Testing - Jest. Files/symbols: AgentInputFieldsStep.test.tsx; AgentViewFrameworkComponents.test.tsx.
- 2025-11-04 | CORE-026 | `b1d84bf690ede099fbb6ea2aa627be1e82e01167` | HSDM | feat: RES-160134 - AI Agents Unit Testing - Jest. Files/symbols: AgentPreviewScreen.test.tsx; FieldConfigPanel.test.tsx; symbols base, agent, launchLabel.
- 2025-11-04 | CORE-026 | `02583d4e072d1a962a685a482464a463bd5baaf3` | HSDM | feat: RES-160134 - AI Agents Unit Testing - Jest. Files/symbols: RfpRoundedSearch.tsx; webpack.config.js.
- 2025-11-05 | CORE-026 | `e6e59ec7c130a33e0b59abd262e201f0ce2dc8e9` | HSDM | feat: RES-160161 - Section level ask rewrite. Files/symbols: ResponseRenderer.tsx; useAgentChats.ts.
- 2025-11-11 | CORE-026 | `8774fa61dfeb0bd7eab2bacc71d3af4080390ef0` | HSDM | feat: RES-160414 - new ui ai agents. Files/symbols: ChatHistory.tsx; DesktopDrawerPane.tsx; symbols isAgentsPanelOpen.
- 2025-11-11 | CORE-026 | `c29c0c0515454da8377aca1167ff80724b1520c3` | HSDM | feat: RES-160414 - new ui ai agents. Files/symbols: ChatHistory.tsx; DesktopDrawerPane.tsx; symbols selectedAgentVO, agentEntityId, result.
- 2025-11-11 | CORE-026 | `25256ee94aaeeda05308fba87315817812230857` | HSDM | feat: RES-160414 - new ui ai agents. Files/symbols: ChatHistory.tsx; DesktopDrawerPane.tsx; symbols selectedAgentVO, agentEntityId, result.
- 2025-11-12 | CORE-026 | `7706e50246f5b1f93ba8734433631a0bd7ac6c90` | HSDM | Revert "feat: RES-160414 - new ui ai agents". Files/symbols: ChatHistory.tsx; DesktopDrawerPane.tsx; symbols result, FileTitle, Label.
- 2025-11-12 | CORE-026 | `00ee18a73d40c80ed014feba6cce9631b8aefaf7` | HSDM | Revert "feat: RES-160414 - new ui ai agents". Files/symbols: ChatHistory.tsx; DesktopDrawerPane.tsx; symbols agentMap, recentAgents, UserRecentagents.
- 2025-11-12 | CORE-026 | `f16e0dbdd04c3ee5e36fdf45ead71cf761699b36` | HSDM | feat: RES-160414 - new ui ai agents. Files/symbols: ChatHistory.tsx; ChatBoxV2.tsx; symbols result, agentIconClass, agentFromList.
- 2025-11-12 | CORE-026 | `4a392fdead630102fe6f8ed3ec1f5294b53f2b71` | HSDM | feat: RES-160414 - new ui ai agents. Files/symbols: DesktopDrawerPane.tsx; ChatBoxV2.tsx; symbols agentsAvailable, agentList, hasAgents.
- 2025-11-12 | CORE-026 | `a1492ff1d29053e8ab8d16a1b3f288d9e1224dfc` | HSDM | feat: RES-160414 - new ui ai agents. Files/symbols: AgentHamIcon.tsx; symbols AgentHamIcon, theme, isDarkMode.
- 2025-11-13 | CORE-026 | `ccfd5ce575e4f7b9a0b6e35783d6f58b5424fd9b` | branch | Service.ts edited online with Bitbucket. Files/symbols: Service.ts; symbols apiAgents.
- 2025-11-13 | CORE-026 | `95c1b071fca128ed9f3584427985db8ba9976114` | HSDM | feat: RES-160414 - new ui ai agents. Files/symbols: ChatHistory.tsx; DesktopDrawerPane.tsx; symbols conversationList, isV2AgentEnabled, selectedAgentVO.
- 2025-11-13 | CORE-026 | `63c07432d10a832babc6698a7e27bfaa82f95103` | HSDM | feat: RES-160414 - new ui ai agents. Files/symbols: AgentsPanel.tsx.
- 2025-11-13 | CORE-026 | `d9fbde3289a78c88f01a4751773bf826c582c2dc` | HSDM | feat: RES-160414 - new ui ai agents. Files/symbols: AgentDetailsPanel.tsx; AgentsPanel.tsx; symbols agentList, handleAgentOpen, agentId.
- 2025-11-13 | CORE-026 | `04dd1b7de000ba57d05d75f0a73245e63d38d285` | HSDM | feat: RES-160414 - new ui ai agents. Files/symbols: ChatHistory.tsx.

### 2026 — 85 patch groups

- 2026-03-06 | CORE-029 | `a13cac6753ef9a2dba89e86ddc111201566517e4` | branch | DS-390 feat: Lyra version upgrade and theme cleanup. Files/symbols: package.json; bootstrap.tsx; symbols darkModeEnabledModules, mModules.
- 2026-03-16 | CORE-029 | `0dae7586367b8eb0cf38ad7d030f527592295958` | branch | Update package.json for lyra version. Files/symbols: package.json.
- 2026-04-07 | CORE-029 | `1488b90dc725e7c783b368c88f2a5922f5d33655` | branch | feat: DS-469 Integrate i18next for localization support in app_v2 with lyra. Files/symbols: global.d.ts; bootstrap.tsx; symbols createRoot, getCurrentLocale, renderAppContent.
- 2026-04-24 | CORE-038 | `2d480aa7b09b06a1f39eaeb13accdb8e9b1ed9ba` | HSDM | Update package.json. Files/symbols: app_v2/package.json.
- 2026-05-11 | CORE-029 | `07da96fb64d0e93708388103098c07154fe9abca` | HSDM | fix: RES-175591 Update package.json for lyra latest version. Files/symbols: package.json.
- 2026-05-15 | CORE-029 | `6eb94f4faff4d96d9f906644ddfc0f82e4296148` | branch | feat: DS-469 Lyra POC - Internationalization. Files/symbols: bootstrap.tsx; BaseLayoutInitiator.tsx; symbols embeddedWindow, getCurrentLocale, renderAppContent.
- 2026-05-18 | CORE-028 | `54007ca1db22d8734802ab085d71fd211d5afbe2` | HSDM | feat: RES-177198 uservolist removal - init migration plan. Files/symbols: uservolist-occurrence.md; ai-agents.md; symbols alone.
- 2026-05-19 | CORE-028 | `08c2b5f45bc57d759e87ef17654edd284f6de02c` | HSDM | feat: RES-177198 uservolist removal - init migration plan. Files/symbols: uservolist-common-todo.md; uservolist-occurrence.md; symbols user, mentionUsers, configs.
- 2026-05-27 | CORE-028 | `d9e73b563f2fc9f57faa4509f927fa7ea3ec50c1` | HSDM | feat: RES-177198 uservolist removal - init migration. Files/symbols: uservolist-occurrence.md; containers.md; symbols configs, div, user.
- 2026-06-11 | CORE-030 | `7739f3417a2cb9028c5e21aa67857d2fbb1ecd74` | branch | chore: RES-179299 add per-package Graphify graphs for app_v2 and MFEs. Files/symbols: graphify.mdc; SKILL.md; symbols doing, cannot, in.
- 2026-07-01 | CORE-030 | `0103599d85284082995e9e85eba4d7e30e18f5ce` | D | feat: RES-179299 Git Nexus Setup. Files/symbols: SKILL.md; SKILL.md; symbols failing, from, flow.
- 2026-07-01 | CORE-027 | `6c75ca697cdbd7de2f547752656fe01cb4d929e8` | branch | feat: Maverick hackcathon Init UI Setup. Files/symbols: package.json; bootstrap.tsx; symbols AddAISource, toTitleCase, getFieldKey.
- 2026-07-01 | CORE-027 | `944dc362a36d85bcca71ffc62dc24bc28ac9230e` | branch | feat: Maverick hackcathon - Phase I. Files/symbols: AddAISourceAuthSchemaService.ts; AddAISourceDrawer.css; symbols authType, fieldKey, SAMPLE_API_TOKEN_RESPONSE.
- 2026-07-02 | CORE-027 | `124e7a681a35825b9f1a8231aa73db163520fcdd` | branch | feat: Maverick hackcathon - Phase II. Files/symbols: AddAISourceAuthSchemaService.ts; AddAISourceDrawer.tsx; symbols discoverExternalSourceRootNodes, response, folders.
- 2026-07-02 | CORE-027 | `de7c83b245e82bab21ce1e8559531ed3757a8d06` | branch | feat: Maverick hackcathon - Phase II. Files/symbols: AddAISource.tsx; AddAISourceAuthSchemaService.ts; symbols USE_ADD_AI_SOURCE_MOCK_API, ADD_AI_SOURCE_MOCK_API_DELAY_MS, waitForMockApi.
- 2026-07-02 | CORE-027 | `f03562e40db280cb7bbfcc7038374ac9ea5022dd` | branch | feat: Maverick hackcathon - Phase II. Files/symbols: AddAISourceAuthSchemaService.ts; AddAISourceDrawer.tsx; symbols getAIExternalSourceProviderKey, sourceKey, addedConfig.
- 2026-07-02 | CORE-027 | `13f34b949c2dda7c67126ea15bc0b359cec00b57` | branch | feat: Maverick hackcathon - Phase II. Files/symbols: package.json; AddAISourceAuthSchemaService.ts; symbols TYPEWRITER_STEP_MS, INPUT_SUGGESTION_PROPS, CREDENTIAL_INPUT_SUGGESTION_PROPS.
- 2026-07-07 | CORE-030 | `9ccfe2363c442bd22ff3231a4800fd7174d04aa1` | D | feat: RES-179299 Git Nexus Setup. Files/symbols: SKILL.md; SKILL.md; symbols fs, path, root.
- 2026-07-09 | CORE-029 | `c53d85c7f4bc7d9e2f70297b051ade793f29b6cc` | D | feat: RES-179299 Lyra Peer dependency fix. Files/symbols: package.json.
- 2026-07-11 | CORE-027 | `ca132bcd6f20a838a8c53aff86beddcfd95206af` | branch | feat: Maverick hackcathon - Phase II. Files/symbols: AddAISourceAuthSchemaService.ts; AddAISourceDrawer.css; symbols USE_ADD_AI_SOURCE_MOCK_API, discoverExternalSourceChildNodes, normalizedSource.
- 2026-07-12 | CORE-027 | `29ece93dc58ddfe0a72a62c2af9f756f3f589cbc` | branch | feat: AI hack feat mavericks. Files/symbols: AddAISourceAuthSchemaService.ts; AddAISourceDrawer.css; symbols DEFAULT_CLARIFICATION_MESSAGE, USE_ADD_AI_SOURCE_MOCK_API, MOCK_SESSION_STORE.
- 2026-07-12 | CORE-027 | `324137eecaa356dc3bef60754aced01a097ddc20` | branch | feat: AI hack feat mavericks. Files/symbols: AddAISourceDrawer.css; AddAISourceDrawer.tsx; symbols AssistantBubble, FolderPickerCard, SNAP_EXIT_MS.
- 2026-07-15 | CORE-035 | `ee20e4207f5947fc49cd08dd704af3f2ad478d31` | HSDM | feat: RES-182292 - AI Linked Company Filters. Files/symbols: AiAssitantFilters.tsx; LinkedCompanyAiFilters.tsx; symbols tagSearchOptions, getTagOptions, dataList.
- 2026-07-15 | CORE-035 | `fbd4493942cca5b81a91974ceff7c7c5455e6f78` | HSDM | feat: RES-182292 - AI Linked Company Filters. Files/symbols: AiAssitantFilters.tsx; LinkedCompanyAiFilters.tsx; symbols tagSearchOptions, getTagOptions, dataList.
- 2026-07-16 | CORE-035 | `e70d60d4c8c1f2b2e62ef66f03cd10746d7ae36f` | HSDM | feat: RES-182292 - AI Linked Company Filters. Files/symbols: FilterActions.tsx; FilterButton.tsx; symbols hasLinkedCompanyFilter, skipKeys, isLinkedCompaniesEnabled.
- 2026-07-16 | CORE-035 | `82b8bfb15a89ea4bbcd0d68dad58ba317bba9480` | HSDM | feat: RES-182292 - AI Linked Company Filters. Files/symbols: FilterActions.tsx; FilterButton.tsx; symbols hasLinkedCompanyFilter, skipKeys, isLinkedCompaniesEnabled.
- 2026-07-16 | CORE-035 | `ca96197289a7519721fda45e39d06da9e889c02e` | HSDM | feat: RES-182292 - AI Linked Company Filters. Files/symbols: FilterButton.tsx; FilterPopover.tsx; symbols showLinkedCompanyAiFilters, nextFilters, hasAppliedLinkedCompanyAiFilter.
- 2026-07-23 | CORE-030 | `9f8522a91e3dd9435443a7c97a835cdf2fd5934c` | HSDM | feat: RES-179299 Add GitNexus configuration and setup scripts. Files/symbols: .gitattributes; .gitignore; symbols fs, path, SCRIPTS.
- 2026-07-23 | CORE-030 | `816b3337a6dbe0b93f42b79c14c74281b105ceaf` | HSDM | feat: RES-179299 Add GitNexus configuration and setup scripts. Files/symbols: .gitnexusrc; _gitnexus-common.sh.
- 2026-07-23 | CORE-030 | `f96d54c85c5f4ec5f0f3e288d2ec5f8c8a64c64d` | HSDM | feat: RES-179299 Add GitNexus configuration and setup scripts. Files/symbols: .gitnexusignore; .gitnexusrc; symbols when, only.
- 2026-07-23 | CORE-030 | `8e65041a732b4bb71794b9e5cd75a41889b343d3` | HSDM | feat: RES-179299 Turbo Config updates. Files/symbols: turbo.json.
- 2026-07-23 | CORE-030 | `2d042993b0efcf012e3d55c19bad1fa06da392ae` | HSDM | feat: RES-179299 Turbo Config updates. Files/symbols: .gitnexusignore.
- 2026-07-29 | CORE-028 | `66d66457e64d3d71270f3956e8c75e410606e8ce` | HSDM | feat: userList revamp ActiveUsers revamp - RES-177198. Files/symbols: RfpUserPicGroup.tsx; companyusermap-occurrence.md; symbols cachedUsersFromStore, cachedUsers, isUserVO.
- 2026-08-05 | CORE-028 | `587b364bd91442464b96d5fa5f3d4ad1c731b3ce` | HSDM | feat: userList rewamp getCompanyUserName REMOVAL - RES-177198. Files/symbols: companyusermap-occurrence.md; getuserlist-getusermap-getusersforbu-occurrence.md; symbols displayText, tooltipTitle, displayName.
- 2026-08-05 | CORE-028 | `60ab7267943002240bdb2dc46e44bbdf3549883a` | HSDM | feat: userList rewamp getCompanyUserName REMOVAL - RES-177198. Files/symbols: authContext.tsx; userDataStore.ts; symbols userCount, currentSuperAdmin, storedSuperAdmin.
- 2026-08-06 | CORE-028 | `5338c74b9d88e611fa7b54aac40f54acb8fb3d63` | HSDM | feat: userList revamp ActiveUsers revamp - RES-177198. Files/symbols: BuFrameWorkComponents.tsx; BuUsersListPage.tsx; symbols cachedUsersSnapshot, cachedUser, hasMatchingRole.
- 2026-08-07 | CORE-028 | `5c050ab4d43bf170c29cc14929b2d1c5d4495b4c` | HSDM | feat: userList revamp ActiveUsers revamp - RES-177198. Files/symbols: CommentsWrapper.tsx; useDebounce.ts; symbols useDebounce, handler, that.
- 2026-08-07 | CORE-028 | `74318edb2392164c572324b3603205d92e7d103b` | HSDM | feat: userList revamp ActiveUsers revamp - RES-177198. Files/symbols: CommentsWrapper.tsx; RfpDiscussionsUtils.ts; symbols asyncMentionConfigs, usersData, mentionMap.
- 2026-08-07 | CORE-028 | `bfbc61183b7bcd30fc16ab0f573320b2e38f6a98` | HSDM | feat: userList rewamp getCompanyUserName REMOVAL2 - RES-177198. Files/symbols: SendMessageDrawer.tsx; BillingContactUtils.ts; symbols getBillingContactsAsync, billingSuggestion, billingUsers.
- 2026-08-10 | CORE-028 | `e0068069be8fa24a2b6ad8a2e7c5f3d87e75fc98` | HSDM | feat: userList rewamp getCompanyUserName REMOVAL2 - RES-177198. Files/symbols: OrgFrameworkRenderers.tsx; ViewUserDetails.tsx; symbols displayText, tooltipTitle, displayName.
- 2026-08-12 | CORE-028 | `036f8107d20976605d889c4a0106a5a21debf987` | HSDM | feat: userList rewamp OTHER METHODS AUG11 - RES-177198. Files/symbols: GeneralStoreInitLoad.ts; activeuserlist-occurrence.md; symbols userInfoVO, cachedUsers, outOfOfficeUserList.
- 2026-08-12 | CORE-028 | `f70dd50c8c5ee82feddfb0341d94a49b379f0934` | HSDM | feat: userList rewamp OTHER METHODS AUG11 - RES-177198. Files/symbols: OrganizationUtils.ts.
- 2026-08-14 | CORE-026 | `713c67f976eafd5bba82c4b1d9ab368e79d5ee5f` | D | fix: RES-185173 uservo bug fixes. Files/symbols: AgentCard.tsx.
- 2026-08-14 | CORE-028 | `3af64d1119634d68e3dd69e78b034e8a05a61516` | HSDM | fix: ULD-14-08-2026 mention display, audit edit, and content search report. Files/symbols: CommentTextBox.tsx; DiscussionPage.tsx; symbols existingTeamIds, editAccess, getDefaultFilterConfig. Identical patch copies: `c44121cc99b983b574fc2a5295394d1400270a19`.
- 2026-08-17 | CORE-028 | `f6020cbfebb59cd8ff5a8b6e1da0835175704005` | HSDM | fix: ULD-14-08-2026 mention display, audit edit, and content search report. Files/symbols: RfpUserPicGroup.tsx; GeneralUtils.ts; symbols sortUsernamesByPrefix, aScore, bScore.
- 2026-08-17 | CORE-028 | `c8030fa1890fde21efdfc03d22ec35b091164f77` | HSDM | fix: enhance AgentRunHistoryTable with user cache integration for improved display and performance. Files/symbols: AgentRunHistoryTable.tsx; symbols getRunDisplayName.
- 2026-08-19 | CORE-006 | `cf0c8866ebdbd357c54e7524379bfd91016c60d6` | HSDM | feat: RES-185427 jest code removal. Files/symbols: jest.config.js; package.json. Identical patch copies: `424779e0f00698574a893095145897bf0cae475f`.
- 2026-08-19 | CORE-006 | `c30af003fb1ec7742bc1eef8c4bfadae9c14b906` | branch | feat: RES-185427 vitest setup. Files/symbols: .eslintrc; TESTING.md; symbols names, mockGet, PlansAndBillingsTest.
- 2026-08-20 | CORE-006 | `360764a19a1dcfbdbc6a631d520862146046b657` | branch | feat: RES-185427 vitest setup. Files/symbols: TESTING.md; PlansAndBillings.test.tsx; symbols r, envelope, seedBillingLocalStorage.
- 2026-08-20 | CORE-038 | `19004ff4a16f54a16c05d7132d2a5dcf6cc3ac8b` | HSDM | Update .npmrc files with new authentication tokens for design-system-npm-local registry. Files/symbols: generated/dependency/empty metadata; no original feature inference.
- 2026-08-26 | CORE-006 | `8718aff634aca1f65d99631c1c79e2390a1e8f7f` | HSDM | feat: RES-185427 Introduce Vitest + MSW testing and Playwright E2E smoke. Files/symbols: ATTRIBUTION.md; SKILL.md; symbols mocks, path, fixtureKey.
- 2026-08-26 | CORE-038 | `c0b2f568786a1e0cb4b957fe11924ede84d4018f` | branch | Merge branch 'staging' of https://github.com/responsive-core/rfp-app into RES-185427-vitest-setup. Files/symbols: app_ask/src/components/chat-box-wrapper/ChatBox.tsx; app_ask/src/components/chat-box-wrapper/ChatBoxV2.tsx; symbols featurePreference, canUseLinkedCompanyAiFilters.
- 2026-08-27 | CORE-006 | `9693de9785e4ac5c52550fdf52a9da561338705c` | HSDM | feat: RES-185427 Introduce Vitest + MSW testing and Playwright E2E smoke. Files/symbols: SKILL.md; pr-validation.md; symbols isSharedInfra, basenameTestCandidates, primary.
- 2026-08-27 | CORE-006 | `510f5d7f14089e79728f5927527a2580c20a7b7e` | HSDM | feat: RES-185427 Introduce Vitest + MSW testing and Playwright E2E smoke. Files/symbols: SKILL.md; pr-validation.md.
- 2026-08-27 | CORE-006 | `e84f8b3e2a54bf5e437fbd7b47b26227a3a98bd3` | HSDM | feat: RES-185427 Introduce Vitest + MSW testing and Playwright E2E smoke. Files/symbols: SKILL.md; pr-validation.md.
- 2026-08-27 | CORE-038 | `379cffddc02cafb3c7b556c25efe606bccdabb4a` | branch | Merge pull request #8282 from responsive-core/sonarqube-local-rfp-app. Files/symbols: .cursor/skills/pr-validation/SKILL.md; .cursor/skills/pr-validation/commands/pr-validation.md.
- 2026-08-27 | CORE-006 | `a8205f82b51334a1b2e74e509b49959a165f9b10` | branch | feat: RES-185427 Introduce Vitest + MSW testing and Playwright E2E smoke. Files/symbols: SKILL.md; run-sonar-gate.cjs; symbols config, formatSonarSection, lines.
- 2026-08-27 | CORE-006 | `d563c1b5c75c378023ac327367bef8d1a9e8d591` | HSDM | feat: RES-185427 Introduce Vitest + MSW testing and Playwright E2E smoke. Files/symbols: SKILL.md; run-sonar-gate.cjs; symbols config, formatSonarSection, lines.
- 2026-08-27 | CORE-006 | `89ebd1836df9d319f38707e6ecc35452be005bdd` | HSDM | feat: RES-185427 Introduce Vitest + MSW testing and Playwright E2E smoke. Files/symbols: LoggedInHeaderLayout.tsx. Identical patch copies: `d99694bb0091c443e8500a7df598c4befdac9bcc`.
- 2026-08-28 | CORE-031 | `5d1922b7e357126f9743a87c948589e62f7762cb` | HSDM | fix: backport merged PRs with single merge-commit cherry-pick and correct conflict markers. Files/symbols: backport-to-lower-branch.yml.
- 2026-08-28 | CORE-031 | `bff331a21a6d77a0f6f20801ac2e8ba095019f6e` | HSDM | fix: backport merged PRs with single merge-commit cherry-pick and correct conflict markers. Files/symbols: backport-to-lower-branch.yml.
- 2026-09-08 | CORE-029 | `4d6ea78f206a85c8324db01f8211bf72d83f6af8` | HSDM | feat: DS-940: migrate design system packages to @responsive-lyra scope and enable material themes. Files/symbols: configuration.md; discovery-checklist.md; symbols renderThumbs, useStyles, LYRA_CSS.
- 2026-09-09 | CORE-038 | `6262df958c4128ee00c918b32ff9ba451453f942` | D | Update @tiptap-editor/editor to version 0.14.0 and remove unused peer dependencies from package.json and pnpm-lock.yaml. Files/symbols: app_v2/package.json; package.json.
- 2026-09-10 | CORE-002 | `f55a0bc6f6cfd94adf43b514c3153ee793aed85c` | HSDM | DS-940 refactor: update webpack config for i18next and react-i18next to non-eager loading. Files/symbols: webpack.config.js. Identical patch copies: `e32c0cdf70bfb609b258788ae66fd1069ed85cf1`.
- 2026-09-10 | CORE-029 | `3e45e258ec5f4a048215ba4c1b5621386bd3742a` | HSDM | fix: DS-940 scoped Lyra theme for hosted responsive-lite. Files/symbols: AppWrapper.tsx; symbols content.
- 2026-09-11 | CORE-005 | `161d9ba8068dbd2a40844742fd090a2ebd2217d4` | HD | perf: RES-187387 optimize CI build pipeline, persistent caching. Files/symbols: package.json; webpack.config.js; symbols webpack, parts, pkgSegment.
- 2026-09-11 | CORE-030 | `01456bc7a974eae211f231a3f67c98fe88463e92` | HSDM | chore: RES-187398 remove GitNexus integration and clean up repository artifacts. Files/symbols: .gitattributes; .gitignore. Identical patch copies: `e9d77b6d04a92c1e9e06f43370dbef550115bf21`.
- 2026-09-11 | CORE-030 | `347f7cf504b3982cd47a4193c7fb0966f54f71f1` | D | chore: RES-187398 remove GitNexus integration and clean up repository artifacts. Files/symbols: .gitattributes; .gitignore.
- 2026-09-11 | CORE-030 | `3c645cbf5c0611e58ad1a22daa1f89d327365dcd` | D | chore: RES-187398 keep host-smoke package-lock.json and remove leftover nexus scripts. Files/symbols: .gitignore; package.json.
- 2026-09-11 | CORE-030 | `10e588311e34ccf7128ff0ebfe9642ca0c06a867` | HSDM | chore: RES-187398 keep host-smoke package-lock.json. Files/symbols: .gitignore. Identical patch copies: `014315540f36c8b7e626eac014ddd74ba5eb1322`.
- 2026-09-11 | CORE-037 | `598814c78bcb2ae62ce8b2d98799b39b2a4ffb48` | D | chore: revert unintentional formatting on merge. Files/symbols: app_ask/package.json; app_ask_utils/package.json.
- 2026-09-11 | CORE-038 | `a2e25e39f6ef73672296a3d5249037729f84af4c` | branch | index on gitnexus-cleanup-dev: 598814c78bc chore: revert unintentional formatting on merge. Files/symbols: generated/dependency/empty metadata; no original feature inference.
- 2026-09-11 | CORE-038 | `301680900c674bcf975a6ce3fbe95d90528416b1` | branch | untracked files on gitnexus-cleanup-dev: 598814c78bc chore: revert unintentional formatting on merge. Files/symbols: generated/dependency/empty metadata; no original feature inference.
- 2026-09-11 | CORE-006 | `1295fc3823a4087c4e320a5915df529cd866bc96` | HSD | fix: RES-185427 - fix sonar coverage path and root test script. Files/symbols: .gitignore; MyWorkHeader.test.tsx; symbols actual, EXCLUDED_PACKAGES_TEST, EXCLUDED_PACKAGES_COVERAGE.
- 2026-09-15 | CORE-028 | `f314727aa4b26afd500d3ff5cb3908ceff713d8e` | HSDM | feat: Add '/users/get-user-directory-meta' to skipCompanySwitchUrl in Axios helper. Files/symbols: Axios.ts. Identical patch copies: `16f8b956a3af36d3181dab7f8a7c329b69e27501`.
- 2026-09-16 | CORE-005 | `ee8cd4824c8eef7b97cbdb762c00d483c9454b76` | HD | perf: RES-187387 optimize CI build pipeline, persistent caching. Files/symbols: vitest.config.mts.
- 2026-09-16 | CORE-005 | `ae0cca354c398462007140b44fbc06b9ab277eef` | D | fix: update webpack configuration for Module Federation compatibility. Files/symbols: webpack.config.js.
- 2026-09-16 | CORE-005 | `5374d37d7b39b0c535b7de86b1eed4aa7cba3d2e` | D | fix: update webpack configuration for Module Federation compatibility. Files/symbols: CI.md; index.cjs.
- 2026-09-17 | CORE-005 | `5d087e5d976cbc126a4c9fa63f7c68354b218243` | D | chore: update package.json and pnpm-lock.yaml for build configurations and dependency versions. Files/symbols: package.json; index.cjs.
- 2026-09-17 | CORE-005 | `c9ba40b9729c9ad398b79c1c9ddc47ccea70396b` | D | RES-187387 perf: parallelize Babel via thread-loader & tune worker concurrency. Files/symbols: package.json; webpack.config.js; symbols isWatch, threadLoaderOptions, parallel.
- 2026-09-18 | CORE-005 | `dfeb53373a3685bb348d9fa0c40dfbc415489478` | D | fix: adjust parallel minimizer settings for CI environments to optimize performance. Files/symbols: index.cjs; symbols cpuCount, parallel.
- 2026-09-18 | CORE-005 | `7c7df975d2a9e534ce1a17ebf8e779bcc96c528e` | D | RES-187387 fix: relocate Webpack FS cache & restore Sonar root sources. Files/symbols: .gitignore; webpack.config.js; symbols rootSources, rootLcov, fileName.
- 2026-09-21 | CORE-005 | `0bced9664b427bc9a5c1c995cf2a55dcc5ba3269` | HD | chore: RES-187387 relocate Webpack FS cache & update build configurations. Files/symbols: .gitignore; settings.json; symbols isWatch, threadLoaderOptions, cpuCount.
- 2026-09-21 | CORE-005 | `8a544fda9fd803364873e882a4eaa072fd2d4e36` | HD | fix: RES-187387 avoid Sonar root/module source double-index. Files/symbols: compose-sonar-properties.cjs; sonar-project.properties.
- 2026-09-29 | CORE-032 | `f812f111a15458dc2e324c3677650352345ff2b4` | branch | chore: RES-189050 Improve performance & Reduce Load. Files/symbols: ChatRenderer.tsx; ChatRenderer.tsx; symbols downloadCanvaToExcel, XLSX, containsMath.

## Supplemental reflog/WIP register

These 18 own records are outside current refs and add no verified shipped feature count. Stash author proves capture ownership, not authorship of every untracked/generated artifact. First-parent tracked diffs, index companions and untracked trees were inspected read-only for relevant paths; no customer fixtures, raw source or credential values retained.

- 2026-09-10 | `1b7ec28572e8f39dbccf3fcc9b1f4831b86dd63b` | DS-940 refactor: update webpack config for i18next and react-i18next to non-eager loading. CORE-002: identical stable patch to e32c0cdf70bf/f55a0bc6f6cf; do not count again.
- 2026-09-09 | `954ebd759aa8e1ce689739179c3eb0ad2d12ed9b` | On ui-opt: we. CORE-038: empty index/untracked companion, OS metadata or generated node_modules shim changes; no product implementation claim.
- 2026-09-09 | `75e8cf4f9a8f11225862bb561ea2fd2066e81cbe` | index on ui-opt: 95aeeefab7e Merge pull request #8678 from responsive-core/feature/stg-res-184268. CORE-038: empty index/untracked companion, OS metadata or generated node_modules shim changes; no product implementation claim.
- 2026-09-09 | `11368a1b9f728b5dfc718b837d16b4d3238d7e42` | untracked files on ui-opt: 95aeeefab7e Merge pull request #8678 from responsive-core/feature/stg-res-184268. CORE-038: empty index/untracked companion, OS metadata or generated node_modules shim changes; no product implementation claim.
- 2026-09-04 | `7903d792157280b556ce0789f30d072655e36cd5` | On sam-test: ew. CORE-038: empty index/untracked companion, OS metadata or generated node_modules shim changes; no product implementation claim.
- 2026-09-04 | `84d738d410424b5f2f4156bee29f5bfe1c8062f0` | index on sam-test: 248dc84fd41 Merge pull request #8434 from responsive-core/kumaresh-stg. CORE-038: empty index/untracked companion, OS metadata or generated node_modules shim changes; no product implementation claim.
- 2026-09-04 | `4230df4d55bf8cd31080884c96833e93f67bd689` | untracked files on sam-test: 248dc84fd41 Merge pull request #8434 from responsive-core/kumaresh-stg. CORE-038: untracked PR-summary skill/draft and Sonar coverage-inventory docs, plus OS metadata; original authorship/use/adoption not established.
- 2026-08-17 | `b21bdf53cc56b13f2007d1a4be9c820556b856b5` | On company-user-load-details-dev: test. CORE-028: WIP/index variant of agent-run user-cache/display changes; historical draft, not new delivery.
- 2026-08-17 | `f5e66160f968517c391802e67ba9c813554f2596` | index on company-user-load-details-dev: 8ed6e9e22fc Merge branch 'development' of https://github.com/responsive-core/rfp-app into company-user-load-details-dev. CORE-038: empty index/untracked companion, OS metadata or generated node_modules shim changes; no product implementation claim.
- 2026-08-17 | `7e931ab5ca7f606b93daeb0bc3e94c556a0d3054` | untracked files on company-user-load-details-dev: 8ed6e9e22fc Merge branch 'development' of https://github.com/responsive-core/rfp-app into company-user-load-details-dev. CORE-038: empty index/untracked companion, OS metadata or generated node_modules shim changes; no product implementation claim.
- 2026-08-17 | `a1e9c9f9d74dffb80ec708164cc7af5c075d9f9e` | On company-user-load-details-dev: u. CORE-028: WIP/index variant of agent-run user-cache/display changes; historical draft, not new delivery.
- 2026-08-17 | `0f97653c93e67e87b864178b64c0b7e9159a0473` | index on company-user-load-details-dev: 8ed6e9e22fc Merge branch 'development' of https://github.com/responsive-core/rfp-app into company-user-load-details-dev. CORE-028: WIP/index variant of agent-run user-cache/display changes; historical draft, not new delivery.
- 2026-08-17 | `e7f29073b69ae9b59ed65c17e288db6da81ba14a` | untracked files on company-user-load-details-dev: 8ed6e9e22fc Merge branch 'development' of https://github.com/responsive-core/rfp-app into company-user-load-details-dev. CORE-038: empty index/untracked companion, OS metadata or generated node_modules shim changes; no product implementation claim.
- 2026-07-15 | `933b8f8c3c584e4f789d9182b329b4fc91558a9e` | WIP on RES-182294-linked-company-filters: 69087748e61 Merge pull request #6578 from responsive-core/RES_26.06.04_14_Jul_2026_Hotfix. CORE-035: WIP/index linked-company filter draft before published follow-ups; no independent deployment.
- 2026-07-15 | `d3994f52709bc70ab5549d363244cfe931d192aa` | index on RES-182294-linked-company-filters: 69087748e61 Merge pull request #6578 from responsive-core/RES_26.06.04_14_Jul_2026_Hotfix. CORE-035: WIP/index linked-company filter draft before published follow-ups; no independent deployment.
- 2026-05-15 | `85c86112a6b8164d554dfb70adb9feb88f14e3c0` | On sam-lyra-i18n: i18n. CORE-029/038: i18n POC dependency/shared-config WIP or empty companion; unmerged experiment.
- 2026-05-15 | `dcbe6eae0a9d060e566a613e1ea206e54598ba7b` | index on sam-lyra-i18n: 6eb94f4faff feat: DS-469 Lyra POC - Internationalization. CORE-029/038: i18n POC dependency/shared-config WIP or empty companion; unmerged experiment.
- 2026-05-15 | `d5105f2b0055c8100ed71a36a3b49079607a2101` | untracked files on sam-lyra-i18n: 6eb94f4faff feat: DS-469 Lyra POC - Internationalization. CORE-029/038: i18n POC dependency/shared-config WIP or empty companion; unmerged experiment.

## Supplemental unreachable-object register

All 53 records below are outside current refs and reflogs, recovered read-only from available local objects. Three ordinary commits have exact authored diffs; 50 stash/index/untracked snapshots are capture evidence, with original authorship of surrounding files UNKNOWN. Status is historical/draft, merge and deployment UNKNOWN; no independent shipped-feature count. Full SHA/date/confirmed identity plus G-20261003 locate each item. Nonempty ordinary patches differ from the ref-reachable stable-patch groups, but belong to existing initiatives. Git can eventually garbage-collect unreachable objects; factual summaries and durable IDs are preserved here.

- 2026-07-12 | CORE-027 | `71b51c794a2e6c42eb4c8dbafe31284f2c51dc5f` | `sanjeev.s+rio@responsive.io` | feat: Maverick hackcathon - Phase II. Ordinary alternate folder-selection/source-preview iteration; same prototype initiative, not another live integration. Changed paths=3; context: app_v2/src/organization-settings/containers/platform/ai-assistance/external-source/AddAISourceDrawer.css; app_v2/src/organization-settings/containers/platform/ai-assistance/external-source/AddAISourceDrawer.tsx; app_v2/src/organization-settings/containers/platform/ai-assistance/external-source/IOSFolderGroup.tsx; symbols AI_FOLDER_SOURCES, FolderSelectionState, getParentId, parentEntry.
- 2026-07-17 | CORE-035/038 | `68950d12aa6b0a8da209b99b82b80043831ee196` | `sanjeev.s+rio@responsive.io` | feat: RES-182292 - AI Linked Company Filters. Ordinary import-order-only variant; feature title does not establish a new feature. Changed paths=1; context: app_ask_utils/src/utils/ResponsiveAIUtils.ts.
- 2026-07-17 | CORE-035 | `5b48ce617447349f5d23b6f39d34bea8e47a741d` | `sanjeev.s+rio@responsive.io` | feat: RES-182292 - AI Linked Company Filters. Ordinary applyFilters ordering variant for feature-gated linked-company criteria; historical. Changed paths=1; context: app_ask_utils/src/utils/ResponsiveAIUtils.ts; symbols canUseLinkedCompanyAiFilters, linkedCompanyFilters.
- 2026-08-19 | CORE-006/038 | `536c2eb32042d8454382cabd1c9d0c87b4ad8379` | `sanjeev.s@responsive.io` | WIP on RES-185427-jest-removal: 9c1bf4aae89 Merge pull request #7985 from responsive-core/RES-184750-ETISALAT-userloadDetails. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=776; context: app_v2/jest.config.js; app_v2/package.json; app_v2/src/ai-agents/test/AgentCreate.test.tsx; symbols appCommonsCompilerOptions, pushMock, setItemMock, getItemMock.
- 2026-08-19 | CORE-006/038 | `687df57c9d61e29c006278fb45d5b561c108de0b` | `sanjeev.s@responsive.io` | index on RES-185427-jest-removal: 9c1bf4aae89 Merge pull request #7985 from responsive-core/RES-184750-ETISALAT-userloadDetails. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=774; context: app_v2/jest.config.js; app_v2/package.json; app_v2/src/ai-agents/test/AgentCreate.test.tsx; symbols appCommonsCompilerOptions, pushMock, setItemMock, getItemMock.
- 2026-08-19 | CORE-006/038 | `7e00b249939f56e5421ca996322ba219b7cc014d` | `sanjeev.s@responsive.io` | WIP on RES-185427-jest-removal: 9c1bf4aae89 Merge pull request #7985 from responsive-core/RES-184750-ETISALAT-userloadDetails. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=776; context: app_v2/jest.config.js; app_v2/package.json; app_v2/src/ai-agents/test/AgentCreate.test.tsx; symbols appCommonsCompilerOptions, pushMock, setItemMock, getItemMock.
- 2026-08-19 | CORE-006/038 | `90e14aef2d9c2345a9588f7bed1734c1992182de` | `sanjeev.s@responsive.io` | index on RES-185427-jest-removal: 9c1bf4aae89 Merge pull request #7985 from responsive-core/RES-184750-ETISALAT-userloadDetails. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=774; context: app_v2/jest.config.js; app_v2/package.json; app_v2/src/ai-agents/test/AgentCreate.test.tsx; symbols appCommonsCompilerOptions, pushMock, setItemMock, getItemMock.
- 2026-08-19 | CORE-006/038 | `0404e87fb08bd1272b916219ce73cfb11ef8c816` | `sanjeev.s@responsive.io` | index on RES-185427-jest-removal: cf0c8866ebd feat: RES-185427 jest code removal. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=0; context: empty/generated/credential-only metadata, no product claim.
- 2026-08-19 | CORE-006/038 | `786ff0869109fa14499c07c4887bdce54a656c91` | `sanjeev.s@responsive.io` | On RES-185427-jest-removal: phase2-vitest-setup. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=3; context: app_v2/.eslintrc; app_v2/package.json.
- 2026-08-19 | CORE-006/038 | `9027e02ab24081112a0527c7b8c1e38570d58429` | `sanjeev.s@responsive.io` | untracked files on RES-185427-jest-removal: cf0c8866ebd feat: RES-185427 jest code removal. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=9; context: app_v2/src/test/__tests__/vitest-dom.test.tsx; app_v2/src/test/__tests__/vitest-unit.test.ts; app_v2/src/test/fileMock.ts; symbols element, mockLyraAi, handlers, createTestServer.
- 2026-08-19 | CORE-006/038 | `5ea18f887399b99769183a79997eb1a6d0bb8c86` | `sanjeev.s@responsive.io` | index on RES-185427-jest-removal-staging: eb9f2953dfc Merge pull request #7996 from responsive-core/subash_staging. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=774; context: app_v2/jest.config.js; app_v2/package.json; app_v2/src/ai-agents/test/AgentCreate.test.tsx; symbols appCommonsCompilerOptions, pushMock, setItemMock, getItemMock.
- 2026-08-19 | CORE-006/038 | `6da368860694796b07f303f21d17969442645038` | `sanjeev.s@responsive.io` | WIP on RES-185427-jest-removal-staging: eb9f2953dfc Merge pull request #7996 from responsive-core/subash_staging. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=776; context: app_v2/jest.config.js; app_v2/package.json; app_v2/src/ai-agents/test/AgentCreate.test.tsx; symbols appCommonsCompilerOptions, pushMock, setItemMock, getItemMock.
- 2026-08-19 | CORE-006/038 | `1e4fadec5447ab33d238a86e8bb619036a4c2201` | `sanjeev.s@responsive.io` | index on vitest-setup-app_v2: 424779e0f00 feat: RES-185427 jest code removal. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=28; context: app_v2/.eslintrc; app_v2/docs/TESTING.md; app_v2/package.json; symbols mockGet, PlansAndBillingsTest, setUserDetails, setAdditionalInfo.
- 2026-08-19 | CORE-006/038 | `7f9a5f6c8036184f9acde9cf4c699f85d56c2497` | `sanjeev.s@responsive.io` | WIP on vitest-setup-app_v2: 424779e0f00 feat: RES-185427 jest code removal. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=28; context: app_v2/.eslintrc; app_v2/docs/TESTING.md; app_v2/package.json; symbols mockGet, PlansAndBillingsTest, setUserDetails, setAdditionalInfo.
- 2026-08-20 | CORE-006/038 | `92a2d4dfac5440ba38f7dce1a9ac19f96abebe13` | `sanjeev.s@responsive.io` | WIP on vitest-setup-app_v2: c30af003fb1 feat: RES-185427 vitest setup. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=8; context: app_v2/docs/TESTING.md; app_v2/src/containers/plans-billings/tests/containers/PlansAndBillings.test.tsx; app_v2/src/containers/plans-billings/tests/mocks/PlansAndBillingsMockData.ts; symbols r, envelope, mockGet, seedBillingLocalStorage.
- 2026-08-20 | CORE-006/038 | `d2def64cea0c151fca14528a0c699b0e0afaf86c` | `sanjeev.s@responsive.io` | index on vitest-setup-app_v2: c30af003fb1 feat: RES-185427 vitest setup. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=8; context: app_v2/docs/TESTING.md; app_v2/src/containers/plans-billings/tests/containers/PlansAndBillings.test.tsx; app_v2/src/containers/plans-billings/tests/mocks/PlansAndBillingsMockData.ts; symbols r, envelope, mockGet, seedBillingLocalStorage.
- 2026-08-26 | CORE-006/038 | `c49af5468fee3f5c227e7a20e565648420f72c0e` | `sanjeev.s@responsive.io` | WIP on RES-185427-vitest-setup-dev-sync: 98d99cdad26 Merge branch 'staging' of https://github.com/responsive-core/rfp-app into RES-185427-vitest-setup. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=2; context: packages/vitest/src/config/createWebpackAppVitestConfig.ts; packages/vitest/src/setup/dom.ts; symbols JSDOMWindow, suppressJSDOMNotImplementedErrors, virtualConsole, stubWindowOpen.
- 2026-08-26 | CORE-006/038 | `dd9ddd88c6567a37269077d4c0b705bc51400b7a` | `sanjeev.s@responsive.io` | index on RES-185427-vitest-setup-dev-sync: 98d99cdad26 Merge branch 'staging' of https://github.com/responsive-core/rfp-app into RES-185427-vitest-setup. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=0; context: empty/generated/credential-only metadata, no product claim.
- 2026-09-08 | CORE-029/038 | `5f14677c20599ab2f1bdffd837ad4516b15e7dc8` | `sanjeev.s@responsive.io` | index on lyra-package-update: 98243afef0f3 Merge pull request #8629 from responsive-core/keerthana_mst2. Saved shared-package/registry/theme integration snapshot; mixed imported changes are not wholly attributed. Changed paths=409; context: .cursor/skills/vitest/references/configuration.md; .cursor/skills/vitest/references/discovery-checklist.md; .cursor/skills/vitest/references/mocking.md; symbols LYRA_CSS, reverseColorNameMap, standardLyraThemes, getLyraThemeFromColor.
- 2026-09-08 | CORE-029/038 | `98058376c31c5466980396bb2b5390f5093b4258` | `sanjeev.s@responsive.io` | WIP on lyra-package-update: 98243afef0f3 Merge pull request #8629 from responsive-core/keerthana_mst2. Saved shared-package/registry/theme integration snapshot; mixed imported changes are not wholly attributed. Changed paths=409; context: .cursor/skills/vitest/references/configuration.md; .cursor/skills/vitest/references/discovery-checklist.md; .cursor/skills/vitest/references/mocking.md; symbols LYRA_CSS, reverseColorNameMap, standardLyraThemes, getLyraThemeFromColor.
- 2026-09-09 | CORE-029/038 | `677c33e5323d175bb17331a14c014aa2b163df6f` | `sanjeev.s@responsive.io` | WIP on lyra-package-update-dev: 5e91d68cb6b Merge branch 'development' of https://github.com/responsive-core/rfp-app into lyra-package-update-dev. Saved shared-package/registry/theme integration snapshot; mixed imported changes are not wholly attributed. Changed paths=3; context: app_v2/package.json; package.json.
- 2026-09-09 | CORE-029/038 | `9f91e09ae4c7a5ec78d9c4032f508c7d9f448425` | `sanjeev.s@responsive.io` | index on lyra-package-update-dev: 5e91d68cb6b Merge branch 'development' of https://github.com/responsive-core/rfp-app into lyra-package-update-dev. Saved shared-package/registry/theme integration snapshot; mixed imported changes are not wholly attributed. Changed paths=0; context: empty/generated/credential-only metadata, no product claim.
- 2026-09-10 | CORE-029 | `23767466a0dcce20f891d85e33b2ea17c826c637` | `sanjeev.s@responsive.io` | WIP on theme-leak-fix: 7bf6c66f86c Merge pull request #8817 from responsive-core/res-185673-author-and-reviewer. Saved Lite theme-isolation draft; related published fix already counted. Changed paths=1; context: responsive-lite/src/components/AppWrapper.tsx; symbols content.
- 2026-09-10 | CORE-029 | `3b674393bfaa71ac39622aa1d73479d324cf97e6` | `sanjeev.s@responsive.io` | index on theme-leak-fix: 7bf6c66f86c Merge pull request #8817 from responsive-core/res-185673-author-and-reviewer. Saved Lite theme-isolation draft; related published fix already counted. Changed paths=1; context: responsive-lite/src/components/AppWrapper.tsx; symbols content.
- 2026-09-11 | CORE-030/038 | `62fc0839b51389fbafb4e7c75b4e379afa21c341` | `sanjeev.s@responsive.io` | index on gitnexus-cleanup-dev: e4f1507b2d7 Merge pull request #8863 from responsive-core/res-181547. Saved cleanup/synchronization/lockfile iteration; unrelated captured recommendation/UI changes do not establish my authorship. Changed paths=24; context: .gitattributes; .gitignore; .gitnexus.env.example; symbols fs, path, root, script.
- 2026-09-11 | CORE-030/038 | `c1a0cfd75a59f54e1155fd2d9f25109f819befda` | `sanjeev.s@responsive.io` | WIP on gitnexus-cleanup-dev: e4f1507b2d7 Merge pull request #8863 from responsive-core/res-181547. Saved cleanup/synchronization/lockfile iteration; unrelated captured recommendation/UI changes do not establish my authorship. Changed paths=24; context: .gitattributes; .gitignore; .gitnexus.env.example; symbols fs, path, root, script.
- 2026-09-11 | CORE-030/038 | `595ce41705ff1fbcd2ee43f066953035023cfedc` | `sanjeev.s@responsive.io` | WIP on gitnexus-cleanup-dev: 347f7cf504b chore: RES-187398 remove GitNexus integration and clean up repository artifacts. Saved cleanup/synchronization/lockfile iteration; unrelated captured recommendation/UI changes do not establish my authorship. Changed paths=3; context: .gitignore; package.json.
- 2026-09-11 | CORE-030/038 | `ab6d7b4e6c8bb80e8bd3aec8aaf7063ee78d7820` | `sanjeev.s@responsive.io` | index on gitnexus-cleanup-dev: 347f7cf504b chore: RES-187398 remove GitNexus integration and clean up repository artifacts. Saved cleanup/synchronization/lockfile iteration; unrelated captured recommendation/UI changes do not establish my authorship. Changed paths=3; context: .gitignore; package.json.
- 2026-09-11 | CORE-030/038 | `ca1b8654adfa4aa3fccca26f58c54be7a4f5d0ce` | `sanjeev.s@responsive.io` | index on gitnexus-cleanup: e9d77b6d04a chore: RES-187398 remove GitNexus integration and clean up repository artifacts. Saved cleanup/synchronization/lockfile iteration; unrelated captured recommendation/UI changes do not establish my authorship. Changed paths=2; context: .gitignore.
- 2026-09-11 | CORE-030/038 | `d0e4c8d3958429c01946a33ac85aeb602b3006fd` | `sanjeev.s@responsive.io` | WIP on gitnexus-cleanup: e9d77b6d04a chore: RES-187398 remove GitNexus integration and clean up repository artifacts. Saved cleanup/synchronization/lockfile iteration; unrelated captured recommendation/UI changes do not establish my authorship. Changed paths=2; context: .gitignore.
- 2026-09-11 | CORE-030/038 | `9e2c877f6d0f00aad23bb1daec2457e84cc4735c` | `sanjeev.s@responsive.io` | WIP on gitnexus-cleanup-dev: 3c645cbf5c0 chore: RES-187398 keep host-smoke package-lock.json and remove leftover nexus scripts. Saved cleanup/synchronization/lockfile iteration; unrelated captured recommendation/UI changes do not establish my authorship. Changed paths=29; context: app_ask/package.json; app_ask_utils/package.json; app_commons/package.json; symbols RecommendationHistoryPopoverProps, entries, user, result.
- 2026-09-11 | CORE-030/038 | `d9f6ad9a10b6ae0021360edeac5e84df0e3e74a1` | `sanjeev.s@responsive.io` | index on gitnexus-cleanup-dev: 3c645cbf5c0 chore: RES-187398 keep host-smoke package-lock.json and remove leftover nexus scripts. Saved cleanup/synchronization/lockfile iteration; unrelated captured recommendation/UI changes do not establish my authorship. Changed paths=29; context: app_ask/package.json; app_ask_utils/package.json; app_commons/package.json; symbols RecommendationHistoryPopoverProps, entries, user, result.
- 2026-09-16 | CORE-006/038 | `3bcd4a7ca2d6c3c246b82024d04c190f6df37f36` | `sanjeev.s@responsive.io` | On test-check-sonar-coverage: kkkk. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=1; context: app_v2/vitest.config.mts.
- 2026-09-16 | CORE-006/038 | `3dfceb5d32468e1cfd0a735f9ff1827eec7d4593` | `sanjeev.s@responsive.io` | index on test-check-sonar-coverage: 7c408d7bcdd Merge pull request #8960 from responsive-core/gitnexus-cleanup-pr. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=0; context: empty/generated/credential-only metadata, no product claim.
- 2026-09-16 | CORE-006/038 | `4f7e878354def0dd35151cca2d2e370a122c24b3` | `sanjeev.s@responsive.io` | untracked files on test-check-sonar-coverage: 7c408d7bcdd Merge pull request #8960 from responsive-core/gitnexus-cleanup-pr. Saved testing deletion/scaffold/coverage/setup iteration; historical draft, not new delivery or tests-passing evidence. Changed paths=2; context: output.txt; pipeline.sh.
- 2026-09-16 | CORE-005/038 | `333434009fe4ec78d1463a54f39215d2d933369a` | `sanjeev.s@responsive.io` | index on ui-opt: e31fce09215 Merge branch 'staging' of https://github.com/responsive-core/rfp-app into ui-opt. Saved build/thread/cache/Sonar iteration or empty companion; original integration counted under its initiative. Changed paths=0; context: empty/generated/credential-only metadata, no product claim.
- 2026-09-16 | CORE-006/038 | `cfc5aa753427745c866ca2429ad2291baddd3817` | `sanjeev.s@responsive.io` | WIP on ui-opt: e31fce09215 Merge branch 'staging' of https://github.com/responsive-core/rfp-app into ui-opt. Saved test-config iteration during build work; no independently verified test result. Changed paths=1; context: app_v2/vitest.config.mts; symbols rootDir, answeringPageTestSetup, baseConfig.
- 2026-09-17 | CORE-005/038 | `64fbe772e3dca1736367c80259d19da6fb03ee9a` | `sanjeev.s@responsive.io` | index on ui-opt-dev: 5d087e5d976 chore: update package.json and pnpm-lock.yaml for build configurations and dependency versions. Saved build/thread/cache/Sonar iteration or empty companion; original integration counted under its initiative. Changed paths=5; context: app_v2/package.json; app_v2/webpack.config.js; packages/build-utils/index.cjs; symbols threadLoaderOptions, isCI.
- 2026-09-17 | CORE-005/038 | `8a0b1c0a6f2ed9ef8e01015e2642b48afdadbf5b` | `sanjeev.s@responsive.io` | WIP on ui-opt-dev: 5d087e5d976 chore: update package.json and pnpm-lock.yaml for build configurations and dependency versions. Saved build/thread/cache/Sonar iteration or empty companion; original integration counted under its initiative. Changed paths=5; context: app_v2/package.json; app_v2/webpack.config.js; packages/build-utils/index.cjs; symbols threadLoaderOptions, isCI.
- 2026-09-17 | CORE-005/038 | `14cf2694b2b7044340c4ed96ce3dd0412ff6c619` | `sanjeev.s@responsive.io` | index on ui-opt-dev: 5d087e5d976 chore: update package.json and pnpm-lock.yaml for build configurations and dependency versions. Saved build/thread/cache/Sonar iteration or empty companion; original integration counted under its initiative. Changed paths=5; context: app_v2/package.json; app_v2/webpack.config.js; packages/build-utils/index.cjs; symbols isWatch, threadLoaderOptions, parallel, path.
- 2026-09-17 | CORE-005/038 | `b8c3844a4fb6fe46618ff82b29bad2ddea706e47` | `sanjeev.s@responsive.io` | WIP on ui-opt-dev: 5d087e5d976 chore: update package.json and pnpm-lock.yaml for build configurations and dependency versions. Saved build/thread/cache/Sonar iteration or empty companion; original integration counted under its initiative. Changed paths=5; context: app_v2/package.json; app_v2/webpack.config.js; packages/build-utils/index.cjs; symbols isWatch, threadLoaderOptions, parallel, path.
- 2026-09-21 | CORE-005/038 | `4058675bb874c5840584c3c1e13659486a923e6f` | `sanjeev.s@responsive.io` | WIP on ui-opt-conflict: 0bced9664b4 chore: RES-187387 relocate Webpack FS cache & update build configurations. Broad synchronization/conflict snapshot; hundreds of surrounding changes are capture-only, not wholly my implementation. Changed paths=588; context: .github/CODEOWNERS; .gitignore; .husky/commit-msg; symbols isAskWidgetPath, hash, previousQuestionFilter, AgentIconWrapper.
- 2026-09-21 | CORE-005/038 | `e8c741dc565bd0f37e34b78ed5929e81d51cb284` | `sanjeev.s@responsive.io` | index on ui-opt-conflict: 0bced9664b4 chore: RES-187387 relocate Webpack FS cache & update build configurations. Broad synchronization/conflict snapshot; hundreds of surrounding changes are capture-only, not wholly my implementation. Changed paths=588; context: .github/CODEOWNERS; .gitignore; .husky/commit-msg; symbols isAskWidgetPath, hash, previousQuestionFilter, AgentIconWrapper.
- 2026-09-21 | CORE-005/038 | `684d17523259dcc4e72e94046dff207ba0219b3e` | `sanjeev.s@responsive.io` | WIP on ui-opt: 0bced9664b4 chore: RES-187387 relocate Webpack FS cache & update build configurations. Saved build/thread/cache/Sonar iteration or empty companion; original integration counted under its initiative. Changed paths=2; context: scripts/compose-sonar-properties.cjs; sonar-project.properties; symbols rootSources, sources, trimmed.
- 2026-09-21 | CORE-005/038 | `a3f5d4a013fc8331e6604aaac03131ff7c44c737` | `sanjeev.s@responsive.io` | index on ui-opt: 0bced9664b4 chore: RES-187387 relocate Webpack FS cache & update build configurations. Saved build/thread/cache/Sonar iteration or empty companion; original integration counted under its initiative. Changed paths=2; context: scripts/compose-sonar-properties.cjs; sonar-project.properties; symbols rootSources, sources, trimmed.
- 2026-09-29 | CORE-032 | `7ea010a1095d3766183b9ee4d682e54a272c21e6` | `sanjeev.s@responsive.io` | index on ux-opt: 8a544fda9fd fix: RES-187387 avoid Sonar root/module source double-index. Saved runtime/lazy-loading/date/dependency iteration; branch-only work already bounded in CORE-032. Changed paths=91; context: app_ask/src/components-v2/ChatContainer/ChatRenderer.tsx; app_ask/src/components/ChatContainer/ChatRenderer.tsx; app_ask/src/components/chat-box-wrapper/ChatBoxV2.tsx; symbols downloadCanvaToExcel, XLSX, RehypePlugin, containsMath.
- 2026-09-29 | CORE-032 | `828dc93d02ad58598bbf2386b1886863b79a9eb8` | `sanjeev.s@responsive.io` | WIP on ux-opt: 8a544fda9fd fix: RES-187387 avoid Sonar root/module source double-index. Saved runtime/lazy-loading/date/dependency iteration; branch-only work already bounded in CORE-032. Changed paths=91; context: app_ask/src/components-v2/ChatContainer/ChatRenderer.tsx; app_ask/src/components/ChatContainer/ChatRenderer.tsx; app_ask/src/components/chat-box-wrapper/ChatBoxV2.tsx; symbols downloadCanvaToExcel, XLSX, RehypePlugin, containsMath.
- 2026-09-29 | CORE-032 | `bbed9b4c1160f665d284895c74773f6fe50c3279` | `sanjeev.s@responsive.io` | index on ux-opt: 8a544fda9fd fix: RES-187387 avoid Sonar root/module source double-index. Saved runtime/lazy-loading/date/dependency iteration; branch-only work already bounded in CORE-032. Changed paths=90; context: app_ask/src/components-v2/ChatContainer/ChatRenderer.tsx; app_ask/src/components/ChatContainer/ChatRenderer.tsx; app_ask/src/components/chat-box-wrapper/ChatBoxV2.tsx; symbols downloadCanvaToExcel, XLSX, RehypePlugin, containsMath.
- 2026-09-29 | CORE-032 | `d0719ac9696a056804d070188301dc436174b2d0` | `sanjeev.s@responsive.io` | WIP on ux-opt: 8a544fda9fd fix: RES-187387 avoid Sonar root/module source double-index. Saved runtime/lazy-loading/date/dependency iteration; branch-only work already bounded in CORE-032. Changed paths=90; context: app_ask/src/components-v2/ChatContainer/ChatRenderer.tsx; app_ask/src/components/ChatContainer/ChatRenderer.tsx; app_ask/src/components/chat-box-wrapper/ChatBoxV2.tsx; symbols downloadCanvaToExcel, XLSX, RehypePlugin, containsMath.
- 2026-09-30 | CORE-005/038 | `3e86653e47d44b9c98a3bb7b1f6abdf71f7d9277` | `sanjeev.s@responsive.io` | WIP on ui-opt: 8a544fda9fd fix: RES-187387 avoid Sonar root/module source double-index. Broad synchronization/conflict snapshot; hundreds of surrounding changes are capture-only, not wholly my implementation. Changed paths=1524; context: .github/CODEOWNERS; app/library-search/controller/rfpio_controllers.js; app/library-search/controller/rfpio_project_controllers.js; symbols entityId, cancelPendingNameEdits, sections, section.
- 2026-09-30 | CORE-005/038 | `b328ff7a4bdba85a35c7585e402e87fade72e344` | `sanjeev.s@responsive.io` | index on ui-opt: 8a544fda9fd fix: RES-187387 avoid Sonar root/module source double-index. Broad synchronization/conflict snapshot; hundreds of surrounding changes are capture-only, not wholly my implementation. Changed paths=1524; context: .github/CODEOWNERS; app/library-search/controller/rfpio_controllers.js; app/library-search/controller/rfpio_project_controllers.js; symbols entityId, cancelPendingNameEdits, sections, section.
- 2026-09-30 | CORE-005/038 | `15634b9779dc212fe1bb1bbc45871525a27e2c59` | `sanjeev.s@responsive.io` | WIP on ui-opt: 8a544fda9fd fix: RES-187387 avoid Sonar root/module source double-index. Broad synchronization/conflict snapshot; hundreds of surrounding changes are capture-only, not wholly my implementation. Changed paths=1524; context: .github/CODEOWNERS; app/library-search/controller/rfpio_controllers.js; app/library-search/controller/rfpio_project_controllers.js; symbols entityId, cancelPendingNameEdits, sections, section.
- 2026-09-30 | CORE-005/038 | `d127b0f8747595d3f0638b5a5fa7d4a65141c648` | `sanjeev.s@responsive.io` | index on ui-opt: 8a544fda9fd fix: RES-187387 avoid Sonar root/module source double-index. Broad synchronization/conflict snapshot; hundreds of surrounding changes are capture-only, not wholly my implementation. Changed paths=1524; context: .github/CODEOWNERS; app/library-search/controller/rfpio_controllers.js; app/library-search/controller/rfpio_project_controllers.js; symbols entityId, cancelPendingNameEdits, sections, section.


## Committer-only and merge attribution register

Twenty ref-reachable records have my committer identity but another author. They are collaboration/transport evidence, not my authored implementation. Multi-parent author-matched merges were inventoried across all refs/dates but their combined diffs were not attributed wholesale.

- 2026-07-15 | `3d267aa92c829ca066861cd77b9d65522566d997` | author Ranjith R; my committer role only | feat: RES-182294 [Linked Company] - [Backend] Ability to define filters for Linked companies in AI Draft, ASK.
- 2025-09-30 | `108c4eaa773a1f8341453add040831d58ef947bb` | author Abarna D; my committer role only | Merged in sam_agtt (pull request #53180).
- 2024-09-18 | `8623fb932fb91a0f48d78ea7feb3b062a522502b` | author INTERNS051-SANT\santhiya.thangavel_r; my committer role only | feat: Sanity fixes.
- 2024-07-11 | `2098e71c476c7afb41a5cee6ffa41d3fee9f0021` | author abishek.k; my committer role only | Merged in abishek_app_stg2 (pull request #39552).
- 2024-07-10 | `f0f18bbae7fe26afa87389ba60762a3c7f8edb86` | author Arunachalam L; my committer role only | Merged in arun_sam_ui (pull request #39545).
- 2024-04-25 | `2b0bf0a0d9eee39467d9e511a47d1b299ca0afb8` | author Gokula Krishnan N; my committer role only | Merged in gk_org_settings_global_st_up (pull request #36840).
- 2024-04-12 | `55ad0cfeabf279daee2da8dc3592d5b5361d6a42` | author Subash Kannan; my committer role only | Merged in subash_org_settings_dev3 (pull request #36416).
- 2024-04-12 | `b2eeaab44506bffd3956b03878cc0e4cbd892200` | author Dinesh; my committer role only | fix: pod-name not setting for guest user.
- 2024-03-06 | `c78a959be0de6ec43735e0bb0c13180bf560a7ce` | author Abishekrfpio; my committer role only | RES-99534.
- 2024-03-01 | `1b2a3bbd1d54270d3526d06cc676cae63f30d9ce` | author abishek.k; my committer role only | Merged in abishek_framework_stg (pull request #34835).
- 2024-02-21 | `851dd5ef45d0f85a834d5dad29b59d88a19dc324` | author abishek.k; my committer role only | Merged in abishek_app_framework (pull request #34503).
- 2024-02-19 | `426185463b6a271d80949dd3993df766357c11b9` | author Arthi; my committer role only | Merged in arthi_app_frame (pull request #34424).
- 2024-02-16 | `977db2445041fb52bbd3a3c2f71adfa7a7f66ad5` | author Subash Kannan; my committer role only | Merged in subash_app_launcher (pull request #34268).
- 2024-01-16 | `7fc1dbb74321ce0959691d23a5be1ee8c0a0ee77` | author Navaneethan; my committer role only | fix: RES-96689 bug fix.
- 2024-01-09 | `1c596141071c86b7e90ca48366554d0df465c79e` | author abishek.k; my committer role only | Merged in abishek_org_settings (pull request #33323).
- 2024-01-02 | `e24c3eeadc8f9b2f5f8b11cf98eeff63af1242a2` | author Kalaiyarasan A; my committer role only | Merged in kalaiy_stag_conflict (pull request #33173).
- 2023-12-22 | `2fc55e63f6e164fb155cde54a3f41b6e3dde8661` | author Srimathi Radhakrishnan; my committer role only | Merged in sri_esign_app (pull request #33162).
- 2023-12-21 | `6071219fc311c7f204b45e27f2b4fea32d5a3c0d` | author abishek.k; my committer role only | Merged in abishek_qrelease_branch (pull request #33137).
- 2023-11-10 | `e25b3a780f1f5ca7d39372b891ac74f7b970844e` | author Arthi; my committer role only | Merged in arthi_stg (pull request #31947).
- 2023-05-09 | `6f1b819887a718e9a8e1634560655d32604d57ed` | author Abarna D; my committer role only | Merged in dev3_confict (pull request #26202).

Maintenance contract: retain stable CORE IDs, add new evidence with inspection SHA/date/source status, keep historical/reverted records, preserve canonical metrics/role dates, and resolve UNKNOWN fields only with evidence or explicit user confirmation. Future tailoring should cite the detailed record, not infer ownership from this large inventory.

### CORE-026 — Dated role attribution reconciliation (2026-10-24)

Source: workflows/apple-frontend-engineer-200687902-1052/analysis.md, Revision evidence (2026-10-21), which records direct authored-commit verification. This resolves the historical role-placement gap above without changing employment dates: bce81162c6c0a099fa74b87fdf5a692651c859f8 (2025-09-19), Easy Peasy agent-authoring store, September 2024–September 2025 role; 2ff7f671dddb6c36122e33ed1be77803e53bbf2e (2025-10-08), Redux-backed agent conversations, current role; 1662e26d80f7e0726fc2d5ed827acd81f2adfb6f (2025-11-04), authored Jest agent create/input/list/preview tests, current role. Original attribution, reverts and suite-retention boundaries remain. No new source-repository inspection was performed during this reconciliation.

### CORE-005 — S3 build-cache reuse reconciliation (2026-10-24)

USER-CONFIRMED personal implementation: S3-backed file-cache reuse in the build pipeline, explicitly confirmed in the Nike R-95778 tailoring record on 2026-10-21, consistent with the earlier U2 companion S3 rollout confirmation. Safe wording: added S3-backed file-cache reuse to the build pipeline. Keep the 10–14+ minutes to ~101 seconds cold-build result attributed to Webpack tuning/disk caches/bounded concurrency; S3 is an additional mechanism, not a newly isolated benchmark. No new metrics, service architecture, environment/date or post-deployment checks established.


### CORE-039 — Current approved BASE: application achievements and role attribution

Status: USER-CONFIRMED / CURRENT RESUME, 2026-11-23.
Source: `main-resume/frontend-base.pdf` (workspace-relative), SHA256 `baf4ed23b5878de7c5ae208387d60828962b606c09aaa467d2ebb28235f9cc93`; complete exact-wording reading copy in `contexts/resume-baseline.md`. User explicitly confirmed the latest resume as correct and requested context synchronization. This record supersedes conflicting older resume counts/wording/attribution only within the statements below.

- Frontend Platform Engineer, October 2025–Present: reduced monorepo cold build time by **86% (10–14 minutes to ~101 seconds)** through Webpack optimization, memory-bounded parallel builds and caching. This replaces older ~88% wording for new resumes. The historical 101.45-second source remains implementation/benchmark provenance, not a competing current printed figure.
- Software Engineer, September 2024–September 2025: React shell/shared headers/layout portals/responsive navigation with **4+ star Gainsight user ratings**; **60% less client polling overhead** via SSE; **2 React micro-frontends** using Webpack Module Federation and Native web components for Trust Center/Builder viewer reuse; **30% better search relevance** using Atlas Vector Search/OpenAI embeddings through Java/Spring Boot APIs (also SERVER-037).
- Associate Software Engineer, July 2023–August 2024: **4 AngularJS modules**, **45% page-load improvement**, Redux/Easy Peasy, cross-browser behavior; **30% less production issue-resolution time** with ELK/root-cause investigation; sign-in/password reset, validation/error feedback, REST integration, guest OTP/Redis sessions; TinyMCE integration/customization for document composition, inline comments and cross-browser formatting.
- Preserve these periods and mechanisms as printed. Do not move the BASE's build bullet into Lyra testing, split internship work into later employment or replace confirmed counts from older reference wording.

Evidence boundary: current user-confirmed resume facts, not a new source-code audit, freshly measured benchmark, test execution or live employer-parsing result. Consult existing anchored records for extra implementation detail; do not invent facts absent from either source. The selected PDF remains unchanged.
