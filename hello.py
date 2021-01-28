#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from tkinter import *

root = Tk()

myLabel = Label(root, text="Hello World!")
myLabel.pack()

myLabel.grid(row=0,column=0)
root.mainloop()
