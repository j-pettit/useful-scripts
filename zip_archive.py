''' Archive a folder into a zip'''

import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='extract the text from a pdf')
parser.add_argument('path', help='choose the folder to archive')
parser.add_argument('-o', '--output', metavar='output', help='set the output file name', default='archive')
args = parser.parse_args()

path = args.path
output = args.output

shutil.make_archive(output, 'zip', path)
