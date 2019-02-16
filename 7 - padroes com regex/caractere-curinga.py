import re

'''
O caractere . (ponto) em uma regex é chamado de curinga e corresponde a qualquer caractere, exceto uma quebra de linha.
'''

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

