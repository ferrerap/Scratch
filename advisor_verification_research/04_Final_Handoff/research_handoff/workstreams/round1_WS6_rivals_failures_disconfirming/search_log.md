# WS6 search log (2026-11-15, ~18:36-18:50 UTC)

## Successful paths
- arXiv PDFs via curl + pdftotext: METR 2507.09089 (S01); Bansal 2006.14779 (S03); Vasconcelos 2212.06823 (S04); Bucinca 2102.09692 (S05).
- Dell'Acqua et al. working paper: MIT Sloan-hosted SSRN PDF (S02).
- Lebovitz et al. 2022: NYU Law-hosted publisher PDF (S06).
- Dietvorst et al.: Wharton marketing manuscript PDF (S07). core.ac.uk copy returned HTML (blocked).
- Yaniv & Milyavsky: Bar-Ilan seminar copy (S08); journal citation checked via Crossref.
- Loewenstein, Cain & Sah 2011: CMU PDF (S09) as a substitute for paywalled Cain et al. 2005.
- Lerner & Tetlock 1999: abstract only, via NCBI E-utilities (S10). The PubMed web page required cookies. A Southampton PDF found by search was a different paper (Sedikides et al. 2002).
- Mata v. Avianca ECF 54: CourtListener RECAP PDF (S12).
- Charlotin AI Hallucination Cases database: WebFetch (S13).
- Deloitte DEWR: ACS Information Age (S14); Region Canberra on Senate Estimates (S15).
- Deloitte Newfoundland and Labrador: The Independent (S16).
- BetterUp workslop blog (S17).
- Tetlock interview, GovExec (S18).

## Queries (WebSearch, standard)
- "Deloitte DEWR report fabricated references partial refund department statement updated report"
- "dewr.gov.au Targeted Compliance Framework assurance review final report Deloitte updated 26 September 2025"
- "Senate estimates October 2025 DEWR Deloitte report final instalment generative AI Hansard ..."
- "should not be double-checking a third-party provider's footnotes" (exact phrase; no primary or Hansard hit)
- "Chris Rudge University of Sydney discovered fabricated references Deloitte DEWR ..."
- "Newfoundland Labrador Health Human Resources Plan Deloitte citations errors government statement 2025"
- "Lerner Tetlock 1999 Accounting for the effects of accountability pdf"; second query adding "preemptive self-criticism" / "defensive bolstering"
- "Pentland 1993 Getting comfortable with the numbers ..." (two variants)
- "Dell'Acqua Navigating the Jagged Technological Frontier working paper 24-013 pdf"
- "Yaniv Kleinberger 2000 Advice taking in decision making egocentric discounting pdf"
- "Dietvorst Simmons Massey Overcoming algorithm aversion modify pdf"
- "Cain Loewenstein Moore 2005 The Dirt on Coming Clean pdf"
- "Lebovitz Lifshitz-Assaf Levina 2022 To Engage or Not to Engage with AI ..."
- "workslop BetterUp Labs Stanford Social Media Lab survey ..."
- "Mata v. Avianca 2023 opinion sanctions Castel ..."

## Unsuccessful or blocked paths, and what they imply
- **dewr.gov.au** (report page, three PDF versions, FOI correspondence PDF): HTTP 503, connection reset, or HTTP/2 INTERNAL_ERROR on every attempt (WebFetch and curl).
  - finance.gov.au FOI document: 503 and connection reset.
  - Wayback Machine: the availability API reported a 2025-10-07 snapshot, but fetching it failed (WebFetch refused web.archive.org; curl tunnel closed by the proxy). Not pursued further.
  - Implication: the primary record of the correction note, the AI disclosure text and the refund letter could not be verified. News reports form one evidence group.
- **aph.gov.au** Estimates summary PDF returned HTML. The Hansard transcript was not located, so the Senate Estimates quotes are unverified against Hansard.
- **CTV News (Newfoundland and Labrador government pledge):** article body not returned. Government primary statements not retrieved.
- **Paywalled or blocked:**
  - ScienceDirect (Pentland abstract): 403.
  - scilit: 403.
  - Crossref and Semantic Scholar: abstracts elided by the publisher for Pentland, Lerner & Tetlock, and Bonaccio & Dalal.
  - CORE downloads: HTML or blocked.
- **Not accessed for time or access reasons:**
  - Bonaccio & Dalal (2006) review.
  - Yaniv & Kleinberger (2000) and Yaniv (2004) originals.
  - Power (1997) The Audit Society (OUP page lookup hit a wrong page).
  - Dietvorst et al. (2015).
  - Cain et al. (2005) original.
- **No public study found of professional clients reviewing outside advisor deliverables with vs without traceability.** No public time-and-motion data was found splitting review into governance vs reconstruction. This suggests the core discriminating tests are not publicly testable with existing literature and would need new data collection, e.g., log data or seeded-error experiments with practitioners.
- **No documented case found of a professional review tool being formally abandoned because verification burden exceeded benefit,** beyond:
  - Lebovitz (2 of 3 radiology departments mostly ignored opaque AI);
  - METR (fewer than 44% of AI generations accepted).
