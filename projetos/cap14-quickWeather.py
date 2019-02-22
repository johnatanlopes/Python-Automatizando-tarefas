# quickWeather.py - Exibe a previsão do tempo para uma locidade obtida na linha de comando.

import json, requests, sys
# Processa a localidade a partir dos argumentos da linha de comando
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()

location = ''.join(sys.argv[1:])

# Faz download dos dados JSON a partir da API de OpenWeatherMap.org
url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=5cd14b75c01966cf91774871f65f2639' % (location)
response = requests.get(url)
response.raise_for_status()

# Carrega dados JSON em uma veriável python
weatherData = json.loads(response.text)

# Exibe as descrições da previsão do tempo
w = weatherData['list']
print('Current weather in %s:' % (location))

inicio = 0
fim = 6
for i in range(inicio, fim):
    print(w[i]['main'])
    print(w[i]['dt_txt'])
print('')
