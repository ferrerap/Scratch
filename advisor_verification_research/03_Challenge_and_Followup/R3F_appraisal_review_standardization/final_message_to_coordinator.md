> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from R3F's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

I wrote and validated (python json.load) 15 sources, 22 evidence items and 14 independent evidence groups to /home/user/Scratch/advisor_verification_research/03_Challenge_and_Followup/R3F_appraisal_review_standardization/ (sources.json, evidence.json). The appraisal case fits the requested structure: appraiser produces, lender reviews, GSE bears the loss. On dispute (1), standardized data plus automated scoring made detection cheap at portfolio level. Most of the observable cut in lender review came from shifting liability to the GSE, not from better verification by the lender. No public, independent study measures lender review effort or missed defects before and after UAD or Collateral Underwriter. On dispute (2), standardization made routine appraisals repeatable enough to be commoditized and partly automated away. Complex or diverse assets, local knowledge and lender-specific acceptance rules still needed bespoke work. Fannie Mae and GAO full texts were blocked, so those items rest on summaries.

# report.md

## R3F — Appraisal review and standardization (Round 3 targeted resolution)

### Why this case
Residential and commercial real-estate appraisal has the structure the dispute needs:
- **Outside producer:** the appraiser, often hired through an appraisal management company (AMC).
- **Accountable recipient:** the lender, who must review the appraisal before relying on it.
- **Consequence-bearer:** the lender, and the GSE (Fannie Mae / Freddie Mac) through repurchase and loss.

Since 2011 the GSEs have required a standard data format for appraisals (the Uniform Appraisal Dataset, UAD) and run every appraisal through automated checks. These are the collateral data portal (UCDP) and the risk scores from Fannie Mae's Collateral Underwriter (CU) and Freddie Mac's Loan Collateral Advisor (LCA). That makes the case a natural experiment in "structured, machine-checkable outside analysis." The caveat is that the public record contains almost no direct measurement of what this did to lender review effort or to detection.

### Findings on dispute (1): is verification cheaper without being worse, or is trust just higher?

**A. Review obligation is formal, risk-tiered, and stays with the recipient.**
- The 2010 Interagency Guidelines require lenders to review each appraisal before the credit decision. The review covers "valuation methods, assumptions, and data sources" (R3F-E05).
- Reviewers cannot change the appraised value.
- Using a third-party reviewer does not shift responsibility (R3F-E05).
- Review depth must be risk-focused (R3F-E06):
  - Automated tools or sampling are allowed only for lower-risk 1–4 family loans, with prior regulator approval and safeguards.
  - Large, complex, specialized or out-of-market commercial properties need deeper technical review.

So regulators accept automation-based triage only for homogeneous, low-risk files. This supports P1.1, and qualifies P2.1 by asset type.

**B. Structure creates detection capacity, but detection did not automatically become verification.**
- The FHFA Inspector General found that in 2013 the GSEs bought loans despite automated warnings from the portal (R3F-E01):
  - Fannie Mae: more than 56,000 loans, $13B, January–June 2013.
  - Freddie Mac: more than 29,000 loans, $6.7B, June–September 2013.
- The warnings were set as "automatic overrides." Stated reasons: the false-positive rate had not been measured, and the GSEs "did not want to burden lenders with having to respond to messages" (R3F-E02).
- A logic error left about $88B of loans bought without a working appraiser-license check (R3F-E03, supports P2.5).
- Reading: the cost of resolving flags, including false positives, was a binding constraint, and the consequence-bearer chose throughput. This qualifies P2.2: machine-checkability raises detection capacity, and verification depends on whether someone pays to clear the flags.

**C. Cross-report structure exposes errors that single-file review cannot see, and standardization did not prevent them.**
- Eriksen, Kuang and Zhu studied 3.5M applications from 2013–2017, in the standardized era (R3F-E12):
  - 98% of properties had at least one of seven attributes reported inconsistently across appraisals.
  - The same appraiser reported the same comparable sale differently in different appraisals.
  - Inconsistent reports predicted 6–15% higher serious delinquency for highly leveraged borrowers (preliminary version).
- FHFA WP 24-06 likewise relied on detailed UAD data to show systematic patterns. It also found that appraisal outcomes depend on the appraiser's local knowledge (R3F-E14).
- Reading: standard fields let analysts with pooled data run consistency checks. Per-file lender review under the standard did not catch the misreporting. Format standardization is not correctness (P2.5). The authors argue a shared, verified reference database is the missing piece (R3F-E13).

**D. The largest observable cut in lender review effort came through liability transfer.**
- Freddie Mac's Guide gives collateral rep-and-warranty relief, meaning no repurchase on value, when the LCA risk score is 2.5 or lower (R3F-E10).
- Fannie Mae reportedly does the same through CU and "Day 1 Certainty." The page was blocked and this is unverified (R3F-E11).
- Appraisal waivers go further: they reuse the more than 29M portal appraisals on file and release the lender from value, condition and marketability representations (R3F-E07).
- The tool owners frame scores as setting the "level of review," to be "used in conjunction with human due diligence." Lenders may not ask for revisions based solely on a score (R3F-E09).
- Reading: the recipient reviews less mainly because the consequence-bearer takes the risk and verifies statistically across its portfolio. This is a different mechanism from the thesis's "traceability makes the recipient's own check cheaper."

**E. Outcome quality, from interested-party evidence only.**
- Freddie Mac's own analysis covers 5.54M loans originated May 2017–June 2023 (R3F-E15).
- Loans closed with ACE appraisal waivers had about 8.9% lower 90+ day delinquency, or 13.9% lower excluding COVID-forbearance delinquencies.
- The authors flag selection on unpublished criteria. Their instrumental-variable estimate is imprecise and not statistically different from zero.
- So skipping or automating the outside product was not shown to worsen loan performance for low-risk files. The evidence is weak and comes from an interested party.

**F. Shift rather than removal.**
- An AMC executive reported that revision requests to appraisers rose right after CU launched. This is anecdotal (R3F-E19, supports P3.2).
- Freddie Mac later barred revision requests based on the score alone (R3F-E09). That is consistent with machine flags generating rework for the producer.

**Net on (1):** Neither side is vindicated.
- The appraisal case supports "structured analysis enables cheaper triage and more portfolio-level detection."
- It does not show per-file recipient verification becoming cheaper at equal or better quality.
- Where review effort visibly fell, the cause was risk transfer to a large consequence-bearer with portfolio data, plus restriction to homogeneous low-risk segments.

### Findings on dispute (2): AS06 repeatability vs customer-specific adaptation
- **Repeatability rose so far that the product commoditized and was partly replaced:**
  - AMC fees clustered at $300–450 vs $350–450 from direct clients (Texas 2012 survey). 40% of appraisers raised workloads to offset lower fees; 27% said quality suffered (R3F-E17).
  - GAO reported concerns that AMCs prioritize cost and speed, with lenders still responsible for review (R3F-E16).
  - Waivers reached about 40% of Freddie Mac fundings in Q3 2020 (8.4% in Q2 2023) and saved borrowers about $1.63B (R3F-E15).
  - The gains went to borrowers, lenders and the GSE rather than to producers. This challenges P6.1 as applied to producers.
- **Heterogeneity still drives bespoke work and price:**
  - 98% of AMCs said property complexity raises the fee (R3F-E17).
  - Automated valuation models (AVMs) are less reliable for dissimilar or data-thin (rural) properties, and early waiver take-up was low (R3F-E08).
  - Local knowledge drives outcomes (R3F-E14).
  - Regulators require deeper review for complex commercial assets (R3F-E06).
- **The standard itself had to adapt.** The 2024–2026 redesign (UAD 3.6) replaces form types and free-text addenda with a "data-driven, dynamic" schema covering all property types (R3F-E20). This qualifies both sides: diversity was absorbed into a richer standard, not abandoned.
- **Recipient-specific policy blocks portability.** For Phase I environmental site assessments (ESAs), a report from another consultant is "typically not accepted by the new lender," and lenders use approved-consultant lists (R3F-E22; practitioner, interested party). The federal environmental-inquiry rule (40 CFR 312.21) requires the report to disclose data gaps and their significance, i.e. mandated scope and omission disclosure (R3F-E21). No evidence on its effects was found.

**Net on (2):** Standardization made delivery repeatable for the homogeneous segment, supporting P5.1 in a bounded way. Asset diversity, local knowledge and lender-specific acceptance policies keep bespoke work in the complex tier (supports P4.1). Repeatability did not lift producer economics; it enabled intermediation and substitution.

### Strongest evidence each way
- **For the thesis (P2.1/P2.2):**
  - R3F-E06: regulators sanction automated triage of standardized outputs.
  - R3F-E12 and R3F-E14: structure enables detection that single-file review can't do.
  - R3F-E15: automated substitution without measured performance loss (interested party).
- **Against or qualifying:**
  - R3F-E01 to E03: flags were overridden because clearing them was costly; an automated check failed silently.
  - R3F-E10 and R3F-E07: review reduction came via liability transfer.
  - R3F-E12: misreporting persisted under the standard.
  - R3F-E16 and R3F-E17: producer fee pressure.
  - R3F-E22: standards don't ensure reuse across recipients.

### Unresolved points and observations that would settle them
1. **Lender review hours and post-purchase defect rates around the 2015 CU launch.** A lender-level difference-in-differences would show whether verification got cheaper at constant detection.
2. **GSE quality-control defect and repurchase rates by CU/LCA score band**, especially at or below 2.5 vs above, and for lenders that use score-based streamlined review vs those that don't.
3. **Portal warning precision and recall.** The OIG noted the false-positive rate was unmeasured, and no follow-up was found.
4. **Appraiser fees, turn times and revision rates under UAD 3.6 vs 2.6.** The trade-press data seen (NMP "fees climb $65") was blocked.
5. **Whether the cut in lender review effort is due to risk transfer or to information quality.** Comparable "relief vs no-relief" files with the same information would separate the two.

### Transferability to renewable-energy investment/credit diligence
- **Transfers:**
  - Risk-tiered review depth written into policy.
  - Cross-report consistency checks need pooled structured data, for example the same parcel, lease or equipment across reports.
  - Automated flags get overridden when false positives are costly, so precision matters more than coverage.
  - Mandated data-gap disclosure (AAI rule) is a direct precedent for scope and omission visibility.
  - Standardization can commoditize a deliverable and invite intermediaries or automated substitutes.
- **Consequential differences:**
  - Appraisal effects depend on a dominant consequence-bearer that sets the standard and can offer liability relief.
  - They also depend on millions of homogeneous units and a central repository.
  - Utility-scale renewable diligence has few, diverse deals, multiple lenders and tax-equity investors with different credit policies, and no central data store. It resembles the "complex commercial real estate" tier, where guidance expects deeper human technical review.
  - The liability-transfer route only exists if some party (insurer, guarantor, tax-equity investor) accepts standardized diligence in place of re-review.
- **Needs verification:** whether any renewable-energy lender or investor reduces its own review when a consultant's report is structured and traceable, absent liability relief.

### Limitations
- Fannie Mae pages (403 / Cloudflare), the GAO full report (Access Denied) and the NMP UAD 3.6 fee article (403) were not read. R3F-E11 is an unverified pointer only.
- The Freddie Mac FAQ and Guide text were read through an extraction tool and a third-party reproduction.
- The academic studies are observational and about bias or misreporting, not review effort.
- The appraisal case is US residential-heavy. Commercial appraisal review evidence beyond the guidance was not found.

# search_log.md

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

