# Changelog — Job Application Workflow

The primary hand-written record of every accepted workflow change. Still
written by hand for every change — git version-controls this file, it does not
replace it. One entry per accepted change.
Format: date, what changed, source/reasoning, cost paid, how to revert.

---

## 2026-08-05 — Foundational build

**What:** Built the full system from scratch across one project:
- `facts.yaml` — canonical facts, claim locks, skills bank
- `evidence/*.md` (7 files) — full ground truth per role/project
- `index/*.facts.json` (7 files, 88 atomic facts) — searchable layer,
  including facts with no bullet yet
- `bullet-bank.json` (53 bullets) — cached CV-ready renderings, linked to evidence
- `validate.py` — length, style, claim-lock, and provenance checks
- `workflow-rules.yaml` — mutable process rules, split into locked (Tier 1,
  explicitly confirmed) and inferred (Tier 2, pattern-based, flagged for
  confirmation)

**Why this shape:** Started as a flat bullet bank built from existing CV
bullets. Rishwanth pointed out that indexing only bullets — rather than the
source evidence — meant facts that never became a bullet were permanently
unretrievable (e.g. the Quantis 75+ companies contacted / 5 secured detail).
Rebuilt evidence-first: full prose evidence → atomic fact index → bullet
cache, in that order, so nothing in the original candidate profile is
structurally lost.

**Known fabrication catch during build:** validate.py's provenance check
correctly flagged an invented "3 months" duration in a demo bullet that had
no basis in any evidence file. Kept as selfcheck case 1 in validate.py as a
standing regression test.

**Known gaps flagged, not fixed:**
- `leadership` theme has only 2 facts (both 180DC). This reflects a real gap
  in the underlying experience, not a retrieval problem — do not manufacture
  a third leadership claim to fill it.
- `experimentation` theme has 1 fact (the P&G A/B test). Same caveat.
- PG-F12 (3,000 hrs/year SharePoint saving) and LIB-F17 (Double Diamond
  personas) remain `verified: "check"` pending Rishwanth's confirmation.

**Revert:** no prior version existed; this is the baseline.

---

## 2026-08-06 — Two-tier keyword extraction in jd-recruiter-brief

**What:** `jd-recruiter-brief/references/task1-prompt.md` (addendum, frozen
prompt text itself untouched), `jd-recruiter-brief/SKILL.md` (Part 1 output
format), `workflow-rules.yaml` (new `researched` tier, entry R01).

**Source:** Rishwanth's own hypothesis — that ATS systems match on discrete
keywords, not full JD sentences, so the must-have list should reflect that.

**Corroboration:** 9 general sources on ATS parsing/matching, plus a
DACH-specific search. Consistent pattern held despite several sources having
a commercial incentive in the answer (Jobscan, CareerBldr, and similar sell
resume-optimization products): exact-match weighting concentrates on atomic
terms (tools, software, certifications, hard skills); broader responsibility
sentences are increasingly handled by semantic/NLP matching on modern
platforms, and copying those sentences verbatim is explicitly flagged across
sources as reading poorly to the eventual human reviewer regardless of ATS
behavior.

**DACH check:** no source gave matching-depth specifics for German-market
ATS platforms (Personio, SAP SuccessFactors, Softgarden). Confirmed instead
that BCG Platinion's own careers portal runs on **Avature**, independently
noted elsewhere as favored by consulting firms (Deloitte, KPMG, Bain).
Treated as reasonably transferable, not independently DACH-verified.

**Rejected:** a full switch to atomic keywords only. The fuller JD phrases
are still needed for fit-gap reasoning and to inform what a bullet needs to
prove — retained as a separate labeled list rather than discarded.

**Cost:** two skill files edited. No changes to `facts.yaml` or any
`evidence/*.md` file. No re-editing of already-submitted CVs required.

**Live validation:** tested on the real BCG Platinion "Consultant Energy
Utilities" JD. The atomic list (SAP, Salesforce, Microsoft Dynamics,
Powercloud, SIV, Wilken) made a real evidence gap visible — zero supporting
facts for any named platform — that the full-sentence format had obscured
inside softer language. Directly produced an honest NO-GO verdict rather
than a forced fit, which is the result this check exists to enable.

**Revert:** predates git, so it sits inside the baseline commit and git cannot
isolate it. Restore prior wording of `task1-prompt.md` /
`jd-recruiter-brief/SKILL.md` from this entry if needed.

---

## 2026-08-06 (2) — Primary-source fact verification (RWE/Aurora/VFG letters + source documents)

**What:** Rishwanth supplied the 3 previously-missing reference letters
(RWE, Aurora, VFG) plus 8 primary source documents (thesis docx/xlsx,
defence deck, Libergy Excel model, Quantis report, Handicap International
scoping deck and meeting notes). Read against `facts.yaml` and evidence,
this surfaced real discrepancies in both directions.

**Findings, verified against primary documents, not assumed:**
- Libergy TCO/LCA model covers **7 verticals, not 6** (missing: Industrial,
  Public services) — corrected in `facts.yaml`, `libergy.md`, `LIB-F15`,
  and bullet `LIB-07` (136 chars, was already over the 100-115 range before
  this fix, unrelated pre-existing issue).
- Both the Libergy and thesis Excel models have Breakeven and Sensitivity
  analysis sheets — Rishwanth's own recollection that these were
  thesis-only was backwards. Corrected in `libergy.md`.
- Quantis student team is **6, not 7** (verified from the report's title
  page: Anisha Kaul, Charlotte Zenatelli, Inês Pedro, Rishwanth Katam,
  Thibaud Auzière, Till Meinhardt) — Rishwanth had confirmed "yes, also 7"
  from memory; the primary source overrode that. The 7 that IS correct is
  expert interviews, a different fact entirely.
- **New engagement discovered:** 180DC had 2 projects, not Libergy as
  Rishwanth's message first stated — Handicap International Belgium
  (donor/communications strategy, ~Aug-Dec 2023, Rishwanth as consultant,
  not lead) and the already-documented ESCP carbon-footprint project
  (Rishwanth led). The HI scoping deck's own last slide says "180DC ESCP
  Service Requirements," confirming which organisation it belongs to.
- Thesis defence date corrected: **26 September 2024**, not 2 September.
  Jury: Joe Miemczyk (also supervisor) + Nitheesh Kumar P.

**Cost:** `facts.yaml`, 4 evidence files, 3 index files, `validate.py`
(2 new claim locks, 1 message correction), `bullet-bank.json` (LIB-07 text
corrected). `cover-letter` references updated with the 3 new real letters,
2 of which (RWE, Aurora) are annotated with which specific claims not to
reuse rather than treated as clean templates.

**Open items, not resolved, flagged for Rishwanth:**
- `LIB-04`'s "10 CO2-reporting tools across 6 verticals" — unclear whether
  this "6" is the same (now-corrected-to-7) TCO/LCA vertical count
  mistakenly reused, or a genuinely separate, correct figure for that
  specific whitespace-analysis activity. No primary source confirms either
  way. Not auto-corrected — flagged instead.
- Whether Handicap International should be added as CV content (a new,
  previously-undocumented, nameable nonprofit engagement) is Rishwanth's
  call, not made here.

**Revert:** predates git; sits inside the baseline commit. This entry documents
every changed file.

---

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

---

## 2026-11-05 — EnergyMap added; Libergy tender facts corrected

**What:**
- `evidence/projects.md`: new section 6, EnergyMap (live site, explorers,
  sources, tools, insights, guardrails incl. the thesis-number mismatch).
- `evidence/libergy.md`: tender monitoring now 16 EU platforms via Google
  Apps Script (was 16 German platforms via Power Automate); Tools line too.
- `facts.yaml`: `side_projects.energymap` added; Libergy `tender_monitoring`
  + note added; skills bank gains Google Apps Script (demonstrated); Power
  Automate kept as demonstrated on Rishwanth's confirmation, with a note that
  no work evidence is on file (skills line only); Claude Code note.
- `index/projects.facts.json`: ENM-F01..F09 added (3 marked `verified:
  check` because they are live-site counts).
- `index/libergy.facts.json`: LIB-F13 corrected.
- `bullet-bank.json`: LIB-03 replaced with the corrected 107-char bullet;
  ENM-01 (preferred) and ENM-02 added; counts 53 -> 55.
- `scripts/validate.py`: 3 claim locks (tender wording, funnel builder
  "built", 78%/31% thesis figures as WARN) and 2 selfcheck cases.
- `scripts/build_bank.py`, `scripts/build_index.py`: same edits mirrored so
  a regeneration does not revert them.
- `SKILL.md`: counts updated (111 facts, 55 bullets); 2 claim guardrails.
- cover-letter `SKILL.md` + `references/style-rules.md`: tender correction,
  EnergyMap as a cluster item / candidate anchor for energy and data roles.
- application-qa `SKILL.md`: new step 5, corrected-fact consistency.

**Source:** Rishwanth's direct instructions, 2026-11-04/05 (Linde session):
add EnergyMap to the system in the same structure as other evidence, and
correct the Libergy tender facts to EU platforms and Google Apps Script.
EnergyMap details from his own statements plus the live site read
2026-11-04. These are factual changes, not article-driven workflow changes.

**Corroboration:** n/a for the Libergy correction (primary source is
Rishwanth). EnergyMap counts checked against the live site on 2026-11-04;
flagged `check` because the site keeps changing.

**Rejected:**
- *Putting EnergyMap only in SKILL.md* (proposed earlier the same session).
  The validator only reads evidence/index/facts, so it would have kept
  flagging every EnergyMap term. Superseded by this change.
- *Editing the master CV assets.* They contain no tender bullet. Their
  Power Automate skills entry stays, since Rishwanth confirmed the skill.
- *jd-recruiter-brief changes.* It reads evidence directly; nothing to edit.

**Cost:** 14 files across 3 skills. Two fact files changed (`facts.yaml`,
`evidence/libergy.md`) on Rishwanth's direct correction. CVs that already
said "Google Apps Script" / "EU platforms" were right; the Linde draft that
was switched to "Power Automate / German platforms" on 2026-11-04 needs
switching back.

**Revert:** `git log --oneline --grep="EnergyMap added"`, then `git revert`
that commit.

---

## 2026-11-09 — Browser-first JD retrieval in jd-recruiter-brief

**What:** `jd-recruiter-brief/SKILL.md` only. Added a HARD RULE section and a
new Step 0 ("Get the JD text — browser first, exact URL only"). The frozen
prompt in `references/task1-prompt.md` and Steps 1–5 are unchanged.

**Source:** Live failure, not external advice. On 2026-11-09 (Birkenstock,
Analytics Manager DTC Europe, München) WebFetch returned a "job has been
filled" fallback page for a posting that was live. Claude reported the role
as filled. Rishwanth's browser and Claude's built-in browser both showed the
full live JD on the exact same URL. Rishwanth noted this had happened before.

**Cause:** Server-side fetch tools get no JavaScript and are treated as bots
by many career platforms, which serve a closed/empty fallback page instead of
the JD. The process error was trusting that single fetch result as fact.

**Change:**
- Links are opened in a real browser (built-in browser, else Claude in Chrome)
  before anything else, with up to 3 read attempts while the page renders.
- A closed/expired/not-found result from a fetch tool or search snippet is
  never reported as fact; it means "could not read the page".
- If no browser is reachable and fetch doesn't return the full JD, Claude asks
  Rishwanth to paste the JD instead of calling the role closed.
- No mirrors or similar postings without his explicit OK in chat.
- The brief header states where the JD text came from.

**Corroboration:** change_protocol steps 1–3 (external-source checks) don't
apply; this is an internal bug fix verified by the live incident. Approved
explicitly by Rishwanth in chat, 2026-11-09.

**Rejected:** Using mirror postings (e.g. ZipRecruiter) as a default
fallback. A mirror can be stale or a different version of the role, so it is
allowed only with Rishwanth's explicit OK in chat.

**Cost:** One SKILL.md edit plus this entry. No CVs, facts or evidence files
affected.

**Revert:** `git log --oneline --grep="Browser-first JD retrieval"`, then
`git revert` that commit.

---

## Template for future entries

```
## YYYY-MM-DD — <short title>

**What:** <files touched, one line each>
**Source:** <article/session/direct instruction>
**Corroboration:** <other sources checked, DACH-applicability note>
**Rejected:** <any sub-claims from the source NOT adopted, and why>
**Cost:** <what had to be re-edited>
**Revert:** <find the commit with: git log --oneline --grep="<short title>">
```
