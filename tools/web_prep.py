"""Prepare a copy of the master for Markdown/HTML conversion.
usage: web_prep.py unzipped_dir   (edits that copy in place)"""
import sys, os, re
sys.path.insert(0, sys.path[0])
from lxml import etree
from dx import Doc, q

U = sys.argv[1]
d = Doc(os.path.join(U, "word/document.xml")); T = d.ptext
body = d.root.find(q("body"))
def st(p):
    s = p.find(q("pPr") + "/" + q("pStyle")); return s.get(q("val")) if s is not None else ""
def set_style(p, val):
    ppr = p.find(q("pPr"))
    if ppr is None: ppr = etree.SubElement(p, q("pPr")); p.insert(0, ppr)
    s = ppr.find(q("pStyle"))
    if s is None: s = etree.Element(q("pStyle")); ppr.insert(0, s)
    s.set(q("val"), val)
    for o in ppr.findall(q("outlineLvl")): ppr.remove(o)

blocks = list(body)
# 1. drop the title page (everything before "Copyright and License")
first = next(i for i, b in enumerate(blocks) if b.tag == q("p") and st(b) == "Heading1" and T(b).strip() == "Copyright and License")
for b in blocks[:first]: body.remove(b)
# 2. drop printed Contents / List of Figures / List of Tables (the site has its own navigation)
blocks = list(body); drop = False
for b in blocks:
    if b.tag == q("p") and st(b) == "Heading1":
        drop = T(b).strip() in ("Contents", "List of Figures", "List of Tables")
    if drop and b.tag != q("sectPr"): body.remove(b)
# 3. headings
n = {"chap": 0, "part": 0, "h2": 0, "h3": 0, "h4": 0, "cap": 0}
for p in list(d.paras()):
    s = st(p); t = T(p).strip()
    if not s: continue
    if re.search(r"Subtitle$", s) or (re.search(r"Title$", s) and not t.startswith("Chapter")):
        if re.match(r"u\d\d", s) or re.match(r"Unit", s):            # part divider: Part I / Orientation
            p.getparent().remove(p); n["part"] += 1
        continue
    if re.search(r"Title$", s) and t.startswith("Chapter"):
        m = re.match(r"(Chapter \d+)(.*)", t)
        for r in list(p):
            if r.tag != q("pPr"): p.remove(r)
        r = etree.SubElement(p, q("r")); tt = etree.SubElement(r, q("t")); tt.text = f"{m.group(1)} — {m.group(2).strip()}"
        set_style(p, "Heading1"); n["chap"] += 1; continue
    level = None
    if s == "Heading1" or re.fullmatch(r"u\d\dHeading1", s): level = 1
    elif s == "Heading2" or re.search(r"heading1$", s) or re.search(r"Unit\du\d\dHeading1$", s): level = 2
    elif re.search(r"heading2$", s): level = 3
    elif re.search(r"heading3$", s) or s == "Heading4" or re.search(r"Heading4$", s): level = 4
    if level is None: continue
    if re.match(r"(Table|Figure) \d+\.\d+", t):                     # captions styled as headings
        set_style(p, "Caption"); n["cap"] += 1; continue
    set_style(p, f"Heading{level}"); n[{1: "chap", 2: "h2", 3: "h3", 4: "h4"}[level]] += 1 if level > 1 else 0
# 4. internal bookmarks/links are page-specific in print; keep text, drop the jump
for h in list(d.root.iter(q("hyperlink"))):
    if h.get(q("anchor")):
        par = h.getparent(); i = par.index(h)
        for c in list(h): par.insert(i, c); i += 1
        par.remove(h)
d.save(); print(n)
