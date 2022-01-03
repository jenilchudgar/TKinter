from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("500x400")

text_box = Text(root,width=40,height=10,font=("Calibri",16))
text_box.pack(pady=20)

def open_file():
    global file_name
    file_name = filedialog.askopenfilename(initialdir="",title="Open File!",filetypes=(("Text Files","*.txt"),))

    with open(file_name,"r") as f:
        text = f.read()
        text_box.insert(END,text)

def save_file():
    global file_name
    
    with open(file_name,"w") as f:
        text = text_box.get(1.0,END)
        f.write(text)

open_btn = Button(root,text="Open!",command=open_file)
open_btn.pack(pady=10)

save_btn = Button(root,text="Save!",command=save_file)
save_btn.pack(pady=10)

root.mainloop()