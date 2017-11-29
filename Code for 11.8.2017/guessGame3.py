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
count = 0
while not guessed:
    guess = int(input("Guess a number: "))
    count += 1
    guessed = isItMyNumber(guess, secret)

print('You guessed the number in', count, 'guesses')


#Now let us print some message with regard to your psychic ability
        
