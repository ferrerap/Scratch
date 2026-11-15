# Research brief: advisor verification, evidence traceability, and workflow integration

Run date: 2026-11-15. Evidence register: `sources.json` (SRC###) and `evidence.json` (EVR###). Disputes: `disputes_and_followups.md` (DIS###). Proposed ledger changes: `revision_candidates.json` (REV###).

## How to read this brief

- **Kinds of evidence.** Each finding names its kind: *obligation* (standard, regulation, doctrine), *observed behaviour*, *experiment*, *self-report/stated preference*, or *vendor claim*. These are not interchangeable. A standard shows that a duty exists, not how much effort it takes.
- **Counts.** Weight of evidence is counted in **independent evidence groups** (one study or event, however many documents report it), not evidence items. Duplicates are flagged in the register (`duplicate_of`).
- **Analyst inference.** Anything not stated by a source is marked **Analyst inference** and stands apart from empirical findings.
- **Transfer.** Almost nothing here is direct evidence from renewable-energy investment committees (IC) or lenders. Most findings are analogies. Each RQ ends with transfer limits.
- **Work types.** W1 required independent judgment or governance; W2 avoidable reconstruction; W3 rework from inaccurate or incomplete output; W4 adaptation to recipient criteria; W5 reformatting and integration.
- **Explanation/evidence types.** X1 persuasive explanation; X2 faithful explanation; X3 traceability to evidence; X4 visibility of scope, checks, omissions and uncertainty; X5 actual correctness.

## Summary of conclusions

1. **Review persists mainly because the recipient's duty cannot be delegated.** Across audit, banking, law, engineering and medicine, the recipient must still decide, still evaluate the producer, still judge whether the work is sufficient, and still follow up red flags. But in most regimes the duty is to *evaluate* outside work, not to *re-perform* it (EVR001, EVR011, EVR039, EVR166, EVR240, EVR246). Independent re-derivation is deliberately required only in specific regimes (EVR017, EVR081). NRC requires independent verification but lets the licensee choose design review instead of recalculation (EVR083). How much review is required scales with risk, significance and producer competence and independence. How well the producer documents its work is not one of the scaling factors (EVR001, EVR167, EVR170).
2. **Avoidable reconstruction (W2) is a real mechanism, but its share is unmeasured.** Standards prescribe extra procedures when producer documentation is missing or restricted (EVR003, EVR004, EVR013, EVR020). Observed behaviour in medicine shows outside evidence is regenerated far less often once it is in the recipient's system (EVR212, EVR259, EVR265, EVR266). No public source splits recipient time into W1–W5, in any domain. In renewable project finance, the lender work described publicly (one lender presentation, one rating action) consists of own-case selection, haircuts and sizing rules (W4). Parallel assessments are listed among the lender's tools but not quantified (EVR275–EVR277, EVR297). The lender justifies this by forecast bias seen in its own portfolio data (EVR276), and independent back-tests measure such bias in wind (EVR285). That W4 adaptation is a response to W3 bias is analyst inference.
3. **Traceability (X3) protects error detection better than persuasive explanation (X1), but it is not correctness and does not reliably save time.** Citations are often wrong or unsupported (EVR062, EVR094, EVR113), and citation checks miss computed claims (EVR236). They raise trust even when irrelevant (EVR102) but are rarely checked: 9.77% of cited answers were checked, and when random citations were checked the trust boost disappeared (EVR103). Links in AI summaries were clicked in about 1% of visits (EVR108). Precise claim-level linking saved ~20–25% of time in two lay studies. In one, detection held (EVR109); in the other, detection of wrong answers fell (EVR110). No published study gives accountable professionals output with versus without source links and measures both effort and detection of seeded errors (R3A search log; EVR228 is the closest).
4. **Coverage visibility (X4) improves the completeness of reports and is how professional systems allocate reliance. Evidence that it improves recipients' decisions is thin, and its effect depends on design and timing.** Assurance standards require test-and-result descriptions so recipients can rely (EVR019, EVR022, EVR250). Courts accept validated coverage evidence in place of item-by-item review in e-discovery (EVR069, EVR071, EVR073). But procedure lists do not move the recipient's legal duty (EVR245, EVR249). Sophisticated recipients reportedly want an accountable conclusion as well as a list of checks (EVR252). Generic checklists or decomposition used as the method of review were associated with lower fraud-risk assessments on known-fraud cases (EVR298, EVR303), and with poorer abnormality detection in a cross-study comparison (EVR309). All three are abstract-only and give direction without effect sizes. Helpful designs were specific documentation (EVR300), a checklist used to verify one's own reading after a first pass (15 ECG experts; EVR313), and prompts toward how assumptions were derived (EVR304); these are also abstract-level evidence. No study tests "checked, no findings" against silence on recipients' detection.
5. **Integration reduces duplicated work when outside evidence lands inside the recipient's working system. The effect is moderate, it relocates some work, and it can reduce scrutiny.** Medical image and record sharing is consistently associated with less repeat imaging: pooled standardized effect −0.17 (EVR259), benefit in all causally designed studies in one review (EVR263), and 16–67% relative reductions in two abstract-only observational studies (EVR265, EVR266). There are offsets and a national null result (EVR260, EVR264, EVR268). Consumer-mortgage process integration is associated with ~20% faster end-to-end processing and no default penalty (EVR270). AI drafting tends to shift effort toward verification, mostly by self-report and author interpretation (EVR119, EVR122, EVR229). One measured case shows a rise in physicians' read time but no change in reply time (EVR237, abstract-only). Recipients scrutinize inherited analysis less (EVR223, EVR219; EVR272, press-release figures).
6. **The commercial extensions are not supported by public evidence.** No source links reduced verification effort to willingness to pay, renewal, pricing or supplier margins (EVR126, EVR129, EVR139). Customer-specific adaptation is pervasive (EVR055, EVR137, EVR206).

---

## RQ1 — Why does review persist?

### Strongest supporting evidence (for the thesis that part of review is avoidable)

- **Standards link missing documentation to extra procedures (obligation).**
  - ISA 402 directs extra user-auditor procedures when a service-organization report lacks test descriptions (EVR020).
  - The PCAOB treats a model description as a substitute for model access or building an alternative model (EVR003).
  - Reviewing a producer's documented data tests may replace re-testing (EVR013).
  - Disclaimers or restrictions "ordinarily" require extra procedures (EVR004).
  - These are prescriptions, not measured effort (audit finding R2C-25).
- **Re-performance is legally not required absent red flags (doctrine).**
  - WorldCom: underwriters "are not being asked to duplicate the work of auditors"; a reasonable investigation lies between collecting comfort letters and re-auditing (EVR246).
  - BarChris: defendants could rely on audited figures without re-checking, but had to investigate non-expert content (EVR240).
  - Under OCC §939A guidance, banks may hand "much of the analytical work" to third parties but not the decision (EVR039).
- **Observed behaviour: inaccessible evidence gets regenerated.**
  - Repeat imaging was 72% when outside images were unavailable, 52% when on CD, and 11% when imported into the local system (single site, observational; EVR212).
  - Replications are moderate: 44–67% relative reductions across 37 vs 410 EDs (EVR265); 16–29% at a second centre (EVR266); pooled ES −0.17 (EVR259).
- **Mechanism evidence that missing rationale raises review cost.**
  - Understanding a change was the main code-review challenge; 91% said unfamiliar files take longer (EVR087).
  - Opaque AI output was ignored in 2 of 3 radiology departments (EVR150).
  - A proposed cause of advice discounting is that judges cannot see the advisor's reasons (EVR153, untested mechanism).
  - Fact-checkers say opacity makes tools unusable (stated; EVR115).

### Strongest counterevidence and competing explanations

- **W1 is non-delegable and would persist under full transparency (obligation; 35 distinct evidence groups labelled "supports" for P1.1 in the final register, mostly standards, regulation and doctrine. These show that an obligation exists, not that it is the dominant driver of effort).**
  - Audit: EVR011, EVR016, EVR017, EVR166.
  - Banking: EVR034, EVR035, EVR041, EVR042.
  - EU lending: EVR043.
  - Law: EVR066, EVR078, EVR079.
  - Engineering: EVR083, EVR085.
  - Environmental: EVR215.
  - Securities offerings: EVR238, EVR241, EVR244.
  - Directors: EVR254, EVR256.
  - Some regimes *require* independent verification or re-derivation and cut off access to the producer's working on purpose: the UK CG 300 Category 3 check is done "without exchange of calculation sheets" (EVR081); NRC requires design verification by people other than the designer, through design review, alternate calculations or testing, at the licensee's choice (EVR083); ISA 610 requires re-performance of some internal-audit work (EVR017).
- **Duties traceability cannot discharge** (doctrine):
  - judging whether procedures are sufficient (EVR249);
  - following up red flags, including from public peer benchmarks (EVR244);
  - building a defensible record of the recipient's own investigation, "even if ... futile" (EVR247, EVR251);
  - vetting the producer's competence, independence and selection (EVR254, EVR170, EVR015). DOE's Inspector General found the Loan Programs Office could identify which engineering advisors also worked for prospective borrowers on only 3 of 18 projects, a conflict-of-interest blind spot (EVR059).
- **Rational discounting of inaccurate output (W3) is well documented in the target domain.**
  - Wind pre-construction yield assessments over-predicted P50 by 6.6–7.4% across 115 assessments, with prediction-error SD of 11.4–13.1% vs stated uncertainty of ~7.5% and no difference between consultants (EVR285).
  - Seven assessors given identical PV inputs produced initial yield assessments with an SD of 9.7% at one site and 3.9% at the other (EVR296; summary-level access); see also EVR286 and EVR287.
  - One lender (Wells Fargo) says IE results "in isolation are generally inadequate". Its stated reasons are bias, uncertainty bands that are too tight, and omitted factors (EVR275, EVR276). Opacity is not among the reasons given (analyst inference).
  - Solar underperformance figures (EVR047) are unverified secondary numbers (R2C-18).
  - AI-assisted outputs add their own error risk: BCG outside-frontier task 84.5% vs 60–70% correct (EVR144); fabricated references in two consultant reports to governments (EVR161, EVR163); ambient-scribe omissions (EVR232).
- **Adaptation to recipient criteria (W4) persists however transparent the producer is.**
  - Rating agencies apply their own P-cases and haircuts to IE forecasts rather than re-running them (EVR045, EVR297; EVR046 unverified).
  - One lender says its sizing rules are "largely established prior to detailed diligence" (EVR277).
  - Model risk guidance expects overlays on vendor models (EVR036).
  - Multi-user reports must be fitted to each user (EVR021, EVR053).
- **Review is often thinner, not thicker, than required (observed by regulators).**
  - Inspectors found under-evaluation of specialists, including ignoring the specialist's own flagged issues (EVR005, EVR171).
  - Interview studies, known only from abstracts, summaries and PCAOB quotations, report that auditors seek "comfort, not insight" from specialists, limit specialist scope for budget reasons, and delete contrary content (EVR026, EVR027, EVR029).
  - This competes with the idea that recipients over-review because of opacity (DIS005).
- **The incremental effort of tighter review rules was small** (self-reported): most of 31 audit partners put the added time from the new specialist requirements below 1% of audit hours (EVR008). The planning-phase shift is not attributable to the rule (EVR010).
- **Where recipient review visibly fell in credit, the mechanism was risk transfer, not cheaper verification (appraisal case).**
  - Lenders must review each appraisal's methods, assumptions and data, and cannot shift responsibility to third-party reviewers. Automated or sampled review is allowed only for lower-risk, homogeneous residential loans (EVR324, EVR325).
  - The observable reduction in lender review came when the government-sponsored enterprises (GSEs) offered representation-and-warranty relief for low automated risk scores, and appraisal waivers. In both cases the consequence-bearer took the risk (EVR329, EVR326).

### What can reasonably be concluded

- *Empirical:* recipient review rests on a non-delegable core (deciding, vetting the producer, judging sufficiency, following up red flags, building a record) that is well established as an obligation across domains (EVR011, EVR039, EVR166, EVR244, EVR247, EVR249, EVR254). In most regimes that core does not require re-performance (EVR240, EVR246).
- *Empirical:* where documentation is missing, standards prescribe more work (EVR003, EVR020). Where evidence is inaccessible, professionals regenerate it (medicine, observed; EVR212, EVR265).
- *Analyst inference:* the reducible part of review is the gap between "evaluate the producer's work" and "re-derive it in order to evaluate it". That gap is largest when the recipient cannot see inputs, assumptions and checks. It is smallest where regimes mandate independent re-derivation (basis: EVR246, EVR020, EVR081).
- *Stated practice, target domain (one lender presentation, one rating action):* the lender work described publicly consists of own-case selection, haircuts and sizing rules (W4). Parallel assessments are listed among the tools but not quantified (EVR275–EVR277, EVR297). The lender justifies this by forecast bias seen in its own portfolio data (EVR276), and independent back-tests also measure such bias in wind (EVR285). *Analyst inference:* W4 adaptation is a response to W3 bias.
- *Analyst inference:* a traceable advisor report would not remove those haircuts. Back-testing evidence would bear on them more directly than clearer reports (basis: EVR275, EVR276, EVR285).
- *Not established:* the share of recipient time that is W2. P1.1 should be split: "an obligation exists" is well supported; "obligation is the dominant driver of effort" is untested (R2C-23; REV001).

### What remains unknown

- How recipient hours split across W1–W5 in any advisor–client setting (DIS001). No public time-use data were found (WS1, WS2, WS3, WS5 and R3C search logs).
- What triggers lenders' parallel energy-yield assessments: unclear reports, disagreement between consultants, or policy (R3C).
- Whether lenders' and ICs' credit policies distinguish expert-certified content (for example, an IE report with a reliance letter) from sponsor content the way Securities Act §11 does (EVR238, EVR293; R3B).

### Limits of transfer to renewable-energy investment workflows

- **Audit** has a closely matching producer → accountable recipient → opinion structure. But its duties are statutory and inspected, so W1 there is probably an upper bound for IC and lender practice, which is governed by credit policy, fiduciary duty and contract (EVR039, EVR043, EVR293).
- **Securities-law doctrine** (§11, WorldCom) does not apply to private lenders or ICs (EVR238, EVR244). The expertised/non-expertised logic is an analogy whose applicability needs checking against actual credit policies.
- **Medicine's "duplicate tests"** are discrete and countable; IC reconstruction is analytic and partly required.
- **Target-domain evidence** comes from one lender presentation, one DFI terms of reference (biogas), one securitization report, IFC guidance, rating actions, and back-tests (EVR275–EVR297). It is too thin to generalize across US tax-equity, construction-debt and M&A diligence.

---

## RQ2 — What makes verification less costly without making it worse?

### Strongest supporting evidence

- **Checkable evidence beats persuasive narrative when the producer is wrong (experiments, lay participants).**
  - With wrong AI explanations, accuracy was 0.54 with retrieved sources, 0.49 with no aid, and 0.35 with the narrative explanation (EVR092).
  - Explanations reduce overreliance only when checking them is much cheaper than solving the task (EVR186, EVR096, EVR188).
- **Fine-grained provenance can save time.**
  - Linking each number to its source cell cut decision time from 2.50 to 1.98 minutes with accuracy unchanged (80.8% vs 80.0%) (EVR109; n=60 crowdworkers, no significance tests, provenance correct by construction).
  - In a clinician crossover RCT (20 clinicians, 200 cases), a tool that cites a source record for every claim cut completion time (ratio 0.624, 95% CI 0.565–0.689) and workload, and was non-inferior on accuracy vs searching the EHR alone (EVR228). Because the comparator had no AI, the citations' own contribution cannot be separated.
  - Analysts strongly preferred cell-level over paragraph-level citations (self-report, developer-run; EVR235).
- **Coverage and uncertainty visibility (X4) can improve appropriate reliance.**
  - First-person LLM uncertainty expressions raised lay participants' accuracy from 63.9% to 72.8%, close to the 74.2% without AI. General uncertainty phrasing had no significant effect (EVR099).
  - Uncertainty highlighting raised correct responses from 26% to 58% (EVR112).
  - Synoptic checklists were associated with higher report completeness in 13 of 14 observational pathology studies (EVR197). Institutions using checklists had complete reports 88% vs 34% of the time (EVR199, correlational).
  - After a mandatory checklist template was introduced, residents' misses of non-fracture emergent findings fell from 28.3% to 9.3% (pre/post, single program). Overall emergent misses did not change significantly, and fracture misses did not improve (EVR201).
- **Process and coverage validation substitutes for item-by-item review under specific conditions (court practice).**
  - Courts accepted technology-assisted review with disclosed protocols, sampling of excluded documents, recall thresholds and adversarial challenge (EVR069, EVR071, EVR075, EVR076).
  - Best-practice TAR reviewed 1.9% of documents with precision 84.7% vs 31.7% for manual review and recall 76.7% vs 59.3% (not significant) (EVR073).
  - Disclosed validation samples let the receiving party show that reported recall/precision of 85%/58% were really 97.4%/16.7% (EVR077).
- **Producers are required to make scope legible.** AS 6101 bans vague procedure terms ("general review", "check", "test") in comfort letters unless the procedures are described, and lets the recipient ask for more (EVR250). Phase I environmental reports must identify data gaps (EVR214). ABS issuers must disclose due-diligence criteria (EVR060).

### Strongest counterevidence and competing explanations

- **Traceability is not correctness (X3 ≠ X5).**
  - 51.5% of generative-search statements were fully supported by their citations; citation precision was 74.5% (EVR094).
  - Source-citing legal research tools hallucinated on 17–33% of 202 queries (EVR062). Misgrounded citations need the source read to catch (EVR063).
  - 50–90% of medical LLM answers were not fully supported (EVR113).
  - Most hallucinations analysts flagged after a citation tool missed them were computed claims; a "supported" label means only that the claim matches its source (EVR236).
  - Fabricated references passed client review in two consultant reports to governments (EVR161, EVR163).
- **Citations and explanations raise trust and acceptance without improving detection (P2.3; 8 distinct evidence groups labelled "supports", mostly lay experiments).**
  - Random citations raised trust (EVR102). 9.77% of cited answers were checked, and checked random citations earned no extra trust (EVR103). A link inside Google's AI summary was clicked in about 1% of visits to pages showing one (EVR108).
  - Explanations raised acceptance whether the AI was right or wrong (EVR146, EVR173, EVR174).
  - The most protective designs were the least liked (EVR177, EVR178).
  - 90% of physicians trusted a drafting tool while most missed its errors (EVR219, EVR220).
- **Time savings can come from checking less.**
  - Highlighting the facts behind a model's reasoning cut time by ~25% but dropped detection of wrong answers from 72.2% to 54.8% (EVR110).
  - Residents edited LLM drafts less (31.5% vs 44.8% of characters) and left more confabulations (EVR223).
  - Auditors who inherited a data-analytic test followed up a red flag 26% of the time vs 54% for those who built it (press-release figures; EVR272).
  - Reading retrieved sources took ~2.5x longer than reading explanations, at equal accuracy (EVR091; retrieval vs explanation, not vs no aid).
- **Professionals are not protected by expertise.**
  - Heatmap explanations did not help clinicians detect a systematically biased model (EVR107).
  - Experienced radiologists were correct 82% of the time with correct suggestions vs 45.5% with incorrect ones (press release; EVR189).
  - Erroneous decision support raised error risk (RR 1.26; EVR183).
  - Auditors discounted identical evidence attributed to AI (EVR191). Professionals show both automation bias and algorithm aversion (DIS008).
- **Coverage disclosure has limits.**
  - Comfort letters with procedures and findings are "important evidence, but ... insufficient by itself" (EVR245).
  - Only the recipient can judge sufficiency (EVR249).
  - Banks reportedly will not proceed on findings without negative assurance (practitioner claim; EVR252).
  - Users may misread assurance language (EVR253).
  - A written program is not proof the steps were performed (EVR243).
  - The only top-level structured-reporting study found worse completeness and accuracy (EVR196, EVR194). Prefilled "normal" text produced contradictions without benefit (EVR202).
  - Structured reports were rated clearer with no difference in decision usefulness (EVR192).
  - Omissions were the most common error in ambient scribes, and links from statements cannot reveal them (EVR232).
- **Explicit lists can narrow attention (experiments with professionals, mostly abstract-level access).**
  - 69 auditors given a standard fraud-risk checklist assessed lower fraud risk on a known-fraud case. A standard audit program produced a less effective fraud plan than an expert benchmark (EVR298, EVR299).
  - The decomposition recommended in auditing standards made 101 experienced auditors less concerned about high-risk schemes (EVR303).
  - A checklist imposed during reading was associated with lower radiologist detection accuracy than an earlier study using the same images (cross-study comparison, abstract-only; EVR309). A salient finding still suppressed reporting of other abnormalities (EVR310).
  - Highlighted audit matters drew readers' attention away from the rest of the statements (students; attention, not detection) (EVR305).
  - Readers of computer-aided detection over-trusted unflagged areas (EVR314).
  - Training for complete coverage did not increase findings (EVR312). Coverage (X4) is not correctness (X5).
- **Machine-checkable structure raises detection capacity but does not by itself produce verification (appraisal case).**
  - The GSEs bought >85,000 loans in 2013 despite automated portal warnings. Flags were set to auto-override because false-positive rates were unmeasured and they did not want to burden lenders (EVR320, EVR321).
  - A logic error left ~$88B of loans without a working appraiser-licence check (EVR322).
  - Cross-report attribute inconsistencies persisted under the standardized format and were detectable only with pooled data (EVR331).
- **Disclosure incentives can produce boilerplate.** Disclosing any matter, even an unrelated one, reduced mock jurors' assessment of auditor liability. Disclosing uncertainty lowered the auditor's perceived responsibility for a later misstatement (EVR307, EVR308).
- **Generated rationales can be unfaithful (X1 ≠ X2).** Models' reasoning traces mentioned hints they used in only 25–39% of cases (EVR105). Biasing features drove answers without being mentioned (EVR104). A system-generated "what was checked" log could share this weakness (Analyst inference; DIS004).

### What can reasonably be concluded

- *Empirical (lay experiments, several groups):* checkable evidence (X3/X4) protects detection better than narrative explanation (X1) when the producer is wrong, but costs reading time unless it is fine-grained and correct (EVR092, EVR186, EVR091, EVR109).
- *Empirical (one lay study each):* claim-level provenance can cut time with detection preserved when the error sits in the linked fact (EVR109). When the error is in the reasoning, linking makes wrong answers look grounded and detection falls (EVR110). The distinction between error in the cited fact and error in the inference is analyst synthesis from these two studies.
- *Empirical (professional settings):* lighter review of AI drafts goes with more surviving errors (EVR223, EVR219). Field studies (one stepped-wedge RCT, one nonrandomized cohort; both abstract-only) show professional time savings without detectable quality loss on rating instruments, but did not test detection (EVR227, EVR231). In one small simulation, most physicians missed most erroneous AI drafts (EVR219). Professional baseline detection of plausible errors without traceability is poor.
- *Empirical (obligation and courts):* coverage information supports reliance when it can be independently verified (sampling, recomputation, adversarial access). It does not move the recipient's duty to judge sufficiency (EVR069, EVR071, EVR077, EVR245, EVR249).
- *Empirical (behavioural, mixed access):* coverage effects depend on design and timing.
  - Associated with lower fraud-risk assessments or poorer detection: generic lists or decomposition imposed as the review method (EVR298, EVR303, EVR309; abstract-only, direction without effect sizes).
  - Helped: specific documentation (EVR300), a checklist used to verify one's own interpretation after a first read (15 ECG experts, abstract-only; EVR313), prompts toward how assumptions were derived (EVR304), and procedure descriptions for flagged matters (EVR319, calibration rather than accuracy).
  - Changed recipients' reactions: statements that a flagged matter was examined and resolved (EVR318). Whether that reassurance was justified was not tested.
- *Analyst inference:* the thesis is best supported in a narrowed form. Claim- and calculation-level traceability, plus coverage records that can be verified, should lower the cost of evaluation that obligations already require. Coverage records should be deal-specific, show checks without findings at the level of the nature and scope of each test, state exclusions, and focus on how key assumptions were derived. The benefit is conditional on accuracy, granularity and when the record is consulted. It must be judged on detection, never on satisfaction or trust (basis: EVR109, EVR110, EVR300, EVR313, EVR304, EVR102).

### What remains unknown

- Whether source links *themselves* reduce professional review time and preserve detection of seeded factual, reasoning, omission and calculation errors. No such professional study was found after targeted searches (R3A search log); see DIS003.
- Whether disclosing "checks with no findings" changes what recipients re-check, or improves detection of omissions, compared with silence or "not checked" (DIS004). No experiment found (R3E search log). Nor whether a material issue planted outside the listed coverage is detected less often (narrowing) or more often (declared gaps cue attention).
- Whether recipients use traceability to check claims or to bolster positions already held (DIS005).

### Limits of transfer to renewable-energy investment workflows

- **Participants and tasks.** Most RQ2 experiments use crowdworkers or students on short tasks with one planted error (EVR176, EVR180). IC reviewers are senior, accountable, time-pressed and work on long multi-document reports.
- **Where errors sit.** Diligence errors often sit in derived metrics (DSCR, P50/P90, degradation-adjusted cash flows). Citing the inputs does not verify a calculation (EVR236). Traceability would need to reach calculations and assumptions.
- **Court acceptance of coverage validation** rests on high-volume statistical sampling and an adversary (EVR071, EVR076). Diligence is low-volume and bespoke, with no adversary.
- **Medicine's structured reporting** is enforced by accreditation and is high-volume. Diligence has no mandatory reporting standard. PV yield uncertainty reporting lacks a standardized framework (EVR294).

---

## RQ3 — Does workflow integration add distinct value?

### Strongest supporting evidence

- **Integration into the recipient's working system reduces duplicated work (observed behaviour, replicated).**
  - Meta-analysis of image sharing and repeat imaging: pooled ES −0.17 (95% CI −0.25 to −0.09); −0.27 in the most rigorous studies (EVR259).
  - Repeat CT fell by 8.7 percentage points (95% CI −14.7 to −2.7) in EDs that adopted health information exchange (EVR265).
  - Importing outside images led to 16–29% fewer repeat CTs (EVR266).
  - All 7 causally designed studies in a 2018 review reported some benefit (EVR263).
  - Availability alone is not enough. CD vs import was 52% vs 11% (EVR212).
- **Finance analog.** Electronic third-party verification plus automated underwriting is associated with ~10 days (~20%) faster end-to-end mortgage processing and ~25% lower FHA default rates. This is a lender-type comparison, not an intervention (EVR270). Gains were capped by steps that are not automated, such as appraisal (EVR271).
- **Drafting and summarising benefit; separation from judgment is plausible for assembly.**
  - Summarising took 12:37 vs 41:34 and was more accurate in the UK government evaluation. But slides were far less accurate, and Excel analysis was slower and worse (EVR124).
  - Treasury's gains were in administrative tasks (EVR128).
  - Memo-survey respondents want memo fields filled automatically (stated; EVR056).
  - An IC decision stays human while preparation shrinks (buyer account; EVR135).
- **Control raises uptake.** Letting people modify an algorithm's output, even trivially, raised use from 32% to 73–76% (one lay evidence group; EVR140).

### Strongest counterevidence and competing explanations

- **AI assistance relocates effort into review.**
  - Knowledge workers report effort shifting to verification and integration (EVR119).
  - Workslop survey (self-report, vendor-affiliated; EVR122).
  - QA time rose for slide decks and code review (EVR125).
  - Checking was sometimes slower than doing the work manually (EVR127).
  - In the radiology department that integrated AI, radiologists were observed investing additional time (qualitative; EVR151).
  - Physicians' read time rose 21.8% with integrated draft replies (EVR237).
  - The Scout authors describe the shift as "from manual curation to verification" (EVR229).
  - Danish users report new oversight tasks (self-report, qualifies; EVR116, EVR118).
- **Task speed-ups do not reduce total hours.**
  - Danish register data rule out effects on hours above 2% (EVR117).
  - The UK Department for Business and Trade (DBT) evaluation found no evidence of productivity improvement. Self-reported per-task savings shrank, and turned negative for some tasks, once unused outputs and novel tasks were accounted for (EVR123, qualifies).
  - Experienced developers took 19% longer with AI while believing they were 20% faster (EVR141, EVR142).
- **Integration effects are moderate and conditional.**
  - Image sharing increased total imaging (ES +0.20; EVR260).
  - Exchanges were used in fewer than 10% of encounters (EVR264).
  - A 2018 national Medicare study found no reduction in repeat imaging from network membership alone (OR 1.06; EVR268).
  - The largest effect relied on hired liaisons whose labour was not netted out (EVR267).
  - In commercial credit spreading, a 70% task-level gain shrank to 21% end to end, and analysts still validate the spreads (vendor; EVR274).
  - No study measured the review time integration adds for the receiving professional (EVR261).
- **Integration can transfer judgment and reduce scrutiny.**
  - Physicians' replies adopted the draft's clinical content (agreement between physicians rose from kappa 0.10 to 0.52; EVR222). This challenges the idea that drafting is separable from judgment.
  - Auditors who inherit analysis show less skepticism; a development memo only partly restores it (26% → 34% vs 54%; press-release figures, significance not verified; EVR272, EVR273).
  - Memos written by external consultants were flagged as a governance concern (EVR056).
- **Governance policies state that reviewer diligence is held constant.** Audit firms told PCAOB staff they apply "the same level of diligence" to GenAI-assisted work (stated policy; EVR130). A&O kept lawyer review after a firm-wide rollout (EVR134).
- **Automated checks can push rework back to the producer.** An appraisal-management executive reported that revision requests to appraisers rose after automated collateral scoring launched (anecdotal; EVR338). Freddie Mac later barred revision requests based on the score alone (EVR328).

### What can reasonably be concluded

- *Empirical (medicine, replicated; finance, one analog):* placing outside evidence inside the recipient's own working system at the point of use reduces regeneration of that evidence, by moderate amounts (EVR259, EVR265, EVR266, EVR270). Mere availability or a separate portal often does not (EVR212, EVR264, EVR268).
- *Empirical (several groups, mostly generic AI tools):* assistance that produces drafts for the recipient tends to move effort into verification. Net time effects range from negative to modest positive, and self-reported savings are unreliable (EVR119, EVR122, EVR237, EVR117, EVR123, EVR142).
- *Empirical (two professional studies):* integration of others' analysis can import their judgments and reduce skepticism.
- *Analyst inference:* integration value for an advisor product is most defensible for W5 (reformatting and assembly) and for W2 caused by inaccessible inputs. It is least defensible for substantive memo content, where it risks anchoring the IC on the advisor's judgment. Integration and traceability need to come together: integration without visible provenance risks the inherited-analysis effect (EVR272).
- *Not established:* any end-to-end reduction in IC, credit or board workflow time. No academic study of investment memos exists (EVR057). Memo templates differ by firm, and writing plus review averages ~2 months (interview-based; EVR055).

### What remains unknown

- End-to-end time from advisor report to IC approval, with and without integration, including follow-up questions and errors caught (DIS006).
- Whether delivery into the client's memo or model template by the supplier differs from the client importing material itself (R3D).
- How much time preparing and reformatting board or IC materials takes. Never quantified; only vendor-linked surveys exist (EVR132, EVR133).

### Limits of transfer to renewable-energy investment workflows

- Health-information-exchange "duplicates" are discrete orders; IC "reconstruction" is analytic and partly required (W1).
- The mortgage analog is high-volume and standardized. Project-finance diligence is low-volume and heterogeneous, and quality outcomes (underperformance, default) are slow and rare, so "no quality loss" is hard to show (EVR270, EVR271).
- Most RQ3 evidence concerns generic AI assistants rather than outside advisors' deliverables.

---

## Secondary questions (only where the core research produced a credible connection)

- **RQ4 — customer-specific implementation.**
  - Heterogeneity is well evidenced:
    - memo templates are "practically never the same" across investors (EVR055);
    - a utility RFP requires native PVsyst files to its own specification (EVR137);
    - board materials follow organization-specific templates (EVR133);
    - national radiology templates covered only 17–49% of one centre's report content (EVR206);
    - templates needed locally added items (EVR217, EVR193);
    - multi-user assurance reports must be fitted to each user (EVR021).
  - *Analyst inference:* deployment needs domain-aware configuration of criteria, templates and data formats, not just a checklist upload.
- **RQ5 — repeatability.**
  - One department built 228 templates covering 94% of volume, with high adherence after all users vetted them (EVR204).
  - The College of American Pathologists (CAP) requires the core elements but lets labs reorder and add items (EVR207).
  - Synoptic adoption in one national system was 77% for resections vs 19% for biopsies (abstract-only; EVR208). That this tracks where accreditation requires it is analyst inference.
  - A shared lexicon still gave only fair agreement on the final judgment (kappa 0.28; EVR216).
  - In PV and wind yield assessment, calls for standardized uncertainty reporting come mainly from suppliers (EVR279, EVR288, EVR294).
  - Credit-domain case (US appraisal):
    - The standardized data format plus automated scoring made routine appraisals repeatable enough to be intermediated, with fee clustering and appraisers raising workloads (EVR336, EVR335), and partly replaced by waivers (EVR326, EVR327).
    - Complex, dissimilar or data-thin properties, and local knowledge, still require bespoke work (EVR327, EVR333, EVR325).
    - The standard itself had to be redesigned to absorb diversity (EVR339).
    - Lender-specific acceptance rules limit report portability (EVR341; practitioner).
  - *Analyst inference:* the core content of a deliverable can be standardized, with local additions on top. Judgment stays variable. Low-volume, heterogeneous renewable diligence resembles the complex-commercial tier more than the homogeneous residential tier.
- **RQ6 — buying, renewal, pricing, supplier economics.**
  - No evidence links reduced verification effort to purchase or price.
  - 72% satisfaction coexisted with no productivity evidence (EVR126).
  - A purchase was justified on a ~13-minutes-a-week break-even (EVR129).
  - Firms in a consulting RCT bought more consulting later, but for operational gains (EVR139).
  - One RFP weighted technical capability at 40% vs cost at 20% (EVR050).
  - In the one credit-domain case where an outside deliverable became standardized and machine-checkable (appraisal), gains accrued to borrowers, lenders and the GSE through waivers and lower costs. The appraiser side saw fee pressure, intermediation and substitution (EVR334, EVR336, EVR335; interested-party and survey evidence).
  - Absence of evidence here reflects public data limits. It is not evidence of absence.

---

## Cross-domain transfer summary

| Mechanism | Source domain(s) | Similarities to target | Consequential differences | What needs verification in renewable-energy IC/credit |
|---|---|---|---|---|
| Non-delegable recipient duty; evaluate rather than re-perform | Audit, banking supervision, securities law, directors' duties | Producer → accountable recipient → decision; reliance letters; independence concerns | Audit and §11 are statutory and inspected. IC duties come from policy, fiduciary duty and contract | Credit policies: what must be independently re-derived vs reviewed; treatment of IE reports with reliance letters |
| Inaccessible evidence gets regenerated; integration reduces it | Medicine (health information exchange, image import) | Outside evidence used at decision time | Discrete, countable tests vs analytic reconstruction | Whether IC teams re-pull or re-key advisor data when delivered as PDF vs inside their model or memo |
| Checkable evidence protects detection better than narrative | Lab human–AI experiments | Plausible-but-wrong outputs | Lay participants, short tasks, one planted error | Professional seeded-error study with long reports and calculation errors |
| Coverage validation can replace item-by-item review | E-discovery (TAR) | Coverage disclosure; sampling | High volume, statistical recall, an adversary | Whether lenders accept coverage maps plus sampling instead of re-review |
| Structured reporting raises completeness; rigid or prefilled templates backfire | Pathology and radiology | Producer report to decision-maker | Accreditation enforcement; high volume; narrow tasks | Follow-up question counts and omission detection with vs without coverage maps |
| Rational discounting of forecasts | Wind/PV yield back-tests; rating actions | Same domain | Mostly wind; solar evidence partly unverified | Lender haircuts by IE provider track record |
| Inherited analysis lowers scrutiny | Audit experiment; clinician drafting | Recipient adopts another's analysis | Hypothetical cases; press-release figures | Replication with investment analysts, with provenance and checks-performed documentation |
| Generic lists narrow attention; specific or after-read coverage helps | Audit fraud experiments; radiology; ECG | Reviewer receives structured scope | Mostly abstract-level access; detection in single cases | Coverage table before vs after an independent read; planted issue inside vs outside listed scope |
| Machine-checkable standardization enables triage; review falls via risk transfer | US appraisal (UAD, Collateral Underwriter, waivers) | Producer → accountable lender → consequence-bearer | Dominant consequence-bearer, millions of homogeneous units, central repository | Whether any lender or investor reduces review for structured, traceable reports *without* liability relief |

## Evidence base

- **Totals:** see `READ_FIRST.md` for final counts of sources, evidence items, independent evidence groups and access status. Every substantive claim above cites EVR IDs that resolve to `evidence.json` with source locators. Abstract-only and summary-only sources are listed in `validation_results.md`.
- **Corrections:** the Round-2 audit verified 23 consequential statistics against originals and led to recorded corrections (relabels, duplicate flags, an added missing study arm). See `disputes_and_followups.md` and `supporting/scripts/manual_overrides.json`.
