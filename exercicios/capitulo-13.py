# 1 Um valor de string com o nome do arquivo PDFF não é passado para a função PyPDF2.PdfFileReader(). O que é passado para essa função em seu lugar?
'''
Um objeto File retornado por open()
'''

# 2 Em quais modos os objetos File para PdfFileReader() e para PdfFileWriter() devem ser abertos?
'''
Em modo de leitura 'rb'
Em modo de escrita 'wb'
'''

# 3 Como podemos adquirir um objeto Page para a página 5 de um objeto PdfFileReader?
'''
getPage(4) retorna para a page 5 devido a primeira ser a 0
'''

# 4 Qual variável de PdfFileReader armazena o número de páginas do documento PDF?
'''
numPages
'''

# 5 Se o PDF de um objeto PdfFileReader estiver criptografado com a senha swordfish, o que devemos fazer antes de podermos obter objetos Page desse PDF?
'''
devemos chamar decrypt('swordfish')
'''

# 6 Quais métodos devemos usar para fazer a rotação de uma página?
'''
rotateClockwise() e rotateCounterClockwise() os graus para rotação são passados como um argumento inteiro
'''

# 7 Qual método retorna um objeto Document para um arquivo chamado demo.docx?
'''
docx.Document('demo.docx')
'''

# 8 Qual é a diferença entre um objeto Paragraph e um objeto Run?
'''
Um documento contém vários parágrafos. Um parágrafo começa em uma nova linha e contém vários runs. Os runs são grupos contíguos de caracteres 
em um parágrafo
'''

# 9 Como podemos obter uma lista de objetos Paragraph para um objeto Document armazenado em uma variável chamada doc?
'''
doc.paragraphs
'''

# 10 Que tipo de obeto tem variávels bold, underline, italic, strike e outline?
'''
Objeto Run e não um objeto Paragraph
'''

# 11 Qual é a diferença entre definir a variável bold com True, False ou None?
'''
True sempre dedixa o objeto Run em negrito e False sempre remove o negrito, independentemente da configuração de netrigo do estilo. None fará o 
objeto Run simplemente usar a configuração de negrito do estilo.
'''

# 12 Como podemos criar um objeto Document para um novo documento Word?
'''
docx.Document()
'''

# 13 Como podemos acrescentar um parágrafo com o texto 'Hello there!' em um objeto Document armazenado em uma variável chamada doc?
'''
doc.add_paragrah('Hello there!')
'''

# 14 Quais inteiros representam os níveis de títulos disponíveis em documentos Word?
'''
0, 1, 2, 3 e 4
'''