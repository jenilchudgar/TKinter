from tkinter import *
from tkhtmlview import HTMLLabel

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

label = HTMLLabel(root,html="<h1>Hello!</h1> <ol><li>Pizza</li><li>Burger</li><li>Pasta</li></ol> <a href='youtube.com'>YouTube</a>")
label.pack()

root.mainloop()