from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

bitmap_btn = Button(root,bitmap="error",width=50,height=50)
bitmap_btn.pack(pady=10)



root.mainloop()