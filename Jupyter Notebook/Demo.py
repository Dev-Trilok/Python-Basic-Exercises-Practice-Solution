import os
from PyPDF2 import PdfFileReader, PdfFileWriter

path = 'T:\Images\Nokia Backup\BackUp03022021\CamScanner\PDF old\Monali bams marksheet.pdf'
pdf = PdfFileReader(path, "rb")

pdf_writer = PdfFileWriter()

for page in range(3, 4):
    pdf_writer.addPage(pdf.getPage(page))

output_fname = "Output.pdf"

with open(output_fname, 'wb') as out:
    pdf_writer.write(out)

print ("PDF file has been split")