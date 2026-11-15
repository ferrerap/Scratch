> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from WS2's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

**WS2 summary.** Three of the four files are written and the two JSON files validate. The harness blocked me from writing `report.md` ("Subagents should return findings as text"). I did not work around the block, so the full report text is below the summary for you to save as `report.md`.

**Counts:** 19 sources, 28 evidence items, 18 independent evidence groups (S03 and S04 are one OCC regulatory package).

**Most consequential findings:**
1. **What review can't remove is owning the decision and vetting the advisor, not redoing the analysis.**
   - OCC s.939A guidance lets banks hand "much of the analytical work" to third parties, but "management may not delegate its responsibility for decision-making" (WS2-E06).
   - The same rule requires the bank's own evidence determination and records (E08).
   - SR 26-2, which replaced SR 11-7 in April 2026, keeps vendor products under model risk rules even when code or data are withheld (E01, E02).
   - EU project-finance rules require both an independent expert check and the lender's own cash-flow assessment (E10).
2. **Lenders and rating agencies always re-cut IE output into their own cases (W4).** Fitch uses its own base case, one-year P90 rating cases and peer-set haircuts (E12, E13). A perfectly traceable IE report would still be adapted. No source tested whether better-structured inputs reduce the reconstruction work (W2).
3. **There is a real accuracy reason to discount yield forecasts in renewables (W3).** About 350 US solar assets underperformed their P50 estimates by 5–13% over 2011–2020 (E14; secondary source). The bias showed up in outcome data; citations alone would not have revealed it.
4. **No source measured whether IC-memo integration reduces total work (RQ3).**
   - Memo templates are nearly unique to each firm: 86% of 54 surveyed organizations use templates (E22).
   - Vendor and survey accounts describe effort moving from assembling the memo to editing it, not disappearing (E21, E23).
   - The survey authors found zero peer-reviewed articles on investment memos (E24).

**Strongest counterevidence:** DOE's Inspector General found the Loan Programs Office relied on borrower-paid advisors "as essential components" of loan review. It could identify the engineering advisors for only 3 of 18 projects reviewed (E26). The failure there was too little scrutiny of who produced the analysis, not too much review. Separately, Fitch's adjusted case for one project was conservative: actual output beat it for seven straight years (E13).

**Access limits:**
- KBRA and S&P criteria are behind logins or blocked. The KBRA finding was seen only through search summaries (S10).
- I could not retrieve the current Fitch criteria. The ESMAP slides and the World Bank and NY Green Bank IE scopes returned 403 or bot pages.
- Brehm v. Eisner could not be retrieved.

---

# report.md (for WS2_investment_credit_IC/; write was blocked, please save)

# WS2: Investment, credit and investment-committee (IC) workflows, including renewable project finance

Run date: 2026-11-15. Files: `sources.json` (19 sources), `evidence.json` (28 items), `search_log.md`.

Most of the evidence is primary regulation or guidance, plus rating-agency methodology. There is one procurement scope (S11), one regulator audit (S17) and one survey (S15). Practitioner and vendor accounts are weaker.

I found no study that measures how recipient work splits across W1–W5, or the end-to-end effect of integration.

## RQ1: What do lenders and committees keep doing, and why?

**1. Owning the decision is formally required and cannot be handed off (W1).** The obligation attaches to the decision and to vetting the advisor, not to re-performing the analysis.
- OCC guidance lets banks rely on third parties for analysis, but not for the decision. Banks must check that advisors are independent and qualified (E06).
- The rule requires the bank's own evidence determination and records regardless of how good the outside analysis is (E08).
- SR 26-2:
  - keeps vendor products under model risk rules even when they are opaque (E01);
  - defines "effective challenge" by the challenger's independence and standing (E02).
- Interagency third-party guidance: using a third party does not reduce responsibility "to the same extent as if" the work were done in-house (E09; analogy).
- EBA project-finance rules require an independent expert to verify costs, plus the lender's own cash-flow assessment (E10).
- Delaware s.141(e) protects good-faith reliance on experts chosen with reasonable care (E18).

So P1.1 is supported, but in a qualified form. Reconstruction is not mandated. Traceability could lower the cost of meeting these duties without removing them.

**2. Adapting to house criteria (W4) is built into the process.**
- Fitch base case (0–10% energy adjustment) and rating case (one-year P90, availability and O&M stresses, technology-specific DSCR thresholds) (E12).
- Fitch's 2024 rating action uses a 2% haircut "in line with peer projects" and a P99 test (E13).
- SR 26-2 treats overlays on vendor output as normal, with documentation required (E03).
- In M&A, a vendor due-diligence report's recipient may have "different interests and views of materiality" (E20).
- A CDFI lender benchmarks assumptions to "current market ranges" (E16).
- What an advisor can change is whether the receiver has to rebuild inputs before applying its haircuts: exceedance tables and adjustable inputs. That is the W2-vs-W4 boundary, and no source tested it.

**3. Discounting because forecasts are wrong (W3).**
- About 350 US solar assets ran 5–13% below P50 over 2011–2020 (E14).
- KBRA's 70 rated deals were "rarely" at P50 (E15; seen only as a lead).
- This is rational discounting, not ritual. But the Fitch Topaz case was conservative: output beat it for 7 years (E13). Haircuts alone do not prove advisor error.

**4. Missing evidence (W2) is acknowledged but not measured.**
- SR 26-2 expects code, data or methodology may be withheld (E01).
- FDIC examiner procedures list the vendor evidence that makes a product reviewable (development evidence, testing, limitations, assumptions) and also list the bank's own sensitivity, benchmarking and outcome checks (E05).
- OCC ties more frequent review to unavailable data (E07).

**5. Counter-pattern: too little scrutiny of who produced the analysis (E26).**
- The DOE Loan Programs Office relies on borrower-paid advisors drawn from a small pool.
- It could identify the engineering advisors for 3 of 18 projects and the marketing or financial advisors for 0 of 18.
- Relying on advisors to self-report conflicts "creates a blind spot".
- Knowing who produced an analysis is a different need from tracing its evidence.

## RQ3: Integration into IC memos

- In the Addepar/Stanford survey of 54 organizations:
  - 97% use memos; 78% of those require memo completion and review before investing;
  - 86% use templates, and the template is "practically never the same for any two investors";
  - writing plus review takes about 2 months on average (E22).
  - So integration work (W5 plus W4) is specific to each customer (P4.1, against P5.1).
- Respondents want to automate filling memo fields so writers do only "higher-order" work (E23). This supports P3.3, but as a stated preference only.
- The same study flagged memos written by external consultants as a possible governance failure (E23).
- An AI memo vendor says the job "shifts from assembling the memo to editing it", with click-through citations and "days to hours" turnaround, unquantified (E21). That describes relocation (P3.2) of drafting work, not judgment.
- A job posting bundles memo drafting with diligence work (E28).
- A practitioner says confirming a vendor due-diligence report is easier than doing the work from scratch (E19), but gives no numbers.
- **RQ3 bottom line:** no evidence either way on whether end-to-end work falls.

## Incidental (RQ2, RQ4, RQ6)

- **RQ2:** SEC Rule 15Ga-2 requires disclosure of the criteria and coverage of third-party due diligence (E27). This is a mandate; there is no outcome data. A model-audit firm claims that clear scope and assurance level make opinions "bankable", and warns that LLMs give "plausible yet unreliable" spreadsheet logic (E25).
- **RQ4:** generative and agentic AI are outside SR 26-2's scope (E04).
- **RQ6:** one RFP asks for per-project pricing and weights technical expertise at 40% against cost at 20% (E17).

## Counterevidence

1. The core that can't be removed is decision ownership and advisor vetting (E06, E08, E10, E18). Adaptation (W4) is criteria-driven (E12, E13), so the reducible W2 share may be small.
2. Haircuts persist even when forecasts are conservative (E13).
3. Correctness problems were found through outcome data, not traceability (E14).
4. The observed failure was over-reliance, not over-review (E26).
5. Integration accounts show work being relocated, not removed (E21, E23).

## Limitations

- Most items are obligations or methodologies, not observed behaviour.
- Rating criteria are dated or behind logins.
- The kWh source is secondary and does not say whether the P50s came from lender IEs or sponsors.
- There are no named buyer accounts.
- Brehm v. Eisner was not retrieved.

## Observations that would settle the open questions

1. Task-time and think-aloud logs of credit analysts reviewing the same IE report with and without exceedance tables, loss breakdowns and model inputs. This would separate W2, W4 and W1.
2. End-to-end timing from report receipt to IC approval, plus the number of IC follow-up questions and the errors caught, before and after integration. This separates trust from appropriate reliance.
3. Whether lender haircuts differ by IE provider based on track record.
4. LPO and green-bank corrective actions after DOE-OIG-25-32.
5. Deals with versus without reliance letters, compared by the scope of extra work lenders commission.

Files are in `/home/user/Scratch/advisor_verification_research/02_Workstreams/WS2_investment_credit_IC/`:
- `sources.json`
- `evidence.json`
- `search_log.md`
- `report.md` is not there yet; save the text above.
