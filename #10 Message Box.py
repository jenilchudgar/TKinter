from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

root = Tk()
root.title("TKinter in Python: Message Box")
root.iconbitmap("computer.ico")

def click():
    # messagebox.showinfo("Message Box","Hello User!")
    # messagebox.showwarning("Message Box","Warning!")
    # messagebox.showerror("Message Box","Error!")
    ans = messagebox.askquestion("Message Box","Is Codemy.com the best?")   
    if (ans=="yes"):
        Label(root,text="Nice! :)",fg="blue").pack()
    else:
        Label(root,text="Bad! ):",fg="red").pack() 
    # messagebox.askokcancel("Message Box","Installing File!")    
    # ans = messagebox.askyesno("Message Box","You are kind!") 
    # if (ans):
    #     Label(root,text="Nice! :)",fg="blue").pack()
    # else:
    #     Label(root,text="Bad! ):",fg="red").pack()



button = Button(root,text="Click Me!",command=click).pack()

root.mainloop()