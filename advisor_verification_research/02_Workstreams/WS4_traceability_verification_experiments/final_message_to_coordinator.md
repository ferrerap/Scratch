> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS4's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

**WS4 summary**

Only 2 of the 4 output files exist. sources.json and evidence.json are written and validated. The harness refused report.md, and search_log.md would hit the same block, so I didn't attempt it. I didn't try to get around this. Both texts are in Appendices A and B below; please save them as report.md and search_log.md in the WS4 folder. Folder: /home/user/Scratch/advisor_verification_research/02_Workstreams/WS4_traceability_verification_experiments/

**Counts:** 17 sources, 25 evidence items, 17 independent evidence groups.

**Main findings**
1. **Sources vs AI narrative (WS4-E01–E03):** sources took 2.5x longer (2.53 vs 1.01 min) for the same accuracy (0.73 vs 0.74). When the AI was wrong, accuracy was 0.54 with sources, 0.35 with the narrative, and 0.49 with no aid. Adding a narrative on top of the sources helped nothing.
2. **Exact claim-to-source links (WS4-E19, SymGen):** about 20% faster (1.98 vs 2.50 min) with error detection unchanged (80.8% vs 80.0%). Lay participants, one planted error.
3. **Counterexample (WS4-E20, HoT):** highlighting the facts behind the reasoning cut time 25% but dropped detection of wrong answers from 72.2% to 54.8%. Citing the inputs does not show the reasoning is valid.
4. **Citations are rarely checked:** 9.77% of cited answers were checked (WS4-E13). Clicks on links in AI summaries happened in about 1% of visits (WS4-E18). Logged clicks were 2.7–7.2% while 75–86% said they used the links (WS4-E10). Even random citations raised trust (WS4-E12).
5. **Showing uncertainty (WS4-E09, E22):** improved appropriate reliance (63.9→72.8%; 26→58%) by moving effort to risky claims, not removing it. No experiment tested disclosing checks that found nothing.

**Strongest counterevidence:** HoT (WS4-E20). Also Jabbour, JAMA 2023 (WS4-E17): a biased AI cut clinicians' accuracy by 11.3 percentage points, and explanations recovered a non-significant 2.3 points.

**Gaps:** I found no study that measures both checking time and error detection for professionals reviewing a source-linked analysis.

**Access limits:** Jabbour and Pew were read through WebFetch summaries, not line by line. Fok & Weld, SymGen and SourceCheckup venues, and Schwarcz's journal, are unverified. I didn't pursue Gaube, Goh, radiology automation-bias work, or Magesh.

---

## Appendix A — report.md

# WS4 — Traceability, explanations, and human verification of AI output (2026-11-15)
17 sources, 25 evidence items, 17 evidence groups. Bansal and Buçinca are left to WS7. Excerpts are verbatim apart from typography (±→"+/-", minus sign→"-", curly→straight quotes, ∼→~).

**Overall:** traceability to sources (X3) reliably protects error detection when people use it. It does not reliably cut checking time, and use is low by default. Exact claim-to-source links can save about 20–25% of the time. Whether detection holds depends on (a) exact, correct links and (b) whether the error sits in the cited fact or in the reasoning drawn from it. The evidence comes almost entirely from lay participants on short tasks. No study measured both time and error detection for professionals reviewing someone else's source-linked analysis.

### RQ2
**1. Sources (X3) vs AI narrative (X1)**
- E01: same accuracy (0.73 vs 0.74), but sources take 2.53 vs 1.01 min per claim.
- E02: when the AI is wrong, accuracy is 0.35 with the narrative vs 0.49 baseline vs 0.54 with sources. People spent the same time on right and wrong narratives. Quotes from the sources inside the narrative didn't protect them.
- E03: narrative plus sources gave no added benefit, took 2.7 min, and scored 0.43 vs 0.54 when the AI was wrong. Contrastive explanations helped when the AI was wrong and hurt when it was right.
- E21: an LLM without links halved task time (1.6 vs 3.4 min). On the item it got wrong, accuracy was 47% vs 93%, and nobody re-queried.

**2. Exact links**
- E19 SymGen: 20% faster, detection unchanged.
- E20 HoT: 25% faster, but detection of wrong answers fell from 72.2% to 54.8%.
- E07: highlighting answers in short sources had no detectable effect; the studies were stopped early.
- My inference: links help when the error is in the linked fact. They make wrong reasoning built on correct facts look grounded.

**3. Persuasion and low checking (P2.3)**
- E12: even random citations raised trust; one citation was trusted as much as five.
- E13: 193/1,976 cited answers (9.77%) were checked; checked random citations earned no extra trust.
- E10: logged clicks were far below self-reported use of the links.
- E18: links in AI summaries were clicked in about 1% of visits.
- E05: citation precision vs perceived usefulness r=-0.96 (system-level averages).

**4. Citations ≠ correctness (X3 ≠ X5)**
- E04: 51.5% of statements fully supported by citations; 74.5% citation precision.
- E23: 50–90% of medical answers not fully supported; about 30% of statements unsupported even with retrieval; automated check agreed with physicians 88% of the time.
- E24 (legal trial): fabricated sources were 3 with the grounded tool, 4 with no AI, 11 with o1-preview. Miscitations were not counted.

**5. Uncertainty and coverage (X4)**
- E09: accuracy 63.9→72.8%; individual uncertain answers took longer.
- E22: 26→58% / 53%, through follow-up queries at a small time cost.
- No test of disclosing checks that found nothing.
- E15: reasoning traces mentioned hints they used in only 25–39% of cases and reward hacks in under 2%. When an AI trace reports no problem, that is weak evidence that none existed.
- E08: Fok & Weld note verification is often one-sided.

**6. Faithfulness (X2) vs persuasiveness (X1)**
- E14: biasing features drove answers without being mentioned (accuracy down up to 36%).
- E15: faithfulness was low.
- E17 (clinicians): heatmap explanations didn't help them detect a biased model (+2.3 percentage points, CI -2.7 to 7.2).
- E08: Fok & Weld argue faithfulness matters less than whether the answer can be verified.
- E06: explanations reduce overreliance only when checking them costs much less than solving the problem; higher stakes also reduced overreliance.

### RQ1
- E25: fact-checkers (stated, not observed) say opacity makes tools unreliable and want a replicable trail plus disclosed gaps. This supports P1.2 and doesn't test P1.1.
- E16: checking attribution took 73–264 s per item after training and grew with source length.

### RQ3
- E21, E24: time savings were measured for the person producing or using the AI output.
- E11: an AI that was right 50% of the time increased both time (2.13 vs 1.57 min) and errors (63.9% vs 74.2% accuracy).
- No reviewer time measured downstream, so P3.1 vs P3.2 is untested.

### Counterevidence
- E20: links raised acceptance of wrong answers.
- E03: adding a narrative cancelled the benefit of the sources.
- E17: professionals didn't detect a biased AI.
- E10, E13, E18: low checking rates.
- E07: highlighting short sources did nothing.

### Limitations
- Participants were mostly crowdworkers or students, with one planted error and binary answers.
- No tests of omissions or judgment errors.
- SymGen and HoT report no significance tests.
- Jabbour and Pew were read via summaries.
- Some sources come from AI developers or search providers (Anthropic, Microsoft, Google, Deloitte co-authors).

### Open questions and the studies that would answer them
1. **Do professionals reviewing an advisor memo do better with claim-to-source links?** An RCT with credit or investment analysts that plants factual, reasoning and omission errors. Measure time per claim, detection by error type, and logged source opens.
2. **Does error location interact with linking?** Cross where the error sits (cited fact vs reasoning) with links on or off.
3. **Does disclosing scope and checks with no findings change what reviewers re-check?**
4. **Professional citation-checking rates.** Use logged behavior, not self-report.
5. **Reviewer time on grounded vs ungrounded drafts.**

## Appendix B — search_log.md

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
