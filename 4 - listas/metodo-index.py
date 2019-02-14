spam = ['hello', 'hi', 'howdy', 'heyas', 'hi']
print(spam.index('hello'))
print(spam.index('heyas'))

'''
print(spam.index('howdy howdy howdy'))
Se o valor não estiver presente na lsita, o Python apresentará um erro ValueError
'''

'''
Quando existir valores duplicados o primeiro indice será retornado
'''
print(spam.index('hi'))

