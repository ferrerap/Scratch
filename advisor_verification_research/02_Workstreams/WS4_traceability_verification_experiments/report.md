# WS4 — Traceability, explanations & human verification of AI output (2026-11-15)

> Provenance note (coordinator): WS4 reported that its own write of this file was refused by the harness. This file is the coordinator's verbatim record of the report text WS4 returned in its final message (Appendix A), saved by the coordinator as part of preserving workstream reports. Temp IDs (WS4-E##) map to stable EVR IDs via `01_Evidence/id_mapping.json`.

Counts: 17 sources, 25 evidence items, 17 evidence groups. Bansal/Buçinca left to WS7. Excerpts are verbatim except typography (±→"+/-", minus sign→"-", curly→straight quotes, ∼→~).

**Bottom line (WS4):** Traceability to sources (X3) reliably protects error detection when used, but does not reliably reduce verification time, and is rarely used by default. Precise claim-level linking can cut time ~20–25%; whether detection is preserved depends on (a) link precision/correctness and (b) whether the error lives in the cited fact or in the reasoning over it. Evidence is almost entirely lay participants, short tasks. No study measured time AND detection for professionals reviewing a third party's source-linked analysis.

## RQ2
**1. Sources (X3) vs AI narrative (X1)**
- E01: equal accuracy (0.73 vs 0.74), but sources cost 2.53 vs 1.01 min per claim.
- E02: when the AI is wrong — narrative 0.35 vs 0.49 baseline vs 0.54 sources. Equal time on right and wrong narratives. Quoted source snippets inside the narrative did not protect.
- E03: narrative + sources gave no complementarity: 2.7 min, and 0.43 vs 0.54 when the AI was wrong. Contrastive explanations helped when the AI was wrong but hurt when it was right.
- E21: an LLM without links halved time (1.6 vs 3.4 min). On the item it got wrong: 47% vs 93% accuracy, and 0 re-queries.

**2. Precise linking**
- E19 SymGen: −20% time, detection unchanged.
- E20 HoT: −25% time, but detection of wrong answers fell from 72.2% to 54.8%.
- E07: highlighting answers in short sources had no detectable effect (studies stopped early).
- Inference: linking helps when the error is in the linked fact; it lends false grounding to wrong reasoning over correct facts.

**3. Persuasion and low checking (P2.3)**
- E12: random citations raised trust; 1 citation ≈ 5.
- E13: only 193/1,976 (9.77%) of cited answers were checked; checked random citations gained no trust.
- E10: logged clicks far below self-reported use.
- E18: about 1% of AI-summary visits included a link click.
- E05: citation precision vs perceived utility, r = −0.96 (system-level averages).

**4. Citations ≠ correctness (X3 ≠ X5)**
- E04: 51.5% of statements fully supported; 74.5% citation precision.
- E23: 50–90% of medical answers not fully supported; ~30% of statements unsupported even with retrieval; automated checker agreed with physicians 88% of the time.
- E24 (legal RCT): hallucinated sources — 3 with the RAG tool, 4 with no AI, 11 with o1-preview. Miscitations not counted.

**5. Uncertainty and coverage (X4)**
- E09: accuracy 63.9% → 72.8%; per-item time rose on uncertain items.
- E22: 26% → 58%/53%, via follow-up queries at a small time cost.
- No test of disclosing checks with no findings.
- E15: traces mentioned hints they used in only 25–39% of cases, and reward hacks in under 2%. An AI trace saying "no issue" is weak evidence of absence.
- E08: Fok & Weld note verification is often one-sided.

**6. Faithfulness (X2) vs persuasiveness (X1)**
- E14: biasing features drove answers unmentioned (accuracy down up to 36%).
- E15: low faithfulness.
- E17 (clinicians): heatmaps did not rescue detection of a biased model (+2.3 pp, CI −2.7 to 7.2).
- E08: Fok & Weld argue verifiability, not faithfulness, is what matters.
- E06: explanations reduce overreliance only when verification is much cheaper than solving; stakes also reduce overreliance.

## RQ1
- E25: fact-checkers (stated, not observed) say opacity makes tools unreliable, and want a replicable trail plus disclosed gaps. Supports P1.2; does not test P1.1.
- E16: attribution checking took 73–264 s per item after training and rose with source length.

## RQ3
- E21, E24: time savings measured for the producer or user, not a downstream reviewer.
- E11: a 50%-accurate AI increased both time (2.13 vs 1.57 min) and errors (63.9% vs 74.2% accuracy).
- No downstream reviewer time measured, so P3.1 vs P3.2 is untested.

## Counterevidence
- E20: linking increased acceptance of wrong answers.
- E03: narrative cancels the benefit of sources.
- E17: professionals did not detect a biased AI.
- E10/E13/E18: low checking rates.
- E07: null result for short-source highlighting.

## Limitations
- Mostly crowdworkers or students; one planted error; binary outcomes.
- No tests of omissions or judgment errors.
- SymGen and HoT report no significance tests.
- Jabbour and Pew read via summaries.
- Some sources by AI developers or search providers (Anthropic, Microsoft, Google, Deloitte co-authors).

## Unresolved questions and discriminating studies
1. **Do professionals reviewing an advisor memo do better with claim-linked sources?** An RCT with credit or investment analysts, with planted factual, reasoning and omission errors. Measure time per claim, detection by error type, and logged source opens.
2. **Does error location interact with linking?** Cross error location (cited fact vs reasoning) with links on or off.
3. **Does disclosing scope and checks with no findings change what reviewers re-check?**
4. **Professional citation-checking rates**, from logs rather than self-report.
5. **Reviewer time on grounded vs ungrounded drafts.**
