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
global my_img,img
img = PhotoImage(file="melon.png")

my_img = canvas.create_image(0,0,anchor=NW,image=img)

def move(e:Event):
    global my_img,img
    x = e.x 
    y = e.y
    img = PhotoImage(file="melon.png")
    my_img = canvas.create_image(x,y,image=img)

root.bind('<B1-Motion>',move)

root.mainloop()