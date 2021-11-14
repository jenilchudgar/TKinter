from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\computer.ico")
root.geometry("400x400")

class Jenil:
    def __init__(self,master) -> None:
        frame = Frame(master)
        frame.pack()

        self.btn = Button(master,text="Click Me!",command=self.click)
        self.btn.pack()

    def click(self):
        print("You clicked a button!")

boy = Jenil(root)
root.mainloop()