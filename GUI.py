from tkinter import *
import math
import threading

class MainFrame():
    def __init__(self, parent):

        parent.columnconfigure(0, weight = 1)
        parent.rowconfigure(0, weight = 1)
        
        self.frame = Frame(parent)
        self.frame.grid(sticky=W+E+N+S)
        self.frame.columnconfigure(0, weight = 1)
        self.frame.rowconfigure(1, weight = 1)
        
        self.label = Label(self.frame, text = "Graph", bg = "red", fg="white")
        self.label.grid(row=0, column=0, columnspan=1, sticky=W+E)

        self.canvas = Canvas(self.frame, width = 500, height = 500, bg = 'white')
        self.canvas.grid(row=1, column=0, sticky=W+E+N+S)

        self.bttnframe = Frame(self.frame)
        self.bttnframe.grid(row=2, column=0, sticky= (W, E))
        self.bttnframe.columnconfigure(0, weight = 1)
        self.bttnframe.columnconfigure(1, weight = 1)

        self.bttn1 = Button(self.bttnframe, text = "Previous", command = self.prev_mode)
        self.bttn1.grid(row=0, column = 0, sticky=(W, E))

        self.bttn2 = Button(self.bttnframe, text = "Next", command = self.next_mode)
        self.bttn2.grid(row=0, column = 1, sticky=(W, E))

        self.radiobttnframe = Frame(self.frame)
        self.radiobttnframe.grid(row=1, column=1, sticky=(N, S))
        self.radiobttnlist = []
        self.radiovariable = IntVar()
        self.buildradio()
        
        parent.update()
        self.draw_axis()
        self.draw_fn()
        self.canvas.bind("<Configure>",self.resize)        
        
    def buildradio(self):

        MODES = [
            ("Flatline", 0),
            ("Square Wave", 1),
            ("Cosine Wave", 2)]

        self.radiovariable.set(0)

        for text, mode in MODES:
            radiobttn = Radiobutton(self.radiobttnframe, text=text,
                                    variable=self.radiovariable, value = mode)
            radiobttn.grid(row=mode, padx=20, sticky = W)
            self.radiobttnlist.append(radiobttn)

    def prev_mode(self):
        mode = self.radiovariable.get()
        self.radiovariable.set((mode - 1) % len(self.radiobttnlist))

    def next_mode(self):
        mode = self.radiovariable.get()
        self.radiovariable.set((mode + 1) % len(self.radiobttnlist))

    def draw_axis(self):
        self.x_axis = self.canvas.create_line(
            0, self.canvas.winfo_height()/2,
            self.canvas.winfo_width(), self.canvas.winfo_height()/2,
            width = 1)
        self.y_axis = self.canvas.create_line(
            self.canvas.winfo_width()/2-180, 0,
            self.canvas.winfo_width()/2-180, self.canvas.winfo_height(),
            width = 1)

    def draw_fn(self):
        self.flatline()

    def flatline(self):
        self.wave = self.canvas.create_line(
            0, self.canvas.winfo_height()/2,
            self.canvas.winfo_width(), self.canvas.winfo_height()/2,
            width = 3)
        
    def resize(self, event):
        self.canvas.delete("all")
        self.draw_axis()
        self.draw_fn()

root = Tk()
MainFrame(root)
