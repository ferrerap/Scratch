import sys
sys.path.insert(0, sys.argv[1])
from docx_util import new_doc, para, table, NAVY
from docx.shared import Inches

d = new_doc(10)
B = "List Bullet"
t = para(d, "Mayfield IE Market — Primary Research and Validation Plan", size=17, after=2)
for r in t.runs: r.bold = True; r.font.color.rgb = NAVY
para(d, "Companion to \"U.S. Solar & Storage Independent Engineering: Competitive Landscape and Market Entry Considerations for Mayfield Renewables\"  ·  November 2026", size=9, italic=True, after=6)
para(d, "**Purpose.** The desk research established how IEs are designated in financing documents and who holds documented acceptance. It could not establish how often lenders approve a new IE, what customers pay, or whether demand exists for Mayfield's proposed offers. This plan sets out the questions that only interviews and internal data can answer, the hypotheses each interview is designed to test, and the decision each answer informs. No interviews have been conducted yet. The plan is built to disprove the entry thesis as readily as to confirm it.")

d.add_heading("1. Ten highest-priority unresolved questions", 1)
Q = [
("1", "How often do lenders approve an IE that is not named in the credit agreement, and what evidence persuades them?", "Agreements allow a 'reputable, qualified' alternative approved by lenders, but no approval data exist; lists change slowly.", "Model A go/no-go"),
("2", "Are DG/community-solar, C&I, private-credit and green-bank lenders more open to a new IE than utility-scale bank groups?", "Mixed evidence: incumbents on disclosed bank DG deals vs. broad 2018 DG list and borrower-selected IE in one facility.", "Which segment to target first"),
("3", "Who actually chooses the IE in DG portfolio financings – the sponsor, the lead arranger or lender counsel?", "Documents show lender control; sponsors often engage and pay.", "Who Mayfield sells to"),
("4", "How much does firm-level track record matter compared with the individual track record of the engineer leading the work?", "Agreements screen on firm 'experience'; whether an experienced hire substitutes is unknown.", "Hire vs. partner vs. acquire"),
("5", "What reliance-letter, liability-cap and professional-liability terms do lenders require, and are they insurable for Mayfield?", "One incumbent caps reliance liability at USD 300,000 in an ABS context; no market standard found.", "Model A feasibility and cost"),
("6", "What do sponsors pay for lender IE and for pre-finance diligence, and what drives their choice of provider?", "No public fee data.", "Pricing; Model B economics"),
("7", "Where do incumbent IEs fall short for C&I, microgrid, storage and small-portfolio clients?", "Lender commentary confirms diligence friction on small deals; specific shortcomings are undocumented.", "Positioning and differentiation"),
("8", "Would sponsors or lenders pay for finance-readiness and evidence standardization, and does it measurably shorten lender diligence?", "Incumbents already use portfolio sampling; willingness to pay is undocumented.", "Model C viability"),
("9", "Which disciplines can be subcontracted (resource assessment, civil/geotech, BESS degradation) without weakening lender acceptance?", "Lenders review the IE's scope; subcontracting practice is undocumented.", "Delivery model and partners"),
("10", "How much of Mayfield's pipeline would be ruled out by independence conflicts with its design work?", "Agreements exclude affiliates; acting as EOR on the same asset is a practical conflict.", "Addressable IE market; conflict policy"),
]
table(d, ["#", "Question", "What desk research showed", "Decision informed"], Q, [0.3, 2.6, 2.55, 1.45], size=8)

d.add_heading("2. Interview program (8 archetypes, 6–8 interviews minimum)", 1)
para(d, "Prioritize I-1, I-2, I-4 and I-7. Each interview should take 45 minutes, be conducted under a no-attribution understanding, and never request confidential deal terms.")
I = [
("I-1  DG / C&I project-finance lender (bank)", "Credit officer or IE/technical lead at a bank active in DG, community-solar or C&I portfolio debt (regional bank or the DG desk of a large lender).",
 "H1: The bank will approve a non-listed IE on a transaction basis when the sponsor proposes a firm with experienced personnel, documented QA and insurable reliance terms – without requiring a minimum number of prior firm-level lender engagements.",
 ["When did you last approve an IE that was new to you, and what made it acceptable?", "Is approval held at bank, desk or transaction level? Who has the veto?", "What minimum firm-level transaction history do you require? Would an experienced individual lead change your answer?", "Would you require a second report from an established IE alongside a new firm's?", "What would cause you to reject a technically strong firm outright?"],
 "Supports: recent approval of a new IE; criteria stated as people, process and insurance. Contradicts: a fixed panel; a minimum firm-level count (e.g., 5–10 deals); a routine second-opinion requirement.",
 "If contradicted by two or more lenders, deprioritize Model A in bank-led DG and pursue teaming or acquisition."),
("I-2  Private-credit or specialty lender", "Investment or technical director at a private-credit, infrastructure-debt or specialty fund financing smaller BESS, C&I or DG assets.",
 "H2: Private-credit lenders choose IEs on expertise and turnaround more than incumbency, and are more open to specialists than banks.",
 ["How do you choose the IE on smaller deals ($10–50M)?", "Have you used a specialist IE instead of a large firm? Why?", "Which reliance terms and liability caps do you accept?", "What technical issues most often delay your closings?"],
 "Supports: specialists chosen for depth or speed; flexible reliance terms. Contradicts: same incumbents as banks; deference to the co-lender's choice.",
 "Determines whether private credit is the first Model A target."),
("I-3  Green bank or mission lender", "Investment or technical staff at a state green bank or CDFI lending to community solar, C&I or resilience projects.",
 "H3: Public lenders offer a qualification pathway that lets small firms do lender-side technical review, not only inspections or technical assistance.",
 ["How do you qualify technical advisers – panel RFQ, per-deal or preferred list?", "What experience, insurance and independence terms are non-negotiable?", "Would you rely on a sponsor-commissioned review?", "Are there small-firm or local-firm pathways?"],
 "Supports: panel or RFQ open to small firms for lender-side review. Contradicts: technical assistance roles only; or experience thresholds that exclude Mayfield.",
 "Decides whether to respond to green-bank RFQs as a reference-building route."),
("I-4  DG / community-solar developer, capital-markets lead", "Head of capital markets or project finance at a DG, community-solar or C&I platform that finances portfolios repeatedly.",
 "H4: Sponsors materially influence IE choice in portfolio financings and would pay for a pre-finance review that reduces IE findings and rework.",
 ["Who proposed the IE on your last two financings? Did lenders accept your nominee?", "Where does IE diligence create rework or delay? What did it cost you?", "Would you pay for a finance-readiness review before the lender's IE starts? What would it need to deliver, at what price?", "What frustrates you about incumbent IEs?"],
 "Supports: sponsor nomination accepted; quantified rework; stated willingness to pay. Contradicts: lender dictates the IE; no budget for a second review.",
 "Validates Model B demand and pricing; identifies the sales channel for Model A."),
("I-5  C&I / microgrid developer or owner (incl. existing Mayfield clients)", "Development, engineering or finance lead at a C&I or microgrid developer.",
 "H5: Financing of complex C&I/microgrid projects is delayed by technical-evidence gaps that Mayfield's design and Standard expertise can close, and clients will pay for it separately from design.",
 ["What technical issues have stopped or delayed a financing?", "Who reviewed the technical package for the financier, and how long did it take?", "Would a standardized evidence package help credit teams, or only your internal team?", "Who would pay – you, the financier or the EPC?"],
 "Supports: recurring, specific gaps; a willing payer. Contradicts: financier requirements are light; problems are commercial, not technical.",
 "Informs Model B scope and Model C value proposition."),
("I-6  Boutique IE principal or former incumbent IE manager", "Principal at a specialist IE, or a senior manager formerly at a large IE.",
 "H6: Specialist firms first won lender acceptance through the founders' personal track records plus a specific sponsor or lender who vouched for them, and some disciplines can be subcontracted without harm.",
 ["How was your first lender-relied engagement won?", "How many references changed sales conversations?", "Which disciplines must be in-house? What can be subcontracted?", "What is the review and sign-off hierarchy? Where do new entrants underestimate the work?", "Do you subcontract C&I, microgrid or codes specialists?"],
 "Supports: a replicable path; openness to teaming. Contradicts: acceptance took many years; subcontracting discouraged.",
 "Informs hiring, partner model and realistic timeline."),
("I-7  Project-finance counsel and professional-liability broker", "Lender-side or sponsor-side project-finance attorney; broker specializing in engineering professional liability.",
 "H7: Reliance and certification terms acceptable to lenders can be insured for a firm of Mayfield's size at a cost the economics can bear, and liability caps are negotiable.",
 ["Which reliance clauses create the most uninsured exposure?", "What liability caps and coverage limits do lenders accept from smaller IEs?", "How are draw certificates treated by insurers?", "What should a new IE refuse to certify?"],
 "Supports: insurable standard terms; negotiable caps. Contradicts: required limits or exclusions that make Model A uninsurable or uneconomic.",
 "Gate for any Model A engagement."),
("I-8  Tax-equity investor or M&A technical director (optional)", "Technical diligence lead at a tax-equity investor, infrastructure fund or acquirer of DG portfolios.",
 "H8: Investors and acquirers commission their own technical diligence and will use specialists for C&I, microgrid and storage assets.",
 ["Do you rely on the lender's IE or commission separate work?", "What distinguishes a useful red-flag report?", "Would you hire a specialist for C&I or microgrid assets? Under what reliance terms?"],
 "Supports: separate diligence with specialist selection. Contradicts: reliance on the lender's IE only.",
 "Determines priority of M&A diligence as a reference-building segment."),
]
for name, prof, hyp, qs, ev, dec in I:
    d.add_heading(name, 2)
    para(d, f"**Respondent:** {prof}", after=2)
    para(d, f"**Hypothesis:** {hyp}", after=2)
    para(d, "**Key questions:**", after=1)
    for q in qs: para(d, q, B)
    para(d, f"**Evidence:** {ev}", after=2)
    para(d, f"**Decision impact:** {dec}", after=4)

d.add_heading("3. Questions to ask every financing counterparty identically", 1)
for q in ["Do you maintain a formal approved-IE list? How many firms are on it, and when was one last added?",
          "What is the minimum firm-level and individual transaction history you require?",
          "Does hiring an experienced IE lead change your answer?",
          "Which independence, reliance and insurance terms are non-negotiable?",
          "May the IE subcontract disciplines? Which ones?",
          "Would technology-assisted evidence review change your diligence time or confidence?",
          "In what situations would you prefer a smaller specialist?",
          "What is the most common reason a technically competent provider is rejected?"]:
    para(d, q, B)
para(d, "Record the answers in a shared matrix (one row per respondent) so results can be compared rather than summarized anecdotally.")

d.add_heading("4. Internal Mayfield information needed", 1)
table(d, ["Information", "Why it matters", "Decision it informs"], [
 ("Past engagements where a lender, investor or acquirer received, reviewed or relied on Mayfield's work, with permission to cite", "Non-public references may materially change the acceptance assessment", "Model A readiness; marketing claims"),
 ("Current IE/TDD revenue, engagement count, pricing and win/loss history", "Only internal source of pricing and demand evidence", "Model B economics; baseline"),
 ("Design/EOR client list and pipeline overlap with likely IE targets", "Quantifies the independence constraint", "Addressable IE market; conflict policy"),
 ("Professional-liability policy: limits, exclusions, treatment of third-party reliance and certificates", "Determines whether lender reliance can be offered at all", "Model A feasibility"),
 ("Staff capacity and disciplines (energy-yield method, civil/geotech, cost/schedule, field monitoring)", "Shows which scope gaps need hires or partners", "Delivery model; partner selection"),
 ("Clients expected to seek financing in the next 12 months", "Candidates for Model B pilots and live lender tests", "Pilot plan"),
 ("Status of the Mayfield Standard and any data or tooling assets", "Starting point for Model C", "Model C investment"),
 ("Relationships with financiers (sponsors, summit partners, logo clients)", "Interview access and warm introductions", "Recruiting plan"),
 ("Leadership objectives: investment budget, time horizon, margin and risk appetite", "Sets go/no-go thresholds", "Overall decision"),
], [2.6, 2.4, 1.9], size=8)

d.add_heading("5. Execution and decision rules", 1)
for b in ["**Weeks 1–2:** compile the internal fact base; recruit through existing client, summit-sponsor and counsel relationships; finalize interview guides.",
          "**Weeks 2–8:** conduct interviews (I-1, I-2, I-4 and I-7 first); hold a weekly synthesis against the hypotheses.",
          "**Week 9:** read out findings against these illustrative thresholds:",
          "Proceed with a Model A pilot if at least two financing counterparties say they would approve Mayfield on a transaction basis, and the broker confirms reliance terms are insurable.",
          "Prioritize Model B if at least three sponsors describe recurring diligence rework and a willingness to pay for prevention.",
          "Pursue Model C only if both sponsors and lenders say standardized evidence would change diligence time or cost.",
          "Shift toward partnering or acquisition if lenders consistently require a firm-level track record Mayfield cannot build within 24 months."]:
    para(d, b, B)
d.save(sys.argv[2]); print("saved")
