---
name: jd-recruiter-brief
description: Analyse a job description Rishwanth Katam shares and produce his structured recruiter brief. Trigger whenever he pastes or links a job posting, before any CV or cover letter work — this runs first and its output feeds cv-tailoring.
---

# JD Recruiter Brief — Rishwanth Katam

Runs first, before `cv-tailoring`. Produces the structured brief that CV
tailoring, base selection, and the GO/BORDERLINE/NO-GO call all depend on.

## The prompt

`references/task1-prompt.md` has Rishwanth's Task 1 prompt frozen verbatim,
confirmed word-for-word from the Bain & Company session. Use it as written.
Do not paraphrase or "improve" the six-part structure without his explicit
approval — see `workflow-rules.yaml`'s change_protocol in the cv-tailoring
skill if a change is ever proposed.

## Steps

1. **Web search the company** for context before answering. Every past
   session did this (e.g. found FEV's named Commercial Vehicles practice,
   which made the thesis directly on-topic rather than adjacent).
2. **Answer the six numbered parts** exactly as the frozen prompt specifies.
   **Part 1 renders as two labeled sub-lists** (approved 2026-08-06, see
   `references/task1-prompt.md` addendum): atomic ATS keywords (short,
   exact terms — tools, software, certifications, hard skills) and core
   requirement themes (the fuller JD phrases, kept for fit-gap reasoning
   and bullet-content guidance, never copied verbatim onto the CV).
3. **For part 6 (fit-gap assessment), pull real candidate data — never
   answer from memory of past sessions.** Load, if available in this
   environment:
   - `facts.yaml` (canonical facts, claim locks)
   - `evidence/*.md` and `index/*.facts.json` (full evidence + searchable
     atomic facts, from the `cv-tailoring` skill)

   These files live at `/mnt/skills/user/cv-tailoring/references/` once
   both skills are installed (the convention is
   `/mnt/skills/user/<skill-name>/` — confirm with `ls /mnt/skills/user/`
   if this ever doesn't resolve).
   If `cv-tailoring` isn't enabled or its files aren't reachable, say so
   plainly and ask Rishwanth to confirm both skills are enabled, rather
   than fabricating a fit-gap assessment from memory.
4. **Add the verdict layer** consistently observed across sessions, even
   though it isn't in the frozen prompt's literal text:
   - **GO / BORDERLINE / NO-GO**, with a stated coverage estimate (e.g.
     "GO at approximately 87% must-have coverage"). This threshold is
     **not numerically locked** — reason case-by-case per
     `workflow-rules.yaml`, never apply a silent cutoff.
   - **Primary real-world risk**, stated separately from the fit-gap list.
     Often not a skills gap — German level, seniority mismatch, or a
     perception risk (e.g. overqualification reading as flight risk).
   - **2-3 named anchor experiences** as the strongest fit evidence. This
     selection is what drives which master CV (A/B/C) gets picked next.
5. **German language:** assess factually against `facts.yaml` (locked B1).
   If a role clearly needs more than B1, name that plainly rather than
   softening it — Rishwanth can choose to proceed anyway, but the brief
   should never quietly minimise a real gap.

## Output → handoff to cv-tailoring

Present the brief in the conversation. Do not write it to a file unless
asked. `cv-tailoring`'s workflow checks whether a brief already exists
earlier in the same conversation before doing its own JD analysis — so
running this skill first and this skill only avoids duplicate work.
