from tkinter import *
from simplePRG import greet

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

greeting = greet("Jenil")
g = Label(root,text=f"{greeting}",font=("Calibri",15))
g.pack(pady=10)

root.mainloop()



