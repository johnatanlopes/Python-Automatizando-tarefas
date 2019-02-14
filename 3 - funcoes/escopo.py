# Variaveis locais não podem ser usadas no escopo global
'''
def spam():
    eggs = 31337
spam()
print(eggs)
'''

# Escopos locais não podem usar variáveis de outros escopos locais
'''
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()
'''

# Variaveis globais podem ser lidas a partir de um escopo local
'''
eggs = 42

def spam():
    print(eggs)

spam()
print(eggs)
'''

# Variaveis locais e globais com o mesmo nome
'''
def spam():
    eggs = 'spam local'
    print(eggs) # exibe 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # exibe 'bacon local'
    spam()
    print(eggs) # exibe 'bacon local'

eggs = 'global'
bacon()
print(eggs) # exibe 'global'
'''

