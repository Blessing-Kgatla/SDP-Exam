#!/usr/bin/env python3
"""Check that AGENTS.md and the skills will load correctly in Qoder IDE.

Qoder truncates active rules beyond 100,000 characters, and a skill needs a
valid name and description in its SKILL.md frontmatter. Run after every edit:

    python scripts/validate.py        (Windows)
    python3 scripts/validate.py       (macOS/Linux)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES_CHAR_LIMIT = 100_000      # all active rule files together; excess is truncated
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NAME_MAX, DESC_MAX = 64, 1024

errors, notes = [], []


def chars(path):
    return len(path.read_text(encoding="utf-8"))


# --- AGENTS.md + .qoder/rules: stay under Qoder's rules budget (counted together, to be safe)
agents = ROOT / "AGENTS.md"
if not agents.is_file():
    errors.append("AGENTS.md is missing from the repository root")
    rule_chars = 0
else:
    rule_chars = chars(agents)
    notes.append(f"AGENTS.md {rule_chars:,} characters")
rules = sorted((ROOT / ".qoder" / "rules").rglob("*.md")) if (ROOT / ".qoder" / "rules").is_dir() else []
for r in rules:
    rule_chars += chars(r)
if rules:
    notes.append(f"{len(rules)} file(s) in .qoder/rules")
if rule_chars > RULES_CHAR_LIMIT:
    errors.append(f"AGENTS.md + .qoder/rules total {rule_chars:,} characters; Qoder truncates rules beyond {RULES_CHAR_LIMIT:,}")
else:
    notes.append(f"instructions total {rule_chars:,} of {RULES_CHAR_LIMIT:,} characters")

# --- skills
skills_dir = ROOT / ".qoder" / "skills"
skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.is_dir() else []
if not skill_dirs:
    errors.append(".qoder/skills/ has no skill folders")

for d in skill_dirs:
    before = len(errors)
    skill_md = d / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"{d.name}: SKILL.md is missing")
        continue
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        errors.append(f"{d.name}: SKILL.md must start with YAML frontmatter between --- lines")
        continue
    fields = dict(
        (k.strip(), v.strip()) for k, v in
        (line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)
    )
    name, desc = fields.get("name", ""), fields.get("description", "")
    if not NAME_RE.match(name) or len(name) > NAME_MAX:
        errors.append(f"{d.name}: name {name!r} must be lowercase letters, numbers and hyphens, max {NAME_MAX} chars")
    if name != d.name:
        errors.append(f"{d.name}: name {name!r} should match the folder name exactly")
    if not desc:
        errors.append(f"{d.name}: description is required (the model picks skills by it)")
    elif len(desc) > DESC_MAX:
        errors.append(f"{d.name}: description is {len(desc)} chars; max {DESC_MAX}")
    # Files the skill's index tables point to (prose mentions of other files are ignored)
    table_text = "\n".join(line for line in text.splitlines() if line.lstrip().startswith("|"))
    for ref in sorted(set(re.findall(r"`([\w.-]+\.md)`", table_text)) - {"AGENTS.md", "SKILL.md"}):
        if not (d / ref).is_file():
            errors.append(f"{d.name}: SKILL.md references {ref}, which does not exist")
    if len(errors) == before:
        notes.append(f"skill {d.name}: ok")

for line in notes:
    print("  " + line)
if errors:
    print("\nFAILED:")
    for line in errors:
        print("  - " + line)
    sys.exit(1)
print(f"\nOK: AGENTS.md and {len(skill_dirs)} skills are ready for Qoder")
