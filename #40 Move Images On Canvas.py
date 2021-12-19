from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("800x400")

w = 350*2
h = 250*2

x = w//2
y = h//2

canvas = Canvas(root,width=w,height=h,bg="white")
canvas.pack(pady=10)

img = PhotoImage(file="melon.png")

my_img = canvas.create_image(0,0,anchor=NW,image=img)

def left(e):
    x = -10
    y = 0
    canvas.move(my_img,x,y)

def right(e):
    x = +10
    y = 0
    canvas.move(my_img,x,y)

def up(e):
    x = 0
    y = -10
    canvas.move(my_img,x,y)

def down(e):
    x = 0
    y = +10
    canvas.move(my_img,x,y)

root.bind("<Left>",left)
root.bind("<Right>",right)
root.bind("<Up>",up)
root.bind("<Down>",down)

root.mainloop()