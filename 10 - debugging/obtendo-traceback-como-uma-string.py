'''
Quando encontra um erro o Python gera o traceback, a mensagem inclui o erro, o número da linha que provocou o erro e a sequência de chamadas
de função que resultou o erro. 

Podemos salvar o erro utilizando o modulo traceback e a função traceback.format_exc().

Por exemplo, em vez de fazer o programa falhar assim que uma exceção ocorrer, podemos gravar as informações de traceback em um arquivo de log e manter o programa
executando. Você poderá dar uma olhada no arquivo de log posteriormente, quando estiver pronto para depurar o programa.
'''

import traceback

def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

try:
    spam()
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info as written to errorInfo.txt')