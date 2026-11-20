#!/usr/bin/env python3
"""Regenerate the Mayfield IE Market Intelligence dashboard from the verified workbook.

Usage:
    python3 build_dashboard.py "<workbook export>.xlsx" [output_dir]

The workbook (Google Sheet "Mayfield IE Competitive Landscape — Verified V2",
exported via File > Download > Microsoft Excel) is the single source of truth for
firms, evidence records, segments, business models, audit items, sources and gaps.
narrative.json holds the short report-derived text (findings, conclusions) that is
not tabular. Outputs:
    Mayfield_IE_Dashboard_Data.json      structured dataset
    Mayfield_IE_Market_Intelligence.html self-contained dashboard (data embedded)
"""
import json, re, sys, os, datetime
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))

def rows(ws):
    it = ws.iter_rows(values_only=True)
    hdr = [str(h).strip() if h is not None else "" for h in next(it)]
    out = []
    for r in it:
        if r is None or all(v in (None, "") for v in r):
            continue
        out.append({hdr[i]: ("" if v is None else str(v).strip()) for i, v in enumerate(r) if i < len(hdr)})
    return out

def sheet(wb, prefix):
    for ws in wb.worksheets:
        if ws.title.startswith(prefix):
            return ws
    raise SystemExit(f"Workbook tab starting with '{prefix}' not found")

def ids(text):
    """Expand 'S06–S08, S10' style references into a list of source IDs."""
    out = []
    for a, b in re.findall(r"S(\d\d)\s*[–-]\s*S(\d\d)", text or ""):
        out += ["S%02d" % i for i in range(int(a), int(b) + 1)]
    out += re.findall(r"S\d\d", text or "")
    seen, res = set(), []
    for i in out:
        if i not in seen:
            seen.add(i); res.append(i)
    return res

def classes(text):
    return sorted({int(c) for c in re.findall(r"\b([1-5])\b", text or "")})

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

# Firm aliases used to link evidence records (whose 'Firm(s)' cell may name several firms) to firms.
ALIASES = [
    (r"\bLeidos\b", "Leidos"), (r"\bDNV\b", "DNV"), (r"\bEnertis\b", "Enertis Applus+"),
    (r"\bICF\b", "ICF"), (r"Sargent", "Sargent & Lundy"), (r"Black (&|and) Veatch", "Black & Veatch"),
    (r"UL Solutions", "UL Solutions"), (r"ArcVera", "Bureau Veritas / ArcVera"), (r"\bVDE\b", "VDE Americas"),
    (r"Luminate", "Luminate"), (r"\bE3\b", "E3 Consulting"), (r"Natural Power", "Natural Power"),
    (r"Clean Energy Associates", "Intertek CEA (Clean Energy Associates)"), (r"Borrego", "Borrego Solar"),
    (r"Radian", "Radian Generation"), (r"\bBEW\b", "BEW Engineering"), (r"Bay4", "Bay4 Energy"),
]

# Segment tags derived from the workbook's own text fields (Technologies, Segment focus, Service orientation).
TAG_RULES = {
    "utility": r"utility",
    "bess": r"BESS|storage",
    "dg": r"\bDG\b|community|residential|portfolio|securiti",
    "ci": r"C&I|microgrid|BTM",
    "sponsor": r"sponsor|buy-side|M&A|acqui|owner|investor|OE\b",
}

# Fallback only: project type derived from the transaction description when the workbook has no "Project type" column.
def project_type(t):
    t2 = t.lower()
    if "manufactur" in t2: return "Manufacturing"
    if re.search(r"solar\s*\+\s*(bess|storage)|solar\+bess|solar \+ storage|solar and storage|pv\).*bess", t2): return "Solar + storage"
    if re.search(r"bess|storage", t2): return "BESS"
    if re.search(r"community|residential|abs|securiti|\bdg\b|microgrid|portfolio|credit agreement|warehouse|facility", t2): return "DG / residential / portfolio facility"
    if "solar" in t2: return "Utility / project solar"
    return "Other / unspecified"

def main():
    src = sys.argv[1]
    outdir = sys.argv[2] if len(sys.argv) > 2 else HERE
    wb = openpyxl.load_workbook(src, data_only=True)

    readme = {r[0]: r[1] for r in sheet(wb, "README").iter_rows(values_only=True) if r and r[0]}
    class_defs = []
    for k, v in readme.items():
        m = re.match(r"Class (\d) – (.+)", str(k))
        if m:
            class_defs.append({"id": int(m.group(1)), "name": m.group(2), "definition": v})

    strength_defs, position_defs = [], []
    for k, v in readme.items():
        m = re.match(r"Strength – (.+)", str(k))
        if m: strength_defs.append({"level": m.group(1), "definition": v})
        m = re.match(r"Position ([A-F]) – (.+)", str(k))
        if m: position_defs.append({"key": m.group(1), "name": m.group(2), "definition": v})
    legend = {"strengthIntro": readme.get("V2 evidence strength", ""), "positionIntro": readme.get("Market position", ""),
              "strength": strength_defs, "positions": position_defs}

    sources = {}
    for r in rows(sheet(wb, "7_")):
        sources[r["Source ID"]] = {
            "id": r["Source ID"], "title": r["Title"], "publisher": r["Publisher"], "date": r["Date"],
            "type": r["Source type"], "url": r["URL"], "access": r["Access status (2026-11-17)"], "usedFor": r["Used for"]}

    firms = []
    for r in rows(sheet(wb, "1_")):
        text = " ".join([r["Technologies"], r["Segment focus"], r["Service orientation"]])
        tags = [t for t, rx in TAG_RULES.items() if re.search(rx, text, re.I)]
        firms.append({
            "id": slug(r["Firm"]), "name": r["Firm"], "category": r["V2 category"], "v1Tier": r["V1 tier (original)"],
            "scale": r["Ownership / scale (public)"], "technologies": r["Technologies"], "segments": r["Segment focus"],
            "orientation": r["Service orientation"], "classesText": r["Evidence classes found (1–5)"],
            "classes": classes(r["Evidence classes found (1–5)"]), "references": r["Key documented references"],
            "v1Class": r["V1 evidence classification"], "v1Confidence": r["V1 confidence"],
            "strength": r["V2 evidence strength"], "change": r["Change vs V1"], "relevance": r["Relevance to Mayfield"],
            "priority": r["Priority shortlist"].lower().startswith("y"), "sourceIds": ids(r["Source IDs"]),
            "status": r["Research status"], "tags": tags, "detail": None})
    byname = {f["name"]: f for f in firms}

    priority, mayfield = [], None
    for r in rows(sheet(wb, "2_")):
        d = {"group": r["Group"], "scale": r["Ownership / scale"], "footprint": r["Geographic footprint"],
             "solarStorage": r["Solar / storage / hybrid"], "segment": r["Segment focus"],
             "lenderVsSponsor": r["Lender IE vs sponsor/investor DD"], "classesText": r["Evidence classes"],
             "classes": classes(r["Evidence classes"]), "strength": r["V2 evidence strength"],
             "acceptance": r["Demonstrated institutional acceptance"], "differentiation": r["Technical differentiation"],
             "delivery": r["Delivery model"], "mayfieldRelevance": r["Relevance to Mayfield (competitor / partner)"],
             "evidenceNote": r["Strength & limits of public evidence"], "sourceIds": ids(r["Source IDs"])}
        if r["Firm"].startswith("Mayfield"):
            mayfield = dict(d, name="Mayfield Renewables", id="mayfield")
        elif r["Firm"] in byname:
            byname[r["Firm"]]["detail"] = d
            priority.append(byname[r["Firm"]]["id"])
        else:
            raise SystemExit(f"Priority firm not in full landscape: {r['Firm']}")

    evidence = []
    for i, r in enumerate(rows(sheet(wb, "3_")), 1):
        fs = r["Firm(s)"]
        linked = []
        for rx, name in ALIASES:
            if re.search(rx, fs) and name in byname and byname[name]["id"] not in linked:
                linked.append(byname[name]["id"])
        yr = re.findall(r"(?:19|20)\d\d", r["Date"])
        evidence.append({
            "id": f"E{i:02d}", "firmsText": fs, "firmIds": linked, "transaction": r["Transaction / document"],
            "date": r["Date"], "year": int(yr[0]) if yr else None, "counterparty": r["Financing counterparty"],
            "role": r["Firm's role / IE mechanics"], "class": int(r["Evidence class"]) if r["Evidence class"].isdigit() else None,
            "sourceIds": ids(r["Source ID(s)"]), "url": r["Primary URL"], "notes": r["Notes"],
            "excerptIds": [x.strip() for x in r.get("Excerpt IDs", "").split(",") if x.strip()],
            "projectType": r.get("Project type") or project_type(r["Transaction / document"] + " " + r["Firm's role / IE mechanics"])})
    for f in firms:
        f["evidenceIds"] = [e["id"] for e in evidence if f["id"] in e["firmIds"]]

    segments = [{"name": r["Segment"], "buyers": r["Typical buyers"], "selector": r["Who selects the IE"],
                 "reliance": r["Reliance requirement"], "competition": r["Competitive intensity"],
                 "complexity": r["Technical complexity"], "disciplines": r["Required disciplines"],
                 "providers": r["Relevant providers"], "alignment": r["Mayfield documented alignment"],
                 "differentiation": r["Potential differentiation"], "uncertainties": r["Key uncertainties"],
                 "v1": r["V1 assessment"], "v2": r["V2 assessment"]} for r in rows(sheet(wb, "4_"))]

    mrows = rows(sheet(wb, "5_"))
    mcols = [k for k in mrows[0].keys() if k != "Dimension"]
    models = {"columns": mcols, "rows": [{"dimension": r["Dimension"], "values": [r[c] for c in mcols]} for r in mrows]}

    audit = [{"id": r["Claim ID"], "claim": r["Original claim (V1 report/workbook)"], "result": r["Verification result"],
              "class": r["Evidence class"], "confidence": r["Confidence"], "sourceIds": ids(r["Source ID(s)"]),
              "url": r["Primary URL"], "correction": r["Corrections / qualifications"], "limitation": r["Unresolved limitations"]}
             for r in rows(sheet(wb, "6_"))]
    gaps = [{"id": r["Gap ID"], "question": r["Unresolved question"], "who": r["Who can answer"], "decision": r["Decision informed"]}
            for r in rows(sheet(wb, "8_"))]

    excerpts = {}
    xs = [ws for ws in wb.worksheets if ws.title.startswith("9_")]
    if xs:
        for r in rows(xs[0]):
            excerpts[r["Excerpt ID"]] = {"id": r["Excerpt ID"], "source": r["Source ID"], "document": r["Document"],
                "shows": r["What it shows"], "quote": r["Verbatim excerpt"], "start": r["Highlight start"],
                "end": r["Highlight end"], "locator": r["Location in document"], "verification": r["Verification status"],
                "firms": [x.strip() for x in r.get("Profile fact for", "").split(";") if x.strip()]}

    # integrity checks
    missing = sorted({s for f in firms for s in f["sourceIds"]} | {s for e in evidence for s in e["sourceIds"]} | {s for a in audit for s in a["sourceIds"]} - set(sources))
    missing = [m for m in missing if m not in sources]
    if missing:
        raise SystemExit(f"Source IDs referenced but missing from register: {missing}")

    narrative = json.load(open(os.path.join(HERE, "narrative.json")))
    for f in firms:
        f["factIds"] = [x["id"] for x in excerpts.values() if f["name"] in x["firms"]]
    unknown = sorted({n for x in excerpts.values() for n in x["firms"]} - set(byname))
    if unknown:
        raise SystemExit(f"Excerpts tagged to firms not in the landscape: {unknown}")
    badev = [(e["id"], x) for e in evidence for x in e["excerptIds"] if x not in excerpts]
    if badev:
        raise SystemExit(f"Evidence records reference unknown excerpts: {badev}")
    bad = [t["excerpt"] for f in narrative["findings"] for t in f.get("trail", []) if t["excerpt"] not in excerpts]
    if bad:
        raise SystemExit(f"Findings reference excerpts missing from the 9_Key_Excerpts tab: {bad}")
    badsrc = [x["id"] for x in excerpts.values() if x["source"] not in sources]
    if badsrc:
        raise SystemExit(f"Excerpts reference unknown sources: {badsrc}")
    data = {"meta": {"title": "U.S. Solar & Storage IE Market Intelligence",
                     "subtitle": "Competitive Landscape & Market Entry | Mayfield Renewables | November 2026",
                     "workbook": os.path.basename(src), "generated": datetime.date.today().isoformat(),
                     "counts": {"firms": len(firms), "priority": len(priority), "evidence": len(evidence),
                                "audit": len(audit), "sources": len(sources), "segments": len(segments), "gaps": len(gaps), "excerpts": len(excerpts)}},
            "classDefs": class_defs, "legend": legend, "firms": firms, "priority": priority, "mayfield": mayfield, "evidence": evidence,
            "excerpts": excerpts, "segments": segments, "models": models, "audit": audit, "sources": sources, "gaps": gaps, "narrative": narrative}

    jpath = os.path.join(outdir, "Mayfield_IE_Dashboard_Data.json")
    json.dump(data, open(jpath, "w"), indent=1, ensure_ascii=False)
    tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = tpl.replace("/*__DATA__*/null", payload)
    hpath = os.path.join(outdir, "Mayfield_IE_Market_Intelligence.html")
    open(hpath, "w", encoding="utf-8").write(html)
    print(json.dumps(data["meta"]["counts"]), "->", hpath)

if __name__ == "__main__":
    main()
