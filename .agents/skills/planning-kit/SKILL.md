---
name: planning-kit
description: Templates and checklists for planning a product end to end. Covers the 20 planning pillars, discovery questions, feature-spec and user-story templates, permissions matrix, nonfunctional targets, data and API checklists, offline/sync and platform matrices, testing types, beta/trial/release plans, operations and cost model, legal and business checklists, documentation structure, ADRs, the planning-readiness scorecard, and the standard planning-output format. Use it for new products, major features, or whenever a written plan, spec, beta plan or release checklist is requested.
---

# Planning kit

Match the depth to the project level in AGENTS.md §12.1. A Level 1 utility needs only a brief, a feature list, the stack and basic tests. Don't produce a document set for a small change.

| Need | Read |
|---|---|
| Planning pillars, discovery questions, research deliverables, P0–P3 scope, feature-spec template, user stories, permissions matrix, nonfunctional targets, UX deliverables | `discovery-and-requirements.md` |
| Data modelling checklist, data portability, platform compatibility matrix, offline-first rules, device feasibility, architecture spec, API checklist, integration register, test types, traceability, performance budgets | `architecture-and-quality.md` |
| Prototype→production stages, beta plan template and exit criteria, commercial trial policy, deployment plan, SLOs, incident questions, cost model, business models, legal/IP checklist, launch, maintenance | `release-and-operations.md` |
| Documentation tree, ADR template, planning-readiness checklist, **standard planning-output format**, reference links (frameworks, security, Coder, Claude) | `docs-and-planning-output.md` |

## Use

- For a new product, produce the plan in the format from `docs-and-planning-output.md`. In Coder, present it through Plan Mode / `propose_plan` before implementing, and keep it at `.coder/plans/`.
- Create a document only when it records a real decision. Don't leave empty templates behind.
- Label illustrative numbers (targets, costs, metrics) as assumptions until the owner approves them.
