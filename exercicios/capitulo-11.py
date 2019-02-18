# 1 - Descreva brevemente as diferenças entre os módulos webbrowser, requests, BeautifulSoup e selenium?
'''
O módulo webbrowser tem um métopdo open() que apenas iniciará um navegador web em um url específico. O módulo requests pode fazer download de arquivos
e de páginas da web. O módulo beautifulSoup faz parse de html. Por fim, o módulo selenium pode iniciar e controlar um navegador
'''

# 2 Que tipo de objeto é retornado por requests.get()? Como podemos acessar o conteúdo baixado na forma de um valor de string?
'''
A função requests.get() retorna um objeto Response; Seu atributo text contém os dados baixados na forma de uma string.
'''

# 3 Que método de Requests verifica se o download funcionou?
'''
O método raise_for_status() gera uma exceção se o download teve problemas e não faz nada se foi bem sucedido
'''

# 4 Como o código de status HTTP de uma resposta de Requests pode ser obtido?
'''
O atributo status_code do objeto Response
'''

# 5 Como podemos salvar uma resposta de Requests em um arquivo?
'''
Após abrir o novo arquivo em seu comptuador em modo 'wb' de escrita binária, utilize um loop for que faça uma iteração pelo método iter_content() do objeto 
Response e grave porções de dados no arquivo.

saveFile = open("filename.html", 'wb')
for chunk in res.iter_content(100000):
    saveFile.write(chunk)
'''

# 6 Qual é o atalho de teclado para abrir as ferramentas de desenvolvedor em um navegador?
'''
ctrl + shit + i no chrome
'''

# 7 Como podemos visualizar o HTML (nas ferramentas de desenvolvedor) de um elemento específico de uma página web?
'''
Especionando o elemento
'''

# 8 Qual é a string de selecot CSS que encontra o elemento com um atributo id igual a main?
'''
'#main'
'''

# 9 Qual é a string de seletor CSS que encontra os elementos com uma classe CSS igual a highlight?
'''
'.highlight'
'''

# 10 Qual é a string de seletor CSS que encontra todos os elementos <div> em outro elemento <div>
'''
'div div'
'''

# 11 Qual é a string de seletor CSS que encontra o elemento <button> com um atributo value definido como favorite?
'''
'button[value="favorite"]'
'''

# 12 Suponha que você tenha um objeto Tag de Beautiful Soup armazenado na variável spam para o elemento <div>Hello world!</div>. Como podemos
# obter a string 'Hello world!' Do objeto tag?
'''
spam.getText()
'''

# 13 Como podemos armazenar todos os atributos de um objeto Tag de Beautiful Soup em uma variável chamada linkElem?
'''
linkElem.attrs
'''

# 14 Executar import selenium não funciona. Como podemos importar devidamente o módulo selenium?
'''
O módulo selenium é importado com from selenium import webdriver
'''

# 15 Qual é a diferença entre os métodos find_element_* e os métodos find_elements_*?
'''
Os métodos find_element_* retornam o primeiro elemento correspondendo como um objeto WebElement. Os métodos find_elements_* retornam uma
lista com todos os lementos correspondentes na forma de obejtos WebElement.
'''

# 16 Quais métodos os objetos WebElement de Slenium têm para simular cliques de mouse e teclas?
'''
Os métodos click() e send_keys() simulam cliques de mouse e pressionamentos de teclas respectivamente
'''

# 17 Você poderia chamar send_keys(Keys.ENTER) no objeto WebElement do botão submit, porém qual é a maneira mais fácil de submeter um formulário
# usando o Selenium?
'''
Chamar o método submit() em qualquer elemento de um formulário submete o form.
'''

# 18 Como podemos simular os cliques nos botões Forward, Back e Refresh de um navegador com o Selenium?
'''
Os métodos forward(), back() e refresh() do Objeto WEbDriver simulam esses botões do navegador
'''