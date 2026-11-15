> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from R3E's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

## R3E: Checklists, explicit coverage and recipient judgment (Round 3 dispute on CL026)

### 1. Findings on the dispute
**Main point.** "Checklist" covers two different things that the Round 2 debate treated as one:
- **Reviewer-side tools.** These are standard lists or programs that a reviewer must work through.
- **Coverage disclosures from the producer.** These are statements of what was examined, how, and with what result, which CL026 is about.

Most of the negative evidence concerns the first. The evidence on the second is thinner, comes from recipients reading audit reports, and is mixed.

**Branch (b), anchoring and narrowing of attention, has the best support.**
- **Asare & Wright 2004 (E01, E02).** 69 auditors worked an SEC fraud case.
  - A standard SAS 82 risk checklist led to lower fraud-risk assessments.
  - A standard audit program led to a less effective fraud program than an expert benchmark.
  - Neither tool made auditors more willing to consult fraud specialists.
- **Simon, Smith & Zimbelman 2018 (E06).** 101 experienced auditors used the likelihood-times-magnitude breakdown that auditing standards recommend. They became less concerned about high-risk fraud schemes.
- **Sirois, Bédard & Bera 2018 (E08), on the recipient side.** Highlighted key audit matters pulled readers' eyes toward those items. With three matters, readers paid less attention to the rest of the financial statements. Participants were students, and the study measured attention, not detection.
- **Hammersley et al. 2010 (E04).** Specific risk documentation combined with a priming reminder lowered auditors' sensitivity to fraud.
- **Mechanism evidence from radiology:**
  - 83% of radiologists searching for nodules missed a gorilla image 48 times the size of a nodule. Most of them looked straight at it (Drew 2013, E14).
  - Adding a salient finding still suppressed reporting of other abnormalities when readers used a vocalized checklist (Berbaum 2016, E13).

**There is credible evidence that explicit coverage helps, under specific conditions.**
- **Specific documentation.** Auditors given specific (not summary) planning-stage risk documentation, without a priming reminder, raised their fraud-risk assessments and asked for more evidence (Hammersley 2010, E03). This is the closest structural analog to a handoff from producer to reviewer.
- **Timing.** ECG experts who used a checklist after their own reading corrected more errors.
  - Errors corrected: 0.29 per ECG with the checklist versus 0.03 without.
  - Net errors: 0.39 versus 1.04 per ECG.
  - Cognitive load did not rise (Sibbald 2013, E16).
  - By contrast, a checklist imposed during reading cut detection accuracy (ROC area) to 0.68, against 0.75 in an earlier study using the same images (Berbaum 2006, E12).
- **Directing attention to assumptions themselves.** Prompting auditors to consider how management arrived at an assumption made them more sensitive to contradictory evidence. Graphs had a similar effect (Backof 2018, E07). This addresses the worry that unlisted judgments go unchallenged: the object to make explicit is how the judgment was reached, not a list of figures that were checked.
- **Describing procedures for a flagged matter.** When the auditor's report described the procedures used, sophisticated users' risk assessments shifted less once the flagged risk event occurred (Boo et al. 2025, E22). This was measured as stability of the assessment, not accuracy.

**Branch (c), no effect beyond a complete document, holds at system level when lists are mandated or underpowered.**
- In Ontario, 101 hospitals adopting surgical checklists showed no significant change in mortality (OR 0.91, 95% CI 0.80–1.03) or complications (OR 0.97) (Urbach 2014, E18).
- In a Norwegian trial, benefits appeared where all three checklist parts were used. Infections fell from 7.4% to 3.6% (Haugen 2019, E19), but implementation quality was not randomized.
- Checklists widened the differential diagnosis (6.5 versus 3.4 diagnoses considered) without a significant drop in errors (Ely & Graber 2015, E20, an underpowered pilot).
- Looking at more of an image did not mean finding more. Students trained for full coverage performed worse (Kok 2016, E15).

That last result supports keeping X4 (visibility of coverage) separate from X5 (correctness). "We looked at X" is not "we would have caught a problem in X."

**Branch (a), boilerplate, is supported as a producer incentive, not as observed skimming.**
- In a mock-juror study, any disclosed matter, even one unrelated to the later fraud, reduced auditor liability relative to explicitly stating there were no critical audit matters. The authors warn this rewards innocuous boilerplate (Brasel 2016, E10).
- Disclosing an area of measurement uncertainty lowered users' confidence in that area. It also lowered the auditor's perceived responsibility for a later misstatement there (Kachelmeier 2020, E11).
- In a small study of loan officers, flagged content steered their early search only when the report came from a credible (Big 4) signer. The effect disappeared over the full search (Järvinen et al. working paper, E09).

**"Checks with no findings" versus silence (P2.4).**
- Recipients do react to "examined and resolved" statements: a resolution paragraph reduced investors' reaction to a flagged matter (Christensen 2014, E21). So these statements are not simply ignored, but whether the reassurance is justified was not tested.
- Silence is over-trusted. Mammography readers using computer-aided detection lost sensitivity most on cancers the software failed to flag (Alberdi 2004, E17).
- No study found compares an explicit "checked, no exceptions" statement with silence on whether recipients detect material issues. This is absence of evidence.

### 2. Strongest evidence each way
- **Against explicit lists improving detection:**
  - Asare & Wright 2004 (E01, E02): professionals, a known-fraud case, an expert benchmark.
  - Sirois 2018 (E08): attention moved away from unlisted areas.
  - Berbaum 2006 (E12): an imposed list lowered experts' accuracy.
- **For explicit coverage helping:**
  - Hammersley 2010 (E03): specific documentation raised downstream vigilance.
  - Sibbald 2013 (E16): a list used for verification after the expert's own pass.
  - Boo 2025 (E22): procedure descriptions calibrated users on flagged areas.
  - Backof 2018 (E07): prompting focus on how assumptions were derived.

### 3. Unresolved
1. No experiment plants a material issue outside the listed coverage and measures whether recipients of a coverage-explicit report detect it less often (narrowing) or more often (because declared gaps cue them) than recipients of a report without coverage.
2. No test of "checked, no findings" versus silence versus "not checked" on recipients' detection and reliance.
3. Whether stating what was not examined, and how sensitive each check was, reverses the narrowing effect.
4. Professional recipients: Sirois used students, and the loan-officer study had cells of 8–10.

Two experiments would discriminate between the branches:
- **Coverage format.** Give IC or credit reviewers a 2x2: coverage table (yes/no) crossed with a planted material issue (inside or outside the listed scope). Measure detection, time, and confidence calibration.
- **Timing.** Compare reviewers who see the coverage table before their own review with those who see it after. Sibbald and Berbaum predict that seeing it after is better.

### 4. Transferability to diligence reports for investment and credit committees
- **Mechanisms that probably transfer:**
  - Explicit lists steer the reader's attention.
  - Reviewers anchor on standardized programs.
  - Readers treat unflagged areas as clean.
  - Producers have liability incentives to pad disclosures.
- **Design implications (inferences, not findings):**
  - Make coverage deal-specific, not generic.
  - State scope exclusions and how sensitive each check was, not just "no exceptions."
  - Make key assumptions and how they were derived the listed objects.
  - Encourage committees to do an independent first read before consulting the coverage table.
- **Consequential differences:**
  - Committee members are accountable decision-makers with their own criteria (W1 and W4).
  - Diligence documents are long, and committee review is time-boxed.
  - None of these studies measures committee decisions or deal outcomes.
- **Limitations:** 18 of 20 sources are abstract-only. Effect sizes are mostly unavailable for the accounting experiments. The medical and aviation-style evidence is mechanism analogy only. Aviation was not searched.
