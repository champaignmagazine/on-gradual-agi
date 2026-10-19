# Regenerating the online edition

`docs/` is generated from the Word master for each release:

```bash
mkdir work && cd work
unzip -q ../On_Gradual_AGI_vX.docx -d un
python3 ../tools/web_prep.py un                 # standard headings; drop print-only title page, Contents and lists
python3 ../tools/zipdocx.py un web.docx
pandoc web.docx -t gfm+tex_math_dollars --wrap=none --extract-media=media -o book.md
python3 ../tools/build_site.py book.md media/media ../docs/media/figure-12-1-full.png .. X
mkdocs build --strict
```

Requires Python 3 with `lxml`, pandoc 3, and MkDocs Material. `docs/index.md` and `docs/media/cover.jpg` are maintained by hand.
