> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS1's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

WS1 summary

`sources.json` and `evidence.json` are written to `/home/user/Scratch/advisor_verification_research/02_Workstreams/WS1_audit_specialists/` and both pass JSON validation. The tool blocked me from writing `report.md` (subagents may not write report files), and I did not try to get around it. I also did not create `search_log.md`, since it would hit the same rule. The full text of both is at the end of this message for you to save. That is why this reply is longer than 300 words.

Counts: 17 sources, 33 evidence items, 16 independent evidence groups.

Most consequential findings:
1. **Required review that transparency can't remove (W1).** The auditor's "sole responsibility" cannot be delegated (WS1-E11). ISA 610 requires the auditor to re-perform some of the producer's work and to keep all significant judgements (WS1-E17). The required amount of work scales with risk, how significant the work is, and the producer's competence and objectivity. Documentation quality is not one of the factors (WS1-E01).
2. **Missing documentation is explicitly tied to extra work (W2).** If a service-auditor report doesn't describe its tests and results, the user auditor has to do more work (WS1-E20). Without a model description, the fallback is building an alternative model (WS1-E03). If the producer has documented its own data tests, reviewing them may stand in for re-testing (WS1-E13).
3. **Checks with no findings.** The IAASB requires reports to describe tests performed even when nothing was found. It does not require sample sizes in that case, citing cost to the producer (WS1-E22).
4. **Tightening the rules added little measured effort.** Most of the 31 partners interviewed estimated the extra time at under 1% of audit hours. This comes from a self-reported, non-random PCAOB review, not a causal study (WS1-E08). Effort moved earlier into planning rather than growing (WS1-E10).
5. **A multi-user report still leaves fit-checking to each receiver (W4).** Each user auditor must check relevance, period coverage and its own complementary controls (WS1-E21).

Strongest counterevidence:
- The documented failure is too little review, including ignoring problems the specialist itself flagged (WS1-E05).
- When specialist work is opaque, auditors tend to do a shallow "comfort" review rather than rebuild it (WS1-E07, WS1-E26).
- In the one experiment found, a more specific explanation made reviewers spend more time, not less (marginal, p=0.09 one-tailed). It changed how they relied on the source, not how much effort they spent (WS1-E33).

Access limits:
- pcaobus.org and SSRN returned 403. US rule content comes from Federal Register and SEC documents instead.
- Five academic sources were read only as abstracts or search summaries.
- ISA texts came from the UK (FRC) and Australian (AUASB) conformed versions.
- I deliberately did not use one Griffith & Hammersley draft marked "do not quote or cite".

=== CONTENT FOR report.md ===
# WS1: Auditing and reliance on outside specialists and other parties' work

**Analogy status.** Everything here is an analogy to renewable-energy investment and credit diligence. Auditing has the producer → accountable receiver → opinion structure. The key difference: audit review duties are set by law and checked by inspectors. For an investment committee (IC) or credit committee, they come from internal policy, fiduciary duty and covenants. So W1 in audit is likely an upper-bound analog.

**Evidence strength.** Most items are standards, which show obligations, not compliance or effort. The only effort data are the PCAOB's own interim review (WS1-E08 to E10): self-reported, non-random sample, not causal. S10, S12, S13, S15 and S16 were read at abstract or summary level only. S11 is read partly through the PCAOB's quotations.

## RQ1: Why does review persist?

**W1: required work that does not depend on transparency (strong, standard-level).**
- **Responsibility can't be delegated.** The auditor has sole responsibility for the opinion and may not refer to an expert or a service auditor in an unmodified report (ISA 620 paras 3 and 14; ISA 402 para 21; WS1-E11, E19).
- **What must be evaluated.** Data, significant assumptions and methods, plus whether conclusions match the work performed (PCAOB AS 1105 App. A, AS 1210, AS 1201 App. C; ISA 620 para 12; ISA 500 para 8; WS1-E02, E13, E16).
- **Re-performance is mandatory.** Under ISA 610, the auditor keeps all significant judgements, does more of the work itself as judgement or risk rises, and "shall include re-performance of some of the work" (WS1-E17).
- **What sets the amount of work.** Risk of material misstatement, significance of the work, the producer's competence, and (PCAOB only) the company's ability to influence the specialist. Documentation transparency is not a factor. It changes how the duty is met, not whether it applies (WS1-E01, E03).
- **The producer itself is a gate.** The auditor must establish the producer's competence and objectivity before evaluating its content. A transparent output cannot satisfy this (IAASB 2026 amendments, WS1-E15).
- **Dividing responsibility is narrow.** Under PCAOB AS 1206 it is allowed only with another audit firm under the same rules, and the reliance must be disclosed in the report. Otherwise the lead auditor supervises and reviews the other firm's documentation (WS1-E24).

**W2: missing documentation causes extra work (the standards say so explicitly).**
- No description of tests and results in a service-auditor report means more user-auditor work (ISA 402 A37, WS1-E20).
- With no model description, the fallback is "using an alternative model" (WS1-E03).
- The auditor cannot rely on internal-audit work unless it was properly "documented" (WS1-E18).
- **Qualification:** opacity often leads to a shallower comfort or sufficiency review rather than rebuilding (WS1-E07, E26). So W2 may show up as hidden risk rather than hours.

**W3: rework from inadequate output.** This is a formally separate step under ISA 620 para 13: the auditor agrees further work with the expert or performs extra procedures, and a modified opinion is possible (WS1-E14). Specialist procedures find the most client problems (WS1-E32, abstract only). I found no public data on how often specialist output is inadequate.

**W4: adapting a multi-user report.** A Type 2 report serves several user auditors. Each must still evaluate relevance to its own assertions, period overlap and bridge periods, and its own complementary controls. Exceptions in the report don't automatically make it unusable (WS1-E19, E21). This supports P1.4 and P4.1.

**P1.6: institutions and comfort (interview evidence).**
- Auditors verify management's model piece by piece and depend on specialists to challenge assumptions (WS1-E25).
- They use specialists "for comfort, not insight" and shape specialists' work to fit their views (WS1-E26).
- They delete contrary content from specialist memos (WS1-E27).
- They limit specialist scope because of budget and client relationships (WS1-E29).
- Auditors and inspectors disagree about what counts as sufficient evidence (WS1-E31).

**How much extra effort the tighter rules added.** Most partners estimated under 1% of hours, with no fee increases. The main effects were coordination and documentation (WS1-E08). Specialist hours per engagement didn't change, but 2.3 percentage points more moved into planning (WS1-E10).

## RQ2: What producer information reduces receiver work?

These are mostly "may" provisions, so they show what regulators accept, not measured savings.
- **Model description:** can replace access to the model or building an alternative one (WS1-E03).
- **The producer's documented tests of source data:** reviewing them may replace re-testing (ISA 620 A39, WS1-E13).
- **Clear scope, standards applied, and errors or deviations encountered:** treated as signs of adequacy (A34, WS1-E13).
- **Tests performed and results, including no exceptions:** lets the auditor evaluate fit instead of re-testing (WS1-E19, E20, E22).
- **Who performed which checks:** treated as a substitute for rules limiting delegation (WS1-E23).
- **Source support attached to assumptions:** the audit team validates it on a test basis instead of re-deriving it (partner quote, WS1-E30).
- **Disclaimers and restrictions:** increase work, because extra procedures are "ordinarily" necessary (WS1-E04).

**Checks with no findings.** The IAASB requires the nature of the tests to be described even when nothing was found. It does not require sample sizes in that case, on cost grounds, and a significant minority of respondents disagreed (WS1-E22).

**Experiments.**
- **Griffith 2018 (abstract only):** a cue highlighting a pattern of aggressive assumptions improved judgments, but only when risk motivated auditors (WS1-E28).
- **Commerford & Holman 2022 (98 audit managers):** greater explanation specificity removed reliance differences between human and AI sources and increased time on task (marginal). There was no accuracy measure (WS1-E33).

**Producer response to receiver demands.** A valuation service provider supplied richer pricing information to meet auditors' new documentation demands. This is one commenter, with no economic data (WS1-E09).

## RQ3 (incidental)
- Earlier, more frequent auditor–specialist communication is linked to fewer inspection findings (correlational, WS1-E06).
- The new rules moved specialist effort into planning rather than removing it (WS1-E10).
- Integration into the receiver's workpapers can strip out contrary findings (WS1-E27).

## Strongest counterevidence
1. The documented failure is under-review, including ignoring issues the specialist flagged (WS1-E05).
2. Opacity tends to produce comfort-seeking rather than reconstruction (WS1-E07, E26).
3. More explanation took more time (WS1-E33).
4. Disclosure is deliberately limited on cost grounds (WS1-E22).
5. Required work does not depend on documentation quality, and re-performance is required regardless (WS1-E01, E17).
6. The added mandated effort was small, under 1% of hours (WS1-E08).

## Limitations
- Standards are not effort data.
- The PIR is regulator-authored, self-reported and non-random.
- Several academic sources are abstract-only.
- Primary PCAOB texts were blocked (AS 1210, AS 2601, AS 2605, adopting releases).
- I used UK and Australian ISA versions.
- The AICPA SOC 1 / AU-C 402 materials were not retrieved.

## Unresolved questions and what would settle them
1. **W2 versus W1 share:** engagement time records splitting mandated evaluation from reconstruction caused by missing documentation, or a comparison of engagements with and without model descriptions or source support.
2. **Do richer SOC 1 test descriptions (including sample sizes for no-exception tests) change user-auditor effort or detection?** An experiment or archival comparison.
3. **Does producer documentation reduce W3 or deficiency rates?** Data linking inspection findings to documentation (the PIR follow-up or comprehensive review, not located).
4. **Does a track record with a producer lower review over time** (ISA 620 para 8(d))? Panel data on repeated use of the same specialist.
5. **Do IC and credit policies impose re-performance-like W1 duties?** Actual policy documents (WS2).

=== CONTENT FOR search_log.md ===
# WS1 search log (2026-11-15, roughly 18:36–18:50 UTC)

## Successful
- **PCAOB specialists rulemaking.** WebSearch "federalregister.gov PCAOB Using the Work of an Auditor-Engaged Specialist…" led to the govinfo HTML of 84 FR 13442 (2019-06425), full text, and SEC 34-86270 (downloaded, not used substantively).
- **ISA 620.** The iasplus PDF link returned HTML (failed). Used FRC ISA (UK) 620 June 2016 instead. Also used the IAASB Jan 2026 basis for conclusions on the experts amendments (ifacweb blob).
- **ISA 402 and ISAE 3402.** The FRC landing page had no direct PDF, so I used AUASB ASA 402 (Dec 2023). The IFAC ISAE 3402 staff overview (2 pages) was used for context only. The ISAE 3402 basis for conclusions (IFAC) was full text.
- **ISA 610 and ISA 500.** AUASB compiled PDFs.
- **Other auditors.** SEC 34-95488 (2022).
- **PCAOB interim analysis (Release 2022-008).** curl is blocked on pcaobus.org, but WebFetch saved the PDF binary, which I converted locally.
- **Academic sources.**
  - Griffith et al. 2015, Griffith 2020 and Glover et al. 2019: IDEAS abstracts.
  - Griffith 2018: search excerpts plus the UW news article.
  - Boritz 2020 and Cannon & Bedard 2017: search summaries only.
  - Glover, Taylor & Wu 2017: full text from typeset.io (provenance uncertain).
  - Commerford & Holman 2022: full text from NHH.

## Unsuccessful or consequential
- **pcaobus.org:** AS 2601 WebFetch returned 403. AS 1210, AS 2605, AS 1105 App. A verbatim text and PCAOB spotlights/inspection observations after 2020 were not retrieved, so post-2020 deficiency patterns are unverified.
- **SSRN 3404297:** 403. **econbiz:** bot-protection block. **iasplus news:** empty.
- **Griffith & Hammersley 2019 VT draft:** downloaded but marked "do not quote or cite without permission", so not used.
- **Not searched for lack of time:** AICPA SOC 1 / AU-C 402 guide, Big 4 workpaper-review descriptions, Pentland 1993, Joe et al. 2017, the PIR follow-up interim analysis.
- **Implication for testability:** I found no public data that splits auditor time into mandated evaluation versus reconstruction caused by missing documentation. The distinction is set out in the standards, but publicly it remains a hypothesis.
