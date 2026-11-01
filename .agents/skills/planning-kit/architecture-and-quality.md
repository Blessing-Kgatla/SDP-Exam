# Data, platforms, architecture and quality

## Data architecture and lifecycle

### Design the information before tables

Define entities, meaning, ownership, identifiers, relationships, constraints, derived values, and invariants. Typical example for an order-based product:

```text
User ──< Order ──< OrderItem >── Product
  │        │
  │        └── PaymentAttempt
  └──< Address
```

This is only illustrative. Real structures depend on inventory allocation, payment processing, guest checkout, tenancy, compliance and fulfillment.

### Data-planning checklist

- [ ] Entities and attributes defined with types and validation.
- [ ] Primary/foreign keys and unique constraints defined.
- [ ] Record ownership/tenant boundaries documented.
- [ ] Query patterns and indexing needs identified.
- [ ] Important state transitions and transactions specified.
- [ ] Handling for duplicates, concurrent edits and retries established.
- [ ] Data creation, retention, archival and deletion documented.
- [ ] Export/import options defined for user-controlled data.
- [ ] Schema migration strategy and rollback/forward compatibility defined.
- [ ] Backups and restore drills planned for valuable information.
- [ ] Offline/sync rules defined if multiple devices can modify the same data.
- [ ] Audit log policy defined for important changes.
- [ ] Personal data minimization and access restrictions reviewed.

### Data portability and trust

For local-only applications, provide a sensible export/backup strategy when users could lose important data. For online services, provide controlled exports, deletion/retention policies and recoverability where required. Document how users can leave the product without becoming trapped by an undocumented proprietary data format.

## Platforms, hardware, offline use, and synchronization

### Compatibility matrix

| Platform | Verify before implementation/release |
|---|---|
| Web | Supported browsers, responsive breakpoints, keyboard/touch, SEO where relevant, storage limits |
| Android | Minimum API level, permissions, foreground/background service restrictions, battery optimization, screen sizes |
| iOS | Minimum iOS version, lifecycle and background modes, permissions, distribution/App Store constraints |
| Windows | Installer, code signing expectations, permissions, update/uninstall behavior |
| macOS | App signing/notarization, sandboxing/permissions, CPU architectures |
| Linux | Target distributions, packaging, desktop environment differences |
| Offline browser | Cache/storage behavior, export, eviction and failed network handling |
| Game | GPU/performance budgets, input devices, resolution, save data, engine exports |

### Offline-first design

When offline capability is required:

1. Identify which tasks must work without a network and which cannot.
2. Keep a clear local source of truth while disconnected.
3. Persist locally before showing “saved” feedback for important records.
4. Queue external work with retry, backoff, and idempotency where appropriate.
5. Expose sync status and unsynced changes to the user when meaningful.
6. Establish conflict resolution: last-write-wins only when safe, merge when possible, explicit conflict resolution when necessary.
7. Test airplane mode, app termination, device clock changes, low storage, corrupted files, forced logout and interrupted sync.
8. Provide export/backup or recovery as appropriate to the value of local data.

### Device-specific functionality

Research native feasibility before designing “magic” buttons. GPS recording, call/SMS access, app blocking, file-system access, notifications, biometric security, background video/audio, and sensors all depend on OS permissions and app store policies. A UI mockup alone does not establish that the feature is implementable.

## Architecture, APIs, and integrations

### System architecture specification

Record:

- **Application boundaries:** Which operations run in browser/mobile client, server, native host or background worker?
- **Module ownership:** Each business rule has one clear home; avoid circular feature dependencies.
- **Data boundaries:** Which system is source of truth; what can be cached/offline?
- **API contracts:** Routes, methods, schemas, errors, authorization, versioning and pagination.
- **External integrations:** Payment, maps, storage, SMS, email, push, authentication, AI inference, analytics.
- **Async processes:** Which jobs require durable queues, retries, cancellation, monitoring?
- **Concurrency:** How to prevent duplicate or conflicting mutations.
- **Failure handling:** Timeouts, circuit behavior if warranted, retries and fallbacks.
- **Caching:** What to cache, TTL/invalidation and correctness constraints.
- **Portability:** Provider lock-in risks and feasible escape plans.

### Recommended default: modular monolith

```text
UI / presentation
       |
Application layer (use cases and permissions)
       |
Domain / business rules
       |
Persistence + external integrations
```

The layers need not always be separate folders in small apps. Separate concerns logically. Add a dedicated API backend only if required for independent clients, unsupported server behavior, integration ownership or meaningful team/deployment constraints.

### API design checklist

- [ ] Request and response contracts documented.
- [ ] Input validation performed at server/trust boundary.
- [ ] Authentication and per-record authorization applied.
- [ ] Appropriate HTTP statuses and actionable error formats.
- [ ] Pagination/filter/search where result sets can grow.
- [ ] Explicit idempotency for risky repeatable mutations.
- [ ] Appropriate timeouts and retry rules.
- [ ] Versioning/backward compatibility policy when external clients depend on API.
- [ ] Logs and trace identifiers without leaking personal information.
- [ ] API tests covering invalid, unauthorized, duplicate and concurrent requests.

### Third-party integration register

For each integration document: purpose, provider, API version, data shared, data classification, cost/quotas, rate limits, outage handling, secret management, test mode, webhook verification, logging, renewal/version changes and a fallback. Don't install a service merely because it is popular.

## Testing and quality assurance

### Tests to choose from

| Type | Checks |
|---|---|
| Unit | Pure business rules, calculations, validation and state transitions |
| Integration | DB, auth, APIs, storage, queues and provider boundaries |
| End-to-end | Complete realistic workflows from entry to persisted outcome |
| UI | Navigation, focus, interaction, states and regression |
| Accessibility | Keyboard, semantics, assistive technology, WCAG criteria |
| Performance | Runtime, memory, battery, latency, rendering and startup |
| Load | Expected concurrent demand/peak operations |
| Stress | Degradation/failure behavior beyond intended limits |
| Security | Authorization bypass, injection, secrets, unsafe upload, abuse |
| Compatibility | Browsers, OS versions, form factors, input devices |
| Offline | No connectivity, resumed sync, conflicts, local durability |
| Recovery | Crash, interrupted transactions, backups/restore, failed upgrades |
| Regression | Existing features remain functional after changes |
| User acceptance | Actual tasks satisfy goals and acceptance criteria |

### Traceability

Maintain a simple relationship:

```text
User need -> Feature ID -> Acceptance criteria -> Implementation -> Tests -> Release status
```

Do not mark a feature done because a component file exists or a screenshot looks convincing. Keep mocks and fixture data clearly labeled and isolated from production paths.

### Performance budgets

Choose measurable targets based on real audience/device/network conditions. Test on representative lower-end hardware, not only the developer's machine. For high-risk data systems, test data consistency under concurrent writes and repeated requests. For gaming/graphics, measure frame times and input latency; for fitness, measure GPS and battery behavior with screen off.
