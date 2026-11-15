> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS8's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

## WS8 summary

Three of the four files are written and the JSON validates. The Write tool refused `report.md` ("Subagents should return findings as text"), so I did not create it. Please save it from the WS8 findings below. The files are in /home/user/Scratch/advisor_verification_research/02_Workstreams/WS8_structured_reporting_coverage/:
- sources.json
- evidence.json
- search_log.md

**Counts:** 21 sources (WS8-S01 to S21), 26 evidence items, 21 evidence groups. Two pairs are not fully independent: S08 and S10 share a department, and S07 and S11 share an author.

**Most consequential findings:**
1. **Required-element lists make reports more complete.** Completeness rose in 13 of 14 synoptic pathology studies (E06). Institutions using checklists produced complete reports 88% of the time versus 34% without (E08). But clinical or decision impact is not shown.
2. **Recipient benefit is mostly stated preference.** Clinicians rated structured reports higher for content (8.33 vs 7.61) and clarity, but rated decision usefulness did not differ (P=.146) (E01). 89% of clinicians said pertinent negatives were useful (E12). The best usability item: surgeons had enough planning information in 96%, 69% and 98% of structured reports versus 31%, 43% and 25% of narrative ones (E09). No study measured clarification calls.
3. **Mandatory re-review continues even though it rarely changes management.** At two referral centres, 1.4% and 1.2% of cases had a management-relevant change (E18, E19). The policy re-examines the original slides and is justified by the cost of errors, which supports P1.1.
4. **Redo depends on access to the evidence, not just on having it.** Repeat imaging was 72% when outside images were unavailable, 52% when they arrived on CD, and 11% once imported into the hospital's system (adjusted OR 9.0) (E21, E22).
5. **Standardization yields a standard core plus local customization.** Five RSNA templates covered only 17–49% of what real reports contained (E15). CAP lets labs change wording and order (E16). The VA used synoptic format in 77% of resections but 19% of biopsies (E17).

**Strongest counterevidence:**
- The only top-grade radiology study found structured reporting lowered completeness (68.7 to 54.3) and accuracy (E05).
- Prefilled "normal" text created contradictions and saved no time (E11).
- A standard vocabulary still gave only fair agreement on the final judgment (kappa 0.28) (E25).

**Access limits:** 12 of 21 sources are abstract-only. PubMed was cookie-walled, so I used Europe PMC. The ASTM E1527-21 page returned 403 and E2018 is paywalled. SOC 1 is left to WS1.

---
## Content for report.md (please save; the tool blocked it)

# WS8: Structured/synoptic reporting and coverage visibility

**Analogy:** a radiologist or pathologist (producer) reports to a treating clinician (recipient with decision authority); the patient bears the consequences. Most items are analogy evidence for renewable-energy diligence. 40 CFR 312 is a non-medical design precedent, not evidence of effect.

**Access:** 9 sources were read in full text: S01, S02, S04, S07, S08, S09, S13, S17, S19. The other 12 are abstract-only.

## 1. RQ2 / P2.4: Does making coverage explicit help recipients?

**1a. Completeness of the report itself (X5)**
- Synoptic pathology: completeness rose in 13 of 14 studies. Gains came in items narrative reports skip, such as margins and lymphovascular/perineural invasion. Examples: margins 54% to 100%, stage 39% to 100%. Tumour type and nodal status were already adequate in narrative reports (E06).
- CAP Q-Probes: 68.8% of reports were complete overall; 88% with checklists vs 34% without. This is correlational (E08).
- Pancreatic CT templates captured 10.6 of 12 key features vs 7.3 (E09).
- A mandatory checklist cut residents' misses of non-fracture findings from 28.3% to 9.3% (p=0.01). Fracture misses did not improve (9.8% vs 14.5%) and the overall change was not significant (E10).
- Attending revisions fell from 10/41 to 2/17, mostly typographical (E26).

**1b. Recipient perception and use**
- Clinicians rated structured reports higher for content and clarity, but rated decision usefulness did not differ (E01).
- 89% of clinicians and 92% of radiologists called pertinent negatives useful (hypothetical reports). Itemized vs prose made no difference (E12).
- Surgeons judged structured reports sufficient for planning far more often and gave more definitive resectability answers (E09). More definitive is not shown to be more correct.
- No study measured clarification calls (see search_log). This is absence of evidence, not evidence of absence.

**1c. Costs and failure modes**
- A rigid structured reporting system reduced completeness and accuracy; users called it "overly constraining" and slow (E05). This is the only level-A study in the review (E03).
- Prefilled templates: 39 of 2,012 errors (1.9%) were template text contradicting the findings, with no error or time benefit (E11).
- Pathologists found synoptic forms inflexible and hard to integrate with IT (E07). Producer time is mostly unmeasured; reporting-time results are mixed (E04).
- The review authors question whether the benefit comes from structure or from agreeing on standard content (E04).

**Net:** supports P2.4 for completeness. Evidence for better recipient decisions or less recipient work is weak and indirect. Agreed content matters more than layout.

## 2. P5.1: Repeatability and customization
- One department built 228 templates over about 2 years, covering 94% of volume. Afterwards it had 100% format adherence and 99% normal-report adherence, after every template was vetted by all its users (E13).
- CAP requires all required elements in at least 90% of resection reports. Labs may still alter wording and responses, reorder, add items, and implement at their discretion. IT use needs a licence and there is an 8-month adoption window (E16).
- RSNA templates covered 17–49% of real report content (E15). Only 13% of radiologists used rigid checklists (E14).
- Templates were built from RSNA templates plus local must-check items (E26), and through 16 disease-management teams (E02).
- VA synoptic use was 77% for resections vs 19% for biopsies (E17). My inference: this follows where accreditation applies.
- BI-RADS final-category agreement was kappa 0.28 (E25).

**Net:** qualifies P5.1. The core content is repeatable and auditable, with local additions on top. Judgment stays variable.

## 3. RQ1: Why recipients re-review or re-order
- **Policy (W1):** Hopkins found 86 of 6,171 (1.4%) changed diagnoses, higher in serosal (9.5%) and female reproductive tract (5.1%) cases (E18). Iowa found 2.3% major and 9.0% minor disagreements, and 1.2% management changes (E19).
- **Quality-driven:** routine re-reads of head and neck imaging changed stage in 56.4% and management in 38.3%. Stage agreed with pathology in 40% of original reports vs 93.3% of second opinions (E20). The authors do not separate missing staging elements from expertise.
- **Inaccessible evidence:** repeat imaging was 72%, 52% and 11% as above. Imported cases matched the all-local rate of 13% (E21, E22). This is observed behavior, relevant to P1.2 and P3.1.
- **Duties kept by the acquirer:** under 40 CFR 312.22 it must check liens, its specialized knowledge, price vs fair market value, and commonly known information (E24).

## 4. Non-medical equivalents
- 40 CFR 312.21(c) requires an opinion plus identified data gaps, the sources consulted to address them, and their significance (E23). This is an obligation, not evidence of effect.
- ASTM E1527-21 and E2018 were not accessed. SOC 1 "no exceptions noted" is cross-linked to WS1.

## 5. Strongest counterevidence
E05, E01 (consistent with P2.3), E11, E25, E18/E19.

## 6. Transferability
- **Likely to transfer:**
  - a recipient-defined list of required elements, with explicit "checked: no issue" entries for items narratives skip;
  - data-gap disclosure, which already exists in Phase I ESAs;
  - delivering evidence into the recipient's own systems.
- **Differences:** medicine has accreditation enforcement, high volume and narrow tasks. Diligence deals are bespoke and low-volume with no mandatory standard.
- **To verify:**
  - whether ICs and lenders actually skip re-checks;
  - counts of follow-up questions;
  - prefilled "no exceptions" text contradicting the report body;
  - how many template variants providers need.

## 7. Limitations
- Many abstracts; single-centre before/after or rating studies.
- No recipient time or call data.
- Old second-opinion data with differing definitions.
- Paywalled ASTM standards.

## 8. Discriminating observations
1. Call, addendum and question logs before and after coverage maps.
2. Same required elements presented as prose vs structured layout.
3. Referral centres relaxing re-review for synoptic reports.
4. Planted omissions, with vs without no-finding entries.
5. Share of standard vs local template content at providers.
