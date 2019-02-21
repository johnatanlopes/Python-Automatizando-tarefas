# combinetePdfs.py - Combina os PDFs do diretório de trabalho atual em um único PDF

import PyPDF2, os

# Obtém os nomes de todos os arquivos PDF

pdfFiles = []
for fileName in os.listdir('.'):
    if fileName.endswith('.pdf'):
        pdfFiles.append(fileName)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Percorre todos os arquivos PDF em um loop.
for fileName in pdfFiles:
    pdfFileObj = open(fileName, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Percorre todas as páginas (exceto a primeira) e as adiciona no PDF de saída
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Salva o PDF resultante em um arquivo
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()