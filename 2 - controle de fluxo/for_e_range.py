# Estamos passando com range o número 5 que equivale o mesmo que 1 2 3 4 5
print('My name is')
for i in range(5):
    print('Johnatan Five Times (' + str(i) + ')')

print('#################')
# Argumentos de inicio e fim no range
# Ira iniciar do 12 e finalizar no 15
for i in range(12, 16):
    print(i)


print('#################')
# Argumento de inicio, fim
# Ira imprimir do 5 ao 0
for i in range(5, -1, -1):
    print(i)

print('#################')
# Passando o incremento para o range
# Nesse caso irá imprimir de 2 em 2
for i in range(0, 10, 2):
    print(i)