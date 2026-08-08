#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_keyword_coverage.py — did the final CV + cover letter actually use
the atomic keywords from the jd-recruiter-brief? This is the OPPOSITE
failure mode from validate.py's provenance check: that catches saying
something untrue; this catches forgetting to say something true and
required. Real precedent: the Accenture session found "operating model"
missing from the CV despite appearing 3 times in the JD -- caught by eye,
after the fact. This script catches it before submission.

Usage:
  python3 check_keyword_coverage.py --keywords "SAP,Salesforce,operating model" \
      --file final_cv_and_letter.txt
"""
import argparse, sys


def check(keywords, text):
    text_l = text.lower()
    present, absent = [], []
    for kw in keywords:
        kw = kw.strip()
        if not kw:
            continue
        (present if kw.lower() in text_l else absent).append(kw)
    return present, absent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keywords", required=True,
                     help="Comma-separated atomic keywords from the recruiter brief's Part 1")
    ap.add_argument("--file", required=True,
                     help="Combined CV text + cover letter text to check against")
    a = ap.parse_args()
    keywords = a.keywords.split(",")
    text = open(a.file, encoding="utf-8").read()
    present, absent = check(keywords, text)

    print(f"Coverage: {len(present)}/{len(present)+len(absent)} atomic keywords found\n")
    if present:
        print("FOUND:")
        for k in present: print(f"  [x] {k}")
    if absent:
        print("\nMISSING -- present in the JD, not found anywhere in the CV/letter:")
        for k in absent: print(f"  [ ] {k}")
        print("\nEach of these is either a real gap (say so) or something Rishwanth")
        print("has evidence for that didn't make it into this draft (add it).")
    sys.exit(1 if absent else 0)


if __name__ == "__main__":
    main()
