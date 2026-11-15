> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from R3A's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

## R3A search log (2026-11-15, about 18:58–19:10 UTC)

**Searches that produced included sources:**
- "primary care clinicians review LLM-drafted patient portal message replies errors not caught Biro npj Digital Medicine" → Biro 2025 (S01). Full text from Europe PMC; PMC returned a reCAPTCHA and nature.com redirected to a login page.
- "Biro Ratwani 2025 npj Digital Medicine patient portal AI drafts errors physicians time to review" → confirmed the citation.
- "radiologists AI-generated draft reports seeded errors detection reading time reader study 2025" → Acosta 2024 (S05). Also turned up Hong (Radiology) and a JMIR 2026 study where the LLM itself detects errors (both excluded, see below).
- "clinicians detect errors in LLM-generated clinical summaries with source attribution highlighting user study verification time" → NYU commentary (S04), which led to Small 2025 (S03); Scout preprint (S07); JMIR Human Factors provenance study (S11).
- "ambient AI scribe randomized trial documentation time note quality errors omissions NEJM AI 2025" → Lukac (S08), Afshar (S09). Abstracts from Europe PMC; PubMed blocked on cookies.
- "Chen 2024 Lancet Digital Health large language model respond patient messages physicians unedited drafts harm" → S02. Author manuscript from Europe PMC. A DEV Community post gave inconsistent details and was ignored.
- "clinicians reviewing AI scribe generated notes seeded errors detection rate simulation study 2025" → Biro JMIR 2025 (S10). Mentions of an Asgari npj study, a Mayo Clinic Proceedings: Digital Health simulation and the "One note in three" preprint were not followed up.
- "Abridge Linked Evidence evaluation clinicians verify AI-generated note transcript study" → vendor support page (S12, HTTP 403). No independent evaluation found. The vendor white paper (Aug 2025) was not retrieved.
- "financial analysts experiment verifying LLM extracted figures from filings with page citations accuracy time user study" → FinGround (S13). Also a NeurIPS 2024 desiderata paper (abstract only, not included) and a Hebbia vendor survey (not included; outside this question).
- "Huang 2025 JAMA Network Open generative AI draft radiograph reports…" → S06.
- Europe PMC title search for Tai-Seale "AI-Generated Draft Replies Integrated Into Health Records" → S14.

**Searches that found nothing relevant (these matter for the conclusion):**
- "auditors experiment generative AI output source documents citations evidence evaluation error detection audit judgment 2025" → no completed experiment. Only the Holmstrom & Peters PCAOB registered report, which has no results yet.
- "internal auditors field experiment generative AI audit task quality time…" → no auditor study. Found a public-sector field experiment (arXiv 2502.09479), not about auditors or traceability; not included.
- "experiment lawyers reviewing AI contract review output accuracy time clause citations missed issues" and "lawyers randomized experiment AI-assisted contract review with source links…2025 2026" → only vendor AI-vs-lawyer comparisons (LawGeex 2018, Onit "Better Call GPT", Ivo). None tests lawyers reviewing AI output with clause links. Schwarcz and Choi are already in the register.
- "randomized study physicians LLM answers with versus without source citations verification accuracy time hallucination detection" → nothing direct. A preprint (huggingface 2606.28960) had a citation arm but its results were not visible. The PRECISE trial (NCT07037940) is registered; I found no results.
- "'seeded errors' OR 'inserted errors' physicians review LLM-generated discharge summary…" → no seeded-error study found. Only error-prevalence studies (Williams ED summaries; Osborne 2026 npj).

**Screened and excluded:**
- Traceable Text (arXiv 2409.13099): phrase-level provenance, but participants were mostly patients or lay people (21 recruited, 16 from a patient advisory council).
- Hong et al., Radiology 2025: accuracy of the model's reports, not a time-and-detection study of radiologists reviewing them.
- LawGeex 2018: vendor study comparing AI with lawyers, not lawyers reviewing AI.
- The Star (July 2026) article on a real-world portal-drafting evaluation: HTTP 503, original study not identified.

**What this implies about public testability:** the with/without traceability × seeded-error × professional-reviewer design appears not to have been published in medicine, audit, law or finance as of this date. Its main parts already exist separately: deployed link features (Abridge Linked Evidence), citation-first tools (Scout), and seeded-error protocols (Biro, Acosta). So the study is feasible, but the result is not in the public record.
