import random

def isItMyNumber(guess, secret):
    if guess == secret:
        print('You guessed the number')
        return True
    elif guess > secret:
        print('You guessed too high')
        return False
    else:
        print('You guessed too low')
        return False

#Generate a random integer from 1 to 100
secret = random.randint(1, 100)

guessed = False
while not guessed:
    guess = int(input("Guess a number: "))
    guessed = isItMyNumber(guess, secret)

#How can we add a score keeper to this game?



        
