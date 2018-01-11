## Draw Circle
## Author: nmessa
## Draws a circle moving in the Y direction with wrap around

from graphics import *
import time

def main():
    height = 480
    width = 640
    radius = 50
    #Create a windows to draw in
    win = GraphWin('Circle Move Y with Wrap', width, height)
    win.setBackground('white')

    #Define a circle to draw
    shape = Circle(Point(width/2, height/2), radius)

    #set the drawing parameters
    shape.setOutline("red")
    shape.setFill("green")
    shape.setWidth(10)

    #draw the circle in the window
    shape.draw(win)
    dx = 0
    dy = 10
    while True:
        shape.move(dx, dy)
        time.sleep(0.06)
        center = shape.getCenter()
        if center.y > height:
            shape.move(0, -height)
    time.sleep(3)
    win.close()

main()
