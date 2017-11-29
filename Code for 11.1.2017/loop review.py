#Loop review

#What does this print?

##for i in range(1,20):
##    for j in range(i):
##        print('*', end = '')
##    print()
    
s = 'Jack jumped over the candlestick'

##for i in range(len(s)-1, -1, -1):
##    print(s[i], end = '')

##print(s[::-1])
##number = int(input("Enter a number (integer): "))
##total = 0
##for i in range(1, number+1):
##    total += i
##print(total)

##finished = False
##while not finished:
##    c = input("Enter a character: ")
##    if c == 'q':
##        finished = True


#Now let's measure how fast you are on the keyboard
from time import time
count = 0
start_time = time()
while count < 50:
    input('Hit enter key')
    count += 1
end_time = time()
timePerKeyhit = (end_time - start_time) / 50
print(timePerKeyhit, 'seconds per key hit')


#Let's make a reaction tester
from random import *
from time import *
delay = randint(1, 5)
sleep(delay)
start_time = time()
input("Go!!!!!")
end_time = time()
print("It took you", (end_time - start_time), 'seconds to react')


    
