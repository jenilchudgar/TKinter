from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

def click(s):
    global l,clicked
    l.configure(text=clicked.get())
    l.pack()


l = Label(root)

options = [str(e) for e in range(1,11)]

clicked = StringVar()
clicked.set(options[0])

dropDown = OptionMenu(root,variable = clicked,*options,command=click).pack()

root.mainloop()