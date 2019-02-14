'''
O tipo de dado tupla é quase idêntico ao tipo de dado lista, exceto em relação a dois aspectos. Em primeiro lugarm, as tuplas são digitadas com parênteses 
no lugar de colchetes.
As tuplas são imutáveis
'''

eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))


'''
Se você tiver apenas um valor em sua tupla, isso pode ser indicado por meio da inserção de uma vírgula final após o valor entre parênteses.
Caso contrário o Python achará que você simplemente digitou um valor entre parênteses normais.
'''

print(type(('hello',)))
print(type(('hello')))