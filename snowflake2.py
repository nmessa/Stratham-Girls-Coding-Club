#Making a snowflake - version 2
import turtle

window = turtle.Screen()
elsa = turtle.Turtle()
elsa.speed(0) #make it go fast

for i in range(20):
    for i in range(2):
        elsa.forward(100)
        elsa.right(60)
        elsa.forward(100)
        elsa.right(120)
    elsa.right(18)

window.exitonclick()
