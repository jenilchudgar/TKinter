from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

def resize():
    root.geometry(f"{w.get()}x{h.get()}")

label_w = Label(root,text="Width")
label_w.pack()

w = Entry(root,font=("Calibri",20))
w.pack(pady=10)

label_h = Label(root,text="Height")
label_h.pack()

h = Entry(root,font=("Calibri",20))
h.pack(pady=10)

resize_btn = Button(root,text="Resize!",command=resize)
resize_btn.pack(pady=10)

root.mainloop()