import re

'''
As expressões regulares serão convenientes se o padrão de texto para a correspondência for simples. Porém fazer a correspondência de padrões
complicados de texto pode exigir expressões regulares longas e confusas. Podemos atenuar esse problema dizendo à função re.compile() que ignore
espaços em branco e comentários na string da regex. Esse modo verbose pode ser habilitado se a variável re.VERBOSE for passada como segundo argumento de
re.compile()
'''

# Agora em vez de uma expressão difícil de ler como:
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)')


# Podemos distribuir a expressão regular em várias linhas usando comentários como:
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # código de área
    (\s|-|\.)?         # separador
    (\d{3})            # primeiros três digitos
    (\s|-|\.)          # separador
    (\d{4})            # ultimos 4 digitos
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extensão
)''', re.VERBOSE)
