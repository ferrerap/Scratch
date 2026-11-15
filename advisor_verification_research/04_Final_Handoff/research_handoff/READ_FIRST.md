# READ FIRST — Advisor Verification Research (run of 2026-11-15)

## What was investigated
Whether better evidence traceability and workflow integration can reduce the work accountable professionals do when evaluating and using an outside advisor's analysis, without weakening their independent judgment. Three core questions:
- **RQ1:** why review persists.
- **RQ2:** what makes verification cheaper without making it worse.
- **RQ3:** whether integration into decision materials adds distinct value.

Secondary questions RQ4–RQ6 (customer-specific implementation, repeatability, buying and supplier economics) were pursued only where the core work surfaced a connection.

Domains covered:
- audit reliance on specialists, SOC reports and comfort letters;
- bank credit, model risk and rating agencies;
- renewable project finance (independent engineer scopes, yield back-tests);
- legal review (AI legal tools, e-discovery technology-assisted review, securities due-diligence doctrine);
- engineering design checking and code review;
- medicine (structured reporting, second opinions, AI drafts, health information exchange);
- mortgage appraisal review;
- lab human–AI verification experiments.

## Strongest findings
1. **Non-delegable evaluation core.** The recipient's duty is to *evaluate*, not *re-perform*, in most regimes. A core persists whatever the advisor's transparency: deciding, vetting the producer, judging sufficiency, following up red flags, and building a record of one's own investigation. Re-performance is not legally required absent red flags. A few regimes deliberately mandate independent verification or re-derivation. (EVR039, EVR166, EVR240, EVR246, EVR247, EVR249; EVR081, EVR083.)
2. **Checkable evidence beats persuasive explanation.** It protects error detection better when the producer is wrong (EVR092, EVR186). But traceability is not correctness: cited outputs are often unsupported or wrong (EVR062, EVR094, EVR236). Citations raise trust even when irrelevant (EVR102), yet are rarely checked (9.77% of cited answers; EVR103).
3. **Integration at the point of use reduces duplicated work, moderately.** Integrating outside evidence into the recipient's working system is consistently associated with less repeat imaging in medical studies. The pooled standardized effect is −0.17, and two abstract-only observational studies show 16–67% relative reductions. There are offsets and one national null result (EVR259, EVR263, EVR265, EVR266, EVR268). Integrating others' *analysis* can import their judgments and lower skepticism (EVR222, EVR272).
4. **Target domain: lender work is adaptation driven by measured bias.** In renewable project finance, publicly described lender work on energy yield (one lender presentation, one rating action) consists of adaptation: own P-cases, haircuts and sizing rules. The lender justifies it by forecast bias it reports seeing, not by opacity. Independent back-tests found pre-construction wind P50s over-predicted by 6.6–7.4% across 115 assessments (EVR275–EVR277, EVR285, EVR297). Linking the adaptation to the bias is analyst inference.

## Most important counterevidence
- **Lighter review means more surviving errors.** Professionals reviewing AI drafts missed most planted errors. Residents edited LLM drafts less and left more confabulations. Time savings can come from checking less. (EVR219, EVR223, EVR110)
- **Generic checklists narrow attention.** Used as the method of review, generic checklists or decomposition were associated with lower fraud-risk assessments and poorer abnormality detection in professional experiments (abstract-level evidence; EVR298, EVR303, EVR309).
- **Disclosure does not discharge the duty.** Procedure-and-findings disclosure does not move the recipient's legal duty, and sophisticated recipients reportedly want an accountable conclusion, not just a list of checks (EVR245, EVR249, EVR252).
- **Credit review cut through risk transfer, not transparency.** Where recipient review visibly fell in credit (mortgage appraisal), the mechanism was liability transfer to the consequence-bearer. Standardization coincided with producer fee pressure and substitution (EVR329, EVR326, EVR336).
- **Under-review is the observed failure.** Regulators observe under-review of outside specialists more often than excessive review (EVR005, EVR171). A public lender had a conflict-of-interest blind spot about borrower-side advisors (EVR059).

## Biggest unresolved issue
No public source measures how recipient effort splits between required judgment (W1) and avoidable reconstruction (W2). No published study gives accountable professionals advisor output with versus without claim-level traceability and coverage disclosure and measures both effort and detection of seeded errors (DIS001, DIS003; searches documented in `workstreams/round3_R3A_*` and `round3_R3C_*`).

**Smallest observations that would resolve it:**
1. **Seeded-error experiment.** A 2×2 design with 20–40 credit or IC analysts: traceability (claim- and calculation-level links: yes/no) × coverage table (yes/no). Use one realistic advisor report with seeded factual, calculation, reasoning and omission errors, some inside and some outside the listed scope. Measure time per section, catch rate by error type, logged source opens, and calibration.
2. **Matched time logs.** Matched-deal logs from one investor of review hours coded W1–W5, with the advisor report delivered as PDF vs as linked model and memo sections.

## What this research does NOT establish
- That reducing recipient effort creates willingness to pay, renewal, pricing power or supplier margins. No supporting public evidence exists (EVR126, EVR129). The one credit-domain standardization case points the other way for producers.
- Any size of avoidable work, time savings, or market for renewable-energy IC or lender workflows.
- That findings from lab participants, medicine, audit or securities law transfer to private renewable-energy investors. Each transfer is labelled with its limits in `research_brief.md`.
- Any change to the canonical ledger, dashboard or user convictions. `revision_candidates.json` contains *proposals only*.

## Evidence base (final)
- **Sources:** 211 (SRC001–SRC212; one ID retired after merging duplicates).
- **Evidence items:** 341, of which 3 are flagged duplicates not counted.
- **Independent evidence groups:** 202 (201 with at least one evidence item).
- **Source access:**
  - full text: 122
  - partial: 32
  - abstract only: 48
  - other: 7
  - blocked: 2
- **By round:** Round 1 contributed 126 sources and 217 items; Round 3 follow-ups contributed 85 sources and 124 items.
- **Verification:** 23 consequential statistics were re-checked against originals by the Round 2 auditor (all matched). 25 audit issues were corrected via recorded overrides.
- **Reading relationship counts:** relationship labels in `evidence.json` are relative to the proposition each item tests. Several propositions are rival explanations, so a "supports" label can cut against the thesis.

The register is larger than the brief's 20–35-source working target. This is because eight parallel workstreams and six follow-ups each documented their own sources. Nothing was added to reach a quota. Weight of evidence should be read from evidence-group counts and from the kind of evidence (obligation / observed / experiment / self-report / vendor), not from totals.

## File guide
| File | Contents |
|---|---|
| `research_brief.md` | Synthesis by research question: support, counterevidence, conclusions (empirical vs analyst inference), unknowns, and transfer limits, with evidence IDs |
| `disputes_and_followups.md` | Eight proposition-level disputes (Reviewer A vs B, evidence on each side), Round 3 follow-ups, statuses, audit corrections, other agent disagreements |
| `revision_candidates.json` | 12 proposed ledger revisions (REV001–REV012); anchors CL025, CL026, CL027, CL029, CL007, K001, AS03, AS06 plus 4 new candidates; no convictions |
| `sources.json` / `evidence.json` | Structured registers with provenance, access status, locators, excerpts, limitations, transferability, analyst inference |
| `run_log.md` | Agent assignments, decisions (D01–D17), rounds, deviations, stopping reason, gaps, validation, storage status |
| `validation_results.md` | Automated validation output; list of sources not reviewed in full text |
| `workstreams/` | Round 1 reports (WS1–WS8), Round 2 reviews (A, B, audit), Round 3 follow-ups (R3A–R3F), each with its own registers and search logs |
| `supporting/` | ID mapping (temp → stable), digest by proposition, source index, register stats, worker brief, Drive manifest, scripts, and the overrides file recording every coordinator correction |

## Google Drive archive
Private folder (owner-only; permissions checked):
https://drive.google.com/drive/folders/1gJHmEIQfNAmcN1udfHZnXnYvQ9EKEeQk

Upload status and per-file links: `supporting/drive_manifest.json` and `run_log.md` (Storage section).
