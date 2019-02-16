import re

# Regra do regex
# Adicionamos o r a frente para tornar a string como pura
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Procurando com search nosso regex
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

