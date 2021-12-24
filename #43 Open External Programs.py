import os
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

def open_ex_pr():
    my_pr = filedialog.askopenfilename()
    os.system('"%s"' % my_pr)

btn = Button(root,text="Open Program!",command=open_ex_pr)
btn.pack(pady=20)

root.mainloop()