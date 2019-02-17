import shutil, os

# Tornando o diretório C:\\tmp como atual
os.chdir('C:\\tmp')

# Movendo um arquivo
shutil.move('C:\\tmp\\bacon.txt', 'C:\\tmp\\delicious')

# Movendo e renomeando
shutil.move('C:\\tmp\\arquivo.txt', 'C:\\tmp\\delicious\\novo-arquivo.txt')
