#Making a snowflake - version 4
#draw a single branch of a snowflake
import turtle, random

window = turtle.Screen()
elsa = turtle.Turtle()
elsa.speed(0) #make it go fast
window.bgcolor("blue")
elsa.color('cyan')

#draw branch - put in function later
for i in range(3):
    for i in range(3):
        elsa.forward(30)
        elsa.backward(30)
        elsa.right(45)
    elsa.left(90)
    elsa.backward(30)
    elsa.left(45)
elsa.right(90)
elsa.forward(90)


window.exitonclick()
