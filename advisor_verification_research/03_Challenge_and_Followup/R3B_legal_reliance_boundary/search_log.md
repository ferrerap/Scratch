> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from R3B's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

## R3B search log (2026-11-15, about 18:58–19:10 UTC)

**Statutes and rules**
- `curl https://www.law.cornell.edu/uscode/text/15/77k` → full text; extracted §11(b)(3) and (c). (S01)
- `curl` eCFR renderer API for 17 CFR 230.176 → full text. (S02)

**Case law**
- `curl` Justia for WorldCom, BarChris and Brehm → **blocked** (Cloudflare "Just a moment" challenge page).
- CourtListener API v4 search → **blocked** ("Authentication credentials were not provided"). CourtListener HTML → 403 (CloudFront).
- WebFetch of CourtListener citation URLs (/c/F. Supp. 2d/346/628/, /c/A.2d/746/244/) → empty content.
- WebSearch: "In re WorldCom ... 346 F. Supp. 2d 628 underwriters comfort letters red flags full text" → only case briefs and a Proskauer memo; not used as sources.
- WebSearch: "Brehm v. Eisner 746 A.2d 244 section 141(e) ... full text" → no opinion text.
- WebSearch: "Escott v. BarChris ... 283 F. Supp. 643 full text" → index pages only.
- **Worked:** Harvard Caselaw Access Project static JSON (static.case.law) for f-supp/283/0643, f-supp-2d/346/0628, a2d/746/0244, a2d/488/0858 → full opinions. (S03, S04, S08, S09) Note: the CAP OCR has minor artefacts ("20%" for 20½; "bebeves"); these were avoided in excerpts or flagged.

**Comfort letters and negative assurance**
- WebFetch pcaobus.org AS 6101 page → **403**.
- WebSearch: "AS 6101 ... 'cannot make any representations' sufficiency ... negative assurance" → found the PCAOB consolidated standards PDF and the Docket 058 proposal.
- `curl` of the PCAOB consolidated auditing standards PDF (FY on/after 2024-12-15) → **worked**; extracted AS 6101 (S05).
- `curl` PCAOB Docket 058 → small challenge page (**blocked**).
- WebSearch: "AU-C 920 ... negative assurance ... sufficiency of the procedures pdf AICPA" → AICPA text is behind a member login; Deloitte DART is a JavaScript app (not retrievable). AU-C 920 not reviewed; AS 6101 used instead (AU-C 920 is described as substantively derived from the same AU 634 source).
- WebSearch: "PCAOB proposed targeted amendments AS 6101 negative assurance 135-day November 2026" → Davis Polk update retrieved by curl (S06). PCAOB release itself not reviewed.

**Agreed-upon procedures**
- WebSearch: "agreed-upon procedures AT-C 215 ... sufficiency of the procedures" → only study aids; not used.
- WebSearch: "ISRS 4400 Revised ... pdf ifac" → the IRBA-hosted standard PDFs returned HTML block pages; the IFAC Basis for Conclusions PDF worked (S07).

**Reliance letters (M&A / project finance)**
- WebSearch: "reliance letter due diligence report lenders project finance independent engineer ... non-reliance" → Clifford Chance blog (S10) and EAIF Homa Bay lenders' technical adviser RfP (S11) retrieved. Brodies and Eversheds reliance-letter pieces were seen in snippets only and not used; R3C covers IE scopes.

**Implications for public testability**
- Doctrine and standards on the reliance boundary are fully public.
- No public source found measures recipient effort or detection under reliance versus investigation, or how often underwriters or lenders re-perform expert work.
- Model reliance-letter terms (LMA, IE standard forms) and English-law reliance cases were not found in open sources within the timebox.
