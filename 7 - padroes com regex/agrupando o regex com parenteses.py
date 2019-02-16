import re

# Suponha que você queira separar o código de área do restante do número de telefone.

# Regra do regex
# Adicionamos o r a frente para tornar a string como pura
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# Procurando com search nosso regex
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(1))
print(mo.group(0))
print(mo.group())

# Se quiser obter todos os grupos de uma só vez, utilize o método groups()
print(mo.groups())

# Como mo.groups() retorna uma tupla podemos usar a atribuição multipla para atribuir cada valor a uma variável
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

