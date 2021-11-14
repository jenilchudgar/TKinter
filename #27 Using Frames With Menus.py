from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# Functions
def file_new():
    hideAllFrames()
    file_new_frame.pack(fill="both",expand=1)
    label = Label(file_new_frame,text="Clicked New!")
    label.pack()

def edit_cut():
    hideAllFrames()
    edit_cut_frame.pack(fill="both",expand=1)
    label = Label(edit_cut_frame,text="Clicked Cut!")
    label.pack()

def hideAllFrames():
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()

def test():
    pass

# Menu
menu = Menu(root)
root.config(menu=menu)

# Create a file menu item
file_menu = Menu(menu)
file_menu.add_command(label="New File",command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)
menu.add_cascade(label="File",menu=file_menu)

# Create an Edit file menu item
edit_menu = Menu(menu)
edit_menu.add_command(label="Cut",command=edit_cut)
edit_menu.add_command(label="Copy",command=test)
edit_menu.add_separator()
edit_menu.add_command(label="Paste",command=test)
menu.add_cascade(label="Edit",menu=edit_menu)

# Create an Options file menu item
options_menu = Menu(menu)
options_menu.add_command(label="Op1",command=test)
options_menu.add_command(label="Op2",command=test)
menu.add_cascade(label="Options",menu=options_menu)

# Create some frames
file_new_frame = Frame(root,width=400,height=400,bg="red")
edit_cut_frame = Frame(root,width=400,height=400,bg="blue")

root.mainloop()