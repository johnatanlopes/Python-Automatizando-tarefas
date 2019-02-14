'''
Todos os programas Python podem	chamar	um	conjunto básico	de funções denominado funções internas (built-in), incluindo as	funções	print(), input() e len(),
que	vimos anteriormente. O	Python também vem com um conjunto de módulos chamado biblioteca-padrão (standard library). 
Cada módulo corresponde	a um programa Python que contém	um	grupo relacionado de funções que pode ser incluído	em	seus programas.	
Por	exemplo, o módulo math contém funções relacionadas	à matemática, o	módulo	random	contém funções	relacionadas a números aleatórios, e assim por diante.


'''

# Importando o modulo random e imprimindo 5 vezes números aleatórios com randint
import random
for i in range(5):
    print(random.randint(1,10))


# Importando 4 modulos de uma unica vez
import random, sys, os, math

'''
Instruções from	import
Uma	forma alternativa para	a instrução	import	é composta	da	palavra-chave from	seguida	do nome	do	módulo,	a palavra-chave	import e um	asterisco; 
por exemplo, from random import	*.
Com	essa forma	da	instrução import, as chamadas às funções em	random não precisarão do prefixo random. Entretanto	usar o	nome completo deixa	o código
mais legível, portanto	é	melhor	usar a	forma normal da	instrução import.
'''