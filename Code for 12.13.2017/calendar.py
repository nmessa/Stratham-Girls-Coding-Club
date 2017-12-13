##calendar.py
##Author: 
##Date: 12.13.2017
##Compensates for a leap year
import time
def isLeapYear(y):
    if y%4 == 0 and y%100 != 0 or y%400 == 0:
        return True
    else:
        return False
    
##Define a months and days dictionary
months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May',
          6:'June', 7:'July', 8:'August', 9:'September', 10:'October',
          11:'November', 12:'December'}
days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:30, 9:30, 10:31,
          11:30, 12:31}

#get year from user
year = int(input("Enter the year: "))

#Add one to February dictionary value if it is a leap year
if isLeapYear(year):
    days[2] += 1

##Print out the dates
#Add code here
    
        
