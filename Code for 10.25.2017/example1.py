#if-else review

##number1 = 10
##number2 = 20

#weird swap demo
##print(number1, number2)
##number1, number2 = number2, number1
##print(number1, number2)

##number1 = 10
##number2 = 20
##if number1 >= number2:
##    print(number2, number1)
##else:
##    print(number1, number2)



###nested if else
##age = int(input("Enter your age: "))
##
###this is the way we did it last week
###if else using logical operators
##if age >= 13 and age <= 19:
##    print("You are a teenager.")
##else:
##    print("You are not a teenager")
##
###this is a nested if else without using logical operators
##if age >= 13:
##    if age <= 19:
##        print("You are a teenager.")
##    else:
##        print("You are not a teenager")
##else:
##    print("You are not a teenager")


#if else to sort numbers or strings
##number1 = 10
##number2 = 4
##number3 = 7

##number1 = 'Judith'
##number2 = 'Mary'
##number3 = 'Erin'
##if number1 > number2 and number1 > number3:
##    largest = number1
##    if number2 > number3:
##        smallest = number3
##        middle = number2
##    else:
##        smallest = number2
##        middle = number3
##        
##if number2 > number1 and number2 > number3:
##    largest = number2
##    if number1 > number3:
##        smallest = number3
##        middle = number1
##    else:
##        smallest = number1
##        middle = number3
##
##if number3 > number1 and number3 > number2:
##    largest = number3
##    if number1 > number2:
##        smallest = number2
##        middle = number1
##    else:
##        smallest = number1
##        middle = number3
##
##print(smallest, middle, largest)

#Your turn
#Write a fortune cookie generator program that picks a random number
#from 1 to 10 and gives you a fortune

#Here is an example
from random import *
secret = randint(1,10)
if secret == 1:
    print("The fortune you seek is in another cookie.")
elif secret == 2:
    print("An alien of some sort will be appearing to you shortly.")
elif secret == 3:
    print("The road to riches is paved with homework.")
elif secret == 4:
    print("Fortune not found? Abort, Retry, Ignore.")
elif secret == 5:
    print("Don’t eat the paper.")
elif secret == 6:
    print("Someone will invite you to a Karaoke party.")
elif secret == 7:
    print("Ask your mom instead of a cookie.")
elif secret == 8:
    print("You will be hungry again in one hour.")
elif secret == 9:
    print("The fortune you seek is in another cookie.")
else:
    print("You will receive a fortune cookie.")

