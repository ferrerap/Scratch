> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from R3D's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

R3D finished: 11 sources and 16 evidence items, all in new evidence groups and nothing re-collected from the register. Both JSON files pass json.load. They are in /home/user/Scratch/advisor_verification_research/03_Challenge_and_Followup/R3D_integration_duplicate_work/ (sources.json, evidence.json).

Answer to the RQ3 question: putting outside evidence into the recipient's own system does reduce duplicated work, and this holds beyond one site. The effect is moderate and uneven, though, and Lu 2012 looks like an upper bound.
- Multi-site and pooled results: 16–67% relative reductions in repeat tests (R3D-E01, E05, E07, E08).
- Offsets: total imaging volume does not fall (E02). A 2018 national Medicare study found no reduction where hospitals were only connected to an exchange (E10). Exchanges are opened in fewer than 10% of patient encounters (E06).
- No study measured how much review time the integration adds for the receiving professional (E03).
- In finance, the end-to-end gain is about 20% (E12), against much larger gains on single tasks (E16).
- In audit, auditors who inherit someone else's analysis follow up on red flags less often (E14). Less work can therefore mean less scrutiny, not just less duplication.

# report.md

## R3D — Does integrating outside evidence into the recipient's systems reduce duplicated or reconstructive work?

### 1. Findings against the uncertainty
**Short answer.** Yes, it reduces the duplicated production of the same evidence, and this is replicated across sites, states and systematic reviews. But:
- the effect is moderate (most estimates are a 16–67% relative reduction, not near-elimination);
- it depends on the evidence being integrated where and when the professional works, not merely available;
- it is partly offset by more total use (more imaging overall);
- it disappears in one national, later-period study where the exposure was only network membership.

No study measured the receiving professional's review or reconciliation effort. "Duplicated work avoided" is observed; "review work added" is unmeasured.

**Health information exchange (HIE) and image sharing: duplicated work avoided (observed utilization, mostly claims and EHR data)**
- **Vest 2015 meta-analysis** (17 articles, 42 studies). Repeat imaging fell: pooled standardized effect size −0.17 (95% CI −0.25 to −0.09); −0.27 in the 25 most rigorous studies. The authors call this "modest" (R3D-E01).
- **Lammers 2014.** 37 EDs that started HIE compared with 410 that did not, California and Florida, 2007–10. Repeat CT −8.7 percentage points (95% CI −14.7 to −2.7), ultrasound −9.1, chest x-ray −13.0. That is 44–67% relative to baseline repeat rates of 14.7–20.7% (R3D-E07).
- **Sodickson 2011.** This replicates Lu's direction at a second centre with a smaller effect. Successful vs failed CD import into the hospital's imaging system: 17% fewer exams (3.30 vs 2.74 per patient) and 16% fewer CTs within 24 hours. Against historical controls, 29% fewer CTs. Imports failed 22% of the time (R3D-E08).
- **Menachemi 2018 review.** All 7 studies with designs suitable for causal inference reported some benefit. Across all 63 analyses: 68.3% beneficial, 7.9% adverse, the rest null. Community HIEs reported benefit more often than enterprise or vendor-run exchanges (70.3% vs 54.2%, P=.04) (R3D-E05).
- **Hersh 2015 (AHRQ-funded review).** Low-quality evidence that HIE reduces duplicate testing. ED studies are consistent; ambulatory studies are mixed, including one where lab testing increased (R3D-E04).

**Offsets, conditions and relocated work**
- **More total imaging.** In the same meta-analysis, image sharing increased any imaging (ES +0.20, 95% CI 0.07–0.32) and had no net effect across all outcomes (ES 0.00) (R3D-E02).
- **Low use.** HIEs were used in fewer than 10% of patient encounters across 13 organizations, with technical and workflow barriers (R3D-E06). Availability is not integration.
- **Network presence did nothing nationally.** 2018 Medicare, 275,860 admission–readmission pairs. Readmission to a different hospital on the same exchange still had adjusted OR 1.06 (95% CI 1.00–1.13) for repeat imaging (R3D-E10). The authors suggest ordering is easier than searching, needed information may be missing, and clinicians may distrust outside interpretations; these are untested (R3D-E11).
- **Work relocated, not removed.** The largest effect (−52% lab tests, −36% radiology) came when hired liaisons ran the HIE queries and handed results to clinicians. Liaison labor was not netted out (R3D-E09).

**Finance and audit analogs**
- **Mortgage lending (Fuster et al.).** Electronic third-party data verification plus centralized, automated underwriting goes with about 10 days (~20%) faster end-to-end processing. FHA default rates were about 25% lower, so no quality loss. Human underwriters remain, and gains are capped by steps that are not automated, such as appraisal (R3D-E12, E13). This is a lender-type comparison, not an intervention.
- **Commercial credit spreading (vendor case study).** 70% faster data extraction but a 21% end-to-end improvement after integration with the bank's credit platform. Analysts still validate the spreads. Self-reported, with no baselines (R3D-E16).
- **Audit (Li, Brazel, Gold & Leiby, JAR 2026).** In an experiment with 173 practitioners, auditors who inherited a data-analytic test took skeptical follow-up on a red flag 26% of the time, vs 54% for auditors who built it. A memo describing how the test was developed raised the inherited group to 34%. These percentages come from the press release (R3D-E14, E15).

**The distinctions you asked for**
- **Duplicated work avoided vs review work added.** The avoided side is measured as test counts. The review side is unmeasured (E03), or the work moves to new staff (E09), or it is partly lost scrutiny (E14).
- **Single task vs end to end.** Large task-level gains shrink to about 20% end to end (E12, E16).
- **Observed vs self-reported.** The HIE results and Fuster are observed behavior. The audit study observes behavior in a hypothetical case. The vendor figures are self-reported.

### 2. Strongest counterevidence
1. The national Medicare null result (E10) and the review's finding of no net change in total utilization (E02).
2. Fewer than 10% of encounters use the exchange (E06). Single-site import studies (Lu, Sodickson) measure a best case that does not show up at population level.
3. Recipients scrutinize inherited analysis less (E14). An apparent cut in reconstruction may partly be lost skepticism, so effort savings must be measured together with error detection.
4. The biggest reductions came with dedicated staff doing the integration (E09).

### 3. Limitations
- **Abstract only:** Rudin, Lammers and Sodickson. **Press release for the percentages:** Li et al.
- **Overlap:** the three reviews share primary studies and probably include Lu 2012, so they are not independent confirmations.
- **What HIE "exposure" means:** usually hospital participation, not clinician use.
- **Medicine vs IC:** medical "duplicates" are discrete and countable; IC reconstruction is analytic and partly required.
- **Thin finance evidence:** one academic analog (consumer mortgages) and one vendor case. No academic or regulator study of commercial credit-memo or spreading automation measured review or rework.

### 4. Unresolved questions and observations that would settle them
- Does integration add reading or reconciliation time for the receiving professional? Needs time-motion or log data on clinicians or analysts using integrated outside evidence vs regenerating it. None found.
- Does pre-integration by the supplier (advisor delivers into the client's memo or model template) differ from the client importing the material itself? Needs a within-firm comparison of IC teams receiving the same advisor output as a PDF vs a linked model or memo section. Measure re-derivations, hours, and detection of seeded errors.
- Does integration lower scrutiny of advisor analyses, as with inherited audit tests? Needs a replication of the inherited-vs-co-developed design with investment analysts, including a variant with provenance and checks-performed documentation.
- Why was the national effect null? HIE use logs linked to repeat-test outcomes would separate "present" from "used".

### 5. Transferability to renewable-energy investment memos and IC workflows
- **What transfers.** When outside evidence sits in the recipient's own working system at decision time, it is regenerated less. Placing advisor evidence (energy yield, independent-engineer findings, interconnection status) inside the IC team's model, data room and memo is more likely to cut re-pulling and re-keying (W2, W5) than a separate portal, which risks low use (E06, E10).
- **Expected size.** Probably moderate. Finance analogs suggest about 20% end to end, and gains are capped by bespoke steps such as site review, title work and interconnection studies (E13).
- **Key differences.** IC re-analysis is often required independent judgment (W1). Project-finance diligence is low-volume and heterogeneous. Quality outcomes such as project underperformance or default are rare and slow, so "no quality loss" is hard to show.
- **Main risk.** Inherited analysis gets less scrutiny (E14). Process and provenance documentation helps only partly (E15).

# search_log.md

## R3D search log (2026-11-15, 18:58–19:10 UTC)

**Successful (sources entered)**
- WebSearch: "Lammers Adler-Milstein Kocher health information exchange redundant imaging emergency departments" → Med Care 2014. Abstract via NCBI E-utilities (PMID 24374414) → R3D-S05.
- WebSearch: "Hersh Totten health information exchange systematic review Annals…2015…" → the paper is in JMIR Med Inform, not Annals. Full text via PMC4704923 → R3D-S02.
- WebSearch: "Menachemi Rahurkar Harle Vest benefits of HIE updated systematic review JAMIA 2018" → full text via PMC7646861 → R3D-S03. The IU scholarworks copy was bot-blocked.
- WebSearch: "image sharing technologies reduction of imaging utilization systematic review meta-analysis Vest" → full text via PMC4730956 → R3D-S01.
- WebSearch: "Rudin Motala Goldzweig Shekelle usage and effect of HIE…Annals 2014" → RAND page returned 403. Abstract via E-utilities (PMID 25437408) → R3D-S04. This is the Annals of Internal Medicine review.
- WebSearch: "Sodickson outside imaging…CD import…Radiology 2011" → abstract via E-utilities (PMID 21507903) → R3D-S06.
- WebSearch: "Everson Kocher Adler-Milstein HIE ED faster accessing…duplicative testing" → the Everson paper was not located. Surfaced PMC7784316 (Yaraghi 2015 JAMIA), full text → R3D-S07.
- WebSearch: "hospital interoperability HIE repeat imaging Medicare national study no significant association…" → Turbow 2024 AJMC PDF, full text → R3D-S08.
- WebSearch: "Fuster Plosser Schnabl Vickery Role of Technology in Mortgage Lending…" → NBER WP 24500 PDF, full text → R3D-S09.
- WebSearch: "Eilifsen Kinserdal Messier McKee…audit data analytics…" → surfaced Li, Gold, Brazel & Leiby (JAR) via the NC State press release. Follow-up search on the title found the VU portal page with abstract excerpt and citation. Wiley full text returned 403 → R3D-S10 (partial).
- WebSearch: "commercial lending automated financial spreading credit memo case study cycle time…" → only vendor cases (Genpact, Evalueserve, EdgeVerve, Scry AI, TCS). Evalueserve page fetched → R3D-S11. EdgeVerve returned 403.

**Unsuccessful or not entered (what this implies)**
- Eilifsen et al. 2020 (Accounting Horizons, NHH PDF): curl connection reset and WebFetch 503. Not entered.
- UNL seminar PDF of the Li/Brazel paper returned an HTML block page.
- PubMed web pages require cookies; NCBI E-utilities worked instead.
- Lammers' $19M national savings estimate appears only in press coverage that was not fetched, so it was not used.
- Flanagan 2012 JACR (regional trauma image transfer, 17% repeat CT rate even with images imported, no comparison group) was found as an abstract but not entered because the design is weak. It could be added as a single-arm observation.
- **Main gap:** no academic or regulator study of commercial-loan spreading or credit-memo automation that measures cycle time together with review or rework steps. Also no audit study measuring end-to-end hours from integrating specialist or analytics output into workpapers. Public testability of RQ3 in finance therefore rests on vendor claims and consumer-lending analogs; a proprietary field study would be needed.
- **Not searched for lack of time:** the Bailey 2013 Memphis HIE back-pain and headache imaging studies, Jung 2015 JACR repeat-imaging costs, Griffith (auditor–specialist integration), and the Austin et al. 2021 CAR data-analytics field study.
