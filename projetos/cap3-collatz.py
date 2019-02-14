def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
   num = int(input('Digite um numero inteiro:'))
   while True:
    resultado = collatz(num)
    num = resultado
    print(resultado)
    if (resultado == 1):
        break
except ValueError:
    print('Por favor digite somente numeros inteiros')
