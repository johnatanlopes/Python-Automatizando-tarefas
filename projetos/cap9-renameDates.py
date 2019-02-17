#! Python3
# renameDates.py - Renomeia os nomes de arquivos com formato de data MM-DD-AAA em estilo americano para o formato DD-MM-AAAA

import shutil, os, re

# Cria uma regex que corresponda aos arquivos com formato de data em estilo americano
datePattern = re.compile(r'''
^(.*?)              # Todo o texto antes da data
((0|1)?\d)-         # Um ou dois dígitos para o mês
((0|1|2|3)?\d)-     # um ou dois dígitos para o dia
((19|20)\d\d)       # quatro dígitos para o ano
(.*?)$              # todo o texto após a data
''', re.VERBOSE)

# Acessa o diretório
os.chdir('C:\\tmp')

# Percorre os arquivos do diretório de trabalho com um loop
for amerFilename in os.listdir('C:\\tmp'):
    mo = datePattern.search(amerFilename)

    # Ignora os arquivos que não tenham uma data
    if mo == None:
        continue

    # Obtém as diferentes partes do nome do arquivo
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Compõe o nome do arquivo para o novo padrão
    newFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Obtém os paths absolutos completos dos arquivos
    absWorkingDir = os.path.abspath('C:\\tmp')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    newFilename = os.path.join(absWorkingDir, newFilename)

    # Renomeia os arquivos
    print('Renaming "%s" to "%s"...' % (amerFilename, newFilename))
    shutil.move(amerFilename, newFilename)