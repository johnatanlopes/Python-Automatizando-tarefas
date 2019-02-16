import re

# O ^ pode ser usado no inicio de uma regex para indicar que uma correspondência deve ocorrer no ínicio
beginWithHello = re.compile(r'^Hello')
print(beginWithHello.findall('Hello World!'))

# O $ pode ser usado no fim de uma regex para indicar que uma correspondência deve ocorre no final
endWithWorld = re.compile(r'World!$')
print(endWithWorld.findall('Hello World!'))

endsWithNumber = re.compile(r'\d+$')
print(endsWithNumber.findall('Your number is 42'))

# também podemos utilizar o ^ e o $ juntos
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.findall('123456789'))
print(wholeStringIsNum.findall('123456789 numeros'))

