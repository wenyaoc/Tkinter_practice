#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("circuit calculation")
root.iconbitmap('favicon.ico')

def open():
    global my_img
    top = Toplevel()
    input_data = Label(top, text="Answer:")
    input_data.grid(row=1, column=0, columnspan=1)
    btn2 = Button(top, text="close", command=top.destroy).pack()



my_img = Image.open('D:\programming\Tkinter_practice\image\circuit.png')
resized = my_img.resize((350, 350), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(resized)
my_label = Label(root, image=my_img).grid(columnspan=3)


input_data = Label(root, text="input data:")
input_data.grid(row=1, column=0, columnspan=3)



beta = Label(root, text=u'\u03B2' + ":")
beta.grid(row=2, column=0)
beta_in = Entry(root, width=10)
beta_in.grid(row=3, column=0)
beta_in.insert(0, "100")

Va = Label(root, text="Va(V):")
Va.grid(row=2, column=1)
Va_in = Entry(root, width=10)
Va_in.grid(row=3, column=1)
Va_in.insert(0, "-100")

r1 = Label(root, text="R1(\u03A9):")
r1.grid(row=2, column=2)
r1_in = Entry(root, width=10)
r1_in.grid(row=3, column=2)
r1_in.insert(0, "800000")

r2 = Label(root, text="R2(\u03A9):")
r2.grid(row=4, column=0)
r2_in = Entry(root, width=10)
r2_in.grid(row=5, column=0)
r2_in.insert(0, "80000")

re = Label(root, text="Rl(\u03A9):")
re.grid(row=4, column=1)
re_in = Entry(root, width=10)
re_in.grid(row=5, column=1)
re_in.insert(0, "10000")

rl = Label(root, text="Re(\u03A9):")
rl.grid(row=4, column=2)
rl_in = Entry(root, width=10)
rl_in.grid(row=5, column=2)
rl_in.insert(0, "1000")

rs = Label(root, text="Rs(\u03A9):")
rs.grid(row=6, column=0)
rs_in = Entry(root, width=10)
rs_in.grid(row=7, column=0)
rs_in.insert(0, "50")

cc = Label(root, text="Cc(\u03BCf):")
cc.grid(row=6, column=1)
cc_in = Entry(root, width=10)
cc_in.grid(row=7, column=1)
cc_in.insert(0, "0.5")

ce = Label(root, text="CE(\u03BCf):")
ce.grid(row=6, column=2)
ce_in = Entry(root, width=10)
ce_in.grid(row=7, column=2)
ce_in.insert(0, "1")


#Vs.pack()
btn = Button(root, text="get answer", command=open).grid(columnspan=3)


mainloop()