''' Archive a folder into a zip'''

import argparse
import os
import zipfile

parser = argparse.ArgumentParser(description='extract the text from a pdf')
parser.add_argument('path', help='choose the folder to archive')
parser.add_argument('-o', '--output', metavar='output', help='set the output file name', default='archive')
args = parser.parse_args()

path = args.path
output = args.output + '.zip'

ziph = zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED)

if os.path.isdir(path):
    for root, _dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
else:
    ziph.write(path)
ziph.close()
