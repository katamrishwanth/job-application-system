#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate.py — gate for any generated CV content.

Four checks:
  1. LENGTH      char ranges per content type
  2. STYLE       em-dashes, banned AI markers
  3. CLAIM LOCK  regex against facts.yaml guardrails
  4. PROVENANCE  every number and proper noun must trace to evidence/

Usage:
  python3 validate.py --text "bullet text" --type work
  python3 validate.py --file draft.txt --type work
  python3 validate.py --selfcheck          # run built-in test cases
"""
import argparse, glob, json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
REFS = os.path.join(os.path.dirname(ROOT), "references")
EVIDENCE_DIR = os.path.join(REFS, "evidence")
INDEX_DIR = os.path.join(REFS, "index")

RANGES = {"work": (100, 115), "project": (120, 130),
          "thesis": (100, 115), "summary": (0, 400)}
COVER_LETTER_PCT_BAND = (75, 85)  # % of sample average, see workflow-rules.yaml L09

# ---------------------------------------------------------------- 2. STYLE
EM_DASH = "\u2014"
BANNED_PHRASES = [
    "leverage synergies", "delve into", "in today's fast-paced",
    "it's worth noting", "seamlessly", "cutting-edge", "game-changing",
    "robust solution", "spearheaded", "passionate about",
]

# ---------------------------------------------------------------- 3. CLAIM LOCKS
# (pattern, severity, message)
CLAIM_LOCKS = [
    (r"\bled\b[^.]{0,40}(lean canvas|workshop)", "ERROR",
     "facts.yaml locks the Libergy lean canvas as 'participated', not 'led'."),
    (r"(lean canvas|workshop)[^.]{0,40}\bI led\b", "ERROR",
     "facts.yaml locks the Libergy lean canvas as 'participated', not 'led'."),
    (r"\b(Jul|Sep|Aug)['’]?25\b[^.]{0,30}thesis|thesis[^.]{0,30}\b20?25\b", "ERROR",
     "Thesis dates are locked to 2024. 2025 contradicts the transcript."),
    (r"\bSep['’]?23\s*[-–]\s*May['’]?24\b[^.]{0,40}Quantis|Quantis[^.]{0,40}Sep['’]?23", "ERROR",
     "Quantis dates are locked to Jan'23 - Apr'23."),
    (r"554/KOL/2011|\bpatent(ed)?\b", "ERROR",
     "Patent 554/KOL/2011 predates involvement by a decade. Never claim it."),
    (r"\b7\s+senior\s+interviews\b", "ERROR",
     "Locked framing is '7 expert interviews'. Only 5 were companies."),
    (r"\bconducted\s+7\s+(expert\s+)?interviews\b", "ERROR",
     "Interviews were a team effort. Use 'synthesised', not 'conducted'."),
    (r"consumer[- ]facing[^.]{0,30}(dashboard|platform)", "ERROR",
     "The Libergy platform is B2B, not consumer-facing."),
    (r"\bGerman\b[^.]{0,20}\b(A1|A2|B2|C1|C2)\b", "ERROR",
     "German is locked at B1 on all CVs."),
    (r"\b(graduat\w+|degree)[^.]{0,25}\b2025\b", "ERROR",
     "Graduation year is locked to 2026."),
    (r"\b3,?000\s*(hrs|hours)[^.]{0,40}\b(saved|saving|delivered)\b", "WARN",
     "The 3,000 hrs/year Paper COT figure is a foundation, not a delivered saving."),
    (r"\bdiscounter[- ]targeted\b|\btargeted[^.]{0,20}discounter[^.]{0,20}(YouTube|YT|ad)", "ERROR",
     "The YouTube frequency test was nationwide, never discounter-targeted."),
    (r"\b(70|90)%\s*GHG\s*reduction\b(?![^.]{0,30}feedstock)", "WARN",
     "HVO's 70-90% GHG reduction is feedstock-dependent. Do not state flat."),
    (r"\bfounder\b|\bco[- ]founded\b", "ERROR",
     "All roles are internships or student projects. Never imply founder status."),
    (r"\bSQL\b", "WARN",
     "SQL status is 'learning' in facts.yaml. Only use with 'familiar with' framing."),
    (r"\bESCP\b[^.]{0,40}\bclient\b|\bclient\b[^.]{0,40}\bESCP\b", "ERROR",
     "180DC's client was ESCP itself and must never be named."),
    (r"Libergy[^.]{0,150}(heavy-duty vehicles|charging infrastructure|breakeven points)", "ERROR",
     "This is thesis-scope detail (vehicle-class CAPEX/OPEX, charging "
     "infrastructure, breakeven analysis), not Libergy's. Libergy's own "
     "TCO/LCA work covers 6 industry sectors for customer education -- "
     "found conflated in the RWE/Aurora reference letters, corrected in VFG."),
    (r"\bteam of 7 students\b|\b7 students\b", "ERROR",
     "Quantis student team is verified at 6 (Anisha Kaul, Charlotte "
     "Zenatelli, Ines Pedro, Rishwanth Katam, Thibaud Auziere, Till "
     "Meinhardt), not 7. The confirmed 7 is expert interviews, a different "
     "number describing a different thing -- found wrong in RWE/Aurora "
     "reference letters, corrected 2026-08-06."),
    (r"\b6 industries\b", "ERROR",
     "Libergy's TCO/LCA model covers 7 verticals, not 6 -- corrected "
     "2026-08-06 against the actual Excel model. Missing two: Industrial, "
     "Public services."),
    (r"\bleading 2 projects\b[^.]{0,30}180 Degrees|180 Degrees[^.]{0,30}\b2 projects\b", "WARN",
     "Verified 2026-08-06: there WERE 2 180DC engagements (Handicap "
     "International Belgium, ESCP carbon footprint), but Rishwanth only "
     "LED the ESCP one -- he was a consultant, not lead, on HI Belgium. "
     "'Leading 2 projects' overstates it; be specific about which one."),
    (r"tender[^.]{0,80}(Power Automate|German platforms)|(Power Automate|German platforms)[^.]{0,80}tender", "ERROR",
     "Libergy tender monitoring was corrected 2026-11-05 by Rishwanth: "
     "16 EU platforms, automated with Google Apps Script."),
    (r"funnel builder[^.]{0,40}\b(built|launched|live|shipped)\b|\b(built|launched|shipped)\b[^.]{0,40}funnel builder", "ERROR",
     "EnergyMap's market funnel builder is in development. Never call it built until it is live."),
    (r"\b78\s*%|\b31\s*%\s*more", "WARN",
     "78% / 31% are EnergyMap site figures for the thesis. The locked thesis "
     "figures are 70-90% (feedstock-dependent) and ~32%. Use those."),
]

# ---------------------------------------------------------------- 4. PROVENANCE
STOPWORDS = set("""
A An The This That These Those It Its He She They We I You His Her Their Our My Your
And But Or So For Nor Yet As At By From In Into Of On To With Without Within Across
Built Ran Led Drove Made Set Won Cut Used Gave Took Kept Sat Was Were Is Are Be Been
Conducted Delivered Developed Designed Created Defined Mapped Managed Owned Reached
Identified Recommended Presented Synthesised Synthesized Translated Coordinated
Negotiated Automated Priced Benchmarked Evaluated Researched Proposed Contributed
Secured Reduced Corrected Improved Supported Applied Analysed Analyzed Quantified
Structured Configured Documented Upskilled Executed Modelled Modeled Normalised
Replaced Chose Found Learned Pushed Wrote Added Ensured Enabled Shaped Turned
Company Team Data Model Tool Project Report Platform Dashboard Analysis Framework
Interviews Insights Bullet Work Role Business Market Customer Product Process
CEO Ownership Assessment
""".split())


def load_evidence_corpus():
    txt = []
    for p in sorted(glob.glob(os.path.join(EVIDENCE_DIR, "*.md"))):
        txt.append(open(p, encoding="utf-8").read())
    for p in sorted(glob.glob(os.path.join(INDEX_DIR, "*.json"))):
        txt.append(open(p, encoding="utf-8").read())
    fy = os.path.join(REFS, "facts.yaml")
    if os.path.exists(fy):
        txt.append(open(fy, encoding="utf-8").read())
    return "\n".join(txt)


def norm_num(tok):
    """Normalise a numeric token for comparison: strip separators/units."""
    return re.sub(r"[,\.\s]", "", tok).lower()


def check_provenance(text, corpus, known_entities=None):
    issues = []
    corpus_l = corpus.lower()
    known_l = set()
    known_nums = set()
    for e in (known_entities or []):
        known_l.add(e.lower())
        known_l.update(w.lower() for w in e.split())
        known_nums.update(norm_num(m) for m in re.findall(r"\d[\d,\.]*", e))

    # Acronym-expansion phrases ("Total Cost of Ownership (TCO)") aren't new
    # claims if the acronym itself already resolves in the corpus. Look
    # backward from the parenthetical for nearby capitalised words rather
    # than requiring an unbroken match -- lowercase connectors ("of", "and")
    # inside the phrase would otherwise break a stricter pattern.
    exempt_words = set()
    for m in re.finditer(r"\(([A-Z]{2,6})\)", text):
        acronym = m.group(1)
        if _resolves(acronym, corpus_l):
            window = text[max(0, m.start() - 50):m.start()]
            exempt_words.update(w.lower() for w in re.findall(r"\b[A-Z][a-z]+\b", window))

    # Strip phone-number- and email-shaped substrings before number checking.
    # Formatting varies ("8610 9845" vs "86109845") but it's the same fact,
    # not a claim needing evidence support -- so compare with all internal
    # whitespace removed instead of flagging a formatting difference.
    phone_re = re.compile(r"\+?\d[\d\-\s]{6,}\d")
    email_re = re.compile(r"[\w\.\-]+@[\w\.\-]+")
    scrub = text
    for m in phone_re.finditer(text):
        candidate = re.sub(r"\s", "", m.group())
        if candidate not in re.sub(r"\s", "", corpus):
            issues.append(("ERROR", f"Phone-like number '{m.group()}' not found in facts.yaml."))
        scrub = scrub.replace(m.group(), "")
    for m in email_re.finditer(scrub):
        if m.group().lower() not in corpus_l:
            issues.append(("ERROR", f"Email '{m.group()}' not found in facts.yaml."))
        scrub = scrub.replace(m.group(), "")

    corpus_nums = set(norm_num(m) for m in re.findall(r"\d[\d,\.]*", corpus))
    for m in re.findall(r"\d[\d,\.]*", scrub):
        if norm_num(m) not in corpus_nums and norm_num(m) not in known_nums:
            issues.append(("ERROR", f"Number '{m}' does not appear in any evidence file."))

    # duration/time phrases are the classic fabrication vector
    for m in re.findall(r"\b\d+\s*(?:month|months|week|weeks|day|days|year|years)\b",
                        scrub, re.I):
        if m.lower() not in corpus_l:
            issues.append(("ERROR", f"Duration '{m}' is not stated in evidence. Likely invented."))

    # proper nouns. Skip any capitalised word that opens the string, follows
    # sentence-ending punctuation, or follows a paragraph break -- greetings
    # like "Dear Hiring Manager," sit at the start of a line, not after a
    # period, so a newline counts as a boundary too. Also skip known_entities
    # (e.g. the target company name) -- a cover letter legitimately names an
    # external company that will never appear in Rishwanth's own evidence.
    # A salutation line ("Dear Hiring Manager," / "Dear Maja,") is title-case
    # by convention across every word, not just the first -- exclude the
    # whole span from the proper-noun scan rather than only the first word.
    scrub = re.sub(r"(?m)^Dear [^,\n]*,", "", scrub)

    for m in re.finditer(r"\b[A-Z][A-Za-z&\.\-]{2,}\b", scrub):
        tok, start = m.group(), m.start()
        prefix = scrub[:start].rstrip(" \t")
        if start == 0 or (prefix and prefix[-1] in ".;:!?\n"):
            continue
        if tok in STOPWORDS or tok.lower() in known_l or tok.lower() in exempt_words:
            continue
        parts = [p for p in tok.split("-") if p and p[0].isupper()] or [tok]
        if all(_resolves(p, corpus_l) for p in parts):
            continue
        issues.append(("ERROR", f"Proper noun '{tok}' does not appear in any evidence file."))
    return issues


def _resolves(tok, corpus_l):
    """True if tok, or a simple morphological variant, appears in the corpus."""
    t = tok.lower()
    variants = {t}
    if t.endswith("s"):
        variants.add(t[:-1])          # HDVs -> HDV
    if t.endswith("es"):
        variants.add(t[:-2])
    variants.add(t + "s")
    return any(vv in corpus_l for vv in variants)


# ---------------------------------------------------------------- runner
def validate(text, ctype, corpus, known_entities=None):
    out = []
    lo, hi = RANGES.get(ctype, RANGES["work"])
    n = len(text)
    if not (lo <= n <= hi):
        d = f"+{n-hi} over" if n > hi else f"{lo-n} under"
        out.append(("ERROR", f"Length {n}, target {lo}-{hi} ({d})."))

    if EM_DASH in text:
        out.append(("ERROR", "Contains an em-dash."))
    for p in BANNED_PHRASES:
        if p.lower() in text.lower():
            out.append(("WARN", f"Banned AI-style phrase: '{p}'."))

    for pat, sev, msg in CLAIM_LOCKS:
        if re.search(pat, text, re.I):
            out.append((sev, f"CLAIM LOCK: {msg}"))

    out += check_provenance(text, corpus, known_entities)
    return n, out


def validate_cover_letter(text, corpus, sample_avg_words=None, known_entities=None):
    """Cover letters are prose, not char-range bullets. Length is checked as
    a word-count percentage against sample_avg_words (if given), not a fixed
    range. Style and provenance checks still apply in full -- fabrication
    risk is at least as high in longer prose as in a single bullet.
    known_entities: target company/role names etc that are EXPECTED to be
    absent from Rishwanth's personal evidence (e.g. the employer's own name)
    -- excluded from the proper-noun fabrication check, not from anything
    else."""
    out = []
    words = len(text.split())
    if sample_avg_words:
        pct = round(100 * words / sample_avg_words)
        lo, hi = COVER_LETTER_PCT_BAND
        if not (lo <= pct <= hi):
            out.append(("WARN", f"{words} words is {pct}% of the {sample_avg_words}-word "
                                 f"sample average, target {lo}-{hi}%."))
    else:
        out.append(("WARN", "No sample_avg_words given; word-count band not checked."))

    if EM_DASH in text:
        out.append(("ERROR", "Contains an em-dash."))
    for p in BANNED_PHRASES:
        if p.lower() in text.lower():
            out.append(("WARN", f"Banned AI-style phrase: '{p}'."))
    for pat, sev, msg in CLAIM_LOCKS:
        if re.search(pat, text, re.I):
            out.append((sev, f"CLAIM LOCK: {msg}"))
    out += check_provenance(text, corpus, known_entities)
    return words, out


def report(text, ctype, corpus, label="", known_entities=None):
    n, issues = validate(text, ctype, corpus, known_entities)
    errs = [i for i in issues if i[0] == "ERROR"]
    warns = [i for i in issues if i[0] == "WARN"]
    status = "FAIL" if errs else ("PASS (warnings)" if warns else "PASS")
    print(f"\n[{status}] {label or ctype} | {n} chars")
    print(f"  {text}")
    for sev, m in issues:
        print(f"    {sev}: {m}")
    return not errs


def selfcheck(corpus):
    cases = [
        ("Reached 75+ companies over 3 months of sustained cold outreach; secured and synthesised 5 expert interviews",
         "work", "SHOULD FAIL: my invented '3 months'"),
        ("Reached 75+ companies through sustained cold outreach; secured and synthesised 5 expert interviews for delivery",
         "work", "SHOULD PASS: corrected version"),
        ("Led the 2-day lean canvas workshop, defining USP and customer segmentation for 3 new product offerings",
         "work", "SHOULD FAIL: the 'led' claim lock"),
        ("Ran a discounter-targeted YouTube ad frequency test and attributed EUR 4.2M in national revenue uplift",
         "work", "SHOULD FAIL: nationwide-vs-discounter lock"),
        ("Partnered with Deloitte and Accenture to rebuild the DACH discounter sellout data model with Nielsen",
         "work", "SHOULD FAIL: fabricated proper nouns"),
        ("Normalised BEV performance to maximum payload capacity, adding ~32% to BEV CAPEX and OPEX in the model",
         "work", "SHOULD PASS: real fact THS-F01"),
        ("Automated tender monitoring across 16 German platforms via Power Automate and wrote the process guide",
         "work", "SHOULD FAIL: Libergy tender correction lock"),
        ("Built 4 data explorers on MaStR, SMARD and CERC data, from battery fleets to negative prices; published 2 market insight studies.",
         "project", "SHOULD PASS: EnergyMap ENM-01"),
    ]
    ok = 0
    for t, ct, lbl in cases:
        if report(t, ct, corpus, lbl):
            ok += 1
    print(f"\n{'='*70}\n{ok}/{len(cases)} passed. "
          f"(Cases 1,3,4,5,7 are SUPPOSED to fail.)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text"); ap.add_argument("--file")
    ap.add_argument("--type", default="work",
                     choices=list(RANGES) + ["cover_letter"])
    ap.add_argument("--sample-avg-words", type=int, default=None,
                     help="For --type cover_letter: average word count of "
                          "reference sample letters, to check the % band.")
    ap.add_argument("--known-entities", default="",
                     help="Comma-separated names expected to be absent from "
                          "evidence (e.g. target company name) -- excluded "
                          "from the proper-noun fabrication check.")
    ap.add_argument("--selfcheck", action="store_true")
    a = ap.parse_args()
    corpus = load_evidence_corpus()
    known = [e.strip() for e in a.known_entities.split(",") if e.strip()]
    if not corpus.strip():
        print("WARNING: evidence corpus empty. Provenance check disabled.", file=sys.stderr)
    if a.selfcheck:
        selfcheck(corpus); return

    if a.type == "cover_letter":
        text = open(a.file, encoding="utf-8").read() if a.file else a.text
        if not text:
            ap.print_help(); return
        words, issues = validate_cover_letter(text, corpus, a.sample_avg_words, known)
        errs = [i for i in issues if i[0] == "ERROR"]
        status = "FAIL" if errs else ("PASS (warnings)" if len(issues) else "PASS")
        print(f"[{status}] cover_letter | {words} words")
        for sev, m in issues: print(f"  {sev}: {m}")
        sys.exit(0 if not errs else 1)

    if a.file:
        for line in open(a.file, encoding="utf-8"):
            line = line.strip().lstrip("•-* ").strip()
            if line:
                report(line, a.type, corpus)
    elif a.text:
        sys.exit(0 if report(a.text, a.type, corpus, known) else 1)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
