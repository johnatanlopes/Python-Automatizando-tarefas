import re

'''
Adicionando o re.I nos tornamos a pesquisa sem diferenciar maiusculas de minusculas
'''

regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part	machine, all cop.').group()) 
print(robocop.search('ROBOCOP protects the innocentc.').group())
print(robocop.search('AI, why does your programming book talk about robocop so much?').group())