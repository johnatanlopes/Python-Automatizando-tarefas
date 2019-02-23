# countDown.py - Um script simples para contagem regressiva

import time, subprocess

timeLeft = 60

while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft -= 1

# No final da contagem regressiva reproduz um arquivo de áudio
subprocess.Popen(['start', 'alarm.wav'], shell=True)
