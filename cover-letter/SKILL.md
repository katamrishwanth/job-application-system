---
name: cover-letter
description: Draft a cover letter for Rishwanth Katam in his established style. Use after cv-tailoring, or whenever he asks for a cover letter. Needs facts.yaml/evidence from the cv-tailoring skill.
---

# Cover Letter — Rishwanth Katam

Runs after `jd-recruiter-brief` and `cv-tailoring` for a given application —
needs the recruiter brief (company research, tone, core problem) and the
selected CV content (which experiences got chosen as anchors) as input.

## Style basis

`references/style-rules.md` documents the four-move structure, salutation
rule, the anchor-swap-by-role-type decision, and the honesty-on-omission
pattern, extracted from five full real letters:
`references/sample-bain.txt`, `sample-detecon.txt`, `sample-rwe.txt`,
`sample-aurora.txt`, `sample-vfg.txt`. Real average across all five: 396
words. **RWE and Aurora contain 3 specific factual errors** (verified
2026-08-06, detailed at the top of style-rules.md) — read that annotation
before using either as a content template, though their structure and tone
are still good reference.

## Steps

1. Confirm a recruiter brief and CV selection already exist in this
   conversation (from `jd-recruiter-brief` / `cv-tailoring`). If not, ask
   Rishwanth to run those first, or pull the minimum needed (company name,
   role, 2-3 anchor experiences) directly from what he's shared.
2. Load `facts.yaml` and the relevant `evidence/*.md` files, at
   `/mnt/skills/user/cv-tailoring/references/` once both skills are
   installed — every claim about Rishwanth must trace there, exactly as
   in CV work.
3. Web search the company if the brief didn't already do this, for move 4's
   "why this company" reasons. Generic praise fails silently here — the
   two real samples both used specific, checkable company facts.
4. Draft following the four-move structure. Pick the opening anchor based
   on what the role actually is, not a fixed default — see the anchor-swap
   note in style-rules.md.
5. Length: target 75-85% of the sample average (396 words —
   `workflow-rules.yaml` L09), unless Rishwanth specifies otherwise.
6. **Validate before presenting:**
   ```
   python3 scripts/validate.py --file draft.txt --type cover_letter \
     --sample-avg-words <N> \
     --known-entities "<Company Name>,<other researched company facts/names>"
   ```
   `validate.py` lives at `/mnt/skills/user/cv-tailoring/scripts/validate.py`
   once both skills are installed. Pass every
   proper noun from the target company's own research as `--known-entities`
   — the provenance check is otherwise correct to flag them, since they
   won't appear in Rishwanth's personal evidence by design. Anything else
   flagged is either a real fabrication risk or a formatting mismatch worth
   fixing before it reaches Rishwanth.
7. If asked to omit something material (e.g. German level), state the risk
   once plainly, then respect the decision — don't relitigate it on later
   turns of the same application.
8. Present as ORIGINAL → REVISED if editing an existing draft, or as a
   clean draft with the word count and % shown, not asserted.

## Claim guardrails

Same as `cv-tailoring`: German is B1, Libergy workshop was "participated,"
Quantis is "synthesised 7 expert interviews," the P&G test was nationwide,
never discounter-targeted, Hermes never appears. See `facts.yaml` for the
full list — a cover letter is prose, not bullets, but the same facts apply.
