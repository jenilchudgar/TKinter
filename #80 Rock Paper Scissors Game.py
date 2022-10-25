from tkinter import *
from tkinter import ttk
from random import randint

root = Tk()
root.title("Rock Paper Scissors Game")
root.iconbitmap("computer.ico")
root.geometry("500x600")

# Function: Runs when the spin button is clicked
def spin():
    # Choose Computer Reply
    comp_no = randint(0,2)
    image_label.config(image=imgs[comp_no])

    # 0 = Rock
    # 1 = Paper
    # 2 = Scissors

    # Defining User Choice Value
    user_choice_val  = -1

    # Convert Dropdown choice to a number
    if user_choice.get() == "Rock":
        user_choice_val = 0
    elif user_choice.get() == "Paper":
        user_choice_val = 1
    elif user_choice.get() == "Scissors":
        user_choice_val = 2
    
    # Result
    won_str = []
    draw = False
    if user_choice_val == 0:
        if comp_no == 1:
            won_str.append(("Alas! You Lost! Paper trapped your Rock.","Red"))
        elif comp_no == 2:
            won_str.append(("Bravo! You Won! You destroyed the Scissor.","Green"))
    elif user_choice_val == 1:
        if comp_no == 0:
            won_str.append(("Bravo! You Won! You trapped the Paper with your Rock.","Green"))
        elif comp_no == 2:
            won_str.append(("Alas! You Lost! Your paper was cut.","Green"))
    elif user_choice_val == 2:
        if comp_no == 0:
            won_str.append(("Alas! You Lost! Rock destroyed your scissor.","Red"))
        elif comp_no == 1:
            won_str.append(("Bravo! You Won! You the cut the paper.","Green"))
    
    # Check for Draw
    if user_choice_val == comp_no:
        won_str.append(("Oh! It's a Draw!","Blue"))
    
    res.config(text=won_str[0][0],fg=won_str[0][1])

# Change Background Color To White
root.config(bg="White")

# Define Images
rock = PhotoImage(file="img/rock.png")
paper = PhotoImage(file="img/paper.png")
scissor = PhotoImage(file="img/scissors.png")

# Add Images to List
imgs = [rock,paper,scissor]

# Pick Random number between 0 and 2
no = randint(0,2)

# Show An Image
image_label = Label(root,image=imgs[no],font=("Calibri",15),relief=GROOVE)
image_label.pack(pady=10)

# Make Our Choice
user_choice = ttk.Combobox(root,value=(
    "Rock",
    "Paper",
    "Scissors"
    ),
)
user_choice.current(0)
user_choice.pack(pady=(10,0))

# Create a Spin Button
spin_btn = Button(root,text="Spin!",command=spin)
spin_btn.pack(pady=(10,0))

# Result Label
res = Label(root,text="",font=("Calibri",15))
res.pack(pady=(30,0))

root.mainloop()