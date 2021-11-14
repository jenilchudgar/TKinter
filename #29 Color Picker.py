from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# Functions
def chooseColor():
    color = colorchooser.askcolor()[1]
    # Label(root,text=color).pack()

    root.config(bg=color)

btn = Button(root,text="Choose Color",command=chooseColor)
btn.pack()

root.mainloop()