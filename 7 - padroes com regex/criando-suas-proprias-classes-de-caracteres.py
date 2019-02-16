import re

# [aeiouAEIOU] corresponderá a qualquer vogal
# também é possível incluir intervalos de letras ou de números usando um hífen [a-zA-Z0-9] corresponderá a todas as letras minúsculas, letras maiúsculas e aos números
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD'))

# Ao inserir um acento circunflexo (^) logo depois do colchete de abertura da classe de caracteres, podemos criar uma classe negativa
# Corresponderá a todos os caracteres que não estejam na classe
vowelRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD'))