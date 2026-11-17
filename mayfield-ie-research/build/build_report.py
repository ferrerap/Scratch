import sys, re
sys.path.insert(0, sys.argv[1])
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx_util import new_doc, para, table, NAVY
from sources import SRC

d = new_doc(10)
B = "List Bullet"; N = "List Number"
used = []
from docx.shared import Inches
def numbered(d, n, text):
    p = para(d, f"{n}.\t" + text, after=2)
    pf = p.paragraph_format; pf.left_indent = Inches(0.3); pf.first_line_indent = Inches(-0.2)
    pf.tab_stops.add_tab_stop(Inches(0.3))
    return p
def c(text):
    ids = re.findall(r"S\d\d", text)
    for a, b in re.findall(r"S(\d\d)–S(\d\d)", text):
        ids += ["S%02d" % i for i in range(int(a), int(b) + 1)]
    for m in ids:
        if m not in used: used.append(m)
    return text

t = para(d, "U.S. Solar & Storage Independent Engineering: Competitive Landscape and Market Entry Considerations for Mayfield Renewables", size=17, after=4)
for r in t.runs: r.bold = True; r.font.color.rgb = NAVY
para(d, "Prepared for Jacob Betcher and Mayfield Renewables leadership  ·  November 2026", size=10, after=0)
para(d, "Basis: desk research with primary-document verification. Lender, sponsor and competitor interviews have not yet been conducted. Source IDs in brackets (e.g., [S07]) refer to the source list at the end of this report and the Source Register in the companion workbook.", size=8.5, italic=True, after=6)

# 1
d.add_heading("1. Executive Summary", 1)
para(d, "Independent engineers (IEs) hold a gatekeeping position in U.S. solar and storage finance. Their reports and certificates are conditions to closing and funding, and lenders take formal reliance on them. This study asked who holds that position, how it is granted, and where a technically capable but financially unproven provider such as Mayfield could compete. The principal findings are:")
for b in [
 "**Acceptance is granted transaction by transaction, by lenders – not by an industry-wide list.** Filed financing agreements name preferred IEs, but almost all of them allow an alternative approved by the agent or required lenders, or in some distributed-generation (DG) facilities chosen by the borrower. The pathway is real. No public source, however, shows how often lenders actually use it, and the filed record shows friction: approved lists change slowly, lenders demanded a second report from an incumbent, and incumbents carry over through refinancings [S01, S02, S10, S17, S18, S20].",
 "**Demonstrated acceptance is concentrated, and it is not a function of size.** Leidos, DNV and Enertis Applus+ appear in executed agreements with reliance and funding-certificate mechanics involving MUFG, Bank of America and Deutsche Bank [S06–S08, S10, S11]. ICF, Sargent & Lundy, Black & Veatch, E3 Consulting, Luminate, VDE Americas, Natural Power and ArcVera have named assignments or contractual eligibility. Several large engineering and testing organizations market IE services but have little public evidence of U.S. solar or storage lender work.",
 "**Specialists can become bankable, but the documented examples took decades.** Luminate (formed in 2006 by project-finance practitioners) and E3 Consulting (founded in 1999; owned by NAES, part of ITOCHU, since 2014) both appear in lender documents [S01, S17, S38, S41]. How either firm first won lender acceptance is not publicly documented.",
 "**The initial view that DG and community solar are the easiest lender-facing entry point is weakened.** In the bank-led DG and microgrid financings that disclosed an adviser, lenders used Black & Veatch or Enertis [S29, S33], and incumbents run dedicated DG diligence programs. There is counter-evidence: a DG-oriented 2018 facility approved ten engineering firms, including small specialists, and one C&I facility lets the borrower select the IE [S17, S20]. The question cannot be settled from public sources.",
 "**Mayfield already advertises an Independent Engineering service line and has documented depth in C&I, storage, microgrids, codes and commissioning** [S77, S96]. No public evidence shows a lender or investor relying on Mayfield's work. For lender-facing work, the binding constraint is the firm-level transaction record, not technical skill.",
 "**Of the three business models examined, only sponsor-side diligence and finance readiness (Model B) can be sold today without third-party acceptance.** Lender-facing IE (Model A) depends on approval rates that desk research cannot establish. Technology-enabled evidence standardization (Model C) addresses a documented pain point, but incumbents already use portfolio sampling, and no public evidence shows customers will pay for it as a separate product.",
]: para(d, c(b), B)
para(d, "**Bottom line.** The evidence supports a staged approach. Mayfield sells sponsor-side work now, tests lender acceptance on specific transactions, and completes six to eight targeted interviews before committing significant resources to a lender-facing IE practice or a standalone diligence product. IE fees, lender approval rates and customer demand are not publicly documented, and they are the decisive unknowns.")

# 2
d.add_heading("2. Research Approach & Methodology", 1)
para(d, "The research was carried out in five stages:")
for n_, b in enumerate([
 "**Discovery.** An initial market scan using ChatGPT Deep Research identified 34 firms active in U.S. solar and storage IE and technical due diligence, along with candidate financing references and a first segment view. That baseline report and workbook are preserved unchanged.",
 "**Structuring.** The firms were organized into a landscape workbook, and each claim was mapped to its evidence. This stage found that the baseline report's inline citations had been lost on export (no source URLs were recoverable) and that the baseline workbook contained no URLs. The source trail was therefore rebuilt.",
 "**Verification.** Thirty-six consequential claims were audited against primary evidence: SEC-filed credit and financing agreements and IE reports filed with asset-backed securities offerings (located through EDGAR full-text search), lender and sponsor financing announcements, company qualification statements, and public procurements. Each claim was recorded as confirmed, partially confirmed, corrected or not found, and each piece of firm evidence was assigned to one of five classes (Table 1). AI research assistants (Claude) retrieved and read the sources, and the decisive contractual language (IE definitions, approved-engineer schedules and the reliance-liability cap) was then re-extracted directly from the filings. Sources seen only in search snippets, or that failed to load, are flagged in the Source Register.",
 "**Analysis.** Documented financing acceptance was assessed separately from organizational scale and applied across seven segments and three business models.",
 "**Synthesis.** Questions that public evidence cannot answer were turned into a primary-research plan, delivered as a separate document.",
], 1): numbered(d, n_, b)
para(d, "**Limits.** This is desk research; no lenders, sponsors or competitors have been interviewed. Fee levels, approval frequency and demand are not publicly documented. Signed reliance letters were not available, so reliance is inferred from the terms of executed agreements. A lack of public evidence does not mean a firm lacks financing experience.")
table(d, ["Class", "Evidence classification (not a ranking of technical competence)"], [
 ("1", "**Confirmed financing reliance** – an executed financing document names the firm as IE and grants named lenders or agents reliance (reliance letter, addressed report or IE certificate)."),
 ("2", "**Named financing assignment** – firm publicly identified as IE/adviser on a specific financing; formal reliance not independently established."),
 ("3", "**Contractual eligibility** – firm expressly listed as an acceptable or approved IE in a financing agreement."),
 ("4", "**Documented lender-facing experience** – lender/investor IE work described without named transactions."),
 ("5", "**Company-reported or adjacent** – marketing claims or relevant capability without verified financing assignments."),
], [0.5, 6.4], size=8, caption="Table 1. Evidence classes used throughout the report and workbook")

# 3
d.add_heading("3. Structure of the Independent Engineering Market", 1)
para(d, "Two dimensions describe this market. **Scale** measures resources and breadth of disciplines. **Demonstrated acceptance** measures whether financing parties have named, approved or relied on a firm. The two are only loosely correlated, and treating them as one leads to two errors: assuming every global engineering firm is a bankable IE, and assuming no specialist can be.")
table(d, ["Tier", "Firms", "Best public evidence", "Implication"], [
 ("Institutional – strongest documented acceptance", "Leidos; DNV; Enertis Applus+", c("Named IE in executed agreements with reliance letters or IE certificates addressed to MUFG, Bank of America, Deutsche Bank [S06–S08, S10, S11]; repeat IE reports in residential ABS [S15, S16]"), "Default choices on bank-led financings; persist through refinancings"),
 ("Institutional – named roles or eligibility", "ICF; Sargent & Lundy; Black & Veatch; UL Solutions", c("Listed acceptable IEs [S01, S02]; B&V as lenders' IE on a microgrid portfolio [S29]; UL IE report on a DG securitization [S22]"), "Competitive across utility-scale and DG"),
 ("Bankable specialists", "Luminate; E3 Consulting", c("Approved or listed IE [S01, S17]; named financings, including private-credit BESS deals [S40, S43–S45]"), "Proof that size is not the gate – but long track records"),
 ("Mid-market lender-facing", "VDE Americas; Natural Power; ArcVera / Bureau Veritas; Intertek CEA", c("Named in 2018–2023 approved-engineer lists [S17, S19]; sponsor-side and M&A assignments [S36, S47, S48]"), "Most direct competitors in DG/community-solar portfolio work"),
 ("Large multidisciplinary / adjacent", "1898 & Co.; Tetra Tech; Stantec; Arup; Mott MacDonald; RINA; AFRY; HDR; TRC; others", "IE services marketed; no named U.S. solar/BESS lender assignment found", "Partners, subcontract sources and hiring pools"),
 ("Specialist / emerging", "Fractal; Pure Power; Illumine-i; GroundWork; Partner ESI", c("Service descriptions and aggregate claims; no named lender reliance [S53–S59]"), "Mayfield's closest peer set"),
], [1.35, 1.45, 2.55, 1.55], size=7.5, caption="Table 2. Competitive tiers by documented financing acceptance (full 40-firm universe in workbook)")
para(d, "Table 3 profiles the 15 firms most relevant to Mayfield. They were chosen to represent every tier, with weight on firms active in segments Mayfield could plausibly enter: DG, C&I, storage and sponsor-side diligence.")
pri = [
 ("Leidos", "U.S. public co.; energy IE practice", "SE Titan (MUFG/DB/CoBank); Angiola East solar+BESS (BofA); Big Five (MUFG) [S06–S08]", "1, 3", "Incumbent; hard to displace"),
 ("DNV", "Global; dedicated DG/residential IE team", "Second report with reliance required by MUFG lenders [S10]; GoodLeap ABS IE [S15]; Spotsylvania tax equity, 2020 [S26]", "1, 2, 3", "Incumbent; strong DG data assets"),
 ("Enertis Applus+", "Global; strong storage scope", "MUFG warehouse IE [S11]; Cider tax equity [S30]; Lightshift/KeyBank BESS [S31]; Dimension community solar [S33]", "1, 2, 3", "Incumbent in BESS and community solar"),
 ("Black & Veatch", "Large employee-owned", "Lenders' IE, Scale Microgrids $225M (KeyBanc) [S29]; DG securitization TDD [S23]", "2, 3", "Competes in microgrid/DG lender work"),
 ("Sargent & Lundy", "Large U.S. power engineering", "Listed IE, Energy Vault BESS 2026 [S01]; Leeward debt and tax equity IE [S34]", "2, 3", "Utility-scale incumbent"),
 ("ICF", "U.S. public consultancy", "Listed IE in Spruce residential facilities [S02]; Pelicans Jaw [S09]", "2, 3", "DG/residential portfolio incumbent"),
 ("UL Solutions", "Global testing/certification", "Luminace securitization IE report [S22]; monitoring and draw services [S35]", "2, 4", "Competitor or testing partner"),
 ("Luminate", "Denver specialist, est. 2006", "Fifth Third approved engineer [S17]; Grape Solar+Storage ~$600M [S40]", "2, 3, 4", "Benchmark specialist; possible teaming"),
 ("E3 Consulting", "Specialist; NAES/ITOCHU-owned", "Listed IE 2026 [S01]; Energy Vault $28M (Eagle Point) and $18M BESS [S43–S45]", "2, 3", "Benchmark; active in small BESS deals"),
 ("Natural Power", "UK-founded; 3 U.S. offices", "Fifth Third approved engineer [S17]; Exus TAG $312M [S47]; Igneo–Soltage M&A [S48]", "2, 3", "DG M&A and IE competitor"),
 ("VDE Americas", "VDE-owned; Bay Area", "Listed IE, Greenbacker/Wells Fargo 2023 [S19]; co-op DG portfolios [S92]", "2, 3, 5", "Most direct DG-portfolio competitor"),
 ("Intertek CEA", "Intertek-owned; QA network", "Fifth Third approved engineer as CEA, 2018–19 [S17]; IE DD services [S51]", "3, 5", "Equipment-QA partner or competitor"),
 ("Fractal ESC", "Austin storage specialist", "Storage IE scope; no named lender [S55]", "4, 5", "BESS partner candidate"),
 ("Pure Power Eng.", "130+ engineers; design-led", "OE/acquisition DD; no named lender [S53, S54]", "5", "Closest structural peer"),
 ("Illumine-i", "Onshore/offshore delivery", "'$2B transactions supported' – not reliance [S57]", "5", "Price competitor in desktop/sponsor work"),
]
for r in pri: c(r[2])
table(d, ["Firm", "Profile", "Strongest documented financing evidence", "Classes", "Relevance to Mayfield"], pri, [1.05, 1.35, 3.0, 0.55, 1.25], size=7.5,
      caption="Table 3. Priority competitor comparison (detailed dimensions in workbook tab 2)")
para(d, c("Several claims from the initial research did not hold up. Leidos's reported \"125+ projects a year\" could not be found in any Leidos source; Leidos now cites 3,000+ projects completed cumulatively [S27]. The ICF project list could not be verified. Black & Veatch's sPower work was a different financing from DNV's 2020 Spotsylvania tax-equity role [S26, S28]. Illumine-i's \"$2 billion\" counts transactions supported, not reports lenders relied on [S57]."))

# 4
d.add_heading("4. Institutional Acceptance and Bankability", 1)
para(d, "The filed agreements show three ways IEs are designated. In each, financing parties hold the decisive control:")
table(d, ["Pattern", "Example language", "Who decides"], [
 ("Named list plus approved alternative", c("Leidos, DNV, ICF \"or any other reputable, qualified engineering firm with substantial experience in the residential solar industry that is not an Affiliate of the Borrower or the Sponsor and has been approved by the Majority Lenders\" [S02]; Energy Vault BESS: Enertis, E3, Sargent and Lundy, DNV \"or other… company mutually agreed\" with the agent [S01]"), "Majority or Super-Majority Lenders [S04]; agent with borrower"),
 ("Lender-selected or agent-appointed", c("Leidos \"or another Person selected by the Required Lenders\" (BofA) [S08]; DNV or a replacement \"of nationally recognized standing\" appointed by the agent [S21]; agent may remove and replace the IE [S01, S07]"), "Lenders / agent"),
 ("Approved schedule or borrower selection", c("Fifth Third (2018): ten Approved Engineers, or any other approved by the agent \"in its sole discretion\" [S17]; Altus Power (Blackstone): \"any qualified third-party engineering and technical consultant to be selected by the Borrower,\" with agent replacement rights [S20]"), "Agent; in Altus, the borrower subject to agent veto"),
], [1.4, 4.2, 1.3], size=7.5, caption="Table 4. How financing documents designate the IE")
para(d, c("**What this flexibility establishes.** There is no single industry list. A firm that is not named has a contractual pathway, controlled by lenders. The stated screening criteria are reputation, sector-specific experience, independence from the sponsor and lender approval; none of the IE definitions reviewed mentions engineering licensure or firm size. Lists also differ by lender and over time. Fifth Third's 2018 schedule included Bay4, Radian Generation, BEW Engineering and the developer Borrego Solar alongside the incumbents, while Greenbacker's 2023 Wells Fargo facility named only Enertis, ArcVera and VDE Americas [S17, S19]."))
para(d, c("**What it does not establish** is how often lenders approve a new firm, how long approval takes, or what persuades them. The filed record points to friction. The Fifth Third list grew by one firm (Leidos) in about 18 months [S18]. MUFG-led lenders accepted Enertis on one project only with an additional DNV report and reliance letter [S10]. Leidos stays on as IE across successive SB Energy facilities [S06–S08]. A vendor publication asserts that a non-listed IE \"typically triggers a request for a second opinion from a Tier 1 firm,\" but cites no evidence [S88]. Approval frequency is the most important question for lender interviews."))
para(d, c("**Reliance, certification and liability.** Agreements require reliance letters that entitle the agent and lenders to rely on IE reports [S01, S06]. IE certificates gate funding: one facility requires an IE certificate five business days before each initial project funding [S10], and another includes a Leidos drawdown certificate addressed to Bank of America [S08]. Liability is negotiated. DNV's IE summary for a GoodLeap ABS states that third-party reliance is subject to its standard reliance terms, which cap DNV's total liability at USD 300,000 [S15]. That figure comes from one context and should not be generalized, but it shows incumbents limit reliance exposure by contract, terms a new entrant would negotiate from a weaker position. No industry-standard professional-liability limit was found; one Connecticut Green Bank technical-consultant RFP requires $1 million [S71]."))
para(d, c("**Independence and data.** Agreements exclude engineers affiliated with the borrower or sponsor [S02]. For Mayfield, the more practical constraint is prior design work: an engineer of record cannot credibly act as IE on the same asset, and a formal conflict policy may remove part of the existing client base from the addressable IE pipeline. Incumbents also hold data advantages. For example, DNV's residential IE work draws on irradiance-adjusted production data from more than 300,000 systems [S15]."))

# 5
d.add_heading("5. Competitive Positioning and Market Segments", 1)
para(d, "**Where smaller specialists have demonstrably competed.** The evidence shows specialists in four settings:")
for b in [
 "On approved lists of a DG-oriented credit facility: Luminate, Natural Power, Clean Energy Associates, Bay4, Radian Generation, BEW Engineering and Borrego Solar (Fifth Third, 2018–19) [S17, S18].",
 "In private-credit financings of smaller BESS projects: E3 was IE on Energy Vault's $28 million (Eagle Point) and $18 million financings, and the 2026 facility agented by a private-credit fund lists E3 beside Sargent & Lundy, Enertis and DNV [S01, S43–S45].",
 "In sponsor-engaged and M&A roles: Natural Power for Exus and for Igneo's acquisition of Soltage [S47, S48]; VDE Americas on cooperative and school-district portfolios [S92].",
 "In public procurements open to small firms: Connecticut Green Bank's 2026 inspection and technical-consultant RFP covering 150 C&I systems prefers \"a sole proprietor or single-principal firm\" [S71]. A Solar for All lender sought a per-project IE but required four years of IE experience [S73], and that program's funding remains legally uncertain [S93].",
]: para(d, c(b), B)
para(d, "A tentative pattern emerges: smaller IEs appear more often with private-credit, specialty and public lenders, and in sponsor-engaged roles, than with money-center banks. The sample is small, so this should be treated as a hypothesis to test.")
para(d, "**Testing the strongest counterargument.** If DG portfolios are often financed by the same banks that favor incumbent IEs, why would a smaller project or portfolio make entry easier? The evidence cuts both ways:")
for b in [
 "**Supports the counterargument:** Scale Microgrids' 2023 facility (KeyBanc, City National) used Black & Veatch as lenders' IE [S29]. Dimension Energy's $650 million community-solar financing (MUFG, First Citizens, ING, National Bank of Canada) used Enertis [S33]. Residential/DG credit agreements list Leidos, DNV and ICF [S02], and incumbents have productized DG diligence [S15, S50, S68]. Of about 14 DG financings checked, only these two disclosed an adviser, and both were incumbents.",
 "**Supports DG accessibility:** DG economics push toward lighter, sampled scopes. Counsel note that full diligence on every project in a 25+ project portfolio \"is neither economically feasible\" [S67]. ICF wrote that utility-scale diligence is \"too expensive and impractical for distributed assets\" [S68], and KeyBanc says there is \"no easy solution\" to the DG diligence problem [S69]. Smaller banks lower transaction costs [S70]. The DG-oriented Fifth Third facility approved a broad list [S17], and the Altus facility lets the borrower choose [S20].",
]: para(d, c(b), B)
para(d, "**Assessment:** DG is not demonstrably more accessible for lender-facing IE work. What it does offer is cost pressure on diligence and, in some facilities, more borrower influence over IE selection. Whether either translates into approval of a new firm can only be determined by interviewing DG lenders and capital-markets leads.")
seg = [
 ("Utility-scale solar & solar+storage", "Lenders control; reliance & funding certificates", "Very high (Leidos, DNV, Enertis, S&L, B&V, ICF, Luminate)", "Low–medium", "Not an entry point; long-term option"),
 ("Standalone utility BESS", "Lender approval; storage specialists listed", "High (Enertis, E3, S&L, DNV, Fractal)", "Medium for electrical, controls, safety and commissioning", "Specialist workstream or teaming only"),
 ("DG & community-solar portfolios", "Varies: incumbent-led in disclosed bank deals; broad lists or borrower choice in some facilities", "Medium–high (DNV, ICF, VDE, Enertis, B&V, Natural Power, UL)", "Medium–high technically; no references", "Plausible but unproven – test first"),
 ("C&I, BTM storage & microgrids", "Often sponsor-led; lender-selected at portfolio scale", "Fragmented; B&V at portfolio scale", "High – Mayfield's documented core", "Best technical fit; paid demand unverified"),
 ("Project & portfolio M&A diligence", "Buyer selects; buyer reliance only", "High (Natural Power, ArcVera, E3, DNV)", "Medium (strong for C&I/storage assets)", "Viable reference-builder"),
 ("Sponsor pre-finance & fatal-flaw", "Sponsor selects; no third-party reliance", "Fragmented (design and OE firms, offshore providers)", "High – service already listed", "Most accessible; sell now"),
 ("Construction monitoring, draws, commissioning, operating reviews", "Lender-side for draws; owner-side for commissioning", "High for lender draws; moderate owner-side", "Medium–high owner-side; low for draws", "Owner-side now; lender draws only after acceptance"),
]
table(d, ["Segment", "IE selection & reliance", "Competition", "Mayfield alignment", "Assessment"], seg, [1.35, 1.75, 1.55, 1.15, 1.1], size=7.5,
      caption="Table 5. Segment assessment (buyers, disciplines and uncertainties detailed in workbook tab 4)")

# 6
d.add_heading("6. Implications for Mayfield Renewables", 1)
para(d, c("**Documented capabilities.** Mayfield, founded in 2007 and based in Corvallis, Oregon, describes itself as acting as \"Engineer of Record, Owner's Engineer, or Investor's Engineer\" [S96]. It lists an Independent Engineering line covering desktop report review, pre-finance technical due diligence, energy-yield validation modeling and technical design review. It also offers owner's engineering covering contract and liquidated-damages review, BESS integration, and golden-row and commissioning oversight [S77, S85]. It has completed more than 30 microgrid feasibility reports [S86]. The Mayfield Standard is a vendor-agnostic, five-phase microgrid roadmap that leadership has positioned partly as a way to give financiers confidence; it is still described as a work in progress [S79, S82]. Mayfield participates in electrical-code development and runs an education platform [S94, S95]."))
para(d, "**Gaps against a lender IE scope.** No named financing references are public. No energy-yield methodology (such as P50/P90 exceedance values) is published. Resource assessment, civil and geotechnical review, cost and schedule validation, contract review and construction monitoring are not documented at IE scale. Independence conflicts with design clients are unresolved. Reliance contracting and professional-liability coverage are unknown. Some of these may be addressed by non-public experience; that is an input Mayfield leadership should supply.")
table(d, ["Dimension", "A – Lender-facing IE", "B – Sponsor-side diligence & finance readiness", "C – Technology-enabled evidence standardization"], [
 ("Buyer / decision", "Lenders approve or select; sponsor usually pays", "Developer, owner, acquirer or investor chooses directly", "Unclear – sponsors, lenders or platforms; not evidenced"),
 ("Customer problem", "Reliable independent opinion for credit and funding", "Find and fix issues before the lender's IE or a buyer does", c("Inconsistent project evidence slows diligence (documented pain [S69, S87])")),
 ("Alternatives", "Leidos, DNV, Enertis, ICF, S&L, B&V, Luminate, E3, VDE", "Incumbent IEs, OE and design firms, offshore providers", "Incumbents' own sampling methods; data rooms; in-house processes"),
 ("Acceptance barrier", "Very high", "Low", "Moderate – credibility of outputs untested"),
 ("Mayfield readiness", "Partial; needs references, full scope or partners, QA, reliance terms, insurance", "High – service already listed", "Concept only; requires product investment"),
 ("Pricing / demand evidence", "None public", "None public", "None public"),
 ("Liability & complexity", "Highest (third-party reliance, certificates)", "Moderate (sponsor reliance)", "Depends on whether outputs are relied on"),
 ("Plausible first customers", "Specific deals where the lender pre-agrees; private-credit and green-bank lenders; teaming under an accepted IE", "Existing clients approaching financing", "Embedded in Model B engagements, measured before productizing"),
], [1.1, 1.9, 1.95, 1.95], size=7.5, caption="Table 6. Three business models compared")
para(d, "**Entry routes, stated without overstating them:**")
for b in [
 "**Sell Model B now under precise terms**, such as \"pre-finance technical due diligence\" or \"finance-readiness review.\" Structure the reports to mirror lender IE categories so a lender could later read them. This builds transaction references; it does not by itself establish lender eligibility.",
 "**Test Model A one transaction at a time.** Before engagement, ask the prospective lender whether it would approve Mayfield under the alternative-IE clause. Prioritize facilities where the borrower selects or the list is broad, and private-credit and green-bank lenders. Teaming under an accepted IE, for example a storage specialist or an incumbent that lacks microgrid depth, is an alternative; whether incumbents subcontract such work is unverified.",
 "**Treat Model C as a capability inside Model B.** Measure its effect first, for example days to data-room readiness and the number of issues found before the lender's IE, and productize only if sponsors pay for it.",
]: para(d, b, B)

# 7
d.add_heading("7. Conclusions and Priority Next Steps", 1)
para(d, "**What the research establishes.** IE acceptance is controlled by lenders deal by deal. It is concentrated among a small set of firms with documented reliance roles, and it is earned through transaction history rather than scale. Specialists can attain it, but the documented examples took many years. Mayfield's sponsor-side and C&I/microgrid capabilities are well aligned with buyers who choose their technical adviser directly.")
para(d, "**What remains uncertain.** How often lenders approve a new IE, and whether DG, private-credit or green-bank lenders are more open. What sponsors pay, and whether they would pay for finance readiness. Which reliance and insurance terms are insurable. How much of Mayfield's pipeline is conflicted by its design work.")
para(d, "**Recommended sequence (about 90 days):**")
for n_, b in enumerate([
 "**Internal fact base (weeks 1–3).** Inventory past work usable as financing references, design-client conflicts, professional-liability terms and available capacity; agree go/no-go criteria.",
 "**Interviews (weeks 2–8).** Conduct six to eight interviews per the companion Primary Research Plan, prioritizing lenders that have approved new IEs in DG, C&I and private credit.",
 "**Counsel and broker review (weeks 3–6)** of a template reliance letter, limitation of liability and coverage.",
 "**Model B pilots (weeks 4–12).** Package the offer and run two or three pilots with clients approaching financing; record whether lenders or their IEs accepted or reused the work.",
 "**Live lender test.** On one transaction, seek lender pre-approval under the alternative-IE clause and document the response, whichever way it goes.",
 "**Decision checkpoint (~day 90).** Proceed, narrow or partner. Illustrative criteria: at least two lenders willing to approve Mayfield on a transaction basis; sponsor willingness to pay validated; reliance terms insurable at acceptable cost.",
], 1): numbered(d, n_, b)

# Sources
d.add_heading("Sources cited", 1)
for sid in sorted(used):
    s = SRC[sid]
    p = para(d, f"[{sid}] {s[1]}. {s[2]}, {s[3]}. {s[5]}", size=7.5, after=1)
para(d, "Full register of 98 sources with access status: workbook tab 7_Source_Register.", size=7.5, italic=True)
out = sys.argv[2]
d.save(out); print("saved", out, len(used), "sources cited")
