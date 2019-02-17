import pprint

# variavel com informações dos cats
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]

# Mostrando na tela os dados dos cats
print(pprint.pformat(cats))

# Criando o arquivo myCats e salvando a variável nele e fechando o arquivo
fileObjs = open('myCats.py', 'w')
fileObjs.write('cats = ' + pprint.pformat(cats) + '\n')
fileObjs.close()

# Importando o arquivo myCats.py que criamos e exibindo a variável que importamos
import myCats
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])