from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

def hide(id):
    tabs.hide(id)

def show(id):
    if id==0:
        tabs.add(frame1,text="Yellow Tab")
    else:
        tabs.add(frame2,text="Red Tab")

def navigate(id):
    tabs.select(id)

# Tabs
tabs = ttk.Notebook(root)
tabs.pack()

# Frame
frame1 = Frame(tabs,bg="Yellow",width=500,height=500)
frame2 = Frame(tabs,bg="red",width=500,height=500)

frame1.pack(fill=BOTH,expand=1)
frame2.pack(fill=BOTH,expand=1)

# Add Text to Frames
tabs.add(frame1,text="Yellow Tab")
tabs.add(frame2,text="Red Tab")

# Buttons
btn_hide2 = Button(frame1,text="Hide tab 2",command=lambda: hide(1))
btn_hide2.pack(pady=10)

btn_show2 = Button(frame1,text="Show tab 2",command=lambda: show(1))
btn_show2.pack(pady=10)

btn_navigate_to_tab2 = Button(frame1,text="Navigate to tab 2",command=lambda: navigate(1))
btn_navigate_to_tab2.pack(pady=10)


btn_hide2 = Button(frame2,text="Hide tab 1",command=lambda: hide(0))
btn_hide2.pack(pady=10)

btn_show1 = Button(frame2,text="Show tab 1",command=lambda: show(0))
btn_show1.pack(pady=10)

btn_navigate_to_tab1 = Button(frame2,text="Navigate to tab 1",command=lambda: navigate(0))
btn_navigate_to_tab1.pack(pady=10)


root.mainloop()