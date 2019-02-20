# 1 O que a função openpyxl.load_workbook() retorna?
'''
Retorna o objeto Workbook
'''

# 2 O que o método de workbook shetnames retorna?
'''
Retorna o nome das planilhas
'''

# 3 Como podemos obter o objet Worksheet de uma planilha chamada Sheet1?
'''
wb['Sheet2']
'''

# 4 Como podemos objet o objeto Worksheet da planilha ativa do workbook?
'''
wb.active
'''

# 5 Como podemos obter o valor que está na célula C5?
'''
sheet['C5'].value
'''

# 6 Como podemos definir o valor da célula C5 para 'Hello'?
'''
sheet['C5'] = 'Hello'
'''

# 7 Como podemos obter a linha e a coluna da célula na forma de inteiros?
'''
Utilize cell.row e cell.column
'''

# 8 O que os métodos max_row e max_column retornam e qual é o tipo de dado desses valores retornados?
'''
max_row retorna o máximo de linhas e max_column retorna o máximo de colunas.
Os dois retornam do tipo int
'''

# 9 Se for preciso obter o índice inteiro da coluna 'M' que função devemos chamar?
'''
openpyxl.cell.column_index_from_string('M')
'''

# 10 Se for preciso obter o nome em string da coluna 14, que função devemos chamar?
'''
openpyxl.cell.get_column_letter(14)
'''

# 11 Como podemos obter uma tupla com todos os objetos Cell de A1 a F1?
'''
sheet['A1':'F1']
'''

# 12 Como podemos salvar o workbook em um arquivo chamado example.xlsx?
'''
wb.save('example.xlsx')
'''

# 13 Como definimos uma fórmula em uma célula?
'''
Uma formula é definida da mesma maneira que qualquer valor. Definida o atributo value da célula com uma string contendo o texto da fórmula
'''

# 14 Se quisermos obter o resultado da fórmula de uma célula e não a fórmula da célula o que devemos fazer antes?
'''
Ao chamar load_workbook(), passe True para o argumento nomeado data_only
'''

# 15 Como podemos definir a altura da linha 5 para 100?
'''
sheet.row_dimension[5].height = 100
'''

# 16 Como podemos ocultar a coluna C?
'''
sheet.column.dimension['C'].hidden = True
'''

# 17 Nomeie alguns recuros que o OpenPyXL não carrega a partir de um arquivo de planilha?
'''
Não carrega painéis congelados, não exibe títulos, imagens ou gráficos
'''

# 18 O que é um painel congelado?
'''
São linhas e colunas que sempre aparecerão na tela. Utilizados como cabeçalhos
'''