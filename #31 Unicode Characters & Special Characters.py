from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("200x50")

label = Label(root,text="42"+u"\u20B9",font=('Calibri',30))
label.pack()

root.mainloop()