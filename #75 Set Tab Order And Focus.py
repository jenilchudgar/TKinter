from tkinter import *
root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

orange = Entry(root,bg="orange")
orange.pack(pady=10)
white = Entry(root,bg="white")
white.pack(pady=10)
green = Entry(root,bg="green")
green.pack(pady=10)

# Pick Focus
orange.focus()

# Change Tab Order
# Change how we define it in the order
def tab_order():
    widgets = [green,orange,white]
    for w in widgets:
        w.lift()

my_btn = Button(root,text="Change Tab Order",command=tab_order)
my_btn.pack(pady=10)
root.mainloop()