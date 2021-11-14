from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("800x250")

def clickMe():
    btn_label.config(text="You clicked a btn!")

# Image
img_btn = PhotoImage(file="img/button.png")

# Label
# img_label = Label(image=img_btn)
# img_label.pack()

# Button
btn = Button(root,image=img_btn,command=clickMe,borderwidth=0)
btn.pack()

# Label
btn_label = Label(root,text="")
btn_label.pack()

root.mainloop()