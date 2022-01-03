from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("500x680")

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

def select():
    s = text_box.selection_get()
    print(s)

def do_bold():
    cur_tags = text_box.tag_names("sel.first")
    bold_font = font.Font(text_box,text_box.cget("font"))
    bold_font.configure(weight=font.BOLD)

    text_box.tag_configure("bold",font=bold_font)

    if "bold" in cur_tags:
        text_box.tag_remove("bold","sel.first","sel.last")
    else:
        text_box.tag_add("bold","sel.first","sel.last")

def do_italic():
    cur_tags = text_box.tag_names("sel.first")
    italics_font = font.Font(text_box,text_box.cget("font"))
    italics_font.configure(slant=font.ITALIC)

    text_box.tag_configure("italic",font=italics_font)

    if "italic" in cur_tags:
        text_box.tag_remove("italic","sel.first","sel.last")
    else:
        text_box.tag_add("italic","sel.first","sel.last")

frame = Frame(root)
frame.pack(pady=20)

scroll_bar = Scrollbar(frame)
scroll_bar.pack(side=RIGHT,fill=Y)

text_box = Text(frame,width=40,height=10,font=("Calibri",16),selectbackground="yellow",selectforeground="black",yscrollcommand=scroll_bar.set,undo=True)
text_box.pack()

scroll_bar.config(command=text_box.yview)

open_btn = Button(root,text="Open!",command=open_file)
open_btn.pack(pady=10)

save_btn = Button(root,text="Save!",command=save_file)
save_btn.pack(pady=10)

image_btn = Button(root,text="Add Image!",command=add_img)
image_btn.pack(pady=10)

select_btn = Button(root,text="Select!",command=select)
select_btn.pack(pady=10)

bold_btn = Button(root,text="Bold!",command=do_bold)
bold_btn.pack(pady=10)

italic_btn = Button(root,text="Italics!",command=do_italic)
italic_btn.pack(pady=10)

undo_btn = Button(root,text="Undo!",command=text_box.edit_undo)
undo_btn.pack(pady=10)

redo_btn = Button(root,text="Redo!",command=text_box.edit_redo)
redo_btn.pack(pady=10)

root.mainloop()