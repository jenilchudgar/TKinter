from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

def hover(e):
    global img,label
    img = PhotoImage(file="states/tripura.png")
    label.config(image=img)
    label.image = img

def left_hover(e):
    global img,labelx
    img = PhotoImage(file="states/goa.png")
    label.config(image=img)
    label.image = img
    
img = PhotoImage(file="states/goa.png")
label = Label(root,image=img)
label.pack(pady=10)

label.bind("<Enter>",hover)
label.bind("<Leave>",left_hover)

root.mainloop()