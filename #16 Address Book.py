import sqlite3
from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("280x400")

#--Databases--

#Create a database or connect to one
conn = sqlite3.connect("address_book.db")

#Create cursor
cursor = conn.cursor()


#Create a Table
'''
cursor.execute("""CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    pincode number
)""")
'''

#Comit Changes
conn.commit()
    

#Function
def save():
    #Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    #Create cursor
    cursor = conn.cursor()

    oid = updateEntryBox.get()
    
    if oid=="":
        editor.destroy()

    cursor.execute("""UPDATE addresses SET 
    first_name = :f,
    last_name = :l,
    address = :a,
    city = :c,
    state = :s,
    pincode = :p

    WHERE oid = :oid""",
    {
        'f':fName_editor.get(),
        'l':lName_editor.get(),
        'a':address_editor.get(),
        'c':city_editor.get(),
        's':state_editor.get(),
        'p':pincode_editor.get(),
        'oid': oid
    })

    #Comit Changes
    conn.commit()

    editor.destroy()

def submit():
    global fName,lName,city,state,pincode,address
    #Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    #Create cursor
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    pincode number
    )""")

    cursor.execute("INSERT INTO addresses VALUES (:firstName,:lastName,:address,:city,:state,:pincode)",
        {
            'firstName':fName.get(),
            'lastName':lName.get(),
            'address':address.get(),
            'city':city.get(),
            'state':state.get(),
            'pincode':pincode.get(),
        }
    )

    fName.delete(0,END)
    lName.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    pincode.delete(0,END)
    address.delete(0,END)
    
    #Comit Changes
    conn.commit()

    #Close Connection
    conn.close()


def update():
    global fName,fName_label,lName,lName_label,address,add_label,city,city_label,state,state_label,pincode,pin_label,updateEntryBox,fName_editor,lName_editor,city_editor,address_editor,state_editor,pincode_editor,editor

    #Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    #Create cursor
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    pincode number
    )""")
    
    editor = Tk()
    editor.title("Update A Record")
    editor.iconbitmap("computer.ico")
    editor.geometry("280x250")
    
    fName_label_editor = Label(editor,text="First Name: ").grid(row=1,column=0,pady=(20,0))
    fName_editor = Entry(editor,width=30)
    fName_editor.grid(row=1,column=1,pady=(20,0))

    lName_label_editor = Label(editor,text="Last Name: ").grid(row=2,column=0)
    lName_editor = Entry(editor,width=30)
    lName_editor.grid(row=2,column=1)

    add_label_editor = Label(editor,text="Address: ").grid(row=3,column=0)
    address_editor = Entry(editor,width=30)
    address_editor.grid(row=3,column=1)

    city_label_editor = Label(editor,text="City: ").grid(row=4,column=0)
    city_editor = Entry(editor,width=30)
    city_editor.grid(row=4,column=1)

    state_label_editor = Label(editor,text="State: ").grid(row=5,column=0)
    state_editor = Entry(editor,width=30)
    state_editor.grid(row=5,column=1)

    pin_label_editor = Label(editor,text="Pincode: ").grid(row=6,column=0)
    pincode_editor = Entry(editor,width=30)
    pincode_editor.grid(row=6,column=1)

    submitBtn_editor = Button(editor,text="Save!",command=save).grid(row=7,column=0,columnspan=2,pady=(10,0))

    oid = updateEntryBox.get()

    if oid == "":
        editor.destroy()

    cursor.execute("SELECT *,oid FROM addresses WHERE oid="+oid)
    records = cursor.fetchall()

    for record in records:
        fName_editor.insert(0,record[0])
        lName_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        pincode_editor.insert(0,record[5])

    printR = ""
    i=0
    for record in records:
        printR += f"{record[-1]}\t{record[0]} {record[1]}"+"\n"
        Label(root,text=printR).grid(row=11+i+1,column=0,columnspan=3,padx=10)

    

    #Comit Changes
    conn.commit()

    #Close Connection
    conn.close()

def delete():
    #Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    #Create cursor
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    pincode number
    )""")

    cursor.execute("DELETE FROM addresses WHERE oid = "+deleteEntryBox.get())

    #Comit Changes
    conn.commit()

    #Close Connection
    conn.close()


def see():
    #Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    #Create cursor
    cursor = conn.cursor()

    # cursor.execute("""CREATE TABLE IF NOT EXISTS addresses(
    # first_name text,
    # last_name text,
    # address text,
    # city text,
    # state text,
    # pincode number
    # )""")

    cursor.execute("SELECT *,oid FROM addresses")
    records = cursor.fetchall()
    
    Label(root,text="S.No\tName",fg="blue").grid(row=11,column=0,columnspan=3)

    printR = ""
    i=0
    for record in records:
        printR += f"{record[-1]}\t{record[0]} {record[1]}"+"\n"
        Label(root,text=printR).grid(row=11+i+1,column=0,columnspan=3,padx=10)

    #Comit Changes
    conn.commit()

    #Close Connection
    conn.close()

see()

#GUI
title = Label(root,text="Address Book",fg="red").grid(row=0,column=0,columnspan=3)

fName_label = Label(root,text="First Name: ").grid(row=1,column=0)
fName = Entry(root,width=30)
fName.grid(row=1,column=1)

lName_label = Label(root,text="Last Name: ").grid(row=2,column=0)
lName = Entry(root,width=30)
lName.grid(row=2,column=1)

add_label = Label(root,text="Address: ").grid(row=3,column=0)
address = Entry(root,width=30)
address.grid(row=3,column=1)

city_label = Label(root,text="City: ").grid(row=4,column=0)
city = Entry(root,width=30)
city.grid(row=4,column=1)

state_label = Label(root,text="State: ").grid(row=5,column=0)
state = Entry(root,width=30)
state.grid(row=5,column=1)

pin_label = Label(root,text="Pincode: ").grid(row=6,column=0)
pincode = Entry(root,width=30)
pincode.grid(row=6,column=1)

submitBtn = Button(root,text="Submit!",command=submit)
submitBtn.grid(row=7,column=0,columnspan=3,pady=10)

seeItems = Button(root,text="Refresh!",command=see)
seeItems.grid(row=8,column=0,columnspan=3)

deleteBtn = Button(root,text="Delete!",command=delete)
deleteBtn.grid(row=9,column=0,columnspan=3,pady=10)

deleteEntryBox = Entry(root,width=5)
deleteEntryBox.grid(row=9,column=1,padx=(20,0))

updateBtn = Button(root,text="Update!",command=update)
updateBtn.grid(row=10,column=0,columnspan=3)

updateEntryBox = Entry(root,width=5)
updateEntryBox.grid(row=10,column=1,padx=(20,0))

#Close Connection
conn.close()

root.mainloop()