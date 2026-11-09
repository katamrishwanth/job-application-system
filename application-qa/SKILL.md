---
name: application-qa
description: Final pre-submission check for Rishwanth Katam's applications — length, fabrication, keyword coverage, and consistency across CV, cover letter, and form answers. Use before he submits anything.
---

# Application QA — Rishwanth Katam

Runs last, after `jd-recruiter-brief`, `cv-tailoring`, and `cover-letter`
have produced their pieces. This is the gate before submission, not a
drafting step — don't rewrite content here, flag it and hand back to the
right skill.

## What this catches that the other skills don't

`cv-tailoring` and `cover-letter` validate content as it's generated, one
bullet or one letter at a time. Two failure modes only show up once
everything is assembled:

1. **Missing required keywords** — the opposite of fabrication. A bullet can
   be perfectly accurate and the application can still fail because a
   must-have term never made it in. Real precedent: the Accenture session
   found "operating model" absent from the CV despite appearing 3 times in
   the JD, caught by eye after the fact. `scripts/check_keyword_coverage.py`
   catches this before submission instead.
2. **Cross-document drift** — the CV says one thing, the cover letter says
   another. Running `validate.py` on each document separately catches
   deviation from a locked fact in each piece individually, but doesn't do
   a true diff between documents. If both documents independently deviate
   from `facts.yaml` in the *same* wrong direction, running each file alone
   still catches it (it's checked against the lock, not against the other
   document) — but be aware this isn't a document-to-document diff, it's
   both being checked against the same source of truth.

## Steps

1. **Length and fabrication, every piece.** `cv-tailoring`'s validator lives
   at `/mnt/skills/user/cv-tailoring/scripts/validate.py` once both skills
   are installed (confirm with `ls /mnt/skills/user/` if this ever doesn't
   resolve — the convention is `/mnt/skills/user/<skill-name>/`):
   ```
   python3 /mnt/skills/user/cv-tailoring/scripts/validate.py --file cv_bullets.txt --type work
   python3 /mnt/skills/user/cv-tailoring/scripts/validate.py --file cv_bullets.txt --type project
   python3 /mnt/skills/user/cv-tailoring/scripts/validate.py --text "<summary>" --type summary
   python3 /mnt/skills/user/cv-tailoring/scripts/validate.py --file letter.txt --type cover_letter \
       --sample-avg-words 396 --known-entities "<company facts>"
   ```
2. **Keyword coverage against the brief's atomic list:**
   ```
   python3 scripts/check_keyword_coverage.py \
       --keywords "<atomic keywords from jd-recruiter-brief Part 1>" \
       --file combined_cv_and_letter.txt
   ```
   Every MISSING result needs a decision: either it's a real gap (say so to
   Rishwanth plainly, don't hide it) or it's something he has evidence for
   that didn't make it into the draft — check `evidence/*.md` and
   `index/*.facts.json` for a matching fact before assuming it's a true gap.
3. **Page/line budget:** target ~53 lines for a one-page CV
   (`workflow-rules.yaml` I04 — this is a rough operating ceiling from past
   sessions, not a measured constant; recount per document). `wc -l` the
   assembled CV text as a rough proxy, but the real check is whether it
   renders to one page in the actual document.
4. **German language consistency:** confirm B1 appears identically (not "A2"
   or upgraded to "B2") across the CV, cover letter, and any application
   form text — `validate.py`'s claim locks catch deviation in each piece
   individually.
5. **Corrected-fact consistency:** check every piece for facts corrected
   after older CVs and letters were written: Libergy tender monitoring is
   **16 EU platforms via Google Apps Script** (never "German platforms" or
   "Power Automate", corrected 2026-11-05). If the EnergyMap link appears,
   re-read the live site and confirm the counts on the CV (explorers,
   studies) still match it, confirm the market funnel builder is not called
   built, and flag that the site's thesis figures (78%, 31%) differ from the
   locked thesis figures (70-90% feedstock-dependent, ~32%) used on the CV.
   `validate.py` claim locks catch the tender and funnel-builder cases; the
   live-site count check is manual.
6. **Document upload guidance (if asked):** past sessions included decoding
   German reference letters (Arbeitszeugnis, Empfehlungsschreiben) — this
   uses established Zeugnissprache convention (coded phrasing where
   ostensibly neutral language signals a specific performance rating).
   Web search to confirm current phrase-meaning conventions each time
   rather than relying on a static bundled table, since getting this wrong
   in either direction (missing a negative code, or reading positive
   language as coded when it isn't) actively misleads Rishwanth.

## Output

A short pass/fail summary per check, not a rewrite. If something fails,
name which skill should fix it (`cv-tailoring` for a bullet, `cover-letter`
for the letter) rather than patching it inline here.
