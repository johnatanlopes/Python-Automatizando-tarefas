import re

# Regra do regex
# Adicionamos o r a frente para tornar a string como pura
# Se precisar mostrar um parenteses na pesquisa será necessário escapa-lo
phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')

# Procurando com search nosso regex
mo = phoneNumRegex.search('My number is (415)-555-4242.')
print(mo.group(1))
print(mo.group(2))

