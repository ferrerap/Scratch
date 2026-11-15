> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from R3C's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

R3C finished. I wrote 16 sources and 23 evidence items (15 independent evidence groups with evidence; S11 was blocked and has none) to /home/user/Scratch/advisor_verification_research/03_Challenge_and_Followup/R3C_project_finance_IE_scopes/ (sources.json, evidence.json); both pass python json.load. Downloads are in /tmp/claude-0/-home-user-Scratch/896551fc-74fd-5092-857d-f83fd4afd7e5/scratchpad/downloads/R3C/.

Headline: public scopes show yield work done as a review of the sponsor's analysis (a DFI lender's terms of reference, a securitization technical due diligence report, and IFC guidance that accepts "produced and/or verified"). The one lender account says IE results "in isolation are generally inadequate", and the reasons it gives are P50 bias and incomplete uncertainty, not opacity. Back-tests and blind comparisons support those reasons. Rating agencies take IE forecasts and apply their own haircuts; they do not re-run them. No source puts a number on how lender work splits between re-derivation (W1), review (W2) and adaptation (W4). No public solar or wind lender's technical advisor scope was retrievable.

# report.md

## R3C: what lenders and investors retain in renewable project finance technical diligence

### The question
How much of the lender's or investor's retained technical work is:
- (a) required independent re-derivation (W1),
- (b) review of the sponsor's or another advisor's analysis, where traceability could matter (W2),
- (c) adaptation to the lender's own criteria (W4)?

### Findings

**1. In the public documents found, yield work by the advisor is usually a review, not a full re-derivation.**
- **DFI lender terms of reference (R3C-E17):** EAIF, EDFI and BIO's 2021 lender's technical advisor RfP asks the advisor to "Review of the energy yield analyses undertaken by the Sponsor and verify..." and to review the sponsor's probability-based forecasts. It asks for no independent energy yield assessment. Caveat: the project is biogas, not solar or wind.
- **Securitization report (R3C-E07):** Black & Veatch's filed report "reviewed the methodology for DSD's energy production estimates." It weather-adjusted them to 98.7% of the original expected energy.
- **IFC guidance accepts either mode.** It accepts an energy yield assessment "produced and/or verified by an experienced consultant" (R3C-E09). It also lists "energy yield prediction with uncertainty analysis" as a minimum technical due diligence task (R3C-E10).
- **Implication:** re-derivation is not mandated by these documents. Each deal's terms of reference set the review-versus-independent split, and those are rarely public.

**2. The lender's own account describes W3 and W4 work, with W1 re-derivation added only some of the time (R3C-E01–E03).**
- Wells Fargo's renewable finance group (one lender) says IE results alone are "generally inadequate". It responds with "sensitivity cases, haircuts, parallel assessments, structural protections".
- The reasons it gives:
  - P50 bias beyond recent IE adjustments;
  - uncertainty distributions that are too tight;
  - commonly omitted factors (availability, degradation);
  - IE 10-year P99:P50 ratios that are "inconsistent, not comprehensive, and trending optimistic".
- Sizing rules are the lender's own (1-yr P99 ×1.0; P50 ×~1.3) and are "largely established prior to detailed diligence".
- **Rating agencies adapt rather than re-run.** In one 2021 Fitch rating action, Fitch used the third-party P50/one-year P90 spread (18%) and applied its own 7% production haircut, citing observed load-factor volatility (R3C-E23). This matches the Fitch items already in the register. An S&P study reportedly treats one-year P90 as the best proxy for Spanish solar output. That is search-summary only (R3C-E15).

**3. Discounting IE estimates looks rational (W3).**
- **Wind back-test (R3C-E11):** 115 pre-construction yield assessments for 94 wind plants (707 plant-years) overestimated P50 production by −7.4% to −6.6%.
  - Prediction-error SD was 11.4–13.1%, against stated long-term uncertainty of 7.5% ± 2.1%.
  - The authors say neither stated uncertainty nor P90 is conservative enough.
  - There was no significant difference between consultants (ANOVA p = 0.7263).
- **Consultant disagreement:**
  - Todd et al. 2022, abstract only: consultant differences of up to $10/MWh in levelized cost; disagreement between consultants "remains flat" through the loss steps (R3C-E12).
  - IEA PVPS blind test: 7 assessors given the same inputs produced P50s of 1095–1406 kWh/kWp at Bolzano, SD 9.7% (R3C-E22).
- DNV's own offshore validation shows a slight negative P50 bias; summary only (R3C-E13).

**4. Where traceability could matter (W2, and visibility into scope and uncertainty).**
- There is no standardized PV uncertainty framework, which makes it "difficult for financers… to compare" (R3C-E20).
- An IE practitioner cites "black box" uncertainty and asks for standardized processes and language (R3C-E05).
- IEA PVPS says extra yield assessments are requested "if results are unclear" (R3C-E21). It recommends showing the assumptions and modelling chain (R3C-E22).
- These are mechanisms and stated needs only. No source measures lower effort or better error detection.

**5. Governance-driven W1 work persists whatever the transparency.**
- Reports carry no-reliance terms: "solely for use of DSD", liability capped at fees (R3C-E08). Equity and mezzanine investors may see the lender's advisor report only on a non-reliance basis (R3C-E19).
- Each lender makes "our respective due diligences" and internal approvals a condition of funding (R3C-E19).
- The IE carries reputational risk only and is often engaged by the sponsor (R3C-E04).

**Net assessment (my inference, not measured).** For energy yield, the lender's in-house work appears to be mostly W4: choosing P-cases, applying haircuts and coverage tests. That adaptation is driven by measured bias (W3). Full W1 re-derivation ("parallel assessments", second yield assessments) appears to happen only some of the time. W2-type review of the sponsor's yield assessment is largely bought from the IE. So any traceability benefit may land first at the IE, which reviews the sponsor's assessment, and only second at the lender.

### Strongest counterevidence to the traceability thesis
- **The bias is systematic and shared across consultants (R3C-E11).** Clearer or second assessments would not remove haircuts. Back-testing would.
- **The lender's stated reasons are accuracy and missing coverage, not opacity (R3C-E01, E02).**
- **Rating agencies adapt the IE number rather than rebuild it (R3C-E23),** so there is little reconstruction to save at that stage.
- **Sizing is largely fixed before detailed diligence (R3C-E03),** which limits the decision value of faster review.
- **The calls for standardization come from suppliers or vendors (R3C-E05, E14).**

### Unresolved points and what would settle them
1. **No solar or wind DFI or green bank advisor scope was read.** The World Bank's IFC-presented wind ToR returned 403 and its mirror PDF returned 404. NY Green Bank's 2014 RfP returned 403. Settle by coding 5–10 public scopes (EBRD/ADB/IFC Scaling Solar, US green banks, LPO) as independent assessment vs review vs both.
2. **No split of lender hours or triggers is known.** Settle with lender interviews or time logs on what triggers parallel assessments: unclear report, dispersion between consultants, or policy.
3. **Does decomposed uncertainty reporting (the IEA PVPS framework) reduce second yield assessments or haircuts?** No source tests this. It would need a comparison of deals with and without standardized uncertainty tables.
4. **Rating methodology text was not read.** S&P's December 2022 methodology change (base case to consider P75 as well as P90 for projects without track records) is known from search summaries only. Moody's, KBRA and DBRS methodology PDFs were gated.
5. **The standard for comparable wind yield reporting is unconfirmed.** IEC 61400-15-1:2025 covers site suitability, with documentation for process traceability. Whether an energy-yield reporting part (61400-15-2) has been published was not verified.

# search_log.md

## R3C search log (2026-11-15, about 18:58–19:10 UTC)

**Searches and fetches**
1. WebSearch: IE scope of work / RFP "energy yield assessment" review lender solar.
   - Found vendor pages (Sgurr, UL) and a Black & Veatch securitization report on SEC EDGAR, which I fetched (R3C-S04).
2. WebSearch: "lender's technical advisor" terms of reference energy yield.
   - Found the World Bank PPP sample wind ToR. WebFetch and curl both returned **403**. The energypedia mirror gave only an abstract; its PDF returned **404**.
3. WebSearch: S&P methodology on IE and P50/P90.
   - Found S&P's Spanish solar article; WebFetch returned **403**, so I have the search summary only (R3C-S10).
   - The S&P 2023 report card also returned **403**.
4. WebSearch: wind pre-construction bias validation.
   - Led to Hammond & Simley 2026 (fetched), Todd et al. 2022 (abstract) and DNV 2023 (listing).
5. WebSearch: IEC 61400-15-1 purpose.
   - It is a site-suitability standard, not an energy-yield standard. I recorded no evidence item.
6. WebSearch: Todd et al. details.
   - The NREL PDF download failed (proxy 502). I used the PNNL abstract.
7. WebSearch: Moody's power generation methodology.
   - Methodology text not found; Moody's documents need a login.
8. WebSearch: green bank / public power IE RFPs.
   - NYSERDA NY Green Bank 2014 PDF returned **403** (search summary only). Connecticut Green Bank RFPs were not yield-relevant.
9. Sandia 2024 PV Performance Modeling workshop slides (Elser, Reusser, Solis) via curl.
   - Full text retrieved (R3C-S01–S03).
10. WebSearch: "independent EYA" vs "review/second opinion".
    - No source clearly separates the two as products. Vendor usage is loose.
11. IFC 2015 Utility-Scale Solar guide via curl.
    - Full text; grepped for due diligence and yield wording.
12. 3E standardisation blog (WebFetch).
    - It does not mention IEC 61400-15. It cites a DTU Walney proficiency test second-hand.
13. WebSearch: KBRA and DBRS methodologies.
    - DBRS page fetched; the methodology PDF is not accessible. KBRA is gated.
14. WebSearch: DFI lender's technical advisor ToRs (EBRD/ADB/AfDB/Scaling Solar).
    - Found the EAIF Homa Bay lender's technical advisor RfP (full text, R3C-S13). No EBRD/ADB/AfDB ToR surfaced.
15. IEA PVPS T13-12:2018 and T13-18:2020 executive summary via curl.
    - Full text of the 2018 report; summary only for 2020.
16. Hammond & Simley follow-up fetch.
    - The paper does not explain 115 assessments for 94 plants and does not mention lenders or IEs.
17. WebSearch: Fitch renewable criteria application.
    - Found the ReNew RG4 2021 rating action via an EQ Mag Pro reproduction (R3C-S16).
18. WebSearch: S&P sector-specific project finance methodology.
    - Text not found. The P75 change is known from summaries only.

**What the failures imply for public testability**
- Solar and wind lender's technical advisor scopes from DFIs and green banks are rarely public, or are blocked to scripted access.
- Rating methodologies are mostly gated.
- The W1/W2/W4 split is therefore not testable from public documents. It needs lender interviews or procured scopes.
