#this function requires a character and
#an integer and prints a box of that size
def hollowBox(letter, size):
    for i in range(1, size+1):
        if i == 1 or i == size:
            for i in range(size):
                print(letter, end = "")
        else:
            print(letter, end = "")
            for i in range(size-2):
                print(" ", end = "")
            print(letter, end = "")
        print()





















##write a function that will print the following box given the function call
##
hollowBox('O', 4.5)
##
##OOOOOOO
##O     O
##O     O
##O     O
##O     O
##OOOOOOO
##
##hollowBox('X', 5)
##
##gives
##
##XXXXX
##X   X
##X   X
##X   X
##XXXXX







