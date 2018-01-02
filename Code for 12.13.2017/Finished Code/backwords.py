##backwords.py
##Author: nmessa
##Date: 12.13.2017

#user enters a word and stores in word
word = input("Enter a word: ")


#if the word has more than 5 characters print it backwards
#or else print it normally
if len(word) > 5:
    print(word[::-1])
else:
    print(word)
