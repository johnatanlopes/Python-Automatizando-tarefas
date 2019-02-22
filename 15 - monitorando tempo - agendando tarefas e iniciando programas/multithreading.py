'''
Para apresentar o conceito de multithreading (várias threads), vamos dar uma olhada em uma situação de exemplo.
Suponha que você queira que um código seja executado após um intervalo de tempo ou em um horário específico.
Você poderá acrescentar um código como este no início de seu programa:

import time, datetime

startTime = datetime.datetime(2019, 10, 31, 0, 0, 0)
while datetime.datetime.now() < startTime:
    time.sleep(1)

print('Program now stating on Halloween 2029')
-- trecho removido --

Esse código designa uma data de início igual a 31 de outubro de 2029 e permanece chamando time.sleep(1)
até que a data de início seja atingida. Seu programa não poderá fazer nada enquanto espera o loop com as chamadas 
a time.sleep() terminar; ele simplemente ficará esperando até o Halloween de 2029. Isso ocorre porque os programas
Python, por padrão tê uma única thread de execução.

Para entender o que é uma thread de execução, lembre-se da discussão do controle de fluxo, quando você imaginou a 
execução de um programa e o movesse para a próxima linha ou para qualquer local em que a instrução de controle
de fluxo o enviasse. Um programa single-threaded (com uma única threads) tem vários dedos. Cada dedo continua
se movendo para a próxima linha de código, conforme definido pelas instruções de fluxo, porém os dedos podem 
estar em diferentes lugadores do programa, executando linhas de código distintas ao mesmo tempo.Até o momento todos
os programas eram single threaded.

Em vez de fazer o seu código esperar até a função time.sleep() terminar, o código a ser executado após um
intervalo de tempo ou agendado para determinado horário poderá estar em uma thread diferente se usarmos o 
módulo threading do Python. A thread separada fará uma pausa para as chamadas time.sleep. Enquanto isso, seu
programa poderá realizar outras tarefas na thread original.

Exemplo:
'''

import threading, time

def takeANap():
    time.sleep(5)
    print('Wake up')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')

'''
A saída será:

End of program.
Wake up

Se print('End of program.') É a última linha do programa, você poderia chaar que ela deveria ser a última
informação exibida. O motivo pelo qual Wake up é apresentado depois deve-se ao fato de que quando threadObj.start() 
é chamado a função alvo de threadObj é executada emuma nova thread de execução. Pense nisso como um segundo
dedo que apareça no início da função takeANap(). A thread principal contiunua em print('End of program.').
Enquanto isso, a nova thread que estava executando a chamada time.sleep(5) faz uma pausa de cinco segundos.
Depois de acordar de um cochilo de cinco segundos, ela exibirá Wake up e retornará da função takeANap().
Cronologicamente Wake up é a última informação exibida pelo programa.

Normalmente um programa termina quando a última linha de código do arquivo é executada (ou a função sys.exit() 
é chamada) Entretando
'''