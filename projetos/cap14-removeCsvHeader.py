# removeCsvHeader.py - Remove o cabeçalho de todos os arquivos CSV no diretório de trabalho atual

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Percorre todos os arquivos no diretório de trabalho atual em um loop
for csvFileName in os.listdir('.'):
    if not csvFileName.endswith('.csv'):
        continue # ignora arquivos que não sejam csv

    print('Removing header from ' + csvFileName + '...')

    # Lê o arquivo CSV (Pula a primeira linha)
    csvRows = []
    csvFileObj = open(csvFileName)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # pula a primeira linha
        csvRows.append(row)
    csvFileObj.close()

    # Grava o arquivo CSV
    csvFileObj = open(os.path.join('headerRemoved', csvFileName), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()