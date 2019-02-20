'''
Alguns docuemntos PDF têm um recurso de criptografia que evita que eles sejam lidos até que uma senha seja fornecida pela pessoa que estiver abrindo o 
documento.
'''

import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))

# Verificando se o pdf esta encriptado
print(pdfReader.isEncrypted)

# Retorna erro ao tentar acessar a primeira page
# pdfReader.getPage(0)

# Passando a senha para descriptografar
pdfReader.decrypt('rosebud')

pageObjs = pdfReader.getPage(0)
print(pageObjs.extractText())