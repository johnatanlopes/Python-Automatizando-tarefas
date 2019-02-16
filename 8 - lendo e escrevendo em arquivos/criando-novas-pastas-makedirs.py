'''
Com o makedirs podemos criar uma arvore de pastas caso elas não exista.
No nosso exemplo abaixo não existem as pastas delicious, walnut e waffles e as três serão criadas mesmo a pai não existindo
'''

import os
os.makedirs('C:\\tmp\delicious\\walnut\\waffles')

