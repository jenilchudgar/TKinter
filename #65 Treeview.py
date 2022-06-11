from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("500x500")

# Treeview Frame
tree_frame = Frame(root)
tree_frame.pack()

# Treeview Scrollbar
tree_scrollbar = Scrollbar(tree_frame)
tree_scrollbar.pack(side=RIGHT,fill=Y)

# Treeview
tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scrollbar.set,)

# Config Scrollbar
tree_scrollbar.config(command=tree.yview)

# Add Some Style
style = ttk.Style()

# Pick A Theame
style.theme_use("clam")
'''
style.configure(
        "Treeview",
        background="Yellow",
        foreground="Black",
        fieldbackground="Yellow"
    )

style.map("Treeview",
    background=[('selected','blue')]
)

'''

# Function
def clear_all():
    # Clear Boxes
    name_entry.delete(0,END)
    id_entry.delete(0,END)
    colour_entry.delete(0,END)

def add_record():
    global count
    count+=1
    r = "even" if count%2==0 else"odd"
    
    tree.insert(parent="",index=END,iid=count+1,text="",values=(
        value["name"],
        count+1,
        value["colour"]
    ),tags=(f"{r}row"))

    # Clear Boxes
    clear_all()

def remove_all():
    for i in tree.get_children():
        tree.delete(i)

def remove_sel():
    for e in tree.selection():
        tree.delete(e)

def sel_record():
    # Clear Boxes
    clear_all()
    
    # Grab record number
    selected = tree.focus()

    # Grab record values
    values = tree.item(selected,'values')

    # Ouput to Entry Boxes
    name_entry.insert(END,values[0])
    id_entry.insert(END,values[1])
    colour_entry.insert(END,values[2])

def update_record():
    # Grab record number
    selected = tree.focus()

    # Save new data
    tree.item(selected,text="",values=
        (name_entry.get(),
        id_entry.get(),
        colour_entry.get())
    ) 

    # Clear Boxes
    clear_all()

# Define our columns
tree['columns'] = ("Name","ID","Favourite Colour")

# Format our columns
tree.column("#0",width=0,stretch=NO)
tree.column("Name",anchor=W,width=120,minwidth=100)
tree.column("ID",anchor=CENTER,width=100,minwidth=100)
tree.column("Favourite Colour",anchor=W,width=140,minwidth=100)

# Headings
tree.heading("#0",text="",anchor=W)
tree.heading("Name",text="Name",anchor=W)
tree.heading("ID",text="ID",anchor=CENTER)
tree.heading("Favourite Colour",text="Favourite Colour",anchor=W)

# Add Data
data = [
    {
        "name":"John",
        "colour":"Red"
    },
    
    {
        "name":"Marry",
        "colour":"Blue"
    },
    {
        "name":"Jenil",
        "colour":"Yellow"
    },
    {
        "name":"John",
        "colour":"Red"
    },
    
    {
        "name":"Marry",
        "colour":"Blue"
    },
    {
        "name":"Jenil",
        "colour":"Yellow"
    },
    {
        "name":"John",
        "colour":"Red"
    },
    
    {
        "name":"Marry",
        "colour":"Blue"
    },
    {
        "name":"Jenil",
        "colour":"Yellow"
    },
    {
        "name":"Jenil",
        "colour":"Yellow"
    },
    {
        "name":"Jenil",
        "colour":"Yellow"
    },
]

# Tag
tree.tag_configure("evenrow",background="lightblue")
tree.tag_configure("oddrow",background="white")

global count
count = 0
r=""
for value in data:
    r = "even" if count%2==0 else"odd"
    
    tree.insert(parent="",index=END,iid=count+1,text="",values=(
        value["name"],
        count+1,
        value["colour"]
    ),tags=(f"{r}row"))
    count+=1

# Add Child
# tree.insert(parent="",index=END,iid=10,text="Child",values=(
#         "Child",
#         1.2,
#         "Yellow"
#     ))

# tree.move(10,"1","1")

# Pack Values
tree.pack()

# Frame for Controls
add_frame = Frame(root)
add_frame.pack(pady=10)

# Labels
name = Label(add_frame,text="Name")
name.grid(row=0,column=0)

id = Label(add_frame,text="ID")
id.grid(row=0,column=1)

colour = Label(add_frame,text="Favourite Colour")
colour.grid(row=0,column=2)

# Entrys
name_entry = Entry(add_frame)
name_entry.grid(row=1,column=0,padx=10)

id_entry = Entry(add_frame)
id_entry.grid(row=1,column=1,padx=10)

colour_entry = Entry(add_frame)
colour_entry.grid(row=1,column=2,padx=10)

# Buttons
add_btn = Button(root,text="Add Record",command=add_record)
add_btn.pack()

add_btn = Button(root,text="Select Record",command=sel_record)
add_btn.pack()

add_btn = Button(root,text="Update Record",command=update_record)
add_btn.pack()

remove_all_btn = Button(root,text="Remove All Records",command=remove_all)
remove_all_btn.pack()

remove_selected_btn = Button(root,text="Remove Selected Record(s)",command=remove_sel)
remove_selected_btn.pack()

root.mainloop()