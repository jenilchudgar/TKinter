from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")
root.resizable(True,True)

size_grip = ttk.Sizegrip(root)
size_grip.pack()

root.mainloop()