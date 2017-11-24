#Making a snowflake - version 3
#change random colors of parallelogram snowflake
import turtle, random

window = turtle.Screen()
elsa = turtle.Turtle()
elsa.speed(0) #make it go fast
window.bgcolor("blue")
elsa.color('cyan')
colors=["cyan","red","white","yellow","purple"] #list of colors we will cycle through

for i in range(20):
    for i in range(2):
        elsa.forward(100)
        elsa.right(60)
        elsa.forward(100)
        elsa.right(120)
    elsa.right(18)
    elsa.color(random.choice(colors))

window.exitonclick()
