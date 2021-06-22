These are the following steps to build youtube video downloader project in python :

Import libraries
Create display window
Create field to enter link
Create function to start downloading

1. Import Libraries
Start the project by importing the required modules.

from tkinter import *
from pytube import YouTube
In this python project, we import Tkinter and pytube modules.

2. Create Display Window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DataFlair-youtube video downloader")

Tk() used to initialize tkinter to create display window

geometry() used to set the window’s width and height

resizable(0,0) set the fix size of window

title() used to give the title of window

Label() widget use to display text that users can’t able to modify.

root is the name of the window

text which we display the title of the label

font in which our text is written

pack organized widget in block

link is a string type variable that stores the youtube video link that the user enters.

Entry() widget is used when we want to create an input text field.

width sets the width of entry widget

textvariable used to retrieve the value of current text variable to the entry widget

place() use to place the widget at a specific position

Button() widget used to display button on the window.

text which we display on the label

font in which the text is written

bg sets the background color

command is used to call the function

root.mainloop() is a method that executes when we want to run the program.