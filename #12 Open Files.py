from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog

root = Tk()
root.title("TKinter in Python: Open Files")
root.iconbitmap("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\computer.ico")

def openFile():
    global l,img
    file = str(filedialog.askopenfile(initialdir="C:\\Users\\sanja\\Pictures",filetypes=(("png files",".png"),("jpg files",".jpg"),("all files","*.*"))))
    filename = ""
    for e in list(file)[25:-29]:
        filename = filename + e
    file = filename
    img = ImageTk.PhotoImage(Image.open(filename))
    l.pack_forget()
    l.configure(image=img)
    l.pack()
    print(file)

l = Label(root)
l.pack()
Button(root,text="Open File",fg="blue",command=openFile).pack()
root.mainloop()