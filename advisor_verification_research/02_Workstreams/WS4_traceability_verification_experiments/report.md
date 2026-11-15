> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS4's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

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
