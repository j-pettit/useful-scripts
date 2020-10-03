import sys
from PyPDF2 import PdfFileReader, PdfFileMerger

pdf_list = sys.argv[1:]

merged = PdfFileMerger()

for pdf in pdf_list:
    merged.append(PdfFileReader(pdf, 'rb'))

merged.write('merged.pdf')
