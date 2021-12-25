from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

def btn_hover(e):
    my_btn.config(bg="white")
    status.config(text="I am hovering")

def btn_left(e):
    my_btn.config(bg="SystemButtonFace")
    status.config(text="")

my_btn = Button(root,text="Click Me!",font=('Calibri',20))
my_btn.pack(pady=20)

my_btn.bind("<Enter>",btn_hover)
my_btn.bind("<Leave>",btn_left)

status = Label(root,text="",font=("Calibri",15),relief=SUNKEN,anchor=E,bd=1)
status.pack(fill=X,side=BOTTOM,ipady=2)

root.mainloop()