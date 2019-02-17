'''
O nosso exemplo abaixo não soma, somente concatena
Necessário utilizar a idle
    - Abrir o arquivo pela idle
    - Na idle abrir o debugger e marcar todas opções
    - No script adicionar o breakpoint na primeira linha
    - Executar o script com F5
    - Clicar em over até chegar aos inputs, passar valores e clicar em over novamente
    - Na janela do debug podemos ver que os valores passados estão como strings, encontramos o bug

'''

print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
print('The sum is ' + first + second + third)

'''
Mais sobre string, se você adicionar um breakpoint no print(i) do for abaixo, o debug sempre irá parar nessa linha
mesmo clicando no botão go. 
Na janela do debugger poderemos ver o resultado de i naquele momento
'''

for i in range(5):
    print(i)
