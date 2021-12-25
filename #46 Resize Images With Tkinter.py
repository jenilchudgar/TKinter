from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

pic = Image.open("states/goa.png")

resized = pic.resize((100,200),Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resized)

label = Label(root,image=new_pic)
label.pack(pady=20)

root.mainloop()