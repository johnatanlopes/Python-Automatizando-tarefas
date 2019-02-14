print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])

spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)
print('howdy' not in spam)
print('cat' not in spam)

# Exemplo de programa com in e not in
myPets = ['Zophie', 'Pooka', 'Fat-tail']
name = input('Enter a pet name: ')
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet')