# Building blocks and tooling defaults

## Preferred building blocks

| Technology | Preferred role | Why |
|---|---|---|
| **React + Vite** | Interactive client-only web app | Lightweight and flexible |
| **Next.js** | Integrated full-stack React web app | Routing, rendering, server actions/routes in one project |
| **Astro** | Content-rich public website | Static/content-first output; minimal default JavaScript |
| **Astro Starlight** | Documentation website | Documentation navigation, layouts, search, content tooling |
| **Django + HTMX** | Back-office, enterprise, record-heavy operations | Auth, forms, ORM, admin, templates and partial updates |
| **Flutter** | Cross-platform native-feeling/offline-first apps | Single codebase, strong device support |
| **Expo + React Native** | Mobile apps with online user accounts | React/TypeScript development and native modules |
| **Tauri** | Cross-platform desktop utilities | Web UI with native Rust host; local OS integrations |
| **Godot** | 2D/3D games | Scenes, input, physics, rendering, animation |
| **SQLite** | Device-local/single-server data | No separate DB service, transactional embedded SQL |
| **PostgreSQL** | Shared online relational data | Robust constraints, concurrent access, transactions |
| **Drizzle ORM** | TypeScript SQL access | Typed schema and migrations |
| **Drift** | Flutter structured SQLite | Type-safe Flutter SQLite queries/migrations |
| **Dexie + IndexedDB** | Local browser app | Convenient browser persistence |
| **Tailwind CSS** | Optional web styling layer | Efficient token-based utility styling |
| **TypeScript** | Web/native JS application logic | Types across data/UI boundaries |
| **Zod** | TypeScript runtime validation | Parse/validate untrusted input |
| **HTMX** | Lightweight Django interactivity | Partial HTML updates without entire SPA |

## Tooling defaults (use the project's existing tools first)

Detect what the repository already uses before adding anything: lockfile → package manager (`package-lock.json` npm, `pnpm-lock.yaml` pnpm, `yarn.lock` yarn, `bun.lock` bun), `pyproject.toml`/`uv.lock`, `pubspec.yaml`, `Cargo.toml`. Never switch package managers or add a second linter/formatter.

| Stack | Unit / integration | End-to-end / UI | Lint / format / types |
|---|---|---|---|
| Next.js, Astro, React + Vite | Vitest (+ Testing Library for components) | Playwright; `@axe-core/playwright` for automated a11y checks | ESLint or Biome (whichever the scaffold chose); `tsc --noEmit` |
| Django + HTMX | pytest + pytest-django | Playwright (Python or Node) | Ruff (lint + format); mypy/pyright optional |
| Expo / React Native | Jest (jest-expo) + React Native Testing Library | Maestro or Detox when device E2E is in scope | ESLint; `tsc --noEmit` |
| Flutter | `flutter test` | `integration_test` package | `flutter analyze`, `dart format` |
| Tauri | Vitest (frontend), `cargo test` (Rust) | WebDriver-based E2E only if justified | `cargo clippy`, `cargo fmt`, frontend linters |
| Godot | GUT or gdUnit4 (headless) | Manual play-test checklist on target hardware | gdtoolkit (`gdlint`, `gdformat`) if adopted |

Automated accessibility scans (axe) catch only part of WCAG. Also check keyboard order, focus visibility, labels and zoom/reflow by hand or with Playwright scripts.

## Version currency

Framework APIs change between majors, and model training data lags. Before scaffolding or writing framework-specific code, check the installed or latest version (`npm view <pkg> version`, `pip index versions <pkg>`, `flutter --version`). Read that version's docs or the project's lockfile, and follow the current conventions. Examples: Next.js 16 renamed `middleware.ts` to `proxy.ts`; Tailwind v4 is configured in CSS rather than `tailwind.config.js`; Astro 5 uses `src/content.config.ts`. Never invent package names. Verify a package exists, is maintained and has an acceptable licence before installing it.
