> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS7's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

# WS7 — Methods, source quality, and transferability audit
Files: sources.json (15), evidence.json (26). Evidence groups (12): pcaob2018-specialists-AS1210 (S01, S02), bansal2021, bucinca2021, choi2024 (S05–S07), lai2021-2023, schemmer2023, goddard2012, vasconcelos2023, fokweld2024, bucinca2020, dratsch2023, commerford2022.
Findings are what the sources report. Analyst inferences are labeled. WS7 has no direct evidence on renewable-energy (RE) diligence; the target column in Part C is my characterization and needs verification.

## Part A — The four initial leads
| Lead | Access | Participants | Stakes | Advisor–client? | Can establish | Cannot establish |
|---|---|---|---|---|---|---|
| AS 1210 (+ AS 1105 App. A) | Full rule text, PCAOB Rel. 2018-006 App. 1 (pcaob.org; pcaobus.org returned 403); 84 FR 13442 | Issuer auditors | High | YES: specialist → engagement partner → opinion | Non-delegable evaluation (E01); risk-scaled extent (E02); required report of work performed, with limitations triggering more work (E03); mandated re-testing for company specialists (E04); objectivity drives procedures (E05); inspections found under-review (E06); prevalence (E07) | Time or effort, compliance rates, whether traceability reduces review |
| Bansal CHI'21 | Full | MTurk lay, ~100 per condition | Low | No | Explanations ≈ confidence-only on accuracy (Beer 0.88 vs 0.89, p=.24) (E08); higher agreement when the AI was right, lower accuracy when it was wrong (E09); less validation when checking was costly (E10) | X3 provenance, experts, objective time (authors' caveat, E11) |
| Buçinca CSCW'21 | Full | MTurk lay, N=199 | Low | No | Cognitive forcing > simple explanations on wrong-AI items (carb-source detection 0.27 vs 0.08, d=.66), but both < no AI (0.49) (E12); trust and preference correlated negatively with performance on wrong-AI items; designs that reduced overreliance most were liked least (E13) | Expert behavior, effort cost |
| Choi et al. MLR 2024 | Abstract only | 60 law students | Moderate | No (drafting own work) | Large speed gains, slight and inconsistent quality gains; quality gains concentrated in lower-skilled participants (E14); news report says 12–32% time savings (unverified) | Review of others' work, error detection, exact effect sizes |
Summary: only AS 1210 has the advisor–client structure, and it records obligations, not effects. None of the leads tests X3 (traceability to source evidence) in an advisor setting.

## RQ1 — Why does review persist?
- The obligation is formal and cannot be delegated (W1): the recipient must test consistency with its own work, other evidence, and its own understanding (E01). For aligned specialists, data, assumptions and methods must be re-tested (E04). Supports P1.1.
- Review is meant to scale with significance, risk and specialist competence; traceability is not a factor (E02). Qualifies P1.1.
- Lower objectivity requires more procedures (E05). Analyst inference: in field data, perceived independence confounds any traceability effect.
- The regulator observed under-review and failures to act on contradictory evidence (E06). This challenges reading review as ritual (P1.6).
- Felt accountability reduced automation bias (2 studies positive, 1 null for external manipulation) (E19).

## RQ2 — Cheaper without worse?
- Verification cost is the key mechanism. Easy-to-check highlights beat written explanations (E21). Explanations helped only on hard tasks (E22). Explanations help only to the extent they enable verification, and many tasks do not allow it (E23). Supports P2.1/P2.2 for cheaply checkable evidence (X2/X3-like), not for persuasive rationales (X1).
- P2.3 is supported: E08, E09, E12, E13, E25.
- Errors pass through even to experts: RR 1.26 (E18); radiologist accuracy fell from 82% to 45.5% (E24).
- Professionals can also under-rely based on source labels: auditors discounted AI-attributed evidence (E26).
- The standard treats disclosure of scope and limitations (X4) as a precondition for reliance (E03). That shows an obligation, not an effect.

## RQ3 — Integration
- No direct WS7 evidence.
- Drafting assistance saves time with little quality change (E14). This is narrow support for P3.3 (W5) and says nothing on P3.2.
- Firms that moved to earlier and more frequent communication with specialists saw fewer inspection findings (E06). Weak, uncontrolled evidence.

## Part B — Methods
Limits of the literature: experts rarely studied (E15); efficiency rarely measured (E16); professional studies show both automation bias (E24) and algorithm aversion (E26).
Discriminating designs:
1. Seeded errors, with outcomes split by whether the advice was correct (E09, E12).
2. Judge-first sequential design measuring RAIR/RSR (correct switches to good advice vs correct rejections of bad advice) (E17) and negative consultations (correct initial judgment changed to incorrect after advice) (E20).
3. Per-item time and action logs together with detection rates, with CIs.
4. Omission probes to test coverage and "no findings" statements (X4).
5. Citation-faithfulness manipulation (correct, irrelevant, or fabricated sources) to separate X3 from X1 and X5.
6. Accountable professional participants, with felt accountability manipulated (E19).
7. Satisfaction and trust only as secondary outcomes (E13, E25).

## Part C — Transferability rubric (H/M/L = similarity to the target; analyst judgment)
| Dimension | RE diligence target (analyst characterization) | Audit | Legal | Engineering | Medicine | Lab human–AI |
|---|---|---|---|---|---|---|
| Accountability / liability | IC or credit committee owns the decision; advisor liability capped by contract and reliance letters | H (E01, E19) | M (students in E14 bear none) | M (no WS7 evidence) | M (E24) | L |
| Regulation | Contractual, internal policy, prudential rules | L–M (E01–E06) | M | M | M–H | L |
| Task structure | Long reports and models; mix of verifiable facts and judgmental forecasts | H (E04) | M (E14) | H (by analogy) | L–M (E24) | L (E21, E23) |
| Expertise | Senior specialists and generalists | H (E26) | M | H | H (E24) | L (E15) |
| Error consequences / detectability | Large, delayed, often unobservable at decision time | M–H | M | M–H | H | L |
| Cadence / volume | Low volume, high value, deal-timeline pressure | M | M | M | L (E19) | L |
| Who pays the advisor | Often the sponsor pays the lenders' independent engineer (IE) | H (E04, E05) | M | M | L | L |
| Independence | Reliance on "independent" advisors | H (E05) | M | M | L | L |
| Overall | n/a | Highest for RQ1 mechanisms | Low–moderate (RQ3 drafting) | Unknown | Moderate (automation-bias risk) | Hypotheses only for RQ2 |
Rule: carry a mechanism over only if the source domain scores at least M on the dimensions the mechanism depends on.

## Strongest counterevidence
- E12, E18, E24: assistance can make detection worse than no assistance.
- E08, E09, E13: explanations raise acceptance without better accuracy, and protective designs are disliked.
- E06, E02: the regulator saw under-review, and traceability is not a scaling factor.
- E26: professionals discount machine-sourced evidence.

## Limitations
- Choi, Dratsch, Commerford, Fok & Weld and Buçinca 2020 are abstract or partial reviews.
- AS 1210 text is the 2018 adopted version; later amendments were not checked.
- Lai et al. was read in the 2021 arXiv version.
- No WS7 source tests real citations or provenance (X3) with professional reviewers of an advisor report. This is absence of evidence in my sources, not evidence of absence.

## Discriminating observations
- Randomized study with credit/IC professionals: traceable vs standard advisor report, seeded material errors and omissions. Outcomes: time per finding, detection rate, and correct-rejection (RSR-type) rate.
- Cross report format with advisor engagement structure (lender-engaged vs sponsor-engaged) and stated credentials.
- Omission probes with and without coverage disclosures.
- Felt-accountability manipulation, measuring negative consultations.
- End-to-end time-and-motion logs before and after integrating advisor outputs into IC memos, with downstream error tracking.
