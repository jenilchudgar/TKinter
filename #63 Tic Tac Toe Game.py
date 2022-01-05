from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe Game")
root.iconbitmap("computer.ico")

# Reset Game
def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,x_clicked,count
    # X starts so True
    x_clicked = True
    count = 0

    # Build Our Buttons
    b1 = Button(root,text=" ",font=("Calibri",20),height=4,width=12,bg="SystemButtonFace",command=lambda: btn_click(b1))
    b1.grid(row=0,column=0)

    b2 = Button(root,text=" ",font=("Calibri",20),height=4,width=12,bg="SystemButtonFace",command=lambda: btn_click(b2))
    b2.grid(row=0,column=1)

    b3 = Button(root,text=" ",font=("Calibri",20),height=4,width=12,bg="SystemButtonFace",command=lambda: btn_click(b3))
    b3.grid(row=0,column=2)

    b4 = Button(root,text=" ",font=("Calibri",20),height=4,width=12,bg="SystemButtonFace",command=lambda: btn_click(b4))
    b4.grid(row=1,column=0)

    b5 = Button(root,text=" ",font=("Calibri",20),height=4,width=12,bg="SystemButtonFace",command=lambda: btn_click(b5))
    b5.grid(row=1,column=1)

    b6 = Button(root,text=" ",font=("Calibri",20),height=4,width=12,bg="SystemButtonFace",command=lambda: btn_click(b6))
    b6.grid(row=1,column=2)

    b7 = Button(root,text=" ",font=("Calibri",20),height=4,width=12,bg="SystemButtonFace",command=lambda: btn_click(b7))
    b7.grid(row=2,column=0)

    b8 = Button(root,text=" ",font=("Calibri",20),height=4,width=12,bg="SystemButtonFace",command=lambda: btn_click(b8))
    b8.grid(row=2,column=1)

    b9 = Button(root,text=" ",font=("Calibri",20),height=4,width=12,bg="SystemButtonFace",command=lambda: btn_click(b9))
    b9.grid(row=2,column=2)

# Disable All Buttons
def disable_all_btn():
    b1["state"] = DISABLED
    b2["state"] = DISABLED
    b3["state"] = DISABLED
    b4["state"] = DISABLED
    b5["state"] = DISABLED
    b6["state"] = DISABLED
    b7["state"] = DISABLED
    b8["state"] = DISABLED
    b9["state"] = DISABLED
    
    reset() if messagebox.askyesno("Tic Tac Toe!","Reset Game?") else None

# Check to See if someone won
def check_winner():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","X Won!")
    
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","X Won!")
        disable_all_btn()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","X Won!")
        disable_all_btn()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","X Won!")
        disable_all_btn()
    
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","X Won!")
        disable_all_btn()
    
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b8.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","X Won!")
        disable_all_btn()
    
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","X Won!")
        disable_all_btn()
    
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","X Won!")
        disable_all_btn()

        
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","O Won!")
        disable_all_btn()
        disable_all_btn()
    
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","O Won!")
        disable_all_btn()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","O Won!")
        disable_all_btn()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","O Won!")
        disable_all_btn()
    
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","O Won!")
        disable_all_btn()
    
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","O Won!")
        disable_all_btn()
    
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","O Won!")
        disable_all_btn()
    
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")

        winner = True
        messagebox.showinfo("Tic Tac Toe","O Won!")
        disable_all_btn()

# Button Click Function
def btn_click(b):
    global x_clicked,count 

    if b["text"] == " ":
        b["text"] = "X" if x_clicked else "O"
        count += 1

        x_clicked = not x_clicked
        check_winner()
    else:
        messagebox.showerror("Tic Tac Toe","This box has already been selected. Please pick another box.")
    
    if count == 9 and winner == False:
        messagebox.showwarning("Tic Tac Toe","Game is Tie!")
        disable_all_btn()

reset()

# Create Menu
menu = Menu(root)
root.config(menu=menu)

# Create Options Menu
options_menu = Menu(menu,tearoff=False)
options_menu.add_command(label="Reset!",command=reset)

menu.add_cascade(label="Options",menu=options_menu)

root.mainloop()