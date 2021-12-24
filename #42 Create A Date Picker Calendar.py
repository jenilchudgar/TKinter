from tkinter import *
from tkcalendar import *
from datetime import datetime as dt
import datetime

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

year = int(dt.now().strftime("%y"))
month = int(dt.now().strftime("%m"))
day = int(dt.now().strftime("%d"))

cal = Calendar(root,selectmode="day",year=year,day=day)
cal.pack(pady=10)

def get_date():
    date.config(text=datetime.datetime.strptime(cal.get_date(), "%m/%d/%y").date().strftime("%B %d, %Y"))

btn = Button(root,text="Get Date!",command=get_date)
btn.pack(pady=20)

date = Label(root,text="",font=("Calibri",20))
date.pack(pady=10)

root.mainloop()