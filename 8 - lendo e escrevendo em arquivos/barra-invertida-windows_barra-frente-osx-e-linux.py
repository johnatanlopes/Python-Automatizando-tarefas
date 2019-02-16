'''
No windows, os paths são escritos com barras intervidas (\) como separados entre os nomes das pastas.
No OSX e no Linux, porém, utilize a barra para frente (/) como separador de path. Se quiser que seu script python
funcione em ambos os sistema será necessário escrever para os dois.

Felizmente, isso é simples de fazer com a função os.path.join(). Se você lhe passar os valores de string com os nomes individuais dos arquivos
e das pastas de seu path, os.path.join() retornará uma string com um path de arquivo que utilizará os separadadores corretos de path.
'''

import os
print(os.path.join('usr', 'bin', 'spam'))

'''
A função os.path.join() será util se houver necessidade de criar strings para os nomes de arquivos.
'''

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\Johnatan', filename))

