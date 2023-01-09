from PyPDF2 import PdfWriter
import glob

pdfFiles=glob.glob(r'.\pdf\*.pdf')

merger = PdfWriter()

for pdf in pdfFiles:
    merger.append(pdf)

merger.write(r'.\pdf\safe.pdf')
merger.close()

