# Git workflow — job application system

The point of this repo is **provenance**, not backup. `git log` is meant to be
read top to bottom as the history of why this system says what it says. Every
commit should answer: what changed, on whose authority, and what it cost.

`CHANGELOG.md` stays the primary human-facing record. Git adds the three things
a changelog structurally cannot do: restore prior file *content*, prove that
`facts.yaml` and `evidence/` have not silently drifted, and timestamp what a
claim said on the day it went onto a submitted CV.

---

## The one command

After Rishwanth approves a change and the `CHANGELOG.md` entry is written, the
change lives on Claude's server. To get it into git:

1. In Claude Desktop, export all four skills (`⋯ → Download`) into `~/Downloads`.
2. Run:

```bash
~/Documents/job-application-system/sync-and-commit.sh
```

It reads the `.skill` exports, makes one commit using the newest CHANGELOG entry
as the message, and pushes to private GitHub. It refuses to run when nothing
changed, so running it twice is harmless. `--dry-run` shows what would happen
without committing.

This is step 8 of `change_protocol` in `workflow-rules.yaml`.

**Why the export step exists:** skills run from the server, and the local folder
is a download-only cache. See "Settled" below.

---

## Why the repo is in Documents and not with the skills

The skills run from inside the Claude app's data folder:

```
~/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/c9caca1d-…/e23955f7-…/skills/
```

A repo was initialised there first. **The app's sync deleted `.git` within about
90 minutes** (2026-08-08, ~23:25, alongside a `manifest.json` rewrite). Ordinary
files were left untouched; only the repo was removed. So a repo cannot live
there, and `sync-and-commit.sh` copies files out instead.

Note the folder path itself is *stable* — those UUIDs are account and
installation identifiers, unchanged since 2026-05-14, despite the
`local-agent-mode-sessions` name. The problem was never the path. It was `.git`
being deleted.

If the app ever does move the folder, the script fails loudly with instructions
rather than committing a half-empty repo.

### Settled: editing files locally does NOT reach the Claude server

Tested and confirmed on 2026-08-09. The skills execute from Claude's **server**
copy. That `~/Library/…/skills/` folder is a **download-only cache**: edits made
there are invisible to the running skill.

How it was established:
- `manifest.json` kept reporting `updatedAt: 2026-08-06` for all four skills
  after local edits — the server never registered them.
- All four skills were exported from Claude Desktop as `.skill` archives and
  diffed against the local cache. The server copies contained none of the edits.
- Functionally confirmed: a fresh Desktop session, asked to quote step 8 of
  `change_protocol`, reported the steps list ending at 7.

**Consequences for this repo:**

1. **Skill files can only be changed from inside a Claude Desktop chat.** To
   apply an edit, paste the prompt in `APPLY_TO_SERVER.md` into a Desktop chat.
   Editing the cache folder achieves nothing.
2. **The authoritative source for this repo is a fresh `.skill` export**, not
   the cache. Export all four from Claude Desktop into `~/Downloads`, then run
   `sync-and-commit.sh` — it prefers the exports automatically and says which
   source it used.
3. **The cache is a fallback only** (`--cache`), trustworthy solely if it has
   refreshed from the server since the change. It is not known whether or when
   it does refresh, so prefer exports.

---

## Committing an approved change

Changes are governed by `change_protocol` in
`cv-tailoring/references/workflow-rules.yaml`. Git is step 8, after step 7.

**Only `workflow-rules.yaml` and skill files change this way.** `facts.yaml` and
`evidence/*.md` never change from an article-driven workflow change — they change
only when a primary source corrects them, which is a different kind of commit
and should say so plainly in its message.

1. Analyse the source per steps 1–5.
2. Present findings and recommendation (step 6).
3. **Implement only on explicit approval.** No approval, no edits, nothing to commit.
4. Write the `CHANGELOG.md` entry — source, corroboration, rejected sub-claims
   and why, cost paid (step 7).
5. Run `sync-and-commit.sh` (step 8).

### The commit message *is* the changelog entry

Not a summary of it. The script takes the newest dated `## YYYY-MM-DD` section
verbatim, so the log and the changelog cannot drift apart. Write the entry
properly and the commit message takes care of itself.

### One commit per accepted change. Never squash.

One accepted change, one commit — even a one-line edit to a single rule. Don't
batch two approved changes together, don't squash on merge, don't rebase
committed history. Two changes accepted the same day are two commits.

A squashed commit destroys the mapping between a decision and its consequence,
which is the only thing this repo exists to preserve.

### On recording commit hashes in the changelog

The old `**Revert:**` lines say "git not yet set up". Deliberately, the script
does **not** write hashes back into entries: amending a commit to add its own
hash changes that hash, so the recorded value is always stale. Entries are
identified by date and title, which are unique — find one with:

```bash
git log --oneline --grep="Two-tier keyword"
```

---

## Branch strategy: commit directly to `main`

No feature branches for article-driven changes:

- **The review gate is upstream.** Step 6 requires explicit approval *before*
  implementation. A branch models a review that already happened in conversation.
- **Single operator, no CI, no concurrent work.** Nothing to isolate against.
- **Merge commits pollute a linear audit trail.** The log should read as a
  sequence of decisions, not a graph.

**One exception:** if a change needs trialling across several real applications
before you commit to it:

```bash
git switch -c trial/<short-name>
```

Merge with `--no-ff` if it holds up, so the trial stays visible. If it doesn't,
delete the branch and log the rejection in `CHANGELOG.md` anyway — a rejected
trial is a finding worth keeping.

---

## Automation

Safe to automate, because the approval gate sits upstream of any file edit: by
the time anything on disk changes, it has already been accepted.

**Do not add a filesystem watcher.** It fires on every save mid-edit, producing
bursts of commits, and it cannot know the changelog text — that gets written at
step 7, *after* the edits. You'd get `auto-commit 2026-08-09` as a message,
which throws away the reason this repo exists. The trigger is workflow
completion, not file modification time.

---

## Checking for drift

The system's value rests on `facts.yaml` and `evidence/*.md` being trustworthy.
Before relying on them:

```bash
cd ~/Documents/job-application-system && ./sync-and-commit.sh --dry-run
```

"No changes" means the live skills match the last approved commit. Unexpected
modifications to `facts.yaml` or `evidence/` should be investigated before
submitting anything, not committed reflexively — this system exists to prevent
fabrication, and an unexplained edit to a fact file is exactly that failure.

To see what a claim said when it was used:

```bash
git log -p --follow cv-tailoring/references/facts.yaml
```

---

## Remote

`origin` → `git@github.com:katamrishwanth/job-application-system.git` (private).

Authentication is an SSH key at `~/.ssh/id_ed25519`, added to GitHub on
2026-08-08. Private means visible only to Rishwanth and anyone explicitly
invited — but the data does sit on GitHub's servers, including full employment
evidence, reference-letter content and three master CVs. That was a deliberate
choice, not a default.

To verify the remote is reachable:

```bash
ssh -T git@github.com
```
