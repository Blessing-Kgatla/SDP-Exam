---
name: project-scaffolds
description: Repository layouts A–H (Astro, Next.js, Django + HTMX, Flutter, Expo, React + Vite local-first, Tauri 2, Godot) with non-interactive scaffold commands, plus default test/lint/type-check tooling per stack and version-currency rules. Use it when creating a new project or app, adding a new top-level module, or choosing test and lint tools.
---

# Project scaffolds and tooling

| Need | Read |
|---|---|
| Folder layout and scaffold commands for structures A–H | `structures.md` |
| Building-block roles, test/lint/type tooling per stack, version checks | `building-blocks.md` |

## Rules when scaffolding

1. **Existing repository?** Extend its conventions. Do not re-scaffold, restructure or switch package manager, framework or linter without an explicit request.
2. **Check versions first** (`npm view <pkg> version`, `flutter --version`, etc.) and read that version's docs. The commands in `structures.md` were checked against create-next-app 16.x, create-vite 9.x, create-astro 5.x, create-expo-app 5.x and create-tauri-app 4.x. Run `<command> --help` if a flag is rejected.
3. **Never run an interactive scaffolder.** Pass `--yes` / `--no-interactive` / explicit template flags, and set `CI=1`. A prompt waiting for input will hang the agent's shell.
4. **Scaffold into a named subdirectory or an empty directory.** Never scaffold over existing files without confirming.
5. **Generated agent files:** current Next.js, Expo and Astro scaffolders write their own `AGENTS.md`/`CLAUDE.md`/`.claude/` files. Coder Agents reads instruction files only at the **top level** of the working directory. Merge any useful framework guidance into the root `AGENTS.md`, and keep the root file under 64 KiB.
6. Create only the folders the first vertical slice needs. Empty placeholder folders and files are noise.
7. After scaffolding, run the stack's install, type-check, lint, test and build commands once and record them in the README. Commit the clean scaffold separately from feature work.
