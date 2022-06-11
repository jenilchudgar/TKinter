from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Menu Items
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)

def new():
    pass

def open_file():
    pass

# Add File Menu Items
file_menu.add_command(label="New",command=new)
file_menu.add_command(label="Open",command=open_file)

# Disable Button
def disable_btn_func():
    file_menu.entryconfig("New",state=DISABLED)

disable_btn = Button(root,text="Disable New",command=disable_btn_func)
disable_btn.pack(pady=10)

# Enable Button
def enable_btn_func():
    file_menu.entryconfig("New",state=NORMAL)

enable_btn = Button(root,text="Enable New",command=enable_btn_func)
enable_btn.pack(pady=10)

root.mainloop()