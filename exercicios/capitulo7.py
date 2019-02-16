# Qual é a função que cria objetos Regex?
'''
re.compile()
'''

# 2 Por que as strings puras (raw strings) geralmente são usadas na criação de objetos regex?
'''
Para todo o texto ser acessado, ignorando os escapes de quebra de linha, tabulação, etc
'''

# 3 O que o método search() retorna?
'''
Retorna um objeto Match do que foi encontrado
'''

# 4 Como podemos obter as strings correspondentes ao padrão a partir de um objeto Match?
'''
utilizando o método group() ou  groups()
'''

# 5 Na regex criada a partidr de r'(\d\d\d)-(\d\d\d-\d\d\d\d)' o que op grupo 0 inclui? e o grupo 1? e o grupo 2?
'''
grupo 0 todo a pesquisa (\d\d\d)-(\d\d\d-\d\d\d\d)
grupo 1 retorna o primeiro grupo (\d\d\d)
grupo 2 retorna o segundo grupo (\d\d\d-\d\d\d\d)
'''

# 6 Os parentereses e os pontos tem sifnificados especificos na sintaxe da regex. Como podemos especificar uma regex que corresponda aos caracteres
# que representam parenteseses e pontos?
'''
Escapando elas com \
    \(
    \.
'''

# 7 O método findall() retorna uma lista de strings ou uma lista de tuplas de strings. O que faz com que uma ou outra opção seja
# retornada?
'''
Retorna listas quando não utilizamos parenteses para formar grupos
E retorna tuplas quando formamos os grupos
'''

# 8 O que o caractere | representa em expressões regulares?
'''
Representa o OR
'''

# 9 Quais são os dois significados do caractere ? em expressões regulares?
'''
? Deixa algo opcional
? Deixa o {3,5} não guloso
'''

# 10 Qual é a diferença entre os caracteres + e * em expressões regulares?
'''
+ um ou mais caracteres
* zero ou mais caracteres
'''

# 11 Qual é a diferença entre {3} e {3,5} em expressões regulares?
'''
{3} vai encontrar no máximo 3
{3,5} vai encontrar no máximo 5, se existir 3 ela vai retornar sempre a maior encontrada
'''

# 12 O que as classes abreviadas de caracteres \d, \w e \s representam?
'''
\d - dígitos númericos
\w - digitos numericos, letras e underscore
\s - Espaços, tabulações e quebras de linhas
'''

# 13 O que as classes abreviadas de caracteres \D, \W e \S representam em expressões regulares?
'''
\D - Qualquer caractere que não seja um dígito
\W - Qualquer caractere que não seja um digito, letra ou underscore
\S - Qualquer caractere que não seja um espaço, tabulação ou quebra de linha
'''

# 14 Como podemos fazer uma regex ignorar as diferenças entre letras maiusculas e minusculas?
'''
Adicionando ao re.compile('', re.IGNORECASE)
'''

# 15 A que o caractere . normalmente corresponde? A que ele corresponderá se re.DOTALL for passado como segundo argumento de re.compile()?
'''
O ponto representa um caractere sem ser uma quebra de linha
Se passar o re.DOTALL o ponto vai corresponder a todos os caracteres até a quebra de linha
'''

# 16 Qual é a diferença entre .* e .*??
'''
O .* vai trazer tudo que encontrar sendo guloso
o .*? vai trazer o minimo que encontrar não guloso
'''

# 17 Qual é a sintaxe da classe de caracteres que corresponde a todos os números e a todas as letras minusculas?
'''
[\d]+|[a-z]+
'''

# 18 Se numRegex = re.compile(r'\d+'), o que numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') retornará?
'''
'X drummers, X pipers, five rings, X hens'
'''

# 19 O que a especificação de re.VERBOSE como segundo argumento de re.compile() permite fazer?
'''
Ele ignora as quebras de linhas na regex e pode ser adicionado comentários para facilitar a visualização de expressões difíceis
'''

# 20 Como você poderá escrever uma regex que corresponda a um número com vírgulas a cada três dígitos? Ele deverá corresponder a:
'''
42
1,234
6,368,745

mas não a:
12,34,567 (que tem somente dois dígitos entre as virgulas)
1234 (que não tem virgulas)
'''

'''
Resposta
^(\d{1,3})(\,\d{3}.*)?$
'''

# 21 Como você poderá escrever uma regex que corresponda ao nome completo de alguém cujo sobrenome seja Nakamoto? Suponha que o primeiro nome que vem antes dele
# sempre seja uma única palavra que comece com uma letra maiúscula. A regex deverá corresponder a:
'''
Satoshi Nakamoto
Alice Nakamoto
Robocop Nakamoto

Mas não a:
satoshi Nakamoto (primeiro nome começa com letra minuscula)
Mr. Nakamoto (em qua a palavra tem um caractere que não é uma letra)
Nakamoto (que não tem primeiro nome)
Satoshi nakamoto (em que Nakamoto não começa com letra maiuscula)
'''

'''
Resposta
^([A-Z]\w+)\sNakamoto
'''

# 22 Como você poderá escrever uma regex que corresponda a uma frase em que a primeira palavra seja Alice, Bob ou Carol, a segunda palavra seja eats,
# pets ou throws, a terceira palavra seja apples, cats ou baseballs e a frase termine com um ponto? Essa regex não deve diferenciar letras maiusculas 
# de minusculas. Ela deve corresponder a:
'''
Alice eats apples.
Bob pets cats.
Carol throws baseballs.
Alice throws Apples.
BOB EATS CATS.

Mas não a:
RoboCop eats Apples.
ALICE THROWS FOOTBALLS.
Carol eats 7 cats.
'''

'''
Resposta
^[A-Z]([a-z]+|[A-Z]+)\s(EATS|..ts|throws)\s([Aa]pples|CATS|cats|baseballs)\.
'''