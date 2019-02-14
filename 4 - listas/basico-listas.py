# Listas
print([1,2,3])
print(['cat', 'bat', 'rat', 'elephant'])
print(['hello', 3.14515, True, None, 42])

spam = ['a', 'b', 'c', 'd']
print(spam)

#  Obtendo valores individuais da lista
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])
print('The ' + spam[1] + ' ate the ' + spam[0] + '.')

# Erro IndexError
'''
Caso tente acessar algum indice que não exista na lista retornará o erro IndexError
spam[1000]
Os indices devem ser somente de números inteiros
'''

# Listas podem conter outras listas
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0])
print(spam[0][1])
print(spam[1][4])

# Indices negativos
# Indices comecam por 0 e aumentam, também podemos usar inteiros negativos para o índice. O valor inteiro -1 refere-se ao último índice 
# de uma lista, o valor -2 refere-se ao penúltimo índice de uma lista e assim por diante.
spam = ['cat', 'bat', 'rat', 'elephante']
print(spam[-1])
print(spam[-3])
print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')
