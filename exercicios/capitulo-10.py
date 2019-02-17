# 1 Escreva uma instrução assert que dispare um AssertionError se a variável spam for um inteiro menor do que 10
'''
spam = 5
assert spam > 10, 'A variável spam deve receber um valor maior que 10'
'''

# 2 Escreva uma instrução assert que dispare um AssertionError se as variáveis eggs e bacon contiverem string que sejam iguais, sem considerar a diferença entre
# letras maiusculas e minusculas (ou seja, 'hello' e 'hello' são consideradas iguais, assim como 'goodbye' e 'GOODbye' também são consideradas iguais)
'''
eggs = 'Hello'
bacon = 'hello'

assert eggs.lower() != bacon.lower(), 'As variáveis eggs e bacon não podem ser iguais'
'''

# 3 Escreva uma instrução assert que sempre dispare um AssertionError
'''
assert False, 'Sempre vai disparar o assert'
'''

# 4 Quais são as duas linhas que seu programa deve ter para poder chamar logging.debug()?
'''
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
'''

# 5 Quais são as duas linhas que seu programa deve ter para poder chamar logging.debug() e enviar uma mensagem de logging para um arquivo
# chamado programLog.txt?
'''
import logging
logging.basicConfig(filename="programLog.txt", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
'''

# 6 Quais são os cinco níveis de logging?
'''
logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
'''

# 7 Qual linha de código pode ser adicionada para desabilitar todas as mensagens de logging em seu programa?
'''
logging.disable(logging.CRITICAL)
'''

# 8 Por que o uso de mensagens de logging é melhor que utilizar print() para exibir a mesma mensagem?
'''
Por que podemos desabilitar a mensagem de logging somente com um comando, já o print teriamos que apagar cada um correndo o risco de apagar alguma linha de uso 
do nosso programa
'''

# 9 Quais são as diferenças entre os botões step, over e out da janela debug control?
'''
step - Ao clicar nele é executado uma linha e pausará a execução. A lista de variáveis será atualizada. Se for uma função ela irá entrar no código da função
over - Ao clicar nele é executado uma linha e pausará a execução. Pula o código da função caso seja a proxima execução
out - Ao entrar em uma função com step pode sair com o out
'''

# 10 Após clicar em go na janela Debug Control, em que momento o debugger para?
'''
Vai parar quando terminar ou quando encontrar um breakpoint
'''

# 11 O que é um breakpoint?
'''
Quando iniciar o debug e ele encontrar um breakpoint mesmo que tenha um loop ele vai parar e aguardar uma ação do usuário
'''

# 12 Como um breakpoint é definito em uma linha de código no IDLE?
'''
Clicando com o botão direito na linha e selecionando set breakpoint
'''
