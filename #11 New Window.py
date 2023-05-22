from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("TKinter in Python: New Window")
root.iconbitmap("computer.ico")

def openWin2():
    global img
    top = Toplevel()
    img = ImageTk.PhotoImage(Image.open("C:\\Users\\sanja\\Pictures\\Jenil\\aaaaa.png"))
    Label(top,image=img).pack()
    closeBtn = Button(top,text="Close Window!",command=top.destroy).pack()

Button(root,text="Click To Open\nSecond Window!",fg="red",command=openWin2).pack()


root.mainloop()