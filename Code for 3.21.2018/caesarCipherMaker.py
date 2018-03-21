# caesarCipherMaker.py

alphabet  = "abcdefghijklmnopqrstuvwxyz"

def make_code(text, key):
    code_text = ""
    
    # loop through the letters and build the code text
    for letter in text:
        if letter in alphabet:
            i = alphabet.find(letter) + key
            code_text = code_text + alphabet[i % 26]   
        else: 
            code_text = code_text + letter
    return code_text

# Get message
plain_text = input("Please enter your text to be encoded:\n")

# Change user input to lower case:
plain_text = plain_text.lower()

# Get cipher key
cipher_key = int(input("Please enter a numerical key between 1 and 26:\n"))

# Create coded message
code_text = make_code(plain_text, cipher_key)
print("Here is your code:\n", code_text.upper())
#To Do
#Modify this program to create a decoder
