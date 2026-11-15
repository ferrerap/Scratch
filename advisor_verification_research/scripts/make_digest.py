#!/usr/bin/env python3
"""Build a compact evidence digest grouped by proposition (for reviewers).
Usage: python3 -I scripts/make_digest.py <project_root>
Writes 01_Evidence/evidence_digest_by_proposition.md and 01_Evidence/source_index.md
"""
import json, re, sys, os
from collections import defaultdict

R = sys.argv[1] if len(sys.argv) > 1 else "."
src = {s["source_id"]: s for s in json.load(open(os.path.join(R, "01_Evidence/sources.json"), encoding="utf-8"))}
ev = json.load(open(os.path.join(R, "01_Evidence/evidence.json"), encoding="utf-8"))

def short(s, n):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 1] + "…"

groups = defaultdict(list)
for e in ev:
    props = re.findall(r"P\d\.\d|P-NEW", e.get("proposition_tested") or "") or ["(none)"]
    for p in sorted(set(props)):
        groups[p].append(e)

out = ["# Evidence digest by proposition", "",
       "One line per evidence item (an item appears under every proposition it names). Full records: `01_Evidence/evidence.json`.",
       "Format: **EVR** [rel] (RQ; access; EG) source — finding | quant | W/X tags", ""]
order = sorted(groups, key=lambda p: (p == "(none)", p))
for p in order:
    items = groups[p]
    rel = defaultdict(int)
    for e in items: rel[e.get("relationship")] += 1
    out.append(f"## {p}  (n={len(items)}; " + ", ".join(f"{k}={v}" for k, v in sorted(rel.items())) + ")")
    for e in sorted(items, key=lambda x: (x.get("relationship") or "", x["evidence_id"])):
        s = src.get(e["source_id"], {})
        tags = ",".join((e.get("work_type_tags") or []) + (e.get("concept_tags") or []))
        out.append(f"- **{e['evidence_id']}** [{e.get('relationship')}] ({'/'.join(e.get('research_question_ids') or [])}; "
                   f"{e.get('access_status')}; {short(e.get('underlying_evidence_group'), 50)}) "
                   f"{e['source_id']} {short(s.get('title'), 70)} — {short(e.get('observed_finding'), 330)}"
                   + (f" | Q: {short(e.get('quantitative_result'), 160)}" if e.get("quantitative_result") else "")
                   + (f" | {tags}" if tags else ""))
    out.append("")
open(os.path.join(R, "01_Evidence/evidence_digest_by_proposition.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")

idx = ["# Source index", "", "| ID | Title | Org/authors | Date | Type | Access | Evidence group | URL |", "|---|---|---|---|---|---|---|---|"]
for sid in sorted(src):
    s = src[sid]
    idx.append(f"| {sid} | {short(s.get('title'), 80)} | {short(s.get('authors_or_organization'), 40)} | {short(s.get('publication_date'), 12)} | "
               f"{s.get('source_type')} | {s.get('access_status')} | {short(s.get('underlying_evidence_group'), 45)} | {s.get('url')} |")
open(os.path.join(R, "01_Evidence/source_index.md"), "w", encoding="utf-8").write("\n".join(idx) + "\n")
print("digest lines:", len(out), "index rows:", len(src))
