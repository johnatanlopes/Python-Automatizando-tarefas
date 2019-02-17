#! Python3
# backupToZip.py - Copia uma pasta toda e seu conteúdo para um arquivo ZIP cujo nome seja incrementado

import zipfile, os

# Acessando o diretório
os.chdir('C:\\tmp')

def backupToZip(folder):
    # Faz backup de todo o conteúdo de folder em um arquivo zip
    folder = os.path.abspath(folder) # Garante que folder é um path absoluto

    # Determina o nome do arquivo que ese código deverá usar de acordo com os arquivos já existentes
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1

    # Cria o arquivo zip
    print('Creating %s...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # Percorre toda a àrvore de diretório e compacta os arquivos de cada pasta
    for folderName, subFolders, filenames in os.walk(folder):
        print('Adding files in %s' % (folderName))
        # Acrecenta a pasta atual ao arquivo zip
        backupZip.write(folderName)

    # Acrescenta todos os arquivos dessa pasta ao arquivo zip
    for filename in filenames:
        newBase = os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue # não faz backupo dos arquivos zip de backup
        backupZip.write(os.path.join(folderName, filename))
    
    backupZip.close()
    print('done')

backupToZip('C:\\tmp\\delicious')