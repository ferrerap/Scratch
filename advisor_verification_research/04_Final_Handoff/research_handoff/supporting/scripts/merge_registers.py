#!/usr/bin/env python3
"""Merge workstream registers into stable SRC/EVR registers.

Reads every */sources.json and */evidence.json under the given input dirs
(workstream folders and follow-up folders), deduplicates sources by normalized
URL / normalized title (plus manual overrides), assigns stable IDs in
first-appearance order, and writes:
  01_Evidence/sources.json, 01_Evidence/evidence.json, 01_Evidence/id_mapping.json,
  01_Evidence/register_stats.json

If 01_Evidence/id_mapping.json already exists, previously assigned stable IDs
are preserved (new items get the next free IDs), so IDs stay stable across
re-merges.

Usage: python3 -I scripts/merge_registers.py <project_root>
"""
import json, re, sys, os, glob
from collections import OrderedDict, Counter

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
EV_DIR = os.path.join(ROOT, "01_Evidence")
OVR_PATH = os.path.join(ROOT, "scripts", "manual_overrides.json")
MAP_PATH = os.path.join(EV_DIR, "id_mapping.json")

ACCESS_RANK = {"full_text": 0, "partial": 1, "abstract_only": 2, "other": 3, "blocked": 4}

def norm_url(u):
    if not u:
        return None
    u = u.strip().lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    u = u.split("#")[0]
    u = u.rstrip("/")
    # arXiv abs/pdf + version normalization
    m = re.match(r"arxiv\.org/(abs|pdf)/([0-9]{4}\.[0-9]{4,5})(v\d+)?(\.pdf)?", u)
    if m:
        return "arxiv:" + m.group(2)
    m = re.match(r"(dx\.)?doi\.org/(.+)", u)
    if m:
        return "doi:" + m.group(2)
    return u

def norm_title(t):
    if not t:
        return None
    t = t.lower()
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t[:120] if len(t) >= 25 else None  # short titles too ambiguous

def load_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def main():
    ovr = load_json(OVR_PATH) if os.path.exists(OVR_PATH) else {}
    forced_merge = ovr.get("source_merge", [])      # list of lists of temp ids
    no_merge = set(tuple(sorted(x)) for x in ovr.get("source_no_merge", []))
    eg_alias = ovr.get("eg_alias", {})
    drop_sources = set(ovr.get("drop_sources", []))
    drop_evidence = set(ovr.get("drop_evidence", []))
    source_patch = ovr.get("source_patch", {})      # temp_or_stable id -> fields
    evidence_patch = ovr.get("evidence_patch", {})

    prior = load_json(MAP_PATH) if os.path.exists(MAP_PATH) else {"sources": {}, "evidence": {}}

    pending = set(ovr.get("pending_dirs", []))
    r3 = [d for d in sorted(glob.glob(os.path.join(ROOT, "03_Challenge_and_Followup", "R3*"))) if os.path.isdir(d)]
    r3 = [d for d in r3 if os.path.basename(d) not in pending]
    # coordinator corrections folder last so its temp IDs follow the follow-up workers
    r3 = [d for d in r3 if not os.path.basename(d).startswith("R3_")] + [d for d in r3 if os.path.basename(d).startswith("R3_")]
    dirs = sorted(glob.glob(os.path.join(ROOT, "02_Workstreams", "*"))) + r3
    all_src, all_ev = [], []
    for d in dirs:
        sp, ep = os.path.join(d, "sources.json"), os.path.join(d, "evidence.json")
        ws = os.path.basename(d)
        if os.path.exists(sp):
            for s in load_json(sp):
                s["_ws"] = ws
                all_src.append(s)
        if os.path.exists(ep):
            for e in load_json(ep):
                e["_ws"] = ws
                all_ev.append(e)

    all_src = [s for s in all_src if s.get("source_id") not in drop_sources]
    all_ev = [e for e in all_ev if e.get("evidence_id") not in drop_evidence]

    # union-find over temp source ids
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        if tuple(sorted((a, b))) in no_merge:
            return
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    key_owner = {}
    for s in all_src:
        tid = s["source_id"]
        find(tid)
        for k in (("u", norm_url(s.get("url"))), ("t", norm_title(s.get("title")))):
            if k[1] is None:
                continue
            if k in key_owner:
                union(key_owner[k], tid)
            else:
                key_owner[k] = tid
    for grp in forced_merge:
        for t in grp[1:]:
            union(grp[0], t)

    groups = OrderedDict()
    for s in all_src:
        groups.setdefault(find(s["source_id"]), []).append(s)

    # stable ID assignment
    prior_src = prior.get("sources", {})  # temp -> SRC
    used = set(prior_src.values())
    next_n = 1 + max([int(v[3:]) for v in used] or [0])
    temp2src, sources_out = {}, []
    for root, members in groups.items():
        sid = None
        for m in members:
            if m["source_id"] in prior_src:
                sid = prior_src[m["source_id"]]
                break
        if sid is None:
            sid = "SRC%03d" % next_n
            next_n += 1
        members_sorted = sorted(members, key=lambda m: ACCESS_RANK.get(m.get("access_status"), 5))
        best = dict(members_sorted[0])
        rec = OrderedDict()
        rec["source_id"] = sid
        for f in ["title", "authors_or_organization", "url", "publication_date", "data_collection_dates",
                  "access_date", "source_type", "access_status", "underlying_evidence_group",
                  "funding_or_commercial_relationships", "archived_file_path", "limitations"]:
            rec[f] = best.get(f)
        lims = []
        for m in members_sorted:
            l = m.get("limitations")
            if l and l not in lims:
                lims.append(l)
        if len(lims) > 1:
            rec["limitations"] = " | ".join(lims)
        eg = rec.get("underlying_evidence_group")
        rec["underlying_evidence_group"] = eg_alias.get(eg, eg)
        rec["contributing_workstreams"] = sorted(set(m["_ws"] for m in members))
        rec["temp_ids"] = [m["source_id"] for m in members]
        for m in members:
            temp2src[m["source_id"]] = sid
        sources_out.append(rec)

    # unify EG labels within merged groups is done via alias; also make EG label consistent per SRC
    for rec in sources_out:
        p = source_patch.get(rec["source_id"])
        if p:
            rec.update(p)
    sources_out.sort(key=lambda r: r["source_id"])
    src_by_id = {r["source_id"]: r for r in sources_out}

    prior_ev = prior.get("evidence", {})
    used_e = set(prior_ev.values())
    next_e = 1 + max([int(v[3:]) for v in used_e] or [0])
    ev_out, temp2ev, unresolved = [], {}, []
    for e in all_ev:
        tid = e["evidence_id"]
        key = e["_ws"] + "::" + tid
        eid = prior_ev.get(key) or prior_ev.get(tid)
        if eid is None:
            eid = "EVR%03d" % next_e
            next_e += 1
        temp2ev[key] = eid
        sid = temp2src.get(e.get("source_id"))
        if sid is None:
            unresolved.append((e["_ws"], tid, e.get("source_id")))
        rec = OrderedDict()
        rec["evidence_id"] = eid
        rec["source_id"] = sid
        for f in ["research_question_ids", "proposition_tested", "work_type_tags", "concept_tags",
                  "observed_finding", "relationship", "evidence_type", "population_and_setting",
                  "study_or_observation_method", "intervention_and_comparator", "outcome_measured",
                  "quantitative_result", "source_locator", "short_exact_excerpt"]:
            rec[f] = e.get(f)
        eg = src_by_id[sid]["underlying_evidence_group"] if sid else e.get("underlying_evidence_group")
        rec["underlying_evidence_group"] = eg_alias.get(eg, eg)
        for f in ["limitations", "transferability_to_target_workflow", "analyst_inference", "access_status"]:
            rec[f] = e.get(f)
        rec["workstream"] = e["_ws"]
        rec["temp_id"] = tid
        p = evidence_patch.get(eid)
        if p:
            rec.update(p)
        ev_out.append(rec)
    ev_out.sort(key=lambda r: r["evidence_id"])

    os.makedirs(EV_DIR, exist_ok=True)
    with open(os.path.join(EV_DIR, "sources.json"), "w", encoding="utf-8") as f:
        json.dump(sources_out, f, indent=2, ensure_ascii=False)
    with open(os.path.join(EV_DIR, "evidence.json"), "w", encoding="utf-8") as f:
        json.dump(ev_out, f, indent=2, ensure_ascii=False)
    with open(MAP_PATH, "w", encoding="utf-8") as f:
        json.dump({"sources": temp2src, "evidence": temp2ev}, f, indent=2)

    egs = Counter(r["underlying_evidence_group"] for r in sources_out)
    stats = OrderedDict()
    stats["n_sources"] = len(sources_out)
    stats["n_evidence"] = len(ev_out)
    stats["n_underlying_evidence_groups"] = len(egs)
    stats["multi_document_groups"] = {k: v for k, v in egs.items() if v > 1}
    stats["merged_sources"] = {r["source_id"]: r["temp_ids"] for r in sources_out if len(r["temp_ids"]) > 1}
    stats["by_access_status"] = Counter(r["access_status"] for r in sources_out)
    stats["by_source_type"] = Counter(r["source_type"] for r in sources_out)
    rq = Counter()
    for e in ev_out:
        for q in e.get("research_question_ids") or []:
            rq[q] += 1
    stats["evidence_by_rq"] = rq
    rel = Counter(e.get("relationship") for e in ev_out)
    stats["evidence_by_relationship"] = rel
    prop = Counter()
    for e in ev_out:
        pt = e.get("proposition_tested") or ""
        for m in re.findall(r"P\d\.\d|P-NEW", pt):
            prop[(m, e.get("relationship"))] += 1
    stats["evidence_by_proposition_relationship"] = {f"{k[0]}|{k[1]}": v for k, v in sorted(prop.items())}
    stats["unresolved_evidence_source_links"] = unresolved
    with open(os.path.join(EV_DIR, "register_stats.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, default=dict)
    print(json.dumps({k: stats[k] for k in ["n_sources", "n_evidence", "n_underlying_evidence_groups"]}))
    print("merged:", stats["merged_sources"])
    print("multi-doc EGs:", stats["multi_document_groups"])
    print("unresolved links:", unresolved)

if __name__ == "__main__":
    main()
