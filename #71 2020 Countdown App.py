from tkinter import *
from datetime import date

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

panic = Label(root,text="DON'T PANIC",font=("Calibri",40),bg="black",fg="green")
panic.pack(pady=20,ipady=5,ipadx=5)

today = date.today()

today_label = Label(root,text=today.strftime("%A - %B %d, %Y"),font=("Calibri",15))
today_label.pack(pady=20)

# Countdown
DAYS_IN_A_YEAR = 366 if int(today.strftime("%Y"))%4 == 0 else 365
DAY_TODAY = int(today.strftime("%j")) - 1
DAYS_LEFT = DAYS_IN_A_YEAR - DAY_TODAY 

output = Label(root,text=f"Days Left: {DAYS_LEFT}",font=("Calibri",20))
output.pack(pady=20)

root.mainloop()