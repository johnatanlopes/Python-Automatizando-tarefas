# Strings literais
'''
Strings começam e terminam com aspas simples. Mas como é possível utilziar aspas simples
dentro de uma string? Digitar 'That is Alice's cat' não funcionará, pois o Python achará que a string termina
após Alice e que o restante (s cat') é um código inválido. Felizmente a diversas maneiras de digitar strings
'''

# Aspas duplas
'''
Podem começar e terminar com aspas duplas, assim como ocorre com as aspas simples. Uma vantagem de usar aspas duplas
está no fato da string poder conter um caractere de aspas simples:

    spam = "That is Alice's cat"

'''

# Caracteres de escape
'''
Um caractere de escape permite usar caracteres que, de outra maneira, não poderiam ser incluídos em uma string.
Um caractere de escape é constituído de uma barra invertida (\) seguida do caractere que você deseja 
incluir na string

    spam = 'Say hi to Bob\'s mother'

Caracteres de escape
\' Aspas simples
\" Aspas duplas
\t Tabulação
\n Quabra ou mudança de linha
\\ Barra invertida

'''

# Strings puras
'''
Podemos inserir um r antes das apas de ínicio em uma string para transformá-la em uma string pura.
Uma string pura (raw string) ignora todos os caracteres de escape e exibe qualquer barra invertida
que estiver na string.

    print(r"That is Carol\'s cat")

'''

# Strings de múltiplas linhas com aspas triplas
'''
Uma string de múltiplas linhas começa e termina com três aspas simples ou três aspas duplas

    print("""Dear Alice,
    
    Eve's cat has been arested for catnapping, cat burglary, and extortion.
    
    Sincerely,
    Bob""")

'''
