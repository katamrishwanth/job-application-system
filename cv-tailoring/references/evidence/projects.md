# EVIDENCE: Side Projects & Competitions

> Layer: evidence. Not CV copy.
> Linked bullets: N8N-01..03, MUM-01..03, MDY-01

---

# 1. Construction invoice automation (n8n + Ollama)

**Status: top differentiator across every application so far.**

| Field | Value |
|---|---|
| Context | Self-initiated, for the family construction business |
| Stack | Self-hosted n8n + AI agent powered by Ollama cloud models |
| Cost | Entire setup runs free (self-hosted, open-source models) |
| Dates | Add dates when used on a CV, to also address the post-P&G period |

## The problem
Material purchased or received on the construction site is entered into a book
after checking the invoice against the actual material on site. That format is
very difficult to use for any further analysis: which materials cost more across
the whole construction, where costs went beyond budget, and so on.

## The solution
1. The person on site photographs the invoice and sends it in a chat
2. The chat forwards the image to an AI agent
3. The agent processes the data into a Google Sheet
4. The sheet is structured so that every new entry automatically updates KPIs
   and analyses

## Why this is the strongest asset
It is the only item in the profile where Rishwanth saw a broken manual process,
taught himself the tools, and fixed it unpaid. It distinguishes him from
candidates who discuss AI strategy without having built anything. Self-hosting
and using open-source models is a substantive detail: it demonstrates
infrastructure decisions, not just prompt use.

## interview_only
- Why self-hosted rather than a paid API: cost, and data staying local
- The "plumbing not model capability" insight: enterprise AI projects fail on
  integration infrastructure rather than model quality. Directly relevant to
  AI strategy roles.
- Non-coder shipping a working production system used by real people

---

# 2. Museum Mapper (MuMa)

| Field | Value |
|---|---|
| Type | ESCP academic project, Leading Digital Innovation Projects course |
| Date | March 2024 |
| Location | Berlin |
| Team | Group A5: Ketaki Mathur, Nicolas Vissokalis, Rishwanth Katam, Sarah Kouam |

## Problem
Overcrowding in European museums diminishes visitor experience, extends wait
times, reduces enjoyment. Traditional crowd management (time slots, staff) is
ineffective, especially at peak periods.

## Rishwanth's contributions
- **5 primary interviews** with museum staff and visitors: Neue Nationalgalerie
  Berlin, Tour Eiffel Paris, Reichstag Dome Berlin, plus visitor interviews in Paris
- Synthesised into **6 structured insights** using a "persona / want / because /
  but" framework
- Built a **stakeholder map** of the full ecosystem: Museum Visitors, Museum
  Staff, Museum Management, Museums, Curators, Graphic Design Teams, Audio Guide
  Providers, Government & Regulatory Bodies, Hardware Providers, Data Centres
- Defined product objectives and the problem statement
- Created **5 customer personas**: Rita Gupta (tourist), Louise Dubois (local
  visitor), Dan Brown (curator), Anna (museum staff), Louis Leclerc (director)
- Developed **18 user stories** (functional requirements)

## AI / technical specification (co-developed)
- **A\* algorithm:** pathfinding to suggest the optimal route covering all
  desired artworks
- **Graph Neural Network (GNN):** predicts crowd density at each node at any
  given time, outputting **dynamic weights consumed by the A\* algorithm**
- Data requirements mapped: museum graph structure, node features, historical
  crowd density, external factors (time, weather, events), real-time visitor GPS
- Proposed **hierarchical model architecture**: base model + museum-specific
  fine-tuning layer

## App features designed
Personalised itinerary generation (by chosen artworks + duration) | QR code
group sync | interactive map with real-time directions | artwork info pages with
audio guides | WiFi details and facility locations | past visit history

## Data sources mapped
Museum websites (floor plans, artwork lists) | digital collection APIs (e.g.
Rijksmuseum object metadata API) | **BestTime.app** for historical crowd density
(~€9/month) | GPS data from users

## GDPR compliance plan
Transparency, anonymisation, granular opt-out controls.

**Artefacts:** wireframes and click dummy in **Figma**; entity relationship
model in **Miro**.

## interview_only
- The **GNN feeds weights into A\*** rather than the two running separately.
  That interaction is the actual technical idea and is worth explaining.
- The hierarchical architecture (base + per-museum fine-tuning) addresses the
  cold-start problem for a new museum.
- GDPR plan was designed in, not bolted on. Useful for Responsible AI roles.
- €9/month for BestTime.app: the crowd-density data problem was solved by
  buying it rather than collecting it. Pragmatic build-vs-buy call.

---

# 3. Moody's Credit Rating Challenge

| Field | Value |
|---|---|
| Organiser | Moody's Investors Service, Paris |
| Year | 2023 |
| Result | **Winner**, among top French business schools |

Forecasted the financials of a firm to investigate profitability, credit
performance, and liquidity risk; projected demand outlook.

**Placement note:** currently sits in Achievements. If promoted into a Projects
section for a finance-adjacent role, **remove it from Achievements** to avoid
duplication.

---

# 4. Co-Chef (8x Mobile Hackathon)

**Source: LinkedIn post session, not the original candidate profile. Verify
details before first CV use.**

| Field | Value |
|---|---|
| Event | 8x Mobile Hackathon, Berlin |
| Collaborators | Muneeruddin Mohammed (friend, ESCP classmate), Daniele Montemale |
| Context | Rishwanth's first hackathon |

**What it does:** extracts ingredients and steps from cooking videos, provides
voice-guided hands-free cooking instructions, and offers photo-based step
verification.

Not currently on any CV. Worth considering for roles that reward shipping
quickly in a team under time pressure.

---

# 5. Hermes job application agent — DO NOT PUT ON CV

Built custom AI agent skills to run the CV customisation and application
workflow end to end. Documented the exact style, constraints, and rules
Rishwanth follows himself, and built a prompt library for the workflow steps.

**Exclusion reason:** advertising an AI that applies to jobs on your behalf
signals volume applying rather than genuine interest in the specific employer.
This is a credibility risk, not an honesty issue.

**Keep strictly as interview material.** If the capability needs to be visible,
the generic framing is: broke down a repeated manual workflow into documented
rules and a prompt library, then built AI agent skills to run it end to end.

---

## name_dropping (across projects)

**High value:** n8n, Ollama, A\*, Graph Neural Network, Figma, Miro, Moody's.
**Institutional:** Neue Nationalgalerie, Reichstag Dome, Rijksmuseum API.
**Avoid:** naming the family construction business.

## Claim guardrails
- MuMa was a **team project of 4**. Rishwanth owned the research, personas,
  stakeholder mapping and user stories; the AI spec was **co-developed**.
- The MuMa app was **specified and prototyped**, not built and deployed.
- n8n project **is** built and running.
- Co-Chef details need verification before first use.
- Never put Hermes on a CV.
