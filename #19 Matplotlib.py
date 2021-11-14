import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("Python")
root.iconbitmap("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\computer.ico")
root.geometry("400x400")

def graph():
    housePrice = np.random.normal(200000,25000,5000)
    plt.bar()
    plt.show()

btn = Button(root,text="Click Me!",command=graph)
btn.pack()
root.mainloop()