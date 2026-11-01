# Discovery, requirements and UX deliverables

## The 20 pillars of product planning

Cover these areas according to project size and risk:

| # | Pillar | Required decisions / outcome |
|---|---|---|
| 01 | **Product identity** | Name, category, vision, purpose, differentiation |
| 02 | **Market research** | Audience, alternatives, competitors, actual unmet needs |
| 03 | **User research** | Personas/jobs, pain points, environments, expectations |
| 04 | **Requirements** | Functional/nonfunctional behavior and constraints |
| 05 | **Scope and roadmap** | MVP, priorities, excluded features, future releases |
| 06 | **User journeys** | Navigation, onboarding, workflows, errors and recovery |
| 07 | **UI/UX** | Layout, design system, usability, accessibility, responsive behavior |
| 08 | **System architecture** | Frontend, backend, modules, service boundaries, integrations |
| 09 | **Data architecture** | Entities, constraints, storage, migrations, retention, backups |
| 10 | **Security/privacy** | Authentication, permissions, threat model, protection and rights |
| 11 | **Compatibility** | Devices, browsers, OS versions, input, permissions |
| 12 | **Performance** | Speed, battery, network, memory, resource budgets and load |
| 13 | **Offline/sync** | Local data, network failures, queues, conflicts, recovery |
| 14 | **Testing/QA** | Unit, integration, E2E, performance, accessibility, security tests |
| 15 | **Infrastructure** | Hosting, environments, CI/CD, backups, monitoring, rollback |
| 16 | **Business model** | Pricing, subscriptions, recurring costs, unit economics |
| 17 | **Legal/compliance** | Licenses, privacy terms, industry-specific obligations |
| 18 | **Trials/betas** | Test audience, goals, feedback, release criteria, trial policies |
| 19 | **Marketing/distribution** | Discovery, SEO/app stores, demonstrations, launch, support |
| 20 | **Maintenance** | Upgrades, incidents, customer feedback, lifecycle/retirement |

## Product discovery, research, and scope

### Research questions

1. What problem exists, who has it, and how frequently or severely?
2. What do target users do today instead? Why are existing alternatives inadequate?
3. What single outcome proves the product delivered value?
4. Who are primary/secondary audiences, and what devices/environments do they use?
5. What are comparable products' useful patterns, strengths, weaknesses, prices, and trust signals?
6. What capability, distribution channel, niche, local context, or experience differentiates this product?
7. Is the proposed solution technically feasible within constraints?
8. What operating costs or legal requirements threaten feasibility?
9. What assumptions are untested, and how can a prototype/pilot test them?
10. What measurable criteria define success (completion, conversion, retention, accuracy, reliability, etc.)?

### Research deliverables

- **Product brief:** Problem, value proposition, audience, unique approach.
- **Assumptions log:** Supported facts vs assumptions vs unknowns.
- **Competitor/alternative review:** Compare task support and real interactions, not screenshots alone.
- **User model:** Roles, jobs, constraints, accessibility, context of use.
- **Risk register:** Severity, likelihood, owner, mitigation, validation action.
- **Success metrics:** Baselines, targets, measurement method, review date.

### Scope controls

- **P0 essential:** Required for core product purpose.
- **P1 important:** Required for reliable and usable initial release.
- **P2 enhancement:** Valuable but can follow later.
- **P3 optional:** Experimental, cosmetic or low impact.

Explicitly document **out of scope** items. Use a single complete core journey for MVP rather than dozens of partially implemented features. Scope should include required security, data integrity, accessibility and recovery for the MVP's level of risk.

## Requirements, user stories, and acceptance criteria

### Feature specification template

```markdown
### FEATURE-ID — Feature name
- **Priority:** P0 / P1 / P2 / P3
- **Goal:** What user outcome does this support?
- **Actors/roles:** Who can perform it?
- **Preconditions:** What must already be true?
- **Trigger:** How is it started?
- **Inputs:** Required and optional data; types/constraints.
- **Primary flow:** Numbered user/system interaction sequence.
- **Alternate flows:** Empty, invalid, duplicate, missing permission, interrupted network, etc.
- **Business rules:** Pricing, scheduling, visibility, limits, calculations.
- **Data changes:** Reads, writes, side effects, retention.
- **Permissions:** Who can view/create/update/delete; server enforcement.
- **Dependencies:** Other features, APIs, OS permissions.
- **Failure/recovery:** Clear feedback, retry/undo, idempotency as appropriate.
- **Acceptance criteria:** Observable checks in Given/When/Then or equivalent.
- **Tests:** Unit/integration/E2E/edge cases.
```

### Example: registration

**AUTH-001 — User account registration**

- Actor: unauthenticated visitor.
- Objective: create personal account when accounts are actually necessary.
- Flow: open registration → enter details → validate client/server → detect duplicate identity → create securely → perform required verification → show next step.
- Exceptions: duplicate email, weak password, invalid input, expired verification, service unavailable, double-submit.
- Acceptance: valid registration succeeds once; invalid/duplicate submissions don't create duplicate accounts; privileged access isn't granted until required checks pass; error messages avoid revealing sensitive details.

### User story pattern

> As a **[role]**, I want **[capability]**, so that **[outcome]**.

Every story must have testable acceptance criteria, dependencies, failure scenarios, and a rationale tied to a user problem. Do not substitute a feature list for behavior specifications.

### Permissions matrix

Create a CRUD/action matrix when there are multiple roles:

| Resource/action | Guest | Member | Manager | Administrator |
|---|---:|---:|---:|---:|
| View public records | Yes | Yes | Yes | Yes |
| View own private records | No | Own only | Policy-based | Policy-based |
| Create/edit own records | No | Own only | Policy-based | Policy-based |
| Manage team users | No | No | Scoped | Scoped |
| Manage all records | No | No | No | Only if expressly authorized |

**Example only:** Specify real role names/scopes and test every server-side permission. Administrator status does not automatically imply permission to inspect all sensitive records.

## Nonfunctional requirements and measurable targets

Functional requirements define **what** the system does; nonfunctional requirements define **how well and under what conditions**.

| Dimension | Planning prompts | Example measurable target (illustrative only) |
|---|---|---|
| Performance | Startup, LCP, navigation, API latency | A defined p95 API latency under defined load |
| Reliability | Crash/error tolerance | Core workflow completes in repeated failure-injection tests |
| Availability | Required hours and outage impact | SLO agreed based on actual user needs |
| Scalability | Users, data volume, writes | Load test against stated peak and concurrency |
| Security | Threats, sensitive operations | No unresolved release-blocking findings |
| Privacy | Collection/retention/rights | Data lifecycle and deletion/export validated |
| Accessibility | Keyboard, labels, contrast | Target WCAG 2.2 AA where applicable |
| Maintainability | Architecture, tests, documentation | Critical modules have tests and ownership |
| Portability | Platforms and migrations | Runs on supported OS/browser matrix |
| Data integrity | Concurrent writes, retries | No duplicate bookings/charges under race tests |
| Observability | Logs, diagnostics, alarms | Critical errors can be identified and traced |
| Recoverability | Backups, restore, incidents | Restore drill completed within stated recovery objective |
| Resource efficiency | RAM/CPU/battery/network | Tested on minimum supported device |
| Localization | Language, time zones, currencies | Dates/currency/translation behave correctly for target locale |

Targets must be realistic, contextual, measurable, and tested. Don't copy invented targets into production requirements as if they were approved. For maps/GPS, define accuracy under actual conditions; for activity tracking, test screen-off behavior; for finance, define numerical precision and reconciliation; for games, define frame rate/input targets on target hardware.

## UX deliverables and interaction-state matrix

### Required design artifacts

1. User journey map for every essential role/job.
2. Information architecture and navigation tree.
3. Screen inventory with purpose, entry/exit points, and connected features.
4. Low-fidelity mobile/desktop wireframes, followed by responsive high-fidelity designs.
5. Design-system tokens: colors, text, spacing, sizing, borders, shadows, iconography, motion.
6. Component inventory and behavior specifications.
7. Accessibility behavior (focus, labels, keyboard, screen readers, contrast, touch sizes, reduced motion).
8. Content and error message guidelines; consistent terminology.
9. Tests using realistic content/data and device sizes.
10. Documented handoff from screens to implemented workflows.

### UX pattern guidance

- Use appropriate progressive disclosure instead of either hiding essentials or showing all options constantly.
- Make forms short but complete, with proper labels, defaults, validation and accessible errors.
- Respect browser/device back behavior, deep links, and navigation history.
- Make user control explicit for important actions, notifications, data deletion and exports.
- Use context-specific language, not generic inspirational copy.
- Maintain predictable focus and action placement; don't over-animate ordinary operations.
