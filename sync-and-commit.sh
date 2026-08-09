#!/usr/bin/env bash
#
# sync-and-commit.sh — save an approved workflow change into git.
#
# THE IMPORTANT THING TO UNDERSTAND:
# The skills run from Claude's SERVER copy, edited from inside a Claude Desktop
# chat. The folder at ~/Library/Application Support/Claude/.../skills/ is a
# download-only cache — editing it changes nothing the skill can see (verified
# 2026-08-09). So the authoritative source for this repo is a fresh export of
# the .skill files from Claude Desktop.
#
# SOURCES, in order of preference:
#   1. ~/Downloads/*.skill        — exported from Claude Desktop (authoritative)
#   2. the local cache folder     — fallback; only trustworthy if the cache has
#                                   refreshed from the server since the change
#
# USAGE
#   ./sync-and-commit.sh              use best available source, commit, push
#   ./sync-and-commit.sh --dry-run    show what would change, commit nothing
#   ./sync-and-commit.sh --cache      force the local cache as source
#
set -euo pipefail

CACHE="/Users/rishwanth/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/c9caca1d-5ea4-44d0-adcf-b708df692cb0/e23955f7-0f0c-4e56-9dfe-31648e7c557d/skills"
DOWNLOADS="$HOME/Downloads"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHANGELOG="$REPO/cv-tailoring/references/CHANGELOG.md"
SKILLS=(cv-tailoring cover-letter jd-recruiter-brief application-qa)

DRY_RUN=0; FORCE_CACHE=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    --cache)   FORCE_CACHE=1 ;;
    *) echo "Unknown option: $arg" >&2; exit 2 ;;
  esac
done

STAGING="$(mktemp -d)"
trap 'rm -rf "$STAGING"' EXIT

# --- pick a source --------------------------------------------------------
EXPORTS_FOUND=0
for s in "${SKILLS[@]}"; do
  [[ -f "$DOWNLOADS/$s.skill" ]] && EXPORTS_FOUND=$((EXPORTS_FOUND + 1))
done

if [[ $FORCE_CACHE -eq 0 && $EXPORTS_FOUND -eq ${#SKILLS[@]} ]]; then
  SOURCE_DESC="Claude Desktop exports in ~/Downloads (authoritative)"
  for s in "${SKILLS[@]}"; do
    tmp="$STAGING/.unzip-$s"; mkdir -p "$tmp"
    unzip -qo "$DOWNLOADS/$s.skill" -d "$tmp"
    # archives contain a single top-level folder named after the skill
    if [[ -d "$tmp/$s" ]]; then cp -R "$tmp/$s" "$STAGING/$s"
    else cp -R "$tmp" "$STAGING/$s"; fi
    rm -rf "$tmp"
  done
else
  if [[ $FORCE_CACHE -eq 0 && $EXPORTS_FOUND -gt 0 ]]; then
    echo "WARNING: found only $EXPORTS_FOUND of ${#SKILLS[@]} .skill exports in ~/Downloads." >&2
    echo "Export all four from Claude Desktop, or re-run with --cache." >&2
    exit 1
  fi
  SOURCE_DESC="local cache folder (NOT authoritative — may lag the server)"
  [[ -d "$CACHE" ]] || { echo "ERROR: cache folder not found at $CACHE" >&2; exit 1; }
  for s in "${SKILLS[@]}"; do
    [[ -d "$CACHE/$s" ]] || { echo "WARNING: '$s' missing from cache, skipping." >&2; continue; }
    cp -R "$CACHE/$s" "$STAGING/$s"
  done
fi

echo "Source: $SOURCE_DESC"
echo

# --- copy into the repo ---------------------------------------------------
for s in "${SKILLS[@]}"; do
  [[ -d "$STAGING/$s" ]] || continue
  rsync -a --delete \
    --exclude='.DS_Store' --exclude='__pycache__' --exclude='*.pyc' \
    "$STAGING/$s/" "$REPO/$s/"
done

cd "$REPO"

if [[ -z "$(git status --porcelain)" ]]; then
  echo "No changes since the last commit. Nothing to do."
  exit 0
fi

echo "Changed files:"
git status --short
echo

# --- build the commit message from the newest CHANGELOG entry -------------
MSG_FILE="$STAGING/commit-msg.txt"
python3 - "$CHANGELOG" > "$MSG_FILE" <<'PY'
import re, sys, pathlib
text = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
parts = re.split(r"^(## .*)$", text, flags=re.M)
entries = [(parts[i].strip(), parts[i+1].rstrip())
           for i in range(1, len(parts), 2)
           if re.match(r"^## \d{4}-\d{2}-\d{2}", parts[i].strip())]
if not entries:
    sys.stderr.write("ERROR: no dated '## YYYY-MM-DD' entry in CHANGELOG.md\n")
    sys.exit(1)
heading, body = entries[-1]
print(heading[3:].strip()); print(); print(heading); print(body.strip())
PY

echo "Commit message (from newest CHANGELOG entry):"
echo "---------------------------------------------"
head -1 "$MSG_FILE"
echo "  ... $(wc -l < "$MSG_FILE" | tr -d ' ') lines total"
echo "---------------------------------------------"
echo

if [[ $DRY_RUN -eq 1 ]]; then
  echo "Dry run — nothing committed or pushed."
  echo "Review the diff with:  git -C '$REPO' diff"
  exit 0
fi

# --- commit and push ------------------------------------------------------
git add -A
git commit -q -F "$MSG_FILE"
echo "Committed: $(git log --oneline -1)"

if git remote get-url origin >/dev/null 2>&1; then
  git push -q origin main && echo "Pushed to $(git remote get-url origin)"
else
  echo "No 'origin' remote — commit is local only."
fi
