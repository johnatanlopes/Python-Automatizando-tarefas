import zipfile, os

# Acessando o diretório
os.chdir('C:\\tmp\\delicious')

# Abrindo o arquivo zip
exampleZip = zipfile.ZipFile('example.zip')

# Listando os arquivos no zip
print(exampleZip.namelist())

# Capturando informações do arquivo
spamInfo = exampleZip.getinfo('spam-novo.txt')

# Tamanho do arquivo sem ser zipado
print(spamInfo.file_size)

# Tamanho do arquivo sendo zipado
print(spamInfo.compress_size)

# Exibindo a diferença do zip do arquivo atual para o compressado
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size)))

# Fechando o zip
exampleZip.close()