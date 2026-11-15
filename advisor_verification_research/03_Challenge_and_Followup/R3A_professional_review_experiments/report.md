> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from R3A's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

## R3A — Professional reviewers: does traceability cut review effort while keeping error detection?

### Bottom line
After targeted searches across medicine, radiology, audit, law and finance, I found **no study with the target design**. That design would be:
- professional reviewers who are accountable for output made by someone or something else;
- assigned at random to output **with vs without** source links, provenance or structured evidence;
- measured on **both** review effort and detection of seeded or audited errors and omissions.

This is absence of evidence, not evidence of absence. The professional studies that do exist fall into three groups:
- (a) traceability as one part of a bundle, with no seeded errors;
- (b) traceability preferences that are self-reported or qualitative only;
- (c) review of AI drafts **with no traceability**, measuring effort and errors.

Group (c) is informative about the baseline any traceability feature would have to improve on.

### Findings by proposition

**P2.1 (traceability reduces verification effort): the professional evidence covers only bundles or self-reports.**
- **Scout RCT (R3A-E10).**
  - Design: randomized crossover, 20 clinicians, 7 specialties, 200 cases.
  - Comparison: an LLM tool that cites a source record for every claim, vs searching the EHR alone.
  - Time: completion time ratio 0.624 (95% CI 0.565–0.689).
  - Workload: NASA-TLX −8.74 (95% CI −12.02 to −5.46).
  - Accuracy: blinded rubric met non-inferiority (+0.20; 95% CI −0.20 to 0.61).
  - Limits: the comparator has no AI at all, so the effect of the citations cannot be separated out. There were no seeded errors, and the paper was written by the tool's developers.
- **FinGround pilot (R3A-E17).**
  - 24 equity-research and compliance analysts checked AI claims against 10-K/10-Q filings.
  - They strongly preferred citations to a specific table cell over paragraph-level ones, reporting verification "in seconds rather than minutes".
  - Limits: uncontrolled, self-reported, run by the developers, one author has a commercial affiliation.
- **Deployed without published evaluation.**
  - A sentence-level provenance interface for clinicians has only a formative, qualitative evaluation (R3A-E15).
  - Abridge's "Linked Evidence" (note statement linked to transcript and audio) is deployed, but I found no outcome data (R3A-E16).

**P2.2 (traceability keeps or improves detection): not tested with professionals. Baseline detection without traceability is poor.**
- **Biro 2025 (R3A-E01).** 20 practicing primary care physicians reviewed AI-drafted patient-portal replies.
  - Each of the 4 erroneous drafts was missed by 13–15 of 20 physicians.
  - 35–45% of erroneous drafts were sent with no edits.
  - On average, 2.67 of the 4 were missed.
- **Small 2025 (R3A-E05).** Residents, blinded to who wrote each draft, edited LLM-drafted vs physician-written hospital-course summaries under time limits.
  - They edited less of the LLM drafts: 31.5% vs 44.8% of characters (P<.001).
  - After editing, the LLM versions had more confabulations (−0.98, SD 3.53; P=.002).
  - The commentary on this study notes the 10-minute review window may have limited detection (R3A-E06).
  - This is the one professional study found that measured both editing effort and remaining errors: less effort went together with more surviving errors.
- **Acosta 2024 (R3A-E07).** Radiology readers edited AI-drafted CT reports, half of which had 1–3 seeded errors.
  - Median reporting time fell from 573 s to 435 s (p=0.003).
  - Clinically significant errors did not differ significantly: 0.27 vs 0.38 per report.
  - Limits: only 3 readers, the catch rate for the seeded errors was not reported, and one reader got slower (R3A-E08).

**P2.3 (trust rises without better detection).**
- In Biro, 90% of physicians said they trusted the tool and 80% said it reduced workload, even though most missed the errors (R3A-E02).
- The gap between trust and detection appears **with no explanation or citation present**, so citations are not needed to produce over-trust.
- Chen 2024 (R3A-E04): physicians' LLM-assisted replies took on the draft's clinical content (similarity to the draft p=0.81; agreement between physicians rose from kappa 0.10 to 0.52). This is anchoring, and it **challenges P3.3**: drafting help carried substantive judgment with it.

**P2.4 (visibility into scope and omissions).**
- Omissions were the most common scribe error: 55/66 errors for product A and 33/61 for product B (R3A-E14).
- The authors argue omissions are the hardest errors for clinicians to spot.
- Links from statements to sources (X3) cannot reveal what was left out. No professional study tests coverage visibility (X4).

**P2.5 (citations do not guarantee correctness).**
- FinGround (R3A-E18): 56% of the 27 hallucinations that analysts flagged after the tool missed them were computed claims.
- The authors say a "supported" label only means the claim matches the retrieved source, not that the source is correct.

**P3.2 (AI assistance shifts effort rather than removing it): mixed.**
- **Supports:**
  - Tai-Seale 2024 (R3A-E19): integrated drafts raised physicians' read time by 21.8% (95% CI 5.2–41.0), reply time did not change, and replies got longer.
  - The Scout authors describe the change as moving work "from manual curation to verification" (R3A-E11).
- **Challenges, at the level of time with audited or rated quality:**
  - Huang 2025 (R3A-E09): field cohort, 15.5% faster radiograph reporting; peer review of 800 studies found no accuracy difference.
  - Afshar 2025 (R3A-E13): −0.36 h/day on notes (95% CI −0.55 to −0.17); note-quality scores stayed high.
  - Lukac 2025 (R3A-E12): one scribe cut time by 9.5% (95% CI −17.2 to −1.8), the other had no effect; inaccuracies were only self-reported.
- None of these field trials measured whether the accountable signer caught errors.

### Strongest counterevidence
- **Against "the evidence is lay-only":** Scout (E10) is a professional RCT with blinded outcome scoring, showing a large time cut with accuracy held, using a tool built around citations.
- **Against "time savings always cost quality":** Huang (E09) and Afshar (E13) show professional time savings in the field with no detectable quality loss.
- **Against the thesis that drafts with traceability preserve independent judgment:** experienced professionals missed most plausible errors (E01), let more confabulations through while editing less (E05), and anchored on the draft's content (E04).

### What remains unresolved
1. Whether source links themselves (not the AI bundle) cut professional review time. This needs Scout-like tasks with an arm that has the AI but no citations.
2. Whether links raise professionals' catch rate for seeded **plausible** errors, **omissions** and **computed-metric** errors, under realistic time budgets.
3. Whether showing coverage (X4) improves detection of omissions.
4. Whether self-reported speed-ups (FinGround) hold up under timed measurement.

**Observations that would settle these:**
- A 2×2 experiment (traceability yes/no × coverage disclosure yes/no) with credit analysts or clinicians, using seeded factual, omission and calculation errors, measuring time and catch rate.
- Usage logs of deployed link features (e.g., how often Linked Evidence is opened) joined to independent audits of signed notes.

### Transferability to investment and credit diligence
- **What carries over:** an accountable reviewer signs off on someone else's draft under time pressure, and omissions and plausible errors evade review.
- **Key differences:**
  - Diligence outputs are long and draw on many documents.
  - Errors often sit in derived metrics (DSCR, P50/P90, degradation-adjusted cash flows), and a link to an input does not verify a calculation (E18).
  - Consequences arrive late.
  - There is a committee-level second review.
- **Implications:**
  - Traceability would need to reach calculations and coverage, not just cite sources.
  - A recipient's stated workload relief is not a valid proxy for verification quality (E02).
  - Integrating advisor text straight into IC memos risks the reviewer adopting the advisor's judgments, not just its wording (E04).
