from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# def displayItem(event):
#     label.config(text=clicked.get())

def displayItemCombo(event):
    label.config(text=comboBox.get())

options = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

clicked = StringVar()
clicked.set(options[0])

# dropDown = OptionMenu(root,clicked,*options,command=displayItem)
# dropDown.pack()

comboBox = ttk.Combobox(root,values=options)
comboBox.current(0)
comboBox.bind("<<ComboboxSelected>>",displayItemCombo)
comboBox.pack()


label = Label(root,text="")
label.pack()

root.mainloop()