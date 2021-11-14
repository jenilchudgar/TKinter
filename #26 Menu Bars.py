from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# Functions
def newFile():
    print("New File")

def cut():
    print("Cut")

def copy():
    print("Copy")

def paste():
    print("Paste")

def test():
    pass

# Menu
menu = Menu(root)
root.config(menu=menu)

# Create a file menu item
file_menu = Menu(menu)
file_menu.add_command(label="New File",command=newFile)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)
menu.add_cascade(label="File",menu=file_menu)

# Create an Edit file menu item
edit_menu = Menu(menu)
edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_separator()
edit_menu.add_command(label="Paste",command=paste)
menu.add_cascade(label="Edit",menu=edit_menu)

# Create an Options file menu item
options_menu = Menu(menu)
options_menu.add_command(label="Op1",command=test)
options_menu.add_command(label="Op2",command=test)
menu.add_cascade(label="Options",menu=options_menu)

root.mainloop()