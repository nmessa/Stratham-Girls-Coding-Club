## Draw Circle
## Author: nmessa
## Draws a circle moving in X and Y direction
## wraps around when it gets to the edge of the screen
## that is not a perfect square

from graphics import *
import time

def main():
    height = 800
    width = 1000
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
    dy = 8
    while True:
        #Add code here
        
        
    time.sleep(3)
    win.close()

main()
