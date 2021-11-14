from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("Python")
root.iconbitmap("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\computer.ico")
root.geometry("400x400")

def check():
    global label,res
    label.configure(text="Checked" if res.get()==1 else "Not Checked")

res = IntVar()
c1 = Checkbutton(root,text="Option 1",variable=res,command=check)
c1.deselect()
c1.pack()
# c2 = Checkbutton(root,text="Option 2",variable=res).pack()
# c3 = Checkbutton(root,text="Option 3",variable=res).pack()
# c4 = Checkbutton(root,text="Option 4",variable=res).pack()

label = Label(root)
check()
label.pack()

root.mainloop()