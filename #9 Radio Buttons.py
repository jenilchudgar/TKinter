from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("TKinter in Python: Radio Buttons")
root.iconbitmap("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\computer.ico")

# r=IntVar()

def click(val):
    label = Label(root,text=str(val))
    label.pack()

editor = StringVar()


MODES = [
    ("Visual Studio Code","Visual Studio Code"),
    ("PyCharm","PyCharm"),
    ("Sublime Text Editor","Sublime Text Editor"),
    ("IDLE","IDLE"),
] 

for text,val in MODES:
    Radiobutton(root,text=text,value=val,variable=editor).pack(anchor=W)

# Radiobutton(root,text="Option 1",variable=r,value=1).pack()
# Radiobutton(root,text="Option 2",variable=r,value=2).pack()
# Radiobutton(root,text="Option 3",variable=r,value=3).pack()
# Radiobutton(root,text="Option 4",variable=r,value=4).pack()

label = Label(root,text=editor.get())
label.pack()

button = Button(root,text="Click Me!",command=lambda: click(editor.get()))
button.pack()
root.mainloop()