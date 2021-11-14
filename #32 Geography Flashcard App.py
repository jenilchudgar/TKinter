from tkinter import *
from random import *
from PIL import ImageTk,Image
import os

root = Tk()
root.title("Geography Flashcard App")
root.iconbitmap("computer.ico")
root.geometry("500x600")
states = [e.replace(".png","") for e in os.listdir("states")]

# Create Funtions
def random_state():
    global state_img,randNo,states
    # Generate a random number
    if len(states) >=1:
        randNo = randint(0,len(states)-1)
        # Create our State Images
        global state
        state = states[randNo]
        state_img = (Image.open(f'states/{state}.png'))
        state_img = state_img.resize((350,300),Image.ANTIALIAS)
        state_img = ImageTk.PhotoImage(state_img)
        img.config(image=state_img)
        states.remove(state)
    else:
        for e in root.winfo_children():
            e.pack_forget()

        l = Label(root,text=f"Game Over!\nScore: {score}",font=('Calibri',50),fg="blue")
        l.place(relx=0.5, rely=0.5, anchor=CENTER)
        return False

def statesF():
    # Hide All Previous Frames
    hideAllFrames()
    state_frame.pack(fill=BOTH,expand=1)

    # Create Score Variable
    global score
    score = 0

    global img
    img = Label(state_frame)
    img.pack()
    if not random_state():
        # Create next Button
        btn = Button(state_frame,text="Pass",command=statesF,font=('Calibri',16))
        btn.pack(pady=10,padx=10)

        # Create Answer Input
        global answer_input
        answer_input = Entry(state_frame,font=('Calibri',18))
        answer_input.pack(pady=15,padx=10)

        # Create a Button to submit Answer
        submit_btn = Button(state_frame,text="Answer",font=('Calibri',15),command=state_answer)
        submit_btn.pack(pady=10)

        # Create Status Label
        global status_label
        status_label = Label(state_frame,text="",font=('Calibri',16))
        status_label.pack()

        global score_label
        score_label = Label(state_frame,text="",font=('Calibri',15))
        score_label.pack()
    else:
        return

def state_answer():
    global score,score_label
    color = ""
    respone = ""
    if answer_input.get().lower() == state.replace("_"," ").lower():
        respone=f"Correct! The state is {state.title().replace('_',' ')}."
        color="blue"
        score += 1
    else:
        respone=f"Sorry your answer is incorrect!\nThe Correct answer was {state.title().replace('_',' ')}."
        color="red"

    # Display Score
    score_label.config(
        text=f"Score: {score}"   
    )

    # Display Message/Respone
    status_label.config(
        text=respone,
        fg=color
    )
    # Clear Answer Box
    answer_input.delete(0,END)

    # Show Next Image
    random_state()
 
def add():
    hideAllFrames()
    addition_frame.pack(fill=BOTH,expand=1)
    Label(addition_frame,text="Math Mix Game",font=('Calibri',20),fg="blue").pack()
    pic_frame = Frame(addition_frame,width=400,height=200)
    pic_frame.pack()

    # Signs
    signs = ['+','-','x','÷']

    # Genarate a random number
    num_1 = randint(1,100)
    num_2 = randint(1,100)
    num_3 = randint(1,100)
    sign_num1 = randint(0,len(signs)-1)
    sign_num2 = randint(0,len(signs)-1)

    # Create 3 Labels in pic_frame
    global add_1,add_2,add_3,math_sign1,math_sign2

    add_1 = Label(pic_frame,font=('Calibri',18))
    add_2 = Label(pic_frame,font=('Calibri',18))
    add_3 = Label(pic_frame,font=('Calibri',18))
    math_sign1 = Label(pic_frame,font=('Calibri',18))
    math_sign2 = Label(pic_frame,font=('Calibri',18))

    # Grid our labels
    add_1.grid(row=0,column=0)
    math_sign1.grid(row=0,column=1)
    add_2.grid(row=0,column=2)
    math_sign2.grid(row=0,column=3)
    add_3.grid(row=0,column=4)
    
    add_1.config(text=num_1)
    add_2.config(text=num_2)
    add_3.config(text=num_3)

    math_sign1.config(text=signs[sign_num1])
    math_sign2.config(text=signs[sign_num2])

    global answer_field
    answer_field = Entry(addition_frame,font=('Calibri','18'))
    answer_field.pack(padx=20,pady=10)

    submit_btn = Button(addition_frame,text="Submit!",font=('Calibri','18'),command=answer_math)
    submit_btn.pack()

def answer_math():
    n1 = add_1.cget("text")
    n2 = add_2.cget("text")
    n3 = add_3.cget("text")

    s1 = math_sign1.cget("text")
    s2 = math_sign2.cget("text")

    answer = eval(
        f"{n1} {s1} {n2} {s2} {n3}"
        .replace("x","*")
        .replace("÷","/")
    )

    # global answer_field
    # print(answer)
    if float(answer_field.get()) == float(answer):
        ans = Label(addition_frame,text="Correct! Your answer is right",font=('Calibri',20),fg="blue")
    else:
        ans = Label(addition_frame,text=f"Wrong! Correct Answer: {answer}",font=('Calibri',20),fg="red")
    ans.after(2000,add)

def hideAllFrames():
    state_frame.pack_forget()
    state_capitals_frame.pack_forget()
    addition_frame.pack_forget()

    for e in state_frame.winfo_children():
        e.destroy()

    for e in addition_frame.winfo_children():
        e.destroy()

    for e in state_capitals_frame.winfo_children():
        e.destroy()

# Create Our Menu
menu = Menu(root)
root.config(menu=menu)

# Create Menu Items

# 1. Geography Menu
states_menu = Menu(menu)
menu.add_cascade(label="Geography",menu=states_menu) 
states_menu.add_command(label="States",command=statesF)

math_menu = Menu(menu)
menu.add_cascade(label="Maths",menu=math_menu) 
math_menu.add_command(label="Mix Game",command=add)

# 2. Controls Menu
controls_menu = Menu(menu)
menu.add_cascade(label="Controls",menu=controls_menu) 
controls_menu.add_command(label="Exit",command=root.quit)

# Create Frames
state_frame = Frame(root,width=500,height=500)
addition_frame = Frame(root,width=500,height=500)
state_capitals_frame = Frame(root,width=500,height=500)

root.mainloop()