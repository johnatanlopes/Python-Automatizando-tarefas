# Por padrão o arquivo é aberto somente com leitura que seria o open recebendo o r
# Se não receber o r ele atribui por default
helloFile = open('C:\\Users\\Johnatan\\hello.txt', 'r')

# Lendo o arquivo com o read
helloContent = helloFile.read()

# Imprimindo o conteudo do arquivo txt
print(helloContent)

# Caso deseja ler outras linhas do arquivo pode abrir o arquivo com open e depois utilizar o readlines()
sonnetFile = open('C:\\Users\\Johnatan\\sonnet29.txt', 'r')
print(sonnetFile.readlines())