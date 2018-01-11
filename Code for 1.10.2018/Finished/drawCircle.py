## Draw Circle
## Author: nmessa
## Draws a circle using alternative graphics module

from graphics import *
import time

def main():
    #Create a windows to draw in
    win = GraphWin('Circle', 640, 480)

    #Define a circle to draw
    shape = Circle(Point(320, 240), 50)

    #set the drawing parameters
    shape.setOutline("red")
    shape.setFill("green")
    shape.setWidth(10)

    #draw the circle in the window
    shape.draw(win)

    time.sleep(3)
    win.close()

main()
