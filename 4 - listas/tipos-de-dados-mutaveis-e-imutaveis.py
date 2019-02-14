'''
Strings são imutáveis
'''
name = 'Zophie a cat'

'''
Ao tentar atribuir um único caractere em uma string resulta em um erro TypeError
name[7] = 'the'
'''

'''
A maneira apropriada de efetuar uma mutação em uma string é usar o slicing e concatenação para criar uma nova string, copiando partes da string antiga
'''
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name)
print(newName)