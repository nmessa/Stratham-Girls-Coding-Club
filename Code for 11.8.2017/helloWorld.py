##Hello world with functions
from turtle import *

def drawAnH():
    left(90)
    forward(100)
    back(50)
    right(90)
    forward(40)
    left(90)
    forward(50)
    back(100)

def drawAnI():
    forward(50)
    penup()
    forward(25)
    stamp()

def moveToNextLetter():
    penup()
    right(90)
    forward(40)
    left(90)
    pendown()

def moveTo(x, y):
    penup()
    goto(x, y)
    pendown()
    setheading(0)

def drawAnX():
    left(45)
    forward(100)
    back(50)
    left(90)
    back(50)
    forward(100)
    back(100)
    right(45)
    
pensize(5)
shape("turtle")
color('red')
for i in range(8):
    moveTo(-400 + 100 * i, -400 + 100 * i)
    drawAnH()
    moveToNextLetter()
    drawAnI()

##drawAnX()
##moveToNextLetter()
##drawAnI()
hideturtle()
done()
