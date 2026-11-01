#!/usr/bin/env python3
"""Check that AGENTS.md and the skills will load in Coder Agents.

Coder silently excludes instruction files over 64 KiB and reports skills with
bad frontmatter as invalid, so run this after every edit:

    python3 scripts/validate.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AGENTS_LIMIT = 64 * 1024        # instruction files: 64 KiB, oversize ones load with no content
SKILL_LIMIT = 64_000            # SKILL.md: "64 KB" (lower reading used to be safe)
SUPPORT_LIMIT = 512_000         # supporting files: "512 KB", larger ones are truncated
TOTAL_LIMIT = 2 * 1024 * 1024   # all loaded files per snapshot: 2 MiB
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

errors, notes = [], []


def size(path):
    return path.stat().st_size


agents = ROOT / "AGENTS.md"
if not agents.is_file():
    errors.append("AGENTS.md is missing from the repository root")
else:
    n = size(agents)
    if n >= AGENTS_LIMIT:
        errors.append(f"AGENTS.md is {n:,} bytes; Coder ignores instruction files of 64 KiB ({AGENTS_LIMIT:,}) or more")
    else:
        notes.append(f"AGENTS.md {n:,} bytes ({AGENTS_LIMIT - n:,} bytes of headroom)")

skills_dir = ROOT / ".agents" / "skills"
skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.is_dir() else []
if not skill_dirs:
    errors.append(".agents/skills/ has no skill directories")

total = size(agents) if agents.is_file() else 0
for d in skill_dirs:
    before = len(errors)
    skill_md = d / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"{d.name}: SKILL.md is missing")
        continue
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{d.name}: SKILL.md must start with YAML frontmatter between --- lines")
        continue
    fields = dict(
        (k.strip(), v.strip()) for k, v in
        (line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)
    )
    name = fields.get("name", "")
    if not NAME_RE.match(name):
        errors.append(f"{d.name}: name {name!r} must be kebab-case")
    if name != d.name:
        errors.append(f"{d.name}: name {name!r} must match the directory name exactly")
    if not fields.get("description"):
        notes.append(f"{d.name}: no description (allowed, but the agent picks skills by description)")
    if size(skill_md) > SKILL_LIMIT:
        errors.append(f"{d.name}: SKILL.md is {size(skill_md):,} bytes; limit is 64 KB")
    # Files the skill's index tables point to (prose mentions of other files are ignored)
    table_text = "\n".join(line for line in text.splitlines() if line.lstrip().startswith("|"))
    for ref in sorted(set(re.findall(r"`([\w.-]+\.md)`", table_text)) - {"AGENTS.md", "SKILL.md"}):
        if not (d / ref).is_file():
            errors.append(f"{d.name}: SKILL.md references {ref}, which does not exist")
    for f in d.rglob("*"):
        if f.is_file():
            total += size(f)
            if f.name != "SKILL.md" and size(f) > SUPPORT_LIMIT:
                errors.append(f"{d.name}: {f.name} is {size(f):,} bytes; files over 512 KB are truncated")
    if len(errors) == before:
        notes.append(f"skill {d.name}: ok")

if total > TOTAL_LIMIT:
    errors.append(f"AGENTS.md plus skills total {total:,} bytes; Coder loads at most 2 MiB per snapshot")

for line in notes:
    print("  " + line)
if errors:
    print("\nFAILED:")
    for line in errors:
        print("  - " + line)
    sys.exit(1)
print(f"\nOK: AGENTS.md and {len(skill_dirs)} skills will load in Coder Agents ({total:,} bytes total)")
