import os

# Com o getcwd() imprimimos o diretório que estamos navegando
print(os.getcwd())

# Com o chdir() navegamos até a pasta indicada
os.chdir('C:\\Windows\\System32')
print(os.getcwd())

# O python exibirá um erro se você tentar ir para um diretório diferente
os.chdir('C:\\Esse\\Diretorio\\Nao\\Existe')