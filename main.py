import PyPDF2
import pdfreader

pdfiles = ["1pdf", "2pdf", "3pgf"]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfMerger(pdfFile)
    merger.append(pdfreader)
    pdfFile.close()
    merger.write('merged.pdf')




