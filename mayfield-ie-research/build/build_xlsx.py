import sys, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
sys.path.insert(0, sys.argv[1])
from sources import SOURCES, SRC
from firms import FIRMS, PRIORITY, PRIORITY_ORDER
from analysis import CLASS_DEF, EVIDENCE, EVIDENCE_PTYPE, AUDIT, SEGMENTS, MODELS, GAPS

orig = openpyxl.load_workbook(sys.argv[2])
out = sys.argv[3]
wb = openpyxl.Workbook()
HDR = PatternFill("solid", fgColor="1F3864"); HF = Font(bold=True, color="FFFFFF", size=10)
BF = Font(size=10); WRAP = Alignment(wrap_text=True, vertical="top")
thin = Side(style="thin", color="BFBFBF"); BOR = Border(top=thin, bottom=thin, left=thin, right=thin)

def first_url(ids):
    for i in [x.strip() for x in ids.replace(";", ",").split(",")]:
        if i in SRC: return SRC[i][5]
    return ""

def sheet(title, headers, rows, widths, first=False):
    ws = wb.active if first else wb.create_sheet()
    ws.title = title
    ws.append(headers)
    for r in rows: ws.append(list(r))
    for c in ws[1]:
        c.fill = HDR; c.font = HF; c.alignment = Alignment(wrap_text=True, vertical="center"); c.border = BOR
    for row in ws.iter_rows(min_row=2):
        for c in row: c.font = BF; c.alignment = WRAP; c.border = BOR
    for i, w in enumerate(widths, 1): ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "B2"
    ws.auto_filter.ref = ws.dimensions
    ws.row_dimensions[1].height = 32
    return ws

# README
ws = wb.active; ws.title = "README"
readme = [
("Mayfield IE Competitive Landscape — Verified V2", ""),
("Prepared", "17 November 2026, for Mayfield Renewables leadership. Companion to the report 'U.S. Solar & Storage Independent Engineering: Competitive Landscape and Market Entry Considerations for Mayfield Renewables'."),
("What changed from V1", "V1 (mayfield_ie_competitive_landscape.xlsx, preserved unchanged in Drive and reproduced in the V1_ tabs) was reconstructed from the Deep Research narrative and had no URLs. V2 re-verifies the most consequential claims against primary sources (SEC-filed financing agreements and IE reports, lender and sponsor announcements, company service pages, public procurements), adds 6 firms (4 identified from SEC-filed approved-engineer schedules), and introduces a five-level evidence classification."),
("Tabs", "1_Full_Landscape (40 firms: 34 from V1 + 6 added) · 2_Priority_Competitors (15 firms + Mayfield reference) · 3_Evidence_References (transaction-level evidence) · 4_Market_Segments · 5_Business_Models · 6_Evidence_Audit (36 audited claims) · 7_Source_Register (98 sources) · 8_Open_Gaps · V1_* (original workbook, unchanged)"),
("Evidence classes", "Classes describe the public evidence of financing acceptance, NOT technical competence. A firm may hold several classes. Absence of public evidence is not evidence of no financing experience."),
] + [(f"Class {c[0]} – {c[1]}", c[2]) for c in CLASS_DEF] + [
("V2 evidence strength", "Strong = class 1 evidence in executed agreements and/or repeated class 2–3 in primary documents · Moderate = class 2/3 present but mainly company-reported or dated · Limited = class 4 or dated class 3 only · Thin = class 5 only · Not re-verified = not checked in V2"),
("Verification method", "Second-stage verification was conducted with Claude and its web-search and document-retrieval tools: original documents were retrieved and examined, claims were cross-checked against them, and the operative text of key contractual provisions (IE definitions, approved-engineer schedules, reliance cap) was extracted verbatim from SEC exhibits. These checks were AI-assisted rather than performed by an independent human reviewer; each is recorded with its source so it can be retraced. 'Access status' in the Source Register records whether a source was opened, seen only as a search snippet, or failed."),
("Limits", "Desk research only. No interviews have been conducted. Fees, approval frequency and demand are not publicly documented and are listed in 8_Open_Gaps. Signed reliance letters were not sighted."),
("How to update", "Add new evidence as rows in 3_Evidence_References with a Source ID; add the source to 7_Source_Register; then update the firm's 'Evidence classes found' and 'V2 evidence strength' in 1_Full_Landscape."),
]
for r in readme: ws.append(r)
ws["A1"].font = Font(bold=True, size=14, color="1F3864")
for row in ws.iter_rows(min_row=2):
    row[0].font = Font(bold=True, size=10); row[0].alignment = WRAP
    row[1].font = BF; row[1].alignment = WRAP
ws.column_dimensions["A"].width = 34; ws.column_dimensions["B"].width = 120

# 1 Full landscape
rows = []
for f in FIRMS:
    rows.append((f["firm"], f["cat"], f["v1tier"], f["scale"], f["tech"], f["segs"], f["orient"], f["classes"], f["refs"],
                 f["v1class"], f["v1conf"], f["v2str"], f["change"], f["relevance"], "Yes" if f["priority"]=="Y" else "No",
                 f["srcs"], f["status"]))
sheet("1_Full_Landscape", ["Firm","V2 category","V1 tier (original)","Ownership / scale (public)","Technologies","Segment focus",
 "Service orientation","Evidence classes found (1–5)","Key documented references","V1 evidence classification","V1 confidence",
 "V2 evidence strength","Change vs V1","Relevance to Mayfield","Priority shortlist","Source IDs","Research status"],
 rows, [24,30,20,30,18,26,26,12,60,24,10,14,40,32,10,22,20])

# 2 Priority
byname = {f["firm"]: f for f in FIRMS}
rows = []
for n in PRIORITY_ORDER:
    p = PRIORITY[n]; f = byname[n]
    rows.append((n, p["group"], f["scale"], p["footprint"], p["solar_storage"], p["segment"], p["lender_vs_sponsor"], f["classes"], f["v2str"],
                 p["accept"], p["diff"], p["delivery"], p["mayfield"], p["evid_note"], f["srcs"]))
rows.append(("Mayfield Renewables (reference)","Prospective entrant","Corvallis OR; founded 2007; headcount not public","U.S.; projects in many states; individual PEs licensed in MA, CA, GA, NJ, MD, FL",
 "Solar, storage, microgrids","C&I; microgrids; small utility-scale; community solar design","Design/EOR; OE; advertises desktop IE review, pre-finance TDD, energy-yield validation, technical design review","5","Thin (public)",
 "No public evidence of named lender/investor reliance","Microgrid/C&I depth; codes (NEC panel participation); Mayfield Standard; education platform","In-house engineering team","—","Non-public references may exist (internal input needed)","S77, S78, S79, S81, S95, S96"))
sheet("2_Priority_Competitors", ["Firm","Group","Ownership / scale","Geographic footprint","Solar / storage / hybrid","Segment focus","Lender IE vs sponsor/investor DD",
 "Evidence classes","V2 evidence strength","Demonstrated institutional acceptance","Technical differentiation","Delivery model","Relevance to Mayfield (competitor / partner)",
 "Strength & limits of public evidence","Source IDs"], rows, [24,18,28,24,18,26,26,10,14,36,34,20,34,30,22])

# 3 Evidence references
rows = [(e[0], e[1], e[2], e[3], e[4], e[5], e[6], first_url(e[6]), e[7], EVIDENCE_PTYPE[i]) for i, e in enumerate(EVIDENCE)]
sheet("3_Evidence_References", ["Firm(s)","Transaction / document","Date","Financing counterparty","Firm's role / IE mechanics","Evidence class",
 "Source ID(s)","Primary URL","Notes","Project type"], rows, [28,44,14,34,44,9,12,50,36,24])

# 4 Segments
rows = [(s["seg"], s["buyers"], s["selector"], s["reliance"], s["competition"], s["complexity"], s["disciplines"], s["providers"],
         s["alignment"], s["diff"], s["uncert"], s["v1"], s["v2"]) for s in SEGMENTS]
sheet("4_Market_Segments", ["Segment","Typical buyers","Who selects the IE","Reliance requirement","Competitive intensity","Technical complexity",
 "Required disciplines","Relevant providers","Mayfield documented alignment","Potential differentiation","Key uncertainties","V1 assessment","V2 assessment"],
 rows, [28,30,32,26,30,26,32,26,30,26,28,24,28])

# 5 Business models
sheet("5_Business_Models", ["Dimension","Model A – Lender-facing IE","Model B – Sponsor-side diligence & finance readiness","Model C – Technology-enabled evidence standardization"],
 MODELS, [28,50,50,50])

# 6 Audit
rows = [(a[0], a[1], a[2], a[3], a[4], a[5], first_url(a[5]), a[6], a[7]) for a in AUDIT]
sheet("6_Evidence_Audit", ["Claim ID","Original claim (V1 report/workbook)","Verification result","Evidence class","Confidence","Source ID(s)","Primary URL",
 "Corrections / qualifications","Unresolved limitations"], rows, [9,50,20,10,12,16,46,56,36])

# 7 Source register
rows = [(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]) for s in SOURCES]
sheet("7_Source_Register", ["Source ID","Title","Publisher","Date","Source type","URL","Access status (2026-11-17)","Used for"], rows, [9,60,22,16,24,60,26,46])

# 8 Gaps
sheet("8_Open_Gaps", ["Gap ID","Unresolved question","Who can answer","Decision informed"], GAPS, [9,80,36,30])

# V1 copies
for w in orig.worksheets:
    n = wb.create_sheet("V1_" + w.title.replace(" ", "_"))
    for r in w.iter_rows(values_only=True): n.append(list(r))
    for c in n[1]: c.font = Font(bold=True)
    for i in range(1, n.max_column + 1): n.column_dimensions[get_column_letter(i)].width = 28
    n.freeze_panes = "B2"
wb.save(out)
print("saved", out, [w.title for w in wb.worksheets])
