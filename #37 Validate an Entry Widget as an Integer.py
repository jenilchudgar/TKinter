from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

def number():
    try:
        int(inputBox.get())
        status_bar.config(text="Is a integer number!")
    except:
        status_bar.config(text="Is not a integer number!")

label = Label(root,text="Enter an integer number:",font=('Calibri',18))
label.pack(pady=10)

inputBox = Entry(root,font=('Calibri',16))
inputBox.pack()

btn = Button(root,text="Submit!",font=('Calibri',14),command=number)
btn.pack(pady=10)

status_bar = Label(root,text="")
status_bar.pack()

root.mainloop()