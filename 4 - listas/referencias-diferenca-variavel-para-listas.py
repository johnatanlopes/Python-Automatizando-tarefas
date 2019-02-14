'''
Variáveis armazenam string e valores inteiros
No nosso exemplo abaixo podemos notar que as variáveis armazenam valores diferentes
'''

spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

'''
As listas não funcionam dessa maneira, ao atribuir uma lista a uma variável, na verdade, você estará atribuindo uma referência de lista à variável.
'''

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello'
print(spam)
print(cheese)