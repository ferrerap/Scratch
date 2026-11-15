> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS1's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

# WS1 search log (2026-11-15, roughly 18:36–18:50 UTC)

## Successful
- **PCAOB specialists rulemaking.** WebSearch "federalregister.gov PCAOB Using the Work of an Auditor-Engaged Specialist…" led to the govinfo HTML of 84 FR 13442 (2019-06425), full text, and SEC 34-86270 (downloaded, not used substantively).
- **ISA 620.** The iasplus PDF link returned HTML (failed). Used FRC ISA (UK) 620 June 2016 instead. Also used the IAASB Jan 2026 basis for conclusions on the experts amendments (ifacweb blob).
- **ISA 402 and ISAE 3402.** The FRC landing page had no direct PDF, so I used AUASB ASA 402 (Dec 2023). The IFAC ISAE 3402 staff overview (2 pages) was used for context only. The ISAE 3402 basis for conclusions (IFAC) was full text.
- **ISA 610 and ISA 500.** AUASB compiled PDFs.
- **Other auditors.** SEC 34-95488 (2022).
- **PCAOB interim analysis (Release 2022-008).** curl is blocked on pcaobus.org, but WebFetch saved the PDF binary, which I converted locally.
- **Academic sources.**
  - Griffith et al. 2015, Griffith 2020 and Glover et al. 2019: IDEAS abstracts.
  - Griffith 2018: search excerpts plus the UW news article.
  - Boritz 2020 and Cannon & Bedard 2017: search summaries only.
  - Glover, Taylor & Wu 2017: full text from typeset.io (provenance uncertain).
  - Commerford & Holman 2022: full text from NHH.

## Unsuccessful or consequential
- **pcaobus.org:** AS 2601 WebFetch returned 403. AS 1210, AS 2605, AS 1105 App. A verbatim text and PCAOB spotlights/inspection observations after 2020 were not retrieved, so post-2020 deficiency patterns are unverified.
- **SSRN 3404297:** 403. **econbiz:** bot-protection block. **iasplus news:** empty.
- **Griffith & Hammersley 2019 VT draft:** downloaded but marked "do not quote or cite without permission", so not used.
- **Not searched for lack of time:** AICPA SOC 1 / AU-C 402 guide, Big 4 workpaper-review descriptions, Pentland 1993, Joe et al. 2017, the PIR follow-up interim analysis.
- **Implication for testability:** I found no public data that splits auditor time into mandated evaluation versus reconstruction caused by missing documentation. The distinction is set out in the standards, but publicly it remains a hypothesis.
