from tkinter import *
import math
import threading

class MainFrame():
    def __init__(self, parent):

        parent.columnconfigure(0, weight = 1)
        parent.rowconfigure(0, weight = 1)
        
        frame = Frame(parent)
        frame.grid(sticky=W+E+N+S)
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure(1, weight = 1)
        
        self.label = Label(frame, text = "Graph", bg = "red", fg="white")
        self.label.grid(row=0, column=0, columnspan=1, sticky=W+E)

        self.canvas = Canvas(frame, width = 500, height = 500, bg = 'white')
        self.canvas.grid(row=1, column=0, sticky=W+E+N+S)

        bttnframe = Frame(frame)
        bttnframe.grid(row=2, column=0, sticky= (W, E))
        bttnframe.columnconfigure(0, weight = 1)
        bttnframe.columnconfigure(1, weight = 1)

        self.bttn1 = Button(bttnframe, text = "Previous")
        self.bttn1.grid(row=0, column = 0, sticky=(W, E))

        self.bttn2 = Button(bttnframe, text = "Next")
        self.bttn2.grid(row=0, column = 1, sticky=(W, E))

        radiobttnframe = Frame(frame)
        radiobttnframe.grid(row=1, column=1, sticky=(N, S))
        radiobttn1 = Radiobutton(radiobttnframe, text="Mode 1")
        radiobttn1.grid(row=0, sticky=W, padx=30)
        radiobttn2 = Radiobutton(radiobttnframe, text="Mode 2")
        radiobttn2.grid(row=1, sticky=W, padx=30)
        radiobttn3 = Radiobutton(radiobttnframe, text="Mode 3")
        radiobttn3.grid(row=2, sticky=W, padx=30)

root = Tk()
MainFrame(root)
