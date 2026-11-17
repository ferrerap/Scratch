import sys, re, json, os
sys.path.insert(0, os.path.dirname(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'qa'))
from excerpts import EXCERPTS
from txt import text
DL = os.path.join(os.path.dirname(__file__), '..', 'dl')
def squash(s): return re.sub(r'\s+', '', s.replace('‘',"'").replace('’',"'").replace('“','"').replace('”','"'))
res = {}
for x in EXCERPTS:
    xid, sid, doc, shows, quote, st, en, loc, local = x
    if not local:
        res[xid] = "Not re-checked: page blocks automated retrieval; excerpt from first-stage research notes"; continue
    t = squash(text(os.path.join(DL, local)))
    ok = squash(quote) in t and (not st or squash(st) in t) and (not en or squash(en) in t)
    if st and en and ok:
        ok = t.find(squash(en), t.find(squash(st))) >= 0
    res[xid] = "Verified verbatim against retrieved copy (2026-11-17)" if ok else "FAILED"
    print(xid, sid, res[xid][:20])
json.dump(res, open(os.path.join(os.path.dirname(__file__), 'excerpt_verification.json'), 'w'), indent=1)
