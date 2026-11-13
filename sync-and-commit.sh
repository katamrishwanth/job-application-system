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
# SOURCES:
#   default            the local cache folder. Preferred for day-to-day use: no
#                      manual export step. Valid ONLY if the cache refreshes
#                      from the server after a change — being verified as of
#                      2026-08-09. Always check the diff before committing.
#   --exports          ~/Downloads/*.skill, exported from Claude Desktop.
#                      Guaranteed to match the server. Use if the cache turns
#                      out not to refresh, or to double-check it.
#
# USAGE
#   ./sync-and-commit.sh              read the cache, commit, push
#   ./sync-and-commit.sh --dry-run    show what would change, commit nothing
#   ./sync-and-commit.sh --exports    read ~/Downloads/*.skill instead
#
set -euo pipefail

CACHE="/Users/rishwanth/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/c9caca1d-5ea4-44d0-adcf-b708df692cb0/e23955f7-0f0c-4e56-9dfe-31648e7c557d/skills"
DOWNLOADS="$HOME/Downloads"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHANGELOG="$REPO/cv-tailoring/references/CHANGELOG.md"
SKILLS=(cv-tailoring cover-letter jd-recruiter-brief application-qa)

DRY_RUN=0; USE_EXPORTS=0; EXPLICIT_MSG=""
while (( $# )); do
  case "$1" in
    --dry-run) DRY_RUN=1 ;;
    --exports) USE_EXPORTS=1 ;;
    -m) shift; EXPLICIT_MSG="${1:-}"
        [[ -n "$EXPLICIT_MSG" ]] || { echo "-m needs a message" >&2; exit 2; } ;;
    *) echo "Unknown option: $1" >&2; exit 2 ;;
  esac
  shift
done

STAGING="$(mktemp -d)"
trap 'rm -rf "$STAGING"' EXIT

# --- refuse to clobber uncommitted repo edits ------------------------------
# The copy step below rsyncs the server copy over the repo with --delete (in
# --dry-run too). Any edit made directly in the repo, e.g. a CHANGELOG entry a
# chat could not save to the server, would be silently wiped. Seen 2026-11-13:
# the 2026-11-09 CHANGELOG entry existed only in the repo, so every sync
# deleted it again.
REPO_CHECK="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIRTY="$(git -C "$REPO_CHECK" status --porcelain -- "${SKILLS[@]}")"
if [[ -n "$DIRTY" ]]; then
  echo "ERROR: the repo has uncommitted edits inside the skill folders:" >&2
  echo "$DIRTY" >&2
  echo >&2
  echo "Syncing now would overwrite them with the server copy." >&2
  echo "  - If the server already has these edits, commit them by hand, or" >&2
  echo "    discard the repo copy:  git -C '$REPO_CHECK' restore -- ${SKILLS[*]}" >&2
  echo "  - If the server does NOT have them, upload the skill to Claude first" >&2
  echo "    (Settings > Capabilities > Skills), let the cache refresh, re-run." >&2
  exit 1
fi

# --- pick a source --------------------------------------------------------
if [[ $USE_EXPORTS -eq 1 ]]; then
  missing=()
  for s in "${SKILLS[@]}"; do
    [[ -f "$DOWNLOADS/$s.skill" ]] || missing+=("$s.skill")
  done
  if (( ${#missing[@]} )); then
    echo "ERROR: missing from ~/Downloads: ${missing[*]}" >&2
    echo "Export all four skills from Claude Desktop, or drop --exports." >&2
    exit 1
  fi
  SOURCE_DESC="Claude Desktop exports in ~/Downloads (matches the server)"
  for s in "${SKILLS[@]}"; do
    tmp="$STAGING/.unzip-$s"; mkdir -p "$tmp"
    unzip -qo "$DOWNLOADS/$s.skill" -d "$tmp"
    # archives contain a single top-level folder named after the skill
    if [[ -d "$tmp/$s" ]]; then cp -R "$tmp/$s" "$STAGING/$s"
    else cp -R "$tmp" "$STAGING/$s"; fi
    rm -rf "$tmp"
  done
else
  SOURCE_DESC="local cache folder (verify the diff — the cache can lag the server)"
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

if [[ -n "$EXPLICIT_MSG" ]]; then
  printf '%s\n' "$EXPLICIT_MSG" > "$MSG_FILE"
else
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

  # Guard: refuse to reuse a CHANGELOG entry that is already committed.
  # Without this, a change made without a new entry silently inherits the
  # previous entry's message and the log claims it did something it did not.
  SUBJECT="$(head -1 "$MSG_FILE")"
  # Write to a file rather than piping into grep: `grep -q` exits on first
  # match, which SIGPIPEs `git log`, and under `set -o pipefail` that makes the
  # pipeline report failure even on a match. The race is intermittent, so the
  # guard would pass sometimes and not others.
  git log --format=%s > "$STAGING/subjects.txt"
  if grep -Fxq "$SUBJECT" "$STAGING/subjects.txt"; then
    echo "ERROR: the newest CHANGELOG entry is already committed:" >&2
    echo "         \"$SUBJECT\"" >&2
    echo >&2
    echo "Reusing it would make the log describe a change this commit did not make." >&2
    echo "Either:" >&2
    echo "  - write a new CHANGELOG entry (normal for an accepted workflow change), or" >&2
    echo "  - for a correction that genuinely needs no entry, pass a message:" >&2
    echo "      ./sync-and-commit.sh -m \"short description of the fix\"" >&2
    exit 1
  fi
fi

echo "Commit message:"
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
