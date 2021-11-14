from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("800x500")


def showText():
    t = ""
    for e in entryBoxes:
        t = t + e.get() + "\n"
        l.config(text=t)


entryBoxes = []

global x, y
x, y = 0, 0
for x in range(5):
    for y in range(5):
        entry = Entry(root)
        entry.grid(row=x, column=y, padx=15)
        entryBoxes.append(entry)

btn = Button(root, text="Show Text!", command=showText)
btn.grid(row=x+1, column=0, pady=10)

l = Label(root, text="")
l.grid(row=x+2, column=0)
x += 1

root.mainloop()
