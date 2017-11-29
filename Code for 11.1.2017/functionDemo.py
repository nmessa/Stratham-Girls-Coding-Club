#Function demo

#Functions return things
def f(x):
    return 3 * x + 7

answer = f(1234)

print(answer)

##def f(x):
##    return x**2 + 7*x + 3
##
##answer = f(3)
##print(answer)

##print('x       f(x)')
##for x in range(-5, 6):
##    answer = f(x)
##    print(x, "     ", answer)

#Functions do things
##def printBackwards(word):
##    for i in range(len(word)-1, -1, -1):
##        print(word[i], end = '')
##
##testWord = 'scrumptious'
##printBackwards(testWord)
##printBackwards('supercalifragilisticexpealodocious')


#Functions do things and return things
##def howManyWords(phrase):
##    numWords = 0
##    for ch in phrase:
##        if ch == ' ':
##            numWords += 1
##    return numWords + 1
##
##testPhrase = 'The quick brown fox jumps over the lazy dog.'
##answer = howManyWords(testPhrase)
##print('The sentence has', answer, 'words')

#Functions can call other functions
##def averageWordLength(phrase):
##    words = howManyWords(phrase)
##    phraseLength = len(phrase)
##    return phraseLength/words
##
##def howManyWords(phrase):
##    numWords = 0
##    for ch in phrase:
##        if ch == ' ':
##            numWords += 1
##    return numWords + 1
##
##testPhrase = 'The quick brown fox jumps over the lazy dog.'
##answer = averageWordLength(testPhrase)
##print('The sentence has', round(answer,2), 'charcters per word')


##Let's make a program that tests your typing speed
##from time import *
##
##def howManyWords(phrase):
##    numWords = 0
##    for ch in phrase:
##        if ch == ' ':
##            numWords += 1
##    return numWords + 1
##    
##s = ""
##
##for i in range(5, 0, -1):
##    print(i)
##    sleep(1)
##print("Go!!!!")
##start_time = time()
##while len(s) < 100:
##    s += input()
##    s += ' '
##end_time = time()
##
##wps = howManyWords(s)/(end_time - start_time)
##wpm = wps * 60
##print("You are typing at", wpm, 'words per minute')



