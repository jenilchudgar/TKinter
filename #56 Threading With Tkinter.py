from random import randint
from tkinter import *
import threading
import time

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

def five_secs():
    time.sleep(5)
    label.config(text="5 Secs Up!!!!")

def rand():
    random_label.config(text=f"Random Number: {randint(1,100)}")

label = Label(root,text="Hello!",font=("Calibri",15))
label.pack(pady=20)

my_btn = Button(root,text="5 Secs!",command=threading.Thread(target=five_secs).start)
my_btn.pack(pady=10)

rand_btn = Button(root,text="Pick Random Number!",command=rand)
rand_btn.pack(pady=10)

random_label = Label(root,text="",font=("Calibri",15))
random_label.pack(pady=10)
root.mainloop()