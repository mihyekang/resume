import sys, markdown

src, dst = sys.argv[1], sys.argv[2]

with open(src, encoding="utf-8") as f:
    body = markdown.markdown(f.read(), extensions=["tables", "sane_lists"])

CSS = """
@page { size: A4; margin: 16mm 15mm 16mm 15mm; }
* { box-sizing: border-box; }
body {
  font-family: "Malgun Gothic", "맑은 고딕", -apple-system, sans-serif;
  font-size: 10.2pt; line-height: 1.62; color: #1a1a1a;
  margin: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
h1 {
  font-size: 21pt; font-weight: 700; margin: 0 0 4pt; letter-spacing: -0.4pt;
  padding-bottom: 7pt; border-bottom: 2.2pt solid #1a1a1a;
}
h1 + p { font-size: 11pt; color: #444; margin: 7pt 0 3pt; font-weight: 600; }
h2 {
  font-size: 13.5pt; font-weight: 700; margin: 20pt 0 8pt; padding-bottom: 4pt;
  border-bottom: 1pt solid #c8c8c8; break-after: avoid; page-break-after: avoid;
}
h3 {
  font-size: 11.5pt; font-weight: 700; margin: 14pt 0 5pt; color: #111;
  break-after: avoid; page-break-after: avoid;
}
h4 {
  font-size: 10.6pt; font-weight: 700; margin: 12pt 0 4pt; color: #222;
  padding-left: 7pt; border-left: 3pt solid #555;
  break-after: avoid; page-break-after: avoid;
}
p { margin: 5pt 0; text-align: justify; }
ul { margin: 4pt 0 8pt; padding-left: 17pt; }
li { margin: 2.5pt 0; }
strong { font-weight: 700; color: #000; }
a { color: #1a1a1a; text-decoration: none; border-bottom: 0.5pt dotted #888; }
code {
  font-family: Consolas, "D2Coding", monospace; font-size: 9pt;
  background: #f0f0f0; padding: 0.5pt 3pt; border-radius: 2pt;
}
table {
  width: 100%; border-collapse: collapse; margin: 7pt 0 10pt; font-size: 9.3pt;
  break-inside: avoid; page-break-inside: avoid;
}
th {
  background: #ececec; text-align: left; font-weight: 700;
  padding: 5pt 7pt; border: 0.6pt solid #b8b8b8;
}
td { padding: 5pt 7pt; border: 0.6pt solid #cfcfcf; vertical-align: top; }
h2, h3, h4 { break-inside: avoid; page-break-inside: avoid; }
li, tr { break-inside: avoid; page-break-inside: avoid; }
"""

html = (
    '<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8">'
    "<title>강미혜 경력기술서</title><style>" + CSS + "</style></head><body>"
    + body + "</body></html>"
)

with open(dst, "w", encoding="utf-8") as f:
    f.write(html)

print("html written:", dst)
