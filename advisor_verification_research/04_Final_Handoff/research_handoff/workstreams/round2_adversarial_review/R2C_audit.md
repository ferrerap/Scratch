> Provenance note (coordinator): verbatim final hand-back of Reviewer C auditor (R2C), saved by `scripts/save_handback.py`. Subagents return narrative as text per harness convention (see run_log D08/D09).

# R2C audit summary (Reviewer C)

Structured findings are in `/home/user/Scratch/advisor_verification_research/03_Challenge_and_Followup/R2C_audit_findings.json` (it loads cleanly with `json.load`): 25 findings (R2C-01 to R2C-25; 2 high, 15 medium, 8 low) and 23 `verified_ok` entries. I did not edit the registers. Downloads are in `/tmp/claude-0/-home-user-Scratch/896551fc-74fd-5092-857d-f83fd4afd7e5/scratchpad/downloads/R2/`.

## Overall reliability

The register is accurate at the level of individual numbers. I re-checked the statistics the synthesis is most likely to lean on against the original documents. Every one I could retrieve matched the register exactly (`verified_ok`):

- **Si et al. 2024:**
  - accuracy 0.74 vs 0.73, p=0.32
  - time 2.53 vs 1.01 min per claim
  - when the explanation was wrong: 0.35 vs 0.49 vs 0.54
- **Liu 2023:** 51.5% / 74.5%.
- **SymGen:** 20% less time; accuracy 80.83 vs 80.00.
- **HoT:** 47.26 s vs 62.38 s; accuracy 54.83 vs 72.21 when the model was wrong.
- **Vasconcelos Study 2:** Table 3 values.
- **METR:** +19%; forecasts -24% / -20%; 136 vs 110 issues.
- **Magesh:** 17–33%; 202 queries.
- **Ding:** 9.77% of cited answers checked; F(2,3037)=10.23.
- **Wu:** ~50–90% of responses not fully supported.
- **Humlum & Vestergaard:** effects above 2% ruled out; 12% (5 pp + 8 pp) and ~18% new workloads; 35% quality-review/ethics share; ~3% time savings.
- **UK DBT Copilot:** Table 5, Table 6, 32% response rate, 72% satisfied, NPS 31.
- **PCAOB 2022-008:** majority of 31 partners put added time below 1% of audit hours; no fee increases; +4.8 / +10.5 pp; +2.3 pp planning shift.
- **Grossman & Cormack 2011:** Table 7 (76.7/59.3 recall, 84.7/31.7 precision); 1.9% of documents reviewed.
- **Addepar/Stanford:** 54 organisations; 97% use memos; 78% of those require review; 86% use templates.
- **DOE-OIG-25-32:** 3 of 18; more than 300 contractor staff.
- **Kronz 1999:** 86/6171 (1.4%).
- **Manion 2008:** 2.3% major disagreements, 1.2% management change.
- **Lu 2012:** 72/52/11/13%; odds ratios 31 / 9.0 / 0.71.
- **Jabbour 2023:** all intervals. The Europe PMC abstract confirms the values the summarizer relayed.
- **Pew:** 8% vs 15% link clicks; 1% clicks inside the AI summary.
- **Deloitte/DEWR quotation:** verbatim, attributed to DEWR Secretary Natalie James; $97,587 of $440,000.

The **Commerford question is settled (R2C-22).** SRC017 (Commerford & Holman: memo specificity × source, 98 audit managers) and SRC105 (Commerford, Dennis, Joe & Ulla, JAR 2022: source × objectivity of management's inputs) are distinct experiments. They share a lead author and a paradigm, so treat them as two studies from one research program, not as replications. The `_flagged_for_audit` note can be closed.

**Could not re-check (sites blocked, not bypassed):**
- Dell'Acqua/BCG: the HBS PDF returns a block page.
- Fitch Topaz via MarketScreener: "Access Denied".
- PV Tech / kWh Analytics: HTTP 403.
- ACS Information Age: Cloudflare challenge.

The pcaobus.org interim report did download with curl, so the brief's general statement that pcaobus.org blocks scripted access did not hold for this file.

The problems are not invented numbers. They are in four places: how items are **labelled**, how they are **counted**, how they are **framed**, and which arms are **reported**. Several of these could change the balance of a proposition.

## Systematic problems

**1. Item counts are presented as weight of evidence (R2C-24, R2C-23).** The digest's n per proposition counts evidence items, not independent evidence groups:

| Proposition | Items | Distinct evidence groups |
|---|---|---|
| P1.1 | 43 | 33 |
| P2.1 | 21 | 17 |
| P2.2 | 19 | 15 |
| P2.3 | 19 (13 "supports") | 15 (9 "supports") |
| P3.2 | 16 | 14 |
| P2.5 | 11 | 9 |
| P3.4 | 2 | 1 |

The causes are cross-workstream duplicates of the same finding:
- Vasconcelos: EVR147 = EVR186, and they carry different relationship labels (R2C-02).
- Workslop survey: EVR122 = EVR164 (R2C-03).
- Dietvorst: EVR140 = EVR152, and these are the only two items under P3.4 (R2C-04).
- Schwarcz 2025: EVR065, an abstract-only item with unverified figures from a search summary, conflicts with EVR114, which was read in full (R2C-05).

P1.1's "supports" pile is mostly standards and regulations. They show an obligation to review exists; they do not show it is the dominant driver of effort. They also do not show it would persist regardless of transparency: several standards scale required effort with evidence quality (R2C-23).

**2. Relationship labels that misstate the source against the named proposition.**
- **R2C-06, DOE-OIG (EVR059):** labelled "challenges" its own P-NEW, which it actually supports. Its text also drops that the 3-of-18 figure refers to advisors working for *prospective borrowers*, so it reads as if LPO could not identify its own advisors.
- **R2C-09, Kronz/Manion (EVR209/EVR210):** labelled "supports" P1.3 ("rework is a major driver"). Second opinions changed diagnoses in only 1.4–2.3% of referred cases, which better fits review driven by policy and consequences (P1.1) than rework as a major driver.
- **R2C-10, Grossman & Cormack (EVR074):** labelled "supports" P1.6, but the study never observes *why* manual review persisted.
- **R2C-11, DBT (EVR123):** labelled "challenges" P3.1, although the self-reported diaries show positive adjusted time savings and the design has no counterfactual. "Qualifies" is accurate. The per-task sample sizes the report gives are missing; some cited rows rest on n=14–22.
- **R2C-13, Si (EVR091):** labelled "challenges" P2.1, but the time contrast is sources vs LLM explanations, not sources vs nothing. The no-evidence baseline time is not reported.

**3. Causal or measurement overclaims.**
- **R2C-07 (high), Humlum (EVR116):** the analyst inference turns self-reported new-task categories from chatbot *users* into "large-sample evidence that AI output adds review work for recipients". The 35% "AI Quality Review + Ethics" category includes teachers detecting AI-written homework. The large sample belongs to the administrative-data part of the paper; the new-task shares come from a survey.
- **R2C-08, METR (EVR141):** labelled "supports" P3.2 (effort is shifted, not removed). The study measures total time, which the authors attribute to several factors, and the confidence interval is not recorded.
- **R2C-15, PCAOB +2.3 pp planning shift (EVR010):** the source itself says the shift is "consistent with a broader shift" of audit hours to earlier phases, i.e., not attributable to the rule. The register omits that sentence.
- **R2C-19, Lu 2012 (EVR213):** a retrospective single-centre study tagged as supporting *end-to-end* work reduction (P3.1), though it measures only repeat imaging.
- **R2C-25, WS1 report:** headlines "missing documentation causes extra work" on the strength of standards that only *prescribe* extra procedures.

**4. Selective reporting (R2C-01, high).** Dell'Acqua/BCG appears only through its outside-the-frontier arm (correctness fell). The register has no item for the paper's main inside-the-frontier gains; a search of evidence.json finds no hit for either. This tilts P1.3 and P3.2 toward the disconfirming reading. I could not re-retrieve the paper, so the EVR144/145 figures are also unverified in Round 2.

**5. Transferability statements (R2C-16).** In 35 of 217 transferability fields a keyword scan finds no stated difference, limitation or verification need. Some are actively overconfident:
- EVR039: "Directly transferable principle".
- EVR045: "Core mechanism transfers directly", resting on 2012 Fitch conference slides.
- EVR186: "Strongest mechanism-level support", for a crowdworker maze task.
- EVR086: treats a design guideline as evidence of an effect.

**6. Access status and denominators.**
- Source-level and item-level access labels disagree after merging. SRC046 should be "partial", since its counts were read through a fetch tool (R2C-17).
- The renewable-domain figures most likely to be quoted (Fitch Topaz DSCRs and ~7% overperformance; kWh Analytics 5–13% underperformance vs P50) rest on fetch-tool summaries of secondary republications that could not be re-checked (R2C-18). They should not be headline numbers until the originals are obtained.
- Missing denominators:
  - Liu's r = −0.96 is computed over four systems (R2C-12).
  - Si: 16 crowdworkers per condition (R2C-13).
  - SymGen: n=60 annotators, with no significance tests (R2C-14).
  - Vasconcelos: its intervals are Bayesian credible intervals, not confidence intervals (R2C-20).
- **R2C-21, Deloitte/DEWR:** the article also reports that Finance learned of the errors only through media reporting. The register omits this; it matters for whether recipients verify at all.

## Most consequential corrections, in priority order

1. **Count by evidence group.** Add a distinct-evidence-group column to the digest and mark the duplicates (EVR147, EVR164, EVR152; EVR065's figures superseded by EVR114). P3.4 should be described as resting on one lay-forecasting study.
2. **Restore the missing BCG arm.** Add the inside-the-frontier result and note that the outside-frontier task was built so GPT-4 would give a plausible wrong answer.
3. **Reword Humlum (EVR116/EVR118).** These are self-reported new tasks among users, including policing other people's AI use. Change the label to "qualifies".
4. **Relabel:**
   - EVR059 → "supports", with the borrower-side wording fixed
   - EVR209/EVR210 → "qualifies" for P1.3
   - EVR123 → "qualifies"
   - EVR141 → "qualifies"
   - EVR213 → "qualifies"
   - EVR074 → "qualifies"/"contextual"
   - EVR091 → "qualifies"
5. **Treat the renewable-domain figures (EVR046/EVR047) as unverified secondary numbers** until the original Fitch and kWh Analytics documents are obtained.
6. **Split P1.1** into "an obligation exists" (well supported) and "obligation is the dominant driver of effort" (not directly tested).

## What would change my assessment

- If someone with access to the full Dell'Acqua paper confirms the inside-frontier figures and the outside-frontier arm is shown in context, R2C-01 drops to low.
- If the original kWh Analytics and Fitch documents confirm the figures, R2C-18 is resolved.

None of the verified traceability experiments involves professionals reviewing an advisor's report. The traceability conclusions therefore remain mechanism-level analogies, however accurately the numbers are transcribed.
