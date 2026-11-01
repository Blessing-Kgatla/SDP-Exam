# Trials, release, operations, business and maintenance

## Prototype, alpha, beta, trial, and release strategy

### Distinguish stages

| Stage | Goal | Typical participants |
|---|---|---|
| Proof of concept | Validate technical feasibility | Developers/researchers |
| Prototype | Validate proposed UX/workflow | Designers, stakeholders, selected users |
| Alpha | Find major defects in integrated product | Internal testers |
| Closed beta | Test real usage and reliability | Invited external users |
| Open beta | Test wider compatibility and operational readiness | Larger audience |
| Production | Provide a supported and stable service/product | Intended customers |

**A commercial free trial is not a beta.** It is a business and onboarding mechanism for a product otherwise ready to serve customers. Never use “beta” or “trial” as cover for unsafe money/data handling.

### Beta plan template

```markdown
# Beta Plan
- Objective and hypotheses:
- Audience, sample size and eligibility:
- Platform/device mix:
- Features in and out of scope:
- Test scenarios and tasks:
- Data/privacy terms and consent:
- Feedback channels and bug reporting template:
- Issue severity, triage owner and response process:
- Metrics and baseline:
- Test duration and evaluation checkpoints:
- Stop/rollback conditions:
- Exit criteria and release decision owner:
- Known limitations:
```

### Example beta exit criteria (adjust to risk)

- Zero unresolved critical defects.
- All mandatory P0/P1 acceptance tests pass.
- No unexplained data loss or corruption.
- Authorization/security blockers resolved.
- Major usability blockers fixed or clearly scoped out with mitigations.
- Required backup/restore path tested.
- Supported device/browser combinations checked.
- Core success metrics reached, or deviation understood and documented.

For regulated/safety-critical software, these are **not sufficient** on their own; use formal validation and review applicable to that domain.

### Commercial trial policy

Explicitly define:

| Aspect | Requirement |
|---|---|
| Eligibility | Who gets a trial and whether it repeats |
| Duration | Days, feature entitlement or usage quota |
| Features | Available vs limited capabilities |
| Expiration | Behavior on expiry and restrictions |
| Payment | Whether card required; billing date and notification |
| Data | Data preservation, access, deletion and export after expiry |
| Conversion | How trial becomes paid, and exact price displayed |
| Cancellation | Easy and explicit cancellation process |
| Communication | Clear terms, renewal notices and reminders |
| Abuse/fraud | Reasonable protections without harmful UX |

Never automatically charge, revoke data access, or promise permanent retention without clearly specified policy and legal review.

## Infrastructure, operations, monitoring, and recovery

### Deployment plan

- **Environments:** Development, test/staging, production; production secrets separated.
- **Version control:** Meaningful commits, PR/review policy appropriate to team size.
- **CI:** Lint, typecheck, tests, build, dependency checks as warranted.
- **CD:** Deployment credentials, explicit gates, migration plan, rollback/forward recovery.
- **Hosting:** Choose durable storage for database/files, suitable regions and service limits.
- **Configuration:** `.env.example` lists keys without credentials; required variables validated at startup.
- **Distribution:** Domain/DNS/HTTPS, mobile store assets, desktop installers/signing, game releases.
- **Observability:** Logs, error reports, operational metrics, user-impacting alerts.
- **Recovery:** Tested backups, restore process, incident response and owners.
- **Documentation:** Runbooks, release notes, known limitations, support steps.

### Service objectives

Define service level objectives **where online availability matters** (successful request rate, latency, error budget, recovery objectives). Measure them with representative traffic. Avoid arbitrary “99.99% uptime” declarations unsupported by budget or infrastructure.

### Incident response and operational questions

- Who receives an alert? How is severity determined?
- What is the user's impact and who communicates it?
- Can a bad release be rolled back safely?
- How do DB schema changes and older clients interact?
- When were backups last successfully restored?
- Can the application operate if payment/maps/email provider is unavailable?
- How are logs retained and redacted?
- How does the team end an incident and prevent recurrence?

### Operating cost model

Track costs for development, domain/DNS/business email, app hosting, database, object storage, backups, bandwidth/CDN, APIs (maps/SMS/email/AI), payment processing, app stores and signing, compliance, marketing, customer support and ongoing maintenance.

Estimate three scenarios: **development**, **normal production**, and **growth/peak**. For paid products, estimate revenue, gross margin, churn/retention assumptions and unit economics. For offline apps, cloud costs may be near zero but distribution/support/maintenance still cost time and money.

## Business, pricing, legal, marketing, and support

### Business model options

- Free/open-source; one-time purchase; freemium; subscription; per-seat licensing; usage-based pricing; marketplace commissions; paid support; enterprise contracts; sponsorship/advertising where appropriate.
- Specify what customers pay for, billing period, currencies, taxes, refunds, cancellations, data migration and entitlement changes.
- Avoid paywalls/advertising that contradict the product's primary task or audience needs.

### Legal/IP checklist

- [ ] Legal entity and contracting requirements considered if commercial.
- [ ] Terms, privacy notices, consent and consumer disclosures appropriate to jurisdiction.
- [ ] Licenses verified for source code dependencies, fonts, photographs, music, datasets and models.
- [ ] Trademark/name/domain conflicts investigated where material.
- [ ] Relevant industry rules and tax/payment obligations checked.
- [ ] Appropriate age restrictions, moderation and user safety rules defined.
- [ ] Data-processing agreements/cross-border requirements addressed if relevant.
- [ ] User rights around data export, deletion, subscriptions and cancellation understood.

### Launch and distribution

Plan app/site naming, branding, logo, authentic screenshots, store listings, SEO/app store search, onboarding, product demonstrations, vertical and horizontal video assets where useful, documentation, FAQs and contact/support mechanisms. For social channels, tailor outputs to platform aspect ratios and conventions rather than recycling a single asset unchanged.

**Marketing truthfulness:** No fake usage metrics, testimonials, comparisons, certifications or supported-feature claims. Promotional screenshots/videos must represent the real product or be explicitly identified as concept demonstrations.

### Product adoption/retention

Track only metrics that answer important product questions (activation, successful core tasks, retained usage, conversion, errors, support themes). Favor privacy-conscious analytics. Local-only privacy-focused applications do not need an analytics backend merely because typical SaaS products have one.

## Long-term maintenance and evolution

Plan beyond launch:

| Responsibility | Approach |
|---|---|
| Bug fixes | Severity definitions, triage, issue ownership |
| Feature updates | Evidence-based roadmap, impact on existing workflows |
| Security | Dependency review, vulnerability response, credential rotation |
| Platform compatibility | OS/browser/app store/API change monitoring |
| Data | Migration testing, integrity checks, backups |
| Technical debt | Scheduled simplification and refactoring after learning |
| Performance | Regression tracking on representative devices |
| Documentation | Keep setup, runbooks and product behavior accurate |
| Support | Feedback intake, help content and escalation |
| Retirement | Communication, export, retention/deletion and safe shutdown |

Write change logs for user-visible behavior. Version APIs and stored data where existing clients depend on them. Don't leave undocumented automation or fragile operational knowledge in one person's memory.
