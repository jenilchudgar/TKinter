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

circle = canvas.create_oval(x,y,x+20,y+20)

def left(e):
    x = -10
    y = 0
    canvas.move(circle,x,y)

def right(e):
    x = +10
    y = 0
    canvas.move(circle,x,y)

def up(e):
    x = 0
    y = -10
    canvas.move(circle,x,y)

def down(e):
    x = 0
    y = +10
    canvas.move(circle,x,y)

root.bind("<Left>",left)
root.bind("<Right>",right)
root.bind("<Up>",up)
root.bind("<Down>",down)

root.mainloop()