spam = 'Hello world!'
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[6:])

'''
O slicing em uma string não altera a string original, sendo necessário criar uma nova 
variavel para recebe-la
'''

fizz = spam[0:5]
print(fizz)