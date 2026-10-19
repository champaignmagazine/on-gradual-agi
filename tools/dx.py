"""Small helpers for editing word/document.xml in place.

Usage from other scripts:
    from dx import Doc
    d = Doc(path)
    d.find("phrase")            -> list of (para_index, para_text)
    d.replace("old", "new", n=1) -> replaces within a single w:t, or across runs of one paragraph
    d.save()
"""
import re, sys, copy
from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
def q(t): return "{%s}%s" % (W, t)


class Doc:
    def __init__(self, path):
        self.path = path
        self.tree = etree.parse(path)
        self.root = self.tree.getroot()
        self.log = []

    def paras(self):
        return self.root.iter(q("p"))

    @staticmethod
    def ptext(p):
        return "".join(t.text or "" for t in p.iter(q("t")))

    def find(self, phrase, show=True):
        out = []
        for i, p in enumerate(self.paras()):
            s = self.ptext(p)
            if phrase in s:
                out.append((i, s))
                if show:
                    print(i, "|", s[:400])
        return out

    def para(self, phrase, nth=0):
        hits = [p for p in self.paras() if phrase in self.ptext(p)]
        if len(hits) <= nth:
            raise KeyError("not found: %r (hits=%d)" % (phrase, len(hits)))
        return hits[nth]

    def replace(self, old, new, count=1, expect=None, within=None):
        """Replace `old` by `new` in paragraph text. Works across run boundaries:
        the replacement text is placed into the w:t where the match starts; the
        remainder of the match is removed from following w:t elements."""
        done = 0
        paras = list(self.paras()) if within is None else [within]
        for p in paras:
            ts = [t for t in p.iter(q("t"))]
            while True:
                full = "".join(t.text or "" for t in ts)
                k = full.find(old)
                if k < 0:
                    break
                # locate start t
                pos = 0
                for idx, t in enumerate(ts):
                    L = len(t.text or "")
                    if pos + L > k:
                        break
                    pos += L
                start_t, off = idx, k - pos
                remaining = len(old)
                t = ts[start_t]
                txt = t.text or ""
                take = min(remaining, len(txt) - off)
                t.text = txt[:off] + new + txt[off + take:]
                remaining -= take
                j = start_t + 1
                while remaining > 0:
                    tt = ts[j]
                    tx = tt.text or ""
                    take = min(remaining, len(tx))
                    tt.text = tx[take:]
                    remaining -= take
                    j += 1
                for tt in ts:
                    if tt.text and (tt.text[0] == " " or tt.text[-1] == " "):
                        tt.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
                done += 1
                if count and done >= count:
                    break
            if count and done >= count:
                break
        if expect is not None and done != expect:
            raise RuntimeError("replace %r: expected %d got %d" % (old[:60], expect, done))
        if done == 0:
            raise KeyError("no match for %r" % old[:80])
        self.log.append((old, new, done))
        return done

    def set_para_text(self, p, text):
        """Replace all text of paragraph p with `text`, keeping the first run's formatting."""
        runs = p.findall(q("r"))
        first = None
        for r in runs:
            if r.find(q("t")) is not None:
                first = r
                break
        for r in runs:
            if r is not first:
                p.remove(r)
        for t in first.findall(q("t")):
            first.remove(t)
        t = etree.SubElement(first, q("t"))
        t.text = text
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        return p

    def insert_after(self, p, text, template=None):
        """Insert a new paragraph after p, copying pPr and first-run rPr from template (default p)."""
        tpl = template if template is not None else p
        newp = copy.deepcopy(tpl)
        for child in list(newp):
            if child.tag != q("pPr"):
                newp.remove(child)
        r0 = None
        for r in tpl.findall(q("r")):
            if r.find(q("t")) is not None:
                r0 = r
                break
        r = etree.SubElement(newp, q("r"))
        if r0 is not None and r0.find(q("rPr")) is not None:
            r.append(copy.deepcopy(r0.find(q("rPr"))))
        t = etree.SubElement(r, q("t"))
        t.text = text
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        p.addnext(newp)
        return newp

    def delete_para(self, p):
        p.getparent().remove(p)

    def save(self, path=None):
        self.tree.write(path or self.path, xml_declaration=True, encoding="UTF-8", standalone=True)


if __name__ == "__main__":
    d = Doc(sys.argv[1])
    for ph in sys.argv[2:]:
        print("==", ph)
        d.find(ph)
