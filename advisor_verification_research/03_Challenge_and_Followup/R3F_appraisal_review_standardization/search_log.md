> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from R3F's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

## R3F search log (2026-11-15, ~19:01–19:14 UTC)

**Retrieved, full text (curl + pdftotext)**
- FHFA OIG AUD-2014-008 (fhfaoig.gov/Content/Files/AUD-2014-008.pdf). Used.
- Interagency Appraisal and Evaluation Guidelines, 75 FR 77450 (govinfo FR-2010-12-10 2010-30913.pdf). Section XV used.
- FHFA OIG WPR-2018-006, appraisal waivers. Used.
- Freddie Mac ACE research note, May 2024 (capitalmarkets.freddiemac.com). Used.
- Eriksen, Kuang, Zhu, AEA 2021 preliminary paper (aeaweb.org). Used.
- FHFA WP 24-06 (fhfa.gov; came through WebFetch as binary, then pdftotext). Used.
- Texas Appraisers and AMC Survey 2012 (talcb.texas.gov). Used.
- 40 CFR 312.21 (govinfo CFR-2024 XML). Used.
- FHFA OIG EVL-2020-002, EVL-2023-003, EVL-2026-001 and AUD-2025-005 were downloaded but are off-topic (servicer fraud, credit models, multifamily loss allowance, Duty to Serve). Not used.

**Searches (WebSearch, standard)**
1. "FHFA OIG Collateral Underwriter evaluation report appraisal". Found the 2014 UCDP audit; no CU-specific OIG evaluation.
2. "Uniform Appraisal Dataset effect appraisal quality study overvaluation Collateral Underwriter empirical". Vendor and GSE material only; no causal study of UAD or CU.
3. "Fannie Mae Collateral Underwriter risk score 2.5 representation warranty relief … Day 1 Certainty". Fannie pages all blocked.
4. "'Collateral Underwriter' study effect appraisal accuracy introduction 2015 working paper". No study of CU's effects found.
5. "'Collateral Underwriter' appraisers response natural experiment …". Led to the Eriksen et al. papers; no CU natural experiment.
6. "FHFA OIG appraisal waivers report value acceptance risk". Found WPR-2018-006; no later OIG waiver or value-acceptance evaluation located.
7. "GAO-12-147 residential appraisals AMC fees". Corrected to GAO-11-653.
8. "FHFA redesigned URAR UAD 3.6 purpose reduce revision requests". Freddie FAQ found; no primary FHFA statement on reducing revisions.
9. "Freddie Mac Loan Collateral Advisor risk score rep warranty relief …". Found the FAQ and the Guide 5602.2 reproduction.
10. "'attribute misreporting' appraisal bias … authors". Identified the Review of Finance 2024 publication.
11. "Fannie Mae CU since launch share of high risk appraisals declined …". No published trend in CU risk scores since launch found.
12. "appraisal waivers loan performance default study …". Freddie ACE note only; no independent peer-reviewed study found.
13. "Phase I ESA commoditization low price quality ASTM E1527 …". Practitioner and vendor material only; no research on quality vs price.
14. "appraiser survey revision requests 'Collateral Underwriter' percent increased time …". No quantified CU or UAD effect on revisions or time.

**Blocked or failed access (not bypassed)**
- fanniemae.com and singlefamily.fanniemae.com: HTTP 403 / Cloudflare "Just a moment" (perspectives page, Day 1 Certainty release, CU job aids, SEL-2017-03).
- gao.gov report HTML and PDF: Access Denied. Only the product page was read through WebFetch.
- revfin.org: HTTP 425.
- my.sf.freddiemac.com fact sheets: proxy CONNECT 502.
- sf.freddiemac.com ucdp_riskscores.pdf: 404.
- nationalmortgageprofessional.com (UAD 3.6 fees article): 403.
- ecfr.gov: redirected to unblock.federalregister.gov; used govinfo CFR instead.
- Wipfli CU article: 404.
- USPAP Standard 3: not attempted. It is sold by The Appraisal Foundation, and time was limited.

**Implications for public testability**
- The key outcomes (lender review hours, QC defect and repurchase rates by CU/LCA score band, warning precision) are held privately by the GSEs and lenders. No public causal evaluation of UAD or CU on review effort or detection was found. This is absence of evidence, not evidence of absence.
- The NAR article citing the CSS 2026 UAD 3.6 appraiser survey (n=863) reports readiness only, with no time, fee or revision metrics. Not used.
