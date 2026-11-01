# SDP Exam Agent: Coder Agents playbook

Instructions and on-demand skills for an AI coding agent running in [Coder Agents](https://coder.com/docs/ai-coder/agents). The agent plans, designs, builds, tests and ships web, mobile, desktop and game projects.

```text
AGENTS.md                  # Core playbook. Coder puts it in the agent's system prompt (must stay under 64 KiB)
.agents/skills/
├── product-categories/    # 40 category design briefs, palettes + contrast audit, stacks, risks
├── project-scaffolds/     # Repo layouts A–H, non-interactive scaffold commands, test/lint tooling
└── planning-kit/          # Specs, beta/release plans, ops, cost, legal, docs templates
install.sh                 # Installs everything into ~/.coder/ (dotfiles mode)
scripts/validate.py        # Checks size limits and skill frontmatter before you commit
```

## Use it in Coder: pick one

**A. In one project.** Keep `AGENTS.md` and `.agents/` at the top level of the project's repository, and make that repository the workspace's working directory. Coder reads `AGENTS.md` only at the top level of the working directory, not in subfolders, and loads skills from `.agents/skills/`. To use the playbook in another project, copy both into that repo's root.

**B. In every workspace (dotfiles).** Use this repository as your Coder dotfiles repo, either through the template's dotfiles prompt or by running:

```bash
coder dotfiles https://github.com/Blessing-Kgatla/SDP-Exam-agent
```

Coder runs `install.sh`, which copies `AGENTS.md` to `~/.coder/AGENTS.md` and the skills to `~/.coder/skills/`. Then every project gets the playbook, with nothing added to its repo.

Use A or B for a given workspace, not both. With both, Coder loads two copies of the playbook.

**Check it loaded:** start a new chat and open its context list. `AGENTS.md` should be included (not "oversize"), and the three skills should show as valid.

## Model setup (Coder admins)

Configure **Admin settings → AI → Models** as described in `AGENTS.md` §3. The default is `claude-sonnet-5-5` at `medium` effort, with Claude Haiku 5.5 for explore sub-agents and titles. Leave **Thinking Budget Tokens** and the sampling fields (Temperature, Top P, Top K) empty, because current Claude models reject them.

## Editing

- Put detailed or rarely needed material in a skill's reference files, not in `AGENTS.md`. Every byte of `AGENTS.md` is sent on every turn, and Coder drops the whole file at 64 KiB.
- A skill's `name` in `SKILL.md` must be kebab-case and match its folder name, or Coder marks the skill invalid.
- Run the check before committing:

```bash
python3 scripts/validate.py
```
