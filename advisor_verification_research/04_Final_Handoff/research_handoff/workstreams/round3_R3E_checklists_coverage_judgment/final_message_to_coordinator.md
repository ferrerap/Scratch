> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from R3E's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

R3E is finished. Files are in /home/user/Scratch/advisor_verification_research/03_Challenge_and_Followup/R3E_checklists_coverage_judgment/: sources.json has 20 sources (20 independent evidence groups) and evidence.json has 22 items (10 qualifies, 6 challenges, 4 supports, 2 contextual). Both load cleanly with json.load.

The evidence splits the dispute rather than settling it. How a list is designed and when it is used decides the effect:
- **Lists handed to a reviewer as the way to review:** these narrow attention and can hurt detection (E01, E02, E06, E08, E12).
- **Specific documentation, or a list used after the reviewer's own pass:** these help (E03, E07, E16).
- **Describing the procedures behind a flagged area:** recipients' risk views on that area are better calibrated (E22).
- **"Checked, no findings" versus silence:** no study tests this directly for recipients' detection.

Access limits: 18 of the 20 sources were read as abstracts only. Pincus 1989 could not be retrieved, so it is not in the register.

# report.md

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

# search_log.md

## R3E search log (2026-11-15, 19:01–19:13 UTC)

**Tools.** WebSearch (standard mode); Europe PMC REST API (abstracts and full-text XML); Crossref API (abstracts and bibliographic checks); IDEAS/RePEc pages; curl plus pdftotext for open PDFs. Downloads went to the scratchpad downloads/R3E folder only.

### Successful queries and paths
1. "Asare Wright 2004 effectiveness of alternative risk assessment and program planning tools in a fraud setting checklist" found Contemporary Accounting Research 21(2). Abstract taken from IDEAS (R3E-S01).
2. "Berbaum checklist satisfaction of search chest radiography Academic Radiology" found the 2006 and 2016 studies. Abstracts from Europe PMC (S10, S11).
3. Europe PMC title searches: "invisible gorilla strikes again" (S12), "Systematic viewing in radiology" (S13, full text from PMC4749649), "Checklists improve experts diagnostic decisions" (S14), Alberdi 2004 CAD (S15), Urbach 2014 Ontario (S16), Haynes 2009 (abstract read and cited in S16's limitations, not registered separately), Haugen surgical checklist trial (S17, the 2019 secondary analysis), Ely & Graber 2015 (S18), Povyakalo 2013 (read, not registered).
4. "Wilks Zimbelman 2004 decomposition…" found S03 via IDEAS. That search surfaced Simon, Smith & Zimbelman 2018 (S04, Crossref abstract).
5. "Hammersley Bamber Carpenter 2010 documentation specificity…" plus a Crossref search returned the published and SSRN abstracts (S02).
6. Crossref search on "Backof Carpenter Thayer construal level evidence formatting" found S05.
7. "Sirois Bédard Bera 2018 … eye-tracking" plus Crossref returned the synopsis (S06). The same search led to an open NHH seminar PDF (Järvinen et al., loan officers, eye-tracking), read in full (S07).
8. Crossref searches for Brasel et al. 2016 (S08, including the CIIA summary abstract) and Kachelmeier et al. 2020 (S09).
9. Crossref searches "Christensen Glover Wolfe CAM paragraphs…" and "audit procedures description in critical audit matter investors perceived assurance experiment" found S19 and S20.
10. All DOIs, volumes, pages and author names were checked against Crossref.

### Unsuccessful or partial searches (and what they imply)
- **Pincus 1989 red-flags questionnaire (AOS 14:153-163):**
  - IDEAS has no abstract.
  - ScienceDirect returned 403.
  - CORE PDFs were behind a Cloudflare challenge (not bypassed); WebFetch also returned 403.
  - Secondary snippets describe the questionnaire's usage and perceptions, not the users-versus-non-users result.
  - Its findings could not be verified, so it is not registered.
- **Asare & Wright full text:** only on a third-party document-sharing site, not used.
- **Sirois 2018 full text:** SSRN and publisher returned 403, and next.sciencegate.app did not resolve (outside the allowed network). The effect of the "procedures overview" condition is therefore unknown.
- **Brasel 2016 CIIA full text (publications.aaahq.org):** 403.
- **White Rose eprint on usefulness of key audit matters:** returned an HTML page, not the PDF.
- **"experiment users perceptions negative assurance review report versus audit report…":** found only older studies (1982 dissertation, 1993 study) through snippets. None isolates negative-assurance wording, and none was verified or registered.
- **"experiment agreed-upon procedures report factual findings users perceived assurance overreliance 'no exceptions'":** only standards, firm marketing pages and exam-prep material. No behavioral study found.
- **"experiment user auditors reliance on SOC 1 … description of tests … exceptions":** only practitioner and exam-prep material. No experiment found.
- **"pertinent negatives radiology report referring physicians … effect on clinical decision" and "referring clinicians preference itemized structured … pertinent negatives":** only stated-preference surveys, no behavioral test. Not registered, since structured-reporting surveys are already in the register.
- **Randle 2020** (Journal of Accounting and Finance; commercial loan officers and critical audit matters; lower approval probability) was seen via Crossref. It was not registered because it is a lower-tier venue with an abstract only. A follow-up could check it.
- **Not searched (time):** aviation checklist studies; workpaper-review experiments on preparer documentation; Hoffman & Zimbelman 2009 (brainstorming and strategic reasoning).

**Implication.** The core CL026 question ("checked, no findings" versus silence, and coverage tables versus none, measured on recipients' detection of material issues) appears untested in public research. The nearest tests are the auditor's-report experiments above, which measure attention, decision change, liability or calibration rather than detection.
