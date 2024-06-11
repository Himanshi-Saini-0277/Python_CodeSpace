from pypdf import PdfWriter
import os

merger = PdfWriter()

for i in os.listdir():
  if i.endswith(".pdf"):
    merger.append(i)

merger.write("merged.pdf")
merger.close()