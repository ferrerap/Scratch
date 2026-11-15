> Provenance note (coordinator): verbatim final hand-back of Reviewer B (R2B), saved by `scripts/save_handback.py`. Subagents return narrative as text per harness convention (see run_log D08/D09).

R2B (Reviewer B, alternative case). Positions file: /home/user/Scratch/advisor_verification_research/03_Challenge_and_Followup/R2B_positions.json. It holds 19 positions, validated with json.load, and every EVR ID was checked against evidence.json. Each entry also has an extra `ledger_anchors` field. Per your correction I did not write R2B_alternative_case.json. The full narrative to save verbatim is below.

---

# R2B — Strongest defensible alternative account

**Role note.** This is an analytical role, not a verdict. "Groups" means independent `underlying_evidence_group` labels, not documents. When I say there is no evidence, that is absence of evidence, not evidence of absence. Nearly all RQ2/RQ3 evidence is analogy: lay or student participants, generic AI tools, or medicine. WS7 notes that no registered source tests real citations or provenance with professionals reviewing an advisor report.

**The rival in one sentence.** Recipient review mainly reflects non-delegable obligation (W1), criteria-driven adaptation (W4) and rational discounting of error-prone outputs (W3). Traceability aids reliably raise trust and speed but improve detection only when the producer is right or checking is cheap. Integration tends to move work rather than remove it. So the reducible W2 share may be modest, and it is in any case unmeasured.

## RQ1 — Why review persists

**P1.1 (obligation).** This is the strongest rival.
- Non-delegable responsibility is codified in at least 17 independent groups:
  - audit: EVR011, EVR016, EVR017, EVR166;
  - bank credit and model risk: EVR039, EVR041, EVR042, EVR043, EVR034, EVR035;
  - law: EVR066, EVR078, EVR079;
  - engineering and nuclear: EVR081, EVR083, EVR085;
  - environmental: EVR215;
  - mandatory pathology and imaging second opinions: EVR209–EVR211.
- In some regimes independence requires re-derivation that traceability cannot replace. UK checking bars exchanging calculation sheets (EVR081). NRC requires alternate calculations (EVR083).
- Where standards scale review effort, they scale it by risk, significance and producer competence or objectivity (EVR001, EVR012, EVR167, EVR017). How traceable the producer's evidence is does not appear among those factors.
- Supports the thesis: the same corpus allows reliance on documented work.
  - No access to proprietary models is required (EVR003).
  - Prior tool validation can justify sampling instead of full review (EVR067).
  - Directors may rely in good faith on experts (EVR051).
  - Banks may rely on third parties for analytical work (EVR039, EVR044).
  - Review can be lightweight even when mandatory (EVR089).
- Limits: these are stated obligations. No source splits recipient hours into W1 versus W2.
- Would change my view: inspectors accepting traceable advisor files as evidence of the recipient's own challenge, or time data showing hours fall with traceability while obligations stay constant.

**P1.2 (avoidable reconstruction).** A limitation, not a refutation.
- Supports the thesis: the mechanism is well attested (EVR007, EVR020, EVR040, EVR052, EVR086, EVR087, EVR115, EVR150, EVR153).
- But the size of the reducible share is not measured in any investment workflow. WS2 says W2 is "acknowledged but not measured".
- The one quantified item (EVR212: repeat imaging 72% when outside images were unavailable, 52% when available but not imported, 11% when imported) concerns data availability and integration, not opaque reasoning.
- Part of what looks like "reconstruction" may be the independent understanding that W1 requires: effective challenge (EVR035), independent checking (EVR081).
- One weak hint that some incremental effort is small: partners estimated less than 1% added audit hours after the specialist rules (EVR008). That is the incremental burden of a rule change, not total evaluation time.

**P1.3 (W3 rework).** Review looks rational.
- Solar assets ran 5–13% below P50 (EVR047; secondary news report, P50 source unknown).
- Consulting reports contained fabricated references (EVR161, EVR163).
- Outside imaging reads differed in stage in 56.4% of cases (EVR211).
- Detection came from outcome data or independent re-reads, not from inspecting the producer's citations.
- Cuts toward the thesis:
  - Pathology re-review changed management in only 1.2–1.4% of cases (EVR209, EVR210), so coverage-based triage could target review.
  - Fitch's conservative case was beaten by actual output (EVR046).
  - KBRA is a lead only (EVR048).

**P1.4 (W4 adaptation).** A substantial rival.
- Rating agencies apply their own cases and haircuts (EVR045, EVR046).
- Multi-user reports may not fit a given user (EVR021).
- Supervisors expect overlays and customization of vendor models (EVR036).
- Preparers did not scope reports to recipients' materiality (EVR053).
- Output must be edited to organizational guidelines (EVR120).
- This W4 work persists however transparent the advisor is.
- Thesis-friendly opening (untested, per WS2): adjustable structured inputs might remove rebuild work before haircuts.

**P1.5 (W5 reformatting).** Real but thinly evidenced, and customer-specific.
- Memo templates are "practically never the same"; writing plus review takes about 2 months, an interview-based figure (EVR055).
- Other support is one job posting (EVR061) and vendor-linked board surveys (EVR132, EVR133).

**P1.6 (accountability, ritual, distrust).** Supported in a refined form: review is misdirected, not excessive.
- Review serves functions beyond finding defects:
  - defects were only 14% of code-review comments (EVR088);
  - review at Google exists mainly for education and norms (EVR090);
  - audit rituals produce "comfort" (EVR157, secondary summary);
  - most accountability produces conformity (EVR165, EVR156);
  - egocentric discounting of advice (EVR154);
  - auditors discount machine-sourced evidence (EVR191, EVR033);
  - auditors limit specialists' scope for budget or client reasons (EVR029);
  - audit teams deleted contradictory specialist content (EVR027);
  - auditors and inspectors disagree about what evidence is sufficient (EVR031).
- Adverse: the regulator-observed failure is under-challenge (EVR005, EVR171), as is DOE LPO overreliance (EVR059). One recipient said its staff should not have to check footnotes (EVR162).
- Synthesis: auditors check the details of management's numbers step by step while assumptions go unchallenged (EVR025).
- Analyst inference, untested: traceability that makes detail-checking easier could reinforce that pattern.
- EVR033 cuts both ways. A more specific memo erased the source bias, but with no ground truth, so it shows reliance, not accuracy.

## RQ2 — Cheaper verification without worse verification

**P2.1 (time).**
- Supports the thesis:
  - Provenance links cut verification time about 20% with accuracy unchanged (EVR109). The study is small, provenance was correct by construction, and no significance tests were located.
  - Easy-to-check explanations lowered overreliance (EVR186).
- Rival reading: savings partly reflect checking less.
  - Highlights cut time about 25% but lowered accuracy when the model was wrong (EVR110).
  - Reading retrieved passages took about 2.5 times longer than reading explanations, with equal accuracy (EVR091).
  - Judging attribution stayed slow for long sources (EVR106).
  - A "perfect" highlights study showed no large effect and was stopped early (EVR097).
  - Links were rarely clicked (EVR100, EVR103 at 9.77%, EVR108 at about 1%).
  - Trust correlated with less critical thinking (EVR121).
  - Users' self-reported speed-ups were unreliable (EVR142).
- Would change my view: a randomized study with credit/IC professionals and seeded errors showing faster time per finding with detection preserved on advisor-wrong trials.

**P2.2 (detection).** Preserved only conditionally.
- Aids help when checking is cheaper than solving (EVR096).
- When the producer is wrong, explanation and highlight designs lowered accuracy (EVR092, EVR093, EVR110, EVR174, EVR111).
- Explanations of a biased AI did not mitigate it (EVR107).
- The higher-evidence structured-reporting cohort found less accurate, less complete reports (EVR196).
- A checklist template reduced non-fracture misses but not fractures (EVR201).
- Average-accuracy nulls hide this right-versus-wrong asymmetry, which is exactly the case error detection is about.
- Adverse: EVR109, EVR073 (TAR precision 84.7% vs 31.7%), EVR147, EVR186, EVR028, EVR217, EVR099, EVR112.

**P2.3 (trust over detection).** The best-supported rival, with about 10 groups.
- Random citations raised trust (EVR102, EVR103).
- Perceived utility ran inverse to citation precision across systems, r = −0.96 at system level (EVR095).
- Users reported relying on links they never clicked (EVR100); in-summary links were clicked in about 1% of visits (EVR108).
- Graders rated AI-assisted incorrect answers higher (EVR145).
- Explanations raised acceptance of wrong advice (EVR173, EVR174).
- Users preferred the least protective designs (EVR178).
- Proxy evaluations mislead (EVR190).
- Structured reports were rated clearer with no outcome difference (EVR192).
- Adverse: EVR099, EVR112, EVR182 (appropriate reliance on correct AI rose; correct rejection of wrong AI did not change), EVR033.
- Transfer to accountable professionals is weak (EVR176, EVR180).

**P2.4 (coverage visibility, incl. checks without findings).** A limitation.
- Much of the evidence is mandates (EVR022, EVR060, EVR214, EVR207) or completeness of the producer's report (EVR197, EVR199, EVR200), not the recipient's appropriate reliance.
- Pre-filled "normal" statements, the closest analog to boilerplate no-findings checks, did not reduce errors. 39 of 2,012 errors were retained template text contradicting the findings (EVR202).
- The only highest-level structured-reporting study found no improvement (EVR194).
- Reported TAR recall and precision (85%/58%) diverged from metrics recomputed from the validation samples (97.4%/16.7%) (EVR077).
- The IAASB chose not to require sample-size detail when no deviations are found (EVR022).
- Supports the thesis, and this is its strongest analog: courts accepted validated TAR in place of item-by-item review (EVR069, EVR070, EVR071, EVR076). But that rested on statistical sampling plus adversarial access, and courts split on seed-set transparency (EVR072).
- Pertinent negatives were rated useful by 89% of clinicians and 92% of radiologists (EVR203), a stated preference.

**P2.5 / P2.6.** Agreed limitations.
- Citation tools are not correct by default:
  - Lexis+ AI hallucinated 17% and Westlaw 33% (EVR062);
  - misgrounding is subtler than fabrication (EVR063);
  - citation recall was 51.5% (EVR094);
  - medical source checks found many unsupported statements (EVR113);
  - court and contract incidents: EVR159, EVR161, EVR163, EVR080.
- Model rationales can be unfaithful (EVR104, EVR105, EVR098).
- Inference, untested: system-generated "what was checked" logs could be unfaithful too, so coverage logs need independent verifiability.

## RQ3 — Integration

**P3.1.** No register item measures end-to-end IC workflow; zero academic work on investment memos was found (EVR057).
- Generic AI results: about 3% of hours saved, mostly reallocated (EVR117); no productivity evidence (EVR123); task time +19% in one RCT (EVR141).
- Supports the thesis: EVR213 (11% vs 52% repeat imaging, adjusted OR 9.0; observational). Vendor claims EVR054 and EVR136 are unmeasured.

**P3.2 (relocation).** Strongly supported, about 13 groups.
- Workers shift to verification, coaching, interrogation and cleanup, and take on new tasks: EVR116, EVR118, EVR119, EVR122/EVR164, EVR125, EVR127, EVR130, EVR134, EVR141, EVR151, EVR054, EVR058, EVR101.
- After the stronger specialist rule, specialist hours did not change; their share in planning rose (EVR010).
- Adverse: quality-assurance time fell for emails and summaries (EVR125); summarising was faster and better (EVR124).

**P3.3.** Separability rests on stated preference and vendor claims (EVR056, EVR135, EVR136).
- Observed: slide and spreadsheet tasks came out worse with Copilot (EVR124).
- The RCT showed only slight speed gains (EVR179).
- Benefits concentrated on administrative tasks (EVR128).
- The memo is where judgment is expressed, and consultant-written memos were flagged as a governance concern (EVR056).

**P3.4.** Uptake rose when users could modify outputs, even trivially (EVR140, EVR152; one group, lay participants). That suggests a sense of control, not better use of evidence.

## Secondary

- **P4.1:** heterogeneity is supported. EVR021, EVR036, EVR055, EVR137; templates were built with 16 teams (EVR193); RSNA templates covered 17–49% of locally used concepts (EVR206); a template needed locally chosen findings added (EVR217).
- **P5.1:** standardization is possible within one organization (EVR204), but agreement stayed low with a standard lexicon (kappa 0.28, EVR216), adoption was uneven (EVR208), and users prefer adaptable structures (EVR205, EVR198).
- **P6.1:** no link to willingness to pay.
  - 72% satisfaction coexisted with no productivity evidence (EVR126).
  - Purchase cases are framed as break-even thresholds (EVR129).
  - Procurement weighted technical capability 40% against cost 20%, with per-project pricing (EVR050).
  - The only revealed-demand item is follow-on purchases of operational consulting (EVR139).

## Ledger anchors

- **CL025:** supported. W4 drivers (EVR021, EVR036, EVR045, EVR046, EVR053), but W1 (EVR039, EVR043) and W3 (EVR047) explain continued diligence equally well, so CL025 is not uniquely identified.
- **CL026:** qualified. Mandated and valued (EVR022, EVR023, EVR203), but boilerplate negatives (EVR202), unverifiable metrics (EVR077) and rare checking (EVR103) mean coverage must be verifiable and right-sized.
- **CL027:** supported for accountability (EVR165, EVR157, EVR029, EVR031) and opacity (EVR150, EVR153). Challenged by observed under-review (EVR005, EVR171, EVR059).
- **CL029:** supported by analogy (EVR193, EVR206, EVR217, EVR205) plus EVR055 and EVR137.
- **CL007:** no evidence. Satisfaction without productivity (EVR126) and trust inflation (EVR102) warn against treating perceived value as value.
- **K001:** adjacent pain exists (EVR132, EVR133, EVR055, EVR056), but it is vendor-sourced or stated, and concerns the recipient's own reporting.
- **AS03:** stated pain only (EVR056). Adoption evidence is generic (EVR134) or a different service (EVR139).
- **AS06:** challenged. Templates are never the same (EVR055), coverage is partial (EVR206), agreement is low (EVR216). Within-organization standardization is feasible (EVR204).

**What would most change my overall view:** a seeded-error randomized study with credit/IC professionals comparing a traceable, coverage-explicit report against a standard one. It should report time per finding, detection on advisor-wrong trials, and correct rejection, together with matched-deal end-to-end time logs.
