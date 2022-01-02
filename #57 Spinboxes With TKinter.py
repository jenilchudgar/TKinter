from tkinter import *
root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# Numbers
# spin_box = Spinbox(root,from_=0,to=100,font=('Calibri',20),increment=2)
# spin_box.pack(pady=20)

def grab_item():
    my_label.config(text=spin_box.get())

names = ("Jenil","John","Tina")
spin_box = Spinbox(root,values=names,font=('Calibri',20))
spin_box.pack(pady=20)

my_btn = Button(root,text="Pick!",command=grab_item,font=('Calibri',15))
my_btn.pack(pady=20)

my_label = Label(root,text="",font=("Calibri",15))
my_label.pack(pady=10)

root.mainloop()