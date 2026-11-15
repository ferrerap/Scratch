> Provenance note (coordinator): verbatim final hand-back of Reviewer A (R2A), saved by `scripts/save_handback.py`. Subagents return narrative as text per harness convention (see run_log D08/D09).

Reviewer A (case FOR the thesis). The positions file is at /home/user/Scratch/advisor_verification_research/03_Challenge_and_Followup/R2A_positions.json. It holds 19 positions (P1.1–P6.1). I checked that it loads with json.load and that every EVR ID in it exists in the register. As you corrected, the full narrative is below. I wrote nothing else, and there is no R2A_case_for_thesis.json.

# R2A — Strongest defensible case for the thesis

## Bottom line
The thesis holds up only in narrowed form. The evidence supports this version: **claim-level traceability to original evidence (X3) plus explicit coverage and test records, including checks without findings (X4), can lower the cost of the evaluation work that obligations already require, and can protect error detection better than generated explanations (X1) do.** That holds when the recipient's duty is to *evaluate* outside work rather than to *re-derive* it, and when errors can be checked against recorded sources.

The evidence does not support:
- that W1 judgement can be reduced;
- that integration reduces end-to-end work (P3.1 is untested in investment settings);
- any commercial link (P6.1).

Most support is mechanism, obligation or analogy, not direct evidence from advisor-to-IC workflows. Counts below are independent evidence groups, not documents.

## RQ1 — Why review persists

**P1.1 (formal obligations): conceded as a floor, but it does not settle the question.** About 18 groups across audit, banking, project finance, law, engineering and medicine make W1 non-delegable. Examples:
- audit: EVR001, EVR002, EVR011, EVR016, EVR166
- banking: EVR034, EVR035, EVR039, EVR042
- project finance: EVR043
- law: EVR066, EVR078
- engineering: EVR083, EVR085
- medicine: EVR209–211

The thesis-favourable reading: these obligations specify *what* the receiver must evaluate and scale effort to risk and significance. They cover source-data accuracy and completeness, significant assumptions and methods (EVR013, EVR169), with effort scaled per EVR001, EVR167, EVR012 and EVR017. They impose an obligation, not a method or a cost. OCC 939A explicitly lets banks rely on third parties for analytical work while keeping the decision (EVR039). ABA 512 allows less item-level review after testing a tool (EVR067), though EVR068 disputes this. Traceability can therefore target the cost of meeting W1, not W1 itself.

Adverse:
- UK CG 300 requires independent analysis "without exchange of calculation sheets" (EVR081). Here re-derivation is the control, and traceability is irrelevant by design.
- Medical second opinions find real discrepancies, for example 86/6,171 major changes (EVR209) and 53/94 stage discrepancies (EVR211). So re-review is often rational.
- In the PCAOB post-implementation review, partners said added time was under 1% of audit hours (EVR008). Effort may not respond much to rule text.

**P1.2 (avoidable reconstruction): defensible as a mechanism, not as a "material share".** About 10 groups show that missing evidence or scope raises recipient effort:
- PCAOB says specialists' work is "often not entirely transparent" and costly to evaluate (EVR007).
- ISA 402 directs extra procedures when a report lacks a description of tests (EVR020).
- Understanding context is the main cost in code review: 91% said unfamiliar files take longer (EVR087).
- PEER guidelines tell designers to highlight key assumptions so review is efficient (EVR086).
- Fact-checkers demand replicable reasoning (EVR115). Judges discount advice partly because they lack the advisor's reasons (EVR153).
- The one quantitative observed-behaviour item: repeat imaging was 52% when outside images were not imported vs 11% when imported, adjusted OR 9.0 (EVR212). It is abstract-only, observational and small.

No source measures the *share* of review that is avoidable.

The adverse evidence matters. In audit, opacity often produces **under-review** or comfort-seeking rather than reconstruction (EVR005, EVR171, EVR026, EVR027). That supports the error-detection half of the thesis more than the effort-reduction half.

**P1.3 (rework from advisor error): conceded, and it bounds the thesis.** Advisor errors are frequent enough to justify checking:
- medicine: EVR209–211
- solar output below P50 estimates: EVR047 (a news report), EVR048 (search summaries only)
- fabricated citations: EVR161, EVR163
- AI output needing major changes: EVR143, EVR144

The thesis-compatible point is that inspectable evidence makes errors cheaper to find. Disclosed TAR validation samples let the receiving party show that reported recall/precision of 85%/58% were really 97.4%/16.7% (EVR077). That case also produced a large amount of receiving-side work. Traceability does not touch W3 that comes from hidden modelling bias such as P50 bias.

**P1.4 (adaptation): conceded as a legitimate rival driver** (CL025). Recipients keep doing their own diligence because of their own requirements:
- banks overlay vendor models (EVR036);
- rating agencies apply their own haircuts to independent-engineer outputs (EVR045, EVR046);
- shared reports are not tailored to a given recipient (EVR021, EVR053);
- templates differ between firms (EVR055);
- output needs editing to fit organisational guidelines (EVR120).

The only favourable reading: explicit assumptions let adaptation be applied as a documented overlay (EVR036) rather than a reconstruction. The adaptation judgement itself stays with the recipient.

**P1.5 (reformatting): plausible but weak** (K001):
- one survey of 54 organisations: 97% use memos, 86% use templates that differ between investors, about two months of writing and review (EVR055);
- respondents call memo writing a "pain" (EVR056);
- a job posting (EVR061) and board-pack surveys (EVR132, EVR133).

This is stated burden, not measured time, and there is little published research on memos (EVR057).

**P1.6 (ritual, accountability, distrust): double-edged** (CL027). Some review is not driven by errors:
- comfort rituals (EVR157, secondary summary);
- only 14% of code-review comments are about defects (EVR088, EVR090);
- the "myth" of exhaustive manual review, with manual recall of 25–80% (EVR074);
- egocentric discounting of advice (EVR153, EVR154).

The part caused by lack of access to the advisor's reasons is addressable. Courts accepted validated coverage evidence in place of exhaustive review (EVR069, EVR071). The part driven by accountability is not informational, and accountability effects are conditional (EVR165, EVR156). The strongest adverse fact remains that inspectors saw *under*-review (EVR005, EVR171), so "avoidable review" may be the wrong target in some settings.

## RQ2 — Cheaper verification without worse verification

**P2.1 (traceability reduces time): only for fine-grained provenance** (about 4 groups):
- Linking each number to its source cell cut decision time from 2.50 to 1.98 minutes with unchanged accuracy (EVR109). The study is small, no significance tests were located, and the provenance was correct by construction.
- Highlighting cited input facts cut time from 62 to 47 seconds (EVR110).
- Visual explanations that are easy to check reduced overreliance (EVR186, EVR147).

Coarse evidence went the other way:
- reading retrieved passages took about 2.5x longer than reading explanations, at equal accuracy (EVR091);
- more specific specialist memos took longer (EVR033);
- AI tools added time for radiologists (EVR151).

Low click-through suggests some apparent time savings come from skipping checks (EVR103, EVR108).

**P2.2 (detection preserved or improved): conditional, and X3 beats X1.**
- When the explanation was wrong, users given sources scored 0.54, users given the explanation 0.35, and the no-help baseline 0.49 (EVR092).
- Provenance preserved accuracy (EVR109).
- Checking was useful only when cheaper than solving the problem (EVR096).
- Disclosed samples exposed misreported metrics (EVR077).
- A relational cue improved auditors' judgements, conditionally (EVR028).
- Checklists reduced non-fracture misses (EVR201) and raised completeness (EVR197, EVR199).

Adverse evidence is of similar weight:
- highlights tied to model reasoning lowered accuracy when the model was wrong, 54.8 vs 72.2 (EVR110);
- adding an explanation to sources hurt (EVR093);
- explanations failed against a biased AI (EVR107);
- a structured reporting system worsened residents' reports (EVR196), and it is the only top-level study in that field (EVR194);
- prefilled templates carried contradictory statements (EVR202).

**P2.3 (trust without detection): conceded as a design constraint** (about 9 groups):
- random citations raised trust (EVR102);
- about 10% of cited answers were checked (EVR103), and links in AI summaries got about 1% of clicks (EVR108);
- citation precision was inversely related to perceived utility (EVR095);
- explanations raised acceptance whether the AI was right or wrong (EVR146, EVR173, EVR174);
- graders scored incorrect AI-assisted answers higher (EVR145);
- the designs that protect users most are liked least (EVR177, EVR178).

So the thesis must be judged on detection and appropriate reliance, never on satisfaction. Uncertainty and coverage cues (X4) are the exception that helps: accuracy rose from 63.9% to 72.8% (EVR099) and from 26% to 58% (EVR112).

**P2.4 (coverage visibility): the thesis's strongest ground, mostly normative** (CL026):
- IAASB keeps the requirement to describe tests and results because user auditors need them to link to their own work (EVR019, EVR022, EVR023). Missing descriptions trigger extra procedures (EVR020).
- The AAI rule requires a report to identify data gaps (EVR214). SEC rules require disclosure of due-diligence criteria (EVR060).
- Courts accept recall estimates, sampling of the excluded ("null") set and disclosed protocols under adversarial challenge (EVR069, EVR071, EVR075, EVR076).
- 89% of clinicians and 92% of radiologists said pertinent negatives are useful (EVR203, stated preference).

Important qualification: IAASB judged sample-level detail for tests that found nothing unnecessary and costly (EVR022). So "checks without findings" should be shown at the level of test nature and scope.

Adverse: EVR196, EVR202, EVR192 (higher ratings without better effectiveness), EVR072 (courts split on seed-set transparency), EVR068.

**P2.5 and P2.6: fully conceded and built into the thesis.**
- Citations are not correctness: 17–33% hallucination in source-citing legal tools (EVR062, EVR063), 51.5% citation recall (EVR094), plus EVR113, EVR161 and EVR080.
- Generated rationales can be unfaithful (EVR104, EVR105).

The thesis should therefore rest on records that can be checked (X3/X4), not on narratives (X1/X2).

## RQ3 — Workflow integration

**P3.1: not established.** The best evidence is an analogy that separates integration from mere availability: 52% vs 11% repeat imaging (EVR213, EVR212). Other support is vendor or practitioner claims without method (EVR054, EVR136, EVR135). Adverse:
- government evaluations found small or no measured productivity gains (EVR123);
- average time savings were about 3% (EVR117);
- developers believed AI saved about 20% while measured time rose 19% (EVR142), so self-reported savings are unreliable.

**P3.2: conceded as the default when outputs are unreliable.** Effort shifts rather than disappears (EVR119, EVR116, EVR141, EVR151, EVR122, EVR127, EVR101). The favourable reading: QA time fell for outputs that are easy to check and rose for complex ones (EVR125). The net sign depends on checkability, which is what traceability targets.

**P3.3: plausible for assembly and summarisation, not analysis.**
- Memo-survey respondents suggest automating field population (EVR056).
- The clearest trial benefits were summarising and drafting (EVR128).
- Blind-scored sessions found better summaries but worse spreadsheet analysis (EVR124).
- Adverse: EVR120, EVR144.

**P3.4: one evidence group.** Uptake rose from 32% to 73–76% when people could modify the algorithm's output (EVR140 and EVR152 are the same group). That is uptake, not appropriate use.

## Secondary questions
- **P4.1, supported** (CL029). National templates covered only 17–49% of the concepts in one centre's reports (EVR206). Other evidence: EVR193, EVR055, EVR137, EVR036. Deployment needs domain-aware configuration, not a checklist upload.
- **P5.1, formats only** (AS06 assets, not economics). One department built 228 templates covering 94% of volume (EVR204); see also EVR199 and EVR207. Against: a shared lexicon still gave weak agreement on judgement, kappa 0.28 (EVR216); adherence was 77% for resections vs 19% for biopsies (EVR208).
- **P6.1, CL007 and AS03: unsupported.** Satisfaction and NPS were high without measured productivity gains (EVR126). The purchase case was framed as a break-even of about 13 minutes a week, not measured (EVR129). Firms in a consulting RCT bought more consulting later, but the benefit was operational, not reduced review (EVR139).

## What would change my view
1. Renewable IC or lender policies turn out to require CG 300-style independent re-derivation.
2. Time-use data show W2 is a small share of retained effort.
3. Professional experiments with seeded errors show claim-level provenance or coverage statements lower detection, or that time saved comes from skipped checks.
4. Recipients re-perform at unchanged rates despite full traceable evidence, which would point to review driven by comfort.
