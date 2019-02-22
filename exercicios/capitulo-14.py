# 1 Quais são alguns recursos presentes em planilhas Excel que não estão em planilhas CSV?
'''
Em excel, as planilhas podedm ter valores com tipos de dados que não sejam string, as células podem ter configurações de fonte, tamanho ou cores diferentes,
as células podem ter larguras e alturas variadas, células adjacentes podem ser mescladas, e você pode incluir imagens e gráficos.
'''

# 2 O que devemos passar para csv.reader() e para csv.writer() para criar objetos Reader e Writer?
'''
objeto File obtido a partir do open()
'''

# 3 Em quais modos os objetos File para objetos Reader e Writer devem ser abertos?
'''
devem ser abertos em modo de leitura binária 'rb' para objetos Reader e em modo de escrita binária 'wb' para objetos Writer
'''

# 4 Qual método aceita um argumento de lista e o grava em um arquivo CSV?
'''
writerow()
'''

# 5 O que os argumentos nomeados delimiter e lineterminator fazem?
'''
O argumento delimiter altera a string usada para separar células em uma linha. O argumento lineterminator altera a string usada para separar linhas
'''

# 6 Qual função aceita uma string com dados JSON e retorna uma estrutura de dados Python?
'''
json.loads()
'''

# 7 Qual função aceita uma estrutura de dados Python e retorna uma string com dados JSON?
'''
json.dumps()
'''