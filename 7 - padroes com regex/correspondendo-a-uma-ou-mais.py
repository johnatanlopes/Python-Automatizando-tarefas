import re

'''
O sinal de + corresponde a um ou mais
'''

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

# Se não encontrar nada ele retornará None 
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)

