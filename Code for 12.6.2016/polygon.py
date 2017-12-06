# polygon.py
import turtle
t=turtle
t.speed(0)
t.color('red')

def polygon(side_length, sides):
    for i in range(sides):
        t.forward(side_length)
        t.right(360/sides)

for i in range(20):
    polygon(150, 5)
    t.left(18)
t.hideturtle()
# end
t.done()
