import re

'''
Enquanto search() retorna um objeto Match do primeiro texto correspondente na string pesquisada, o método findall() retorna as strings
de todas as correspondências na string pesquisada. Vamos ver como search() retorna um objeto Match somente da primeira instância do texto 
correspondente
'''

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneNumberRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo1.group())

# o findall retorna uma lista de strings
print(phoneNumberRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

'''
Se houver grupos na expressão regular, findall() retornará uma lista de tuplas.
Cada tupla representa uma correspondência identificada e seus itens serão as strings correspondentes a cada grupo da regex
'''

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneNumberRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

