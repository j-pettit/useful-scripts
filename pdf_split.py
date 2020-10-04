''' Split a PDF into multiple files'''

import argparse
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

parser = argparse.ArgumentParser(description='split a pdfs into multiple files')
parser.add_argument('file', help='choose the file to be split')
parser.add_argument('-p', '--pages', metavar='pages', help='choose the number of pages in each split file', type=int)
parser.add_argument('-o', '--output', metavar='output', help='set the base name of the split output files', default='split')
parser.add_argument('-d', '--defined', metavar='defined', help='select pages after which to create a split', nargs='+', type=int)
args = parser.parse_args()

pdf = PdfFileReader(args.file)

if args.defined:
    splits = args.defined
    splits.append(pdf.getNumPages())
elif args.pages:
    splits = [i for i in range(args.pages, pdf.getNumPages(), args.pages)]
    splits.append(pdf.getNumPages())
else:
    splits = [i+1 for i in range(pdf.getNumPages())]

os.makedirs('./split_files', exist_ok=True)
page = 0
for split in splits:
    writer = PdfFileWriter()
    while page < split:
        writer.addPage(pdf.getPage(page))
        output = './split_files/' + args.output + str(split) + '.pdf'
        with open(output, 'wb') as out:
            writer.write(out)
        page += 1
