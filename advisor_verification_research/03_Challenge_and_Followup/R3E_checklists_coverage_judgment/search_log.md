> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from R3E's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

## R3E search log (2026-11-15, 19:01–19:13 UTC)

**Tools.** WebSearch (standard mode); Europe PMC REST API (abstracts and full-text XML); Crossref API (abstracts and bibliographic checks); IDEAS/RePEc pages; curl plus pdftotext for open PDFs. Downloads went to the scratchpad downloads/R3E folder only.

### Successful queries and paths
1. "Asare Wright 2004 effectiveness of alternative risk assessment and program planning tools in a fraud setting checklist" found Contemporary Accounting Research 21(2). Abstract taken from IDEAS (R3E-S01).
2. "Berbaum checklist satisfaction of search chest radiography Academic Radiology" found the 2006 and 2016 studies. Abstracts from Europe PMC (S10, S11).
3. Europe PMC title searches: "invisible gorilla strikes again" (S12), "Systematic viewing in radiology" (S13, full text from PMC4749649), "Checklists improve experts diagnostic decisions" (S14), Alberdi 2004 CAD (S15), Urbach 2014 Ontario (S16), Haynes 2009 (abstract read and cited in S16's limitations, not registered separately), Haugen surgical checklist trial (S17, the 2019 secondary analysis), Ely & Graber 2015 (S18), Povyakalo 2013 (read, not registered).
4. "Wilks Zimbelman 2004 decomposition…" found S03 via IDEAS. That search surfaced Simon, Smith & Zimbelman 2018 (S04, Crossref abstract).
5. "Hammersley Bamber Carpenter 2010 documentation specificity…" plus a Crossref search returned the published and SSRN abstracts (S02).
6. Crossref search on "Backof Carpenter Thayer construal level evidence formatting" found S05.
7. "Sirois Bédard Bera 2018 … eye-tracking" plus Crossref returned the synopsis (S06). The same search led to an open NHH seminar PDF (Järvinen et al., loan officers, eye-tracking), read in full (S07).
8. Crossref searches for Brasel et al. 2016 (S08, including the CIIA summary abstract) and Kachelmeier et al. 2020 (S09).
9. Crossref searches "Christensen Glover Wolfe CAM paragraphs…" and "audit procedures description in critical audit matter investors perceived assurance experiment" found S19 and S20.
10. All DOIs, volumes, pages and author names were checked against Crossref.

### Unsuccessful or partial searches (and what they imply)
- **Pincus 1989 red-flags questionnaire (AOS 14:153-163):**
  - IDEAS has no abstract.
  - ScienceDirect returned 403.
  - CORE PDFs were behind a Cloudflare challenge (not bypassed); WebFetch also returned 403.
  - Secondary snippets describe the questionnaire's usage and perceptions, not the users-versus-non-users result.
  - Its findings could not be verified, so it is not registered.
- **Asare & Wright full text:** only on a third-party document-sharing site, not used.
- **Sirois 2018 full text:** SSRN and publisher returned 403, and next.sciencegate.app did not resolve (outside the allowed network). The effect of the "procedures overview" condition is therefore unknown.
- **Brasel 2016 CIIA full text (publications.aaahq.org):** 403.
- **White Rose eprint on usefulness of key audit matters:** returned an HTML page, not the PDF.
- **"experiment users perceptions negative assurance review report versus audit report…":** found only older studies (1982 dissertation, 1993 study) through snippets. None isolates negative-assurance wording, and none was verified or registered.
- **"experiment agreed-upon procedures report factual findings users perceived assurance overreliance 'no exceptions'":** only standards, firm marketing pages and exam-prep material. No behavioral study found.
- **"experiment user auditors reliance on SOC 1 … description of tests … exceptions":** only practitioner and exam-prep material. No experiment found.
- **"pertinent negatives radiology report referring physicians … effect on clinical decision" and "referring clinicians preference itemized structured … pertinent negatives":** only stated-preference surveys, no behavioral test. Not registered, since structured-reporting surveys are already in the register.
- **Randle 2020** (Journal of Accounting and Finance; commercial loan officers and critical audit matters; lower approval probability) was seen via Crossref. It was not registered because it is a lower-tier venue with an abstract only. A follow-up could check it.
- **Not searched (time):** aviation checklist studies; workpaper-review experiments on preparer documentation; Hoffman & Zimbelman 2009 (brainstorming and strategic reasoning).

**Implication.** The core CL026 question ("checked, no findings" versus silence, and coverage tables versus none, measured on recipients' detection of material issues) appears untested in public research. The nearest tests are the auditor's-report experiments above, which measure attention, decision change, liability or calibration rather than detection.
