from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")


# Variables
count = 0
size = 16


def expand():
    global count,size

    if count < 10:
        size += 2

        # Config Button font size
        btn.config(font=("Calibri",size))

        # Increament Count
        count += 1

        root.after(10,expand)

    elif count == 10:
        contract()
        

def contract():
    global count,size
    
    if count <= 10 and count > 0:
        size -= 2
        btn.config(font=("Calibri",size))

        # Config Button font size
        btn.config(font=("Calibri",size))

        # Dereament Count
        count -= 1

        root.after(10,contract)

# Create a Button
btn = Button(root,text="Click Me!",command=expand,font=("Calibri",16))
btn.pack(pady=150)

root.mainloop()