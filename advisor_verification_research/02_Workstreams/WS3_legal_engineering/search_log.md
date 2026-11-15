> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS3's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

**Succeeded:**
- arXiv 2405.20362 (v1).
- jolt.richmond.edu/jolt-archive/v17i3/article11.pdf (after the /files/2011/04/ path returned 404 and scholarship.richmond.edu hit a Cloudflare challenge).
- eCFR renderer API for App. B (nrc.gov returned a "Request Access" page).
- CourtListener RECAP storage PDFs for Da Silva Moore (Doc 96) and Mata (Doc 54). Justia was Cloudflare-blocked; the CourtListener API needs authentication.
- Steptoe-hosted Rio Tinto (Doc 207).
- standardsforhighways.co.uk CG 300 attachments (v0.1.0, v0.2.0, v0.2.1).
- PEER report 2017/06.
- sback.it PDFs for Bacchelli 2013 and Sadowski 2018.
- Sedona TAR Case Law Primer 2d ed., public-comment version.
- Charlotin database landing page.

**Failed or blocked:**
- americanbar.org ABA 512: Cloudflare via curl, 403 via WebFetch. Got verbatim text via josephhollander.com (Stephens 2024), NCBE Bar Examiner and National Law Review.
- Schwarcz et al.: UMN PDF Cloudflare/403, SSRN Cloudflare. Abstract via WebFetch summary only; Law360 seen only as a search snippet; UMN Law magazine read.
- Published JELS Magesh PDF (nlp.stanford.edu): connection reset twice.
- In re Broiler Chicken validation protocol: the govinfo hit was a different order (Doc 1090), not used.
- ABA 08-451: only secondary summaries found, not included.
- Choi et al. Minnesota Law Review: guessed URL returned 404; left to WS7.

**Not attempted (time):**
- Owner's/independent engineer submittal-review mechanics (WS2 may cover).
- ASME NQA-1 (paywalled).
- Experiments timing professional reviewers with vs without evidence linkage in legal or engineering settings.

**Implication:**
- Primary ABA opinions and law-repository papers are bot-blocked; court records are reachable via RECAP.
- No public data found on supervising-lawyer or engineer review time.
