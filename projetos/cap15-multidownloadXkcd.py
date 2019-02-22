# multidownloadXkcd.py - Faz download das tirinhas KXCD usando várias threads

import requests, os, bs4, threading

# Armazena as tirinhas em ./xkcd
os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Faz download da pagina
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features="html.parser")

        # Encontra o URL da imagem da tirinha
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Faz o download da imagem
            print('Downloading imagem %s...' % ('http' + comicUrl))
            res = requests.get('http:' + comicUrl)
            res.raise_for_status()

            # Salva a imagem em .xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


# Cria e inicia os objetos Thread
downloadThreads = [] # uma lista com todos os objetos Thread
for i in range(0, 1400, 100): # Executa o loop 14 vezes e cria 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

'''
A thread principal prosseguirá normalmente enquanto as demais threads que criamos fazem download das tirinhas. 
No entando suponha que há um código que você não queira executar na thread principal até que todas as threads
tenham sido concluídas. Chamar o método join() de um objeto Thread deixará o código bloqueado até essa thread
ser finalizado. Ao usar um loop for para fazer uma iteração por todos os objetos Thread na lista downloadThreads a 
thread principal poderá chamar o método join() em cada uma das demais threads.

Dessa forma a string Done. não será exibida até que todas as chamadas a join() tenham retornado.
Se um objeto Thread já tiver terminado quando seu método join() for chamado, o método simplesmente retornará 
de imediato.
'''

# Esperar todas as threads terminarem
for downloadThread in downloadThreads:
    downloadThread.join()

print('Done.')