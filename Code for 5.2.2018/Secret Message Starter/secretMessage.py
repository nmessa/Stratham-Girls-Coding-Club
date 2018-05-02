
#This function generates a key value based on your name
#This function adds up the ASCII values of all letters in your name
def nameValue(name):
    #Add code here

    #return a value from 1 to 127

#This function takes plainText and a key and encrypts it using Caesar Cipher
def encrypt(plainText, key):
    cipherText = ""
    #Add code here

    
    return cipherText

#This function takes cipherText and a key and decrypts it using Caesar Cipher
def decrypt (cipherText, key):
    plainText = ""
    #Add code here

    
    return plainText


#Test code
plainText = input("Enter a message: ")
name = input("Enter your first name: ")
key = nameValue(name)
cipherText = encrypt(plainText, key)
print('Encrypted message =', cipherText)
print()
name = input("Enter your first name to decrypt: ")
key = nameValue(name)
plainText = decrypt(cipherText, key)
print('Original message =', plainText)


