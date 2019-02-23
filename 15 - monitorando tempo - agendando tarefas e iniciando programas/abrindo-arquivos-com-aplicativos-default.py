'''
O start informa ao Popen que utilize o programa padrão do sistema no Windows, no Linux/OSX é o open e no Ubuntu é see
O parametro shell=True é necessário somente no Windows.
'''

import subprocess

fileObj = open('hello.txt', 'w')
fileObj.write('Ola mundo!')
fileObj.close()

subprocess.Popen(['start', 'hello.txt'], shell=True)