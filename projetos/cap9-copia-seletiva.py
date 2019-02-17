#! Python3
# cap9-copia-seletiva.py - Copia arquivos filtrando a extensão

import re, shutil, os

# Transforma em diretório atual
os.chdir('C:\\tmp')

# Função que recebe o destino
def copyArquivos(folder):

    # Regex para verificar a extensão
    verificaExtensao = re.compile(r'^(.*\.)(pdf|jpg|png)')

    # Loop para verificar a extensão e copiar o arquivos
    for fileName in os.listdir('C:\\tmp'):
        file = verificaExtensao.search(fileName)

        # Se retornou None o arquivo não é indicado para copia
        if file != None:

            # Pega o caminho absoluto
            fileAbs = os.path.abspath(fileName)
            folderAbs = os.path.abspath(folder)

            print('Copiando arquivo %s para a pasta %s...' % (fileAbs, folderAbs))

            # Inicia a cópia
            shutil.copy(fileAbs, folderAbs)
    print('Done')

copyArquivos('C:\\tmp\\nova-pasta')