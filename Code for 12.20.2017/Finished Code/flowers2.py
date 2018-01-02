import turtle
from random import *
colors= ['red', 'yellow', 'green', 'blue', 'cyan', 'magenta', 'hot pink',
         'lavender', 'maroon', 'misty rose']
def drawFlower(size, x, y):
    color1 = choice(colors)
    color2 = choice(colors)
    t.color(color1, color2)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    while True:
        t.forward(size)
        t.left(170)
        if t.distance(x,y)<1:
            break
    t.end_fill()
    
t = turtle
t.speed(0)
for i in range(50):
    rsize= randint(75, 200)
    rx = randint(-300, 300)
    ry = randint(-300, 300)
    drawFlower(rsize, rx, ry)

t.hideturtle()
t.done()
