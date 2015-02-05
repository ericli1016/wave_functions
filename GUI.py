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
        self.canvas.grid(row=1, column=0, columnspan=1, sticky=W+E+N+S)

root = Tk()
MainFrame(root)
