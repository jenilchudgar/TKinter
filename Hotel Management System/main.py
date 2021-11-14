from tkinter import *
from database import *
from tkinter import ttk
import json

root = Tk()
root.title("Hotel Management System")
root.iconbitmap("home.ico")
root.geometry("1000x500")

def save_food_to_database():
    food_name = name.get()
    food_price = price.get()
    Food.start()
    Food.add_food(food_name,food_price)
    top.destroy()
    listBox.delete(0,END)
    # Add Food Items to Listbox
    Food.start()
    items = Food.show_all(food_only=True)

    for e in items:
        listBox.insert(END,e[0])

def add():
    global name,price,top
    top = Toplevel()
    top.title("Add Food Item")
    top.geometry("350x200")

    title = Label(top,text="Add Food Item",font=('Calibri',14))
    title.grid(row=0,column=1)

    name_label = Label(top,text="Food Name:",font=('Calibri',14))
    name_label.grid(row=1,column=0)
    name = Entry(top,font=('Calibri',14))
    name.grid(row=1,column=1)

    price_label = Label(top,text="Food Price:",font=('Calibri',14))
    price_label.grid(row=2,column=0)
    price = Entry(top,font=('Calibri',14))
    price.grid(row=2,column=1)

    save_btn = Button(top,text="Add",font=('Calibri',14),command=save_food_to_database)
    save_btn.grid(row=3,column=1,pady=10)

def take_order():
    # Save selections
    orders = []
    for i in listBox.curselection():
        orders.append(listBox.get(i))
    Order.start()
    Order.add_food(user_name.get(),json.dumps(orders))

    # Write order to text file
    f = open("order.txt","w")
    f.write(f"""Customer: {user_name.get()}
Food Items:\n""")
    Order.start()
    l = Order.show_all()
    for order in l:
        food_items = json.loads(order[2])
        print(food_items)
        Food.start()
        print(Food.show_all())
        Food.cursor.execute(f"SELECT PRICE FROM FOOD WHERE NAME = Roti;")
        price = Food.cursor.fetchall()[0]
        print("Roti",price)
        # for food in food_items:
        #     Food.start()
        #     Food.cursor.execute(f"SELECT PRICE FROM FOOD WHERE NAME = "+str(food)+";")
        #     price = Food.cursor.fetchall()[0]
        #     print(food,price)


####################################################

# json.dumps(['please','help','me']) -> list to str
# json.loads('["please", "help", "me"]') -> str to list

# Root Content

# Title
title = Label(root,text="YC Hotel Management System".center(130),font=('Calibri',20))
title.grid(row=0,column=0)

# User's Name
user_name_label = Label(root,text="User's Name: ",font=('Calibri',14))
user_name_label.grid(row=1,column=0)
user_name = Entry(root,font=('Calibri',14))
user_name.grid(row=2,column=0,pady=10)

# Content Frame
content_frame = Frame(root,width=800,height=600)
content_frame.grid(row=3,column=0)

# List Box and scrollbar
scrollbar = Scrollbar(content_frame,orient=VERTICAL)
listBox = Listbox(content_frame,width=30,selectmode=MULTIPLE,yscrollcommand=scrollbar.set)
listBox.grid(row=0,column=0)
scrollbar.config(command=listBox.yview)
scrollbar.grid(row=0,column=1,sticky=NS)

# Add Food Items to Listbox
Food.start()
# Food.add_food("Chole Puri",500)
items = Food.show_all(food_only=True)

for e in items:
    listBox.insert(END,e[0])

# Add Button
add_btn = Button(root,text="Add Food Item",font=('Calibri',14),command=add)
add_btn.grid(row=4,column=0,pady=10)

# Take Order Button
order_btn = Button(root,text="Take Order",command=take_order,font=('Calibri',14))
order_btn.grid(row=5,column=0)

print(Order.show_all())

root.mainloop()