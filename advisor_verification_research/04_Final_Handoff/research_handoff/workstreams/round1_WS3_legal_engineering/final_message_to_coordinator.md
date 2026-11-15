> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS3's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

## WS3 summary (legal and engineering review)

**Delivery problem:** `sources.json` (15 sources) and `evidence.json` (29 items) are written and valid. I could not write `report.md` or `search_log.md`: the harness refuses .md report files from subagents. Their full text is in Appendices A and B below for you to save into `/home/user/Scratch/advisor_verification_research/02_Workstreams/WS3_legal_engineering/`.

**Counts:** 15 sources, 29 evidence items, 15 independent evidence groups.

**Most consequential findings:**
1. **Courts accepted process and coverage checks instead of reviewing every item (e-discovery).** The conditions were a disclosed protocol, sampling of excluded documents, recall thresholds, a qualitative look at what was missed, and an adversary who could challenge (E08, E10, E14, E15). Well-run technology-assisted review had humans look at about 1.9% of documents. Precision beat exhaustive manual review (84.7% vs 31.7%); recall was 76.7% vs 59.3%, not significant (E12).
2. **Courts weighed outcome evidence over explanations of the method.** Judge Peck put recall and precision above "the science behind the black box", and counsel need not explain why documents were coded (E09).
3. **In one case, disclosed sample data let the other side catch a wrong headline metric.** Claimed recall/precision was 85%/58%; recomputed it was 97.4%/16.7%. The review burden then shifted to the recipient, who had 70 attorneys on it (E16).
4. **Citing sources did not make legal AI answers correct.** Commercial source-citing tools hallucinated on 17–33% of 202 queries (E01). Real sources cited for claims they don't support take full reading to catch (E02).
5. **Review effort scales with risk and complexity.** ABA Opinion 512 ties it to tool and task (E05, E06), UK structures checking uses categories 0–3 (E21), and NRC grades supplier oversight by importance (E23).

**Strongest counterevidence:** UK structures standard CG 300 requires the independent checker to work "without exchange of calculation sheets" (E20). There, re-deriving the work is the point of governance, and access to the producer's working is deliberately cut off. Also: legal and engineering sign-off responsibility can't be delegated (E17, E18, E24), and code review mostly does things other than catch defects (E27, E29).

**Access limitations:**
- ABA 512: americanbar.org blocked; read only through verbatim secondary quotation.
- Schwarcz et al.: full text and SSRN blocked; abstract only. Its hallucination counts are unverified.
- Magesh et al.: read as arXiv v1; the published journal PDF failed to download.
- Sedona TAR primer: superseded public-comment draft.

---
## Appendix A: report.md content

# WS3: Legal review and engineering/technical review (RQ1, RQ2)
All evidence here is analogy. No source studies advisors and investment committees directly.

## Bottom line
1. **Governance requires much retained review (W1), regardless of what the producer discloses, but scales it to risk.**
   - Legal: the lawyer's gatekeeping duty under Rule 11 can't be delegated (E17, E18); ABA 512 requires "an appropriate degree of independent verification or review" (E05).
   - Engineering: independent checking is built in (E20, E22, E24).
   - Depth is graded: ABA 512 by tool and task (E05, E06); CG 300 by category 0–3, with a separate-organisation check team only for complex or novel structures (E21); NRC App. B supplier oversight by "importance, complexity, and quantity" (E23).
2. **Re-derivation is sometimes the purpose, not a symptom of opacity.** At its higher check categories, CG 300 requires independent analysis "without exchange of calculation sheets" (E20). The only permitted link is comparing results against an agreed Approval in Principle. This is the strongest counterexample to the thesis.
3. **Courts accept coverage validation (X4) in place of item review in e-discovery, under conditions.** Disclosed protocol, sampling of excluded ("null") documents, recall thresholds, qualitative review of misses, and adversarial challenge (E08, E10, E14, E15). With about 1.9% human review, good TAR matched or beat manual review: precision 84.7% vs 31.7%; recall 76.7% vs 59.3%, not significant (E12). Manual review missed 20–75% of relevant documents (E13).
4. **Outcome and coverage evidence (X4/X5) is accepted without explanation of the system's internals (X2).** Peck cares about recall/precision, not the black box; counsel need not explain why documents were coded (E09). ABA 512 allows reliance after testing on a sample (E06).
5. **Citations (X3) are not correctness (X5).** Source-citing legal tools hallucinated on 17–33% of queries (E01). Misgrounded citations need the source read to catch (E02). The court-decisions database lists 971 cases categorised as "Misrepresented" (E19).
6. **In engineering, understanding context and rationale (W2) drives review cost.** At Microsoft, understanding was the main challenge, and 91% of programmers said unfamiliar files take longer (E26). PEER tall-building guidance: "More is not necessarily better"; flag key assumptions, give worked examples, and agree an early Basis of Design that becomes "the set of rules" for checking (E25). This is guidance, not a measured effect.

## RQ1: why review persists
- **W1, required judgment (strong):**
  - Legal: Rule 11 gatekeeping (E17). The signer who read none of a colleague's cited cases acted in bad faith, and knowledge is not imputed (E18); the producer was human, the closest analog to an outside advisor. ABA 512 and Rules 5.1/5.3 (E05). Validation folded into Rule 26(g)'s "reasonable inquiry" (E14).
  - Engineering: CG 300 (E20, E21); NRC Criterion III, verification by others via design review, alternate calculations or testing (E22); PEER independent peer review (E24); even code owners get reviewed at Google (E28).
  - Qualification: W1 is a menu. NRC counts "design reviews" of documented work (E22); CG 300 allows comparing results (E20).
- **W2, missing rationale (moderate):** E26, E25. Missing vendor reliability information forces checking everything (E03).
- **W3, producer error (strong for legal AI):** E01, E19 (913 lawyer decisions), E17. That many lawyers skipped verification suggests it is genuinely costly.
- **P1.6, ritual or other functions:** the "myth" of exhaustive manual review (E13). Defects were only 14% of review comments; review also serves education and norms (E27, E29).
- **W4/W5:** thin. Agreeing criteria up front (Basis of Design, Approval in Principle) front-loads adaptation (E25, E20).

## RQ2: cheaper verification without worse detection
- Courts accepted validation with sampled excluded documents and acceptable-miss thresholds: recall 70–80% target, 74–89% accepted in Diisocyanates, about 85% in Lawson (E15). They also required qualitative review of misses, because recall alone is weak for rare documents, plus stopping rules (relevance ≤10%) and a counterparty who could challenge (E08, E11, E15).
- Underlying data, not just the headline metric, enabled error detection, but shifted burden to the recipient (E16; P3.2).
- Traceability cuts the cost of finding evidence, not of judging it (E02).
- Reliability evidence must be revalidated as tools change (E06 vs E07).
- Small units, attached automated checks and reviewers with context go with light review: median 1 reviewer, 24 lines, under 4 hours (E28; correlational only).
- Source grounding reduced fabrication in an RCT; reviewer time not measured (E04, abstract only).

## Strongest counterevidence
1. CG 300 no-exchange rule (E20).
2. Citation-grounded tools still err, and subtly (E01, E02).
3. Responsibility can't be delegated and review layers are deliberate redundancy (E17, E18, E24).
4. Review is not only verification (E27, E29).
5. Coverage metrics are weak for rare, material items, i.e. fatal-flaw diligence issues (E15).

## Discriminations
- **Re-derivation required (W1):** E18, E20, E21, E22, E24.
- **Caused by missing rationale (W2):** E03, E26.
- **Caused by producer error (W3):** E01, E16, E19.
- **X4 substitutes for item review only** for high-volume work, where the comparator is itself imperfect, with validation per production, null-set sampling, thresholds, qualitative review of misses, and adversarial checking. Not shown for bespoke judgment work.

## Limitations
- All analogy; standards show obligations, not effectiveness; code-review studies are single-company and observational.
- Access gaps as noted in the summary; Grossman & Cormack compare best-in-class TAR and the authors have interests.

## Unresolved questions and what would resolve them
1. **What share of IC/credit re-review is W1 vs W2?** Time-use logs coded into mandated checks, finding evidence, understanding rationale, and fixing errors.
2. **Does curated linkage cut review time without lowering detection?** A seeded-error experiment with advisor-style reports, measuring time and detection of rare material errors.
3. **Would lenders accept null-set sampling or coverage disclosures instead of re-review?** Credit policies or IE procurement documents.
4. **Where is independent re-derivation mandated in energy diligence (e.g., IE re-running energy yield)?** IE scopes that say "independent" vs "review".
5. **Do source-linked AI tools shift burden to the recipient?** Buyers' review hours before and after adoption.

---
## Appendix B: search_log.md content

**Succeeded:**
- arXiv 2405.20362 (v1).
- jolt.richmond.edu/jolt-archive/v17i3/article11.pdf (after the /files/2011/04/ path returned 404 and scholarship.richmond.edu hit a Cloudflare challenge).
- eCFR renderer API for App. B (nrc.gov returned a "Request Access" page).
- CourtListener RECAP storage PDFs for Da Silva Moore (Doc 96) and Mata (Doc 54). Justia was Cloudflare-blocked; the CourtListener API needs authentication.
- Steptoe-hosted Rio Tinto (Doc 207).
- standardsforhighways.co.uk CG 300 attachments (v0.1.0, v0.2.0, v0.2.1).
- PEER report 2017/06.
- sback.it PDFs for Bacchelli 2013 and Sadowski 2018.
- Sedona TAR Case Law Primer 2d ed., public-comment version.
- Charlotin database landing page.

**Failed or blocked:**
- americanbar.org ABA 512: Cloudflare via curl, 403 via WebFetch. Got verbatim text via josephhollander.com (Stephens 2024), NCBE Bar Examiner and National Law Review.
- Schwarcz et al.: UMN PDF Cloudflare/403, SSRN Cloudflare. Abstract via WebFetch summary only; Law360 seen only as a search snippet; UMN Law magazine read.
- Published JELS Magesh PDF (nlp.stanford.edu): connection reset twice.
- In re Broiler Chicken validation protocol: the govinfo hit was a different order (Doc 1090), not used.
- ABA 08-451: only secondary summaries found, not included.
- Choi et al. Minnesota Law Review: guessed URL returned 404; left to WS7.

**Not attempted (time):**
- Owner's/independent engineer submittal-review mechanics (WS2 may cover).
- ASME NQA-1 (paywalled).
- Experiments timing professional reviewers with vs without evidence linkage in legal or engineering settings.

**Implication:**
- Primary ABA opinions and law-repository papers are bot-blocked; court records are reachable via RECAP.
- No public data found on supervising-lawyer or engineer review time.
