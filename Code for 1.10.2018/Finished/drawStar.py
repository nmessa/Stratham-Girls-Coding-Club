## Draw Star
## Author: nmessa
## Draws a star using alternative graphics module

from graphics import *
import time

def main():
    #Create a windows to draw in
    win = GraphWin('Star', 640, 640)

    #Define vertices of Star
    p1 = Point(320, 50)
    p2 = Point(50, 200)
    p3 = Point(590, 200)
    p4 = Point(50, 590)
    p5 = Point(590, 590)

    #Create the star
    shape = Polygon(p1, p4, p3, p2, p5)

    #set the drawing parameters
    shape.setOutline("red")
    shape.setFill("green")
    shape.setWidth(5)

    #draw the star in the window
    shape.draw(win)

    time.sleep(5)
    win.close()

main()
