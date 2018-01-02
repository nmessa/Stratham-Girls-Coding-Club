##Mailing Label Printer
##Author: nmessa
##Date: 12.13.2017

#Get user input and store date in names, addresses, city, state, and zipcode
name = input("Enter your name: ")
address = input("Enter your address: ")
city = input("Enter your city: ")
state = input("Enter your state: ")
zipcode = input("Enter your zipcode: ")


#print the mailing label
print(name)
print(address)
print(city + ', ' + state + "   " + zipcode)

## Sample output
## Enter your name: Joe Smith
## Enter your address: 127 Main Street
## Enter your city: Exeter
## Enter your state: NH
## Enter your zipcode: 03833
## Joe Smith
## 127 Main Street
## Exeter, NH   03833
