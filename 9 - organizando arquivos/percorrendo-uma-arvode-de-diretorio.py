'''
A função os.walk() recebe um único valor de string o path de uma pasta. Pode ser usada em uma instrução de loop for para percorrer uma árvore de diretório
de modo muito semelhante à forma como a função range() é utilizada para percorrer um intervalo de números. De modo diferente de range(), a função os.walk() retornará
três valores a cada iteração pelo loop:

    1 - Uma string com o nome da pasta atual
    2 - Uma lsita de strings com a pasta da pasta atual
    3 - Uma lista de strings com os arquivos da pasta atual
'''

import os

for folderName, subFolders, fileNames in os.walk('C:\\tmp\\delicious'):
    print('The current folder is ' + folderName)

    for subFolder in subFolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subFolder)

    for fileName in fileNames:
        print('FILE INSIDE ' + folderName + ': ' + fileName)
    print('')