#!/usr/bin/env python3
"""Validate the research handoff: registers, cross-references, revision candidates.

Usage: python3 -I scripts/validate_handoff.py <handoff_dir> [<out_md>]
handoff_dir must contain sources.json, evidence.json and may contain
research_brief.md, READ_FIRST.md, disputes_and_followups.md, revision_candidates.json.
"""
import json, re, sys, os
from collections import Counter

D = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else None
lines, errors, warnings = [], [], []

def load(name):
    p = os.path.join(D, name)
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None

SRC_F = ["source_id", "title", "authors_or_organization", "url", "publication_date", "data_collection_dates",
         "access_date", "source_type", "access_status", "underlying_evidence_group",
         "funding_or_commercial_relationships", "archived_file_path", "limitations"]
EV_F = ["evidence_id", "source_id", "research_question_ids", "proposition_tested", "observed_finding",
        "relationship", "evidence_type", "population_and_setting", "study_or_observation_method",
        "intervention_and_comparator", "outcome_measured", "quantitative_result", "source_locator",
        "short_exact_excerpt", "underlying_evidence_group", "limitations", "transferability_to_target_workflow",
        "analyst_inference", "access_status"]
ACCESS = {"full_text", "abstract_only", "partial", "other", "blocked"}
REL = {"supports", "challenges", "qualifies", "contextual"}
RQS = {"RQ1", "RQ2", "RQ3", "RQ4", "RQ5", "RQ6"}
ANCHORS = {"CL025", "CL026", "CL027", "CL029", "CL007", "K001", "AS03", "AS06"}
CHANGE = {"wording", "scope", "evidence", "relationship", "new_candidate"}

src = load("sources.json") or []
ev = load("evidence.json") or []
sids = Counter(s.get("source_id") for s in src)
eids = Counter(e.get("evidence_id") for e in ev)
for k, v in sids.items():
    if v > 1: errors.append(f"duplicate source_id {k}")
for k, v in eids.items():
    if v > 1: errors.append(f"duplicate evidence_id {k}")
for s in src:
    miss = [f for f in SRC_F if f not in s]
    if miss: errors.append(f"{s.get('source_id')}: missing fields {miss}")
    if not re.fullmatch(r"SRC\d{3}", s.get("source_id", "")): errors.append(f"bad source id {s.get('source_id')}")
    if s.get("access_status") not in ACCESS: errors.append(f"{s['source_id']}: access_status {s.get('access_status')!r}")
    if not s.get("url"): warnings.append(f"{s['source_id']}: no URL")
    if not s.get("limitations"): warnings.append(f"{s['source_id']}: no limitations recorded")
src_ids = set(sids)
ev_by_src = Counter()
for e in ev:
    eid = e.get("evidence_id")
    miss = [f for f in EV_F if f not in e]
    if miss: errors.append(f"{eid}: missing fields {miss}")
    if e.get("source_id") not in src_ids: errors.append(f"{eid}: source_id {e.get('source_id')} unresolved")
    ev_by_src[e.get("source_id")] += 1
    if e.get("relationship") not in REL: errors.append(f"{eid}: relationship {e.get('relationship')!r}")
    if e.get("access_status") not in ACCESS: errors.append(f"{eid}: access_status {e.get('access_status')!r}")
    bad = [q for q in (e.get("research_question_ids") or []) if q not in RQS]
    if bad or not e.get("research_question_ids"): errors.append(f"{eid}: research_question_ids {e.get('research_question_ids')}")
    loc = (e.get("source_locator") or "").strip()
    if not loc: errors.append(f"{eid}: empty source_locator")
    elif "not located" in loc.lower(): warnings.append(f"{eid}: source_locator 'not located'")
    ex = e.get("short_exact_excerpt")
    if ex and len(ex.split()) > 60: warnings.append(f"{eid}: excerpt {len(ex.split())} words (>60)")
    if not e.get("analyst_inference"): warnings.append(f"{eid}: no analyst_inference")
for s in src:
    if ev_by_src[s["source_id"]] == 0: warnings.append(f"{s['source_id']}: no evidence items reference this source")

ev_ids, dis_ids = set(eids), set()
def check_refs(name, text):
    refs = set(re.findall(r"\b(EVR\d{3}|SRC\d{3}|DIS\d{3}|REV\d{3})\b", text))
    bad = [r for r in refs if (r.startswith("EVR") and r not in ev_ids) or (r.startswith("SRC") and r not in src_ids)]
    if bad: errors.append(f"{name}: unresolved IDs {sorted(bad)}")
    return refs

rc = load("revision_candidates.json")
rev_ids = set()
if rc is not None:
    items = rc if isinstance(rc, list) else rc.get("revision_candidates", [])
    for r in items:
        rid = r.get("revision_id"); rev_ids.add(rid)
        for f in ["revision_id", "target_claim_id", "research_question_ids", "proposed_wording_or_qualification",
                  "supporting_evidence_ids", "challenging_evidence_ids", "rationale", "unresolved_user_judgment", "change_type"]:
            if f not in r: errors.append(f"{rid}: missing {f}")
        if r.get("target_claim_id") not in ANCHORS | {None}: errors.append(f"{rid}: target_claim_id {r.get('target_claim_id')} not a known anchor")
        if r.get("change_type") not in CHANGE: errors.append(f"{rid}: change_type {r.get('change_type')}")
        for k in ("supporting_evidence_ids", "challenging_evidence_ids"):
            bad = [x for x in r.get(k) or [] if x not in ev_ids]
            if bad: errors.append(f"{rid}: {k} unresolved {bad}")
        if any("conviction" in k.lower() for k in r.keys()): errors.append(f"{rid}: contains a conviction field")

for name in ["research_brief.md", "READ_FIRST.md", "disputes_and_followups.md", "run_log.md"]:
    p = os.path.join(D, name)
    if not os.path.exists(p):
        warnings.append(f"{name} not present"); continue
    text = open(p, encoding="utf-8").read()
    refs = check_refs(name, text)
    if name == "disputes_and_followups.md":
        dis_ids = set(r for r in refs if r.startswith("DIS"))
    if name == "research_brief.md":
        # bullets / paragraphs with claim-like content and no evidence ID
        unref = []
        for para in re.split(r"\n\s*\n|\n(?=[-*] )", text):
            t = para.strip()
            if not t or t.startswith("#") or t.startswith("|") or len(t) < 140: continue
            if re.search(r"EVR\d{3}|SRC\d{3}|DIS\d{3}|REV\d{3}", t): continue
            if re.match(r"^(>|\*\*Analyst|_Analyst|Analyst inference|Note|Scope)", t): continue
            unref.append(t[:110].replace("\n", " "))
        if unref:
            warnings.append(f"research_brief.md: {len(unref)} long paragraphs without evidence IDs (review manually):")
            warnings.extend("   - " + u for u in unref)

abstract_only = [f"{s['source_id']} ({s['access_status']}): {s['title'][:80]}" for s in src if s.get("access_status") != "full_text"]
egs = Counter(s.get("underlying_evidence_group") for s in src)

lines.append("# Validation results\n")
lines.append(f"- Sources: {len(src)}; evidence items: {len(ev)}; underlying evidence groups: {len(egs)}")
lines.append(f"- Revision candidates: {len(rev_ids)}; disputes referenced in disputes file: {len(dis_ids)}")
lines.append(f"- Errors: {len(errors)}; warnings: {len(warnings)}\n")
lines.append("## Errors"); lines += ["- " + x for x in errors] or ["- none"]
lines.append("\n## Warnings"); lines += ["- " + x for x in warnings] or ["- none"]
lines.append("\n## Sources not reviewed in full text (access_status != full_text)")
lines += ["- " + x for x in abstract_only] or ["- none"]
lines.append("\n## Evidence groups with more than one document")
lines += [f"- {k}: {v} documents" for k, v in egs.items() if v > 1] or ["- none"]
out = "\n".join(lines) + "\n"
if OUT:
    open(OUT, "w", encoding="utf-8").write(out)
print(out[:4000])
sys.exit(1 if errors else 0)
