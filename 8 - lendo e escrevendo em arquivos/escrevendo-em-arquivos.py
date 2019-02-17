# Abrindo o arquivo, escrevendo e fechando
# O modo de escrita w sobrescreve o conteudo existente no arquivo
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
baconFile.close()

# Abrindo o arquivo, adicionando texto e fechando
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable')
baconFile.close()

# Exibindo o que escrevemos
baconFile = open('bacon.txt', 'r')
print(baconFile.read())
baconFile.close()