from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("500x600")


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

def add_img():
    global img

    # Image
    img = PhotoImage(file="img/melon.png")
    text_box.image_create(text_box.index(INSERT),image=img)

frame = Frame(root)
frame.pack(pady=20)

scroll_bar = Scrollbar(frame)
scroll_bar.pack(side=RIGHT,fill=Y)

text_box = Text(frame,width=40,height=10,font=("Calibri",16),selectbackground="yellow",selectforeground="black",yscrollcommand=scroll_bar.set)
text_box.pack()

scroll_bar.config(command=text_box.yview)

open_btn = Button(root,text="Open!",command=open_file)
open_btn.pack(pady=10)

save_btn = Button(root,text="Save!",command=save_file)
save_btn.pack(pady=10)

image_btn = Button(root,text="Add Image!",command=add_img)
image_btn.pack(pady=10)

root.mainloop()