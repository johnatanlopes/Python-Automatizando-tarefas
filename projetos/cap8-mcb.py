#! Python3.7.2
# mcb.py - Salva e carrega porções de texto no clipboard
# Usage: py.exe mcb.py save <palavra-chave> - Salva clipboard na palavra-chave
#   py.exe mcb.py <palavra-chave> - Carrega palavra chave no clipboard
#   py.exe mcb.py list - Carrega todas as palavra-chave no clipboard
#   py.exe mbc.py delete <palavra-chave> - Deleta a palavra-chave
#   py.exe mbc.py delete-all - Deleta todas as palavras


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Salva conteúdo do clipboard
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf.keys():
        del mcbShelf[sys.argv[2]]
    else:
        print('Chave não encontrada')
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete-all':
    for key in mcbShelf.keys():
        del mcbShelf[key]
elif len(sys.argv) == 2:
    # Lista palavras-chave e carrega conteúdo
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()