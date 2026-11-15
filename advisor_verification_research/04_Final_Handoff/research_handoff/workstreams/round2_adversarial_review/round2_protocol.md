# Round 2 — Adversarial review protocol

All three reviewers receive the SAME evidence bundle:
- `01_Evidence/sources.json` and `01_Evidence/evidence.json` (merged, stable SRC/EVR IDs; `temp_id` + `workstream` fields map back to workstream files)
- `01_Evidence/register_stats.json` (counts, merged duplicates, multi-document evidence groups)
- `02_Workstreams/*/report.md` and `search_log.md` (worker findings, limitations, unsuccessful searches)
- `00_Start_Here/research_instructions.md` (definitions W1–W5, X1–X5, proposition catalog P1.1–P6.1)

Roles are temporary analytical roles, not conclusions. Each reviewer must cite evidence IDs (EVR###) for every claim, acknowledge adverse evidence, and state what observation would change their interpretation.

## Reviewer A — strongest defensible case FOR the thesis
For each proposition in the catalog that has evidence: the strongest defensible reading that supports the thesis (traceability/coverage visibility/integration can reduce avoidable recipient work while preserving judgment), the conditions under which it holds, adverse evidence acknowledged, and what would change the interpretation. Must not overclaim: separate direct evidence from analogy; mechanism from commercial relevance.

## Reviewer B — strongest defensible ALTERNATIVE explanation or limitation
For the same propositions: the strongest rival account (e.g., review persists because of obligation/accountability/comfort; traceability raises trust more than accuracy; integration relocates work; customer-specific adaptation dominates), conditions, adverse evidence acknowledged, and what would change the interpretation.

## Reviewer C — audit
Audit the register and worker reports for: factual fidelity (re-check consequential statistics and quotations against originals where retrievable), causal claims stronger than design allows, duplicate underlying evidence counted as independent, cross-domain transfers lacking limitation statements, missing denominators/controls, selective reporting, conclusions stronger than evidence. Produce issue-level findings with EVR/SRC IDs and recommended corrections.

## Outputs
(Amended 18:56 — see run_log D09: narrative reviews are returned as text in each reviewer's final reply and saved verbatim by the coordinator as R2x_*.md; reviewers write only structured JSON: `R2A_positions.json`, `R2B_positions.json`, `R2C_audit_findings.json`.)
- `03_Challenge_and_Followup/R2A_case_for_thesis.md` + `R2A_positions.json`
- `03_Challenge_and_Followup/R2B_alternative_case.md` + `R2B_positions.json`
- `03_Challenge_and_Followup/R2C_audit.md` + `R2C_audit_findings.json`

`R2x_positions.json`: array of {proposition_id, position_summary, holds_under_conditions, supporting_evidence_ids, adverse_evidence_ids_acknowledged, would_change_my_view_if, strength_of_evidence_note (qualitative, no numeric scores)}.
`R2C_audit_findings.json`: array of {issue_id (R2C-01...), issue_type (fidelity / causal_overclaim / duplicate_evidence / transfer / denominator_control / selective_reporting / overclaim / other), ids_affected, description, verified_against (what was re-checked, with locator), recommended_correction, severity (high/medium/low)}.

## Coordinator after Round 2
Compare A vs B at proposition level -> dispute register (DIS###) with evidence IDs on each side; fold C's corrections into the register (patches recorded in `scripts/manual_overrides.json`, never silently); convert disputes into neutral, discriminating Round 3 questions (not "find evidence for side X").
