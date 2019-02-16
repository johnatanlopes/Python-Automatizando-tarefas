'''
os.path.getsize(path) - Retornará o tamanho em bytes do arquivo no argumento path

os.listdir(path) - Retornará uma lista de strings com nome de arquivo para cada arquivo no argumento path.
    (Observe que essa função esta no modulo os e não no os.path)
'''

import os

print(os.path.getsize('C:\\Windows\\System32\\Calc.exe'))

print(os.listdir('C:\\Windows\\Temp'))


'''
Se quiser descobrir o tamanho total de todos os arquivos nesse diretório, podemos usar os.path.getsize() e o os.listdir() juntos:
'''

totalSize = 0
for filename in os.listdir('C:\\Windows\\Temp'):
    totalSize += os.path.getsize(os.path.join('C:\\Windows\\Temp', filename))
print(totalSize)