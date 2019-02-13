'''
Os três operadores booleanos (and, or e not) são usados para comparar valores booleanos.
'''

# Tabela verdade para o operador and
'''
True and True = True
True and False = Faslse
False and True = False
False and False = False
'''

# Tabela verdade para o operador or
'''
True or True = True
True or False = True
False or True = True
False or False = False
'''

# Tabela verdade para o operador not
'''
not True = False
not False = True
'''

# Misturando operadores booleanos e de comparação
print((4 < 5) and (5 < 6))
print((4 < 5) and (9 < 6))
print((1 == 2) or (2 == 2))

# Também podemos usar vários operadores booleanos em uma expressão juntamente com operadores de comparação
print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)