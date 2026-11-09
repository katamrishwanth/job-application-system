# Cover Letter Style Rules

Derived from five full letters (Bain, Detecon, RWE, Aurora, VFG — all in
this folder). Real average length across all five: **396 words**. Use
`--sample-avg-words 396` for the validator unless Rishwanth gives a
different target for a specific application.

**All three older letters (RWE, Aurora, VFG) contain the Libergy "6
industries" error** (should be 7 verticals) — verified against the actual
Excel model 2026-08-06. RWE and Aurora additionally have 2 more errors:

- "A multinational team of 7 students" for Quantis — verified at 6.
- "Leading 2 projects at 180 Degrees Consulting ESCP" — there were 2
  projects, but only 1 was led (ESCP); the other (Handicap International
  Belgium) had Rishwanth as consultant, not lead.

VFG is clean on those last two — no team-size or leadership overstatement
— but still needs the "6 industries" → "7 verticals" fix like the others.

## The four-move structure

Both recovered letters follow the same shape:

1. **Opening.** "I am writing to express my interest in the [role] position
   at [company]." + one sentence positioning (degree + relevant experience
   type) + one sentence on why this specific environment appeals, tied to
   real researched company positioning, not generic praise.
2. **Primary proof point.** One deep story, not several shallow ones. CAR-
   shaped, with a specific number written into the prose naturally ("a 4.2M
   EUR revenue uplift," "a 30 to 80 percent misrepresentation"), closing on
   a reflective one-line reframe — what the achievement taught, not just
   what it produced. ("That project taught me as much about defending a
   method as about running one.")
3. **Second proof point.** A different capability than move 2 — Bain paired
   quantitative (P&G) with qualitative (Quantis); Detecon paired a single
   deep story with a denser paragraph naming several supporting projects
   (n8n, Libergy, 180DC, Quantis) as a "consulting foundation" cluster
   rather than a third full story. Match the density to how much room is
   left after move 2, don't force a second full narrative if it doesn't fit.
   EnergyMap (added 2026-11-05, `evidence/projects.md` section 6) can join
   that cluster for energy, data or analytics roles, framed by its data
   explorers on official sources (MaStR, SMARD) and its published studies.
4. **Why this company.** Two concrete, specific reasons, each tied to a
   real fact from that session's company research — never generic culture
   language. Detecon: Deutsche Telekom/T-Systems backing = real enterprise
   scale; energy/transport practices connect to the thesis. Bain: a stated
   company commitment ("rethinking how primary research is produced")
   connected to a specific personal build project.
5. **Close.** "Thank you for considering my application. I look forward to
   hearing from you." / "Best regards, Rishwanth Katam"

## Salutation rule

If the JD names a contact, address them by first name directly: "Dear
Maja," — standard and better received in Germany than staying formal. Never
guess a surname to construct "Dear Ms. X." If no name is given, use "Dear
Hiring Manager,".

## The anchor swaps by role type — this was an explicit editorial decision

The "usual" opening anchor across several older letters was a Prajjawala
origin story (clean-cooking-fuel access in India), which works for
energy/sustainability-coded roles. For Detecon (an AI/digital strategy
role), that anchor was dropped in favour of a "build-and-advise" opening,
because the sustainability framing would have pulled the letter away from
the actual practice area. **Don't default to one fixed opening anchor
— choose it based on what the role is actually about, and say so if you're
deviating from what a template might suggest.**

For energy-market, data or analytics roles, EnergyMap is a candidate
build-and-advise anchor alongside n8n: a live tool built on official energy
data, which shows both the domain interest and the ability to ship.

## Length

Target 75-85% of the average length of Rishwanth's own sample letters (see
`workflow-rules.yaml` L09). If Rishwanth specifies a different percentage
for a specific session (he asked for 85-90% once, for Detecon), treat that
as a one-off override for that application, not a change to the locked
default.

## Honesty on requested omissions

When asked to leave something material out (e.g. German language level),
state the real risk once, plainly, then respect the decision without
relitigating it in every subsequent turn. Example, from the Detecon session:
noting that the JD's "very good German" requirement makes its absence from
an otherwise thorough letter "the kind of gap a recruiter reads as an
answer" — said once, then dropped.

## Sign-off varies

"Regards," (RWE), "Best regards," (Aurora, VFG, Bain), "Best regards,"
(Detecon) — "Best regards" is the more common default; "Regards" alone
isn't wrong, just slightly more clipped.

## Optional availability line

RWE's letter includes "I am available to start at your earliest
convenience" in the opening paragraph. This is optional, not part of the
core structure — include only where the JD or role signals urgency, not
as a default addition.

## Mechanical rules (shared with CV bullets)

No em-dashes. No invented facts or numbers — every number and every claim
about Rishwanth must trace to `facts.yaml` or `evidence/*.md`. Company facts
(researched that session) are a separate, legitimate category — see
`SKILL.md` for how `validate.py --type cover_letter` handles this via
`--known-entities`.
