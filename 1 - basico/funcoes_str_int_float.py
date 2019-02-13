print(str(0))
print(str(-3.14))

print(int('42'))
print(int('-99'))
print(int(1.99))

print(float('3.14'))
print(float(10))

# Quando recebemos algum parametro via input sem alterar o tipo dela estamos repassando uma string
spam = input() 
print(spam) 

# Podemos pegar o que digitamos e alterar para inteiro
print(int(spam))

# A função int também é util quando precisamos arredondar um ponto flutuante para baixo
print(int(7.7))
print(int(7.7) + 1)
