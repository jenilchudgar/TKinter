from tkinter import *
from tkinter import ttk,messagebox,colorchooser
import sqlite3

root = Tk()
root.title("CRM Tool With Treeview And Database")
root.iconbitmap("data.ico")
root.geometry("1000x600")

# Columns
columns = ("ID","Name","Order Number","Cost of Order (INR ₹)","Address","City","State","Pincode")
extra = ("name","order_no","cost","address","city","state","pincode")

d = {}
for i in range(len(extra)):
    d[columns[i+1]] = extra[i]

# Add Menu
menu = Menu(root)
root.config(menu=menu)

primary_color = '#FFFFFF'
highlight_color = '#347083'

# Colorchanging Functions
def change_primary(cl=''):
    if cl:
        tree_view.tag_configure('color',background=cl)
        return

    global primary_color
    primary_color = colorchooser.askcolor()[1]
    if primary_color:
        tree_view.tag_configure('color',background=primary_color)
    
def change_highlight(cl=''):
    if cl:
        style.map('Treeview',background=[('selected',cl)])
        return

    global highlight_color
    highlight_color = colorchooser.askcolor()[1]
    if highlight_color:
        style.map('Treeview',background=[('selected',highlight_color)])

def save():
    global highlight_color,primary_color
    with open("color.dat","w") as f:
        f.write(f"{primary_color}\n{highlight_color}")

def reset_color():
    global highlight_color,primary_color
    primary_color = '#FFFFFF'
    highlight_color = '#347083'
    change_primary(primary_color)
    change_highlight(highlight_color)

    save()

# Configure Menu
option_menu = Menu(menu,tearoff=0)
menu.add_cascade(menu=option_menu,label="Options")
option_menu.add_command(label="Change Primary Color",command=change_primary)
option_menu.add_command(label="Change Highlight Color",command=change_highlight)
option_menu.add_command(label="Save Color Choices",command=save)
option_menu.add_command(label="Reset Color Choices",command=reset_color)
option_menu.add_separator()
option_menu.add_command(label="Exit",command=exit)

# Search Function
def search():
    s = search_box.get()
    tree_view.delete(*tree_view.get_children())

    c.execute(f"SELECT rowid, * FROM customers WHERE {extra[dropdown.current()]} like ?",(s,))
    records = c.fetchall()
    
    # Add Data 
    for count,record in enumerate(records):
        tree_view.insert(parent='',
                        index=END,
                        iid=count,
                        text='',
                        values=tuple(record),
                        tags="color"
                    )
    
    # Commit Changes
    conn.commit()

# Configure Search Bar
search_bar = Frame(root)
search_bar.pack()

search_box = Entry(search_bar)
search_box.grid(row=0,column=0,padx=5,pady=5)

drop_var = StringVar()
dropdown = ttk.Combobox(search_bar,values=columns[1::1],textvariable=drop_var)
dropdown.current(0)
dropdown.grid(row=0,column=1)

# Add a Search button to trigger the search operation
search_button = Button(search_bar, text="Search",command=search)
search_button.grid(row=0,column=2,padx=5,pady=5)

# Create Database / Connect to One that Exists
conn = sqlite3.connect("Treeview_CRM.db")

# Create a cursor instance
c = conn.cursor()   

# Create a Table
c.execute("""CREATE TABLE IF NOT EXISTS CUSTOMERS (
    NAME text,
    ORDER_NO text,
    COST integer,
    ADDRESS text,
    CITY text,
    STATE text,
    PINCODE integer
)""")

def querry_database():
    # Create Database / Connect to One that Exists
    conn = sqlite3.connect("Treeview_CRM.db")

    # Create a cursor instance
    c = conn.cursor()   

    c.execute("SELECT rowid, * FROM customers")
    records = c.fetchall()
    
    # Add Data 
    for count,record in enumerate(records):
        tree_view.insert(parent='',
                        index=END,
                        iid=count,
                        text='',
                        values=tuple(record),
                        tags="color"
                    )
    
    # Commit Changes
    conn.commit()

# Add Style
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3"
            )

# Change Selected Color
style.map("Treeview",background=[('selected','#347083')])

# Create a Treeview Frame
tf_frame = Frame(root)
tf_frame.pack(pady=5)

tf_scrollbar = Scrollbar(tf_frame)
tf_scrollbar.pack(side=RIGHT,fill=Y)

# Create the TreeView
tree_view = ttk.Treeview(tf_frame,yscrollcommand=tf_scrollbar.set,selectmode=EXTENDED)
tree_view.pack()

# Configure the Scrollbar
tf_scrollbar.config(command=tree_view.yview)

# Format Columns & Create Headings
tree_view['columns'] = columns

tree_view.column("#0",width=0,stretch=0) # Hide the 0th columns (it is useless)
tree_view.heading("#0",text="",anchor=W) # Same as above

for item in columns:
    if not item == "ID":
        tree_view.column(item,anchor=CENTER,width=120)
    else:
        tree_view.column(item,anchor=E,width=100)
    tree_view.heading(item,text=item,anchor=CENTER)

# Create Row Tag
tree_view.tag_configure('color',background="white")

# Add Record Entry Boxes
data_frame = LabelFrame(root,text="Records")
data_frame.pack(fill=X,expand=YES,padx=15)

# Calculate the number of rows needed based on the number of items in columns
num_rows = (len(columns) + 1) // 2

record_label_entries_dict = {}
for j, item in enumerate(columns):
    # Calculate the row and column indices for the current item
    row = j % 2
    col = j // 2
    
    label = Label(data_frame, text=item)
    label.grid(row=row,column=col*num_rows,padx=20,pady=5)

    entry = Entry(data_frame)
    entry.grid(row=row,column=1+col*num_rows)

    record_label_entries_dict[item] = [label,entry]

list(record_label_entries_dict.values())[0][1].config(state="disabled")
# First Item is ID (Label,Entry), selects Entry then configs

# Add Control Buttons
button_frame = LabelFrame(root,text="Controls")
button_frame.pack(fill=X,expand=YES,padx=10)

btn_list = ["Add","Remove","Remove All","Update","Select","Move Up","Move Down","Clear Search"]
control_btns_list = []

# Control Buttons Function
def control_btns(func):
    list(record_label_entries_dict.values())[0][1].config(state="normal")

    # Add
    if func == btn_list[0]:
        d = {}
        new_values = [entry[1].get() for entry in record_label_entries_dict.values()]
        col = ['name','order_no','cost','address','city','state','pincode']

        for i in range(1, len(new_values)):  # Start from 1 to skip the ID
            d[col[i - 1]] = new_values[i]

        c.execute("INSERT INTO customers VALUES (:name, :order_no, :cost, :address, :city, :state, :pincode)",d)
        conn.commit()

        # Clear Entry Boxes
        for entry in record_label_entries_dict.values():
            entry[1].delete(0,END)

        # Refresh the Treeview
        tree_view.delete(*tree_view.get_children())

        querry_database()
    
    # Remove
    elif func == btn_list[1]:
        if (messagebox.askyesno("Confirmation","Are you sure you want to delete the following records in the database?")):
            sel = tree_view.selection()
            if sel:
                for s in sel:
                    # Delete from Database
                    row_id = tree_view.item(s, 'values')[0]  # Get the rowid from the selected item
                    c.execute("DELETE FROM customers WHERE rowid=?", (row_id,))
                    tree_view.delete(s)  # Remove from the Treeview
                conn.commit()
            else:
                messagebox.showwarning("Warning", "No item selected. Please select an item.")

    # Remove All
    elif func == btn_list[2]:
        if (messagebox.askyesno("Confirmation","Are you sure you want to delete all the records in the database?")):
            tree_view.delete(*tree_view.get_children())
            c.execute("DROP TABLE customers")
            c.execute("""CREATE TABLE IF NOT EXISTS CUSTOMERS (
                NAME text,
                ORDER_NO text,
                COST integer,
                ADDRESS text,
                CITY text,
                STATE text,
                PINCODE integer
            )""")
            
            conn.commit()

    # Select
    elif func == btn_list[4]:
        # Clear Entry Boxes
        for entry in record_label_entries_dict.values():
            entry[1].delete(0,END)

        selected = tree_view.selection()
        if len(selected) == 1:
            values = tree_view.item(selected[0], 'values')
            
            for i, entry in enumerate(record_label_entries_dict.values()):
                entry[1].insert(0, values[i])

        elif len(selected) > 1:
            messagebox.showwarning("Warning","Multiple items selected. Please select only one item.")

        else:
            messagebox.showwarning("Warning","No item selected. Please select an item.")

    # Update
    elif func == btn_list[3]:
        selected = tree_view.focus()
        if selected:
            new_values = [entry[1].get() for entry in record_label_entries_dict.values()]
            tree_view.item(selected, values=new_values)
            
            col = ['name','order_no','cost','address','city','state','pincode']

            d = {}

            for i in range(1, len(new_values)):  # Start from 1 to skip the ID
                d[col[i - 1]] = new_values[i]
            d['oid'] = new_values[0]  # Assuming the ID is in the first position

            c.execute("""UPDATE customers SET 
                      name = :name,
                      order_no = :order_no,
                      cost = :cost,
                      address = :address,
                      city = :city,
                      state = :state,
                      pincode = :pincode
                    
                      WHERE rowid = :oid""", d
                    )
            conn.commit()
        else:
            messagebox.showwarning("Warning", "No item selected. Please select an item.")
        
        # Clear Entry Boxes
        for entry in record_label_entries_dict.values():
            entry[1].delete(0,END)

    # Move Up
    elif func == btn_list[5]:
        rows = tree_view.selection()
        for row in rows:
            tree_view.move(row,tree_view.parent(row),tree_view.index(row)-1)
    
    # Move Down
    elif func == btn_list[6]:
        rows = tree_view.selection()
        for row in reversed(rows):
            tree_view.move(row,tree_view.parent(row),tree_view.index(row)+1)

    # Clear Search
    elif func == btn_list[7]:
        search_box.delete(0,END)
        tree_view.delete(*tree_view.get_children())
        dropdown.current(0)
        querry_database()

    list(record_label_entries_dict.values())[0][1].config(state="disabled")

for i,item in enumerate(btn_list):
    btn = Button(button_frame, text=item, command=lambda item=item: control_btns(item))
    btn.grid(row=0,column=i,padx=32,pady=5)

    control_btns_list.append(btn)

querry_database()

with open("color.dat","r") as f:
    p,h = f.read().split("\n")
    if p and h:
        change_primary(p)
        change_highlight(h)

# Commit Changes
conn.commit()

root.mainloop()

# Close our Connection
conn.close()