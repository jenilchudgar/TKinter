from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

def clicker():
    global pop
    pop = Toplevel(root)
    pop.title("My Title")
    pop.geometry("200x150")
    pop.config(bg="yellow")

    frame = Frame(pop,bg="yellow")
    frame.pack()

    global img
    img = PhotoImage("img\button.png")
    img_label = Label(frame,image=img,font=("Calibri",15))
    img_label.grid(row=0,column=0,padx=10)

    def yes():
        print("Yes")

    def no():
        print("No")
    
    yes_btn = Button(frame,text="Yes",command=yes)
    yes_btn.grid(row=0,column=1)

    no_btn = Button(frame,text="No",command=no)
    no_btn.grid(row=0,column=2)

    label = Label(pop,text="Would like to die?",font=("Pacifico",12),fg="red")
    label.pack(pady=20)
    

my_btn = Button(root,text="Click Me",command=clicker)
my_btn.pack(pady=50)        

root.mainloop()