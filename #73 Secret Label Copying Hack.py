from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# Create Label
label = Label(root,text="Label 1",font=("Calibri",20))
label.pack(pady=10)

# Create String Var
text = StringVar()
text.set("Label 2")

# Create Entry Box
entry = Entry(root,font=("Calibri",20),bd=0,state="readonly",textvariable=text,justify="center")
entry.pack(pady=10)

root.mainloop()