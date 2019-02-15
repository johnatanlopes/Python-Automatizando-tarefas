'''
Às vezes você pode querer remover caracteres de espaços em branco, tabulação e quebra de linhas do lado
esquerdo, direito ou em ambos
'''

# Para remover ambos espaços em branco
print('  Hello World   '.strip())

# Para remover espaços em branco no lado esquerdo
print('  Hello World   '.lstrip())

# Para remover espaços em branco no lado direito
print('  Hello World   '.rstrip())

'''
Opcionalmente um argumento do tipo string especificará quais caracteres deverão ser removidos 
das extremidades.
'''

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

'''
A ordem dos caracteres na string passada para strip() não importa, strip('ampS') fará o mesmo que
strip('mapS') ou strip('Spam')
'''