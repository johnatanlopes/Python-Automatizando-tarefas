'''
O módulo selenium permite que o Python controle diretamente o navegador ao clicar em links e preencher informações de login por meio de programação,
quase como se houvesse um ser humano interagindo com a página. O selenium permite interagir com páginas web de uma maneira muito mais sofisticada que o Requests
e o Beautiful Soup; contudo pelo fato de iniciar um navegador web, ele é um pouco mais lento e díficil de ser executado em background, se por exemplo for necessário
fazer download de apenas alguns arquivos da web.
'''

# Iniciando um navegador controlado pelo selenium
# Necessário ter o firefox instalado e o selenium (pip3 install selenium)
# Install geckodriver: https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-win64.zip

from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\\Users\\Johnatan\\Documents\\Desenvolvimento\\geckodriver\\geckodriver.exe')

print(type(browser))
browser.get('http://inventwithpython.com')

'''
Localizando elementos na pagina

Os objetos webdriver têm alguns métodos para localizar elementos em uma página. Eles são divididos em métodos find_element_* e find_elements_*.
Os métodos find_element_* retornam um único objeto WebElement que representa o primeiro elemento da página que corresponda a sua consulta. Os métodos find_elements_* 
retornam uma lista de objetos WebElement_* contendo todos os elementos correspondentes da página.

Tabela
    browser.find_element_by_class_name(nome)    -   Elemento que utiliza a classe CSS nome
    browser.find_elements_by_class_name(nome)   -   Elemento que utiliza a classe CSS nome
    browser.find_element_by_css_selector(seletor)   -   Elemento que corresponde ao seletor CSS
    browser.find_elements_by_css_selector(seletor)  -   Elemento que corresponde ao seletor CSS
    browser.find_element_by_id(nome)            -   Elemento com um valor de atributo id
    browser.find_elements_by_id(nome)           -   Elemento com um valor de atributo id
    browser.find_element_by_link_text(texto)    -   Elementos <a> que correspondem totalmente ao texto especificado
    browser.find_elements_by_link_text(texto)   -   Elementos <a> que correspondem totalmente ao texto especificado
    browser.find_element_by_partial_link_text(texto)   -   Elementos <a> que contêm o texto especificado
    browser.find_elements_by_partial_link_text(texto)  -   Elementos <a> que contêm o texto especificado
    browser.find_element_by_name(nome)         -   Elementos com um valor de atributo nome correspondente
    browser.find_elements_by_name(nome)        -   Elementos com um valor de atributo nome correspondente
    browser.find_element_by_tag_name(nome)    -    Elementos com uma tag nome correspondente (sem diferenciar letras maiusculas de minusculas; um elemento <a>
        corresponde a 'a' e a 'A')
    browser.find_elements_by_tag_name(nome)    -    Elementos com uma tag nome correspondente (sem diferenciar letras maiusculas de minusculas; um elemento <a>
        corresponde a 'a' e a 'A')
    

Exceto pelos métodos *_by_tag_name(), os argumentos para todos os métodos consideram as diferenças entre letras maiúsculas e minúsculas. Se não houver nenhum
elemento na página que corresponda ao que o método esta procurando, o módulo selenium gerará uma exceção NoSuchElement. Se não quiser que essa exceção provoque uma
falha em seu programa acrescente instruções try e except.

Após ter o objeto WebElement, você poderá descobrir mais sobre ele ao ler os atributos ou chamar os métodos abaixo:

    tag_name    -    O nome da tag, por exemplo, 'a' para um elemento <a>
    get_attribute(nome) -   O valor do atributo nome do elemento
    text        -   OP texto do elemento, por exemplo 'hello' em <span>hello</span>
    clear()     -   Para campos de texto ou elementos correspondentes à área de texto, limpa o texto digitado.
    is_displayed()  -   Retorna True se o elemento estiver visível; caso contrário, retorna False
    is_enabled()    -   Para elementos de entrada, retorna True se o elemento estiver habilitado; caso contrário, retorna False
    is_selected()   -   Para elementos relacionados a caixas de seleção ou botões de rádio, retorna True se o elemento estiver selecionado; 
        caso contrário retorna False
    location        -   Um dicionário com chaves
'''

'''
Vamos ao exemplo:

Nesse caso, abrimos o firefox e o direcionamos a um URL. Nessa página tentamos encontrar elementos com o nome da classe igual a 'bookcover' e caso esse
elemento seja encontrado, exibimos seu nome de tag usando o atributo tagname. Se um elemento desse tipo não for encontrado exibimos uma mensagem.
'''

try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an with that name.')


'''
Clicando na página
'''

linkElem = browser.find_element_by_link_text('Blog')
print(type(linkElem))
linkElem.click()

'''
Preenchendo e submetendo formulários
'''

# browser = webdriver.Firefox(executable_path=r'C:\\Users\\Johnatan\\Documents\\Desenvolvimento\\geckodriver\\geckodriver.exe')
# browser.get('https://mail.yahoo.com')
# emailElem = browser.find_element_by_id('login-username')
# emailElem.send_keys('not_my_real_email')
# passwordElem = browser.find_element_by_id('login-passwd')
# passwordElem.send_keys('123456')
# passwordElem.submit()


'''
Enviando teclas especiais

O Seleniumtem um módulo	para teclas	que	são	impossíveis	de digitar em um valor de string que funciona de modo muito semelhante aos caracteres de escape.

Variáveis comumente utilizadas do módulo selenium.webdriver.common.keys

    Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT       -       As teclas de direção do teclado
    Keys.ENTER, Keys.RETURN                         -       As teclas ENTER e RETURN
    Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP       -       As teclas HOME, END, PAGEDOWN E PAGEUP
    Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE       -       As teclas ESC, BACKSPACE e DELETE
    Keys.F1, Keys.F2, ..., Keys.F12                 -       As teclas F1 a F12 na parte superior do teclado
    Keys.TAB                                        -       A tecla TAB

Por exemplo, se o cursor não estiver em um campo de texto no momento de pressionar as teclas HOME e END fará o navegador fazer rolagens para o início
e o fim da página.
'''
from selenium.webdriver.common.keys	import Keys 
browser = webdriver.Firefox(executable_path=r'C:\\Users\\Johnatan\\Documents\\Desenvolvimento\\geckodriver\\geckodriver.exe')
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)
htmlElem.send_keys(Keys.HOME)

'''
Clicando nos botões do navegador

O selenium também é capaz de simular cliques em diversos botões do navegador por meio dos métodos a seguir:

    browser.back() - Clica no botão Back (Retornar)
    browser.forward()  - Clica no botão Forwarch (avançar)
    browser.refresh() - Clica no botão refresh (Atualizar)
    browser.quit() - Clica no botão close Windows (Fechar janela)
'''

# Mais informações sobre o selenium
'''
	http://seleniumpython.readthedocs.org/.

'''