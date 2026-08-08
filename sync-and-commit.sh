#!/usr/bin/env bash
#
# sync-and-commit.sh — save an approved workflow change.
#
# Run this ONCE after Rishwanth has approved a change and the CHANGELOG.md
# entry has been written. It:
#
#   1. copies the four job-application skills out of the Claude app folder
#      into this repo (the app folder is where they actually run from, but
#      it cannot hold a git repo — the app's sync deletes .git),
#   2. commits everything as one atomic commit, using the newest CHANGELOG.md
#      entry verbatim as the commit message,
#   3. pushes to the private GitHub repo.
#
# It refuses to run if nothing changed, so it is safe to run twice.
#
# Usage:  ./sync-and-commit.sh            commit and push
#         ./sync-and-commit.sh --dry-run  show what would happen, change nothing
#
set -euo pipefail

APP_SKILLS="/Users/rishwanth/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/c9caca1d-5ea4-44d0-adcf-b708df692cb0/e23955f7-0f0c-4e56-9dfe-31648e7c557d/skills"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHANGELOG="$REPO/cv-tailoring/references/CHANGELOG.md"
SKILLS=(cv-tailoring cover-letter jd-recruiter-brief application-qa)

DRY_RUN=0
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=1

# --- 1. sanity ------------------------------------------------------------
if [[ ! -d "$APP_SKILLS" ]]; then
  echo "ERROR: Claude app skills folder not found at:" >&2
  echo "  $APP_SKILLS" >&2
  echo "The app may have moved it. Find the new path with:" >&2
  echo "  find ~/Library/Application\\ Support/Claude -name 'facts.yaml'" >&2
  echo "then update APP_SKILLS at the top of this script." >&2
  exit 1
fi

# --- 2. copy the four skills across ---------------------------------------
# --delete so that a file deleted in the app folder is deleted here too,
# otherwise the repo would silently keep resurrected copies of removed files.
for s in "${SKILLS[@]}"; do
  if [[ ! -d "$APP_SKILLS/$s" ]]; then
    echo "WARNING: skill '$s' missing from app folder, skipping." >&2
    continue
  fi
  rsync -a --delete \
    --exclude='.DS_Store' --exclude='__pycache__' --exclude='*.pyc' \
    "$APP_SKILLS/$s/" "$REPO/$s/"
done

cd "$REPO"

# --- 3. anything to commit? -----------------------------------------------
if [[ -z "$(git status --porcelain)" ]]; then
  echo "No changes since the last commit. Nothing to do."
  exit 0
fi

echo "Changed files:"
git status --short
echo

# --- 4. pull the newest CHANGELOG entry to use as the commit message ------
# Entries are appended in chronological order and start with '## YYYY-MM-DD'.
# The newest is therefore the LAST dated section, stopping before the
# '## Template for future entries' block at the end of the file.
MSG_FILE="$(mktemp)"
trap 'rm -f "$MSG_FILE"' EXIT

python3 - "$CHANGELOG" > "$MSG_FILE" <<'PY'
import re, sys, pathlib

text = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
# split on level-2 headings, keeping the heading with its body
parts = re.split(r"^(## .*)$", text, flags=re.M)
entries = []
for i in range(1, len(parts), 2):
    heading, body = parts[i].strip(), parts[i + 1]
    if re.match(r"^## \d{4}-\d{2}-\d{2}", heading):
        entries.append((heading, body.rstrip()))

if not entries:
    sys.stderr.write("ERROR: no dated '## YYYY-MM-DD' entry found in CHANGELOG.md.\n")
    sys.exit(1)

heading, body = entries[-1]
subject = heading[3:].strip()          # drop the leading '## '
print(subject)
print()
print(heading)
print(body.strip())
PY

echo "Commit message will be:"
echo "---------------------------------------------"
head -1 "$MSG_FILE"
echo "  ... (full CHANGELOG entry, $(wc -l < "$MSG_FILE" | tr -d ' ') lines)"
echo "---------------------------------------------"
echo

if [[ $DRY_RUN -eq 1 ]]; then
  echo "Dry run — nothing committed or pushed."
  exit 0
fi

# --- 5. one atomic commit -------------------------------------------------
git add -A
git commit -q -F "$MSG_FILE"
echo "Committed: $(git log --oneline -1)"

# --- 6. push --------------------------------------------------------------
if git remote get-url origin >/dev/null 2>&1; then
  git push -q origin main
  echo "Pushed to $(git remote get-url origin)"
else
  echo "No 'origin' remote set — commit is local only."
fi
