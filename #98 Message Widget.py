from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

frame1 = LabelFrame(root,text="Right Aligned")
frame1.pack()

msg = Message(
    frame1,
    text="Lorem ipsum dolor \nsit amet, consectetur adipiscing \nelit. Donec id nisl quam.\nSed at velit.",
    font=("Calibri",15),
    aspect=500,
    justify=RIGHT
)
msg.pack()

root.mainloop()