import re

'''
Podemos usar o ponto-asterisco (.*) para indicar qualquer caractere
'''

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))


'''
O ponto asterisco utiliza o modo greedy, ele sempre tentará fazer a correspondência no máximo de texto possível. Para corresponder a todo e qualqeur texto
em modo nongreedy, utilize ponto, asterisco e ponto de interrogação (.*?). Assim como no caso das chaves, o ponto de interrogação diz ao python para fazer
a correspondência em modo nongreedy
'''

nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

