import os

def verificaArquivosDesnecessarios(pasta):
    os.chdir(pasta)
    for fileName in os.listdir(pasta):
        fileNameAbs = os.path.abspath(fileName)
        fileSize = os.path.getsize(fileNameAbs)
        if (fileSize > 104857600):
            print(fileName + ': ' + str(fileSize))

verificaArquivosDesnecessarios('C:\\Users\\Johnatan\\Downloads')