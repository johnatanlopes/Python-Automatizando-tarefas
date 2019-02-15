'''
isalpha() - Retornará True se a string for constituída somente de letras e não estiver vazia

isalnum() - Retornará True se a string for constituída somente de letras e números e não estiver vazia

isdecimal() - Retornará True se a string for constituída somente de caracteres numéricos e não estiver vazia

isspace() - Retornará True se a string for constituída somente de espaços, tabulações e quebras de linha e 
    não estiver vazia

istitle() - Retornará True se a string for constituída somente de palavras que comecem com uma letra 
    maiúscula seguida somente de letras minúsculas
'''

print('hello'.isalpha())
print('hello123'.isalpha())

print('hello123'.isalnum())
print('hello'.isalnum())

print('123'.isdecimal())

print(' '.isspace())

print('Title Is Title Case'.istitle())
print('Title Is Title Case 123'.istitle())
print('This Is NOT Title Case Either'.istitle())


