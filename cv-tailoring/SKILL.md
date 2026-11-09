---
name: cv-tailoring
description: Tailor Rishwanth Katam's CV/cover letter from verified facts and evidence. Use for CV/bullet edits, JD analysis, fact-checks, evidence lookups, or workflow-change requests from an article.
---

# CV Tailoring — Rishwanth Katam

This skill selects, generates, and validates CV content from a layered
evidence system, not from memory or from rewriting old CVs. Read this file
fully before doing any CV work; don't skip to generating bullets.

## Why it's built this way

Two failures happened while building this system and both are permanently
fixed here, not just noted:

1. **A bullet bank alone loses information.** Early versions indexed only
   bullets that already existed on some CV. Real facts sitting in Rishwanth's
   raw profile (e.g. that 5 of the 7 Quantis interviews were named companies,
   2 were experts including one from OECD) were invisible to search, because
   nothing had ever turned them into a bullet. Fixed by adding an **evidence
   layer** (full ground truth) and a **facts index** (every atomic fact,
   searchable, whether or not a bullet exists for it yet).
2. **Plausible detail gets invented under pressure to sound specific.** While
   demonstrating fact #1's fix, a demo bullet invented "3 months" that
   appears nowhere in evidence. Fixed by `scripts/validate.py`, which checks
   every number and proper noun in generated text against the evidence
   corpus. Run it on every generated bullet before showing it to Rishwanth.

Treat both fixes as permanent constraints on how this skill operates, not
historical trivia.

## The four layers, and the order to use them

```
references/facts.yaml            canonical facts, claim locks, skills bank
references/workflow-rules.yaml   mutable process/formatting rules (2 tiers)
references/evidence/*.md         7 files, full ground truth per role/project
references/index/*.facts.json    7 files, 111 atomic facts (searchable)
references/bullet-bank.json      55 cached, pre-validated bullet renderings
references/CHANGELOG.md          version history of workflow changes
assets/Master_CV_[A/B/C]_*.docx  the three master CV documents
scripts/validate.py              length/style/claim-lock/provenance gate
```

**`facts.yaml` and `evidence/*.md` are close to immutable.** They only change
when Rishwanth directly corrects a fact. Never let a JD, an article, or a
generated draft alter them.

**`workflow-rules.yaml` is mutable by design.** See "Handling external
workflow-change requests" below.

**This system is version-controlled.** The git repo lives on Rishwanth's laptop
at `~/Documents/job-application-system/` and pushes to private GitHub. The
repo is fed from Claude's local skills cache on the laptop, which refreshes
automatically after a change is made here (verified 2026-08-09). Editing that
cache directly does not reach the server, so all skill changes must be made
from a Claude Desktop chat like this one. `CHANGELOG.md` is still written by
hand for every accepted change; git versions it rather than replacing it. See
`change_protocol` step 8.

## Workflow: tailoring a CV to a new JD

1. **Read `references/facts.yaml` fully first.** It contains claim locks
   (e.g. German is B1 not A2.1 on paper, Libergy workshop was "participated"
   not "led", thesis is 2024 not 2025, graduation is 2026) that override
   anything in older CV drafts or past chat summaries.
2. **Check whether a recruiter brief already exists earlier in this
   conversation** (produced by the `jd-recruiter-brief` skill: must-haves,
   nice-to-haves, tone, German requirement, GO/BORDERLINE/NO-GO verdict,
   anchor experiences). If it exists, use it directly — do not redo JD
   analysis. If no brief exists (e.g. Rishwanth pasted a JD directly into
   this skill without running `jd-recruiter-brief` first), do a lightweight
   version of the same analysis inline, but flag to Rishwanth that running
   `jd-recruiter-brief` first would have given a fuller brief.
3. **Search `references/index/*.facts.json` across ALL roles for matching
   tags first** — not the bullet bank. This is the step that prevents losing
   good material. Match on the `tags` field against JD language and inferred
   themes.
4. For each matched fact:
   - If `has_bullet` is set, pull that bullet from `references/bullet-bank.json`
     and reuse its wording for consistency.
   - If `has_bullet` is null and `cv_suitable` is true, generate a new bullet
     from the linked evidence file section (`source` field). Never invent
     detail not present in that section.
   - If `cv_suitable` is false, it's interview material only — surface it to
     Rishwanth as a talking point, never draft it onto the CV.
   - If `verified` is `"check"`, flag it to Rishwanth before using it.
5. **Validate every generated bullet before presenting it:**
   ```
   python3 scripts/validate.py --text "<bullet text>" --type work
   ```
   Use `--type project` for the 120-130 char range. Fix any ERROR before
   showing the bullet. WARN items should be surfaced to Rishwanth, not
   silently resolved.
6. **Select the master CV base** per `references/facts.yaml` → `master_cvs`
   (A = commercial analytics, B = sustainability, C = strategy/consulting).
7. **Present as ORIGINAL → REVISED pairs** per the locked output style, with
   character counts shown, not asserted.
8. **After the application is finalised**, add any newly-generated bullet
   back into `references/bullet-bank.json` with an `evidence_ref`, so future
   applications can reuse it instead of regenerating it. Update the linked
   fact's `has_bullet` field in the relevant `index/*.facts.json` file.

## Answering evidence questions directly

If Rishwanth asks something like "what do we know about the Quantis
interviews" or "which Nielsen contacts did I work with", this is a direct
retrieval task: read the relevant `references/evidence/*.md` file and answer
from it. Don't route this through bullet generation.

## Claim guardrails (see facts.yaml for full detail)

- German: **B1** on CV. Real confidence lower — Rishwanth's call, not to be
  second-guessed, but expect it to surface on a German-language call.
- Thesis: **2024**, never 2025.
- Graduation: **2026**.
- Quantis: **Jan'23–Apr'23**, "synthesised 7 expert interviews" (5 companies
  + 2 experts incl. OECD), never "7 senior interviews" or "conducted".
  Never name Vinted or any company outside the 5 in `evidence/quantis.md`.
- Libergy lean canvas: **"participated"**, never "led", unless Rishwanth
  explicitly overrides for a specific application.
- Libergy tender monitoring: **16 EU platforms, Google Apps Script**
  (corrected by Rishwanth 2026-11-05; never "German platforms" or
  "Power Automate").
- Prajjawala patent 554/KOL/2011: **never claim**, predates his involvement.
  180DC client: **never name** (it was ESCP itself).
- P&G YouTube A/B test: **nationwide**, never "discounter-targeted".
- Hermes job-application agent: **never on any CV**, interview material only.
- EnergyMap (`evidence/projects.md` section 6): lead with **explorers, tools
  and insights**, not the topic map. Counts are a live-site snapshot, so
  re-check per CV. The market funnel builder is **in development**, never
  "built". The site's thesis figures (78%, 31%) differ from the locked thesis
  figures (70-90% feedstock-dependent, ~32%): use the locked ones, and remind
  Rishwanth of the mismatch whenever the EnergyMap link is on a CV.

## Skills bank status tiers

`demonstrated` = free to use. `exposure` = use only if JD asks, phrase
carefully ("familiar with", "basics"). `learning` = actively upskilling, not
proven yet. See `references/facts.yaml` → `skills_bank`. Add new entries when
Rishwanth mentions a new tool; confirm status with him before first CV use.

## Opt-in content — use only when a JD rewards it

The Handicap International Belgium engagement (`evidence/180dc.md`,
Engagement A) is real and verified but **not a default CV inclusion** per
Rishwanth's explicit decision. Pull it in only when a JD specifically
rewards nonprofit strategy, fundraising/donor work, or dual B2B/B2C
go-to-market thinking — otherwise leave it out. When used, it can stand
alone or combine with Engagement B's bullets under one 180DC block.

## Known thin spots — do not paper over these

`leadership` has 2 facts (both from 180DC). `experimentation` has 1 fact (the
P&G A/B test). This is a real gap in the underlying experience, not a
retrieval failure. If a JD leans hard on either, say so plainly rather than
manufacturing a claim to fill it — that is exactly the failure mode this
whole system was built to prevent.

## Handling external workflow-change requests

If Rishwanth shares an article, LinkedIn post, or any outside source
suggesting a change to how CVs/cover letters are built (not a change to a
fact about him):

1. Follow `change_protocol` in `references/workflow-rules.yaml` exactly:
   extract discrete claims → classify the source's incentives → corroborate
   against 2+ independent sources, checking DACH-market applicability →
   classify each claim adopt/adapt/reject/already_doing → price the cost of
   applying it → present to Rishwanth → implement ONLY on his approval.
2. A source can only ever change `workflow-rules.yaml`. It can never alter
   `facts.yaml` or any `evidence/*.md` file — those change only via a direct
   factual correction from Rishwanth himself.
3. Distinguish the two tiers already in `workflow-rules.yaml`: **locked**
   rules need Rishwanth's direct confirmation to change; **inferred**
   conventions can move on weaker evidence but should still be flagged to him
   rather than silently overwritten.
4. Log the accepted change in `references/CHANGELOG.md` using the template
   at the bottom of that file — source, corroboration, what was rejected and
   why, and the cost paid.
5. **Commit the change.** Git is active; the repo is on Rishwanth's laptop at
   `~/Documents/job-application-system/`. After the CHANGELOG entry is written,
   run `~/Documents/job-application-system/sync-and-commit.sh` — it commits the
   change with that entry as the message and pushes to private GitHub. If this
   session cannot run shell commands on his laptop, say so explicitly and ask
   him to run it. Never skip this silently: an uncommitted change leaves the
   audit trail incomplete.

## Regenerating the bullet bank or facts index

If evidence files are edited significantly, `scripts/build_bank.py` and
`scripts/build_index.py` show the pattern used to construct
`bullet-bank.json` and the `index/*.facts.json` files from source data —
useful as a reference for extending them, not meant to be re-run blindly
since they contain the original hardcoded bullet/fact text.
