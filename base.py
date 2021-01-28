#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from tkinter import *
from PIL import ImageTk, Image


root = Tk()

def open():
    global my_img
    top = Toplevel()
    my_img = Image.open('D:\programming\Tkinter_practice\image\circuit.png')
    resized = my_img.resize((300, 300), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(resized)
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close", command=top.destroy).pack()


btn = Button(root, text="open window", command=open).pack()




mainloop()