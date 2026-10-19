"""Split the converted book Markdown into MkDocs pages.
usage: build_site.py book.md media_dir fig121_full.png repo_dir version"""
import sys, re, os, shutil

src, media, fig_full, repo, version = sys.argv[1:6]
docs = os.path.join(repo, "docs")
os.makedirs(os.path.join(docs, "media"), exist_ok=True)
for f in os.listdir(media): shutil.copy(os.path.join(media, f), os.path.join(docs, "media", f))
shutil.copy(fig_full, os.path.join(docs, "media", "figure-12-1-full.png"))

md = open(src, encoding="utf-8").read()
md = re.sub(r"\[<u>(.*?)</u>\]", r"[\1]", md)                                    # underline inside links
md = md.replace("<u>", "").replace("</u>", "")
md = re.sub(r'src="media/media/', 'src="../media/', md)   # pages are served one level down (directory URLs)
md = md.replace("\\<", "&lt;")                                                   # Python-Markdown has no \< escape
md = re.sub(r'<img ([^>]*?) style="[^"]*"', r'<img \1 loading="lazy"', md)       # printed sizes -> responsive
# Figure 12.1: show the full-resolution version, click to open it
md = re.sub(r'<img src="\.\./media/(image\d+\.png)" title="Figure 12\.1"',
            r'<a href="../media/figure-12-1-full.png"><img src="../media/figure-12-1-full.png" title="Figure 12.1 (select to open full size)"', md)
md = re.sub(r'(<a href="\.\./media/figure-12-1-full.png"><img [^>]*?/?>)', r"\1</a>", md)
# display math inside pipe-table cells -> inline math
md = "\n".join(re.sub(r"\$\$(.+?)\$\$", r"$\1$", l) if l.startswith("|") else l for l in md.split("\n"))

PAGES = [  # (H1 text prefix, file name)
    ("Copyright and License", "copyright.md"), ("Preface", "preface.md"),
    ("Contributors and AI Collaboration", "contributors.md"), ("About the Author", "about-the-author.md"),
    ("Notation Quick Reference", "notation-quick-reference.md"), ("Reader Guide", "reader-guide.md"),
] + [(f"Chapter {n} ", f"chapter-{n:02d}.md") for n in range(1, 13)] + [
    ("Glossary", "glossary.md"), ("Full Notation Guide", "notation-guide.md"),
    ("Claims and Status Register", "claims-and-status-register.md"), ("Revision Record", "revision-record.md"),
    ("Unified References", "references.md")]
parts = re.split(r"(?m)^(?=# )", md)
assert parts[0].strip() == "", parts[0][:200]
written = []
for part in parts[1:]:
    title = part.split("\n", 1)[0][2:].strip()
    fn = next((f for p, f in PAGES if title.startswith(p)), None)
    assert fn, title
    open(os.path.join(docs, fn), "w", encoding="utf-8").write(part.rstrip() + "\n")
    written.append((title, fn))
assert len(written) == len(PAGES), (len(written), len(PAGES))
for t, f in written: print(f, "|", t)
