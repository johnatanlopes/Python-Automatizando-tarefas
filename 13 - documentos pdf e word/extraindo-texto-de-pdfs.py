# pip3 install PyPDF2

import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Exibindo quantidade de paginas
print(pdfReader.numPages)

# Acessando a primeira pagina e extraindo o texto dela
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

