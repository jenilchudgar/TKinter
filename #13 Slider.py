from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("Python")
root.iconbitmap("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\computer.ico")
root.geometry("400x400")

# verticalSlider = Scale(root,from_=0,to=100)
# verticalSlider.pack()

def s(event):
    global horizontalSlider
    l.configure(text=horizontalSlider.get())
    l.pack()

var = IntVar()
horizontalSlider = Scale(root,from_=0,to=1000,orient=HORIZONTAL,command=s)
horizontalSlider.pack()

l = Label(root,text=horizontalSlider.get())
l.pack()
root.mainloop()