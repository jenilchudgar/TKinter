from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("200x200")

def resize(e):
    x = ((e.width)/0.60*e.height)
    btn1_btn.config(font=("Calibri",int((x/1000)/10)))


btn1_btn = Button(root,text="Button 1")
btn1_btn.grid(row=0,column=0,sticky=NSEW)

Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)

# Binding
root.bind("<Configure>",resize)

root.mainloop()