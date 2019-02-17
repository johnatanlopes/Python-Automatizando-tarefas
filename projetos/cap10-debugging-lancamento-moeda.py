'''
Ao utilizar o debug do IDLE você vai reparar que o toss recebe um numero e o gues é uma palavra, então ele sempre entrará no 
else já que os valores nunca serão iguais dessa forma
'''

import random

guess = ''

while guess not in ('head', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 é coroa (tails) e 1 é cara (heads)
if toss == guess:
    print('You got it')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.head')