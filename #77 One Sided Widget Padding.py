from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")
root.config(bg="blue")

# E.g 1
l1 = Label(root,text="Hi",font=("Calibri",15))
l1.pack(pady=(10,0))

l2 = Label(root,text="Hi",font=("Calibri",15))
l2.pack()

# E.g 2
l1 = Label(root,text="Hi",font=("Calibri",15))
l1.grid(row=0,column=0,padx=(10,10))

l2 = Label(root,text="Hi",font=("Calibri",15))
l2.grid(row=0,column=1)


# !!! Run only on e.g on time
root.mainloop()