'''
O módulo time é útil para obter um timestamp Unix epoch com o qual trabalhar. 
Porém se você quiser exibir uma data em um formato mais conveniente ou realizar 
operações aritméticas com datas (por exemplo, descobrir qual a data correspondendote a 205 dias
atrás ou qual será a data dentro de 123 dias), você deverá usar o módulo datetime.
'''

import datetime, time

# Imprimindo a data e hora atual
print(datetime.datetime.now())

# Passando uma data para criação
print(datetime.datetime(2019, 2, 25, 12, 45, 00))

# Podemos passar o valor do datetime para uma variável e acessar cada um separadamente:
dt = datetime.datetime(2019, 2, 25, 12, 45, 00)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

# Chamar o datetime.datetime.fromtimestamp() e passar um timestamp faz o objeto datetime
# retorna a data
print(datetime.datetime.fromtimestamp(10000))
print(datetime.datetime.fromtimestamp(time.time()))

# Comparando datas
halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newYears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
print(halloween2019 == oct31_2019)
print(halloween2019 > newYears2020)
print(newYears2020 > halloween2019)
print(newYears2020 != oct31_2019)


# Tipo de dado timedelta
'''
O módulo datetime também disponibiliza um tipo de dado timedelta que representa uma duração, em vez
de um instante no tempo.

A função timedelta() aceita argumentos nomeados weeks, days, hours, minutes, seconds, milliseconds 
e microseconds. Não há nenhum argumento nomeado month ou year, pois um mês ou um ano corresponde a uma quantidade
variável de tempo de acordo com o mês ou o ano em particular. Um objeto timedelta contém a duração total 
representada em dias, segundos e microssegundos. Esse números são armazenados nos atributos days, seconds, e 
microseconds respectivamente. O método total_seconds() retorna a duração somente em número de segundos. Passar
um objeto timedelta a str() retornará uma representação em string do objeto elegantemente formatada e legível aos
seres humanos.
'''

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta)) # convertendo o delta para uma data exibivel

'''
Operadores aritméticos podem ser usados para realizar operações aritméticas com datas em valores datetime.
Os objetos timedelta podem ser somados ou subtraídos de objetos datetime ou de outros objetos timedelta com 
os operadores + e -. Um objeto timedelta pode ser multiplicado ou divido por valores inteiros ou de ponto flutuante
com os operadores * e /.
'''

# Somando
dt = datetime.datetime.now()
print(dt)
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)

# Multiplicando
oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
print(oct21st)
print(oct21st - aboutThirtyYears)
print(oct21st - (2 * aboutThirtyYears))


# Convertendo objetos datetime em strings
'''
Os epoch timestamps e os objetos datetime não são muito amigáveis aos olhos humanos. Utilize o método strftime()
para exibir um objeto datettime como uma string. [o f no nome da função strftime() quer dizer format].

O método strftime() utiliza diretivas semelhantes àquelas usadas na formatação de strings em Python:

    %Y      - Ano com o séclo, como em 2019
    %y      - Ano sem o século, de 00 a 99 (de 1970 a 2069)
    %m      - Mês com um número decimal de 01 a 12
    %B      - Nome completo do mês, como em November
    %b      - Nome abreviado do mês, como em Nov
    %d      - Dia do mês, de 01 a 31
    %j      - Dia do ano de 001 a 366
    %w      - Dia da semana de 0 (domingo) a 6 (sábado)
    %A      - Nome completo do dia da semana, como em Monday
    %a      - Nome do dia da semana abreviado, como em Mon
    %H      - Hora de 00 a 23
    %I      - Hora de 01 a 12
    %M      - Minuto de 00 a 59
    %S      - Segundo de 00 a 59
    %p      - AM ou PM
    %%      - Caracterel literal % (porcentagem)

'''

# Convertendo datetime para string
'''
A função strptime() faz o inverso do método strftime(). Uma string com formato personalizado que utilize 
as mesmas diretivas de strftime() deverá ser passada para que strptime() saiba como fazer parse e compreender
a string. (O  p no nome da função strptime() quer dizer parse)
'''

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y-%m-%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))

# Convertendo string em objeto datetime
print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("October of '15", "%B of '%y"))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))
