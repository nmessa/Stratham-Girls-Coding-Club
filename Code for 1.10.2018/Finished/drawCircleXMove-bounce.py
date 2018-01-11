## Draw Circle
## Author: nmessa
## Draws a circle moving in the x direction and bouncing
## when it gets to the edge of the screen

from graphics import *
import time

def main():
    height = 800
    width = 1000
    radius = 50
    #Create a windows to draw in
    win = GraphWin('Circle Move and Bounce', width, height)

    #Define a circle to draw
    shape = Circle(Point(width/2, height/2), radius)

    #set the drawing parameters
    shape.setOutline("red")
    shape.setFill("green")
    shape.setWidth(10)

    #draw the circle in the window
    shape.draw(win)
    dx = 10
    dy = 0
    while True:
        shape.move(dx, dy)
        time.sleep(0.006)
        center = shape.getCenter()
        if center.x > width - radius or center.x < radius:
            dx = -dx

    
    time.sleep(3)
    win.close()

main()
