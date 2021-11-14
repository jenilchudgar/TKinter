from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# Create Canvas
canvas = Canvas(root,width=200,height=200,bg="white")
canvas.pack(pady=20)

# Properties: x1,y1,x2,y2,fill="color" 

# Create Line
canvas.create_line(0,100,200,100,fill="red")
canvas.create_line(100,0,100,200,fill="red")

# Create Rectangle
# canvas.create_rectangle(x1,y1,x2,y2,fill="color")

# Create Oval
# Oval x1,y1: Top Left
# Oval x2,y2: Bottom Right
canvas.create_oval(50,100,150,50,fill="cyan")

root.mainloop()