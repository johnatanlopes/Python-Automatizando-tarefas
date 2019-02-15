spam = ['apples', 'bananas', 'tofu', 'cats']

def addVirgularEmLista(lista):
    str = ''
    count = 0
    for i in lista:
        if count == len(lista) - 1:
            str += ' and ' + i
        elif count == len(lista) - 2:
            str += i
        else:
            str += i + ', '
        count += 1
    return str

print(addVirgularEmLista(spam))



