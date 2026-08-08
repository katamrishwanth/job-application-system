# EVIDENCE: Master's Thesis — Decarbonising Long-Haul Trucking

> Layer: evidence. Not CV copy.
> Linked bullets: THS-01 through THS-05

## Engagement facts

| Field | Value |
|---|---|
| Full title | "Decarbonising Long-Haul Trucking in Germany: A Comparative TCO and LCA Analysis of Diesel, HVO, and Battery Electric Vehicles" |
| Short title (CV) | "Decarbonising Long-Haul Trucking in Germany: Comparison of Diesel, HVO, & Electric" |
| Institution | ESCP Business School |
| Dates | 2024 (LOCKED — defended 26 September 2024, corrected 2026-08-06 from an earlier wrong "2 Sep" note, verified against the defence deck) |
| Supervisor | Joe Miemczyk |
| Jury | Joe Miemczyk (jury member 1, also supervisor), Nitheesh Kumar P. (jury member 2) |
| Built in | **Excel** (multi-scenario model, self-built). NOT Python. |
| Scope | 5-year vehicle lifetime, German long-haul operators, geographic scope Germany |

## TCO model components
- **CAPEX:** vehicle, battery, infrastructure
- **OPEX:** energy, insurance, taxes, tolls, maintenance
- **Performance normalisation for BEVs** (see technical contributions below)

## LCA model components
- Vehicle production emissions
- Energy consumption emissions (tank-to-wheel and well-to-wheel)
- Infrastructure lifecycle emissions

## Sensitivity analyses run
- **TCO side:** diesel price, electricity price, battery cost
- **LCA side:** electricity grid mix, feedstock source, battery technology

## Key finding
- **HVO is the viable short-term decarbonisation solution.** Same vehicle, same
  infrastructure, **70–90% GHG reduction depending on feedstock**.
- **BEV is superior long-term** as battery costs fall and the German electricity
  grid decarbonises.

## Regulatory context modelled
- EU ETS carbon pricing
- RED II biofuel targets
- European HDV CO2 Standards
- German **Gesamtkonzept Klimafreundliche Nutzfahrzeuge** (€1.6B government
  grant scheme)

## Notable technical contributions
- **BEV performance normalisation to maximum payload capacity**, which adds
  **~32% to BEV CAPEX/OPEX**. This is the methodological contribution most
  worth defending in interview: without it, BEV/diesel comparisons are not
  like-for-like, because a BEV carrying less payload does less work.
- **Infrastructure guesstimate methodology** for charging vs. refuelling stations
- Battery cost adds **~23% to BEV TCO vs. diesel**

## name_dropping

**High value for mobility, automotive, and energy roles:** HVO, BEV, TCO, LCA,
EU ETS, RED II, HDV CO2 Standards, well-to-wheel / tank-to-wheel.

**Gesamtkonzept Klimafreundliche Nutzfahrzeuge:** naming the German grant
scheme in German signals genuine engagement with the German policy landscape,
which offsets the language question for German employers. Use where relevant.

**FEV Consulting precedent:** FEV runs a named Commercial Vehicles practice and
publishes truck TCO analyses. Any employer with a commercial-vehicle practice
makes this thesis directly on-topic, not merely adjacent.

## interview_only

- **The payload normalisation insight.** Most people comparing BEV and diesel
  trucks compare vehicle to vehicle. Normalising to payload capacity is the
  correct unit of comparison and changes the answer by ~32%. This is the single
  most technically impressive thing in the profile and it is not on any CV.
- **The finding is genuinely two-part and time-dependent** (HVO now, BEV later),
  not a single-answer conclusion. Shows comfort with conditional recommendations.
- Built entirely in Excel with no external model. Defensible line by line.
- Sensitivity design: six variables split across cost and emissions sides.

## Claim guardrails

- Dates are **2024**, not 2025. See facts.yaml for the full reasoning.
- Built in **Excel**, not Python. Do not imply a programmatic model.
- 70–90% GHG reduction is **feedstock-dependent**. Never state as a flat figure.
- ~32% and ~23% are modelled outputs, always keep the tilde.
- This is a master's thesis, an academic work product. It can sit under
  Education or as its own section, but never inside Work Experience as if paid.
