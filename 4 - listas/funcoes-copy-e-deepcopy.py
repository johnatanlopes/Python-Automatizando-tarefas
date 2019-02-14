'''
Com o copy ao copiar uma lista estamos criando uma nova lista com os valores sem utilizar a referência.
a função copy.copy() cria uma duplicata e a função copy.deepcopy() é utilizada quando a lista possuem listas internas
'''

import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42

print(spam)
print(cheese)

