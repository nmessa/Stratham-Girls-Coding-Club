import random

def isItMyNumber(guess, secret):
    if guess == secret:
        print('You guessed the number')
    elif guess > secret:
        print('You guessed too high')
    else:
        print('You guessed too low')

#Generate a random integer from 1 to 100
secret = random.randint(1, 100)

guess = int(input("Guess a number: "))
isItMyNumber(guess, secret)

#How can we make this allow the player to continue guessing
#Until the find the secret number
