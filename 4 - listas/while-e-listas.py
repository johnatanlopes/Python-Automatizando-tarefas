catNames = []

while True:
    name = input('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.): ')
    if name == '':
        break
    catNames = catNames + [name] # Concatenação de lista
    print('The cat names are:')
    for name in catNames:
        print(' ' + name)