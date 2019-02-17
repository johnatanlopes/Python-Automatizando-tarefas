'''
Em vez de exibir as mensagens de log na tela, podemos gravá0las em um arquivo texto. A função logging.basicConfig() aceita um argumento
nomeado filename.

As mensagens de log serão salvadas em myProgramLog.txt. Apesar de serem úteis, as mensagens de logging podem congestionar sua tela e dificultar a leitura
da saída do programa. Gravar mensagens de logging em um arquivo manterá sua tela limpa e fará suas mensagens serem armazenadas para que possam ser lidas
após a execução do programa. Esse arquivo de log poderá ser aberto em qualquer editor
'''

import logging
logging.basicConfig(filename="myProgramLog.txt", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')