from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# Keep track of Button State
global btn_state
btn_state = True

# Create a Label
label = Label(root,text="The switch is On!",font=("Calibri",15),fg="Green")
label.pack(pady=10)

# Define Our Images
on = PhotoImage(file="img/on.png")
off = PhotoImage(file="img/off.png")

# Create Image Buttons
def click():
    global btn_state
    if btn_state:
        btn.config(image=off)
        label.config(fg="Grey",text="The switch is Off!")
    else:
        btn.config(image=on)
        label.config(fg="Green",text="The switch is On!")

    btn_state = not btn_state

btn = Button(root,image=on,command=click,bd=0)
btn.pack(pady=10)


root.mainloop()