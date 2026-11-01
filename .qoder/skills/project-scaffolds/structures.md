# Reusable file structures A–H

**Use the smallest appropriate structure**. These are starting blueprints, not requirements to create empty folders. The feature names are examples; substitute those from `product-categories/stacks.md`. Preserve established repository conventions when extending existing code.

### Structure A — Astro static/content-first website

**For:** Corporate, portfolio, news, nonprofit, public university, documentation, restaurant menu.

```text
my-website/
├── public/
│   ├── images/
│   ├── fonts/
│   └── favicon.svg
├── src/
│   ├── assets/
│   ├── components/
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   └── Navigation.astro
│   ├── layouts/
│   │   └── BaseLayout.astro
│   ├── pages/
│   │   ├── index.astro
│   │   ├── about.astro
│   │   ├── contact.astro
│   │   └── services/index.astro
│   ├── content/
│   │   └── articles/
│   ├── styles/
│   │   ├── global.css
│   │   └── tokens.css
│   └── content.config.ts
├── astro.config.mjs
├── package.json
└── tsconfig.json
```

For Starlight documentation, use its established `src/content/docs/` structure. Avoid installing backend/database/auth libraries for sites that only publish content.

```bash
# Non-interactive. Verify flags with --help first; add --no-ai if the repo already has an AGENTS.md
npm create astro@latest my-website -- --template minimal --install --no-git --skip-houston --yes
```

### Structure B — Next.js integrated full-stack web app

**For:** E-commerce, booking, SaaS, LMS, recruitment, marketplaces and multi-user apps.

```text
my-web-app/
├── public/
│   ├── images/
│   └── icons/
├── src/
│   ├── app/
│   │   ├── (marketing)/
│   │   │   └── page.tsx
│   │   ├── (auth)/
│   │   │   ├── login/page.tsx
│   │   │   └── register/page.tsx
│   │   ├── (app)/
│   │   │   ├── dashboard/page.tsx
│   │   │   └── settings/page.tsx
│   │   ├── api/
│   │   │   └── webhooks/payments/route.ts
│   │   ├── layout.tsx
│   │   └── globals.css
│   ├── features/
│   │   ├── products/
│   │   │   ├── components/
│   │   │   ├── actions.ts
│   │   │   ├── queries.ts
│   │   │   ├── schema.ts
│   │   │   └── types.ts
│   │   ├── cart/
│   │   ├── checkout/
│   │   └── orders/
│   ├── components/
│   │   ├── ui/
│   │   └── layout/
│   ├── db/
│   │   ├── index.ts
│   │   └── schema.ts
│   ├── lib/
│   │   ├── auth.ts
│   │   ├── payments.ts
│   │   └── validations.ts
│   └── styles/
│       └── tokens.css
├── drizzle/
├── tests/
├── .env.example
├── drizzle.config.ts
├── next.config.ts
├── package.json
└── tsconfig.json
```

- `app/`: Routes, layouts, page/route entry points.
- `features/`: Domain-specific UI/business logic.
- `components/`: Truly reusable presentation components.
- `db/`: Database connection/schema; `drizzle/`: migrations.
- `lib/`: Shared integrations and cross-cutting utilities.
- `tests/`: Relevant automated tests.
- Keep privileged business logic and database access on the server. Use framework-appropriate server actions for app mutations and route handlers for external webhooks/APIs. Validate on the server.
- **Every Server Action and Route Handler is a public HTTP endpoint.** Authenticate and authorize inside each one, re-checking record ownership. Never rely only on page-level checks, hidden UI or middleware/proxy (`middleware.ts`, renamed `proxy.ts` in Next.js 16).

```bash
# Non-interactive (create-next-app 16.x flags; verify with --help). Tailwind is ON by default in current versions.
npx create-next-app@latest my-web-app --ts --app --src-dir --eslint --import-alias "@/*" --use-npm --disable-git --yes
cd my-web-app
```

Current create-next-app also writes an `AGENTS.md` into the new project by default (`--agents-md`). Merge its framework rules into the repository's root `AGENTS.md` and delete the generated copy. Keep a single `AGENTS.md`, at the root of the folder opened in Qoder.

### Structure C — Django + HTMX administration/enterprise app

```text
my-enterprise-app/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── apps/
│   ├── accounts/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── services.py
│   │   └── migrations/
│   ├── inventory/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── admin.py
│   │   └── migrations/
│   ├── operations/
│   └── reports/
├── templates/
│   ├── base.html
│   ├── dashboard/
│   └── partials/
├── static/
│   ├── css/tokens.css
│   ├── js/
│   └── images/
├── tests/
├── manage.py
├── pyproject.toml
└── .env.example
```

Start with Django's auth, ORM, forms, migrations, admin and templates. HTMX can add partial-page interactions without a React frontend. Do not expose Django admin as the entire customer-facing product unless that internal-use UX is explicitly suitable.

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install django django-htmx            # pin versions in pyproject.toml / requirements
django-admin startproject config .        # creates config/ and manage.py as shown above
mkdir -p apps/accounts && python manage.py startapp accounts apps/accounts
# then set name = "apps.accounts" in apps/accounts/apps.py and add it to INSTALLED_APPS
```

Vendor a pinned `htmx.min.js` into `static/js/` (or use a pinned CDN URL with SRI); don't load an unpinned "latest". Use `pytest` + `pytest-django` for tests and `ruff` for lint/format.

### Structure D — Flutter offline-first mobile app

```text
my-mobile-app/
├── android/
├── ios/
├── lib/
│   ├── main.dart
│   ├── app/
│   │   ├── app.dart
│   │   ├── router.dart
│   │   └── theme.dart
│   ├── core/
│   │   ├── database/
│   │   │   ├── app_database.dart
│   │   │   └── tables.dart
│   │   ├── services/
│   │   ├── utils/
│   │   └── widgets/
│   └── features/
│       ├── tracking/
│       │   ├── data/
│       │   ├── domain/
│       │   └── presentation/
│       ├── activities/
│       ├── routes/
│       ├── goals/
│       └── settings/
├── assets/
│   ├── icons/
│   └── images/
├── test/
├── integration_test/
└── pubspec.yaml
```

Use Drift/SQLite for local structured persistence, native plugins only as needed, and simple state management initially. Riverpod can help if shared asynchronous state becomes complex. `data/` owns persistence; `domain/` business rules; `presentation/` UI/screens. For a tiny app, a simpler feature-local `models`, `screens`, `services` layout is acceptable. Background GPS and sensors require actual OS/device testing.

```bash
flutter create my_mobile_app
cd my_mobile_app
flutter pub add drift drift_flutter dev:drift_dev dev:build_runner
dart run build_runner build --delete-conflicting-outputs   # regenerate after every table change
```

*Important:* Open the database with `drift_flutter`'s `driftDatabase(...)` helper (or the documented executor for each target platform). Installing packages alone does not complete DB initialization. Add schema versioning and `MigrationStrategy` before the first release. iOS builds and signing need macOS/Xcode. On Windows or Linux you can run `flutter analyze`, `flutter test` and Android/web builds only, so say that instead of claiming iOS verification.

### Structure E — Expo / React Native social-mobile app

```text
my-social-app/
├── app/
│   ├── _layout.tsx
│   ├── (auth)/
│   │   ├── login.tsx
│   │   └── register.tsx
│   ├── (tabs)/
│   │   ├── _layout.tsx
│   │   ├── index.tsx
│   │   ├── discover.tsx
│   │   ├── messages.tsx
│   │   └── profile.tsx
│   └── post/[id].tsx
├── src/
│   ├── features/
│   │   ├── feed/
│   │   ├── profiles/
│   │   ├── messages/
│   │   └── notifications/
│   ├── components/
│   ├── hooks/
│   ├── lib/
│   │   ├── api.ts
│   │   └── auth.ts
│   └── styles/tokens.ts
├── assets/
├── tests/
├── app.json
└── package.json
```

Expo Router provides file-based navigation. Managed backend services (e.g., Supabase) can provide PostgreSQL, auth, storage, and optional realtime; enforce authorization in database policies/server code, not just client views. With Supabase: enable Row Level Security on every exposed table with explicit policies, never ship the `service_role` key to the app, and keep privileged work in Edge Functions or a server.

```bash
# --yes = default template (Expo Router). Current versions also write AGENTS.md/.claude files; add --no-agents-md if the repo already has one.
npx create-expo-app@latest my-social-app --yes
```

Native iOS builds need macOS or a cloud build service (for example EAS Build, which needs the owner's account). On Windows or Linux, verify with type-checks, unit tests and the web/Android targets, and report iOS as unverified.

### Structure F — React + Vite local-first browser app

```text
my-local-web-app/
├── public/
├── src/
│   ├── main.tsx
│   ├── App.tsx
│   ├── features/
│   │   ├── tasks/
│   │   │   ├── components/
│   │   │   ├── hooks/
│   │   │   ├── repository.ts
│   │   │   └── types.ts
│   │   ├── calendar/
│   │   ├── projects/
│   │   └── settings/
│   ├── components/
│   │   ├── ui/
│   │   └── layout/
│   ├── storage/
│   │   ├── db.ts
│   │   ├── migrations.ts
│   │   └── backup.ts
│   ├── hooks/
│   ├── lib/
│   └── styles/
│       ├── global.css
│       └── tokens.css
├── tests/
├── index.html
├── package.json
├── tsconfig.json
└── vite.config.ts
```

For a creative editor, swap `tasks/calendar/projects` for `canvas/layers/tools/export`. Dexie wraps IndexedDB. Plan import/export because browser-only data can be lost by clearing the browser, profile migration, or storage eviction depending on browser/storage conditions.

```bash
# --no-interactive stops create-vite from prompting; --no-immediate stops it from starting a dev server
npm create vite@latest my-local-web-app -- --template react-ts --no-interactive --no-immediate
cd my-local-web-app
npm install
npm install dexie dexie-react-hooks
```

### Structure G — Tauri 2 desktop utility

```text
my-desktop-app/
├── src/
│   ├── main.tsx
│   ├── App.tsx
│   ├── features/
│   │   ├── dashboard/
│   │   ├── applications/
│   │   ├── protection/
│   │   └── settings/
│   ├── components/
│   ├── native/commands.ts
│   ├── storage/database.ts
│   └── styles/tokens.css
├── src-tauri/
│   ├── src/
│   │   ├── lib.rs
│   │   ├── main.rs
│   │   └── commands.rs
│   ├── capabilities/default.json
│   ├── icons/
│   ├── Cargo.toml
│   └── tauri.conf.json
├── public/
├── index.html
├── package.json
└── vite.config.ts
```

Frontend handles interface and state; native Rust host handles OS-level actions that are supported and authorized. SQLite can be accessed via suitable Tauri plugin/native integration. Tauri cannot universally block arbitrary apps without platform-specific functionality/permissions.

```bash
npm create tauri-app@latest my-desktop-app -- --template react-ts --manager npm --identifier com.example.mydesktopapp --yes
```

Building needs Rust plus the OS's WebView/system libraries. Windows `.msi`/`.exe` and macOS `.app`/`.dmg` bundles, code signing and notarization must be built on (or cross-built for) those OSes. Verify the build for the OS you are on plus the frontend, and report the other platforms as unverified. Grant the minimum Tauri capabilities/permissions in `src-tauri/capabilities/`.

### Structure H — Godot game

```text
my-game/
├── scenes/
│   ├── main.tscn
│   ├── menus/
│   │   ├── main_menu.tscn
│   │   └── settings.tscn
│   ├── levels/
│   ├── characters/
│   └── ui/
├── scripts/
│   ├── game/
│   ├── characters/
│   ├── systems/
│   └── ui/
├── assets/
│   ├── textures/
│   ├── models/
│   ├── animations/
│   ├── sounds/
│   └── fonts/
├── resources/
│   ├── items/
│   └── levels/
├── save/
├── tests/
└── project.godot
```

Use Godot's native save/config resource/file APIs for simple game state. Add SQLite only if complex searchable records justify it. Keep rendering, game logic, data and UI separate. Test game performance and input on the actual target device. Godot has no built-in test runner: use GUT or gdUnit4 for `tests/`, and run them headless (`godot --headless ...`). Exports need the matching export templates installed. Godot is often not installed or not on `PATH`, so check `godot --version` before promising builds.

### Shared web styling layout

```text
src/styles/
├── tokens.css
├── typography.css
├── global.css
└── animations.css
```

This lets the agent revise branding without rewriting business logic. Do not introduce more design-system files if they would be empty or duplicative.
