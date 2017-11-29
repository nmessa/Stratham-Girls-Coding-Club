def handsTall(inches):
    return inches / 4

def numMickeys(inches):
    return inches * 500

def numWiffles(inches):
    return inches/3.5

height = int(input('How tall are you in inches? '))

print("You are", handsTall(height), "hands tall")
print("You are", numMickeys(height), "mickeys tall")
print("You are", numWiffles(height), "wiffles tall")
