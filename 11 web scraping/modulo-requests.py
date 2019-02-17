'''
O módulo requests permite fazer facilmente o download de arquivos da web sem se preocupar com problemas complicados como erros de rede, problemas de conexão
e compressão de dados. O módulo requests não vem com o Python, portando será necessário instalá=lo antes. Digite pip3 install requests.

O módulo requests foi criado por que o módulo urllib2 do Python é complicado demais para usar.
'''

import requests

'''
A função requests.get() aceita uma string contendo uma URL para download.
Ao chamar type() no valor de retorno você perceberá que um objeto Response é retornado.
'''

# Realizando uma requisição
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# Verificando o tipo do res
print(type(res))

# Verificando o status da requisição
print(res.status_code == requests.codes.ok)

# Verificando o tamanho do texto recebido
print(len(res.text))

# Exibindo uma parte do resultado
print(res.text[:250])


'''
Verificando se houve erros

Com o método raise_for_status() é uma maneira de garantir que um programa seja interrompido caso um download indevido ocorra. Isso é bom: Você deve interromper
seu programa assim que algum erro inesperado ocorreur. Se um download com falhas não for motivo para interromper o seu programa, você poderá inserir instruções
try e except ao redor de sua linha raise_for_status para que esse erro seja tradado sem provocar falhas.

Retornará a seguinte saída de erro: There was a problem: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist
'''
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
# print(res.raise_for_status())

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))


'''
Salvando arquivos baixados no disco rígido
A partir de agora, você poderá salvar a página web em um arquivo em seu disco rígido com a função open() e o método write() padrões. Porém há algumas pequenas diferenças.
Inicialmente você deve abrir o arquivo em modo de escrita binária passando a string 'wb' como segundo argumento de open(). Mesmo que a página estiver em formato
texto simples, será necessário gravar dados binários em vez de dados em formato texto para preservar a codificação Unicode do texto.


Para gravar a págna web em um arquivo, podemos usar um loop for com o método iter_content() do objeto Response.
O método retorna porões do conteúdo a cada iteração pelo loop. Cada porção tem o tipo de dado bytes e é possível especificar quantos bytes cada
porção terá.
'''

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()