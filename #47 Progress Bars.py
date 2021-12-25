from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

progress_bar = ttk.Progressbar(root,orient=HORIZONTAL,length=300,mode="determinate")
progress_bar.pack(pady=20)

def step():
    # progress_bar.start[3)
    for i in range(10):
        progress_bar['value'] += 10
        root.update_idletasks()
        label.config(text=f"{progress_bar['value']}")
        time.sleep(1)

step_btn = Button(root,text="Step!",command=step)
step_btn.pack(pady=20)

def stop():
    progress_bar.stop()

stop_btn_btn = Button(root,text="Stop!",command=stop)
stop_btn_btn.pack()

label = Label(root,text="")
label.pack(pady=10)

root.mainloop()