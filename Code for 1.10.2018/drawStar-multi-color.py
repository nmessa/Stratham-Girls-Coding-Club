## Draw Star
## Author: nmessa
## Draws a star using alternative graphics module

from graphics import *
import time
from random import choice

def main():
    colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'magenta',
              'maroon', 'PeachPuff', 'PapayaWhip', 'MistyRose4', 'cornsilk',
              'Chartreuse'] 
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
    shape.setWidth(5)

    while True:
        #set the drawing parameters
        #Add code here
    
        #draw the star in the window
        #Add code here
        

        #wait 0.2 seconds then undraw the star
        #Add code here
        
    win.close()

main()
