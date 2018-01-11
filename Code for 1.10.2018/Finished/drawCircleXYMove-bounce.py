## Draw Circle
## Author: nmessa
## Draws a circle moving in the X and Y direction
## it bounces when it gets to the edge of the screen

from graphics import *
import time

def main():
    height = 480
    width = 640
    radius = 50
    #Create a windows to draw in
    win = GraphWin('Circle Move XY with Bounce', width, height)

    #Define a circle to draw
    shape = Circle(Point(width/2, height/2), radius)

    #set the drawing parameters
    shape.setOutline("red")
    shape.setFill("green")
    shape.setWidth(5)

    #draw the circle in the window
    shape.draw(win)
    dx = 30
    dy = 30
    while True:
        shape.move(dx, dy)
        time.sleep(0.06)
        center = shape.getCenter()
        if center.y > height - radius or center.y < radius:
            dy = -dy
        if center.x > width - radius or center.x < radius:
            dx = -dx
    
    time.sleep(3)
    win.close()

main()
