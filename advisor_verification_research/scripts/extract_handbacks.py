#!/usr/bin/env python3
"""Extract a subagent's final hand-back message verbatim from its transcript and
save it into its workstream folder (the harness asks subagents to return report
.md content to the coordinator instead of writing it).

Writes:
  <ws_dir>/final_message_to_coordinator.md   (full verbatim hand-back)
  <ws_dir>/report.md                          (section after the report marker)
  <ws_dir>/search_log.md                      (section after the search-log marker, if any
                                               and only if no search_log.md written by the worker)
Usage: python3 -I extract_handbacks.py <transcript.jsonl> <ws_dir> <label>
"""
import json, re, sys, os

tpath, wsdir, label = sys.argv[1], sys.argv[2], sys.argv[3]
msg = None
for line in open(tpath, encoding="utf-8"):
    try:
        d = json.loads(line)
    except Exception:
        continue
    m = d.get("message")
    if not isinstance(m, dict):
        continue
    for b in m.get("content") or []:
        if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "SubagentHandback":
            msg = (b.get("input") or {}).get("message")
if not msg:
    print("no handback found"); sys.exit(1)

HDR = ("> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from "
       f"{label}'s final hand-back message. The harness asks subagents to return report .md content to the "
       "coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.\n\n")
open(os.path.join(wsdir, "final_message_to_coordinator.md"), "w", encoding="utf-8").write(HDR + msg + "\n")

lines = msg.splitlines()
rep_re = re.compile(r"(content for report\.md|appendix a\b.*report\.md|^#+\s*report\.md)", re.I)
log_re = re.compile(r"(content for search_log\.md|appendix b\b.*search_log\.md)", re.I)
ri = next((i for i, l in enumerate(lines) if rep_re.search(l)), None)
li = next((i for i, l in enumerate(lines) if log_re.search(l)), None)

def clean(block):
    out = [l for l in block if not re.fullmatch(r"\s*=+\s*", l)]
    while out and not out[0].strip(): out.pop(0)
    while out and (not out[-1].strip() or re.fullmatch(r"\s*-{3,}\s*", out[-1])): out.pop()
    return "\n".join(out) + "\n"

if ri is not None:
    end = li if (li is not None and li > ri) else len(lines)
    open(os.path.join(wsdir, "report.md"), "w", encoding="utf-8").write(HDR + clean(lines[ri + 1:end]))
    print("report.md lines:", end - ri - 1)
else:
    print("no report marker; full message saved only")
slp = os.path.join(wsdir, "search_log.md")
if li is not None:
    worker_written = os.path.exists(slp) and "Provenance note (coordinator)" not in open(slp, encoding="utf-8").read()
    if worker_written:
        print("search_log.md written by worker; kept")
    else:
        open(slp, "w", encoding="utf-8").write(HDR + clean(lines[li + 1:]))
        print("search_log.md lines:", len(lines) - li - 1)
