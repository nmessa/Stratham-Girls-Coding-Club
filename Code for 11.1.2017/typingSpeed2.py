from time import *
from random import *

##
def calcAccuracy(st, txt):
    count = 0
    st = st.split()
    txt = txt.split()
    for i in range(len(txt)):
        if st[i] != txt[i]:
            count += 1
    return count/len(txt) * 100
    

def howManyWords(phrase):
    numWords = 0
    for ch in phrase:
        if ch == ' ':
            numWords += 1
    return numWords + 1
s = ''
text = ''
phrases = ['Now is the time for all good men to come to the aid of their country',
           'The quick brown fox jumps over the lazy dog',
           'Jack be nimble Jack be quick Jack jumped over the candlestick',
           'We promptly judged antique ivory buckles for the next prize',
           'How razorback jumping frogs can level six piqued gymnasts',
           'Sixty zippers were quickly picked from the woven jute bag',
           'Crazy Fredrick bought many very exquisite opal jewels']

print("When you see a phrase, type it in and hit enter")

for i in range(5, 0, -1):
    print(i)
    sleep(1)
print("Go!!!!")
start_time = time()
for i in range(3):
    phrase = choice(phrases)
    text += phrase + ' '
    print(phrase)
    s += input()
    s += ' '
end_time = time()

wps = howManyWords(s)/(end_time - start_time)
wpm = wps * 60
print("You are typing at", wpm, 'words per minute')

errorRate = calcAccuracy(s, text)
print("The error rate is", errorRate, '%')

