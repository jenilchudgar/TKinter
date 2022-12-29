from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# error
# gray75
# gray50
# gray12
# hourglass
# info
# questhead
# question
# warning

bitmap_btn = Button(root,bitmap="error",width=50,height=50)
bitmap_btn.pack(pady=10)

root.mainloop()