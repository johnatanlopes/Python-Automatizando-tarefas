'''
webbroser - Vem junto com o Python e abre um navegador em uma página especifica
a função open() pode iniciar um novo navegador em uma URL especificada.

'''

import webbrowser

# Abrindo uma aba no navegador padrão do S.O
webbrowser.open('http://inventwithpython.com')

'''
É praticamente a única tarefa que o módulo webbroser faz. Mesmo assim, a função open() possibilita realizar algumas tarefas interessantes.
Por exemplo, copiar um endereço residencial para o clipboard e apresentar um mapa do Google Maps com esse endereço é uma tarefa maçante. 
Você poderia eliminar alguns passos dessa tarefa ao escrever um script simples para iniciar automaticamente o mapa em seu navegador usando o conteúdo de seu
clipboard. Dessa maneira será necessário apenas copiar o endereço para o clipboard e executar o script.
'''