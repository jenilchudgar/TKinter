from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

btn1_btn = Button(root,text="Button 1")
btn1_btn.grid(row=0,column=0,sticky=NSEW)

btn2_btn = Button(root,text="Button 2")
btn2_btn.grid(row=1,column=0,sticky=NSEW)

Grid.rowconfigure(root,(0,1),weight=1)
Grid.columnconfigure(root,0,weight=1)

root.mainloop()