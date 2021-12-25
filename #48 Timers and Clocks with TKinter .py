from tkinter import *
import time

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# def update():
#     label.config(text="Hello!")

# label = Label(root,text="OLD")
# label.pack(pady=10)

# label.after(2000,update)

def clock():
    hr = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")

    am_or_pm = time.strftime("%p")
    timezone = time.strftime("%Z")

    label.config(text=f"{hr}:{min}:{sec} {am_or_pm}\n{timezone}")

    label.after(1000,clock)

label = Label(root,text="",font=("Calibri",25),bg="black",fg="red")
label.after(1000,clock)
label.pack(pady=20)

root.mainloop()