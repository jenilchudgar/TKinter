from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x680")

l = ["error","gray75","gray50","gray12","hourglass","info","questhead","question","warning"]

for x in l:
    Button(root,bitmap=x,width=50,height=50,fg="red").pack(pady=10)

root.mainloop()