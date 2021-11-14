from tkinter import *
root = Tk()
root.title("Calculator")

def click(val):
    inputField.insert(END,str(val))
def clear():
    inputField.delete(0,END)
def equals():
    exp = inputField.get().replace("÷","/").replace("X","*")
    clear()
    inputField.insert(0,str(eval(exp)))
def backspace():
    val = inputField.get()[0:-1]
    clear()
    inputField.insert(0,val)

inputField=Entry(root,width=30,borderwidth=10)
inputField.grid(row=0,column=0,columnspan=3,padx=20,pady=20)

button_backSpace = Button(root,text="⌫",padx=15,pady=15,command=lambda:backspace()).grid(row=6,column=2)
button_0 = Button(root,text="0",padx=20,pady=20,command=lambda:click("0")).grid(row=6,column=1)
button_equals = Button(root,text="=",padx=20,pady=20,command=lambda:equals()).grid(row=6,column=0)
button_1 = Button(root,text="1",padx=20,pady=20,command=lambda:click("1")).grid(row=5,column=2)
button_2 = Button(root,text="2",padx=20,pady=20,command=lambda:click("2")).grid(row=5,column=1)
button_3 = Button(root,text="3",padx=20,pady=20,command=lambda:click("3")).grid(row=5,column=0)
button_4 = Button(root,text="4",padx=20,pady=20,command=lambda:click("4")).grid(row=4,column=2)
button_5 = Button(root,text="5",padx=20,pady=20,command=lambda:click("5")).grid(row=4,column=1)
button_6 = Button(root,text="6",padx=20,pady=20,command=lambda:click("6")).grid(row=4,column=0)
button_7 = Button(root,text="7",padx=20,pady=20,command=lambda:click("7")).grid(row=3,column=2)
button_8 = Button(root,text="8",padx=20,pady=20,command=lambda:click("8")).grid(row=3,column=1)
button_9 = Button(root,text="9",padx=20,pady=20,command=lambda:click("9")).grid(row=3,column=0)
button_dot = Button(root,text=".",padx=20,pady=20,command=lambda:click(".")).grid(row=2,column=2)
button_clear = Button(root,text="C",padx=20,pady=20,command=lambda:clear()).grid(row=2,column=1)
button_div = Button(root,text="÷",padx=20,pady=20,command=lambda:click("÷")).grid(row=2,column=0)
button_mul = Button(root,text="X",padx=20,pady=20,command=lambda:click("X")).grid(row=1,column=2)
button_minus = Button(root,text="-",padx=20,pady=20,command=lambda:click("-")).grid(row=1,column=1)
button_add = Button(root,text="+",padx=20,pady=20,command=lambda:click("+")).grid(row=1,column=0)

root.mainloop()