'''
Objeto Font()

    name - String - O nome da fonte, por exemplo 'Calibri' ou Times New Roman
    size - Integer - O tamanho em pontos
    bold - Boolean - True para fonte em negrito
    italic - Boolean - True para fonte em itálico
'''

import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb.active
italic24Font = Font(name='Times New Roman',size=24, italic=True)
a1 = sheet['A1']
a1.font = italic24Font
a1.value = 'Hello world!'

wb.save('styled.xlsx')


