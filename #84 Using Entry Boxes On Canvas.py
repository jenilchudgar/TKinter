from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x700")
root.resizable(width=False,height=False)

def entry_clear(e):
    if us_entry.get() == 'Username' or pw_entry.get() == "Password":
        us_entry.config(fg="blue")
        pw_entry.config(fg="blue")
        us_entry.delete(0,END)
        pw_entry.delete(0,END)

        pw_entry.config(show="*")

def login():
    if us_entry.get() == 'jenilchudgar@cbi.in' or pw_entry.get() == "123":
        for w in root.winfo_children():
            w.destroy()
        label1 = Label(root,text="Hello! Welcome Officer!",font=("Calibri",15))
        label1.pack(pady=50)
    else:
        for i in range(1,6):
            print("Erorr!!")

# Define BG Image
bg = PhotoImage(file="img/login.png")

# Define Canvas
canvas = Canvas(root,width=400,height=700,highlightthickness=0)
canvas.pack(fill=BOTH,expand=FALSE)

canvas.create_image(0,0,image=bg,anchor=NW)

us_entry = Entry(root,font=("Calibri",20),width=15,fg="grey",bg="cyan",relief=SUNKEN)
pw_entry = Entry(root,font=("Calibri",20),width=15,fg="grey",bg="cyan",relief=SUNKEN)

us_entry.insert(0,"Username")
pw_entry.insert(0,"Password")



# Add Entry to Canvas
us_win = canvas.create_window(80,290,anchor=NW,window=us_entry)
pw_win = canvas.create_window(80,370,anchor=NW,window=pw_entry)

# Add Login Btn


login_btn = Button(root,text="Login!",command=login,width=15,bg="yellow")
login_btn.pack(pady=10)

login_btn_win = canvas.create_window(120,500,anchor=NW,window=login_btn)

us_entry.bind("<Button-1>",entry_clear)
pw_entry.bind("<Button-1>",entry_clear)

root.mainloop()