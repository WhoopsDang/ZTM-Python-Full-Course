import PyPDF2
import os

pdf_dir = "files/"
wtr_dir = "wtr/"

watermark = PyPDF2.PdfReader(f"{pdf_dir}wtr.pdf")
watermark_page = watermark.pages[0]


for file in os.listdir(pdf_dir):
    output = PyPDF2.PdfWriter()
    input_pdf = PyPDF2.PdfReader(f"{pdf_dir}{file}")
    for i in range(len(input_pdf.pages)):
        pdf_page = input_pdf.pages[i]
        pdf_page.merge_page(watermark_page)
        output.add_page(pdf_page)

    with open(f"{pdf_dir}{file}", "wb") as newfile:
        output.write(newfile)
