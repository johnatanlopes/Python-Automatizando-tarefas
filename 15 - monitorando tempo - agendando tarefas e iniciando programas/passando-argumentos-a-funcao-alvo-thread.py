'''
Se a função-alvo que você quer executar na nova thread aceitar argumentos, eles poderão ser passados a função
threading.Thread(). Por exemplo, suponha que você queira executar a chamada a print():
'''

print('Cats', 'Dogs', 'Frogs', sep=' & ')

'''
Essa chamada a print() tem três argumentos normais, que são 'Cats', 'Dogs' e 'Frogs' e um argumento nomeado
sep=' & '. Os argumentos normais podem ser passados como uma lista ao argumento nomeado args em threading.Thread().
O argumento nomeado pode ser especificado como um dicionário ao argumento nomeado kwargs em threading.Thread().
'''

import threading

threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()