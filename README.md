# SDP-Exam: Qoder IDE agent playbook

Instructions and on-demand skills for the AI agent in [Qoder IDE](https://docs.qoder.com/). The agent plans, designs, builds, tests and ships web, mobile, desktop and game projects.

```text
AGENTS.md                  # Core playbook; Qoder reads it from the project root
.qoder/skills/
├── product-categories/    # 40 category design briefs, palettes + contrast audit, stacks, risks
├── project-scaffolds/     # Repo layouts A–H, non-interactive scaffold commands, test/lint tooling
└── planning-kit/          # Specs, beta/release plans, ops, cost, legal, docs templates
install.sh                 # Copies the playbook into another project (or your user-level skills)
scripts/validate.py        # Checks Qoder's limits and skill frontmatter before you commit
```

## Start a project in Qoder IDE

1. On Qoder's start screen, click **Clone repo** and paste `https://github.com/Blessing-Kgatla/SDP-Exam`. Choose a parent folder, and Qoder opens the cloned folder. (Already cloned? Use **Open project** or **File → Open Folder…** and pick the `SDP-Exam` folder itself, the one that contains `AGENTS.md`.)
2. Check the skills loaded: in the chat panel, type `/`. You should see `product-categories`, `project-scaffolds` and `planning-kit`. If not, restart Qoder.
3. Switch the chat to **Agent** mode, pick a model (see `AGENTS.md` §3), and paste your project brief. The agent builds the project inside this repo.

## Use the playbook in another project

From this folder, in Git Bash:

```bash
sh install.sh /c/Users/<you>/path/to/other-project
```

This copies `AGENTS.md` and `.qoder/skills/` into that project. To make the skills available in **every** project instead, run `sh install.sh --user`; it copies them to `~/.qoder/skills/`. Each project still needs its own `AGENTS.md`.

## Model choice

See `AGENTS.md` §3 for which Qoder tier or model to use for building, planning and quick tasks.

## Editing

- `AGENTS.md` goes into every request, so keep it lean. Put detailed or rarely needed material in a skill's reference files.
- Qoder truncates active rules (`AGENTS.md` plus anything in `.qoder/rules/`) beyond 100,000 characters.
- A skill's `name` must be lowercase letters, numbers and hyphens, and should match its folder name. Its `description` (max 1,024 characters) is how the agent decides when to use it.
- Run the check before committing:

```bash
python scripts/validate.py
```
