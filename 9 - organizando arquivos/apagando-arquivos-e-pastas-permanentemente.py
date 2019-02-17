'''
Cuidado, ao apagar dessa forma não tem como recuperar os arquivos

os.unlink(path) - Apagará o arquivo em path

os.rmdir(path) - Apagará a pasta em path, esta pasta deve estar vazia, ou seja, não deve conter nenhum arquivo ou pasta

shutil.rmtree(path) - Removerá a pasta em path; além disso, todos arquivos e as pastas nele contidos também serão apagados
'''

# Apagando arquivos txt
import os

os.chdir('C:\\tmp\\delicious')

for filename in os.listdir():
    if filename.endswith('.txt'):
        os.unlink(filename)