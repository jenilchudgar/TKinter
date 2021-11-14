from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Frames")

frame = LabelFrame(root,padx=10,pady=10) #Inside Padding
frame.pack(padx=10,pady=10) #Outside Padding

button = Button(frame,text="Button")
button.grid(row=0,column=0)

button2 = Button(frame,text="Button 2")
button2.grid(row=1,column=0)

root.mainloop()