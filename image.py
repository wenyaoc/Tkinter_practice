#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("image")
root.iconbitmap('D:\programming\Tkinter_practice\image\\favicon.ico')

my_img = ImageTk.PhotoImage(Image.open('D:\programming\Tkinter_practice\image\circuit.png'))
my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)

root.mainloop()