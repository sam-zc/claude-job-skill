# Server / Backend Resume Context

Current resume facts follow [the approved BASE snapshot](../resume-baseline.md), user-confirmed 2026-11-23, recorded in SERVER-037. Read `../index.md` for routing/boundaries; older records in `evidence.md` supply additional implementation detail. Current confirmation overrides older conflicting resume wording, not unrecorded scope.

## Positioning

Personally attributable Java REST/service/DAO, authorization, data migration, reporting resilience, retrieval metadata and AI persistence work at Responsive. Prefer verified narrow implementations. Commerce is separate freelance production. SSE/60%, Redis/OTP, Dockerized Sonar/Jenkins and internship backend work are now USER-CONFIRMED / PERSONAL IMPLEMENTATION; the invented 15+ field quantity remains excluded.

## Primary Tech Stack

- Code-verified: Java, JAX-RS/Jersey, Spring-injected services, MongoDB DAOs, Solr/search metadata, JUnit/Mockito; Spring Boot daily-report module context.
- Project implementation: Next.js, GraphQL, Neon PostgreSQL, Google/Discord OAuth, RBAC, PayRam, S3, Vercel, Ubuntu VPS, SMTP — SERVER-034.
- Tooling: Python Sonar aggregation/reporting/tests, Java static-analysis fixes, scoped review — SERVER-010, SERVER-030, SERVER-031.
- USER-CONFIRMED personal implementation: SSE, Redis caching, OTP guest-session verification, Spring Boot/REST internship background processing — SERVER-032, SERVER-033.
- USER-CONFIRMED tooling: Dockerized Sonar validation in Jenkins CI and Lyra deployment/Sonar management — SERVER-033, LYRA-025; other skills-only items still require their own scope evidence.

## Strongest Capabilities

### Java / REST APIs

- Summary: Implemented targeted user onboarding/lookup, validation and business-unit membership REST contracts
- Status: STRONG.
- Evidence IDs: SERVER-001, SERVER-002, SERVER-006.
- Verified metrics / scope: One combined membership API response; original call count/latency unknown.
- JD keywords: Java, REST, input validation, APIs, Spring.
- Boundary: Inspected controller paths include JAX-RS/Jersey and Spring-injected services; do not call all of them Spring MVC/Spring Boot.

### MongoDB / DAO Work

- Summary: Refactored company-scoped membership lookup, selective projection and matching list/count query construction
- Status: STRONG.
- Evidence IDs: SERVER-006, SERVER-007, SERVER-015.
- Verified metrics / scope: One membership response; exactly 11 excluded fields in inspected projection.
- JD keywords: MongoDB, DAO, projection, data minimization.
- Boundary: Do not use historical invented 15+ or infer payload/latency percentages.

### Authorization / Security

- Summary: Protected super-admin usernames with server-derived support exception, permission/input guards and activation-state safeguards
- Status: STRONG.
- Evidence IDs: SERVER-001, SERVER-002, SERVER-012, SERVER-014.
- Verified metrics / scope: Scoped guards in existing services.
- JD keywords: authorization, permission checks, secure coding, BYOK validation.
- Boundary: No auth-engine/encryption/KMS architecture ownership; SERVER-003 TOTP QR repair is distinct from the now user-confirmed guest OTP implementation (SERVER-032).

### Reporting Resilience

- Summary: Moved exception isolation inside company report loop, validated missing data/cells and improved diagnostics
- Status: STRONG.
- Evidence IDs: SERVER-005.
- Verified metrics / scope: Daily-report service; no company count or percentage.
- JD keywords: Spring Boot, resilience, fault isolation, validation, logging.
- Boundary: No invented success rate, retries, SLAs or all-report-system ownership.

### Search / MongoDB / Solr

- Summary: Propagated response-header metadata/filter context through content/retrieval paths and Java index synchronization
- Status: STRONG.
- Evidence IDs: SERVER-023, SERVER-024.
- Verified metrics / scope: Response-header indexing/filter scope; no record count.
- JD keywords: Solr, MongoDB, search, indexing, metadata.
- Boundary: Existing model/vector/embedding infrastructure is not personal invention.

### Data Migration / Backfills

- Summary: Implemented tenant-aware email-template migration preserving edited content, response-header backfills and preference compatibility
- Status: STRONG.
- Evidence IDs: SERVER-017, SERVER-024, SERVER-028.
- Verified metrics / scope: Historical migration code; rollout/execution must be checked per record.
- JD keywords: data migration, backfill, tenant-aware, compatibility.
- Boundary: No universal idempotency/rollback or proven execution from a release hook.

### External Integrations

- Summary: Repaired provider diagnostics, Slack markup normalization, SharePoint ranking/configuration and organization glossary integration
- Status: STRONG.
- Evidence IDs: SERVER-020, SERVER-021, SERVER-022, SERVER-026.
- Verified metrics / scope: Scoped contributions to existing connectors; DeepL begins as POC.
- JD keywords: integrations, API troubleshooting, Markdown, configuration, translation.
- Boundary: Not sole connector/authentication architecture; no measured relevance/security gain.

### RAG / Retrieval Data Flow

- Summary: Current BASE reports replacing keyword retrieval with Atlas Vector Search/OpenAI embeddings through Java/Spring Boot APIs. Additional code-backed detail covers response-header metadata/filters, Mongo/Solr updates and backfill.
- Status: STRONG data flow; SUPPORTED broader baseline.
- Evidence IDs: SERVER-023, SERVER-024.
- Verified metrics / scope: Current approved result: 30% better search relevance, Software Engineer September 2024–September 2025 (SERVER-037). Code-supported data plumbing remains SERVER-023/024; no extra intent-traversal mechanism is inferred from the BASE.
- JD keywords: RAG, vector search, embeddings, retrieval filters, context.
- Boundary: Preserve the confirmed 30% relevance result; do not invent model/embedding-engine ownership, a measurement method, recall percentages or other additional results.

### AI Application Persistence

- Summary: Implemented Agent Studio conversation/input and reopenable canvas persistence with compatibility fixes
- Status: STRONG.
- Evidence IDs: SERVER-027, SERVER-036.
- Verified metrics / scope: Mongo persistence and response-contract/merge fixes.
- JD keywords: AI applications, conversation persistence, MongoDB, compatibility.
- Boundary: SSE ownership is now user-confirmed via SERVER-032; these DTOs alone do not establish ADK/model runtime ownership. Some DTO changes are collaborative; tests include ignored history.

### Dynamic API Hackathon

- Summary: AI-Powered External Source Connector: a Java/LLM hackathon prototype interpreted API documentation, identified endpoints/parameters and executed authenticated OAuth/API-token requests. Its concept later evolved into a production AI Search connector; July Phase II details remain separate.
- Status: SUPPORTED HACKATHON; POC code.
- Evidence IDs: SERVER-029.
- Verified metrics / scope: Current BASE: 5+ service demos including Chorus/Jira and later production-concept evolution (SERVER-037). Supporting internal period: June 2026; July branch work remains separate; no printed project dates.
- JD keywords: Java, AI integrations, OAuth, API tokens, lazy discovery.
- Boundary: Prototype implementation and later production-concept evolution are confirmed. This does not establish sole ownership of every production subsystem or turn July branch code into June demo evidence.

### Testing

- Summary: Added mocked JUnit/Mockito API/DAO tests and Python Sonar reporting tests
- Status: TOOLING.
- Evidence IDs: SERVER-006, SERVER-030, SERVER-031.
- Verified metrics / scope: 11 Python tests passed in prior audit; Java suite not run there.
- JD keywords: JUnit, Mockito, unit tests, mocking, Python.
- Boundary: Do not claim whole Java suite passing, coverage percentage or all legacy DB-backed tests isolated.

### Sonar / Quality Tooling

- Summary: Corrected coverage aggregation to avoid overlapping-path double counts; added weighted module reporting, Java null fixes and review requests
- Status: TOOLING.
- Evidence IDs: SERVER-010, SERVER-030, SERVER-031.
- Verified metrics / scope: One reporting initiative; 11 Python tests, not new Java coverage.
- JD keywords: SonarQube, coverage reporting, static analysis, Python.
- Boundary: Dockerized Sonar in Jenkins CI and Lyra deployment/Sonar management are USER-CONFIRMED via SERVER-033/LYRA-025; collaborator reviews remain reviews and no all-employer CI ownership is inferred.

### Commerce Backend / GraphQL / PostgreSQL

- Summary: Freelance E-Commerce Platform: released/maintained Next.js/Vercel product/cart/checkout/order-dashboard flows, GraphQL schemas/resolvers, Google/Discord OAuth, RBAC and PayRam-triggered license delivery with Neon PostgreSQL/S3.
- Status: PROJECT; SUPPORTED production baseline.
- Evidence IDs: SERVER-037 current BASE; SERVER-034 supplementary detail.
- Verified metrics / scope: Freelance May 2026 – June 2026; two OAuth providers.
- JD keywords: GraphQL, PostgreSQL, Neon, OAuth, RBAC, payments.
- Boundary: Separate project production; no employer GraphQL/PostgreSQL implementation inference.

### Deployment / S3 / Vercel / VPS

- Summary: Commerce S3 image storage, Vercel app deployment and separately hosted PayRam on Ubuntu VPS with SMTP notifications
- Status: PROJECT.
- Evidence IDs: SERVER-037 current BASE; SERVER-034 supplementary detail.
- Verified metrics / scope: Named project deployment/storage services.
- JD keywords: Amazon S3, Vercel, Linux, deployment, SMTP.
- Boundary: No broad AWS architecture; SMTP is delivery, not user authentication.

### Personally Scoped Internship Work

- Summary: Extended project-template creation activities/projection and repaired Java null/static-analysis behavior
- Status: STRONG.
- Evidence IDs: SERVER-009, SERVER-010.
- Verified metrics / scope: January/March 2023 authored contributions.
- JD keywords: Java, background-process extension, Mongo projection, static analysis.
- Boundary: Spring Boot REST/backend background-processing ownership is USER-CONFIRMED via SERVER-033; retain CODE detail in SERVER-009/010 and do not invent API count or pipeline scale.

## Attribution / Metric Quick Reference

| Fact | Safe use | Record |
|---|---|---|
| One membership API response | Combined API contract; no original call count/latency | SERVER-006 |
| Exactly 11 excluded fields | Count in inspected selective Mongo projection only | SERVER-007 |
| 15+ fields | Invented historical number; not a verified metric | SERVER-007 |
| 11 Python tests | Prior audit run of Sonar reporting tests, not Java coverage | SERVER-030 |
| 5+ integration demos | June hackathon baseline, not July branch rollout | SERVER-029 |
| Two OAuth providers | Freelance Google/Discord implementation | SERVER-034 |
| SSE / Redis guest sessions | USER-CONFIRMED / PERSONAL IMPLEMENTATION; SSE polling overhead reduced 60% | SERVER-032 |

Deployment, test execution and benchmark evidence must be checked independently of authored code. Missing measurement does not justify an invented result.

## Best Resume Candidates

Factual building blocks; select by JD and preserve the stated attribution/status.

1. Support-aware super-admin username protection — SERVER-001.
2. Permission/input checks and company-scoped user onboarding lookup — SERVER-002.
3. Historical TOTP QR-provider repair, clearly superseded — SERVER-003.
4. Document import default-font fallback repair — SERVER-004.
5. Daily-report per-company failure isolation — SERVER-005.
6. Combined business-unit membership response with Mongo DAO refactor — SERVER-006.
7. Mocked JUnit/Mockito tests tied to membership/data-access contracts — SERVER-006.
8. Selective user-list data minimization; omit invented 15+ — SERVER-007.
9. Discussion hidden-user persistence and E-Sign compatibility — SERVER-008.
10. Internship project-template activity/projection extension — SERVER-009.
11. Targeted Java null/static-analysis fixes — SERVER-010.
12. Organization-activity list/count pagination — SERVER-015.
13. Email route/render compatibility and edited-template-preserving migration — SERVER-016, SERVER-017.
14. Gmail/Outlook HTML repair and URL metadata transformation — SERVER-018, SERVER-019.
15. Slack markup-to-search-text normalization — SERVER-021.
16. SharePoint ranking and integration upsert/configuration fixes — SERVER-022.
17. Response-header retrieval/answer-context propagation and backfills — SERVER-023, SERVER-024.
18. Agent Studio Mongo persistence/reopenable canvases — SERVER-027.
19. Weighted Sonar coverage aggregation with tested Python reporting — SERVER-030.
20. Separate freelance GraphQL/PostgreSQL/auth/payments/deployment — SERVER-034.

## JD Keyword Map

| JD keyword / capability | Evidence IDs |
|---|---|
| Java REST | SERVER-001, SERVER-002, SERVER-006 |
| Spring Boot reporting resilience | SERVER-005 |
| MongoDB / DAO | SERVER-006, SERVER-007, SERVER-015, SERVER-017 |
| Authorization | SERVER-001, SERVER-002, SERVER-012, SERVER-014 |
| Data migration | SERVER-017, SERVER-024, SERVER-028 |
| RAG / vector search / Solr | SERVER-023, SERVER-024 |
| Integrations | SERVER-020, SERVER-021, SERVER-022, SERVER-026, SERVER-029 |
| AI persistence | SERVER-027 |
| JUnit / Mockito | SERVER-006 |
| Sonar / Python testing | SERVER-010, SERVER-030, SERVER-031 |
| Verified internship scope | SERVER-009, SERVER-010 |
| GraphQL / PostgreSQL / payments / deployment | SERVER-034 |
| SSE / Redis / OTP personal implementation | SERVER-032 |
| Internship Spring Boot/REST/background work; Dockerized Sonar/Jenkins | SERVER-033, SERVER-009, SERVER-010 |

## Important Boundaries

- Framework precision: JAX-RS/Jersey controllers are not automatically Spring MVC; distinguish Spring Boot module context.
- One membership API does not establish original call count, latency or bytes saved; 15+ fields is invented.
- Code/merge/release scheduling does not by itself prove production rollout or current behavior.
- June hackathon baseline and July prototype branch contributions have different dates/provenance.
- No broad AWS, universal integrations, secure-by-audit or invented accuracy/traffic/revenue claims.
- Use the latest USER-CONFIRMED / PERSONAL IMPLEMENTATION corrections in SERVER-032/033 over historical archive labels. Permanent BASE changes require explicit user authorization; ordinary JD tailoring uses duplicates.

## Latest Canonical Resume-Safe Contributions

The 2026-11-23 BASE confirmation is current; SERVER-037 records its printed backend/project facts. The following earlier 2026-10-03 confirmations remain supplementary personal implementation evidence, superseding old negative attribution labels within their scope. They are not fresh transport/CI code inspections or measurements.

| Contribution | Current status | Evidence / boundary |
|---|---|---|
| SSE implementation; 60% client polling-overhead reduction | USER-CONFIRMED / PERSONAL IMPLEMENTATION; resume-safe YES | SERVER-032; no invented event/reconnect internals or fresh benchmark |
| Redis caching and OTP verification for secure guest access/session management | USER-CONFIRMED / PERSONAL IMPLEMENTATION; resume-safe YES | SERVER-032; distinct from historical TOTP QR repair SERVER-003 |
| Dockerized Sonar validation in Jenkins CI; Lyra deployment/Sonar management | USER-CONFIRMED / PERSONAL IMPLEMENTATION; resume-safe YES | SERVER-033, LYRA-025; no all-employer CI ownership; hosted job internals uninspected |
| Internship Spring Boot REST APIs/Java background processing with product/QA | USER-CONFIRMED / PERSONAL IMPLEMENTATION; resume-safe YES | SERVER-033 plus code-backed project-template/activity metadata SERVER-009 and null/static-analysis fixes SERVER-010 |
| Membership/user metadata in one permission-checked Java API response; MongoDB DAOs/projection and JUnit/Mockito during SBOM remediation | USER-CONFIRMED / PERSONAL IMPLEMENTATION plus scoped CODE evidence | SERVER-006, SERVER-007; no broad SBOM/CVE/tooling ownership or latency claim |

## Historical Quantity Not for Public Use

- 15+ response fields remains HISTORICAL / INVENTED (USER-CONFIRMED); do not restore it as a verified metric.
- The inspected selective Mongo projection excludes exactly 11 fields in that path.
- Additional supported backend wording may use selective projection without an invented quantity, MongoDB DAO refactoring, one Java API response, JUnit/Mockito and scoped SBOM remediation. These are reserve facts, not statements that they are printed in the current BASE.
- Evidence: SERVER-006, SERVER-007. This re-verification does not invent additional excluded fields or universal fixes.

## Current BASE and supplementary backend context

Use SERVER-037 / resume-baseline.md for the current printed retrieval, commerce and connector claims. Reporting resilience, membership APIs, DAOs/projection/JUnit/Mockito, MongoDB–Solr synchronization and internship backend work remain available as individually supported JD-relevant input, not a separate Full Stack BASE. Preserve their original periods. S3 build-cache reuse is CORE-005; project S3 product data/image storage is SERVER-034/037. Neither establishes Lambda, DynamoDB, Step Functions, IaC or broad AWS ownership.
