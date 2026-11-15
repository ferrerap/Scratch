> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS7's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

# WS7 search log (2026-11-15)
- pcaobus.org AS1210 page: WebFetch returned HTTP 403. Not retried with curl, per the brief.
- WebSearch "SEC order approving PCAOB amendments ... AS 1210" found: sec.gov 34-86270, govinfo FR 2019-06425, pcaob.org Docket044 PDF.
- sec.gov 34-86270.pdf (curl): "Request Rate Threshold Exceeded". Not read.
- govinfo FR-2019-04-04 html (curl): OK. Contains the Board's summary, not the full rule text.
- pcaob.org/Rulemaking/Docket044/2018-006-specialists-final-rule.pdf (curl): OK, 149 pp; App. 1 holds the rule text. ACCESS ROUTE USED.
- Bansal PDF (microsoft.com): OK. Buçinca PDF (harvard): OK.
- Choi et al.:
  - UMN landing page: OK, abstract only.
  - viewcontent.cgi PDF: Cloudflare challenge (curl), 403 (WebFetch).
  - SSRN 4626276: Cloudflare (curl), 403 (WebFetch).
  - minnesotalawreview.org PDF: Cloudflare (curl), 403 (WebFetch).
  - law.umn.edu news page: qualitative only.
  - TaxProf Blog: SSRN abstract (N=60, four tasks).
  - Two WebSearches for per-task percentages: only the Legal Futures range (12–32%).
  - Conclusion: per-task effect sizes are not publicly testable without full-text access.
- arXiv 2112.11471 (Lai): OK, but this is the 2021 survey; the FAccT 2023 camera-ready was not retrieved.
- arXiv 2302.02187 (Schemmer), 2212.06823 (Vasconcelos), 2305.07722 (Fok & Weld), 2001.08298 (Buçinca 2020): all OK.
- PMC3240751 (Goddard): OK.
- PubMed 37129490 (Dratsch): cookie/bot page from both curl and WebFetch. WebSearch then found the RSNA press release; curl of the release: OK.
- ScienceDirect, Skitka 2000 (accountability): Elsevier page, not read. The accountability claim is recorded only via Goddard.
- WebSearch for Commerford et al. 2022: abstract OK via the UNLV repository.
- Not searched in this timebox: dedicated searches for experiments testing citation/provenance (X3) with professional reviewers of advisor reports; engineering-review studies. These gaps remain open for other workstreams.
- Downloads are stored only in the scratchpad downloads/WS7 folder. No PDFs were copied to the project folder.
