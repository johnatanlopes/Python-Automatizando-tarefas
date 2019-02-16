'''
Um path absoluto, que sempre começa com a pasta raiz.
Um path relativo, que é relativo ao diretório de trabalho atual do programa.

Temos também as pastas ponto (.) e ponto-ponto (..). Essas não são pastas ded verdade, mas nomes especiais que podem ser usados
em um path. Um único ponto é abreviação para este diretório, dois pontos quer dizer a pasta pai
''' 

# Lidando com paths absolutos e relativos

'''
O modulo os.path disponibiliza funções que retornam o patha bsoluto de um path relativo e para verificar se um dado path representa um path absoluto.

os.path.abspath(path) - Retornará uma string com o path absoluto referente ao argumento. Essa é uma maneira fácil de converter um path relativo
em um path absoluto.

os.path.isabs(path) - Retornará True se o argumento for um path absoluto e False se for um path relativo.

os.path.relpath(path, inicio) - Retornará uma string contendo um path relativo ao path inicio para path. Se inicio não for especificado o diretório
de trabalho atual será usado como path de inicio
'''

import os

# Mostrando o path absoluto
print(os.path.abspath('.'))

# Verificando se estamos em um path absoluto
print(os.path.isabs('.'))

# Passando o path absoluto para verificar se é True ou False
print(os.path.isabs(os.path.abspath('.')))

# Exibindo o diretório relativo para C:\\Windows
print(os.path.relpath('C:\\Windows', 'C:\\'))

# Exibindo o diretório relativo para C:\\Windows
print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))

# Imprimindo o diretório corrente
print(os.getcwd())

'''
Chamar os.path.dirname(path) retornará uma string contendo tudo que estiver antes da última barra no argumento path.
Chamar os.path.basename(path) retornará uma string contendo tudo que estiver após a última barra no argumento path.
'''

path = 'C:\\Windows\\System32\\Calc.exe'

# Imprime o nome do programa que é Calc.exe
print(os.path.basename(path))

# Imprime o caminho absoluto onde se encontra o programa
print(os.path.dirname(path))

'''
Se o nome de diretório e o nome base de um path forem necessário ao mesmo tempo, você poderá simplesmente chamar os.path.split() para
obeter um valor de tupla contendo essas duas strings.
'''
print(os.path.split(path))

'''
Observe que o mesmo valor anterior pode ser criado da seguinte forma:
'''
print((os.path.dirname(path), os.path.basename(path)))

'''
Porém os.path.split() será um atalho conveniente se você precisar de ambos valores.

Além disso, observe que os.path.split() não recebe um path de arquivo e retorna uma lista de strings com cada pasta. Para isso utilize o método
de string split() e separe a string em os.sep.
'''
print(path.split(os.path.sep))

# Em sistemas OSX e Linux
print('/usr/bin'.split(os.path.sep))