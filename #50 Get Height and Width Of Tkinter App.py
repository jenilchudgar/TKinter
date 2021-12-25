from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

def click_me():
    label.config(text=f"{root.winfo_geometry()}\n\nWidth: {root.winfo_width()}\nHeight: {root.winfo_width()}\n x: {root.winfo_x()}\ny: {root.winfo_y()}")

    click_btn.after(500,click_me)


label = Label(root,text=f"{root.winfo_geometry()}")
label.pack(pady=20)

click_btn = Button(root,text="Click Me!",command=click_me)
click_btn.pack()

root.mainloop()