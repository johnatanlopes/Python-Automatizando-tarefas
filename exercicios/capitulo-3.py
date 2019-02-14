# 1 Por que é vantajoso ter funções em seus programas?
'''
Para não ficar repetindo código
'''

# 2 Em que momento o código de uma função é executado: Quando a função é definida ou quando ela é chamada?
'''
Quando é chamada
'''

# 3 Que instrução cria uma função?
'''
def spam():
'''

# 4 Qual é a diferença entre uma função e uma chamada de função?
'''
A função é parte do código estatica aguardando ser chamada para execução
A chamada da função é quando pedimos para executar seus dados
'''

# 5 Quantos escopos globais existem em um programa Python? Quantos escopos locais?
'''
Um escopo global no programa e um escopo local a cada função criada
'''

# 6 O que acontece às variaveis em um escopo local quando a chamada da função retorna?
'''
As variáveis do escopo local são destruidas
'''

# 7 O que é um valor de retorno? Um valor de retorno pode fazer parte de uma expressão?
'''
O valor de retorno é o resultado de uma função e sim ela pode fazer parte de uma determinada expressão
'''

# 8 Se uma função não tiver uma instrução de retorno, qual será o valor de retorno de uma chamada a essa função?
'''
None
'''

# 9 Como podemos fazer com que uma variável em uma função refira-se a variável global?
'''
Adicionando a palavra 'global' e logo em seguida o nome da variável
global eggs
'''

# 10 Qual é o tipo de dado de None?
'''
NoneType
'''

# 11 O que a instrução import areallyourpetsnamederic faz?
'''
Retorna erro, pois o modulo não existe ou não foi encontrado
'''

# 12 Se você tivesse uma função chamada bacon() em um módulo chamado spam, como você a chamaria 
# após ter importado spam?
'''
spam.bacon()
'''

# 13 Como podemos evitar que um programa falhe quando houver um erro?
'''
Utilizando try e exception
'''

# 14 De que é composto a cláusula try? De que é composta a cláusula except?
'''
O try contém o código a ser executado, já a except contem a exception que indica qual erro ela irá tratar
'''