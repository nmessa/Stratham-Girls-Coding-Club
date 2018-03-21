#### Chapter 2 Answers

# Idea 3
# A Random Joke Generator App

from tkinter import *
import random

# key press function:
def click():
    entered_text = entry.get()  # collect text from text entry box
    output.delete(0.0, END)  # clear text box
    try:
        answer = my_flashcards[entered_text]
    except:
        answer = "There is no entry for this word."
    output.insert(END, answer)

def click1():
    questions = list(my_flashcards.keys()) # put all the keys into a list so that their indexes are numerical
    question = random.choice(questions) # choose a random question
    entry.delete(0, END)  # clear input text box
    output.delete(0.0, END)  # clear output text box
    entry.insert(END, question)

##### main:
window = Tk()
window.title("My Joke App")

# Add a get question button:
b='GET JOKE'
Button(window, text=b, width=10, command=click1).grid(row=0,column=0, sticky=W)

# create text entry box
entry = Entry(window, width=58, bg="light green")
entry.grid(row=1, column=0, columnspan=2, sticky=W)

# Add a submit button:
b='GET ANSWER'
Button(window, text=b, width=10, command=click).grid(row=0,column=1, sticky=E)

# create another label
Label(window, text="\nAnswer:").grid(row=3, column=0, sticky=W)

# create text box
output = Text(window, width=75, height=6, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

# The tuple of tuples:
my_flashcards = { 
    'What goes clip?': 'A one-legged horse.',
    'Why did the scarecrow get a gold medal?': 'He was outstanding in his field.',
    'A man threw some cheese at me today in the supermarket.': 'That was so mature.',
    'Doctor, Doctor I seem to be fading away.': 'Next patient please.',
    'How many fools does it take to fit a light bulb?': 'Five: One to hold the bulb and four to turn the ladder.',
    'Where did Napoleon keep his armies?': 'Up his sleevies.',
    'There are only 10 kinds of people in this world.': "Those who know binary and those who don't."
    }

##### Run mainloop
window.mainloop()

