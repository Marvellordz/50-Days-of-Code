import PyPDF2
pdf = open("patch.pdf", "rb")  # this specifies the pdf file to read from
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(12)  # this line specifies the page to copy from
text = page.extractText()
print('Extraction completed, Writing commenced...')
with open('result.txt', 'w') as fp:
    print('writing in progress...')
    fp.write(text)
    pass
print('Writing completed!!')
