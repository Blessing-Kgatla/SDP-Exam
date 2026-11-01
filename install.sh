#!/usr/bin/env sh
# Install this playbook for Coder Agents in every workspace.
#
# Copies AGENTS.md to ~/.coder/AGENTS.md and each skill in .agents/skills/
# to ~/.coder/skills/<name>/, where Coder Agents loads them for any project.
# Coder runs this automatically when this repo is your dotfiles repo
# (`coder dotfiles <repo-url>` or the template's dotfiles prompt).
#
# Safe to re-run: an existing, different ~/.coder/AGENTS.md is backed up to
# AGENTS.md.bak, and only the skills shipped here are replaced.
set -eu

SRC_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
DEST="${CODER_AGENTS_HOME:-$HOME/.coder}"

mkdir -p "$DEST/skills"

if [ -f "$DEST/AGENTS.md" ] && ! cmp -s "$SRC_DIR/AGENTS.md" "$DEST/AGENTS.md"; then
  cp "$DEST/AGENTS.md" "$DEST/AGENTS.md.bak"
  echo "Backed up existing $DEST/AGENTS.md to $DEST/AGENTS.md.bak"
fi
cp "$SRC_DIR/AGENTS.md" "$DEST/AGENTS.md"

count=0
for skill in "$SRC_DIR"/.agents/skills/*/; do
  [ -f "${skill}SKILL.md" ] || continue
  name=$(basename "$skill")
  rm -rf "${DEST:?}/skills/$name"
  cp -R "$skill" "$DEST/skills/$name"
  count=$((count + 1))
done

echo "Installed AGENTS.md and $count skills into $DEST"
