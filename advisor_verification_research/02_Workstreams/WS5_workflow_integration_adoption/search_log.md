> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS5's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

1. Humlum & Vestergaard: NBER w33777 PDF via curl worked. It is the March 2026 revision, retitled.
2. Lee et al., CHI 2025: Microsoft Research PDF worked.
3. Workslop: HBR article body is paywalled (WebFetch returned only the header). The BetterUp blog was retrieved; its sample size is inconsistent (1,004 vs 1,150). A university-hosted copy of a follow-up HBR article was not used because its licensing is unclear.
4. UK DBT and Australian Treasury Copilot evaluations: PDFs worked. Press figures like "35 minutes longer" are not in DBT's Table 5 and were not used.
5. Board packs:
   - Search found the Board Intelligence blog (vendor) and the Society for Corporate Governance (SCG) blog.
   - NACD 2024 figures appear only on Board Intelligence pages, so they were not used.
   - PwC 2026 directors survey ("82% see opportunities to improve materials", search snippet only): pwc.com returned 403, so this is unverified.
   - Diligent/Nasdaq was not searched (time).
   - UNSUCCESSFUL: no survey quantifying preparer hours or reformatting of board packs.
6. IC-memo AI case studies: vendor claims only (V7, Binocs, Agentman, Brownloop). Binocs was fetched.
7. UNSUCCESSFUL: no independent before/after measurement of end-to-end IC or credit-approval cycle time. P3.1 is not currently testable from public sources in this domain.
8. Buyer accounts:
   - Morgan Stanley Debrief press release returned 503. The Celent "30 min saved" figure was not verified or used.
   - A&O, Moonfare and PCAOB worked. The PCAOB PDF came via WebFetch's saved binary and was extracted with pdftotext.
9. Procurement:
   - Entergy Appendix D retrieved.
   - NY Green Bank and CT Green Bank lender's-engineer RFPs were not retrieved (time).
   - UNSUCCESSFUL: no investor-side RFP found that requires advisor deliverables in IC-template format.
10. Bloom et al., NBER w24249: worked.
11. Dietvorst et al.: core.ac.uk returned HTML; the Wharton preprint worked.
12. MIT NANDA "GenAI Divide": the mirror returned not found. Not used (weak method anyway).

Downloads are in `/tmp/claude-0/-home-user-Scratch/896551fc-74fd-5092-857d-f83fd4afd7e5/scratchpad/downloads/WS5/`. Files written to `/home/user/Scratch/advisor_verification_research/02_Workstreams/WS5_workflow_integration_adoption/`: `sources.json` and `evidence.json`.
