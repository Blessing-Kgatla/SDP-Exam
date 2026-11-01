# Technology recommendations for the 40 product categories

The **Structure** column refers to the repository layouts A–H in the `project-scaffolds` skill (`structures.md`). Folder names under **Features** are examples of domain-based modules; adapt to actual user requirements.

### Commerce and services

| # | Category | Recommended minimal reliable stack | Main features | Structure |
|---|---|---|---|---|
| 01 | E-commerce | Next.js + Drizzle + PostgreSQL | `catalog`, `cart`, `checkout`, `orders`, `inventory` | B |
| 02 | Marketplace | Next.js + Drizzle + PostgreSQL | `vendors`, `listings`, `search`, `orders`, `reviews` | B |
| 03 | Restaurant | Astro static menu; Next.js + PostgreSQL if taking orders/reservations | `menu`, `tables`, `orders`, `reservations` | A or B |
| 04 | Travel | Next.js + PostgreSQL | `destinations`, `trips`, `itineraries`, `bookings` | B |
| 05 | Hotels | Next.js + PostgreSQL | `properties`, `rooms`, `availability`, `reservations` | B |
| 06 | Real estate | Next.js + PostgreSQL | `properties`, `agents`, `search`, `viewings` | B |
| 07 | Events/ticketing | Next.js + PostgreSQL | `events`, `venues`, `tickets`, `checkin` | B |
| 08 | Service booking | Next.js + PostgreSQL | `services`, `providers`, `availability`, `appointments` | B |

**Notes:** Transactionally reserve limited inventory; confirm payments from trusted provider callbacks; don't rely only on client-side stock checks. Add PostGIS for property search only when spatial queries warrant it. Implement correct refunds/cancellations where relevant. **Check that the payment provider supports the merchant's country, currency and payout bank before designing checkout.** For South African merchants, check Stripe's current country support rather than assuming it. Local options include Paystack (Stripe-owned), Yoco, Payfast, Peach Payments and Ozow. Prices in ZAR, VAT (currently 15%) and the provider's webhook/ITN verification must be handled server-side.

### Business and enterprise

| # | Category | Recommended minimal reliable stack | Main features | Structure |
|---|---|---|---|---|
| 09 | Corporate | Astro + CSS/Tailwind + MDX | `services`, `projects`, `team`, `contact` | A |
| 10 | SaaS | Next.js + Drizzle + PostgreSQL | `auth`, `workspace`, `billing`, `settings` | B |
| 11 | ERP/admin | Django + HTMX + PostgreSQL | `accounts`, `inventory`, `operations`, `reports` | C |
| 12 | Project management | Next.js + PostgreSQL | `projects`, `tasks`, `boards`, `members` | B |
| 13 | CRM | Django + HTMX + PostgreSQL | `contacts`, `companies`, `deals`, `activities` | C |
| 14 | Banking/fintech | Next.js + PostgreSQL + regulated service providers | `accounts`, `transactions`, `ledger`, `audit` | B |
| 15 | Recruitment | Next.js + PostgreSQL | `jobs`, `candidates`, `applications`, `employers` | B |
| 16 | Developer tools | Next.js + PostgreSQL; separate Astro Starlight for docs if needed | `projects`, `api_keys`, `logs`, `usage` | B + A |

**Notes:** Django admin is excellent for **internal** back-office administration, but customer-facing tasks still deserve a proper UX. Financial software requires controls and compliance far beyond a framework decision. SaaS requires tenant isolation when users belong to different organizations.

### Media and creative

| # | Category | Recommended minimal reliable stack | Main features | Structure |
|---|---|---|---|---|
| 17 | News/magazine | Astro + MDX; CMS if editors need one | `articles`, `categories`, `authors` | A |
| 18 | Streaming | Next.js + PostgreSQL + hosted transcoding/media/CDN | `catalog`, `playback`, `profiles`, `watchlist` | B |
| 19 | Games/esports | Godot for game; Astro for promotional web | `scenes`, `scripts`, `assets`, `save` | H (+A) |
| 20 | Portfolio/agency | Astro + MDX | `projects`, `case-studies`, `about` | A |

**Notes:** Don't build a custom video transcoder or CDN as an MVP. Phaser/TypeScript may be simpler for browser-only 2D games. Use Godot when a proper game engine is appropriate.

### Education and knowledge

| # | Category | Recommended minimal reliable stack | Main features | Structure |
|---|---|---|---|---|
| 21 | LMS | Next.js + PostgreSQL | `courses`, `lessons`, `assessments`, `progress` | B |
| 22 | University | Astro for public site; Django + PostgreSQL for student/admin services | `departments`, `programmes`, `admissions` | A + C |
| 23 | Documentation/research | Astro Starlight + Markdown/MDX | `guides`, `reference`, `tutorials` | A |

### Social and community

| # | Category | Recommended minimal reliable stack | Main features | Structure |
|---|---|---|---|---|
| 24 | Social media | Expo + React Native + PostgreSQL | `feed`, `profiles`, `posts`, `notifications` | E |
| 25 | Messaging | Next.js + PostgreSQL + managed realtime if needed | `chats`, `messages`, `contacts`, `attachments` | B |
| 26 | Forums | Next.js + PostgreSQL | `communities`, `threads`, `replies`, `moderation` | B |
| 27 | Dating | Expo + React Native + PostgreSQL | `profiles`, `discovery`, `matches`, `messages` | E |

**Notes:** Use hosted storage for media, secure server-side user access rules, reporting and moderation. Consider abuse, safety, privacy and notifications during planning, not after launch. For a web-first social product, Next.js is also viable; choose Expo when mobile is the primary experience.

### Personal and public services

| # | Category | Recommended minimal reliable stack | Main features | Structure |
|---|---|---|---|---|
| 28 | Healthcare | Django + PostgreSQL | `patients`, `appointments`, `records`, `prescriptions` | C |
| 29 | Fitness/running | Flutter + SQLite + Drift | `tracking`, `activities`, `routes`, `goals` | D |
| 30 | Productivity | React + Vite + Dexie/IndexedDB | `tasks`, `calendar`, `projects`, `focus` | F |
| 31 | Budgeting | Flutter + SQLite + Drift | `transactions`, `budgets`, `categories`, `reports` | D |
| 32 | Government/civic | Django + PostgreSQL | `citizens`, `services`, `applications`, `cases` | C |
| 33 | Nonprofit | Astro + MDX + external donation provider | `campaigns`, `impact`, `volunteers`, `donations` | A |

**Notes:** Fitness and budgeting can remain local-only, with no accounts or cloud backend. GPS/background features demand platform testing. Healthcare and government products require enhanced privacy, audit, access, and legal review.

### Technical and specialized

| # | Category | Recommended minimal reliable stack | Main features | Structure |
|---|---|---|---|---|
| 34 | Logistics/fleet | Next.js + PostgreSQL + PostGIS | `vehicles`, `drivers`, `routes`, `deliveries` | B |
| 35 | Maps/navigation | Next.js + MapLibre + PostgreSQL/PostGIS | `map`, `places`, `routes`, `search` | B |
| 36 | Creative editor | React + Vite + Konva/Fabric + IndexedDB | `canvas`, `tools`, `layers`, `export` | F |
| 37 | Cybersecurity | Django + PostgreSQL for modest monitoring console | `assets`, `events`, `alerts`, `incidents` | C |
| 38 | AI application | Next.js + PostgreSQL; FastAPI only if Python inference demands it | `models`, `conversations`, `jobs`, `results` | B |
| 39 | Automotive | Next.js + PostgreSQL | `vehicles`, `maintenance`, `bookings`, `history` | B |
| 40 | Desktop utility | Tauri + React + Vite + SQLite | `features`, `native`, `storage`, `settings` | G |

**Notes (AI applications):** Keep model API keys server-side. Stream long responses. Set per-user rate and cost limits. Treat model output as untrusted (escape/sanitize before rendering, never execute or interpolate into SQL/shell). Defend against prompt injection from retrieved documents. Keep a small evaluation set to catch regressions when prompts or models change.

**Notes:** Maps require actual map tiles/data and often routing/geocoding providers. Security platforms may need ingestion/streaming components beyond a small Django console. Native desktop app locking might require OS-level permissions and platform-specific native code; a Tauri frontend alone cannot universally block arbitrary applications.
