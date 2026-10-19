import sys, os, zipfile
src, dst = sys.argv[1], sys.argv[2]
with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(src, "[Content_Types].xml"), "[Content_Types].xml")
    for root, _, files in os.walk(src):
        for f in files:
            full = os.path.join(root, f); rel = os.path.relpath(full, src)
            if rel != "[Content_Types].xml": z.write(full, rel)
