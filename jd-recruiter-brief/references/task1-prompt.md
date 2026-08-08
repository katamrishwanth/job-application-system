# Task 1 prompt — frozen verbatim

This is the exact prompt Rishwanth has used across multiple sessions
(confirmed verbatim in the Bain & Company session, 2026-08-03). Do not
paraphrase or "improve" it without his explicit approval — see
workflow-rules.yaml change_protocol if a change is ever proposed.

---

You are a senior recruiter in Germany specializing in entry-level roles.
Analyze this job description. You can also use the internet to find more
information about the company.

Return a structured brief with:
(1) Top 8 must-have keywords/phrases from the JD — use the company's exact words.
(2) Top 5 nice-to-have skills or experiences.
(3) The tone of the JD (formal/startup/corporate).
(4) Whether German language is required and at what level.
(5) The 1–2 core problems this role is hired to solve.
(6) A fit-gap assessment against the candidate profile & side-projects
    provided in project sources.

<JD>
[pasted job description]
</JD>

---

## Observed additions across sessions (not in the frozen prompt text itself,
## but consistently produced as follow-on output — keep doing these)

- Web search on the company for context before answering (all sessions did
  this; Bain session searched for "AI Insights & Solutions team primary
  research practice"; FEV session searched for the Commercial Vehicles
  practice and found it aligned with the thesis)
- A verdict line: GO / BORDERLINE / NO-GO, with a stated coverage estimate
  (e.g. "GO at approximately 87% must-have coverage" — GO2 Markets session).
  See workflow-rules.yaml: this threshold is NOT numerically locked, reason
  case-by-case and state the % transparently rather than applying an
  unstated cutoff.
- Explicit identification of the primary real-world RISK, separate from the
  fit-gap list — often not a skills gap but something else: German level
  (BASF), seniority mismatch / overqualification (GO2 Markets, BASF), a
  perception risk (BASF: over-qualification read as flight risk given P&G).
- 2-3 "anchor experiences" named explicitly as the strongest fit evidence,
  which then drives which master CV (A/B/C) gets selected as the base.
- German language requirement assessed factually per facts.yaml (B1), but
  when the role clearly needs more, this gets flagged plainly rather than
  minimised (FEV: "flagged as the binding real-world constraint but excluded
  from the formal scoring" — i.e. named, then set aside per Rishwanth's
  explicit instruction for that session, not silently dropped).

---

## Approved refinement — Part 1 output format (2026-08-06)

The frozen prompt text above is unchanged and stays that way. This is a
layered instruction for how to RENDER the answer to Part 1, approved by
Rishwanth after live verification, not an edit to what he originally typed.

**Split Part 1 into two labeled sub-lists instead of one:**

1. **Atomic ATS keywords** — short, exact terms: named tools, software,
   platforms, certifications, systems, hard skills. Pulled unmodified from
   the JD's exact spelling. These are the terms that belong in a CV skills
   section or embedded naturally in a bullet.
2. **Core requirement themes** — the fuller JD phrases/sentences, kept for
   fit-gap reasoning and to inform what a bullet needs to PROVE. Never
   copied verbatim onto the CV — that reads as low-effort to a human
   reviewer and doesn't help on modern semantic-matching ATS anyway.

**Why:** verified via web research (2026-08-06), corroborated across
multiple independent sources despite several having a commercial incentive
in the answer (Jobscan, CareerBldr, and similar sell resume-optimization
products). The consistent pattern: exact-match weighting concentrates on
atomic terms (tools/skills/certs); broader responsibility sentences are
increasingly handled by semantic/NLP matching on modern platforms, and
literal copying of those sentences is explicitly flagged across sources as
reading poorly to the eventual human reviewer.

**DACH check:** no source gave matching-depth specifics for German-market
ATS platforms (Personio, SAP SuccessFactors, Softgarden) specifically.
Confirmed instead that BCG Platinion's own careers portal runs on
**Avature** (visible in their posting URLs), a platform independently
noted as favored by consulting firms including Deloitte, KPMG, and Bain for
custom workflows. Treat the general finding as reasonably transferable but
not independently DACH-verified — worth re-checking if ATS practice moves.

**Live validation:** tested on the real BCG Platinion "Consultant Energy
Utilities" JD. The atomic list (SAP, Salesforce, Microsoft Dynamics,
Powercloud, SIV, Wilken) made an evidence gap visible — zero supporting
facts for any named platform — that the full-sentence version had
obscured inside softer language ("theoretical and practical experience...
e.g."). Directly informed an honest NO-GO verdict rather than a forced fit.

See `workflow-rules.yaml` → `researched_conventions` for the logged version
of this, and `CHANGELOG.md` for the full change record.
