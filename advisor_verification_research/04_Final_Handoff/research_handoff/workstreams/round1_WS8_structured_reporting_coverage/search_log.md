# WS8 search log (2026-11-15, ~18:38-19:00 UTC)

Tools: WebSearch (standard), WebFetch, Europe PMC REST API (curl), GovInfo PDF (curl + pdftotext). Downloads in /tmp/claude-0/-home-user-Scratch/896551fc-74fd-5092-857d-f83fd4afd7e5/scratchpad/downloads/WS8/.

## Productive
- "Schwartz Panicek Radiology 2011 structured reporting referring clinicians" -> PMC3121011 full text (S01).
- "Sluijter effects of implementing synoptic pathology reporting systematic review" -> PMC4887530 (S04).
- "Nobel Structured reporting in radiology systematic review" -> PMC8921035 (S02).
- "Johnson Chen Swan Applegate Littenberg structured reporting cohort" -> Europe PMC abstract PMID 19709993 (S03).
- "Kronz Westra Epstein mandatory second opinion" / "Manion Cohen Weydert" -> PubMed pages blocked by cookie wall in WebFetch; abstracts retrieved via Europe PMC REST API (S15, S16).
- "Lin Powell Kagetsu checklist cervical spine CT" -> PMC4171436 full text (S07).
- "second opinion interpretation outside imaging referral center discrepancy" -> Lysack 2013 PMC3680178 full text (S17); other hits (ultrasound, MSK, breast, ED overreads) seen only as search summaries - not used.
- Europe PMC title queries: Idowu 2010 CAP Q-Probes (S05), Brook 2015 (S06), Marcovici & Taylor 2014 (seen, not used: similar to S01/S06, trainee chest radiographs), Bosmans COVER/ROVER 2011 (seen, not used), Powell & Silberzweig 2015 (S11), Larson 2013 (S10), Hawkins 2012 (S08, full text via PMC3389086), Hong & Kahn 2013 (S12), Lazarus 2006 BI-RADS (S20), Ould Ismail 2025 VA (S14), Lu 2012 outside image import (S18), Johnson TF 2019 CTA template revisions (S21).
- "radiology report pertinent negatives referring physicians survey" -> Eskander 2010 AJNR PMC7964006 (S09) - the only located study with an explicit pertinent-negatives question.
- CAP cancer protocol FAQ page (S13) via WebFetch.
- 40 CFR 312 (GovInfo 2020 edition PDF) (S19). eCFR renderer API returned empty file.

## Unsuccessful / consequential gaps
- **Clarification calls**: "radiology report clarification phone calls referring clinicians structured reporting reduced calls"; Europe PMC "(radiology) AND structured report* AND (telephone OR phone call* OR clarification) AND referring" -> no study measuring referring-clinician call volume before/after structured reporting. Only trade-press items (Gunn 2013 AJR feedback study on report complaints; revision-rate study S21). Implication: the recipient-work outcome most relevant to the thesis (fewer clarification requests) appears untested publicly in radiology; would require internal call logs.
- **Pertinent negatives as isolated variable**: no experiment manipulating presence/absence of pertinent negatives and measuring recipient behavior; only stated-preference survey (S09).
- **Outside pathology report completeness as driver of re-review**: Europe PMC query combining second opinion/outside + synoptic/required elements + referral -> nothing on point. Studies report discrepancy rates but do not attribute them to incomplete outside reports vs interpretive error.
- **ASTM E1527-21** (astm.org product page) -> HTTP 403; standard paywalled. User responsibilities and report viability rules therefore only via 40 CFR 312 (S19). **ASTM E2018** not attempted further (paywalled) - gap.
- PubMed pages (pubmed.ncbi.nlm.nih.gov) -> cookie wall for WebFetch; Europe PMC used instead (no access controls bypassed).
- Not pursued for time: RSNA RadReport adoption statistics; ESR white papers on structured reporting; Canadian (Ontario/CAP-ACP) synoptic initiative primary reports (Srigley 2009); cost-effectiveness of second-opinion pathology; clinicians independently re-reading images.
