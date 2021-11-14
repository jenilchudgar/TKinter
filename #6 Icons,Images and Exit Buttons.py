from tkinter import *
from time import sleep
from PIL import ImageTk,Image

root = Tk()
root.title("Window")
root.iconbitmap("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\application-blue.ico")
button = Button(root,text="Exit",fg="red",command=root.quit,padx=40,pady=10).pack()

img = ImageTk.PhotoImage(Image.open('C:\\Users\\sanja\\Pictures\\Icons\\icons\\share.png'))
label = Label(root,image=img)
label.pack()
root.mainloop()