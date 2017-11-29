from time import *
##
def howManyWords(phrase):
    numWords = 0
    for ch in phrase:
        if ch == ' ':
            numWords += 1
    return numWords + 1
    
s = ""

for i in range(5, 0, -1):
    print(i)
    sleep(1)
print("Go!!!!")
start_time = time()
while len(s) < 100:
    s += input()
    s += ' '
end_time = time()

wps = howManyWords(s)/(end_time - start_time)
wpm = wps * 60
print("You are typing at", wpm, 'words per minute')
