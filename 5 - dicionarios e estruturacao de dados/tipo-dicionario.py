'''
Dicionarios são iguais listas, porém podem utilizar vários tipos de dados diferentes nos índices
'''
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat)
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur')

'''
Dicionarios também podem usar valores inteiros como chaves assim como listas utilizam inteiros para os índices, porém eles não precisam começar em 0
e qualquer número pode ser usado
'''

spam = {1234: 'Luggage Combination', 42: 'The Answer'}
