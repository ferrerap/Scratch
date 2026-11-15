> Provenance note (coordinator): verbatim final hand-back of Final fidelity checker (FC), saved by `scripts/save_handback.py`. Subagents return narrative as text per harness convention (see run_log D08/D09).

I checked the brief against the register and wrote the fidelity check to `/home/user/Scratch/advisor_verification_research/03_Challenge_and_Followup/final_fidelity_check.json`. It loads cleanly with `json.load`. It lists 29 issues (4 high, 11 medium, 14 low), and about 84 claim-to-EVR citations checked out. I pulled every record with python. The Summary and all three "What can reasonably be concluded" sections were checked in full; the rest of the brief was checked mostly in full, with RQ4–RQ6 and the transfer limits spot-checked. No project files were edited.

**High severity**
- **FC-01, Summary 3:** "They raise trust whether or not they are checked" is contradicted by EVR103. In that study, checked random-citation answers were *not* more trusted than answers with no citations, and checking went with lower trust. EVR108 measures link clicks, not trust.
- **FC-02, Summary 1 and RQ1:** "NRC requires alternate calculations (EVR083)" is wrong. The rule lets the licensee choose design review, alternate calculations or testing.
- **FC-04, Summary 2 and the RQ1 conclusion:** The claim that public lender work is "mostly W4 ... driven by measured W3 bias" is labelled "Empirical". It actually rests on one lender's presentation and one rating action. Neither "mostly" nor "full parallel assessments happen only some of the time" appears in the records, and "driven by" links them to a separate wind back-test, which is my-side inference by the synthesis.
- **FC-06, Summary 4 and the RQ2 conclusion:** "Lowered fraud or abnormality detection" overstates three abstract-only items. EVR298 measured risk assessments, not detection. EVR303 is about decomposition, not a checklist, and its result is ambiguous. EVR309 is a non-randomized comparison across two studies.

**Medium severity, main themes**
- **Wrong category or wrong source:** EVR245 is a court decision but is cited as a standard prescribing extra procedures (FC-03). EVR059 is about spotting conflicts of interest but is used as evidence of thin review (FC-12).
- **Numbers:**
  - The 16–67% range in Summary 5 comes from just two abstract-only studies (FC-08).
  - EVR296's 9.7% SD is from one site only; the other site was 3.9% (FC-11).
  - EVR199's 88% vs 34% is the share of complete reports, not of institutions, and the data are correlational (FC-14).
- **Missing caveats:** The press-release caveat on EVR272/273 is dropped in RQ3 (FC-10). "AI drafting generally moves effort into review" rests mostly on self-report (FC-09).
- **revision_candidates.json (FC-26 to FC-29):** The supporting/challenging lists seem to be set against the *original* claims, not the proposed wording. As a result:
  - In REV005 and REV007 they are effectively reversed.
  - REV002, REV003, REV006, REV008, REV009 and REV010 list as "challenging" items that the proposed wording relies on.
  - The fix is either a note saying the lists refer to the original claim, or moving the IDs.

**Low severity:** Denominator and framing slips (EVR108's "1% of clicks", EVR189's "fell from 82%"), causal wording for pre/post or observational designs (EVR201, EVR197), stated policy presented as behaviour (EVR130), and analyst inferences without a label ("not opacity", "adoption followed accreditation").

The three items marked as duplicates (EVR147, EVR152, EVR164) are not cited anywhere in the brief or the revision file.

I did not check the cross-domain transfer table, the "~33" and "~9 evidence group" counts, or REV011's challenging IDs.

Each issue in the file includes exact replacement wording.
