# stopwatch.py - Um programa simples de cronômetro

import time
# Exibe as instruções do programa
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl+C to quit.')
input() # Tecle Enter para começar
print('Started.')
startTime = time.time() # Obtém o horário de início da primeira rodada
lastTime = startTime
lapNum = 1

# Começa a monitorar a duração das rodadas
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap # %s: %s (%s)' %(lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reinicia a última rodada
except KeyboardInterrupt:
    # Trata a exceção de Ctrl+C para evitar que sua mensagem de erro seja exibida
    print('\nDone.')