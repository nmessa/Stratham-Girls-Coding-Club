###Variable review
##
####var1 = 3.14
####var2 = 42
####var3 = "Hello"
####var4 = 'World'
####
#####What data types are these?
######print(type(var1))
######print(type(var2))
######print(type(var3))
######print(type(var4))
####
#####print the variables
####print('var1 =' + str(var1))
####print('var2 =' + str(var2))
####print('var3 =' + var3)
####print('var4 =' + var4)
##
###Your turn
###Create a variable called name and assign 'Mary' to it
##name = 'Mary'
##
###Create a variable called age and assign 13 to it
##age = 13
##
###Create a variable called gpa and assign 3.45 to it
##gpa = 3.45
##
###print the variables with descriptive comments
##print("My name is " + name)
##print("My age is " + str(age) + " years old")
##print("My GPA is", gpa)

#Activities using input function

##name = input("Enter your name: ")
##age = int(input("Enter your age: "))
##gpa = float(input("Enter your gpa: "))
##
###What data type are name, gpa, and age?
##
####print(type(name))
####print(type(age))
####print(type(gpa))
##
###print the variables with descriptive comments
##
##print("Your name is " + name)
##print("Your age is " + str(age))
##print("Your gpa is " + str(gpa))

#getting multiple values from one input function call
person1, person2, person3 = input("Enter 3 friends: ").split()
print(person1)
print(person2)
print(person3)


month, day, year = input("Enter the date (mm/dd/yyyy): ").split('/')
print(month)
print(day)
print(year)

hour, minute, second = input("Enter the time (hh:mm:ss): ").split(':')
print(hour)
print(minute)
print(second)




