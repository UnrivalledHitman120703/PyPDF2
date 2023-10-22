# PDF Merger
# Name = Indrajeet Mondal; Date = 22th October 2023
# SourceCode

import PyPDF2

with open("dummy.pdf", "rb") as file:
    # Creating a reader object
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    page.rotate(270)
    # Creating a writer object
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open("tilt.pdf", "wb") as new_file:
        writer.write(new_file)
