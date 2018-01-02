##calendar.py
##Author: nmessa
##Date: 12.13.2017
##Compensates for a leap year
import time
def isLeapYear(y):
    if y%4 == 0 and y%100 != 0 or y%400 == 0:
        return True
    else:
        return False
    
##Define a months dictionary
months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May',
          6:'June', 7:'July', 8:'August', 9:'September', 10:'October',
          11:'November', 12:'December'}
days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:30, 9:30, 10:31,
          11:30, 12:31}

year = int(input("Enter the year: "))
if isLeapYear(year):
    days[2] += 1

##Print out the dates
for m in range(1, 13):
    for d in range(1, days[m]+1):
        print(months[m]+ ' ' + str(d) + ', ' + str(year))
        
