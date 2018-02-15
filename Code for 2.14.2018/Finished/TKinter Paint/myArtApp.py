# myArtApp.py
from tkinter import *

#### Set variables:
canvas_height = 800
canvas_width = 1200
canvas_color = "white"
x_coord = canvas_width/2
y_coord = canvas_height
line_color = "red"
line_width = 5
line_length = 5

#### Functions:   
def erase_all(event):
    canvas.delete(ALL)

def line_red():
    global line_color
    line_color = "red"

def line_green():
    global line_color
    line_color = "green"

def line_blue():
    global line_color
    line_color = "blue"

def line_yellow():
    global line_color
    line_color = "yellow"

def line_black():
    global line_color
    line_color = "black"

def line_white():
    global line_color
    line_color = "white"

def smaller():
    global line_width
    global line_length
    if (line_width > 5):
        line_width = line_width-5
        line_length = line_length-5

def bigger():
    global line_width
    global line_length
    if (line_width <= 50):
        line_width = line_width + 5
        line_length = line_length + 5

def paint(event):
    width = line_width/2
    x1 = event.x - width
    y1 = event.y - width
    x2 = event.x + width
    y2 = event.y + width
    canvas.create_oval(x1, y1, x2, y2, fill=line_color, outline="")

#### main:
window = Tk()
window.title("MyArtApp")
canvas = Canvas(bg=canvas_color, height=canvas_height,
                width=canvas_width, highlightthickness=0)
canvas.pack()

window.bind("e", erase_all)

## load images for buttons:
red = PhotoImage(file="red.gif")
blue = PhotoImage(file="blue.gif")
green = PhotoImage(file="green.gif")
yellow = PhotoImage(file="yellow.gif")
black = PhotoImage(file="black.gif")
white = PhotoImage(file="white.gif")
plus = PhotoImage(file="plus.gif")
minus = PhotoImage(file="minus.gif")

## create frame:
frame = Frame(window)
frame.pack()

## build set of buttons
Button(frame, image=red, command=line_red).pack(side=LEFT)
Button(frame, image=green, command=line_green).pack(side=LEFT)
Button(frame, image=blue, command=line_blue).pack(side=LEFT)
Button(frame, image=yellow, command=line_yellow).pack(side=LEFT)
Button(frame, image=black, command=line_black).pack(side=LEFT)
Button(frame, image=white, command=line_white).pack(side=LEFT)
Button(frame, image=plus, command=bigger).pack(side=LEFT)
Button(frame, image=minus, command=smaller).pack(side=LEFT)

## bind mouse movement to a function:
canvas.bind("<B1-Motion>", paint)
canvas.bind("<Button-1>", paint)

# start tkinter's main loop
window.mainloop()
