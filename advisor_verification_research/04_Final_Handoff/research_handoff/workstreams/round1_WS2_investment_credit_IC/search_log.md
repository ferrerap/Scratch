# WS2 search log (2026-11-15, approx. 18:35–19:00 UTC)

## Regulatory and supervisory sources
- **SR 11-7.**
  - `curl` of federalreserve.gov `sr1107a1.pdf`, `sr1107.htm` and `sr1107.pdf`: all returned "Page not Found" HTML.
  - WebSearch then showed that SR 11-7 was **superseded by SR 26-2 (2026-04-17)**.
  - Downloaded SR2602.pdf and SR2602a1.pdf successfully, giving WS2-S01.
  - OCC Bulletin 2011-12 PDF URL returned 404.
- **FDIC.** The model risk examination module (rc-mrm.pdf) downloaded and gave WS2-S02. FIL-22-2017 was also downloaded (context only).
- **OCC s.939A rules and guidance.**
  - The Federal Register API citation search worked.
  - federalregister.gov full-text pages returned a "Request Access" bot page.
  - govinfo PDFs worked: 2012-14168 gave WS2-S03.
  - eCFR renderer API worked for 12 CFR 1.2 and 1.5 (WS2-S04).
- **2023 interagency third-party risk guidance.** Found via the FR API; govinfo PDF worked (WS2-S05).
- **EBA GL/2020/06.**
  - The first PDF found (nbb.be) was the Dutch translation.
  - The English PDF from eba.europa.eu worked (WS2-S06).
- **SEC rules.**
  - eCFR worked for 240.15Ga-2 and 240.17g-10 (WS2-S18).
  - Form ABS Due Diligence-15E: the sec.gov URL I guessed returned 404, so the item text was not retrieved.

## Rating agency criteria (renewables)
- **Fitch.**
  - Searched for "Renewable Energy Project Rating Criteria" with independent engineer, P90/P99 and haircut terms. The criteria document itself was not found or accessed.
  - The 2012 Fitch CDFA slide deck downloaded (WS2-S07).
  - The ESMAP Fitch training PDF returned a Cloudflare "Just a moment" bot page. Not bypassed.
  - The Topaz rating action was read via WebFetch on MarketScreener (WS2-S08). A direct curl returned a stub.
- **KBRA.**
  - The project finance methodology (2021) page loaded only the table of contents; the body is behind a login (recorded, not used).
  - "Trends in KBRA's Renewable Portfolio" (2022): the KBRA page needs a login, and BusinessWire, Jotup and financialcontent returned 403 or redirect loops.
  - Only search summaries were seen (WS2-S10, access "other").
- **S&P.**
  - The criteria text was not found.
  - The "How bright are production forecasts for Spanish solar plants" article (2024) returned 403.
  - The spglobal research PDF returned an HTML stub.
  - *Implication:* receiver-side rating methodology on IE reports is largely behind logins. Public testing has to rely on dated slides or on rating actions.
- **Moody's and Morningstar DBRS.** Not attempted after the S&P and KBRA blocks, because of the timebox. Both are typically login-gated.
- **Forecast accuracy.** The kWh Analytics 2021 index was reached via PV Tech through WebFetch (WS2-S09). The original report was not retrieved.

## Independent engineer / lender's technical advisor procurement
- **Green bank RFP search.**
  - Found the 2014 NY Green Bank lender's engineer RFP summary on nyserda.ny.gov. WebFetch returned 403 and curl returned HTML; not accessed.
  - Connecticut Green Bank RFPs found were mostly development technical assistance or inspection, not lender IE work. Not used.
- **World Bank PPP sample terms of reference ("Technical Due Diligence Wind Power Project").** WebFetch returned 403, curl returned an HTML stub, and the energypedia mirror was empty. Not accessed.
- **Hope Enterprise Corporation RFP** (Solar for All engineering technical assistance, 2025) via CESA: downloaded (WS2-S11). This is the only actual lender-side scope of work I obtained.
- **DOE LPO.** The search surfaced LPO pages and DOE-OIG-25-32, which downloaded from oversight.gov (WS2-S17). The LPO application pages themselves were not fetched (timebox).
- *Implication:* public, current lender IE scopes with reliance language are scarce in open procurement. Most IE engagements are private contracts.

## M&A, private equity and board reliance
- **Vendor due diligence, quality of earnings and reliance letters.** Search found mostly advisory-firm marketing. Used Rosen/EisnerAmper 2018 (WS2-S13), with key excerpts verified verbatim via curl.
- **Delaware DGCL s.141(e).** The delcode.delaware.gov statute text worked (WS2-S12).
  - Brehm v. Eisner: Justia returned 403 and the CourtListener API needs authentication. Not retrieved.
- **s.939A empirical effects.** The search found no study of changes in bank due-diligence behaviour after s.939A. An American Banker piece on small banks and the OCC rule was found but is paywalled, so not accessed.
  - *Implication:* the behavioural effect of mandated internal credit assessment appears untested in open literature (absence of evidence).

## IC memo and AI integration
- Searches for named private equity, credit or renewable investors describing AI in IC memos or diligence verification returned only vendor content: Hebbia, Model ML, Stack AI, V7, Multimodal, neurons-lab and others. No named buyer-authored account with verification detail was found.
- Used Model ML's workflow page (WS2-S14), with key text verified verbatim via curl. Not used: secondary vendor claims about "verification burden" (neurons-lab) and a cited S&P 2026 PE survey (via a blog; not verifiable).
- "Investment committee memo" process searches led to the Addepar/Stanford research brief PDF (WS2-S15).
- A job-posting search for renewable investment associates with IC memo duties led to the Capital Dynamics PDF (WS2-S19). No posting found explicitly mentioning "independent engineer reports".
- Model audit and AI: the Forvis Mazars page (WS2-S16) was verified verbatim via curl.

## Overall implications for public testability
- I found no public measurement of how lender, credit or IC reviewers split time between W1–W5, or of end-to-end effects of integration.
- The Addepar brief reports zero peer-reviewed articles on investment memos as of March 2023.
- Discriminating evidence will likely require field observation or proprietary data, such as lender credit files, IE report versions and IC question logs.
