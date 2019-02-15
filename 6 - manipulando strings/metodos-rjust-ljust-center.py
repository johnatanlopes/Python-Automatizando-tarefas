'''
Os métodos de string rjust() e ljust() retornam uma versão preenchida da string em que são chamados,
com espaços inseridos para justificar o texto. O primeiro argumento de ambos os métodos é um inteiro
referente ao tamanho da string justificada.
'''
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello'.ljust(10))

'''
Um segundo argumento opcional de rjust() e ljust() especifica um caractere de preenchimento que não seja um
caractere de espaço.
'''

print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))

'''
O método center() funciona como ljust() e rjust(), porém centraliza o texto
'''
print('Hello'.center(20))
print('Hello'.center(20, '='))
