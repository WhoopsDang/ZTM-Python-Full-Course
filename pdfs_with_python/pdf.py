import PyPDF2


reader = PyPDF2.PdfReader(open("files/dummy.pdf", "rb"))
print(len(reader.pages))

print(reader.pages[0])

page = reader.pages[0]
# page.rotate(90)

with open("files/tilt.pdf", "wb") as newfile:
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    writer.write(newfile)
