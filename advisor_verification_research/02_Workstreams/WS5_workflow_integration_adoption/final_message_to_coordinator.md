> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS5's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

WS5 SUMMARY

**report.md and search_log.md are not in my folder.** The harness blocked me from writing report .md files and told me to return the content instead, so I did not create either one. Both are below for you to save. sources.json (15 sources) and evidence.json (25 items) are written and pass JSON validation.

Counts: 15 sources, 25 evidence items, 14 independent evidence groups. The HBR workslop article shares an evidence group with the BetterUp blog.

Most consequential findings:
1. **Work moves to review rather than disappearing.** In Danish survey-plus-register data (about 25,000 workers), 35% of new AI-related tasks are quality review or compliance (E01). Accountants say they now check AI-drafted financial output (E03). Knowledge workers say their effort moves to checking, fitting output in and overseeing it (E04). Two government buyers' own evaluations agree (E10, E12).
2. **Saving time on one task does not reduce total hours.** Workers report saving about 3% of hours (1.6–1.9% in finance jobs), but recorded hours show no effect, ruling out anything above 2% (E02). UK DBT found no productivity gain, and its time savings shrank sharply once discarded outputs and AI-created extra work were counted (E08).
3. **Building decision materials is not reliably "easy" to speed up.** In DBT's observed tasks, slides were made faster but scored 1.5 vs 5 on accuracy, and checking slide decks took longer (E09, E10; tiny samples). Summarising got both faster and better.
4. **Rules hold the reviewer's work constant.** In PCAOB staff outreach (stated policies), firms said reviewers apply "the same level of diligence" to GenAI-assisted work and review policies were unchanged (E15). Allen & Overy (A&O) kept lawyer review after firm-wide rollout (E19). Moonfare says the investment committee's (IC's) decision stays human (E20).
5. **Buyers set their own formats, and adoption does not prove less effort.** Entergy requires native PVsyst files built to its own spec (E22). DBT had 72% satisfaction but no productivity evidence (E11). Australia's Treasury justified the purchase on a 13-minutes-a-week break-even without measuring savings (E14).

**Strongest counterevidence:** E02, E08, E09/E10, E12.

**Gaps:**
- No public study measures end-to-end IC, credit or board-pack workflow time.
- No source tests integrating traceable outputs specifically.
- Reformatting effort for board or IC materials is never quantified.

**Access:** HBR paywalled. PwC directors-survey pages returned 403. Morgan Stanley returned 503. The board-pack sources are vendor-linked and only partly accessed.

---
FULL CONTENT FOR report.md

# WS5: Workflow integration and buyer adoption

## Bottom line
Public evidence does not show that putting outside or AI-generated analysis into the recipient's work reduces their total work end to end. The consistent pattern is that work moves:
- Drafting and information gathering go down.
- Checking, quality assurance, fitting output in and adapting it go up.

The net effect depends on output quality and the type of task. Accountable settings explicitly keep the reviewer's diligence unchanged.

No source measured end-to-end time for an IC, credit or board-pack workflow. No source tested traceable or structured outputs built into decision materials. Both are gaps in the evidence, not evidence that there is no effect.

## RQ3: Does integration remove work or move it?

**1. Review and integration work is created (supports P3.2).**
- In the Danish data, 35% of new AI tasks are oversight. "AI Integration" is the most common new-task type, at about 26% (E01).
- Accountants name reviewing AI financial output as a new task (E03).
- Knowledge workers (n=319) say effort moves to checking and integrating. Evaluation shows the least effort reduction, 55% (E04).
- Australia's Treasury says checking for accuracy and fit with the audience was sometimes slower than doing the work manually (E12).
- At DBT, quality-assurance time went up in 30% of slide-deck cases and 29% of code-review cases (E10).
- The workslop survey reports 1 h 51 min per low-quality AI deliverable, about 20 minutes more than if the sender had done it. This is self-reported and vendor-run (E07).

**2. Faster tasks do not mean fewer total hours (challenges P3.1).**
- Danish workers report saving about 3% of hours, and 85% move the saved time to other tasks. Hours show no effect above 2% (E02).
- DBT found no productivity gain after its adjustments. Data analysis fell from 2.0 to 0.6 hours saved per task, and presentations from 0.8 to 0 (E08).

**3. Drafting, reformatting and judgment can be separated, but reformatting is not reliably easy (qualifies P3.3).**
- Summarising took 12:37 vs 41:34 and was more accurate. Treasury's gains were in admin tasks (E09, E13).
- Slides took 10:47 vs 18:30 but scored 1.5 vs 5 on accuracy. Excel analysis was slower and less accurate (E09).
- Moonfare says preparation shrinks while the IC decision stays human (E20).
- A vendor claims 50–70 analyst hours saved on a memo, with no method given (E21).

**4. Governance caps cuts to W1 (supports P1.1).** PCAOB firms keep review diligence unchanged (E15), and A&O requires careful lawyer review (E19). Any cut must come from W2, W3 or W5.

**5. Adaptation and reformatting costs exist but are not quantified (qualitative support for P1.4 and P1.5).**
- Users fit output to organisational guidelines "in form and content" (E05).
- Board materials follow each organisation's templates. In 71% of organisations the corporate secretary contributes directly (E18).
- 63% of packs are rated "Weak/Poor", averaging 220–226 pages (E17; vendor data).
- No source measures preparation or reformatting time. The ledger anchor stays plausible but unquantified.

**6. Control and the client's own capacity shape uptake.**
- Letting people adjust a model raised its use from 32% to 73–76% and improved performance (E25; lab study).
- In a consulting field experiment, about half of adopted practices were later dropped, mainly because plant managers left or directors lacked time (E23).

**7. Trust confound.** Higher trust in AI goes with lower perceived checking effort (Evaluation beta −0.24, p<0.001) (E06). Shorter review time may mean complacency rather than efficiency, so detection has to be measured alongside time.

## Secondary RQs
- **RQ4 (customer-specific implementation):** Entergy's native-file and Scope Book requirement (E22), board templates (E18) and guideline alignment (E05) support P4.1 on stated requirements. The resulting effort is not measured.
- **RQ5 (repeatability):** Indirect only. Gains decay when key client staff turn over (E23).
- **RQ6 (buying, renewal, abandonment):**
  - Satisfaction and productivity diverge (E11).
  - Treasury used a low break-even, and usage declined when expectations were not met (E14).
  - A&O adopted without claiming less review (E19).
  - Firms that received consulting bought more consulting afterwards (E24).
  - No renewal or pricing evidence tied to reduced verification effort.

## Strongest counterevidence
E02, E01, E08, E12, E09/E10, E15.

## Limitations
- Mostly generic AI assistants rather than advisor deliverables, so findings carry over by mechanism only.
- Mostly self-reported.
- The DBT observed tasks have tiny samples.
- The private-equity sources are one blog and one vendor case study.
- The board-pack sources are vendor-linked and only partly accessed.

## Discriminating observations needed
1. Full-workflow time logs (advisor report → memo → reviewer edits → IC rework) on matched deals, with and without integration.
2. Activity sampling of the share of analyst hours spent fitting third-party reports to IC templates.
3. A reviewer experiment with seeded errors, comparing drafts with and without source links and scope statements. Measure time, detection rate and false reassurance.
4. Whether checking time rises for the financial sections and model outputs of IC memos.
5. Renewal, non-renewal or pricing records tied to measured effort, for example DBT's pending value-for-money assessment.

---
FULL CONTENT FOR search_log.md

1. Humlum & Vestergaard: NBER w33777 PDF via curl worked. It is the March 2026 revision, retitled.
2. Lee et al., CHI 2025: Microsoft Research PDF worked.
3. Workslop: HBR article body is paywalled (WebFetch returned only the header). The BetterUp blog was retrieved; its sample size is inconsistent (1,004 vs 1,150). A university-hosted copy of a follow-up HBR article was not used because its licensing is unclear.
4. UK DBT and Australian Treasury Copilot evaluations: PDFs worked. Press figures like "35 minutes longer" are not in DBT's Table 5 and were not used.
5. Board packs:
   - Search found the Board Intelligence blog (vendor) and the Society for Corporate Governance (SCG) blog.
   - NACD 2024 figures appear only on Board Intelligence pages, so they were not used.
   - PwC 2026 directors survey ("82% see opportunities to improve materials", search snippet only): pwc.com returned 403, so this is unverified.
   - Diligent/Nasdaq was not searched (time).
   - UNSUCCESSFUL: no survey quantifying preparer hours or reformatting of board packs.
6. IC-memo AI case studies: vendor claims only (V7, Binocs, Agentman, Brownloop). Binocs was fetched.
7. UNSUCCESSFUL: no independent before/after measurement of end-to-end IC or credit-approval cycle time. P3.1 is not currently testable from public sources in this domain.
8. Buyer accounts:
   - Morgan Stanley Debrief press release returned 503. The Celent "30 min saved" figure was not verified or used.
   - A&O, Moonfare and PCAOB worked. The PCAOB PDF came via WebFetch's saved binary and was extracted with pdftotext.
9. Procurement:
   - Entergy Appendix D retrieved.
   - NY Green Bank and CT Green Bank lender's-engineer RFPs were not retrieved (time).
   - UNSUCCESSFUL: no investor-side RFP found that requires advisor deliverables in IC-template format.
10. Bloom et al., NBER w24249: worked.
11. Dietvorst et al.: core.ac.uk returned HTML; the Wharton preprint worked.
12. MIT NANDA "GenAI Divide": the mirror returned not found. Not used (weak method anyway).

Downloads are in `/tmp/claude-0/-home-user-Scratch/896551fc-74fd-5092-857d-f83fd4afd7e5/scratchpad/downloads/WS5/`. Files written to `/home/user/Scratch/advisor_verification_research/02_Workstreams/WS5_workflow_integration_adoption/`: `sources.json` and `evidence.json`.
