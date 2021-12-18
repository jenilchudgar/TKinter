from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

w = 350
h = 250

x = w//2
y = h//2

canvas = Canvas(root,width=w,height=h,bg="white")
canvas.pack(pady=10)


root.mainloop()