# Após gerar o arquivo podemos importa-lo e ler os dados
import os, cencus2010
print(cencus2010.allData['AK']['Anchorage'])

anchoragePop = cencus2010.allData['AK']['Anchorage']['pop']
print('The 2010 population of Anchrage was ' + str(anchoragePop))