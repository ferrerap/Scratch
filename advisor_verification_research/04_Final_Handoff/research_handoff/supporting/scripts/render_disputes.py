#!/usr/bin/env python3
"""Render 04_Final_Handoff/disputes_and_followups.md from the dispute register and the R2C audit findings.
Usage: python3 -I scripts/render_disputes.py <project_root>"""
import json, sys, os
R = sys.argv[1] if len(sys.argv) > 1 else "."
D = json.load(open(os.path.join(R, "03_Challenge_and_Followup/dispute_register.json"), encoding="utf-8"))
A = json.load(open(os.path.join(R, "03_Challenge_and_Followup/R2C_audit_findings.json"), encoding="utf-8"))
L = []
w = L.append
w("# Disputes and follow-ups\n")
w("This file records proposition-level disagreements between the Round 2 reviewers, the evidence on each side, the Round 3 follow-up searches, and why each dispute was resolved or remains open. It does not take a majority vote: agent agreement is not corroboration, and disagreements are preserved.\n")
w("**How disputes were generated.** Reviewer A (strongest defensible case *for* the thesis) and Reviewer B (strongest defensible *alternative*) worked independently on the same frozen Round 1 bundle (217 evidence items). Their 19 proposition-level positions were compared mechanically (`workstreams/round2_adversarial_review/round2_comparison.md`), and disagreements became DIS001–DIS008. Reviewer C audited the register; its corrections are listed below. Round 3 questions were phrased to find a discriminating observation, not to support a side. Full reviewer texts: `workstreams/round2_adversarial_review/R2A_case_for_thesis.md`, `R2B_alternative_case.md`, `R2C_audit.md`.\n")
w("**Status categories:** Resolved by additional evidence · Partly resolved · Dependent on context or assumptions · Unresolved with available public evidence.\n")
w("## Summary\n")
w("| ID | Question | Propositions / anchors | Status |")
w("|---|---|---|---|")
for x in D:
    w(f"| {x['dispute_id']} | {x['question']} | {', '.join(x['proposition_ids'])}{' / ' + ', '.join(x['ledger_anchors']) if x['ledger_anchors'] else ''} | **{x['status']}** |")
w("")
for x in D:
    w(f"## {x['dispute_id']} — {x['question']}\n")
    w(f"- **Propositions:** {', '.join(x['proposition_ids'])}" + (f"; **ledger anchors:** {', '.join(x['ledger_anchors'])}" if x['ledger_anchors'] else ""))
    w(f"- **Reviewer A:** {x['reviewer_A_position']}")
    w(f"  - Evidence cited by A: {', '.join(x['reviewer_A_evidence'])}")
    w(f"- **Reviewer B:** {x['reviewer_B_position']}")
    w(f"  - Evidence cited by B: {', '.join(x['reviewer_B_evidence'])}")
    w(f"- **Shared ground:** {x['shared_ground']}")
    w(f"- **Discriminating observation sought:** {x['discriminating_observation']}")
    w(f"- **Follow-up assignments:** {', '.join(x['followup_assignments'])} (see `workstreams/round3_*`)")
    w(f"- **Follow-up findings:** {x['followup_findings']}")
    w(f"- **Status:** **{x['status']}** — {x['status_rationale']}\n")

w("## Points where the reviewers agreed (recorded, not treated as corroboration)\n")
w("- **P2.5 (citations ≠ correctness) and P2.6 (rationales may be unfaithful):** both reviewers built these into their cases (EVR062, EVR094, EVR113, EVR161, EVR104, EVR105). Round 3 added that analysts' missed hallucinations were mostly computed claims (EVR236), and that an automated appraisal check failed silently (EVR322).")
w("- **P6.1 / CL007 / AS03 (commercial links):** both found no supporting evidence (EVR126, EVR129, EVR139). Round 3 (R3F) added a credit-domain case in which standardization coincided with producer fee pressure and substitution (EVR334, EVR336).")
w("- **P3.4 (ability to modify raises uptake):** rests on one lay evidence group (EVR140; EVR152 is a duplicate). It shows uptake, not appropriate use.")
w("- **P1.3 (rework from inaccurate output):** both treated discounting as rational. Detection of forecast bias came from outcome data, not from inspecting citations (EVR047 [unverified], EVR285, EVR046 [unverified]).\n")

w("## Round 2 audit (Reviewer C): issues and coordinator actions\n")
w("Reviewer C re-checked 23 consequential statistics against originals and found them accurate (`verified_ok` in `workstreams/round2_adversarial_review/R2C_audit_findings.json`). The issues below were applied as explicit overrides (`supporting/scripts/manual_overrides.json`), each tagged with its issue ID inside the corrected field.\n")
w("| Issue | Severity | Type | IDs | Coordinator action |")
w("|---|---|---|---|---|")
act = {
 "R2C-01": "Coordinator retrieved HBS WP 24-013 (MIT Sloan-hosted copy), verified inside-frontier figures, added EVR218; caveat added to EVR144",
 "R2C-02": "EVR147 marked duplicate_of EVR186; both relabelled 'qualifies'; 'Bayesian credible interval' wording",
 "R2C-03": "EVR164 marked duplicate_of EVR122; survey caveat added",
 "R2C-04": "EVR152 marked duplicate_of EVR140; P3.4 reported as one evidence group",
 "R2C-05": "EVR065 figures marked superseded by EVR114; SRC038 limitations replaced",
 "R2C-06": "EVR059 relabelled 'supports'; borrower-side wording added",
 "R2C-07": "EVR116/EVR118 relabelled 'qualifies'; inference rewritten (self-reported new tasks among users)",
 "R2C-08": "EVR141 relabelled 'qualifies'; producer-side/multi-causal caveat",
 "R2C-09": "EVR209/EVR210 relabelled 'qualifies' for P1.3; denominator note",
 "R2C-10": "EVR074 relabelled 'qualifies'",
 "R2C-11": "EVR123 relabelled 'qualifies'; per-task N added",
 "R2C-12": "EVR095 relabelled 'qualifies'; 4-system denominator noted",
 "R2C-13": "EVR091–093 population details; EVR091 relabelled 'qualifies'",
 "R2C-14": "EVR109 population/no-tests note",
 "R2C-15": "EVR010 caveat added; relabelled 'contextual'",
 "R2C-16": "Transferability caveats added to EVR039, EVR045, EVR069, EVR084, EVR086, EVR134, EVR186, EVR118",
 "R2C-17": "SRC046 access set to 'partial'; item-level access labels govern",
 "R2C-18": "EVR046/EVR047 flagged as unverified secondary figures; not used as headline numbers",
 "R2C-19": "EVR213 relabelled 'qualifies'; outcome/confounding caveat",
 "R2C-20": "Credible-interval wording in SRC054 items",
 "R2C-21": "EVR162: Finance learned of errors via media (news-only) added",
 "R2C-22": "SRC017/SRC105 confirmed distinct experiments; cross-reference added",
 "R2C-23": "P1.1 split into 'obligation exists' vs 'dominant driver' in brief and REV001",
 "R2C-24": "Digest reports distinct evidence groups; brief cites evidence-group counts",
 "R2C-25": "Brief describes standards as prescribing extra procedures, not as measuring effort; inference added to EVR003/EVR018/EVR020",
}
for f in A["findings"]:
    w(f"| {f['issue_id']} | {f['severity']} | {f['issue_type']} | {', '.join(map(str, f['ids_affected']))[:80]} | {act.get(f['issue_id'], 'see manual_overrides.json')} |")
w("")
w("## Other disagreements between agent interpretations\n")
w("- **Round 1 vs Round 3 on integration (RQ3).** WS5 concluded that integration mainly relocates work. R3D found replicated, moderate reductions in duplicated work when outside evidence is integrated at the point of use (EVR259, EVR265, EVR266). Both are retained. They concern different kinds of integration (AI drafting vs evidence import), and R3D also found offsets and a national null (EVR260, EVR268). See DIS006.")
w("- **'Lay-only' characterization of RQ2 evidence.** WS4 and WS7 reported no professional traceability study. R3A found a professional RCT with a citation-first tool (EVR228) and professional seeded-error studies without traceability (EVR219, EVR225). The characterization was narrowed to: no professional study isolates traceability with seeded errors.")
w("- **WS1's 'missing documentation causes extra work' heading** was judged an overclaim by Reviewer C (R2C-25). Standards prescribe extra procedures; effort is not observed. The brief adopts the narrower wording.")
w("- **Humlum & Vestergaard interpretation.** WS5 read the new-task shares as evidence that AI output adds review work for recipients. Reviewer C showed these are self-reports by users, including teachers policing AI use (R2C-07). The narrower reading is adopted.")
w("- **BCG field experiment.** WS6 registered only the outside-frontier arm. Reviewer C flagged selective reporting (R2C-01). The coordinator added the inside-frontier arm (EVR218).")
w("- **Fitch evidence vintage.** WS2 relied on 2012 Fitch criteria slides and a 2024 rating action read via a secondary site (unverified). R3C found a 2021 Fitch rating action applying its own haircut to IE P50/P90 (EVR297). The direction is consistent; the specific Topaz figures remain unverified.")
w("- **CL026 framing.** Reviewer A treated coverage visibility as the thesis's strongest ground; Reviewer B treated it as mostly mandates. R3E showed both partly right depending on design and timing (DIS004).\n")
w("## Follow-up searches performed (Round 3)\n")
w("| Assignment | Uncertainty | Outcome | Key unsuccessful searches |")
w("|---|---|---|---|")
w("| R3A | Professional reviewers: does traceability cut effort while preserving detection? | No study with the target design; professional bundle RCT and seeded-error drafting studies found | Auditors/lawyers/analysts with vs without source links and seeded errors: none |")
w("| R3B | Legal boundary between reliance and required investigation | Doctrine located: expert status + red flags; disclosure ≠ discharge | Model reliance-letter terms; PCAOB 2026 AS 6101 docket (blocked) |")
w("| R3C | Renewable PF: re-derivation vs review vs adaptation | Public scopes are reviews; lender work is mostly W4 driven by measured W3 bias | Solar/wind DFI or green-bank IE scopes (blocked/absent); rating methodologies (gated); lender hour splits |")
w("| R3D | Integration and duplicated work at scale | Replicated moderate reduction; offsets; national null; finance ~20% end-to-end | Commercial credit-memo/spreading studies with review time: none (vendor only) |")
w("| R3E | Do coverage lists/checklists help or narrow judgment? | Design- and timing-dependent; no test of 'checked, no findings' vs silence | Pincus 1989 (blocked); AUP/SOC user experiments: none |")
w("| R3F | Structured, standardized outside analysis in credit (appraisal) | Triage and portfolio detection enabled; review cut via liability transfer; commoditization | Lender review hours / defect rates around CU launch: not public |")
w("")
w("Stopping note: wave 3b (R3E, R3F) added material independent evidence but did not resolve the two central empirical gaps (W2 share of effort; professional seeded-error traceability study). The searches indicate these cannot be resolved from public information. See `READ_FIRST.md` for the smallest observations that would resolve them.\n")
open(os.path.join(R, "04_Final_Handoff/disputes_and_followups.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print("written", len(L), "lines")
