#loop demonstration

#Simple for loop

##for i in [1,2,3,4]:
##    print(i)

#keep them on the same line
##for i in [1,2,3,4]:
##    print(i, end = ' ')


#for loop using the range function

#what will it print?
##for i in range(10):
##    print(i, end = ' ')
##print()

#what will it print?
##for i in range(3, 10):
##    print(i, end = ' ')
##print()

#what will it print?
##for i in range(3, 10, 2):
##    print(i, end = ' ')
##print()

#what will it print?
##for i in range(10, -1, -1):
##    print(i, end = ' ')
##print()

##code that prints 3 to 11 in increments of 3
##for pqsd in range(3, 12, 3):
##    print(pqsd, end = ' ')



#while loop
##again = True
##while again:
##    answer = input("Loop again? (y/n)")
##    if answer == 'n':
##        again = False
##print("All done")


##count = 10
##while count > 0:
##    print(count)
##    count -= 1
##print('Blast off!!!')


#Write code that asks you to enter your name
#print hello + your name
#repeats until you enter quit

##name = input("enter your name: ")
##while name != 'quit':
##    print("Hello " + name)
##    name = input("enter your name: ")
    
#multiplication 
##from random import *
##n1 = randint(5, 10)
##n2 = randint(5,10)
##answer = int(input("What is " + str(n1) + 'x' + str(n2) + "? "))
##while answer == n1 * n2:
##    n1 = randint(5, 10)
##    n2 = randint(5,10)
##    answer = int(input("What is " + str(n1) + 'x' + str(n2) + "? "))

#Nested loop
##for i in range(1,16):
##    for j in range(1,16):
##        print(i, 'x', j, '=', i*j)
##    print()

#ended here

#Using break and continue
##for i in range(1, 101):
##    if i%10 == 0:
##        continue
##    if i%2 == 0:
##        print(i, end = ' ')

##for i in range(1, 101):
##    if i%50 == 0:
##        break
##    if i%2 == 0:
##        print(i, end = ' ')


#Nested loop example
##for i in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
##    for j in ['Clubs', 'Spades', 'Diamonds', 'Hearts']:
##        print(i, 'of', j)
        
#Your turn
#Write some code that prints the odd numbers from 1 to 100
##for i in range(1, 101, 2):
##    print(i, end=' ')
##
##print("\n\n\n")
##for i in range(101):
##    if i % 2 == 1:
##        print(i, end = ' ')


#Write some code that prints numbers by fives up to 100 (5, 10, 15, .... 100)
##print("\n\n\n")
##for i in range(5, 101, 5):
##    print(i, end = ' ')


#Write some code that prints allows the user to enter a number and prints the
#the square root of the number until the user enters a negative number.

number = float(input("Enter a number: "))
while number >= 0:
    print(number ** 0.5)
    number = float(input("Enter a number: "))
