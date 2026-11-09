# -*- coding: utf-8 -*-
"""
Builds bullet-bank.json from every bullet found across:
  - Master_CV_A_Commercial_Analytics.docx
  - Master_CV_B_Sustainability.docx
  - Master_CV_C_Strategy_BizDev.docx
  - The 4 customised sample CVs (A, B, C, VFG)
  - Rishwanth's candidate profile (raw detail not yet on any CV)

Character counts are COMPUTED, never asserted.
"""
import json, re, unicodedata

WORK_RANGE = (100, 115)
PROJ_RANGE = (120, 130)

# type: work | thesis | project
# verified: True = fact confirmed in facts.yaml or candidate profile
#           "check" = needs Rishwanth to confirm before use
B = []

def add(id, role, text, type, themes, metric=None, source=None,
        verified=True, notes=None):
    B.append(dict(id=id, role=role, text=text, type=type, themes=themes,
                  metric=metric, source=source, verified=verified, notes=notes))

# ---------------------------------------------------------------- P&G
add("PG-01", "pg",
    "Ran nationwide YT ad frequency A/B test; attributed +€4.2M revenue uplift and shaped media investment priorities for OND 2025.",
    "work", ["experimentation", "analytics", "commercial"],
    "+€4.2M revenue uplift", "CV-A",
    notes="Strongest single metric. Nationwide YouTube frequency test, NOT discounter-targeted.")
add("PG-02", "pg",
    "Diagnosed Always Discreet discounter gap via ABC analysis + store visit mapping; recommended SKU addition with est. +€1–2M NOS upside.",
    "work", ["analytics", "strategy", "commercial"],
    "est. +€1-2M NOS upside", "CV-A")
add("PG-03", "pg",
    "Executed behavioural consumer survey (3-panel targeting) to map purchase drivers; surfaced affinity-index whitespace opportunities at Lidl.",
    "work", ["market_research", "analytics"], None, "CV-A")
add("PG-04", "pg",
    "Rebuilt discounter sellout data model with Nielsen + DevOps teams; corrected 30–80% misrepresentation in business KPIs across DACH.",
    "work", ["data_infrastructure", "analytics", "stakeholder_management"],
    "30-80% KPI misrepresentation corrected", "CV-A")
add("PG-05", "pg",
    "Mapped and restructured DACH analytics toolset across 8+ data sources; saved est. 720 hrs/year by improving tool accessibility.",
    "work", ["data_infrastructure", "project_management"],
    "est. 720 hrs/year saved", "CV-A")
add("PG-06", "pg",
    "Diagnosed discounter performance gap; built recommendation deck with assortment, promo, and in-store execution measures for Lidl and Aldi.",
    "work", ["analytics", "strategy", "communication"], None, "CV-C")
add("PG-07", "pg",
    "Mapped analytics tool needs across commercial functions via 1:1 interviews; restructured A&I Hub saving est. 720 hrs/year organisation-wide.",
    "work", ["data_infrastructure", "stakeholder_management"],
    "est. 720 hrs/year saved", "CV-C")
add("PG-08", "pg",
    "Delivered NielsenIQ, YouGov, and Kantar-based consumer insights across DACH categories; shaped discounter channel strategy for key brands.",
    "work", ["market_research", "strategy"], None, "CV-B")
add("PG-09", "pg",
    "Mapped cross-functional data needs via 1:1s, supporting internal programs to improve productivity & efficiency.",
    "work", ["project_management", "stakeholder_management"], None, "sample-VFG")
add("PG-10", "pg",
    "Translated business needs into tech requirements for DevOps, enabling structured cross-functional execution.",
    "work", ["data_infrastructure", "stakeholder_management", "project_management"],
    None, "sample-VFG")
add("PG-11", "pg",
    "Kept senior stakeholders updated and delivered on time, ensuring progress tracking against business targets.",
    "work", ["project_management", "stakeholder_management"], None, "sample-VFG")
add("PG-12", "pg",
    "Conducted quantitative analyses across categories and developed presentations for brand strategy decisions.",
    "work", ["analytics", "communication"], None, "sample-B")
add("PG-13", "pg",
    "Delivered full cashback promo analysis in 1 day under deadline pressure; identified key outcomes and survey design improvements.",
    "work", ["analytics", "commercial"], None, "profile",
    notes="From profile (BP Cashback). Not yet on any CV. Good for 'works at pace' signals.")
add("PG-14", "pg",
    "Built Paper COT SharePoint hub with buy-in from BabyCare and FemCare functions; foundation set to save est. 3,000 hrs/year.",
    "work", ["data_infrastructure", "stakeholder_management"],
    "est. 3,000 hrs/year (foundation only)", "profile",
    verified="check",
    notes="CAUTION: profile states the 3,000 hrs/year saving was NOT yet delivered, only the foundation set up. Phrase as foundation, never as delivered saving. Confirm before use.")

# ---------------------------------------------------------------- Libergy
add("LIB-01", "libergy",
    "Priced biofuel product by modelling full value chain costs vs. carbon certificate benchmarks; defined competitive price band for B2B sales.",
    "work", ["pricing", "commercial", "strategy"], None, "CV-A")
add("LIB-02", "libergy",
    "Built no-code B2B dashboard (Bubble) covering fuel orders, GHG tracking, CSRD reporting, and automated invoice and certificate provision.",
    "work", ["product", "sustainability", "automation"], None, "CV-A",
    notes="B2B platform, not consumer-facing. Keep that distinction.")
add("LIB-03", "libergy",
    # Corrected 2026-11-05 (Rishwanth): Google Apps Script, EU platforms.
    "Automated tender monitoring across 16 EU platforms via Google Apps Script and documented the process guide.",
    "work", ["automation", "commercial"], "16 platforms", "CV-A")
add("LIB-04", "libergy",
    "Conducted whitespace analysis and benchmarked 10 CO2-reporting tools across 6 verticals to shape go-to-market priorities.",
    "work", ["strategy", "market_research", "sustainability"],
    "10 tools, 6 verticals", "CV-A")
add("LIB-05", "libergy",
    "Built B2B sales pitch deck covering storyboard, digital product positioning, and CTA for clean-fuel customer acquisition.",
    "work", ["communication", "commercial", "strategy"], None, "CV-A")
add("LIB-06", "libergy",
    "Researched EU climate regulations (RED II, EU ETS, BEHG, CSRD); built biofuel compliance tool and education deck for B2B clean-fuel clients.",
    "work", ["regulation", "sustainability", "product"], None, "CV-B")
add("LIB-07", "libergy",
    "Built TCO/LCA model across 6 industries to quantify biofuel GHG/cost trade-offs vs. diesel; outputs used directly in B2B sales decisions.",
    "work", ["sustainability", "analytics", "commercial"], "6 industries", "CV-B")
add("LIB-08", "libergy",
    "Researched GLEC 3.0 transport GHG accounting standards; aligned product methodology with international carbon reporting norms.",
    "work", ["regulation", "sustainability", "product"], None, "CV-B")
add("LIB-09", "libergy",
    "Represented Libergy at 70-person green energy summit; engaged decision-makers and panellists on Europe's sustainable energy transition.",
    "work", ["communication", "commercial"], "70 attendees", "CV-B")
add("LIB-10", "libergy",
    "Conducted competitor analysis across product, customer, and geographic dimensions; shaped go-to-market priorities for clean-fuel B2B market.",
    "work", ["strategy", "market_research"], None, "CV-C")
add("LIB-11", "libergy",
    "Contributed to 2-day lean canvas workshop defining USP and customer segmentation; shaped roadmap for 3 new product and service offerings.",
    "work", ["strategy", "product"], "3 new offerings", "CV-C (rewritten)",
    notes="REWRITTEN. Original CV-C said 'Led 2-day lean canvas workshop'. facts.yaml locks this as 'participated'. Use 'contributed to' / 'participated in', never 'led'.")
add("LIB-12", "libergy",
    "Built CSRD reporting module inside the platform, turning regulation into guided questions and a generated compliance report.",
    "work", ["regulation", "sustainability", "product"], None, "profile",
    notes="Strongest Libergy proof point for ESG/regulatory roles. Mechanism-led framing (regulation in, report out).")
add("LIB-13", "libergy",
    "Defined user personas and product objectives via Double Diamond design process to shape the B2B platform roadmap.",
    "work", ["product", "market_research"], None, "profile", verified="check")

# ---------------------------------------------------------------- 180DC
add("180-01", "consulting_180dc",
    "Led a 6-person team delivering carbon impact recommendations, aligning stakeholders through analysis.",
    "work", ["leadership", "sustainability", "stakeholder_management"],
    "6-person team", "CV-A/B",
    notes="The ONE genuine leadership claim. Spend leadership signalling here, not on Libergy.")
add("180-02", "consulting_180dc",
    "Owned project scoping, client check-ins, & final delivery, maintaining cadence, risks, & decisions for execution.",
    "work", ["project_management", "stakeholder_management"], None, "CV-A/B")
add("180-03", "consulting_180dc",
    "Fostered team culture through streamlined coordination across countries, functions, and time zones.",
    "work", ["leadership", "project_management"], None, "CV-A/B")
add("180-04", "consulting_180dc",
    "Mapped student carbon footprint across 5 European campuses; prioritised interventions by impact vs. effort across mobility, food, and commute.",
    "work", ["sustainability", "strategy", "analytics"], "5 campuses", "CV-A/B")
add("180-05", "consulting_180dc",
    "Benchmarked train vs. flight cost and emissions on 3 inter-campus routes; identified Paris–London as the most viable green travel shift.",
    "work", ["analytics", "sustainability"], "3 routes", "CV-A/B")
add("180-06", "consulting_180dc",
    "Evaluated partnerships across 5 country campuses; delivered vendor recommendations with cost estimates and phased implementation guidance.",
    "work", ["strategy", "commercial"], "5 campuses", "CV-B/C")
add("180-07", "consulting_180dc",
    "Converted research findings into board-ready strategy recommendations; influenced sustainability partnership decisions across 5 campuses.",
    "work", ["communication", "strategy"], "5 campuses", "CV-A")

# ---------------------------------------------------------------- Quantis
add("QNT-01", "quantis",
    "Synthesised 7 expert interviews with Adidas, The North Face and Vibram into a diagnostic framework for circular business models",
    "project", ["market_research", "sustainability", "strategy"],
    "7 expert interviews", "BASF chat",
    notes="PREFERRED wording. 'expert interviews' is the locked framing (5 companies + 2 industry experts incl. OECD). Never 'conducted 7 company interviews'.")
add("QNT-02", "quantis",
    "Diagnosed circular business model barriers in fashion and sports; synthesised 7 expert interviews into a structured framework.",
    "work", ["market_research", "sustainability", "strategy"],
    "7 expert interviews", "CV-A/C (corrected)",
    notes="Original said 'senior interviews' — corrected to 'expert'.")
add("QNT-03", "quantis",
    "Developed diagnostic framework mapping value proposition, activities, and stakeholder factors driving circular model success.",
    "work", ["strategy", "sustainability"], None, "CV-B")
add("QNT-04", "quantis",
    "Conducted qualitative research and synthesised 7 expert interviews to identify circular business model barriers.",
    "work", ["market_research", "sustainability"], "7 expert interviews", "sample-B")

# ---------------------------------------------------------------- Prajjawala
add("PRJ-01", "prajjawala",
    "Developed investment case quantifying ₹386B industry inefficiency; secured ₹1M seed funding through data-driven pitch to angel investors.",
    "work", ["commercial", "strategy", "communication"],
    "₹386B sized, ₹1M raised", "CV-A/C")
add("PRJ-02", "prajjawala",
    "Built IoT supply chain MVP using real-time consumption data; automated demand forecasting and reduced LPG inefficiency by 58%.",
    "work", ["product", "analytics", "automation"], "58% inefficiency reduction", "CV-A/C")
add("PRJ-03", "prajjawala",
    "Built IoT-based supply chain MVP for a green energy startup; cut inventory inefficiency 58% and secured ₹1M seed funding.",
    "work", ["product", "commercial", "analytics"],
    "58%, ₹1M", "CV-B (merged)",
    notes="Use when Prajjawala is compressed to a single line.")

# ---------------------------------------------------------------- Thesis
add("THS-01", "thesis",
    "Built a 5-year TCO model for Diesel, HVO, and BEV long-haul HDVs, supporting strategic fuel-pathway decisions.",
    "thesis", ["sustainability", "analytics"], "5-year model, 3 pathways", "sample-C")
add("THS-02", "thesis",
    "Conducted LCA across 3 fuel pathways, modelling lifecycle GHG/km with EU ETS sensitivity for decisions made.",
    "thesis", ["sustainability", "analytics", "regulation"], "3 pathways", "sample-C")
add("THS-03", "thesis",
    "Identified HVO as viable short term and BEV superior long term as costs fall and grids decarbonise in Germany.",
    "thesis", ["sustainability", "strategy"], None, "sample-C")
add("THS-04", "thesis",
    "Built 5-year TCO model covering vehicle, energy, and infrastructure costs for German long-haul fleet operators.",
    "thesis", ["sustainability", "analytics"], None, "CV-B")
add("THS-05", "thesis",
    "Modelled EU ETS sensitivity in a 5-year TCO/LCA analysis, supporting structured sustainability investment decisions.",
    "thesis", ["sustainability", "regulation", "analytics"], None, "sample-B")

# ---------------------------------------------------------------- Projects
add("N8N-01", "n8n_automation",
    "Site material data sat in handwritten books, blocking cost analysis; built a self-hosted n8n and AI agent workflow to digitise it",
    "project", ["automation", "ai_ml", "data_infrastructure"], None, "BASF chat",
    notes="Top differentiator across every application so far. Lead the projects section with this.")
add("N8N-02", "n8n_automation",
    "Invoice photos sent in a chat are now parsed into a Google Sheet where cost and material KPIs refresh with every new entry",
    "project", ["automation", "ai_ml", "analytics"], None, "BASF chat")
add("N8N-03", "n8n_automation",
    "Self-hosted the full stack on Ollama open-source models, running the entire automation at zero recurring software cost",
    "project", ["automation", "ai_ml"], "zero recurring cost", "profile")
add("MUM-01", "muma",
    "Interviewed 5 museum staff and visitors on overcrowding; synthesised 6 insights and mapped every stakeholder in the ecosystem",
    "project", ["market_research", "product"], "5 interviews, 6 insights", "BASF chat")
add("MUM-02", "muma",
    "Translated those insights into 18 user stories and applied A* and GNN route optimisation to improve visitor flow and experience",
    "project", ["ai_ml", "product"], "18 user stories", "BASF chat")
add("MUM-03", "muma",
    "Specified a GDPR compliance plan covering transparency, anonymisation and granular opt-out for all visitor location data",
    "project", ["ai_ml", "regulation", "product"], None, "profile",
    notes="Use for roles touching Responsible AI or data governance.")
add("MDY-01", "moodys",
    "Forecasted firm financials to assess profitability, credit performance and liquidity risk; won against top French schools",
    "project", ["analytics", "commercial"], None, "sample-A",
    notes="If promoted to Projects, REMOVE from Achievements to avoid duplication.")

# Added 2026-11-05: EnergyMap (evidence/projects.md section 6)
add("ENM-01", "energymap",
    "Built 4 data explorers on MaStR, SMARD and CERC data, from battery fleets to negative prices; published 2 market insight studies.",
    "project", ["data_infrastructure", "analytics", "sustainability", "ai_ml"], None, "Linde CV 2026-11-04",
    notes="Preferred. Counts are a site snapshot; re-check per CV.")
add("ENM-02", "energymap",
    "Built live explorers on MaStR and SMARD data for battery fleets and negative power prices; published source-backed market studies.",
    "project", ["data_infrastructure", "analytics", "sustainability", "ai_ml"], None, "Linde CV 2026-11-04",
    notes="Alternative without counts.")

# ================================================================ emit
EM_DASH = "\u2014"
out = []
for b in B:
    t = b["text"]
    n = len(t)
    lo, hi = PROJ_RANGE if b["type"] == "project" else WORK_RANGE
    b2 = dict(b)
    b2["chars"] = n
    b2["target_range"] = [lo, hi]
    b2["in_range"] = lo <= n <= hi
    b2["over_by"] = n - hi if n > hi else 0
    b2["under_by"] = lo - n if n < lo else 0
    b2["has_em_dash"] = EM_DASH in t
    out.append(b2)

bank = {
    "meta": {
        "owner": "Rishwanth Katam",
        "generated": "2026-08-05",
        "source_of_truth": "facts.yaml",
        "counts": {
            "total": len(out),
            "in_range": sum(1 for b in out if b["in_range"]),
            "needs_trim": sum(1 for b in out if b["over_by"] > 0),
            "needs_pad": sum(1 for b in out if b["under_by"] > 0),
            "unverified": sum(1 for b in out if b["verified"] != True),
        },
        "usage": "Select by role + theme overlap with JD, then trim/pad to target_range. Never invent; if no bullet fits, say so.",
    },
    "theme_taxonomy": [
        "analytics", "experimentation", "market_research", "strategy", "pricing",
        "commercial", "sustainability", "regulation", "automation", "ai_ml",
        "data_infrastructure", "product", "stakeholder_management", "leadership",
        "project_management", "communication",
    ],
    "bullets": out,
}

with open("/home/claude/bullet-bank.json", "w", encoding="utf-8") as f:
    json.dump(bank, f, ensure_ascii=False, indent=2)

# ---- report
print(f"TOTAL {len(out)}  in-range {bank['meta']['counts']['in_range']}  "
      f"trim {bank['meta']['counts']['needs_trim']}  "
      f"pad {bank['meta']['counts']['needs_pad']}")
print()
roles = {}
for b in out:
    roles.setdefault(b["role"], []).append(b)
for r, bs in roles.items():
    print(f"--- {r} ({len(bs)})")
    for b in bs:
        flag = "OK  " if b["in_range"] else (f"+{b['over_by']:<3}" if b["over_by"] else f"-{b['under_by']:<3}")
        em = " [EM-DASH]" if b["has_em_dash"] else ""
        v = "" if b["verified"] is True else "  [VERIFY]"
        print(f"  {b['id']:<7} {b['chars']:>3} {flag}{em}{v}")
