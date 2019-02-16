# 1 O que são caracteres de escape?
'''
São caracteres que são escapados pela contra barra \ como o ' ou "" ou a propria contra barra
'''

# 2 O que os caracteres de escape \n e \t representam?
'''
Nova linha e tabulação respectivamente
'''

# 3 Como podemos inserir um caractere de barra invertida em uma string?
'''
Utilizando duas barras \\
'''

# 4 O valor de string "Howl's Moving Castle" é uma string válida. Por que não há problema no fato de o caractere único de aspas
# simples na palavra Howl's não estar escapado?
'''
Por que a frase esta dentro de aspas duplas
'''

# 5 Se não quiser colocar \n em sua string, como você poderá escrever uma string contendo quebras de linha?
'''
Podemos utilizar aspas simples triplas ou aspas duplas triplas
'''

# 6 Para que valores as expressões a seguir são avaliadas?
'''
'Hello world!'[1]
'Hello world!'[0:5]
'Hello world!'[:5]
'Hello world!'[3:]
'''

'''
Respostas
e
Hello
Hello
lo world!
'''

# 7 Para que valores as expressões a seguir são avaliadas?
'''
'Hello world'.upper()
'Hello world'.upper().isupper()
'Hello world'.upper().lower()
'''

'''
Resposta
HELLO WORLD
True
hello world
'''

# 8 Para que valores as expressões a seguir são avaliadas?
'''
'Remember, remember, the fifth os November'.split()
'-'.join('There can be only one.'.split())
'''

'''
Resposta
['Remember,', 'remember,', 'the', 'fifth', 'os', 'November']
There-can-be-only-one.
'''

# 9 Quais métodos de string podem ser usados para justificar uma string à direita, à esquerda e para centralizá-la?
'''
rjust(), ljust() e center()
'''

# 10 Como podemos remover caracteres de espaços em branco no inicio e no fim de uma string?
'''
strip()
'''