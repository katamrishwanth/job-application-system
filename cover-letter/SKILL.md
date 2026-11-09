---
name: "cover-letter"
description: "Draft a cover letter for Rishwanth Katam in his established style. Use after cv-tailoring, or whenever he asks for a cover letter. Needs facts.yaml/evidence from the cv-tailoring skill."
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
`sample-aurora.txt`, `sample-vfg.txt`. **RWE and Aurora contain 3 specific
factual errors** (verified 2026-08-06, detailed at the top of
style-rules.md) — read that annotation before using either as a content
template, though their structure and tone are still good reference.
**The Detecon sample still says tender monitoring ran "across 16 platforms
in Power Automate"** — wrong since the 2026-11-05 correction (16 EU
platforms, Google Apps Script). Never copy that sentence.

## Length: 300–335 words

The cover letter body (salutation to sign-off) is **300–335 words**, unless
Rishwanth gives a different limit for a specific application (treat that as
a one-off, not a new default). This replaces the old "75-85% of the sample
average" wording (decided by Rishwanth 2026-11-06, same band in plain
words). If `style-rules.md` or `workflow-rules.yaml` L09 still mention a
percentage, this word limit wins. Never calculate or report percentages.

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
5. Keep the draft within 300–335 words.
6. **Validate before presenting:**
   ```
   python3 scripts/validate.py --file draft.txt --type cover_letter \
     --sample-avg-words 396 \
     --known-entities "<Company Name>,<other researched company facts/names>"
   ```
   Always pass `--sample-avg-words 396` exactly as written: it is only the
   switch that makes the validator enforce the 300–335 band, not something
   to calculate with. The validator prints the word count; use that number
   and do no further length arithmetic.
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
   clean draft with the validator's word count shown (no percentage).

## Claim guardrails

Same as `cv-tailoring`: German is B1, Libergy workshop was "participated,"
Quantis is "synthesised 7 expert interviews," the P&G test was nationwide,
never discounter-targeted, Hermes never appears. Libergy tender monitoring
covered **16 EU platforms with Google Apps Script** (corrected 2026-11-05,
never "German platforms" or "Power Automate"). See `facts.yaml` for the
full list — a cover letter is prose, not bullets, but the same facts apply.

**EnergyMap** (`evidence/projects.md` section 6) is available as proof of
initiative for energy, data and analytics roles. Lead with the data
explorers, tools and insights rather than the topic map; re-check counts
against the live site; never call the market funnel builder built. Quote
thesis results with the locked thesis figures (70-90% feedstock-dependent,
~32%), not the site's 78% / 31%.