# 1 Qual é a aparência do código para criar um dicionário vazio?
'''
dicionario = {}
'''

# 2 Qual é a aparência de um valor de dicionário com uma chave igual a 'foo' e um valor de 42?
'''
dicionario = {'foo': 42}
'''

# 3 Qual é a principal diferença entre um dicionário e uma lista?
'''
No dicionário podemos adicionar ao indice qualquer tipo de valor, podendo ser
inteiro, float ou string
'''

# 4 O que acontecerá se você tentar acessar spam['foo'] se spam for igual a {'bar': 100}?
'''
Retornará KeyError, pois não existe o índice solicitado
'''

# 5 Se um dicionário estiver armazenado em spam, qual será a diferença entre as expressões 'cat' in spam e 'cat' in spam.keys()?
'''
Retornará false, e as duas formas levam ao mesmo caminho, por padrão 
quando não passamos o método ele pega por padrão o keys()
'''

# 6 Se um dicionário estiver armazenado em spam, qual será a diferença entre as expressões 'cat' in spam e 'cat' in spam.values()?
'''
A primeira irá procurar nos indices, já o segundo nos valores
'''

# 7 Qual seria um atalho para o código a seguir?
#   if 'color' not in spam:
#       spam['color'] = 'black'
'''
spam.setdefault('color', 'black');
'''

# 8 Qual módulo e qual função podem ser usados para fazer uma apresentação elegante (pretty print) dos
# valores do dicionário?
'''
Módulo pprint e método pprint
'''