from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry(f"{eval('400*2')}x{eval('250*2')}")

# Define image
bg = PhotoImage(file="img/mario.png")

# Step 1
# # Define label
# label = Label(root,image=bg,font=("Calibri",15))
# label.place(x=0,y=0,relwidth=1,relheight=1)

# l = Label(root,text="Hi",font=("Calibri",50),bg="#6b88fe")
# l.pack(pady=500/5+50)

# Step 2
canvas = Canvas(root,width=800,height=500)
canvas.pack(fill=BOTH,expand=True)

# Set Img in Canvas
canvas.create_image(0,0,image=bg,anchor=NW)

canvas.create_text(400,250,text="Welcome!",font=("Calibri",50),fill="YELLOW")

def lol1():
    pass

one_btn = Button(root,text="Start!",command=lol1)
one_btn.pack(pady=10)

two_btn = Button(root,text="Reset!",command=lol1)
two_btn.pack(pady=10)

one_win = canvas.create_window(10,10,anchor=NW,window=one_btn)
lol = canvas.create_window(50,10,anchor=NW,window=two_btn)
root.mainloop()