# This program merges two or more PDF files into a singular PDF.

import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.chdir(r"C:\Users\robv\Documents")):
    if file.endswith("pdf"):
        merger.append(file)
    merger.write("combinedDocs.pdf")


