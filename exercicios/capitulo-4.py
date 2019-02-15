# 1 O que é []?
'''
Uma lista vazia
'''

# 2 Como você atribuiria o valor 'hello' como o terceiro valor de uma lista armazenada em uma variável chamada spam? (Suponha que spam contenha [2, 4, 6, 8, 10])
'''
spam[2] = 'hello'
'''

# Para as três perguntas a seguir, vamos supor que spam contenha a lista ['a', 'b', 'c', 'd']
# 3 Para que valor spam [int(int('3' * 2) / 11)] é avaliado?
'''
spam[3]
'''

# 4 Para que valor spam[-1] é avaliado?
'''
d
'''

# 5 Para que valor spam[:2] é avaliado?
'''
a, b
'''

# Para as três perguntas a seguir, vamos supor que bacon contenha a lista [3.14, 'cat', 11, 'cat', True]
# 6 Para que valor bacon.index('cat') é avaliado?
'''
1
'''

# 7 Como bacon.append(99) altera o valor de lista em bacon?
'''
[3.14, 'cat', 11, 'cat', True, 99]
'''

# 8 Como bacon.remove('cat') altera o valor de lista em bacon?
'''
[3.14, 11, 'cat', True]
'''

# 9 Quais são os operadores para concatenação de lista e para repetição delista?
'''
+ e *
'''

# 10 Qual é a diferença entre os métodos de lista append() e insert()?
'''
O append adiciona o valor ao final da lista
O insert adiciona o valor informando o número do indice
'''

# 11 Quais são as duas maneiras de remover valores de uma lista?
'''
com as funções del e remove
'''

# 12 Nomeie alguns aspectos em relação aos quais os valores de lista são semelhantes aos valores de strings?
'''
Com listas e strings podemos fazer slicing e acessar seus valores por index
'''

# 13 Qual a diferença entre listas e tuplas?
'''
Listas usam colchetes, tuplas utilizam parenteses
Listas são mutaveis, tuplas são imutaveis
'''

# 14 Como você deve digitar o valor de uma tupla que contenha somente o valor inteiro 42?
'''
(42,)
'''

# 15 Como podemos obter a forma de tupla de um valor de lista? Como podemos obter a forma de lista de um valor de tupla?
'''
tuple(['a', 'b'])
list(('a', 'b'))
'''

# 16 As variáveis que contêm valores de lista não contêm realmente as listas diretamente. O que elas contêm em seu lugar?
'''
Contém uma referência que apontam para a lista
'''

# 17 Qual é a diferença entre copy.copy() e copy.deepcopy()?
'''
Ambas criam um clone de uma lista sem utilizar referência, com a diferença que o deepcopy clona listas internas de uma lista, o copy não
'''