from tkinter import *
from random import randint

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

num_label = Label(root,text="Pick A Number From 1-10",font=("Calibri",20))
num_label.pack(pady=10)

def guess_num():
    global num
    x = guess_entry.get()
    if x.isdigit():
        # Reset The Label
        num_label.config(text="Pick A Number From 1-10")
        
        # Find How Far Away Our Pick Was
        diff = abs(num - int(x))

        bc = "yellow"

        # Check to see if correct
        if int(x) == num:
            num_label.config(text="Correct!")
        elif diff == 5:
            # White
            bc = "white"
        elif diff < 5:
            # Red
            bc = f"#ff0{diff}{diff}{diff}"
        elif diff > 5:
            # Blue
            bc = f"#{diff}{diff}{diff}{diff}ff"
        root.config(bg = bc)
        num_label.config(bg = bc)

    else:
        # Throw Error
        num_label.config(text="HEY! THAT IS NOT A NUMBER!")
        # Clear Guess Box
        guess_entry.delete(0,END)

def reset():
    global num
    num = randint(1,10)
    # Clear Guess Box
    guess_entry.delete(0,END)

guess_entry = Entry(root,font=("Calibri",100),width=2)
guess_entry.pack(pady=10)

guess_btn = Button(root,text="Guess!",command=guess_num)
guess_btn.pack(pady=10)

reset_btn = Button(root,text="Reset!",command=reset)
reset_btn.pack(pady=10)

# Generate Random Number
reset()

root.mainloop()