from tkinter import *
import pyttsx3

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def say():
    speak(entry.get())
    entry.delete(0,END)

entry = Entry(root,font=("Calibri",20))
entry.pack(pady=20)

btn = Button(root,text="Say!",command=say)
btn.pack(pady=10)

root.mainloop()