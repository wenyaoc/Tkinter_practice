#!/usr/bin/env python 
# -*- coding:utf-8 -*-


from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name:")  #defult value

def myClick():
    myLabel = Label(root, text="hello " + e.get())
    myLabel.pack()

myButton = Button(root, text="Enter your name", padx=50, command=myClick, fg="red")
myButton.pack()
root.mainloop()
