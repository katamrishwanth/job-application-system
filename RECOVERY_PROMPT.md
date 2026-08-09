# Recovery prompt

Paste the block below into a Claude Desktop chat if the skill edits ever get
reverted — i.e. if `change_protocol` stops at step 7, or the version-control
note is missing from `cv-tailoring/SKILL.md`.

**How to know you need this:** run

```bash
~/Documents/job-application-system/sync-and-commit.sh --dry-run
```

If it lists `cv-tailoring/SKILL.md` or `workflow-rules.yaml` as changed when you
haven't approved anything, the server copy has overwritten your local edits.
Check what was lost with `git diff`, then paste the prompt below.

---

## The prompt

```
I need you to restore two edits to my cv-tailoring skill that got reverted.
Both files are in your skills folder. Do not create a git repo in that folder —
the app's sync deletes it. The repo lives at ~/Documents/job-application-system/

EDIT 1 — cv-tailoring/references/workflow-rules.yaml

In the `change_protocol:` block, the `steps:` list currently ends at step 7
("7. Log the accepted change in CHANGELOG.md..."). Add this step 8 immediately
after step 7, before the `never:` key, matching the existing indentation:

    - "8. Commit it: run ~/Documents/job-application-system/sync-and-commit.sh
        That copies these skills into the git repo, makes ONE commit using the
        new CHANGELOG entry as its message, and pushes to the private GitHub
        repo. One commit per accepted change — never batch two, never squash;
        the log is the audit trail. Do NOT git init inside this skills folder:
        the Claude app's sync deletes .git (verified 2026-08-08), which is why
        the repo lives in Documents. If this session cannot run the script,
        say so plainly rather than skipping it — an uncommitted change leaves
        the audit trail incomplete. Details in that repo's GIT_WORKFLOW.md."

EDIT 2 — cv-tailoring/SKILL.md

Find the line that reads:

  **`workflow-rules.yaml` is mutable by design.** See "Handling external
  workflow-change requests" below.

Immediately after it, add:

  **This system is version-controlled.** The git repo lives at
  `~/Documents/job-application-system/`, not in this skills folder — the Claude
  app's sync deletes `.git` from here. After any approved change is logged in
  `CHANGELOG.md`, run `~/Documents/job-application-system/sync-and-commit.sh` to
  commit and push it (change_protocol step 8). One commit per accepted change,
  never squashed: `git log` is the human-facing audit trail. See
  `GIT_WORKFLOW.md` in that repo.

AFTER BOTH EDITS

Do not add a CHANGELOG entry — this is a restoration of a previously logged
change (the 2026-08-08 entry), not a new one. Then run:

  ~/Documents/job-application-system/sync-and-commit.sh --dry-run

and tell me what it reports. If you cannot run shell commands, say so
explicitly — do not skip it silently — and I will run it myself.
```

---

## If you also need to rebuild the repo from scratch

Only if `~/Documents/job-application-system/` is lost entirely. The GitHub copy
is authoritative:

```bash
cd ~/Documents && git clone git@github.com:katamrishwanth/job-application-system.git
chmod +x job-application-system/sync-and-commit.sh
```

Then copy the skills back into the Claude app folder from the repo if those were
lost too — the reverse of what `sync-and-commit.sh` does.
