##dateFormat.py
##Author: nmessa
##Date: 12.13.2017
import time

##Define a months dictionary
months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May',
          6:'June', 7:'July', 8:'August', 9:'September', 10:'October',
          11:'November', 12:'December'}
#Get the date from the user
myDate = input("Enter the date (mm/dd/yyyy): ")

#Split the date up
d = myDate.split('/')

#store the 3 parts of the date in monthName, day, and year
monthName = months[int(d[0])]
day = d[1]
year = d[2]

#print the date in December 13, 2017 format
print(monthName + ' ' + day + ', ' + year)

#print the date in 13 December 2017 format
print(day + ' ' + monthName + ' ' + year)
        
