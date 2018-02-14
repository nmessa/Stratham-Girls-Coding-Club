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
    #Add code here

def line_blue():
    #Add code here

def line_yellow():
    #Add code here

def line_black():
    #Add code here

def line_white():
    #Add code here

def smaller():
    global line_width
    global line_length
    if (line_width > 5):
        line_width = line_width-5
        line_length = line_length-5

def bigger():
    #Add code here

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

#Create a canvas to draw on
canvas = Canvas(bg=canvas_color, height=canvas_height,
                width=canvas_width, highlightthickness=0)
canvas.pack()

#Connect the e key to the erase_all function
window.bind("e", erase_all)

## load images for buttons:
red = PhotoImage(file="red.gif")
#Add code here

## create frame:
frame = Frame(window)
frame.pack()

## build set of buttons
Button(frame, image=red, command=line_red).pack(side=LEFT)
#Add code here


## bind mouse movement to a function:
canvas.bind("<B1-Motion>", paint)
canvas.bind("<Button-1>", paint)

# start tkinter's main loop
window.mainloop()
