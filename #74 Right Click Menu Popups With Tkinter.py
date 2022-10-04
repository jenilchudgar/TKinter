from cProfile import label
from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

l = Label(root,text="",font=("Calibri",15))
l.pack(pady=10)

def hi():
    l.config(text="Hello!")

def bye():
    l.config(text="Bye!")

def my_popup(e):
    menu.tk_popup(e.x_root,e.y_root)

# Creating a Menu
menu = Menu(root,tearoff=False)
menu.add_command(label="Say Hi!",command=hi)
menu.add_command(label="Say Bye!",command=bye)
menu.add_separator()
menu.add_command(label="Exit!",command=root.quit)

# Bind
root.bind("<Button-3>",my_popup)

root.mainloop()