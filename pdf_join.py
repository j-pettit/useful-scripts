import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_list = sys.argv[1:]
writer = PdfFileWriter()
files = []
for pdf in pdf_list:
    open_pdf = open(str(pdf), 'rb')
    reader = PdfFileReader(open_pdf)
    for page in range(reader.numPages):
        page_obj = reader.getPage(page)
        writer.addPage(page_obj)
    files.append(open_pdf)
    
output = open('merged.pdf', 'wb')
writer.write(output)
print(files)
output.close()
for pdf in files:
    pdf.close()