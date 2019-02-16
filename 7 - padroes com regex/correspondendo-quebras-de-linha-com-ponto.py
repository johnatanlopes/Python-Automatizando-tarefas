import re

'''
O ponto-asterisco corresponderá a qualquer caractere, exceto uma quebra de linha. Ao passar re.DOTALL como segundo argumento de re.compile(),
podemos fazer que o caractere ponto corresponder a todos os caracteres, incluindo o de quebra de linha
'''

noNewLineRegex = re.compile('.*')
mo = noNewLineRegex.search('Serve the public trust.\nProtecte the innocent')
print(mo.group())

newLineRegex = re.compile('.*', re.DOTALL)
mo = newLineRegex.search('Serve the public trust.\nProtecte the innocent')
print(mo.group())
