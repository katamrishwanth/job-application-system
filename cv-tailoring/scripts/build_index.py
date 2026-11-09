# -*- coding: utf-8 -*-
"""Emits per-role facts index files. Every fact traceable to an evidence file."""
import json, os
from collections import Counter

F = []
def f(id, role, fact, tags, has_bullet=None, cv_suitable=True,
      source=None, verified=True, notes=None):
    F.append(dict(id=id, role=role, fact=fact, tags=tags, has_bullet=has_bullet,
                  cv_suitable=cv_suitable, source=source, verified=verified,
                  notes=notes))

# ================================================================ P&G
f("PG-F01","pg","Ran nationwide long-form YouTube ad frequency A/B test; unlocked EUR 4.2M SOP potential for BabyCare",
  ["experimentation","analytics","media","commercial"],"PG-01",True,"pg.md#project-3")
f("PG-F02","pg","Pushed the team to wait for a more conclusive bin selection rather than proceed prematurely",
  ["judgment","rigour","stakeholder_management","disagreement"],None,False,"pg.md#project-3",
  notes="Best 'time you disagreed with a team' answer available. Interview only.")
f("PG-F03","pg","Upskilled in basic Python and MS Azure in a short timeframe to run the Test & Control analysis",
  ["learning_agility","technical"],None,True,"pg.md#project-3")
f("PG-F04","pg","Documented and handed over post-analysis to a colleague with structured detail",
  ["documentation","handover","project_management"],None,True,"pg.md#project-3")
f("PG-F05","pg","Coordinated 5 named Nielsen contacts across POD data, historical mapping, methodology, coverage and delivery",
  ["vendor_management","stakeholder_management","data_infrastructure"],None,True,"pg.md#project-2")
f("PG-F06","pg","Collaborated with the DevOps team at Lingaro Group in Poland; proposed 2 implementation approaches",
  ["vendor_management","data_infrastructure","technical_translation"],"PG-10",True,"pg.md#project-2")
f("PG-F07","pg","Negotiated with Nielsen to maximise data access within timeline constraints",
  ["negotiation","vendor_management","commercial"],None,True,"pg.md#project-2")
f("PG-F08","pg","Corrected 30-80% under/over-representation in discounter sellout data across DACH",
  ["data_infrastructure","analytics","data_quality"],"PG-04",True,"pg.md#project-2")
f("PG-F09","pg","Configured data in OctoPaGe and Axon with MM team and Seven Seven Global Services to prevent data misuse",
  ["data_governance","data_infrastructure","vendor_management"],None,True,"pg.md#project-2")
f("PG-F10","pg","Mapped tool needs via 1:1 interviews across functions; restructured A&I Hub for est. 720 hrs/year saving",
  ["stakeholder_management","data_infrastructure","process_improvement"],"PG-05",True,"pg.md#project-2")
f("PG-F11","pg","Proposed a chat assistant to help users select the right analytics tool, scoped post-Copilot rollout",
  ["ai_ml","product","process_improvement"],None,True,"pg.md#project-2",
  notes="Only P&G fact touching AI product thinking. Valuable for AI strategy roles.")
f("PG-F12","pg","Built Paper COT SharePoint hub with buy-in from BabyCare and FemCare; foundation est. 3,000 hrs/year",
  ["stakeholder_management","data_infrastructure"],"PG-14",True,"pg.md#project-2",
  verified="check", notes="Saving NOT delivered, foundation only. Phrase accordingly.")
f("PG-F13","pg","Found the ABC Assortment Booster tool's limitations and re-ran the full analysis from scratch",
  ["rigour","judgment","analytics"],None,False,"pg.md#project-1",
  notes="Shows not trusting tool output blindly. Interview only.")
f("PG-F14","pg","Manually mapped every private label SKU using FastMart data, store visits and desk research",
  ["analytics","fieldwork","persistence"],None,True,"pg.md#project-1")
f("PG-F15","pg","Recommended adding the Ultimate Night size to discounter shelf range; est. +EUR 1-2M NOS upside",
  ["analytics","commercial","category_management"],"PG-02",True,"pg.md#project-1")
f("PG-F16","pg","Used all 3 behavioural purchase constraints for survey targeting, the most sophisticated use of the panel",
  ["market_research","survey_design"],"PG-03",True,"pg.md#project-1")
f("PG-F17","pg","Proactively proposed a dummy survey first to preview quality before full execution",
  ["rigour","survey_design","initiative"],None,False,"pg.md#project-1",
  notes="Shows anticipating quality risk. Interview only.")
f("PG-F18","pg","Found affinity-index opportunity capturing drug store private label buyers at Lidl",
  ["market_research","analytics","commercial"],"PG-03",True,"pg.md#project-1")
f("PG-F19","pg","Identified 55+ competitor brand loyalists as an awareness-driven acquisition opportunity",
  ["market_research","segmentation","commercial"],None,True,"pg.md#project-1")
f("PG-F20","pg","Self-upskilled on brand building via How Brands Grow; applied double jeopardy law to frame recommendations",
  ["learning_agility","brand_strategy","market_research"],None,False,"pg.md#project-1",
  notes="Independent learning applied to real work. Strong interview material.")
f("PG-F21","pg","Delivered a full cashback promo analysis in 1 day under deadline pressure",
  ["pace","analytics","commercial"],"PG-13",True,"pg.md#project-3")
f("PG-F22","pg","Learned to push teams to define the decision they are making, not just the analysis they request",
  ["consulting","stakeholder_management","judgment"],None,False,"pg.md#project-3",
  notes="Most consulting-relevant lesson from the internship. Interview only.")
f("PG-F23","pg","Drove optimisation of promo plan and quota pack size benefits at a key account",
  ["commercial","analytics"],None,True,"pg.md#project-3")
f("PG-F24","pg","Delivered NielsenIQ, YouGov and Kantar market intelligence shaping DACH discounter channel strategy",
  ["market_research","strategy"],"PG-08",True,"pg.md#tools-used")
f("PG-F25","pg","Prepared the first market and shopper data insights for a Lidl customer meeting, reused for Aldi",
  ["market_research","communication","commercial"],"PG-06",True,"pg.md#project-1")

# ================================================================ Libergy
f("LIB-F01","libergy","Built CSRD compliance module inside the platform: customer inputs details, platform generates the report",
  ["regulation","product","sustainability","automation"],"LIB-12",True,"libergy.md#csrd-specifically",
  notes="Strongest Libergy asset for ESG and regtech roles.")
f("LIB-F02","libergy","Identified CSRD as the most pressing customer regulatory need among 6 regulations researched",
  ["regulation","commercial","prioritisation"],None,True,"libergy.md#csrd-specifically")
f("LIB-F03","libergy","Researched CSRD implementation timelines differing by company size: large, SME, listed SME",
  ["regulation","sustainability"],None,True,"libergy.md#csrd-specifically")
f("LIB-F04","libergy","Researched RED II targets: 32% renewable by 2030, 14% transport sub-target, 3.5% advanced biofuels",
  ["regulation","sustainability","policy"],None,True,"libergy.md#regulatory-research")
f("LIB-F05","libergy","Researched EU ETS, BEHG, nEHS and EED alongside RED II and CSRD",
  ["regulation","sustainability","policy"],"LIB-06",True,"libergy.md#regulatory-research")
f("LIB-F06","libergy","Researched GLEC 3.0 transport GHG accounting and aligned product methodology to it",
  ["regulation","sustainability","product"],"LIB-08",True,"libergy.md#glec-30-research")
f("LIB-F07","libergy","Priced biofuel by benchmarking premium over diesel against carbon certificate cost for equivalent reduction",
  ["pricing","commercial","strategy"],"LIB-01",True,"libergy.md#pricing-model",
  notes="Elegant, explainable pricing logic. Good whiteboard answer.")
f("LIB-F08","libergy","Decomposed the full biofuel value chain and summed cost contributions at each stage",
  ["pricing","analytics","supply_chain"],None,True,"libergy.md#pricing-model")
f("LIB-F09","libergy","Self-taught Bubble and built a B2B customer-facing platform from scratch as a non-coder",
  ["product","no_code","learning_agility"],"LIB-02",True,"libergy.md#digital-platform")
f("LIB-F10","libergy","Built scope 3 allocation feature distributing emissions savings to downstream customers",
  ["sustainability","product","regulation"],None,True,"libergy.md#digital-platform")
f("LIB-F11","libergy","Automated invoicing and sustainability certificate provision inside the platform",
  ["automation","product"],"LIB-02",True,"libergy.md#digital-platform")
f("LIB-F12","libergy","Benchmarked CO2 reporting tools of 10 companies to inform product design",
  ["market_research","product","sustainability"],"LIB-04",True,"libergy.md#digital-platform")
# Corrected 2026-11-05 (Rishwanth): Google Apps Script, EU platforms.
f("LIB-F13","libergy","Automated tender monitoring across 16 EU platforms using Google Apps Script and CPV code filters",
  ["automation","commercial","public_sector"],"LIB-03",True,"libergy.md#tender-monitoring-automation")
f("LIB-F14","libergy","Documented handling logic per inbound channel and wrote a process guide for tender monitoring",
  ["documentation","process_improvement","automation"],None,True,"libergy.md#tender-monitoring-automation")
f("LIB-F15","libergy","Built TCO/LCA model across 6 industries: logistics, construction, agriculture, waste, public transport, freight",
  ["sustainability","analytics","commercial"],"LIB-07",True,"libergy.md#tco--lca-model")
f("LIB-F16","libergy","Researched data centres as a new non-traditional customer vertical",
  ["strategy","market_research","commercial"],None,True,"libergy.md#market-research",
  notes="Lateral market thinking. Underused fact.")
f("LIB-F17","libergy","Defined user personas and product objectives using the Double Diamond design process",
  ["product","market_research","design"],"LIB-13",True,"libergy.md#user-needs-definition", verified="check")
f("LIB-F18","libergy","Participated in a 2-day lean canvas workshop defining USP, segmentation and roadmap for 3 new offerings",
  ["strategy","product"],"LIB-11",True,"libergy.md#lean-canvas",
  notes="PARTICIPATED, never led. See facts.yaml.")
f("LIB-F19","libergy","Represented the company at a 70-person green energy summit for trend scouting and venture identification",
  ["communication","commercial","networking"],"LIB-09",True,"libergy.md#events")
f("LIB-F20","libergy","Built full B2B sales deck including storyboard, CTA and digital product offering",
  ["communication","commercial","strategy"],"LIB-05",True,"libergy.md#sales-pitch-deck")

# ================================================================ 180DC
f("180-F01","consulting_180dc","Led a 6-person team delivering carbon impact recommendations to a multi-campus European institution",
  ["leadership","sustainability","stakeholder_management"],"180-01",True,"180dc.md#engagement-facts",
  notes="PRIMARY leadership proof point in the entire profile.")
f("180-F02","consulting_180dc","Reported that 2 of 3 benchmarked routes were not viable, including one 29.61% more expensive and 60% slower",
  ["intellectual_honesty","analytics","consulting"],None,False,"180dc.md#mobility",
  notes="Best 'data contradicted what the client wanted' answer. Interview only.")
f("180-F03","consulting_180dc","Benchmarked Paris-London train as 12.46% cheaper and 52% faster than flying, the highest-ROI shift",
  ["analytics","sustainability","cost_benefit"],"180-05",True,"180dc.md#mobility")
f("180-F04","consulting_180dc","Built an impact/effort matrix across 4 footprint categories to prioritise 3 interventions",
  ["prioritisation","strategy","sustainability"],"180-04",True,"180dc.md#carbon-footprint-mapping")
f("180-F05","consulting_180dc","Tailored food and commute recommendations separately for each of 5 country campuses",
  ["localisation","strategy","multi_market"],None,True,"180dc.md#food",
  notes="Shows multi-country rollout is not one solution repeated. Underused.")
f("180-F06","consulting_180dc","Researched transport partners including SNCF, Deutsche Bahn, BlaBlaCar Daily, Mollow and Byway",
  ["partnerships","market_research","commercial"],"180-06",True,"180dc.md#mobility")
f("180-F07","consulting_180dc","Identified a carbon accounting platform willing to donate source code, outside the original brief",
  ["initiative","partnerships","opportunity_spotting"],None,True,"180dc.md#additional-opportunity")
f("180-F08","consulting_180dc","Owned project scoping, client check-ins and final delivery, maintaining cadence and risk tracking",
  ["project_management","stakeholder_management"],"180-02",True,"180dc.md#methodology")
f("180-F09","consulting_180dc","Coordinated a team across 5 countries, functions and time zones",
  ["leadership","distributed_teams","project_management"],"180-03",True,"180dc.md#engagement-facts")
f("180-F10","consulting_180dc","Quantified EUR 60 per student saving and 92g CO2 offset per student on one route",
  ["analytics","sustainability","cost_benefit"],None,True,"180dc.md#mobility")
f("180-F11","consulting_180dc","Converted findings into board-ready recommendations influencing partnership decisions across 5 campuses",
  ["communication","strategy","influence"],"180-07",True,"180dc.md#methodology")

# ================================================================ Thesis
f("THS-F01","thesis","Normalised BEV performance to maximum payload capacity, adding ~32% to BEV CAPEX/OPEX",
  ["modelling","rigour","technical","mobility"],None,True,"thesis.md#technical-contributions",
  notes="Most technically impressive fact in the profile. On NO current CV.")
f("THS-F02","thesis","Built a 5-year TCO model covering CAPEX, OPEX and infrastructure for German long-haul operators",
  ["modelling","analytics","mobility"],"THS-01",True,"thesis.md#tco-model-components")
f("THS-F03","thesis","Conducted LCA across 3 fuel pathways covering production, tank-to-wheel, well-to-wheel and infrastructure",
  ["sustainability","modelling","lca"],"THS-02",True,"thesis.md#lca-model-components")
f("THS-F04","thesis","Ran 6 sensitivity analyses: diesel price, electricity price, battery cost, grid mix, feedstock, battery tech",
  ["modelling","sensitivity","rigour"],None,True,"thesis.md#sensitivity-analyses-run")
f("THS-F05","thesis","Found HVO delivers 70-90% GHG reduction depending on feedstock, with no fleet modification needed",
  ["sustainability","strategy","mobility"],"THS-03",True,"thesis.md#key-finding")
f("THS-F06","thesis","Delivered a time-dependent two-part recommendation: HVO short term, BEV long term",
  ["strategy","judgment","conditional_reasoning"],"THS-03",True,"thesis.md#key-finding",
  notes="Comfort with conditional rather than single-answer recommendations.")
f("THS-F07","thesis","Modelled EU ETS, RED II, EU HDV CO2 Standards and the German EUR 1.6B Gesamtkonzept grant scheme",
  ["regulation","policy","sustainability","germany"],None,True,"thesis.md#regulatory-context-modelled",
  notes="Naming the German scheme in German signals real engagement with DE policy.")
f("THS-F08","thesis","Developed an infrastructure guesstimate methodology comparing charging and refuelling station costs",
  ["modelling","estimation","infrastructure"],None,True,"thesis.md#technical-contributions")
f("THS-F09","thesis","Built the entire multi-scenario model self-directed in Excel with no external model",
  ["modelling","excel","independence"],None,True,"thesis.md#engagement-facts")
f("THS-F10","thesis","Quantified battery cost as adding ~23% to BEV TCO versus diesel",
  ["modelling","analytics","mobility"],None,True,"thesis.md#technical-contributions")

# ================================================================ Prajjawala
f("PRJ-F01","prajjawala","Sized a INR 386B annual industry inefficiency from component figures including INR 220B blocked inventory",
  ["market_sizing","commercial","analytics"],"PRJ-01",True,"prajjawala.md#the-problem",
  notes="Bottom-up sizing from components, not top-down estimate.")
f("PRJ-F02","prajjawala","Secured INR 1M seed funding through a data-driven pitch to angel investors as a student",
  ["fundraising","commercial","communication"],"PRJ-01",True,"prajjawala.md#investment-pitch")
f("PRJ-F03","prajjawala","Built an IoT MVP using consumption and logistics data; reduced inventory inefficiency by 58%",
  ["product","analytics","automation","iot"],"PRJ-02",True,"prajjawala.md#the-mvp")
f("PRJ-F04","prajjawala","Designed a pay-per-use pricing model with weight-based sensors to solve an affordability problem",
  ["pricing","product","business_model"],None,True,"prajjawala.md#the-solution",
  notes="Solved affordability via pricing-model change, not just technology. Underused.")
f("PRJ-F05","prajjawala","Built automated demand registration triggering real-time booking below a threshold",
  ["automation","product","forecasting"],None,True,"prajjawala.md#the-solution")
f("PRJ-F06","prajjawala","Defined a B2B model targeting 3 public oil marketing companies and ~20,000 dealers",
  ["business_model","commercial","b2b"],None,True,"prajjawala.md#business-model")
f("PRJ-F07","prajjawala","Built the pitch covering market sizing, competitive landscape, revenue model, projections and exit strategy",
  ["commercial","strategy","communication"],None,True,"prajjawala.md#investment-pitch")
f("PRJ-F08","prajjawala","Earliest instance of a repeating pattern: found a broken manual process, quantified it, built a system",
  ["pattern","initiative"],None,False,"prajjawala.md#interview_only",
  notes="Same shape as the n8n project 4 years later. Strong narrative thread for interviews.")

# ================================================================ Projects
f("N8N-F01","n8n_automation","Self-hosted an n8n and Ollama AI agent workflow turning invoice photos into a live analysis sheet",
  ["automation","ai_ml","data_infrastructure","initiative"],"N8N-01",True,"projects.md#1")
f("N8N-F02","n8n_automation","Ran the entire automation stack at zero recurring cost using self-hosting and open-source models",
  ["automation","ai_ml","cost_efficiency","infrastructure"],"N8N-03",True,"projects.md#1")
f("N8N-F03","n8n_automation","Replaced a handwritten site logbook that blocked any cost or budget-variance analysis",
  ["process_improvement","automation","analytics"],"N8N-01",True,"projects.md#1")
f("N8N-F04","n8n_automation","Structured the destination sheet so KPIs and analyses refresh automatically on every new entry",
  ["analytics","automation","data_infrastructure"],"N8N-02",True,"projects.md#1")
f("N8N-F05","n8n_automation","Chose self-hosting over paid APIs for cost control and keeping data local",
  ["infrastructure","judgment","ai_ml"],None,False,"projects.md#1",
  notes="Infrastructure decision-making, not just prompt use. Interview only.")
f("MUM-F01","muma","Specified a GNN predicting crowd density that outputs dynamic weights consumed by an A* pathfinder",
  ["ai_ml","technical","product"],"MUM-02",True,"projects.md#2",
  notes="The actual technical idea is the INTERACTION between the two, not either alone.")
f("MUM-F02","muma","Proposed a hierarchical architecture with a base model plus per-museum fine-tuning layer",
  ["ai_ml","architecture","product"],None,True,"projects.md#2",
  notes="Addresses cold-start for a new museum. On no current CV.")
f("MUM-F03","muma","Conducted 5 primary interviews and synthesised 6 insights using a persona/want/because/but framework",
  ["market_research","product","user_research"],"MUM-01",True,"projects.md#2")
f("MUM-F04","muma","Mapped 10 stakeholder groups across the full museum ecosystem",
  ["stakeholder_management","product","ecosystem"],"MUM-01",True,"projects.md#2")
f("MUM-F05","muma","Created 5 customer personas and developed 18 user stories as functional requirements",
  ["product","requirements","user_research"],"MUM-02",True,"projects.md#2")
f("MUM-F06","muma","Designed a GDPR plan with transparency, anonymisation and granular opt-out for visitor location data",
  ["regulation","ai_ml","privacy","product"],"MUM-03",True,"projects.md#2",
  notes="Designed in, not bolted on. Valuable for Responsible AI roles.")
f("MUM-F07","muma","Solved the crowd-density data problem by buying a data source at ~EUR 9/month rather than collecting it",
  ["judgment","build_vs_buy","product"],None,False,"projects.md#2",
  notes="Pragmatic build-vs-buy call. Interview only.")
f("MDY-F01","moodys","Won the Moody's Credit Rating Challenge 2023 among top French business schools",
  ["finance","analytics","competition"],"MDY-01",True,"projects.md#3")
f("MDY-F02","moodys","Forecasted firm financials assessing profitability, credit performance and liquidity risk",
  ["finance","analytics","forecasting"],"MDY-01",True,"projects.md#3")

# Added 2026-11-05: EnergyMap (evidence/projects.md section 6). The live JSON
# carries per-fact notes; see index/projects.facts.json for the full records.
f("ENM-F01","energymap","Built EnergyMap, a live source-backed energy and clean-tech market map, self-directed with Claude Code",
  ["product","data_infrastructure","initiative","ai_ml","sustainability"],"ENM-01",True,"projects.md#6")
f("ENM-F02","energymap","Built 4 data explorers: battery fleet, renewable buildout, India power market and prices, power prices with negative hours",
  ["analytics","data_infrastructure","energy","sustainability"],"ENM-01",True,"projects.md#6",verified="check")
f("ENM-F03","energymap","Explorers pull official data from MaStR and SMARD (Bundesnetzagentur) on weekly and daily refresh, plus CERC India market reports",
  ["data_infrastructure","energy","germany","multi_market","automation"],"ENM-01",True,"projects.md#6")
f("ENM-F04","energymap","Published 2 insight studies: a virtual power plant market study and the long-haul trucking thesis",
  ["market_research","communication","strategy","energy"],"ENM-01",True,"projects.md#6",verified="check")
f("ENM-F05","energymap","Built an interactive VPP funnel chart sizing German home batteries reachable via manufacturer clouds, 2026 to 2030",
  ["market_sizing","analytics","energy","commercial"],None,True,"projects.md#6")
f("ENM-F06","energymap","Market funnel builder tool based on the Cloudline study is in development, not yet live",
  ["product","market_sizing"],None,False,"projects.md#6")
f("ENM-F07","energymap","Mapped 159 energy and clean-tech topics across 3 layers and 9 domains, including Carbon Capture & Removal",
  ["market_research","energy","strategy"],None,True,"projects.md#6",verified="check")
f("ENM-F08","energymap","Every figure on the site links to its source and a last-checked date",
  ["rigour","data_quality"],None,False,"projects.md#6")
f("ENM-F09","energymap","Scope set as Germany first, then Europe, India and Asia",
  ["multi_market","strategy"],None,True,"projects.md#6")

# ================================================================ emit
os.makedirs("/home/claude/index", exist_ok=True)
roles = {}
for x in F:
    roles.setdefault(x["role"], []).append(x)

filemap = {"pg":"pg","libergy":"libergy","consulting_180dc":"180dc","thesis":"thesis",
           "prajjawala":"prajjawala","n8n_automation":"projects","muma":"projects",
           "moodys":"projects","energymap":"projects"}
grouped = {}
for r, items in roles.items():
    grouped.setdefault(filemap[r], []).extend(items)

for fname, items in grouped.items():
    with open(f"/home/claude/index/{fname}.facts.json","w",encoding="utf-8") as fh:
        json.dump(items, fh, ensure_ascii=False, indent=2)

bank = json.load(open("/home/claude/bullet-bank.json"))
existing = {b["id"] for b in bank["bullets"]}

print(f"TOTAL FACTS INDEXED: {len(F)}   (bullet bank has {len(existing)} bullets)")
print()
nb = [x for x in F if x["has_bullet"] is None]
print(f"FACTS WITH NO BULLET YET: {len(nb)}  <-- these were previously UNRETRIEVABLE")
cvable = [x for x in nb if x["cv_suitable"]]
iv = [x for x in nb if not x["cv_suitable"]]
print(f"   CV-suitable, bullet generatable on demand : {len(cvable)}")
print(f"   Interview-only                            : {len(iv)}")
print()
bad = [x for x in F if x["has_bullet"] and x["has_bullet"] not in existing]
print(f"BROKEN BULLET REFS: {len(bad)}  {[b['id'] for b in bad]}")
print()
c = Counter(t for x in F for t in x["tags"])
print(f"UNIQUE TAGS: {len(c)}  (bullet bank had 16 themes)")
print("New retrievable dimensions that did not exist before:")
oldthemes = set(bank["theme_taxonomy"])
new = sorted(t for t in c if t not in oldthemes)
for i in range(0, len(new), 4):
    print("   " + ", ".join(new[i:i+4]))
print()
for fn, items in sorted(grouped.items()):
    n_nb = sum(1 for x in items if x["has_bullet"] is None)
    print(f"  index/{fn}.facts.json  {len(items):>3} facts  ({n_nb} with no bullet)")
