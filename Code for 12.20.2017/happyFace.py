import turtle
from random import *
def happyFace(x, y):
    t.penup()
    t.home()
    t.goto(x,y)
    t.color('black', 'yellow')
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

happyFace(0,0)
drawEye(-50, 250)
drawEye(70, 250)
drawNose(15, 150)
drawMouth(-60, 90)

t.hideturtle()
t.done()

#Modify this program to have multicolored happy faces
