# Ordenando listas com sort
spam = [-7, 1, 2, 3, 14, -7]
spam.sort()
print(spam)

spam = ['ants', 'cat', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

# Pode-se passar true para o argumento nomeado reserve de modo a fazer com que sort() ordene valores em ordem inversa
spam = [-7, 1, 2, 3, 14, -7]
spam.sort(reverse=True)
print(spam)

'''
sort() utiliza a ordem ASCII em vez da ordem alfabética para ordenar strings. Isso quer dizer que as letras
maiúsculas vêm antes das letras minúsculas. Sendo assim, a letra a minúscula é ordenada de modo que virá após a letra Z
'''
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

'''
Se houver necessidade de ordenar os valores em ordem alfabética normal, passe str.tolower para o argumento nomeado
key na chamada do método sort() isso fará a função tratar todos os itens da lista como se tivesse letras
minúsculas, sem realmente alterar os valores da lista
'''
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)