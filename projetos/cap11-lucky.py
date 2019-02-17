# lucky.py - Abre vários resultados de pesquisa no google

import requests, sys, webbrowser, bs4

print('Googling') # Exibe um texto enquanto faz download da página do google
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

# Obtém os links dos principais resultados da pesquisa
soup = bs4.BeautifulSoup(res.text)

# Abre uma aba do navegador para cada resultado
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))