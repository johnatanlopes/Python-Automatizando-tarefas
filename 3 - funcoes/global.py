def spam():
    global eggs
    eggs = 'spam' # essa é a variavel global

def bacon():
    eggs = 'bacon' # essa é uma variável local

def ham():
    print(eggs) # Essa é uma variável global

eggs = 42 # Essa é a variável global
spam()
print(eggs)