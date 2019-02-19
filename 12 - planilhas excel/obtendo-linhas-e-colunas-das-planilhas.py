import openpyxl, os

os.chdir('12 - planilhas excel')
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']

print(tuple(sheet['A1':'C3']))

for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--END OF ROW--')

sheet = wb.active

i = 1
while True:
    resultado = sheet.cell(row=i, column=2).value
    if resultado == None:
        break
    print(resultado)
    i += 1