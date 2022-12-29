from pickle import dump, load
from tkinter import *
from tkinter.font import Font
from tkinter.filedialog import asksaveasfilename,askopenfilename
from tkinter.messagebox import showinfo

root = Tk()
root.title("To-Do List")
root.iconbitmap("computer.ico")
root.geometry("500x500")

# Functions: Buttons
def add_item():
    # Get Item From Entry
    item = entry.get()
    # Insert it in the ListBox
    list_box.insert(END,item)

    # Delete the item from Entry
    entry.delete(0,END)

def delete_item():
    # Delete Item
    list_box.delete(ANCHOR)

def cross_item():
    # Cross Off Item
    list_box.itemconfig(
        list_box.curselection(),
        fg="#969696",   
    )
    # Get Rid of Selection 
    list_box.select_clear(0,END)
    
def uncross_item():
    # Uncross Item
    list_box.itemconfig(
        list_box.curselection(),
        fg="BLACK",
    )
    # Get Rid of Selection 
    list_box.select_clear(0,END)

def delete_crossed_item():
    counter = 0
    while counter < list_box.size():
        if list_box.itemcget(counter,"fg") == "#969696":
            list_box.delete(list_box.index(counter))
        else:
            counter+=1

# Functions: Menu
def open_list():
    f_name = askopenfilename(
        title="Open File",
        filetypes=(
            ("Dat Files","*.dat"),
            ("All Files","*.*")
        ),
    )
    if f_name:
        # Delete Current List
        clear_list()

        # Open The File
        input_file = open(f_name,"rb")

        # Load data
        data = load(input_file)

        for item in data:
            list_box.insert(END,item)

    root.title(f"To-Do List - {f_name.split('/')[-1]}")

def save_list():
    f_name = asksaveasfilename(
        title="Save File",
        filetypes=(
            ("Dat Files","*.dat"),
            ("All Files","*.*")
        ),
    )
    if f_name:
        if not f_name.endswith(".dat"):
            f_name = f_name + ".dat"

    delete_crossed_item()

    # Grab All the data from The Listbox
    data = list_box.get(0,END)

    # Open The File
    output_file = open(f_name,"wb")

    # Add the Data
    dump(data,output_file)

    # Message Conformation
    showinfo(
        title="File Saved!",
        message=f"Your file {f_name.split('/')[-1]} has been saved!"
    )

    root.title(f"To-Do List - {f_name.split('/')[-1]}")

def clear_list():
    list_box.delete(0,END)

# Define Our Font
font = Font(
    family="Pacifico",
    size=25,
    weight=NORMAL
)

# Create Frame
frame = Frame(root)
frame.pack(pady=20)

# Create Listbox
list_box = Listbox(
    frame,
    font=font,
    width=20,
    height=5,
    bg="SystemButtonFace",
    bd=0,
    fg="BLACK",
    highlightthickness=0,
    selectbackground="CYAN",
    activestyle=NONE,
    selectforeground="DARK BLUE"
)
list_box.pack(side=LEFT)

# Create Scrollbar
scroll_bar = Scrollbar(frame)
scroll_bar.pack(side=RIGHT,fill=BOTH)

# Add Scrollbar
list_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)

# Create Entry Box
entry = Entry(
    root,font=(
        "Calibri",
        15
    ),
    width=30
)
entry.pack(pady=10)

# Create A Button Frame
btn_frame = LabelFrame(root,text="Controls")
btn_frame.pack(pady=10)

# Add Buttons

add_btn = Button(btn_frame,text="Add!",command=add_item)
add_btn.grid(row=0,column=1,padx=20)

del_btn = Button(btn_frame,text="Delete!",command=delete_item)
del_btn.grid(row=0,column=0,padx=20)

cross_btn = Button(btn_frame,text="Cross!",command=cross_item)
cross_btn.grid(row=0,column=2,padx=20) 

uncross_btn = Button(btn_frame,text="Uncross!",command=uncross_item)
uncross_btn.grid(row=0,column=3,padx=20) 

del_crossed_btn = Button(btn_frame,text="Delete Crossed!",command=delete_crossed_item)
del_crossed_btn.grid(row=0,column=4,padx=20) 

# Create A Menu
menu = Menu(root)
root.config(menu=menu)

# Add Items to The Menu
file_menu = Menu(menu,tearoff=False)
menu.add_cascade(menu=file_menu,label="File")

file_menu.add_command(label="Open",command=open_list)
file_menu.add_command(label="Save",command=save_list)
file_menu.add_separator()
file_menu.add_command(label="Clear",command=clear_list)

root.mainloop()
