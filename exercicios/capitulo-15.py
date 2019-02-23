# 1 O que é o Unix epoch (Era Unix ou Época Unix)?
'''
É um instante de referência que muitos programas que manipulam data e hora utilizam. Esse instante corresponde a 1 de janeiro de 1970 UTC
'''

# 2 Qual função retorna o número de segundos desde o Unix epoch?
'''
time.time()
'''

# 3 Como podemos fazer uma pausa de exatamente cinco segundos em um programa?
'''
time.sleep(5)
'''

# 4 O que a função round() retorna?
'''
Um inteiro arredondado para o mais próximo
'''

# 5 Qual é a diferença entre um objeto datetime e um objeto timedelta?
'''
Um objeto datetime representa um instante específico no tempo. Um objeto timedelta representa uma duração
'''

# 6 Suponha que você tenha uma função chamada spam(). Como podemos chamar essa função e executar seu código em uma thread separada?
'''
threadObj = threading.Thread(target=spam)
'''

# 7 O que devemos fazer para evitar problemas de concorrência com várias threads?
'''
Certifique-se de que o código que executar em uma thread não leia nem escreva nas mesmas variáveis que o código que estiver executando outra thread.
'''

# 8 Como podemos fazer seu programa Python executar o programa calc.exe localizado na pasta C:\Windows\System32?
'''
subprocess.Popen('C:\\Windows\\System32\\calc.exe')
'''