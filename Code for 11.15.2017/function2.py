#Functions do things
##def printBackwards(word):
##    for i in range(len(word)-1, -1, -1):
##        print(word[i], end = '')
##    print()
##
testWord = 'scrumptious'
##printBackwards(testWord)
##printBackwards('supercalifragilisticexpealodocious')

#add a function that counts all of the vowels i the word
def countVowels(word):
    vowels = 'aeiou'
    numVowels = 0
    for ch in word:
        if ch in vowels:
            numVowels += 1
    return numVowels

print(countVowels(testWord))
print(countVowels('supercalifragilisticexpealodocious'))
