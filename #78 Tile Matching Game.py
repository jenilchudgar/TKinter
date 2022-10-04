from tkinter import messagebox
from tkinter import *
import random

root = Tk()
root.title("Tile Matching Game")
root.iconbitmap("computer.ico")
root.geometry("720x432")

# Variables
global count,ans_list,ans_dict,btns,winner

count = 0
ans_list = []
ans_dict = {}
btns = []
START = 1
END = 6
matches = []
winner = 0

# Create our matches
for i in range(START,END+(1)):
    for j in range(START,3):
        matches.append(i) 

# Shuffle The Buttons
random.shuffle(matches)

# Function: Create a Right Click Menu
def menu_popup(e):
    menu.tk_popup(e.x_root,e.y_root)

# Function: Reset the Game
def reset():
	global matches, winner
	winner = 0
	# Create our matches
	matches = [1,1,2,2,3,3,4,4,5,5,6,6]
	# Shuffle our matches
	random.shuffle(matches)

	# Reset our Tiles
	for button in btns:
		button.config(text=" ", bg="cyan", state="normal")

# Function: Runs When The User Wins
def win():
    global btns
    messagebox.showinfo("You Won!","Congrats, you Won!")
    # Loop Through Buttons And CHange Their Colors
    for btn in btns:
        btn.config(bg="lightgreen")

# Function: Runs When A Button Is Clicked
def button_click(btn,i):
    # print(matches)
    global count,ans_list,ans_dict,winner

    if btn["text"] == " " and count < 2:
        btn["text"] = matches[i]
        
        # Add Number To Answer List
        ans_list.append(i)

        # Add Button and Number to Answer Dictionary
        ans_dict[btn] = matches[i]

        # Increment The Count Variable
        count+=1

        # Evaluate Correct Or Wrong
        if len(ans_list) == 2:
            if matches[ans_list[0]] == matches[ans_list[1]]:
                print("Matched!")
                winner+=1
                for key in ans_dict.keys():
                    key["state"] = DISABLED
                ans_dict.clear()

                if winner == END:
                    win()
                    
                    # Ask To Reset The Game
                    if messagebox.askyesno("Reset The Game","Would you like to reset the game?"):
                        reset()

            else:
                messagebox.showwarning("Incorrect Match","The Match selected by you is incorrect!")
                for key in ans_dict.keys():
                    key["text"] = " "
                
            # Reset
            count = 0
            ans_list.clear()
            ans_dict.clear()
                
# Create Buttons
for i in range(START-1,(END*2)):
    btns.append(Button(root,font=("Calibri",50),width=5,text=" ",bg="cyan",relief=GROOVE))
    if i>=0 and i<=3:
        btns[i].grid(row=0,column=i)
    elif i>=4 and i<=7:
        btns[i].grid(row=1,column=i-4)
    if i>=8 and i<=11:
        btns[i].grid(row=2,column=i-8)


btns[0].config(command=lambda: button_click(btns[0],0))
btns[1].config(command=lambda: button_click(btns[1],1))
btns[2].config(command=lambda: button_click(btns[2],2))
btns[3].config(command=lambda: button_click(btns[3],3))
btns[4].config(command=lambda: button_click(btns[4],4))
btns[5].config(command=lambda: button_click(btns[5],5))
btns[6].config(command=lambda: button_click(btns[6],6))
btns[7].config(command=lambda: button_click(btns[7],7))
btns[8].config(command=lambda: button_click(btns[8],8))
btns[9].config(command=lambda: button_click(btns[9],9))
btns[10].config(command=lambda: button_click(btns[10],10))
btns[11].config(command=lambda: button_click(btns[11],11))

# Creating A Menu
menu = Menu(root,tearoff=False)
menu.add_command(label="Reset",command=reset)
menu.add_separator()
menu.add_command(label="Exit!",command=root.quit)

# Bind
root.bind("<Button-3>",menu_popup)

root.mainloop()