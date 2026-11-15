> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS6's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

# WS6: Rival explanations, failures, and disconfirming cases

Run date 2026-11-15. 18 sources (WS6-S01 to S18), 25 evidence items (WS6-E01 to E25), 16 evidence groups. The `relationship` field is relative to the named proposition. Several propositions are rivals (P1.3, P1.6, P2.3, P2.5, P3.2), so "supports" there means the item cuts against the unconditional thesis.

## Bottom line
1. **Not refuted, but narrowed to a conditional form.**
   - Explanations reduce verification effort, without losing error detection, only when they make checking cheaper than redoing (E07).
   - Narrative explanations either raise acceptance regardless of correctness (E06) or are ignored (E08).
   - AI polish raises perceived quality even when the answer is wrong (E05).
2. **Three drivers of review that traceability does not address:**
   - formal obligation (E18, E22);
   - the accountability structure, i.e. who reviews, when, and for whom (E25, E16);
   - egocentric discounting and the wish to own the analysis (E14, E12).
3. **AI-assisted output adds recipient rework (W3).** When citations are fabricated, traceability gives false assurance (E19, E20, E21, E23).
4. **Perceived and measured effort diverge** (E02), so testimonials and surveys are weak evidence for P2.1 and P6.1.

## RQ1: Why review persists
- **W1 obligation:**
  - Mata v. Avianca: Rule 11 makes the attorney the gatekeeper for accuracy (E18).
  - The minister expects department processes to ensure consultant quality (E22).
  - After the failure, the Premier's office ordered a review of guidelines, i.e. more review (E23).
  - Traceability cannot remove the duty, though it may make the duty cheaper to discharge.
- **P1.6 accountability, comfort or ritual:**
  - Tetlock: "most forms of accountability do not have beneficial effects"; accountability after a decision produces bolstering (E25).
  - Lerner & Tetlock, abstract only (E16).
  - Pentland, secondary summary: audit rituals produce comfort (E17).
  - The evidence is weak. If the rival holds, traceability may be used to defend positions rather than to check them.
- **W3 inaccurate output:**
  - METR: fewer than 44% of AI suggestions accepted; 75% of developers read every line (E03).
  - BCG: 19 percentage points lower correctness (E04).
  - Fabricated references (E20, E21, E23).
  - Workslop survey: 1 h 51 min per incident, self-reported (E24).
  - Traceability lowers the cost of each check, not the number of checks.
- **W2 opacity (supports the thesis):**
  - Opaque AI was mostly ignored in 2 of 3 radiology departments (E10).
  - Yaniv's proposed mechanism: judges see their own reasons but not the advisor's (E13). Untested.
- **Egocentric discounting and ownership:**
  - Judges heavily discount advice far from their own view (E14).
  - Use of an algorithm rose from 32% to 73-76% when even trivial modification was allowed, and did not depend on how much modification was allowed (E12).

## RQ2: Verification cost vs quality
- **Persuasion rival (P2.3), supported** by E06 (Bansal) and E05 (BCG).
  - These involve model or narrative explanations (X1/X2), not source links (X3).
  - Counterpoint: hard written explanations made no difference compared with giving the prediction alone (E08).
- **Conditional support for the thesis (E07):**
  - Highlight explanations reduced overreliance compared with written ones. Contrasts: -1.63 (95% CI -2.78 to -0.56) and -1.63 (95% CI -2.57 to -0.69).
  - The authors attribute earlier null results to explanations "not sufficiently reducing the costs of verifying."
- **Effort-accuracy trade-off:**
  - The designs that most reduced overreliance were the least liked (E09).
  - Successful integration added time (E11).
- **Citations do not guarantee correctness (P2.5):**
  - Mata v. Avianca (E19).
  - Charlotin database: 2,293 decisions, 913 involving lawyers, no denominator (E20).
  - DEWR report: 14 fabricated references and a fabricated quote (E21).
  - Newfoundland and Labrador (E23).
- **Disclosure can backfire (analogy only):** when conflicts were disclosed, advisors exaggerated more and recipients under-corrected (E15). Relevant to scope disclosures (X4) turning into boilerplate.

## RQ3: Integration
- AI help can move effort rather than remove it: E01 (+19% time), E11, E24.
- Letting recipients modify output raises uptake (E12), but the mechanism appears to be control, not better verification.
- I found no evidence that integration reduces total end-to-end recipient work. That is an absence of evidence, not evidence of absence.

## Rivals and observations that would discriminate
- **R1 Obligation.**
  - Predicts: time on governance steps does not change.
  - Test: activity logs that split governance from reconstruction, under high vs low traceability.
- **R2 Accountability/ritual.**
  - Predicts: review effort follows the audience and decision stage, not evidence quality.
  - Test: vary accountability while holding evidence fixed, and vice versa. Log whether reviewers open linked sources, and whether they open confirming or disconfirming ones.
- **R3 Output quality.**
  - Predicts: review falls as the error rate falls, whatever the traceability.
  - Test: a factorial experiment crossing seeded error rate with traceability, measuring both time and detection of seeded errors and omissions.
- **R4 Persuasion.**
  - Predicts: time falls because detection falls.
  - Test: the same factorial. If time and detection both fall, R4 holds; if time falls and detection holds, the thesis holds.
- **R5 Egocentrism/ownership.**
  - Predicts: rework depends on whether the conclusion agrees with the team's prior.
  - Test: compare agreeing vs diverging conclusions, with editability and traceability as separate treatments.
- **R6 Effort-accuracy trade-off.**
  - Test: time to check one claim with pinpoint links vs document-level citations vs narrative rationale.
- **R7 Disclosure backfire.**
  - Test: compare advisor reports before and after a traceability or disclosure standard (caveat counts, citation padding, detection of omissions).
- **R8 Fabrication.**
  - Test: do clients check citations at all (E22 suggests some do not)? Compare links that resolve to original documents with free-text references.

## Strongest counterevidence (ranked)
1. BCG: E04, E05.
2. METR: E01-E03.
3. Bansal: E06.
4. Lebovitz: E11.
5. Deloitte cases: E21-E23. These suggest the value of traceability may lie in tail risk and after-the-fact auditability rather than less routine review.

## Evidence that supports the thesis
E07, E10, E13, and partly E12.

## Transferability to renewable-energy diligence
- **Mechanisms that transfer:**
  - the cost of checking each claim (E07);
  - polish masking error (E05);
  - fabricated references (E21, E23);
  - bolstering in committees (E25, my inference);
  - non-delegable duty (E18).
- **Consequential differences:** the experiments use lay participants or producers, not reviewing clients. Source documents (PPAs, interconnection agreements, independent engineer reports) can be checked if links resolve to them.
- **Still to verify:**
  - whether IC reviewers open linked sources;
  - the split between reconstruction and governance work;
  - error rates in AI-assisted advisor deliverables.

## Limitations
- No study tests professional clients reviewing advisor reports with vs without traceability.
- Causal evidence is lab, producer-side or qualitative.
- Deloitte evidence is news only; primary sites were blocked and Hansard was not verified.
- Lerner & Tetlock: abstract only. Pentland: secondary summary. Cain et al. 2005: via the authors' 2011 summary.
- The workslop survey (E24) is vendor-hosted and weak.
- The METR confidence interval is shown only in a figure and was not extracted.

## Unresolved questions
1. How review time splits across W1-W5 in advisor-client work.
2. Whether pinpoint traceability reduces time per check while keeping seeded-error detection, with professional reviewers.
3. Whether reviewers use traceability to check or to bolster.
4. Whether public failures make clients increase review of all advisors.
5. Whether the main value is less routine effort or lower tail risk (relevant to P6.1).
