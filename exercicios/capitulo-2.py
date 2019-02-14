# 1 Quais são os dois valores do tipo de dado booleano? Como eles são escritos?
'''
True e False
'''

# 2 Quais são os três operadores booleanos
'''
and, or e not
'''

# 3 Escreva as tabelas verdade de cada operador booleano (ou seja, todas as combinações possíveis de valores booleanos para o operador e como elas são avaliadas)
'''
True and True = True
True and False = False
False and True = False
False and False  = False

True or True = True
True or False = True
False or True = True
False or False  = False

not True = False
not False = True
'''

# 4 Para que valores as expressões a seguir são avaliadas?
'''
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False) 
(not False) or (not True) 
'''

'''
Respostas
False
False
True
False
False
True
'''

# 5 Quais são os seis operadores de comperação?
'''
==
!=
>
<
>=
<=
'''

# 6 Qual é a diferença entre o operador "igual a" e o operador de atribuição?
'''
O operador de == faz uma comparação retornando um valor booleano
O operador de = atribui um valor a uma variável
'''

# 7 - Explique o que é uma condição e quando você usaria uma?
'''
Uma condição verifica se uma expressão é True ou False
Para verificar se um determinado valor é igual a outro
'''

# 8 Identifique os três blocos no código a seguir:
'''
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham)
    print('spam')
print('spam')
'''

'''
Resposta
primeiro bloco inicia em if spam == 10:
segundo bloco inicia em if spam > 5:
terceiro bloco inicia em else:
'''

# 9 Escreva um código que exiba Hello se 1 estiver armazenado em spam, Howdy se 2 estiver armazenado em spam e Greetings! se outro valor estiver em spam.
'''
spam = 3
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
'''

# 10 Que tecla você deve pressionar se o seu programa estiver preso em um loop infinito?
'''
CTRL + C
'''

# 11 Qual é a diferença entre break e continue?
'''
Se encontrar algum break ele para o loop de vez, se encontrar algum continue ele pula para a próxima etapa do loop
'''

# 12 Qual é a diferença entre range(10), range(0, 10) e range(0, 10, 1) em um loop for?
'''
Nenhuma diferença, todos os três vão mostrar o mesmo resultado
'''

# 13 Crie um pequeno programa que mostre os números de 1 a 10 usando um loop for. Em seguida, crie um programa equivalente que mostre os números de 1 a 10 usando um loop while
'''
for i in range(1, 11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1
'''

# 14 Se você tivesse uma função chamada bacon() em um módulo chamado spam, como você a chamaria após ter importado spam?
'''
spam.bacon()
'''

# Extra
# Dê uma olhada nas funções round() e abs() na Internet e descubra o que elas fazem. Faça experimentos com elas no shell interativo