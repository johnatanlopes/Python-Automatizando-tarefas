'''
O Beautiful Soup é um módulo usado para extrair informações de uma página HTML (E é muitop melhor para isso do que as expressões regulares). 
Para instalar pip3 install beautifulsoup4

Esse código utiliza requests.get() para fazer download da página principal do site No Starch Press e em seguida passa o atributo text da resposta para
bs4.BeautifulSoup().
'''

import requests, bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchchSoup = bs4.BeautifulSoup(res.text)
print(type(noStarchchSoup))

'''
Você também pode carregar um arquivo HTML de seu disco rígido passando um objeto File para bs4.BeautifulSoup()
'''

exampleFile = open('exemplo.html', 'r')
exampleSoup = bs4.BeautifulSoup(exampleFile)
print(exampleSoup)

'''
Encontrando um elemento com o método select()

Podemos obter um elemento de uma página web a partide de um objeto bs4.BeautifulSoup chamando o método select() e passando uma string com um seletor CSS para
o elemento que estamos procurando. Os seletores são como expressões regulares: Eles especificam um padrão a ser procurado, nesse caso, em páginas HTML em vez de 
strings de texto genéricas.


Seletores:

soup.select('div)   -   Todos os elementos de nome <div>
soup.select('#author)   -   O elemento com um id author
soup.select('.notice')  -   Todos os elementos que utilizem um atributo classe chamado notice
soup.select('div span') -   Todos os elementos de nome <span> que estejam em um elemento chamado <div>
soup.select('div > span')   -   Todos os elementos de nome <span> que estejam diretamente em um elemento chamado <div>, sem que haja outros elementos intermediários
soup.select('input[name]')  -   Todos os elementos de nome <input> que tenham um atributo name com qualquer valor
soup.select('input[type="button"]') -   Todos os elementos de nome <input> que tenham um atributo chamado type com o valor button
'''

# Extraindo o autor
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

# Extraindo o paragrafo
pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(str(pElems[1]))
print(str(pElems[2]))
print(pElems[0].getText())
print(pElems[1].getText())
print(pElems[2].getText())

''' 
Obtendo dados dos atributos de um elemento com o .get() do beautifulSoup
'''

spanElem = exampleSoup.select('span')
print(str(spanElem[0]))
print(spanElem[0].get('id'))
print(spanElem[0].get('some_nonexistent_addr') == None)
print(spanElem[0].attrs)

