#!/usr/bin/env sh
# Copy this playbook into another project so Qoder IDE uses it there.
#
#   sh install.sh <path-to-project>   copies AGENTS.md and .qoder/skills/ into that project
#   sh install.sh --user              copies the skills to ~/.qoder/skills/ for all projects
#
# Works in Git Bash on Windows and in any POSIX shell. Safe to re-run: an
# existing, different AGENTS.md is backed up to AGENTS.md.bak, and only the
# skills shipped here are replaced.
set -eu

SRC_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

if [ $# -ne 1 ]; then
  echo "usage: sh install.sh <path-to-project> | --user" >&2
  exit 2
fi

copy_skills() {  # $1 = destination skills folder
  mkdir -p "$1"
  count=0
  for skill in "$SRC_DIR"/.qoder/skills/*/; do
    [ -f "${skill}SKILL.md" ] || continue
    name=$(basename "$skill")
    rm -rf "${1:?}/$name"
    cp -R "$skill" "$1/$name"
    count=$((count + 1))
  done
  echo "Copied $count skills into $1"
}

if [ "$1" = "--user" ]; then
  copy_skills "$HOME/.qoder/skills"
  echo "Restart Qoder IDE, then type / in chat to see the skills."
  exit 0
fi

DEST=$(CDPATH= cd -- "$1" && pwd)
if [ "$DEST" = "$SRC_DIR" ]; then
  echo "That is this repository already; nothing to copy." >&2
  exit 1
fi

if [ -f "$DEST/AGENTS.md" ] && ! cmp -s "$SRC_DIR/AGENTS.md" "$DEST/AGENTS.md"; then
  cp "$DEST/AGENTS.md" "$DEST/AGENTS.md.bak"
  echo "Backed up existing AGENTS.md to $DEST/AGENTS.md.bak"
fi
cp "$SRC_DIR/AGENTS.md" "$DEST/AGENTS.md"
copy_skills "$DEST/.qoder/skills"
echo "Done. Open $DEST in Qoder IDE (restart Qoder if it was already open)."
