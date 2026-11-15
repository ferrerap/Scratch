#!/usr/bin/env python3
"""Save a subagent's full final hand-back message verbatim to a file (with provenance header).
Usage: python3 -I scripts/save_handback.py <transcript.jsonl> <out.md> <label>"""
import json, sys
t, out, label = sys.argv[1:4]
msg = None
for line in open(t, encoding="utf-8"):
    try: d = json.loads(line)
    except Exception: continue
    m = d.get("message")
    if isinstance(m, dict):
        for b in m.get("content") or []:
            if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "SubagentHandback":
                msg = (b.get("input") or {}).get("message")
if not msg: sys.exit("no handback")
hdr = (f"> Provenance note (coordinator): verbatim final hand-back of {label}, saved by `scripts/save_handback.py`. "
       "Subagents return narrative as text per harness convention (see run_log D08/D09).\n\n")
open(out, "w", encoding="utf-8").write(hdr + msg + "\n")
print(out, len(msg.split()), "words")
