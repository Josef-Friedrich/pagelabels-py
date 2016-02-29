#!/usr/bin/env python3

from pagelabels import PageLabels, PageLabelScheme
from pdfrw import PdfReader, PdfWriter
import argparse

parser = argparse.ArgumentParser(description='Add page labels to a PDF file')
parser.add_argument('file', type=PdfReader, metavar="file.pdf",
                   help='the PDF file to edit')
parser.add_argument('--delete', action='store_true',
                   help='delete the existing page labels')
parser.add_argument('--startpage', '-s', type=int, default=1,
                    help="the index (starting from 1) of the page of the PDF where the labels will start")
parser.add_argument('--type', "-t", default="arabic", choices=PageLabelScheme.styles(),
                    help="""type of numbers:
                                arabic  = 1, 2,  3,
                                roman   = i, ii, iii, iv,
                                letters = a, b, c""")
parser.add_argument("--prefix", "-p", default="",
                    help="prefix to the page labels")
parser.add_argument("--firstpagenum", "-f", type=int, default=1,
                    help="number to attribute to the first page of this index")
options = parser.parse_args()

reader = options.file
if options.delete:
    labels = PageLabels()
else:
    labels = PageLabels.from_pdf(reader)
    newlabel = PageLabelScheme(startpage    = options.startpage-1,
                               style        = options.type,
                               prefix       = options.prefix,
                               firstpagenum = options.firstpagenum)
    labels.append(newlabel)
    print(labels)
# Write the new page labels to the PDF
labels.write(reader)
print(reader.Root.PageLabels)

writer = PdfWriter()
writer.trailer = reader
writer.write("/tmp/test.pdf")
