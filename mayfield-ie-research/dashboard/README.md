# Mayfield IE Market Intelligence Dashboard

An interactive, self-contained HTML dashboard that makes the verified U.S. solar & storage
independent engineering (IE) research navigable for Mayfield Renewables leadership.

## Opening it
Download `Mayfield_IE_Market_Intelligence.html` and open it in any modern browser (Chrome, Edge,
Safari, Firefox). It needs no server, login or internet connection. The only network use is
when you click an external source link. Google Drive's preview pane does not run the app;
download the file first.

## Views
1. **Overview**: the landscape matrix comes first, with firms placed by evidence strength (rows)
   and market position (columns A–F). A legend under it defines every row level and column, using
   the definitions in the workbook README. Below it come counts derived from the workbook and the
   principal findings, labelled Documented / Unproven / Hypothesis. Each
   finding has a **"How we concluded this"** panel:
   - the reasoning, step by step;
   - the specific documents behind it, each with why it matters, the exact quoted passage, where
     it sits in the document, and its verification status;
   - an **"Open at highlighted passage"** link that opens the original filing scrolled to that
     passage and highlighted.
2. **Landscape explorer**: all 40 firms; search, sort, combinable filters (market position,
   derived segment/service tags, evidence class), and a toggle between the full landscape and the
   priority shortlist (15). Selecting a firm opens its profile.
3. **Company profiles** (side panel):
   - scale, footprint, capabilities, segments and lender vs sponsor services;
   - **"Key facts — how we know"**: the exact passages behind the main profile claims (all 15
     priority firms and 10 others);
   - evidence classes;
   - each linked evidence record as an expandable item showing why it has its class and the exact
     supporting passage;
   - sources, uncertainties and a "Compare with Mayfield" action.
4. **Financing evidence**: 39 records filterable by firm, counterparty, project type, year and
   evidence class. Each record has a **"How we know"** toggle, and an "Expand all passages"
   option opens them all. The toggle shows:
   - a plain-language reason for the record's evidence class;
   - any qualification;
   - the exact passage(s), with highlighted-passage links.

   Class 1 records always note that the signed reliance letter itself was not examined.
5. **Market segments**: the seven segments, with buyers, selection mechanism, competitors,
   requirements, Mayfield fit, obstacles, and V1 vs V2 assessments.
6. **Mayfield positioning**: Mayfield beside any selected firms, evidence gaps, unvalidated
   routes, and the three business models (A/B/C). No numerical scores.
7. **Findings & open questions**: what the research establishes and what remains uncertain, next
   steps, open gaps, planned interviews, the 36-claim evidence audit, the 98-source register,
   and links to the report, workbook and research plan.

**Source cards:** clicking any source ID (e.g., S02) opens a short card instead of the raw
document. The card shows what the source is, what it was used for, which findings and firms it
supports, and its key passages, with highlighted and full-document links.

**Highlight links:** these use standard URL text fragments (`#:~:text=`), supported by Chrome,
Edge, Safari 16.1+ and Firefox 131+. In other browsers the document opens at the top; the quoted
text is shown in the dashboard and can be found with Ctrl/Cmd+F. PDFs open without highlighting.

## Data lineage
- **Source of truth:** Google Sheet "Mayfield IE Competitive Landscape — Verified V2". Its tabs
  README, 1_Full_Landscape, 2_Priority_Competitors, 3_Evidence_References, 4_Market_Segments,
  5_Business_Models, 6_Evidence_Audit, 7_Source_Register and 8_Open_Gaps are read. The V1_ tabs
  are ignored.
- Tab **9_Key_Excerpts** holds 82 verbatim passages: excerpt ID, source ID, document, what it
  shows, quote, highlight start/end phrases, location, verification status, and "Profile fact
  for" (the firm, if the passage supports a profile claim). The "Excerpt IDs" column in
  3_Evidence_References links each record to its passages.
- 81 of the 82 quotes were checked word for word against a retrieved copy of the source. The
  Dimension Energy release (S33) blocks automated retrieval and is flagged as not re-checked.
- Two passages sit in collapsed sections of their web pages (S36, S90). Those open without
  highlighting, with a note to search for the quoted text.
- `narrative.json` holds the short text drawn from the final report and research plan (findings,
  conclusions, next steps, interview archetypes). It contains no tabular research data.
- Derived fields:
  - Segment/service filter tags come from keyword matching on each firm's Technologies, Segment
    focus and Service orientation text.
  - Links between firms and evidence records come from firm names in the "Firm(s)" column.
  - Project type is read from the workbook's "Project type" column. If that column is absent, it
    is derived from the transaction text.

## Refreshing after the workbook changes
1. In Google Sheets: File → Download → Microsoft Excel (.xlsx).
2. Run `python3 build_dashboard.py "<downloaded file>.xlsx" <output folder>` (requires Python 3
   and `openpyxl`). The script checks that every referenced source ID exists in the Source
   Register, that every priority firm exists in the full landscape, and that every excerpt cited
   by a finding or evidence record, and every firm named in "Profile fact for", exists.
3. It writes `Mayfield_IE_Dashboard_Data.json` and a regenerated
   `Mayfield_IE_Market_Intelligence.html` (data embedded). `template.html` is the app shell.

## Deploying later (optional)
The HTML file is a complete static site. To publish it, place it (renamed `index.html` if
preferred) on any static host, such as an internal web server, SharePoint/Intranet file hosting,
GitHub Pages, Netlify or S3. Check who should have access first: the dashboard contains the full
research dataset.

## Limitations
- Desk research only; no interviews conducted. Evidence strength describes the public record,
  not engineering competence, and absence of public evidence is not evidence of absence.
- Fees, lender approval frequency and demand are not publicly documented, so they do not appear.
- Tested with Playwright/Chromium at desktop (1440px), tablet (820px) and phone (390px) widths.
  Other browsers were not tested.
