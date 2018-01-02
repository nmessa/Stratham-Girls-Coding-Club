##vowelCount.py
##Author: nmessa
##Date: 12.13.2017
def vowelCount(phrase):
    #initialize count variable
    count = 0
    
    #parse the phrase counting the vowels
    for letter in phrase:
        if letter in vowels:
            count += 1

    return count



#user enters a phrase and stores in phrase
phrase = input("Enter a phrase: ")

#Create a vowel string
vowels = 'aieouAEIOU'

print(phrase, 'has', count, 'vowels')


## Sample Output
## Enter a phrase: this is a test
## this is a test has 4 vowels
