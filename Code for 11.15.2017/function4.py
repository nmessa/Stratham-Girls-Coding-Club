##def printRamp(letter, level):
##    for i in range(1, level+1):
##        for j in range(i):
##            print(letter, end = "")
##        print()
####
##printRamp('X', 40)
    
## Output
## Q
## QQ
## QQQ
## QQQQ
## QQQQQ
## QQQQQQ
## QQQQQQQ
## QQQQQQQQ
## QQQQQQQQQ
## QQQQQQQQQQ

# Create a function printRamp2 which prints the following pattern
## BBBBBBBBBB
## BBBBBBBBB
## BBBBBBBB
## BBBBBBB
## BBBBBB
## BBBBB
## BBBB
## BBB
## BB
## B

# when called with printRamp2("B", 10)

# Create a function printRamp3 which prints the following pattern

##          X
##         XX
##        XXX
##       XXXX
##      XXXXX
##     XXXXXX
##    XXXXXXX
##   XXXXXXXX
##  XXXXXXXXX
## XXXXXXXXXX

# when called with printRamp3("X", 10)

##def printRamp2(letter, level):
##    for i in range(level, 0, -1):
##        for j in range(i):
##            print(letter, end = "")
##        print()
##
##printRamp2('B', 10)


def printRamp3(letter, level):
    for i in range(level):
        for j in range(level-1-i, 0, -1):
            print(' ', end = "")
        for k in range(i+1):
            print(letter, end = "")
        print()

printRamp3('X', 40)
