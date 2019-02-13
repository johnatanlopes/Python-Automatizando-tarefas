# Este programa diz hello e pergunta o meu nome

print('Hello world!')
print('What is your name?') # pergunta o nome
myName = input()
print('It is good to meet you,' + myName)
print('The length of your name is:')
print(len(myName)) # A função len conta cada caractere de uma string
print('What is your age?') # pergunta a idade
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')