import subprocess

# No Windows
# subprocess.Popen('C:\\Windows\\System32\\calc.exe')

# No Linux
# subprocess.Popen('/usr/bin/gnome-calculator')

'''
O valor ded retorno é um objeto Popen que tem dois métodos úteis: poll() e wait()

Podemos pensar no método poll() como se você estivesse perguntando a uma amiga se ela acabou de executar o código que você lhe deu.
O método poll() retornará None se o processo ainda estiver executando quando poll() for chamado. Se o programa tiver terminado um inteiro referente 
ao código de saída (exit code) do processo será retornado. Um código de saída é usado para indicar se o processo terminou sem erros (um código de saída igual a 0)
ou se um erro fez o processo terminar (um código de saída diferente de zero, geralmente é 1, mas pode variar conforme o programa).

O método wait() é como esperar sua amiga acabar de usar seu código antes que você possa trabalhar no seu. O método wait() ficará bloqueado até que o processo
iniciadotenha terminado. Isso é útil se você quiser que seu programa faça uma pausa até que o usuário acabe de usar o outro programa. O valor de retorno de wait()
um inteiro com o código de saída do processo.
'''

calcProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
print(calcProc.poll() == None)
print(calcProc.wait())
print(calcProc.poll())

# Passando argumentos da linha de comando a Popen()
subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\tmp\\spam.txt'])