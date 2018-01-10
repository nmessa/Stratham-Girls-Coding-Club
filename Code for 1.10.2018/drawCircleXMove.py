## Draw Circle
## Author: nmessa
## Draws a circle moving in the x direction

from graphics import *
import time

def main():
    #Create a windows to draw in
    win = GraphWin('Moving Circle', 640, 480)

    #Define a circle to draw
    shape = Circle(Point(320, 240), 50)

    #set the drawing parameters
    shape.setOutline("red")
    shape.setFill("green")
    shape.setWidth(10)

    #draw the circle in the window
    shape.draw(win)
    dx = 10
    dy = 0

    #Animate in the x direction
    while True:
        #Add code here

    
    time.sleep(3)
    win.close()

main()
