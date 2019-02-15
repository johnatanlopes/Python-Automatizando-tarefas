'''
Com o método get podemos verificar se uma chave existe sem retornar um erro, se existir retorna o valor, se não retorna o que for decidido como segundo parametro
'''

pcnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(pcnicItems.get('cups', 0)) + ' cups')
print('I am bringing ' + str(pcnicItems.get('eggs', 0)) + ' cups')