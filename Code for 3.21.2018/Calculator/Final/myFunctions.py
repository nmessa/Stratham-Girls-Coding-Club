# calc_functions.py
# function module for Calculator Application in Python: Next Steps    
    
# Calculate the factorial of a number:
def factorial(n):
    try:
        n = int(n)
    except:
        return "--> Error!"
    
    # '0' is special:
    if n == 0:
        return 1

    # back out if too large:
    if n > 40:
        return "--> Answer will not fit on screen!"

    #catch negative numbers:
    if n < 0:
        return "--> Error!"
    
    # apply factorial algorithm:
    ans=n # set initial value of answer before loop
    while n > 1:
        ans = ans*(n-1)
        n = n-1
    return ans

# Convert number to roman numerals:
def to_roman(n):
    try:
        n = int(n)
    except:
        return "--> Error!"

    # opt out of numbers greater than 4999:
    if n > 4999:
        return "--> out of range"

    # start algorithm:
    romans = (
              (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
              (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
              )
    result = ""
    value=0
    while value < len(romans):
        while n >= romans[value][0]:
            result = result+romans[value][1]
            n = n-romans[value][0]
        value = value+1
    return result

# Convert base 10 numbers to binary function:
def to_binary(n):
    try:
        n = int(n)
        return bin(n)[2:]
    except:
        return "--> Error!"


# Convert base 2 numbers to base 10 function:
def from_binary(n):
    try:
        return int(n, 2)
    except:
        return "--> Error!"

# Find the square of a given number:
def square(n):
    return float(n)**2

# Find the square root of a given number:
def square_root(n):
    return float(n)**0.5
