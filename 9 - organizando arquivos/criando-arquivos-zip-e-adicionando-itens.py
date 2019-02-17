'''
Nota: Utilizamos compress_type=zipfile.ZIP_DEFLATED isso especifica o algoritmo de compressão deflate, que funciona bem para todos os tipos de dados.
Para criar um arquivo passe o w, lembre-se que se existir arquivos no zip ele apagará todos.
Se quiser adicionar troque o w por a.
'''

import zipfile, os

# Acessando o diretório
os.chdir('C:\\tmp\\delicious')

newZip = zipfile.ZipFile('newzip.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()