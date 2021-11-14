from tkinter import *

root = Tk()

def clicked():
    label = Label(root,text=inputField.get())
    label.pack()
    button["state"] = DISABLED
    inputField.delete(0,END)

inputField=Entry(root,width=30,borderwidth=10)
inputField.pack()

button = Button(root,text="Click Me!",pady=10,padx=50,command=clicked,fg="black",bg="white")
button.pack()

root.mainloop()