# myArtApp.py
from tkinter import *

#### Set variables:
canvas_height = 800
canvas_width = 1200
canvas_color = "black"
x_coord = canvas_width/2
y_coord = canvas_height
line_color = "red"
line_width = 5
line_length = 5

background = "treescape.gif"
pen_up = False
current_line = None

#### Functions:
def erase_all(event):
    canvas.delete(ALL)
    canvas.create_image(0, 0, image=scene, anchor=NW)

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
        line_width = line_width+5
        line_length = line_length+5

def add_tree():
    canvas.create_image(x_coord, y_coord, image=tree, anchor=S)

def add_campbell():
    #Add code here

def add_ayesha():
    #Add code here

def add_jeff():
    #Add code here

def add_krysta():
    #Add code here

def add_hana():
    #Add code here

def add_jose():
    #Add code here

def add_leela():
    #Add code here

def paint(event):
    width = line_width/2
    x1 = event.x - width
    y1 = event.y - width
    x2 = event.x + width
    y2 = event.y + width
    canvas.create_oval(x1, y1, x2, y2, fill=line_color, outline="")

def paint2(event):
    #Add code here
    
    
#### main:
window = Tk()
window.title("MyArtApp")
canvas = Canvas(bg=canvas_color, height=canvas_height,
                width=canvas_width, highlightthickness=0)

#Create background scene
scene = PhotoImage(file=background)
canvas.create_image(0, 0, image=scene, anchor=NW)
canvas.pack()

#Connect e key to erase_all function
window.bind("e", erase_all)

## load images for top buttons:
red = PhotoImage(file="red.gif")
blue = PhotoImage(file="blue.gif")
green = PhotoImage(file="green.gif")
yellow = PhotoImage(file="yellow.gif")
black = PhotoImage(file="black.gif")
white = PhotoImage(file="white.gif")
plus = PhotoImage(file="plus.gif")
minus = PhotoImage(file="minus.gif")

## create top frame:
topframe = Frame(window)
topframe.pack()

## build top set of buttons
Button(topframe, image=red, command=line_red).pack(side=LEFT)
Button(topframe, image=green, command=line_green).pack(side=LEFT)
Button(topframe, image=blue, command=line_blue).pack(side=LEFT)
Button(topframe, image=yellow, command=line_yellow).pack(side=LEFT)
Button(topframe, image=black, command=line_black).pack(side=LEFT)
Button(topframe, image=white, command=line_white).pack(side=LEFT)
Button(topframe, image=plus, command=bigger).pack(side=LEFT)
Button(topframe, image=minus, command=smaller).pack(side=LEFT)

## load images for bottom buttons:
tree = PhotoImage(file="tree.gif")
#Add code here


## create bottom frame:
bottomframe = Frame(window)
bottomframe.pack()

## build bottom set of buttons:
Button(bottomframe, image=campbell, command=add_campbell).pack(side=LEFT)
#Add code here


## bind mouse movement to a function:
canvas.bind("<B1-Motion>", paint)
canvas.bind("<Button-1>", paint)
canvas.bind("<Button-3>", paint2)

# start tkinter's main loop
window.mainloop()
