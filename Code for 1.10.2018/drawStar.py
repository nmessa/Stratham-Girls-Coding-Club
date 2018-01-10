## Draw Star
## Author: nmessa
## Draws a star using alternative graphics module

from graphics import *
import time

def main():
    #Create a windows to draw in
    win = GraphWin('Star', 640, 640)

    #Define vertices of Star
    #Add code here
    

    #Create the star
    #Add code here
    

    #set the drawing parameters
    shape.setOutline("red")
    shape.setFill("green")
    shape.setWidth(5)

    #draw the star in the window
    shape.draw(win)

    time.sleep(5)
    win.close()

main()
