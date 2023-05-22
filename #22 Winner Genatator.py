from tkinter import *
from random import randint

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

global entries
entries = ['Person A','Person B','Person C','Person D']

def pickWinner():
    global entries
    entries = list(set(entries))
    randomNum = randint(0,len(entries)-1)
    win.configure(text=entries[randomNum])
    
label = Label(root,text="Winner is...",font=('Calibri',15),pady=10)
label.pack()

button = Button(root,text="Pick!",command=pickWinner,font=('Calibri',18))
button.pack()

win = Label(root,font=('Calibri',18),pady=10)
win.pack()
root.mainloop()