> Provenance note (coordinator): extracted verbatim by script (`scripts/extract_handbacks.py`) from R3B's final hand-back message. The harness asks subagents to return report .md content to the coordinator rather than write it. Temp IDs map to stable IDs via `01_Evidence/id_mapping.json`.

R3B is done. sources.json (11 sources) and evidence.json (21 items) are written in /home/user/Scratch/advisor_verification_research/03_Challenge_and_Followup/R3B_legal_reliance_boundary/. Both load cleanly with json.load. Every excerpt was checked by script against the downloaded source text. There are 11 independent evidence groups, all new to the register.

What R3B found about the boundary: a recipient may rely without re-checking only on content an accountable expert certifies, and only until a red flag appears (E03, E07). For everything else the recipient must investigate. That means targeted inquiry and checking against records, not re-performing the expert's work (E04, E09). Disclosing "procedures performed and findings" does not move the duty. It is evidence the recipient can cite, "insufficient by itself" (E08, E12, E13, E16). The strongest counterevidence to CL026: banks usually will not proceed on a comfort letter limited to procedures and findings, without negative assurance. That rests on a law-firm claim with no data (E15).

Access: pcaobus.org pages, the PCAOB 2026 proposal docket and the ISRS 4400 standard text were blocked. Justia and CourtListener were blocked; case texts came from the Caselaw Access Project instead.

# report.md

## R3B — Where legitimate reliance on outside work ends and independent investigation begins

**Scope.** This is doctrine and professional standards, not observed effort. None of the 11 sources measures how much time recipients spend or how many errors they catch. All IDs below are temporary R3B IDs.

### 1. Findings on the uncertainty

**(a) Expert status draws the line, not documentation quality.**
- Securities Act §11 has two standards:
  - For content an expert stands behind, the defendant only has to show no reasonable ground to doubt it (§11(b)(3)(C)).
  - For all other content, the defendant must show a "reasonable investigation" (§11(b)(3)(A)) (E01).
- BarChris held that only the consenting auditor was a statutory expert, and only for the audited figures.
  - The company's and underwriters' lawyers who drafted the prospectus were not experts.
  - Defendants could rely on the audit without re-checking it, but had to investigate everything else (E03).
- Implication: a well-documented advisor product that has no accountable, consenting expert behind it leaves the recipient's investigation duty intact.

**(b) Conditions that move the boundary.**
- *Red flags.* Reliance even on audited content "may not be blind." WorldCom treats any information that undermines confidence as a red flag, including public peer benchmarks. Whether one exists is a fact question, and no category of information can always be ignored (E07).
- *The recipient's own knowledge and role.*
  - A defendant who knew the facts could not "shut his eyes ... and rely on" the auditor (E05).
  - The director who drafted the document was held to a higher investigation standard (E05).
  - Rule 176 makes depth of investigation depend on role, access to information, and reasonable reliance on people whose duties gave them knowledge (E02).
- *Delegation.* The lead underwriter was bound by its counsel's failure to verify. Accountability stays with whoever delegated (E04).
- *Expert selection and competence (directors).* Under Brehm, reliance under §141(e) is presumed proper unless plaintiffs show:
  - no actual reliance, or bad faith;
  - advice outside the expert's competence;
  - careless selection of the expert;
  - a material gap so obvious that ignoring it was grossly negligent "regardless of the expert's advice" (E17).
  - An expert's omitted calculation, regretted in hindsight, did not by itself defeat reliance (E18).
- *Substance and a knowable basis.* In Van Gorkom, a 20-minute oral presentation was not a §141(e) "report." Reliance on a valuation is protected only if it was "reached on a sound basis." Had the directors informed themselves of the price's "source and derivation," they could not have relied on it in good faith (E19).
- *Contract.* Who may rely is set by reliance letters. In one renewable-energy RfP, the lenders' technical adviser's report goes to equity and mezzanine investors on a "non-reliance basis" (E21).

**(c) How much rework is mandatory (W1 vs W2).**
- WorldCom says explicitly that underwriters "are not being asked to duplicate the work of auditors." A reasonable investigation sits between "obtaining comfort letters ... and doing little more" and "having to re-audit" (E09).
- Without red flags, re-performing the expert's work is not legally required. What is required:
  - targeted inquiry using the recipient's own business expertise;
  - checking management's answers against records — BarChris held that asking questions without verification was insufficient (E04);
  - follow-up until satisfied whenever a red flag appears (E09).
- Two parts of the mandatory work persist whatever the advisor's transparency:
  - Recipients must decide whether the procedures are sufficient. AS 6101 says only the underwriter can make that call, because no authoritative standard exists (E12).
  - They must build a defensible record of their own process. The investigation must be done "even if ... futile" (E10), and comfort letters exist to help "develop a record of reasonable investigation" (E14).

**(d) Does disclosing "procedures performed and findings, including none" (CL026) change what the recipient must do?**
- *Legally, no.*
  - Comfort letters do not turn non-expert content into expert content.
  - Receiving them is "important evidence, but ... insufficient by itself" (E08).
  - AS 6101 forbids implying the procedures are sufficient for the underwriter's purposes (E12).
  - ISRS 4400 has the engaging party acknowledge that the procedures are appropriate, and states that an agreed-upon-procedures (AUP) report gives no assurance (E16).
- *In practice, it may lower the cost of the required steps.*
  - AS 6101 already requires procedures to be set out clearly, bans vague terms ("general review," "check," "test") unless the procedures are described, and lets the recipient ask for more (E13). This is the closest existing institutional version of CL026. Its stated purpose is to allocate responsibility, not to save effort, and no effect data were found.
  - A stated program is not proof of performance. In BarChris, the auditor's written program met professional standards, but steps were skipped and the review was "useless" in results (E06).

### 2. Strongest counterevidence
- **Recipients want a conclusion, not just a list of checks (E15, challenges CL026/P2.4).** Davis Polk says banks "usually" will not proceed with an offering if the comfort letter has procedures and findings but no customary negative assurance. A sophisticated recipient apparently treats the producer's accountable statement ("nothing came to our attention") as distinct from coverage disclosure. Limits: practitioner assertion, no data, and the firm has a stated policy position.
- **Users may misread assurance language (E16).** IAASB respondents worried that users do not understand "reasonable or limited assurance." Coverage disclosure could be read as assurance it does not give (a P2.3-type risk).
- **Transparency can enlarge the recipient's duty (E05, E07, E17, E18 — analyst inference).** Making omissions or conflicting data visible can make them "obvious" or a red flag, and so expand mandatory follow-up.
- **Doctrine can diverge from practice (E11).** WorldCom quotes commentators and an ABA committee saying the standard is "not possible" to meet in shelf offerings. Doctrine cannot be used to infer actual effort.

### 3. Unresolved points
- No source measures recipient time or error detection when outside work is relied on with versus without procedure-level disclosure. The legal sources describe what is required, not what is done.
- Whether lenders' and investment committees' credit policies separate expert-certified content (for example, an independent engineer's report with a reliance letter) from sponsor or counsel content, the way §11 does.
- Whether "findings-only" consultant reports (AUP-like) are accepted by credit committees, or opinions and negative assurance are required, as E15 suggests for underwriters.
- The 2026 PCAOB AS 6101 proposal (Release 2026-008) was not reviewed in primary form; the docket was blocked.
- The later Disney trial decisions (2005/2006), Software Toolworks (9th Cir.), and English-law reliance-letter cases were not reviewed.

**Observations that would settle these:**
- reviewer logs from lenders comparing time spent on expert-certified versus non-certified sections;
- credit-file documentation rules;
- lender acceptance or rejection data for vendor or findings-only diligence.

### 4. Transferability to renewable-energy investment and credit diligence
- **What carries over:**
  - The independent engineer's (IE) or energy-yield consultant's report with a reliance letter is the closest analogue to "expertised" content.
  - Sponsor models and counsel summaries are analogues of non-expertised content.
  - Red-flag triggers carry over: portfolio underperformance, curtailment data, peer benchmarks (E07).
  - Policy-driven duplicate work: some lenders insist on their own counsel (E20).
  - Duplicate work caused by low-quality output: descriptive vendor reports and restricted access to documents (E20). This is the part a traceable, evaluative product could plausibly reduce.
- **Consequential differences:**
  - Lenders and investors are not under §11. Their duties come from credit policy, banking supervision guidance (SR 26-2, interagency third-party risk management guidance, already in the register), fiduciary duty, and contract.
  - Delaware's gross-negligence standard (Brehm) is more forgiving than §11's.
- **Net for the thesis:**
  - Doctrine supports reducing *re-performance* (W2): it is not legally required absent red flags.
  - It does not support reducing *recipient judgment on sufficiency, red-flag follow-up, and record-building* (W1).
  - Coverage disclosure (X4) supplies inputs to W1. The evidence does not show it substitutes for an accountable producer conclusion.

# search_log.md

## R3B search log (2026-11-15, about 18:58–19:10 UTC)

**Statutes and rules**
- `curl https://www.law.cornell.edu/uscode/text/15/77k` → full text; extracted §11(b)(3) and (c). (S01)
- `curl` eCFR renderer API for 17 CFR 230.176 → full text. (S02)

**Case law**
- `curl` Justia for WorldCom, BarChris and Brehm → **blocked** (Cloudflare "Just a moment" challenge page).
- CourtListener API v4 search → **blocked** ("Authentication credentials were not provided"). CourtListener HTML → 403 (CloudFront).
- WebFetch of CourtListener citation URLs (/c/F. Supp. 2d/346/628/, /c/A.2d/746/244/) → empty content.
- WebSearch: "In re WorldCom ... 346 F. Supp. 2d 628 underwriters comfort letters red flags full text" → only case briefs and a Proskauer memo; not used as sources.
- WebSearch: "Brehm v. Eisner 746 A.2d 244 section 141(e) ... full text" → no opinion text.
- WebSearch: "Escott v. BarChris ... 283 F. Supp. 643 full text" → index pages only.
- **Worked:** Harvard Caselaw Access Project static JSON (static.case.law) for f-supp/283/0643, f-supp-2d/346/0628, a2d/746/0244, a2d/488/0858 → full opinions. (S03, S04, S08, S09) Note: the CAP OCR has minor artefacts ("20%" for 20½; "bebeves"); these were avoided in excerpts or flagged.

**Comfort letters and negative assurance**
- WebFetch pcaobus.org AS 6101 page → **403**.
- WebSearch: "AS 6101 ... 'cannot make any representations' sufficiency ... negative assurance" → found the PCAOB consolidated standards PDF and the Docket 058 proposal.
- `curl` of the PCAOB consolidated auditing standards PDF (FY on/after 2024-12-15) → **worked**; extracted AS 6101 (S05).
- `curl` PCAOB Docket 058 → small challenge page (**blocked**).
- WebSearch: "AU-C 920 ... negative assurance ... sufficiency of the procedures pdf AICPA" → AICPA text is behind a member login; Deloitte DART is a JavaScript app (not retrievable). AU-C 920 not reviewed; AS 6101 used instead (AU-C 920 is described as substantively derived from the same AU 634 source).
- WebSearch: "PCAOB proposed targeted amendments AS 6101 negative assurance 135-day November 2026" → Davis Polk update retrieved by curl (S06). PCAOB release itself not reviewed.

**Agreed-upon procedures**
- WebSearch: "agreed-upon procedures AT-C 215 ... sufficiency of the procedures" → only study aids; not used.
- WebSearch: "ISRS 4400 Revised ... pdf ifac" → the IRBA-hosted standard PDFs returned HTML block pages; the IFAC Basis for Conclusions PDF worked (S07).

**Reliance letters (M&A / project finance)**
- WebSearch: "reliance letter due diligence report lenders project finance independent engineer ... non-reliance" → Clifford Chance blog (S10) and EAIF Homa Bay lenders' technical adviser RfP (S11) retrieved. Brodies and Eversheds reliance-letter pieces were seen in snippets only and not used; R3C covers IE scopes.

**Implications for public testability**
- Doctrine and standards on the reliance boundary are fully public.
- No public source found measures recipient effort or detection under reliance versus investigation, or how often underwriters or lenders re-perform expert work.
- Model reliance-letter terms (LMA, IE standard forms) and English-law reliance cases were not found in open sources within the timebox.
