'''
Você pode salvar variáveis em seus programas Python em arquivos shelf binários usando o módulo shelve. Dessa maneira, seu programa, podera
restaurar dados em variáveis que estão no disco rígido. O módulo shelve permitirá adicionar funcionalidades Save e Open em seu programa. Por exemplo,
se você executar um programa e inserir alguns parâmetros de configuração, será possível salvar essas configurações em um arquivo shelf e em seguida
fazer o programa carregá-las na próxima vez em que for executado.
'''

import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats

'''
Após executar o código acima você terá três novos arquivos no diretório atual: mydata.bak, mydata.dat e mydata.dir. No OSX somente um único arquivo
mydata.db.
Os arquivos terão armazenado os valores das variáveis. Esses arquivos são binários.
'''

# Verificando o tipo dos dados e imprimindo
print(type(shelfFile))
print(shelfFile['cats'])

# Listando as keys que estão cadastradas no shelf
print(list(shelfFile.keys()))

# Listando os valores cadastrados
print(list(shelfFile.values()))

# Fechando o arquivo shelve
shelfFile.close()


