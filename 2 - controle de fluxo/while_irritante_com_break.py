# O while será finalizado somente quando digitar 'your name'

name = ''

while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break

print('Thank your!')