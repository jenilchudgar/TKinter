from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

def ring():
    root.bell()

ring_btn = Button(root,text="Ring!",command=ring,font=("Calibri",30))
ring_btn.pack(pady=10)


root.mainloop()