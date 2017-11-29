# squares.py
import turtle
t=turtle
t.speed(0)
t.color('red')

def square(side_length):
    n=0
    while n < 4:
        t.forward(side_length)
        t.right(90)
        n = n+1

for i in range(20):
    square(150)
    t.left(18)
t.hideturtle()
# end
t.done()
