from tkinter import *
from tkinter import messagebox
from random import randint

root = Tk()
root.title("Python")
root.iconbitmap("spanish.ico")
root.geometry("600x400")

global score
score = 0

words = [
    (("Hola"), ("Hello")),
    (("Adios"), ("Goodbye")),
    (("Gracias"), ("Thank you")),
    (("Por favor"), ("Please")),
    (("Si"), ("Yes")),
    (("Amigo"), ("Friend")),
    (("Casa"), ("House")),
    (("Agua"), ("Water")),
    (("Bueno"), ("Good")),
    (("Aeropuerto"), ("Airport")),
    (("Baño"), ("Bathroom")),
    (("Camisa"), ("Shirt")),
    (("Abrigo"), ("Coat")),
]

def next():
    # Generate Random Number
    no = randint(0,len(words)-1)
    global rand_word,hinter,hint_count
    rand_word = words[no]

    # Update Label
    spanish_word.config(text=rand_word[0])

    hinter = ""
    hint_count = 0
    hint_label.config(text="")


def answer():
    global score
    if entry.get().upper() == rand_word[1].upper():
        messagebox.showinfo("Correct!", "¡Hurra! You are correct!") 
        score+=1
    else:
        messagebox.showerror("Incorrect!", f"Lo siento! You are incorrect! The correct answer is '{rand_word[1]}'") 
        score-=1
    
    next()
    entry.delete(0,END)

# Keep track of the Hint
hinter = ""
hint_count = 0
def hint():
    global hint_count,hinter,no_hints

    if hint_count<len(rand_word[1]):
        hinter = hinter + rand_word[1][hint_count]
        hint_label.config(text=hinter)

        hint_count+=1
    else:
        messagebox.showwarning("Hints","Full Word has been Shown!")


heading = Label(root,text="Spanish Language App",font=("Pacifico",20))
heading.pack()

spanish_word = Label(root,text="",font=("Calibri",30))
spanish_word.pack(pady=30)

entry = Entry(root,font=("Calibri",16))
entry.pack(pady=20)

btn_frame = Frame(root)
btn_frame.pack(pady=5)

ans_btn = Button(btn_frame,text="Answer!",command=answer)
ans_btn.grid(row=0,column=0,padx=10)

next_btn = Button(btn_frame,text="Next",command=next)
next_btn.grid(row=0,column=1)

hint_btn = Button(btn_frame,text="Hint",command=hint)
hint_btn.grid(row=0,column=2,padx=10)

hint_label = Label(root,text="",font=("Calibri",16))
hint_label.pack()

next()

root.mainloop()