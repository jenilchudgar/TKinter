from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

def click(e):
    Label(root,text="Hi "+e.keysym).pack()

btn = Button(root,text="Click Me!")
btn.bind("<Key>",click)
btn.pack(pady=10)

root.mainloop()