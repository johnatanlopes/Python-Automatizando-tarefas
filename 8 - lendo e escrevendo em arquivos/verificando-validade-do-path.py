'''
os.path.exists(path) - Retornará True se o arquivo ou a pasta referenciada no argumento existir e retornará False caso contrário

os.path.isfile(path) - Retornará True se o argumento referente ao path existir e for um arquivo e retornará False caso contrário

os.path.isdir(path) - Retornará True se o argumento referente ao path existir e for uma pasta e retornará False caso contrário
'''

import os

# Verificando se existe
print(os.path.exists('C:\\Windows'))
print(os.path.exists('C:\\Windows\\Nao\\Existe'))
print(os.path.exists('Z:\\'))

# Verificando se é uma pasta
print(os.path.isdir('C:\\Windows\\Temp'))

# Verificando se é um arquivo
print(os.path.isfile('C:\\Windows\\Temp'))
print(os.path.isfile('C:\\Windows\\System32\\Calc.exe'))

