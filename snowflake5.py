#Making a snowflake - version 5
#draw a snowflake
import turtle, random

#draws branch of snowflake
def branch():
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

#setup window and turtle
window = turtle.Screen()
elsa = turtle.Turtle()
elsa.speed(0) #make it go fast
window.bgcolor("gray")

#place turtle at center of screen
elsa.penup()
elsa.forward(90)
elsa.left(45)
elsa.pendown()

#draw eight branches of snowflake
for i in range(8):
    branch()
    elsa.left(45)
elsa.hideturtle()
window.exitonclick()



window.exitonclick()
