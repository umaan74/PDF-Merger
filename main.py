from PyPDF2 import PdfMerger

merger=PdfMerger()
pdf_list=["/*Here we have to put the pdf's */"]
for pdf in pdf_list:
    merger.append(pdf)

merger.write("New Merged.pdf")
merger.close()