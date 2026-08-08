# Git workflow — job application system

The point of this repo is **provenance**, not backup. `git log` is meant to be
read by a human, top to bottom, as the history of why this system says what it
says. Every commit should answer: what changed, on whose authority, and what it
cost.

`CHANGELOG.md` remains the primary human-facing record. Git adds the three
things a changelog structurally cannot do: restore prior file *content*, prove
that `facts.yaml` and `evidence/` have not silently drifted, and timestamp what
a claim said on the day it went onto a submitted CV.

---

## Where this repo lives

Repo root is the Claude app's skills directory:

```
~/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/c9caca1d-5ea4-44d0-adcf-b708df692cb0/e23955f7-0f0c-4e56-9dfe-31648e7c557d/skills/
```

This is the live directory the skills actually run from, so there is **no copy
step** — what you commit is exactly what executed.

Two things to know about this location:

1. **The UUIDs are stable, not per-session.** They have been unchanged since
   2026-05-14, and the same pair appears in other app subtrees, so they are
   account/installation identifiers despite the `local-agent-mode-sessions`
   folder name.
2. **It is a sync target.** `manifest.json` shows each skill carries a server
   side `skillId` and `updatedAt`, meaning this folder is a local cache of
   cloud-held skills. A future app sync could in principle overwrite files
   here. Git is what makes that *visible* (`git status` would show it) and
   *reversible* — but the repo itself is not yet backed up anywhere off this
   machine. See "Remote" below.

Tracked: `cv-tailoring/`, `cover-letter/`, `jd-recruiter-brief/`,
`application-qa/`. Everything else is ignored — see `.gitignore`, which
explains each exclusion.

---

## Committing an approved change

Changes to this system are governed by `change_protocol` in
`cv-tailoring/references/workflow-rules.yaml`. Git is step 8, after that
protocol's step 7.

**Only `workflow-rules.yaml` and skill files change this way.** `facts.yaml`
and `evidence/*.md` are never edited by an article-driven workflow change — they
change only when a primary source corrects them, which is a different kind of
commit and should say so explicitly in its message.

### The sequence

1. Article or suggestion is analysed per `change_protocol` steps 1–5.
2. Findings and recommendation presented to Rishwanth (step 6).
3. **Implement only on his explicit approval.** No approval, no file edits, so
   nothing to commit.
4. Write the `CHANGELOG.md` entry — source, corroboration, rejected sub-claims
   and why, cost paid (step 7).
5. Stage the edited files *and* the changelog together, and commit once, using
   the full changelog entry as the message body:

```bash
git add -A && git commit -F <(printf '%s\n' "<paste the full CHANGELOG.md entry here>")
```

In practice the session doing the work should write the message to a temp file
and commit with `git commit -F <file>`, so the entry keeps its formatting.

6. Record the resulting hash back into that changelog entry's `**Revert:**`
   line, replacing the "git not yet set up" placeholder, then amend:

```bash
git commit --amend --no-edit -a
```

### The commit message *is* the changelog entry

Not a summary of it. The whole entry — What / Source / Corroboration /
Rejected / Cost / Revert. First line is a short subject (`YYYY-MM-DD — <title>`),
then a blank line, then the entry verbatim. This is what makes `git log` and
`CHANGELOG.md` two views of one record rather than two records that can drift.

### One commit per accepted change. Never squash.

Each accepted change is one commit, even a one-line edit to a single rule. Do
not batch two approved changes into one commit, do not squash on merge, do not
rebase history that has been committed. Two changes accepted on the same day are
two commits.

The log is the audit trail. A squashed commit destroys the mapping between a
decision and its consequence, which is the only thing this repo exists to
preserve.

---

## Branch strategy: commit directly to `main`

No feature branches for article-driven changes. The reasoning:

- **The review gate is upstream.** `change_protocol` step 6 requires
  Rishwanth's explicit approval *before* implementation. A branch would model a
  review that has already happened in conversation — ceremony, not safety.
- **Single operator, no CI, no concurrent work.** Nothing to isolate against.
- **Merge commits pollute a linear audit trail.** The log should read as a
  sequence of decisions, not a graph.

**The one exception:** if a change needs to be trialled across several real
applications before you commit to it, branch it:

```bash
git switch -c trial/<short-name>
```

Run live applications from that branch. If it holds up, merge with
`--no-ff` so the trial period stays visible in the history; if it doesn't,
delete the branch and log the rejection in `CHANGELOG.md` anyway — a rejected
trial is a finding worth keeping.

---

## Automation

Safe to automate, because the approval gate is upstream of any file edit: by the
time anything on disk changes, it has already been accepted.

**Do not use a filesystem watcher.** It would fire on each save mid-edit,
producing a burst of commits with generic messages, and it cannot carry the
changelog entry — that entry is written at step 7, *after* the edits land. Both
outcomes break "one commit per accepted change".

Instead, make the commit the final action of the change workflow itself: once
step 7 writes the changelog entry, the same session runs the commit with that
entry as the message. That is automation triggered by *workflow completion*
rather than by file modification time.

---

## Checking for drift

The system's value rests on `facts.yaml` and `evidence/*.md` being trustworthy.
Before relying on them for an application, confirm nothing has changed
underneath you:

```bash
git status --short && git log --oneline -5
```

A clean status means the facts are as last approved. Unexpected modifications to
`facts.yaml` or `evidence/` should be investigated before submitting anything,
not committed reflexively — the system exists to prevent fabrication, and an
unexplained edit to a fact file is exactly the failure it guards against.

To see what a claim said at the time it was used:

```bash
git log -p --follow cv-tailoring/references/facts.yaml
```

---

## Remote

Not configured. The repo currently lives only in a synced app cache directory,
which means a folder-level reset would still lose the history.

Pushing to a private GitHub repo would close that gap. Note that these files
contain personal career data — full employment evidence, reference letter
content, and the contents of three master CVs — so this is a deliberate decision
to make, not a default. Nothing has been pushed anywhere.

To add one when you decide to:

```bash
git remote add origin git@github.com:<user>/<private-repo>.git && git push -u origin main
```
