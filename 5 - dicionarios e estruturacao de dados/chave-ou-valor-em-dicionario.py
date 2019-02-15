spam = {'name': 'Zophie', 'age': 7}

print('name'in spam.keys())
print('Zophie' in spam.values())
print('color' in spam.keys())
print('color' not in spam.keys())
print('color' in spam) # Por padrão quando não informamos o método ele assumirá o keys()
