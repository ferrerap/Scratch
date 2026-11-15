> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS4's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

- **Read from arXiv in full (curl + pdftotext):** 2310.12558 (Si), 2304.09848 (Liu), 2212.06823 (Vasconcelos), 2305.07722 (Fok & Weld), 2405.00623 (Kim), 2501.01303 (Ding), 2305.04388 (Turpin), 2505.05410 (Chen), 2112.12870 (Rashkin), 2311.09188 (SymGen), 2503.02003 (HoT), 2307.03744 (Spatharioti), 2402.02008 (SourceCheckup), 2502.09083 (Warren).
- **Other full text:** the Schwarcz PDF from law.berkeley.edu.
- **Via WebFetch summaries:** jamanetwork.com/journals/jama/fullarticle/2812908 (Jabbour; first 100k characters) and the Pew 2025-07-22 short read.
- **WebSearch queries:**
  - "user study verification time error detection LLM summary source highlighting evidence linking clinicians or analysts" → found SymGen and HoT. **No clinician or analyst study measuring both time and detection** — suggests this is not publicly tested.
  - "Jabbour 2023 JAMA…"
  - "Pew Research 2025 Google AI summary…"
  - "Schwarcz 2025 AI-Powered Lawyering…"
  - "Warren CHI 2025 Show Me the Work…"
- **Not pursued (time):** Gaube 2021, Goh 2024, Dratsch radiology automation bias, Magesh legal RAG, Bo et al. 2024 reliance interventions, LongEval.
- **Housekeeping:** one download (schwarcz.pdf) landed in /home/user/Scratch by mistake; it was moved to the WS4 downloads folder right away.
