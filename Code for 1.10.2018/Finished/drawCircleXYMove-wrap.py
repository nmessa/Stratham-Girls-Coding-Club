## Draw Circle
## Author: nmessa
## Draws a circle moving in X and Y direction
## wraps around when it gets to the edge of the screen

from graphics import *
import time

def main():
    height = 640
    width = 640
    radius = 50
    #Create a windows to draw in
    win = GraphWin('Circle Move XY with wraparound', width, height)
    win.setBackground('white')

    #Define a circle to draw
    shape = Circle(Point(0, 0), radius)

    #set the drawing parameters
    shape.setOutline("red")
    shape.setFill("green")
    shape.setWidth(10)

    #draw the circle in the window
    shape.draw(win)
    dx = 10
    dy = 10
    while True:
        shape.move(dx, dy)
        time.sleep(0.06)
        center = shape.getCenter()
        if center.y > height:
            shape.move(-width, -height)
        
    time.sleep(3)
    win.close()

main()
