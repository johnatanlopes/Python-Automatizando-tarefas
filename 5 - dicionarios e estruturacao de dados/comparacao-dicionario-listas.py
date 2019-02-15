'''
De modo diferente das listas, os itens de um dicionário não estão ordenados. O primeiro item de uma lista chamada spam será spam[0]
Entretanto não há um primeiro item em um dicionário. Enquanto a ordem dos itens é importante para determinar suas duas listas são iguais, não importa em que ordem
os pares chave-valor são digitados em um dicionário
'''

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)

'''
Tentar acessar uma chave inexistente em um dicionário resultará no erro KeyError
'''
ham['color']