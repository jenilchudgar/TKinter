from tkinter import *
from tkinter import font

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("500x400")

text_box = Text(root,width=40,height=10,font=("Calibri",16))
text_box.pack(pady=20)

btn_frame = Frame(root,pady=10,padx=10)
btn_frame.pack()

def clear():
    text_box.delete(1.0,END)

clear_btn = Button(btn_frame,text="Clear",command=clear)
clear_btn.grid(row=0,column=0)

def get_text():
    print(text_box.get(1.0,END))

get_text_btn = Button(btn_frame,text="Get Text!",command=get_text)
get_text_btn.grid(row=0,column=1,padx=10)

root.mainloop()