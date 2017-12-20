##calendar.py
##Author: 
##Date: 12.13.2017
##Compensates for a leap year
import time
def isLeapYear(y):
    #Add code here
    
##Define a months and days dictionary
months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May',
          6:'June', 7:'July', 8:'August', 9:'September', 10:'October',
          11:'November', 12:'December'}
days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:30, 9:30, 10:31,
          11:30, 12:31}

#get year from user
year = int(input("Enter the year: "))

#Add one to February dictionary value if it is a leap year
#Add code here

##Print out the dates
#Add code here
for m in range(1, 13):
    for d in range(1, days[m]+1):
        print(months[m]+ ' ' + str(d) + ', ' + str(year)) 
        
