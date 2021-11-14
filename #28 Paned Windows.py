from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# Panels
panel1 = PanedWindow(bd=4,bg="red")
panel1.pack(fill=BOTH,expand=1)

left_label = Label(panel1,text="Left Panel")
panel1.add(left_label)

# Second Panel
panel2 = PanedWindow(panel1,bd=4,bg="blue",orient=VERTICAL)
panel1.add(panel2)

# Top
top = Label(panel2,text="Top Panel")
panel2.add(top)

# Bottom
bottom = Label(panel2,text="Bottom Panel")
panel2.add(bottom)

root.mainloop()