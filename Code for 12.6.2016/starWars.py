def starWarsName(firstName, lastName, momName, birthCity):
    fName = lastName[0:3] + firstName[0:2].lower()
    lName = momName[0:2] + birthCity[0:3].lower()
    return fName + " " + lName


firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
momName = input("What is your mom's maiden name? ")
birthCity = input("What city were you born in? ")

swn = starWarsName(firstName, lastName, momName, birthCity)
print ("Your Star Wars name is", swn)
