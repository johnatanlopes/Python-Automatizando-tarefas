'''
Não faça debug com print()
Digitar import logging e o logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') de certo modo é complicado.
Talvez você queira usar chamadas print() em vez de utilizar o logging, porém não se deixe cair nessa tentação! Após terminar o debugging você acabará gastando
muito tempo removendo as chamadas a print() de seu código para cada mensagem de log. Você poderá até mesmo remover acidentalmente algumas chamadas a print() que 
poderiam estar sendo usadas para mensagens que não sejam de log.

O interessante sobre as mensagens de log é que você tem a liberdade de encher seu programa com quantas mensagens de logs você quiser e sempre poderá desabilitá-las
quando quiser ao adicionar uma única chamada a logging.disable(logging.CRITICAL). De modo diferente de print(), o módulo logging facilita alternar entre mostrar e 
oculstar as mensagens de log.
'''

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total
    
print(factorial(5))
logging.debug('End of program')
