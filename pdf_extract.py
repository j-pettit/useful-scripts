''' Extract the text from a PDF file'''

import argparse
import os
from PyPDF2 import PdfFileReader

parser = argparse.ArgumentParser(description='extract the text from a pdf')
parser.add_argument('file', help='choose the file to extract text from')
parser.add_argument('-o', '--output', metavar='output', help='set the output file name', default='extracted')
parser.add_argument('-c', '--copy', help='copy the text to the clipboard', action='store_true')
args = parser.parse_args()

pdf = PdfFileReader(args.file)
out = open(args.output + '.txt', 'a')
text = ''

for i in range(pdf.getNumPages()):
    page = pdf.getPage(i)
    content = page.extractText()
    text += content + '\n'

if args.copy:
    try:
        import pyperclip
    except ImportError:
        print('pyperclip module is required to use the copy argument')
    else:
        pyperclip.copy(text)

out.write(text)
out.close()
