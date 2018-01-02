##noVowels.py
##Author: nmessa
##Date: 12.13.2017

#user enters a phrase and stores in phrase
phrase = input("Enter a phrase: ")

#Create a null string new phrase
newPhrase = ''

#Create a vowel string
vowels = 'aieouAEIOU'

#parse the phrase removing vowels
for letter in phrase:
    if letter in vowels:
        newPhrase += '_'
    else:
        newPhrase += letter

print(phrase)
print(newPhrase)

## Sample Output
## Enter a phrase: this is a test
## this is a test
## th_s _s _ t_st
