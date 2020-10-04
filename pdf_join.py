''' Join multiple PDF files into a single file'''

import argparse
import sys
from PyPDF2 import PdfFileReader, PdfFileMerger

parser = argparse.ArgumentParser(description='join pdfs into one file')
parser.add_argument('files', nargs='+', help='list the files to be joined')
parser.add_argument('-o', '--output', metavar='output', help='set the name of the joined output file', default='merged.pdf')
args = parser.parse_args()

merged = PdfFileMerger()

for pdf in args.files:
    merged.append(PdfFileReader(pdf, 'rb'))

merged.write(args.output)
