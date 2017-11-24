#Making a snowflake - version 1
import turtle

window = turtle.Screen()
elsa = turtle.Turtle()


for i in range(2):
    elsa.forward(100)
    elsa.right(60)
    elsa.forward(100)
    elsa.right(120)

window.exitonclick()
