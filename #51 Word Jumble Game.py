from tkinter import *
from random import choice, shuffle

root = Tk()
root.title("Word Jumble Game")
root.iconbitmap("img/word.ico")
root.geometry("600x400")

states = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

correct_ans = ""
current_index = 0

def shuffle_states():
    result_label.config(fg="black",text="")

    global correct_ans
    # Choose a random state
    word = choice(states)

    # Store Correct Answer
    correct_ans = word
    
    # Change to list
    list_word = list(word)


    # Shuffle the letters
    shuffle(list_word)

    # List to str
    state_label.config(text="".join(list_word))

def answer():
    result_label.config(text=f"{correct_ans}")

def submit():
    user_ans = answer_box.get()

    color = ""

    if user_ans == correct_ans:
        result_label.config(text="Correct!")
        color = "green"

    else:
        result_label.config(text="Wrong!")
        color = "red"
    
    result_label.config(text=f"{result_label.cget('text')} Correct Answer was {correct_ans}.",fg=color)
    
    answer_box.delete(0,END)
    root.after(3000,shuffle_states)

def hint():
    global current_index

    if current_index < len(correct_ans):
        hint_label.config(text=f"{hint_label.cget('text')} {correct_ans[current_index]}")
        current_index+=1

state_label = Label(root,text="",font=("Calibri",25))
state_label.pack()

answer_box = Entry(root,font=("Calibri",18))
answer_box.pack(pady=20)

sumbit_btn = Button(root,text="Submit!",command=submit,font=("Calibri",12))
sumbit_btn.pack()

ans_btn = Button(root,text="Answer!",command=answer,font=("Calibri",12))
ans_btn.pack(pady=10)

hint_btn = Button(root,text="Hint!",command=hint,font=("Calibri",12))
hint_btn.pack(pady=10)

choose_btn = Button(root,text="Choose New Word!",command=shuffle_states,font=("Calibri",15))
choose_btn.pack(pady=10)

hint_label = Label(root,text="",font=("Calibri",18))
hint_label.pack()

result_label = Label(root,text="",font=("Calibri",18))
result_label.pack()

shuffle_states()

root.mainloop()