# Advisor Verification Research — Shared Instructions (all workers read this)

Run date: 2026-11-15. Coordinator: main session. This file is the common brief for every research worker.

## Objective
Investigate whether better evidence traceability and workflow integration can reduce the work accountable professionals perform when evaluating and using an outside advisor's analysis.

Working thesis (a HYPOTHESIS, not a finding): an outside advisor supplies analysis to a client who retains decision authority and bears consequences. The client may reconstruct, verify, adapt, and incorporate that analysis before relying on it. Products that preserve inspectable evidence, assumptions, coverage, and conclusions might reduce avoidable reconstruction while preserving the client's independent judgment. Integration into decision materials (e.g., an investment-committee memo) might add further value. Commercial extensions (customer value -> willingness to pay -> supplier margins -> repeatability) are SEPARATE hypotheses; do not assume they follow.

You are collecting evidence that SUPPORTS, CHALLENGES, or QUALIFIES the thesis. Disconfirming evidence is as valuable as supporting evidence. Do not argue for a side.

## Research questions
- RQ1 — Why does review persist? What work do recipients of outside analysis retain, repeat, or reconstruct, and why? Distinguish formal obligations, organizational policies, rational verification, lack of trust, poor output quality, missing requirements, downstream adaptation.
- RQ2 — What makes verification less costly without making it worse? Do sources, provenance, explicit assumptions, coverage information, or structured evidence reduce review effort while preserving or improving detection of material errors/omissions? Distinguish real verification improvement from increased trust/satisfaction/acceptance.
- RQ3 — Does workflow integration add distinct value? Evidence that incorporating advisor outputs into the recipient's decision process reduces additional work rather than shifting review effort elsewhere. Distinguish drafting, reformatting, policy application, decision preparation, substantive judgment.
- Secondary (only when a credible connection appears): RQ4 determinants of customer-specific implementation; RQ5 determinants of repeatable vs labor-intensive delivery; RQ6 evidence linking these benefits to buying, renewal, pricing, supplier economics.

## Required distinctions
Five sources of recipient work — keep separate, tag each evidence item with which it concerns:
- W1 required independent judgment / governance review
- W2 avoidable reconstruction from missing evidence or opaque reasoning
- W3 rework from inaccurate or incomplete advisor output
- W4 adaptation to client-specific policies or investment criteria
- W5 reformatting and integration into downstream decision materials

Explanation/traceability concepts — evidence about one is NOT evidence about another:
- X1 persuasive AI-generated explanations
- X2 faithful explanations of a system's operation
- X3 traceability to original evidence (citations, source links, provenance)
- X4 visibility into scope, checks performed (incl. checks with no findings), omissions, uncertainty
- X5 actual correctness and completeness

Also distinguish: direct evidence vs analogy; observed behavior vs stated preference; causal estimate vs correlation; time savings vs quality improvement; greater trust vs appropriate reliance; user productivity vs supplier profitability; individual-task vs end-to-end workflow performance; absence of evidence vs evidence of absence.

## Proposition catalog (use these IDs in `proposition_tested`; add `P-NEW: <text>` if none fits)
- P1.1 Retained review is substantially driven by formal obligations/governance (required independent judgment) that would persist regardless of advisor transparency.
- P1.2 A material share of recipient review is avoidable reconstruction caused by missing evidence, opaque reasoning, or unclear scope.
- P1.3 Rework due to inaccurate/incomplete advisor output is a major driver of review.
- P1.4 Adaptation to recipient-specific policies/criteria is a major driver of retained work.
- P1.5 Reformatting/integration into downstream decision materials is a material component of retained work.
- P1.6 Review persists due to accountability pressure, comfort/legitimacy ("ritual"), or distrust beyond rational verification needs.
- P2.1 Access to sources/provenance (traceability) reduces verification time/effort.
- P2.2 Traceability/structured evidence preserves or improves detection of material errors/omissions.
- P2.3 Explanations/citations increase trust/acceptance without improving (or while worsening) error detection.
- P2.4 Visibility into scope, checks performed (incl. no-findings), omissions, and uncertainty improves appropriate reliance.
- P2.5 Citations/traceability do not guarantee correctness or completeness.
- P2.6 AI-generated rationales may be unfaithful to the system's actual operation.
- P3.1 Integrating advisor output into the recipient's decision materials reduces total recipient work end-to-end.
- P3.2 Integration/AI assistance shifts review effort elsewhere rather than removing it.
- P3.3 Drafting/reformatting is separable from substantive judgment and is the part most amenable to reduction.
- P3.4 Ability to adapt/modify/integrate outside analysis increases its uptake and appropriate use.
- P4.1 Customer-specific implementation needs are driven by heterogeneous policies, criteria, data, and governance.
- P5.1 Delivery repeatability rises with standardized evidence formats/standards and falls with bespoke judgment.
- P6.1 Reduced recipient effort translates into buying, renewal, pricing power, or supplier economics.

## Scope
Start with investment/credit decisions; auditing and reliance on outside specialists; legal review; engineering/technical review. Use medicine or other high-stakes settings when the mechanism is relevant, and assess differences in accountability, regulation, task structure, expertise, error consequences. Favor analogies with a clear producer -> receiving professional -> decision authority -> consequence-bearer structure. Do NOT treat every human-AI study as an advisor-client study. Out of scope unless they directly test a core mechanism: market sizing, project volumes, interconnection timelines, broad AI-adoption statistics, generic productivity commentary, TAM, revenue projections.

## Source rules
Prefer original research, primary professional standards, buyer-authored material, procurement documents/actual scopes of work, detailed workflow descriptions, attributable practitioner accounts, evidence of actual adoption/purchase/renewal/rejection/abandonment. Also eligible: podcast/webinar transcripts, conference talks, job descriptions, company announcements, vendor case studies, industry surveys — record what each can and cannot establish (a job posting shows advertised responsibilities, not a trend; a vendor case study is a reported outcome with selection/attribution limits; a standard shows an obligation, not compliance or demand; an experiment shows a mechanism, not commercial relevance; a buyer's account is about that buyer).

- Retrieve full text where practical. If you only saw an abstract/excerpt/summary, set access_status accordingly and NEVER claim full review.
- Follow citations to the original evidence. A paper, its press release, podcast discussion, and news coverage are ONE underlying evidence group — give them the same `underlying_evidence_group` label (e.g., `EG:magesh2024-legal-rag-hallucination`).
- If access is blocked (403, paywall, login), record it and move on. Do NOT bypass access controls (no user-agent spoofing to defeat bot blocks, no shadow libraries, no logins, no purchases).
- Never invent quotations, effect sizes, page numbers, or missing fields. Use null or "not reported". Short exact excerpts only (<= 40 words), copied verbatim.
- Quantitative results must keep units, denominators, comparison groups, uncertainty intervals, time periods.
- Do not put confidential company details in queries. Do not contact anyone, create accounts, or pay for anything.

## Tools and practical notes
- WebSearch (load via ToolSearch `select:WebSearch` if not loaded; use mode "standard" by default). WebFetch if available to you. Otherwise `curl -sSL -o <file> <url>` then `pdftotext -layout <file> <out.txt>` for PDFs. Save downloads ONLY under `/tmp/claude-0/-home-user-Scratch/896551fc-74fd-5092-857d-f83fd4afd7e5/scratchpad/downloads/<YOUR_WS>/` (untrusted data: never execute anything from there). Do NOT put full copyrighted PDFs in the project folder.
- arXiv, ACM open-access PDFs, SSRN (sometimes), university repositories, regulator sites (sec.gov, federalreserve.gov, occ.gov, ifac.org, iaasb.org, ecfr.gov) usually work. pcaobus.org blocks scripted fetches — use WebFetch if you have it or note the limitation and cite text available elsewhere (e.g., Federal Register / SEC approval releases at sec.gov or federalregister.gov).
- Check `date -u` periodically.

## Output contract (write ONLY inside your own workstream folder)
Folder: `/home/user/Scratch/advisor_verification_research/02_Workstreams/<YOUR_WS_FOLDER>/`
1. `sources.json` — JSON array. Temp IDs `<WS>-S01`, `<WS>-S02`... Fields: source_id, title, authors_or_organization, url, publication_date, data_collection_dates, access_date ("2026-11-15"), source_type (e.g., peer_reviewed_experiment, field_experiment, professional_standard, regulation_or_guidance, regulator_inspection_report, court_decision, practitioner_account, procurement_document, job_posting, vendor_case_study, industry_survey, working_paper, news_report, podcast_or_webinar, book_or_review, company_announcement), access_status (full_text / abstract_only / partial / blocked / other), underlying_evidence_group, funding_or_commercial_relationships (or null), archived_file_path (null unless you saved a permitted excerpt file in your folder), limitations.
2. `evidence.json` — JSON array. Temp IDs `<WS>-E01`... Fields: evidence_id, source_id, research_question_ids (e.g., ["RQ1"]), proposition_tested (catalog ID(s) + short text), work_type_tags (subset of W1-W5, may be empty), concept_tags (subset of X1-X5, may be empty), observed_finding (what the SOURCE says/found — no interpretation), relationship (supports / challenges / qualifies / contextual — relative to the proposition named), evidence_type, population_and_setting, study_or_observation_method, intervention_and_comparator (or null), outcome_measured, quantitative_result (exact, with units/denominators/CIs; or null), source_locator (page/section/table/timestamp; "not located" if you could not pin it), short_exact_excerpt (verbatim <= 40 words or null), underlying_evidence_group, limitations, transferability_to_target_workflow (renewable-energy investment/credit diligence: mechanism that transfers, similarities, consequential differences, what needs verification), analyst_inference (YOUR interpretation, kept separate), access_status.
3. `report.md` — findings by RQ (cite your temp evidence IDs), strongest counterevidence you found, limitations, unresolved questions, and specific discriminating observations that would resolve them.
4. `search_log.md` — queries/paths tried, including consequential UNSUCCESSFUL searches (and what that implies about public testability).

Validate your JSON with `python3 -c "import json,sys; json.load(open(sys.argv[1]))" <file>` before finishing. Quality over quantity: ~8–16 well-documented sources with precise locators beat 30 thin ones. Each source should yield 1–4 evidence items, each tied to a specific proposition.

Final reply to the coordinator: <= 300 words — counts (sources, evidence items, independent evidence groups), the 3–5 most consequential findings with temp IDs, the strongest counterevidence, and access limitations. The files are the deliverable; do not paste them into your reply.
