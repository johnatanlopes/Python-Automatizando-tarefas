spam = 'Hello world!'

# upper() deixa todas as letras em maiusculo
print(spam.upper())

# lower() deixa todas as letras minusculas
print(spam.lower())

# Utilizar os métodos não altera a string
print(spam)

# Verificando se uma palavra é minuscula
print(spam.islower())
print('hello'.islower())
print('abcd1234'.islower())
print('1234'.islower())

# verificando se uma palavra é maiuscula
print(spam.isupper())
print('HELLO'.isupper())

# Podemos transformar uma palavra em maiusculo e verificar se a mesma ta em maiusculo
print('hello'.upper().isupper())
