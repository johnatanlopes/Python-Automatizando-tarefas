'''
Com frequência, será necessário definir um valor em um dicionário para uma chave específica somente se essa chave ainda não
tiver um valor. O c´dogio será semelhante a:
'''
spam1 = {'name': 'Pooka', 'age': 5}
if 'color' not in spam1:
    spam1['color'] = 'black'

print(spam1)

'''
O método setdefault() oferece uma maneira de fazer isso em uma linha de código
'''

spam2 = {'name': 'Pooka', 'age': 5}
spam2.setdefault('color', 'black')
print(spam2)
spam2.setdefault('color', 'white')
print(spam2)

'''
Na primeira vez que setdefault é chamado o dicionário em spam é alterado a color para black, quando chamamos novamente para alterar a color para white não funciona.
Ele não é alterado devido já ser uma chave já existente
'''
