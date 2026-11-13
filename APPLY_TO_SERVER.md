# Prompt: apply the git-workflow changes to the skills

**Why this file exists.** Skills execute from Claude's **server** copy. The
folder at `~/Library/Application Support/Claude/.../skills/` is a download-only
cache — editing it from the laptop changes nothing the skill can see (verified
2026-08-09 by exporting the `.skill` archives and diffing). Skill files can only
be changed from inside a **Claude Desktop chat**.

So: paste the block below into a Claude Desktop chat. Then follow "After it's
done" at the bottom.

---

## Rule for every change applied from a chat: the CHANGELOG lives in `cv-tailoring`

There is one `CHANGELOG.md` for all four skills, at
`cv-tailoring/references/CHANGELOG.md`. So a change to `jd-recruiter-brief`,
`cover-letter` or `application-qa` touches **two** skills on the server: the
one being changed, and `cv-tailoring` for its entry. The chat must save both
before you run `sync-and-commit.sh`.

If the entry only reaches the repo (or a "Claude outputs" folder), the server
never has it, and every sync wipes it from the repo. This happened with the
2026-11-09 `jd-recruiter-brief` change: the skill edit landed, the entry didn't,
and it kept disappearing until `cv-tailoring` was re-uploaded on 2026-11-13.

When you write a prompt for a change to any skill other than `cv-tailoring`,
add this line to it:

```
Also add the CHANGELOG entry to references/CHANGELOG.md in my cv-tailoring
skill, and save that skill too. Confirm both skills are saved before you finish.
```

If the entry still doesn't reach the server, `sync-and-commit.sh` will refuse
to run because the repo has edits the server lacks. Upload the skill in Claude
(Settings → Capabilities → Skills), let the local cache refresh, then re-run.

---

## The prompt — paste everything between the lines

---

```
Please make the following edits to my cv-tailoring skill. There are 8 edits
across 3 files. Make all of them, then show me the changed sections so I can
verify. Do not touch facts.yaml, evidence/*.md, index/*.facts.json or
bullet-bank.json — none of them need changing.

Context you need: git version control is now set up. The repo lives on my
laptop at ~/Documents/job-application-system/ and pushes to a private GitHub
repo. CHANGELOG.md stays the primary hand-written record — git versions it, it
does not replace it. Several files still say git isn't set up; that's what most
of these edits fix.


======================================================================
FILE 1: references/workflow-rules.yaml
======================================================================

EDIT 1 — replace the whole `meta:` block.

FIND:
meta:
  version: 1
  status: "git not yet set up (2026-08-05) — see CHANGELOG.md for interim
    tracking. Set up git BEFORE implementing the first article-driven
    change, per explicit instruction."

REPLACE WITH:
meta:
  version: 2
  status: "Git version control active since 2026-08-09. Repo on Rishwanth's
    laptop at ~/Documents/job-application-system/, pushed to a private GitHub
    repo. CHANGELOG.md remains the primary hand-written record and must still
    be written for every accepted change — git versions it, it does not
    replace it. Commit procedure: change_protocol step 8."


EDIT 2 — add a step 8 to change_protocol.

In the `change_protocol:` block, the `steps:` list currently ends with step 7
("7. Log the accepted change in CHANGELOG.md..."). Add this immediately after
step 7 and before the `never:` key, matching the existing indentation exactly:

    - "8. Commit the change. The git repo is on Rishwanth's laptop at
        ~/Documents/job-application-system/ and pushes to private GitHub. Run
        ~/Documents/job-application-system/sync-and-commit.sh — it reads the
        skills, makes ONE commit using the new CHANGELOG entry as its message,
        and pushes. If this session cannot run shell commands on his laptop,
        say so explicitly and ask him to run it himself. One commit per
        accepted change: never batch two, never squash — the log is the audit
        trail. Never skip this silently: an uncommitted change leaves the
        audit trail incomplete. Details in GIT_WORKFLOW.md."


======================================================================
FILE 2: SKILL.md
======================================================================

EDIT 3 — replace item 5 under "Handling external workflow-change requests".

FIND:
5. Git isn't set up yet. Flag this to Rishwanth before implementing the
   first such change, per his explicit instruction — CHANGELOG.md is interim
   tracking only.

REPLACE WITH:
5. **Commit the change.** Git is active; the repo is on Rishwanth's laptop at
   `~/Documents/job-application-system/`. After the CHANGELOG entry is written,
   run `~/Documents/job-application-system/sync-and-commit.sh` — it commits the
   change with that entry as the message and pushes to private GitHub. If this
   session cannot run shell commands on his laptop, say so explicitly and ask
   him to run it. Never skip this silently: an uncommitted change leaves the
   audit trail incomplete.


EDIT 4 — add a version-control note.

FIND:
**`workflow-rules.yaml` is mutable by design.** See "Handling external
workflow-change requests" below.

ADD IMMEDIATELY AFTER IT (keep the existing two lines, then a blank line):
**This system is version-controlled.** The git repo lives on Rishwanth's laptop
at `~/Documents/job-application-system/` and pushes to private GitHub. It is
fed by exporting the `.skill` files from Claude Desktop — not by editing files
directly, which does not reach the server. `CHANGELOG.md` is still written by
hand for every accepted change; git versions it rather than replacing it. See
`change_protocol` step 8.


======================================================================
FILE 3: references/CHANGELOG.md
======================================================================

EDIT 5 — replace the description on line 3.

FIND:
Interim version tracking until git is set up. One entry per accepted change.
Format: date, what changed, source/reasoning, cost paid, how to revert.

REPLACE WITH:
The primary hand-written record of every accepted workflow change. Still
written by hand for every change — git version-controls this file, it does not
replace it. One entry per accepted change.
Format: date, what changed, source/reasoning, cost paid, how to revert.


EDIT 6 — fix the Revert line of the 2026-08-06 two-tier keyword entry.

FIND:
**Revert:** git not yet set up. Restore prior wording of
`task1-prompt.md` / `jd-recruiter-brief/SKILL.md` from this entry if needed.

REPLACE WITH:
**Revert:** predates git, so it sits inside the baseline commit and git cannot
isolate it. Restore prior wording of `task1-prompt.md` /
`jd-recruiter-brief/SKILL.md` from this entry if needed.


EDIT 7 — fix the Revert line of the 2026-08-06 (2) fact-verification entry.

FIND:
**Revert:** git not yet set up. This entry documents every changed file.

REPLACE WITH:
**Revert:** predates git; sits inside the baseline commit. This entry documents
every changed file.


EDIT 8 — fix the Revert line in the template at the bottom, and add a new
entry.

8a. In the "Template for future entries" code block, FIND:
**Revert:** <git hash once git exists, or "restore <file> from this entry's
  pre-change copy">

REPLACE WITH:
**Revert:** <find the commit with: git log --oneline --grep="<short title>">

8b. Add this as a new entry immediately BEFORE the "## Template for future
entries" heading (keep the `---` separator above it):

## 2026-08-09 — Git version control activated

**What:** `workflow-rules.yaml` (`meta` block rewritten, version 1 → 2; new
`change_protocol` step 8), `SKILL.md` (item 5 of external workflow-change
handling rewritten; version-control note added), `CHANGELOG.md` (header and
three stale "git not yet set up" lines corrected). On Rishwanth's laptop: git
repo at `~/Documents/job-application-system/` with `.gitignore`,
`GIT_WORKFLOW.md`, `sync-and-commit.sh`, `APPLY_TO_SERVER.md`, pushed to a
private GitHub repo (katamrishwanth/job-application-system).

**Source:** Rishwanth's direct instruction. One-time setup that this protocol
itself required before the first article-driven change could be accepted.

**Corroboration:** n/a — infrastructure, not an external claim about hiring
practice. No fact or CV content is affected.

**Rejected:**
- *Git repo inside the local skills cache folder.* Tried first. The Claude app
  deleted `.git` within ~90 minutes (2026-08-08 23:25). Ordinary files
  survived; only the repo was removed.
- *Editing skill files on the laptop.* Tried second. That folder is a
  download-only cache; edits are invisible to the running skill, which loads
  from the server. Verified by exporting the four `.skill` archives and
  diffing, and confirmed functionally — a fresh session reported the steps
  list ending at 7. Hence this change is applied from a Desktop chat instead.
- *A filesystem watcher auto-committing on save.* Would fire mid-edit producing
  bursts of commits, and could not use the CHANGELOG entry as the message,
  which is the whole point of the log.

**Cost:** 3 files edited in cv-tailoring. No changes to `facts.yaml`, any
`evidence/*.md`, any `index/*.facts.json`, or `bullet-bank.json`. No re-editing
of submitted CVs. Adds an export-and-run step at the end of each accepted
change.

**Revert:** `git log --oneline --grep="Git version control activated"`, then
`git revert` that commit.
```

---

## After it's done

The chat may offer to run `sync-and-commit.sh` itself — let it try. That is the
intended end state, and either result is useful information.

**Then check whether the local cache picked up the change:**

```bash
~/Documents/job-application-system/sync-and-commit.sh --dry-run
```

- **It lists `SKILL.md`, `workflow-rules.yaml`, `CHANGELOG.md` as changed** →
  the cache refreshed from the server. Drop `--dry-run` to commit and push. No
  exporting needed, now or in future.
- **It says "No changes"** → the cache has not refreshed yet. Wait a few
  minutes, reopen Claude Desktop, and retry. If it stays empty, fall back to
  exporting the four skills into `~/Downloads` and run with `--exports`.

**Finally, verify in a new Desktop chat:**

> Quote step 8 of change_protocol from workflow-rules.yaml.

If it quotes step 8, the server, the repo and GitHub are all consistent.
