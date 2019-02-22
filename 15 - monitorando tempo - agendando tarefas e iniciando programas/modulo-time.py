'''
O módulo time permite que seus programas Python leiam o relógio do sistema para obter o horário atual.
As funções time.time() e stime.sleep() são as mais úteis.
'''

import time

'''
O Unix epoch (Época Unix) é uma referência de tempo comunente usada emprogramação: 00:00 hora de 1 de janeiro
de 1970 UTC. A função time.time() retorna o número de segundos desde esse momento na forma de um valor de
ponto flutuante. Esse número é chamado de epoch timestamp.

No exemplo abaixo retorna 22 de fevereiro de 2019 às 12 horas UTC. 
'''
print(time.time())

# Medindo quanto tempo demorou para executar uma instrução
# Diminuimos o tempo de inicio menos o tempo de encerramento e temos o tempo em segundos
def calcProd():
    # Calcula o produto dos 10.000 primeiros números
    product = 1
    for i in range(1, 10000):
        product *= i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()

print("The result is %s digits long." % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))


# Função sleep para quando for necessário fazer uma pausa no programa em segundos.
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)


# Arredondando números
'''
Com o round() basta passar o número que você quer arredondar, além de um segundo argumento opcional que representa 
para quantos dígitos após o ponto decimal você quer arredondar. Se o segundo argumento for omitido, round()
arredondará seu número para o inteiro mais próximo.
'''
now = time.time()
print(now) # Exibindo o tempo atual em segundos sem arredondar
print(round(now, 2)) # Redondando para 2 casas decimais após o ponto o tempo atual
print(round(now, 4)) # Redondando para 4 casas decimais após o ponto o tempo atual
print(round(now)) # Arredondando para o inteiro mais próximo.


# Para fazer uma pausa de 30 segundos utilize um loop for para fazer 30 chamadas time.sleep(1)
# Ou pode ser chamado da seguinte forma time.sleep(30)
# Para finalizar pressione CTRL+C
for i in range(30):
    time.sleep(1)

print('Aguarde mais 30 segundos')
time.sleep(30)

