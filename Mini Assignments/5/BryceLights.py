# Your name: Bryce Matthes  
# Student ID: 10147880
# Tutorial #: T07
# Version: 1
# LC: 94
'''
A simple program that generates three circles with tkinter and then
allows those circles to be refilled with a random choice of red,blue,green,orange
when a button is clicked.

Based on Tam's source for graphics.py
'''

import random
from tkinter import *

aWindow = Frame()
aButton = Button(aWindow)

def createShapes():
    '''
    Based of Tam's example, draws three circles.

    The first circle (Far Left) has the ID of redCirc because it defaults to red
    The next circle (Middle) has the ID of greenCirc because it defaults to green
    The final circle (Far Right) has the ID of blueCirc because it defaults to blue

    aDrawingCanvas is a global because button actions can't handle parameters (from my testing)
    '''
    # Shape's first four properties: Top LHS(x,y),Bottom RHS(x,y) 
    global aDrawingCanvas
    aDrawingCanvas.create_oval(30,200,120,105, fill = "red", tag="redCirc")
    aDrawingCanvas.create_oval(150,200,240,105, fill = "green", tag="greenCirc")
    aDrawingCanvas.create_oval(270,200,360,105, fill = "blue", tag="blueCirc")       

def colorChange():
    '''
    Handles changing the color of the three circles. Each circle is
    given a string value of a color (IE: "blue", "red", "green") and that
    is used as the new fill color

    Color picker is used to get the string value to fill the circles

    the message "Run color_change" is used to show that the function is being run
    '''
    global aDrawingCanvas
    global counter
    counter = counter + 1
    print("Run colorChange()")
    print("Counter:" +str(counter))
    colorName1 = pickColor()
    colorName2 = pickColor()
    colorName3 = pickColor()
    aDrawingCanvas.itemconfig("redCirc", fill = colorName1)
    aDrawingCanvas.itemconfig("greenCirc", fill = colorName2)
    aDrawingCanvas.itemconfig("blueCirc", fill = colorName3)

def pickColor():
    '''
    Generates 0-3 randomly, each number points to a color.
    that color value is returned.
    '''
    colorPicker = random.randrange(0,4,1)
    colorName = ""
    if colorPicker == 0:
        colorName = "red"
    if colorPicker == 1:
        colorName = "blue"
    if colorPicker == 2:
        colorName = "green"
    if colorPicker == 3:
        colorName = "orange"        
    return (colorName)           


def start():
    '''
    Main function, generates the windows for the button and circles.
    '''
    global aDrawingCanvas
    window = Tk()
    window.title("Colored Lights")   # Label the title bar
    aDrawingCanvas = Canvas(window,width=390,height=260,bg ="white")
    createShapes() # Makes the circles
    aWindow.pack()
    aButton['text'] = "Change Color" #Button Label
    aButton['command'] = colorChange #onClick run colorChange
    aButton.grid(row=0, column=0)
    aDrawingCanvas.pack()
    window.mainloop()

aDrawingCanvas = Canvas() #For global   
counter = 0 #For global
start()