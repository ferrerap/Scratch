> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS5's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

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
