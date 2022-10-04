from tkinter import *

splash_root = Tk()
splash_root.title("Splash Screen")

# Hide the title bar
splash_root.overrideredirect(True)

splash_root.geometry("300x200+500+200")

splash_lable = Label(splash_root,text="Splash Screen!",font=("Calibri",15))
splash_lable.pack(pady=10)

def main_window():
    splash_root.destroy()
    root = Tk()
    root.title("Python")
    root.iconbitmap("computer.ico")
    root.geometry("400x400")

splash_root.after(3000,main_window)

mainloop()