---
name: "jd-recruiter-brief"
description: "Analyse a job description Rishwanth Katam shares and produce his structured recruiter brief. Trigger whenever he pastes or links a job posting, before any CV or cover letter work — this runs first and its output feeds cv-tailoring."
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

## HARD RULE — never report a posting as closed from a fetch tool

A web-fetch tool (WebFetch or any server-side HTTP fetch, including curl)
does NOT see what Rishwanth's browser sees. Most career sites (Phenom,
Workday, SuccessFactors, Avature, Personio, Softgarden) build the job
description with JavaScript, and many return a fallback page to non-browser
requests: "job has been filled", "no longer available", "not found", an
empty body, or a redirect to a search page.

**Incident, 2026-11-09 (Birkenstock, Analytics Manager DTC Europe):** WebFetch
returned a "job has been filled" stub for a live posting. Claude reported it
to Rishwanth as filled. The same exact URL, opened in the built-in browser,
showed the full live JD with an Apply button. This had happened before too.

Therefore:
- A "filled / closed / expired / not found / no longer available" result
  from a fetch tool or a search snippet is **never** reported as fact. It is
  treated as "could not read the page", nothing more.
- Only a real browser render of the exact URL (Step 0) can show a posting
  as closed, and even then Claude says what the page showed ("the page shows
  a 'position filled' notice in my browser") and asks Rishwanth to confirm
  on his end. Claude never states "the role has been filled".

## Steps

0. **Get the JD text — browser first, exact URL only.**
   - **If Rishwanth pasted the JD text**, use it. No fetching needed.
   - **If he gave a link**, open that exact URL in a real browser before
     anything else:
     1. Load the `built-in-browser` skill (or `chrome-browser` if the
        built-in browser isn't available), then load its tools.
     2. Open the exact URL (built-in browser: `preview_start` with the URL).
     3. Read it with `get_page_text`. If the text is empty or only shows the
        header, the page is still rendering: wait 2–3 seconds and read again,
        up to 3 attempts, before concluding anything.
     4. Use the JD text from this render as the only source for the brief.
   - **Never substitute a different posting.** Do not use a mirror
     (ZipRecruiter, LinkedIn, Stepstone, aggregators), a similar title, or
     another location's version unless Rishwanth explicitly OKs it in chat.
     If he does, label the brief "JD source: mirror copy, not the employer
     page".
   - **If no real browser is reachable** (tools missing, desktop app
     offline), WebFetch may be tried as a fallback. If it returns the full
     JD, proceed and note "JD read via fetch, not browser" in the brief
     header. If it returns anything else (a closed notice, an empty page, a
     partial page), stop and tell Rishwanth plainly: "I couldn't read the
     posting from here; the page didn't render for my tools. Can you paste
     the JD text?" Do not say or imply the role is closed.
   - **State the JD source in the brief header**, e.g. "JD read from your
     link in the built-in browser".

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