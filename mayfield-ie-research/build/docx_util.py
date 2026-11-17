import re
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY = RGBColor(0x1F, 0x38, 0x64)

def new_doc(base_pt=10):
    d = Document()
    s = d.sections[0]
    s.page_width, s.page_height = Inches(8.5), Inches(11)
    s.left_margin = s.right_margin = Inches(0.8)
    s.top_margin = s.bottom_margin = Inches(0.7)
    st = d.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(base_pt)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    st.paragraph_format.space_after = Pt(4); st.paragraph_format.line_spacing = 1.08
    for name, size in (("Heading 1", 13), ("Heading 2", 11)):
        h = d.styles[name]; h.font.name = "Calibri"; h.font.size = Pt(size); h.font.bold = True
        h.font.color.rgb = NAVY; h.paragraph_format.space_before = Pt(10 if name == "Heading 1" else 6)
        h.paragraph_format.space_after = Pt(3)
        rpr = h.element.get_or_add_rPr(); rf = rpr.find(qn("w:rFonts"))
        if rf is None: rf = OxmlElement("w:rFonts"); rpr.append(rf)
        for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"): rf.set(qn(a), "Calibri")
    for lst in ("List Bullet", "List Number"):
        d.styles[lst].font.size = Pt(base_pt); d.styles[lst].paragraph_format.space_after = Pt(2)
    return d

def add_runs(p, text, size=None):
    # **bold** markup
    for i, part in enumerate(re.split(r"(\*\*.+?\*\*)", text)):
        if not part: continue
        if part.startswith("**") and part.endswith("**"):
            r = p.add_run(part[2:-2]); r.bold = True
        else:
            r = p.add_run(part)
        if size: r.font.size = Pt(size)
    return p

def para(d, text, style=None, size=None, after=None, italic=False, align=None):
    p = d.add_paragraph(style=style) if style else d.add_paragraph()
    add_runs(p, text, size)
    if italic:
        for r in p.runs: r.italic = True
    if after is not None: p.paragraph_format.space_after = Pt(after)
    if align: p.alignment = align
    return p

def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), hexcolor)
    tcPr.append(sh)

def table(d, headers, rows, widths, size=8, caption=None):
    if caption:
        c = para(d, caption, size=9, after=2); c.runs[0].bold = True
        for r in c.runs: r.font.color.rgb = NAVY
    t = d.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for i, h in enumerate(headers):
        cell = t.rows[0].cells[i]; cell.text = ""
        p = cell.paragraphs[0]; r = p.add_run(h); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shade(cell, "1F3864")
    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = ""
            p = cells[i].paragraphs[0]; add_runs(p, str(v), size)
            p.paragraph_format.space_after = Pt(0)
            if ri % 2 == 1: shade(cells[i], "EEF2F8")
    for row in t.rows:
        for i, w in enumerate(widths):
            row.cells[i].width = Inches(w)
    grid = t._tbl.tblGrid
    for i, gc in enumerate(grid.findall(qn("w:gridCol"))):
        gc.set(qn("w:w"), str(int(widths[i] * 1440)))
    tblPr = t._tbl.tblPr
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
    # repeat header row
    trPr = t.rows[0]._tr.get_or_add_trPr(); th = OxmlElement("w:tblHeader"); th.set(qn("w:val"), "true"); trPr.append(th)
    d.add_paragraph().paragraph_format.space_after = Pt(2)
    return t
