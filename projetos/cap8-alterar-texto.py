# Abre o arquivo em somente leitura e atribui o texto a uma variável
textoPadrao = open('cap8-texto-exemplo.txt', 'r')
content = textoPadrao.read()

# Fecha o arquivo textoPadrao
textoPadrao.close()

# Transforma o texto recebido em uma lista
contentList = content.split()

# Palavras procuradas para serem alteradas
words = ['ADJECTIVE', 'NOUN', 'VERB']

for i in range(len(contentList)):
    key = contentList[i].replace('.', '')
    if key in words:
        answer = input('Enter an ' + key + ': ')
        contentList[i] = contentList[i].replace(key, answer)

# Recebe o novo texto
novoTexto = ' '.join(contentList)


# Cria um novo arquivo e salva o conteudo que tratamos nele, logo em seguida fechamos o arquivo
novoArquivo = open('novoArquivo.txt', 'w')
novoArquivo.write(novoTexto)
novoArquivo.close()