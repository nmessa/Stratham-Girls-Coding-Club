#Making a snowflake - version 6
#make 4 snowflakes at random locations
import turtle, random
colors = ["white", "red", "cyan", "yellow"]

#function to draw a branch of a snowflake
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

def place():
    elsa.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    elsa.goto(x, y)
    elsa.pendown()
    
#setup window and turtle
window = turtle.Screen()
window.bgcolor("grey")
elsa = turtle.Turtle()
elsa.color("white")
elsa.speed(0)

#place turtle in the center of the screen
elsa.penup()
elsa.forward(90)
elsa.left(45)
elsa.pendown()

#draw four snowflakes at random locations
for i in  range(4):
    place()
    elsa.color(colors[i])
    #draw eight branches of snowflake
    for i in range(8):
        branch()
        elsa.left(45)
        
elsa.hideturtle()
window.exitonclick()

