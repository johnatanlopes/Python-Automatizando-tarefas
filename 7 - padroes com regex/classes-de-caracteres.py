import re

'''
O \d pode representar qualquer dígito ou seja, \d é uma versão abreviada da expressão regular (0|1|2|3|4|5|6|7|8|9).
Há várias dessas classes abreviadas de caracteres:
    
\d  -   Qualquer dígito de 0 a 9
\D  -   Qualquer caractere que não seja um dígito de 0 a 9
\w  -   Qualquer letra, dígito ou o caractere underscore
\W  -   Qualquer caractere que não seja uma letra, um dígito ou o caractere underscore
\s  -   Qualquer espaço, tabulação ou caractere de quebra de linha
\S  -   Qualquer caractere que não seja um espaço, uma tabulação ou quebra de linha

A classe de caracteres [0-5] corresponderá somente aos números de 0 a 5
'''

'''
A expressão regular \d+\s\w+ corresponderá a textos que tenham um ou mais dígitos (\d+) seguidos de um caractere de espaço em branco (\s)
seguido de um ou mais caracteres que sejam letra/dígito/underscore (\w+)
'''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 hoves, 1 partidge'))

