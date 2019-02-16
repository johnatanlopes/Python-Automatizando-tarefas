import re

'''
Se quiser uma regex que ignore as diferenças de letras maiusculas e minusculas e inclua quebras de linha para que correspondam
ao caractere ponto, sua chamada a re.compile() deverá ser feita da seguinte forma:
'''
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)

# Podemos adicionar o verbose utilizando o pipe
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)