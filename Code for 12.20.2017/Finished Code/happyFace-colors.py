import turtle, time
from random import *

colors= ['red', 'yellow', 'green', 'blue', 'cyan', 'magenta', 'hot pink',
         'lavender', 'maroon', 'misty rose']

def happyFace(x, y):
    t.penup()
    t.home()
    t.goto(x,y)
    t.color('black', choice(colors))
    t.pensize(10)
    t.pendown()
    t.begin_fill()
    for i in range(36):
        t.forward(30)
        t.left(10)
    t.end_fill()
    t.penup()

def drawEye(x, y):
    t.penup()
    t.goto(x,y)
    t.color('black')
    t.pensize(25)
    t.pendown()
    t.dot()

def drawNose(x, y):
    t.penup()
    t.goto(x,y)
    t.color('black')
    t.pensize(30)
    t.pendown()
    t.dot()

def drawMouth(x, y):
    t.penup()
    t.goto(x,y)
    t.color('black')
    t.pensize(10)
    t.pendown()
    t.right(60)
    t.circle(100, 120)
    
t = turtle
t.speed(0)

while True:
    happyFace(0,0)
    drawEye(-50, 250)
    drawEye(70, 250)
    drawNose(15, 150)
    drawMouth(-60, 90)
    time.sleep(2)
    t.clear()

t.hideturtle()
t.done()
