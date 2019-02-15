'''
Podemos transformar um dicionario em uma lista
no exemplo abaixo estamos repassando somente os indices
'''
print(list(spam.items()))

'''
Podemos utilizar atribuição multipla para passar todos os dados com um for
'''
for k, v in spam.items():
    print('Key: ' + k + ' - Value: ' + str(v))