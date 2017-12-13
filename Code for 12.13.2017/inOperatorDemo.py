##The in operator demonstration
##Author: nmessa
##Date: 12/12/2017

vowels = 'aeiouAEIOU'
newPhrase = ""
vowelPhrase = ""
phrase = 'The quick brown fox jumped over the lazy dog'

for letter in phrase:
    if letter in vowels:
        vowelPhrase += letter
    else:
        newPhrase += letter

print(newPhrase)
print(vowelPhrase)
    
