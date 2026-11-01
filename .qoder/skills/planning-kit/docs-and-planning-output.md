# Delivery phases, documentation structure, readiness checklist, planning output and references

## End-to-end delivery process with phase gates

### Nine phases

| Phase | Work | Minimum deliverable | Gate to continue |
|---|---|---|---|
| **01 Discover** | Problem, audience, alternatives, success, risks | Product brief + assumptions/risk list | Core value understood |
| **02 Specify** | Roles, user stories, workflows, requirements, scope | Prioritized requirements + MVP exclusions | Testable feature definitions |
| **03 Design** | Journey, IA, wireframes, visual system, states, responsive | Prototype + design specification | Essential journeys are usable |
| **04 Architect** | Stack, schema, boundaries, integrations, security | Architecture + data model + file tree | Major risks and design choices justified |
| **05 Implement** | Build a complete thin slice, then prioritized features | Working product + migrations + tests | Real core journey works and persists |
| **06 Verify** | Functional, edge, security, accessibility, performance | Evidence-based QA results | Release blockers resolved |
| **07 Trial** | Closed beta/pilot; representative use; feedback | Beta report + decision | Exit criteria met or documented decision |
| **08 Release** | Deploy/distribute, monitor, document, support | Supported release | Monitoring/recovery in place as needed |
| **09 Maintain** | Updates, feedback, measurement, support | Roadmap/maintenance cycle | Continue evidence-led iteration |

Phases overlap and iterate: testing starts during requirements, accessibility during design, and security during architecture—not solely before release.

## Project documentation structure

Use a subset of this structure proportional to complexity. A simple utility can use `README.md` + `PLAN.md` + tests; a serious multi-user product benefits from more detailed records.

```text
project/
├── README.md
├── docs/
│   ├── 01-product/
│   │   ├── product-brief.md
│   │   ├── target-users.md
│   │   ├── competitor-research.md
│   │   ├── success-metrics.md
│   │   └── roadmap.md
│   ├── 02-requirements/
│   │   ├── functional.md
│   │   ├── nonfunctional.md
│   │   ├── user-stories.md
│   │   ├── permissions-matrix.md
│   │   └── acceptance-criteria.md
│   ├── 03-design/
│   │   ├── design-brief.md
│   │   ├── user-flows.md
│   │   ├── information-architecture.md
│   │   ├── design-system.md
│   │   ├── responsive-behavior.md
│   │   └── accessibility.md
│   ├── 04-architecture/
│   │   ├── architecture.md
│   │   ├── tech-stack.md
│   │   ├── database-schema.md
│   │   ├── api-contracts.md
│   │   ├── integrations.md
│   │   ├── data-lifecycle.md
│   │   └── decisions/
│   ├── 05-security/
│   │   ├── threat-model.md
│   │   ├── privacy-plan.md
│   │   ├── security-requirements.md
│   │   └── incident-response.md
│   ├── 06-testing/
│   │   ├── test-strategy.md
│   │   ├── test-cases.md
│   │   ├── beta-plan.md
│   │   └── release-criteria.md
│   ├── 07-operations/
│   │   ├── deployment.md
│   │   ├── monitoring.md
│   │   ├── backups.md
│   │   ├── cost-model.md
│   │   └── maintenance.md
│   └── 08-business/
│       ├── pricing.md
│       ├── legal-checklist.md
│       ├── marketing-plan.md
│       └── launch-plan.md
├── src/
├── tests/
└── .github/
    └── workflows/
```

**Avoid dozens of empty documents.** Create a file when it records meaningful decisions. Use short **architecture decision records (ADRs)** for consequential choices:

```markdown
# ADR-001 — Use PostgreSQL for shared transactional data
- Status: Accepted
- Context: Multiple users create and modify shared records concurrently.
- Decision: PostgreSQL rather than a local database file.
- Alternatives: SQLite on a persistent single server; managed key-value database.
- Rationale: Concurrent writes, transactions, relational constraints, deployment fit.
- Consequences: Managed database costs, operational backup and migration needs.
- Revisit when: Measured requirements change materially.
```

## Planning-readiness checklist

These 18 baseline checks may be used as a project intake scorecard. An unchecked item means **unknown/not completed**—not automatically a failed project. High-risk items cannot be waived solely because a numeric score is high.

### Product (3)
- [ ] Target users and problem clearly defined.
- [ ] Core value and differentiator understood.
- [ ] Measurable success criteria defined.

### Requirements (4)
- [ ] Core features and business rules documented.
- [ ] MVP scope and explicit exclusions agreed.
- [ ] User roles and permissions understood.
- [ ] Critical edge cases identified.

### Experience (3)
- [ ] Primary user journeys mapped.
- [ ] Key screens, layouts and interface states planned.
- [ ] Accessibility and target device requirements established.

### Engineering (4)
- [ ] Technology choices justified by requirements.
- [ ] Data entities, access and ownership documented.
- [ ] Integrations and third-party dependencies identified.
- [ ] Security and privacy risks assessed.

### Delivery (4)
- [ ] Testing strategy and acceptance criteria planned.
- [ ] Resources and operating costs estimated.
- [ ] Deployment, backups, monitoring/recovery considered as appropriate.
- [ ] Trial/release criteria and ownership established.

**Interpretation:** A high completion percentage indicates planning coverage, not proof of correctness, security or production readiness. Apply risk-based gates and validate actual evidence.

### Standard agent output for a planning request

Use this structure, adjusting sections to project scope:

```markdown
# [Product] — Product and Engineering Plan

## 1. Executive product brief
- Problem, audience, value and differentiator
- Classification and complexity level
- Key assumptions and unknowns

## 2. Requirements and release scope
- Actors and roles
- P0/P1/P2/P3 features, exclusions
- Functional flows and acceptance criteria
- Nonfunctional and compliance requirements

## 3. UX / UI design specification
- Art direction and reasons
- Selected palette + accessible text/action variants
- Typography, imagery, layout architecture and component principles
- Site map / screen inventory / navigation
- Responsive breakpoints and state matrix
- Key user journeys and interaction behavior

## 4. Architecture and technology
- Minimal chosen stack and rationale
- Deployment model and external integrations
- Data entities/relationships/ownership/migrations
- Authentication/authorization, security, privacy
- API/contracts and offline/sync behavior if needed

## 5. Repository blueprint
- Actual project file tree tailored to features
- Naming and module boundaries
- Setup/build/test/deploy commands

## 6. Build plan
- Dependency-ordered milestones and vertical slices
- Concrete tasks and definition of done
- Tests and acceptance gates per milestone

## 7. Beta and launch
- Test audience, scenarios, metrics, feedback process
- Exit criteria and rollout
- Monitoring, backup, rollback, distribution

## 8. Costs, risks and maintenance
- Dev/monthly/growth cost drivers
- Highest risks, likelihood, impact and mitigations
- Documentation, ownership and update plan

## 9. Decisions and outstanding questions
- Decisions made
- Assumptions to confirm
- Known limitations and what was not tested
```

## Reference links

These are starting references. Confirm current framework version, licensing, requirements and documentation **at build time** rather than assuming this file captures every change.

### Frameworks and databases

- React: https://react.dev/
- Vite: https://vite.dev/
- Next.js: https://nextjs.org/docs
- Astro: https://docs.astro.build/
- Astro Starlight: https://starlight.astro.build/
- Django: https://docs.djangoproject.com/
- HTMX: https://htmx.org/docs/
- Flutter: https://docs.flutter.dev/
- Expo: https://docs.expo.dev/
- React Native: https://reactnative.dev/
- Tauri: https://tauri.app/
- Godot: https://docs.godotengine.org/
- SQLite: https://www.sqlite.org/
- PostgreSQL: https://www.postgresql.org/docs/
- Drizzle ORM: https://orm.drizzle.team/
- Drift: https://drift.simonbinder.eu/
- Dexie: https://dexie.org/
- Tailwind: https://tailwindcss.com/docs
- TypeScript: https://www.typescriptlang.org/docs/
- Zod: https://zod.dev/
- MapLibre: https://maplibre.org/
- PostGIS: https://postgis.net/
- Supabase: https://supabase.com/docs
- Better Auth: https://www.better-auth.com/docs
- Playwright: https://playwright.dev/docs/intro
- Vitest: https://vitest.dev/

### Qoder

- Rules and AGENTS.md: https://docs.qoder.com/user-guide/rules
- Skills: https://docs.qoder.com/extensions/skills
- Model selector: https://docs.qoder.com/user-guide/chat/model-tier-selector
- Documentation index: https://docs.qoder.com/llms.txt

### Quality, security, UX and public services

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
- NIST Secure Software Development Framework: https://csrc.nist.gov/pubs/sp/800/218/final
- GOV.UK Design System: https://design-system.service.gov.uk/
- Google SRE books: https://sre.google/books/
- South African Information Regulator: https://inforegulator.org.za/
- ISO 9241-210 overview: https://www.iso.org/standard/77520.html
