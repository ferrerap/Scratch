> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from R3C's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

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
