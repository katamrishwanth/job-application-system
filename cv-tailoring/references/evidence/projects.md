# EVIDENCE: Side Projects & Competitions

> Layer: evidence. Not CV copy.
> Linked bullets: N8N-01..03, MUM-01..03, MDY-01, ENM-01..02

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

# 6. EnergyMap (energy & clean-tech market map)

**Added 2026-11-05.** Sources: Rishwanth's own statements, plus the live site
read on 2026-11-04. Counts below are a snapshot of a site that keeps
changing: re-read the site or confirm with Rishwanth before each new CV.

| Field | Value |
|---|---|
| Name | EnergyMap |
| URL | https://energymap-olive.vercel.app/ |
| Context | Self-directed, ongoing side project, built out of enthusiasm for the green energy transition |
| Built with | Claude Code (stated by Rishwanth); hosted on Vercel |
| Status | Live and ongoing |
| Dates | No start date recorded. Ask before putting a date on a CV |
| Scope | Germany first, then Europe, India and Asia (4 focus regions) |

## What it is
A connected, source-backed map of energy and clean-tech markets: how each part
works, what official data shows, and which rules shape it. Every figure links
to its source and a last-checked date.

## Data explorers (CV focus)
4 explorers as of 2026-11-04, 2 of them marked "Live":
- Battery fleet
- Renewable buildout
- India power market and prices
- Power prices with negative hours

## Data sources
- **Marktstammdatenregister (MaStR)**, Bundesnetzagentur, refreshed weekly
- **SMARD**, Bundesnetzagentur, refreshed daily
- **CERC** Market Monitoring Cell monthly reports (India: NLDC, IEX, PXIL, HPX)
- BSW-Solar and Bundesnetzagentur data in the Cloudline model

## Tools
- Interactive **virtual power plant (VPP) funnel chart** with data table:
  German home batteries reachable via manufacturer clouds, 2026 to 2030
  (2.83m home batteries in 2026 rising to 4.88m in 2030; serviceable market
  292k to 1.33m homes; some reach and size shares are stated assumptions)
- **Market funnel builder** based on the Cloudline study: **IN DEVELOPMENT.**
  Never describe it as built until it is live.
- Public roadmap of planned explorers and tools

## Insights (published studies)
2 as of 2026-11-04:
- A virtual power plant market study (Aug 2026), from the Flexa / Cloudline
  case challenge. Realistic 2030 reach of 213k homes, EUR 61 per home per year
- The master's thesis on long-haul trucking (Sep 2024), see `thesis.md`

## Content map (secondary, NOT the CV focus)
3 layers (physical, commercial, rules), 9 domains, 159 topics. Domains:
Generation, Transmission & Distribution, Storage & Flexibility, Consumption,
Carbon Capture & Removal, Markets & Prices, Business Models & Finance,
Policy & Regulation, Carbon & Certificates.

## interview_only
- Non-coder shipping a live, source-backed data product with Claude Code
- Chose official sources (Bundesnetzagentur, CERC) over third-party
  aggregates; every number carries its source and a last-checked date
- Same pattern as n8n and Prajjawala: spot a gap, build the system
- The Carbon Capture & Removal domain is a hook for industrial-gas and CCUS
  employers (e.g. Linde)

## Claim guardrails
- Rishwanth's explicit preference (2026-11-04): the CV line leads with
  **explorers, tools and insights**, not the topic/content map.
- Counts (4 explorers, 2 studies, 159 topics) are snapshots: verify per CV.
- The market funnel builder is in development: never "built".
- The VPP study came from an interview case challenge: describe it as a
  market study, never as paid or client work.
- **Thesis-number mismatch:** the site's thesis insight says HVO cuts
  emissions "by 78%" at about EUR 38 per tonne avoided and BEV costs "31%
  more" for the same freight. The locked thesis evidence is 70-90%
  feedstock-dependent and ~32% (payload normalisation). On the CV and in
  letters, always use the locked thesis figures. When the EnergyMap link is
  on a CV, remind Rishwanth of the mismatch until the site is aligned or he
  confirms 78% is a named base-case scenario.

---

## name_dropping (across projects)

**High value:** n8n, Ollama, A\*, Graph Neural Network, Figma, Miro, Moody's,
Claude Code, MaStR, SMARD (Bundesnetzagentur).
**Institutional:** Neue Nationalgalerie, Reichstag Dome, Rijksmuseum API.
**Avoid:** naming the family construction business.

## Claim guardrails
- MuMa was a **team project of 4**. Rishwanth owned the research, personas,
  stakeholder mapping and user stories; the AI spec was **co-developed**.
- The MuMa app was **specified and prototyped**, not built and deployed.
- n8n project **is** built and running.
- EnergyMap **is** live; its market funnel builder is **not** yet.
- Co-Chef details need verification before first use.
- Never put Hermes on a CV.
