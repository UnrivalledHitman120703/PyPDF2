# Putting a watermarker
# Name = Indrajeet Mondal; Date = 23rd October 2023
# SourceCode

import PyPDF2

template = PyPDF2.PdfReader(open("super.pdf", "rb"))
watermark = PyPDF2.PdfReader(open("wtr.pdf", "rb"))
output = PyPDF2.PdfWriter()


for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

with open("watermarked_output.pdf", "wb") as file:
    output.write(file)
