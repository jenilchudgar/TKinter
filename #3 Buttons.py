from tkinter import *

root = Tk()

def clicked():
    label = Label(root,text="Hi, this is python!")
    label.pack()

button = Button(root,text="Click Me!",pady=10,padx=50,command=clicked,fg="blue",bg="yellow")
button.pack()

root.mainloop()