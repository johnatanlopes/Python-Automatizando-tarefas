'''
O método join() é útil quando temos uma lista de strings que devem ser unidas em um único valor de string
'''

print(','.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))


'''
O método split() faz o inverso do join(), é chamado em um valor de string e retorna uma lista de strings
'''

print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))

spam = """Dear Alice,
How have you been? I am fine,
There is a container in the fridge
that is labeled 'Milk Experiment'.
Please do not drink it.
Sincerely,
Bob"""

print(spam.split('\n'))