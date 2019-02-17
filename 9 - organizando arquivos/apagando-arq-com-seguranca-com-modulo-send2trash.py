'''
Com o send2trash os arquivos apagados serão enviados para a lixeira, mas não irá liberar espaço em disco.
Se quiser liberar espaço em disco utilize as funções do os e shutil para apagar arquivos e pastas.
'''

# pip3 install send2trash
import send2trash

# Cria o arquivo
baconFile = open('C:\\tmp\\bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

# Apagando arquivo e enviando para a lixeira
send2trash.send2trash('C:\\tmp\\bacon.txt')