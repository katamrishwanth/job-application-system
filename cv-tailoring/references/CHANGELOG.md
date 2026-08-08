# Changelog — Job Application Workflow

Interim version tracking until git is set up. One entry per accepted change.
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

**Revert:** git not yet set up. Restore prior wording of
`task1-prompt.md` / `jd-recruiter-brief/SKILL.md` from this entry if needed.

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

**Revert:** git not yet set up. This entry documents every changed file.

---

## 2026-08-08 — Git version control, and commit step 8 in change_protocol

**What:** `workflow-rules.yaml` (new `change_protocol` step 8),
`cv-tailoring/SKILL.md` (version-control pointer). New git repo at
`~/Documents/job-application-system/` holding the four job-application skills,
plus `.gitignore`, `GIT_WORKFLOW.md` and `sync-and-commit.sh`. Pushed to a
private GitHub repo (katamrishwanth/job-application-system).

**Source:** Rishwanth's direct instruction. One-time setup, required by this
protocol itself before the first article-driven change can be accepted.

**Corroboration:** n/a — infrastructure change, not an external claim about
hiring practice. No CV content or fact is affected by it.

**Rejected:**
- *Git repo inside the skills folder.* Attempted first, and it failed: the
  Claude app's sync deleted `.git` within ~90 minutes (verified 23:25 on
  2026-08-08, alongside a `manifest.json` rewrite). Ordinary files survived;
  only the repo was removed. Hence the repo lives in `~/Documents/`.
- *A filesystem watcher that auto-commits on change.* It would fire mid-edit,
  producing bursts of meaningless commits, and could not use the CHANGELOG
  entry as its message — which is the whole point of the log. The commit is
  triggered by workflow completion instead (step 8).

**Cost:** 2 skill files edited. No changes to `facts.yaml`, any `evidence/*.md`,
any `index/*.facts.json`, or `bullet-bank.json`. No re-editing of already
submitted CVs. Adds a one-command step to the end of every accepted change.

**Open risk, not resolved:** it is not established that files edited locally
propagate back to the Claude server's copy of these skills. `manifest.json`
records `updatedAt: 2026-08-06T17:54` for cv-tailoring and did *not* change
when these edits were written, which suggests the sync may run server→local
only. If that is so, a future sync could silently revert step 8. Test: open a
new Claude session, invoke cv-tailoring, and ask it to quote step 8 of
change_protocol. Git at least makes any such reversion visible as a diff
rather than silent.

**Revert:** `git revert` the commit carrying this entry, or restore the two
edited files from that commit's parent. The baseline is the Foundational
build commit.

---

## Template for future entries

```
## YYYY-MM-DD — <short title>

**What:** <files touched, one line each>
**Source:** <article/session/direct instruction>
**Corroboration:** <other sources checked, DACH-applicability note>
**Rejected:** <any sub-claims from the source NOT adopted, and why>
**Cost:** <what had to be re-edited>
**Revert:** <git hash once git exists, or "restore <file> from this entry's
  pre-change copy">
```
