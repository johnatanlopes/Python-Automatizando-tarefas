import shutil, os

# Alterando o diretório atual para C:\\tmp
os.chdir('C:\\tmp')

# Copiando o arquivo spam.txt para delicious
shutil.copy('C:\\tmp\\spam.txt', 'C:\\tmp\\delicious')

# Copiando o arquivo e alterando o nome
shutil.copy('C:\\tmp\\spam.txt', 'C:\\tmp\\delicious\\spam-novo.txt')

# Copiando uma pasta completa
shutil.copytree('C:\\tmp\\bacon', 'C:\\tmp\\delicious\\bacon_bkp')