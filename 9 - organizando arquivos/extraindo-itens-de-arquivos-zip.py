import zipfile, os

# Alterando para o diretório atual
os.chdir('C:\\tmp\\delicious')

# Abrindo o zip, extraindo todos arquivos
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()

# O objeto extract() do zipfile extrai somente um objeto
# Também podemos informar o diretório que desejamos extrair os arquivos passando como segundo argumento
# exampleZip.extract('spam-novo.txt')
# exampleZip.extract('spam-novo.txt', 'C:\\tmp\\outro-dir')

# Fechando o zip
exampleZip.close()