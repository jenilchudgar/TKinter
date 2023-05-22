import playsound
from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")
global counter
def su():
    global counter
    counter = int(t.get())

t = Entry(root,font=('Calibri',20))
t.pack()
s = Button(root,text="Submit Time!",command=su,font=('Calibri',20))
s.pack()

def update():
    global counter,Label
    if counter>0:
        label.configure(text=str(counter))
        label.pack()
        counter-=1
        label.after(1000,update)
    elif counter==-1:
        label.config(text="Done!")
    else:
        label.config(text="Done!")
        playsound.playsound("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\UC3CKCR-game-over-a.mp3")
        playsound.playsound("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\UC3CKCR-game-over-a.mp3")
        playsound.playsound("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\UC3CKCR-game-over-a.mp3")


def startT():
    global counter,label
    label = Label(root,text="",font=('Calibri',60),pady=20)
    label.pack()

    label.after(1000,update)

def close():
    global counter
    counter=-1

start = Button(root,text="Start",font=('Calibri',20),command=startT)
start.pack(pady=20)

stop = Button(root,text="Stop",font=('Calibri',20),command=close)
stop.pack()
root.mainloop()