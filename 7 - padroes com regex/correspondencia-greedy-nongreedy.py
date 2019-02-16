import re

'''
Com (Ha){3,5} pode corresponder a três, quatro ou cinco instâncias de Ha na string 'HaHaHaHaHa'
Então esse nosso padrão pode pegar HaHaHa e também HaHaHaHa.
As expressões regulares são greedy (gulosas) por default, o que significa que em situações ambíguas a correspondência será feita com a 
maior string possível.

Na versão nongreedy (não gulosa) das chaves, que faz a correspondência com a menor string possível, um ponto de interrogação
é usado depois da cahve de fechamento
'''

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

greedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = greedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
