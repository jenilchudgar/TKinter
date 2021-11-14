import mysql.connector
import csv
from tkinter import * 
from tkinter import ttk
global g
root = Tk()
root.title("CRM")
root.iconbitmap("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\computer.ico")
root.geometry("720x500")

def add():
    sql = "INSERT INTO customers (first_name,last_name,pin,paid,email,state,country,address,payment_method,discount_code,phone) VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (fName_box.get(),lName_box.get(),pin_box.get(),amountpaid_box.get(),email_box.get(),state_box.get(),country_box.get(),add_box.get(),paymentMethod_box.get(),discountCode_box.get(),phone_box.get())
    curr.execute(sql,values)

    clear()

    db.commit()

def search():
    global searchCus
    global fName_box,lName_box,add_box,state_box,country_box,pin_box,paymentMethod_box,discountCode_box,phone_box,email_box,amountpaid_box
    searchCus = Tk()
    searchCus.title("Search Customers")
    searchCus.iconbitmap("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\computer.ico")
    searchCus.geometry("600x400")

    dropDown = ttk.Combobox(searchCus,value=["Search By","First Name","Email","ID"],font=('Calibri',15))
    dropDown.current(0)
    dropDown.grid(row=1,column=2)

    j = 0
    r = ""

    def edit(oid,row):
        searchCus.geometry("800x800")
        fName_label2 = Label(searchCus,text="First Name",font=('Calibri',15))
        fName_label2.grid(row=row+1,column=0,sticky=W,padx=40)
        lName_label2 = Label(searchCus,text="Last Name",font=('Calibri',15))
        lName_label2.grid(row=row+2,column=0,sticky=W,padx=40)
        add_label2 = Label(searchCus,text="Address",font=('Calibri',15))
        add_label2.grid(row=row+3,column=0,sticky=W,padx=40)
        state_label2 = Label(searchCus,text="State",font=('Calibri',15))
        state_label2.grid(row=row+4,column=0,sticky=W,padx=40)
        country_label2 = Label(searchCus,text="Country",font=('Calibri',15))
        country_label2.grid(row=row+5,column=0,sticky=W,padx=40)
        pin_label2 = Label(searchCus,text="Pincode",font=('Calibri',15))
        pin_label2.grid(row=row+6,column=0,sticky=W,padx=40)
        paymentMethod_label2 = Label(searchCus,text="Payment Medthod",font=('Calibri',15))
        paymentMethod_label2.grid(row=row+7,column=0,sticky=W,padx=40)
        discountCode_label2 = Label(searchCus,text="Discount Code",font=('Calibri',15)).grid(row=row+8,column=0,sticky=W,padx=40)
        phone_label2 = Label(searchCus,text="Phone",font=('Calibri',15))
        phone_label2.grid(row=row+9,column=0,sticky=W,padx=40)
        email_label2 = Label(searchCus,text="Email",font=('Calibri',15))
        email_label2.grid(row=row+10,column=0,sticky=W,padx=40)
        amountpaid_label2 = Label(searchCus,text="Amount Paid",font=('Calibri',15))
        amountpaid_label2.grid(row=row+11,column=0,sticky=W,padx=40)

        id_label2 = Label(searchCus,text="ID",font=('Calibri',15))
        id_label2.grid(row=row+12,column=0,sticky=W,padx=40)

        global fName_box2,lName_box2,add_box2,state_box2,country_box2,pin_box2,paymentMethod_box2,discountCode_box2,email_box2,amountpaid_box2,id_box2,phone_box2
        fName_box2 = Entry(searchCus,font=('Calibri',15),width=25)
        fName_box2.grid(row=row+1,column=2)
        lName_box2 = Entry(searchCus,font=('Calibri',15),width=25)
        lName_box2.grid(row=row+2,column=2)
        add_box2 = Entry(searchCus,font=('Calibri',15),width=25)
        add_box2.grid(row=row+3,column=2)
        state_box2 = Entry(searchCus,font=('Calibri',15),width=25)
        state_box2.grid(row=row+4,column=2)
        country_box2 = Entry(searchCus,font=('Calibri',15),width=25)
        country_box2.grid(row=row+5,column=2)
        pin_box2 = Entry(searchCus,font=('Calibri',15),width=25)
        pin_box2.grid(row=row+6,column=2)
        paymentMethod_box2 = Entry(searchCus,font=('Calibri',15),width=25)
        paymentMethod_box2.grid(row=row+7,column=2)
        discountCode_box2 = Entry(searchCus,font=('Calibri',15),width=25)
        discountCode_box2.grid(row=row+8,column=2)
        phone_box2 = Entry(searchCus,font=('Calibri',15),width=25)
        phone_box2.grid(row=row+9,column=2)
        email_box2 = Entry(searchCus,font=('Calibri',15),width=25)
        email_box2.grid(row=row+10,column=2)
        amountpaid_box2 = Entry(searchCus,font=('Calibri',15),width=25)
        amountpaid_box2.grid(row=row+11,column=2)
        id_box2 = Entry(searchCus,font=('Calibri',15),width=25)
        id_box2.grid(row=row+12,column=2)

        sql2 = "SELECT * FROM customers WHERE user_id = %s"
        n = (oid,)
        curr.execute(sql2,n)
        res = curr.fetchall()[0]
        fName_box2.insert(0,res[0])
        lName_box2.insert(0,res[1])
        pin_box2.insert(0,res[2])
        amountpaid_box2.insert(0,res[3])
        id_box2.insert(0,res[4])
        email_box2.insert(0,res[5])
        state_box2.insert(0,res[6])
        country_box2.insert(0,res[7])
        add_box2.insert(0,res[8])
        paymentMethod_box2.insert(0,res[9])
        discountCode_box2.insert(0,res[10])
        phone_box2.insert(0,res[11])

        save = Button(searchCus,text="Save!",font=('Calibri',15),command=lambda:saveNow(oid))
        save.grid(row=row+15,column=2)
        
    def saveNow(oid):
        sql = """UPDATE customers SET first_name = %s,last_name = %s,pin = %s,paid = %s,email = %s,state = %s,country = %s,address = %s,payment_method = %s,discount_code = %s,phone = %s WHERE user_id = %s"""
        fname = fName_box2.get()
        lname = lName_box2.get()
        pin = pin_box2.get()
        amountpaid = amountpaid_box2.get()
        email = email_box2.get()
        ad = add_box2.get()
        state = state_box2.get()
        phone = phone_box2.get()
        discountCode = discountCode_box2.get()
        pay = paymentMethod_box2.get()
        placeHolders = (fname,lname,pin,amountpaid,email,state,country_box2.get(),ad,pay,discountCode,phone,oid)

        curr.execute(sql,placeHolders)
        db.commit()

        global done
        done = Tk()
        done.title("Done!")
        done.geometry("210x90")
        Label(done,text="Done!",font=('Calibri',15)).pack()
        Button(done,text="Ok!",command=ex,font=('Calibri',15)).pack()
        

    def search_inside():
        global result,j,r,g
        selected = dropDown.get()
        value=["Search By","First Name","Email","ID"]
        v = ""
        if selected == value[0]:
            Label(searchCus,text="Choose a field",font=('Calibri',15)).grid(row=3,column=1)
            return
        if selected == value[1]:
            v = "first_name"
        elif selected == value[2]:
            v = "email"
        elif selected == value[3]:
            v = "user_id"

        searched = searchBox.get()
        sql = f"SELECT * FROM customers WHERE {v} = %s"
        name = (searched,)
        curr.execute(sql,name)
        result = curr.fetchall()
        g = result
        if not result:
            result = "Record Not Found!"
            Label(searchCus,text=result,font=('Calibri',15)).grid(row=3,column=0)
        else:
            i=3
            oid = result[0][4]
            for x in result:
                editBtn = Button(searchCus,text="Edit",font=('Calibri',12),command=lambda:edit(oid=oid,row=i+1))
                editBtn.grid(row=i+1,column=0)

                Label(searchCus,text=f"{x[4]}. {x[0]} {x[1]}\n{x[5]} {x[11]}\n{x[8]} {x[2]} {x[6]} {x[7]}\n{x[9]} {x[10]} {x[3]}\n______________________________",font=('Calibri',15)).grid(row=i+1,column=1,columnspan=2)
                i+=1
            j=i
            r = result
    
    global g
    title = Label(searchCus,text="Search",font=('Calibri',20))
    title.grid(row=0,column=0,columnspan=2,pady=(0,20))

    searchBox = Entry(searchCus,font=('Calibri',15))
    searchBox.grid(row=1,column=1)
    searchLabel = Label(searchCus,text="Search",font=('Calibri',15))
    searchLabel.grid(row=1,column=0,padx=(80,0))
    
    csvBtn = Button(searchCus,text="Save as CSV!",command=lambda:writeToCSV(g),font=('Calibri',15))
    csvBtn.grid(row=2,column=2,pady=20)

    searchB = Button(searchCus,text="Search!",font=('Calibri',15),command=search_inside)
    searchB.grid(row=2,column=1)


def writeToCSV(result):
    with open('customers.csv','w',newline='') as f:
        w = csv.writer(f,dialect='excel')
        w.writerow("S.No,First Name,Last Name,Email,Phone Number,Address,Pincode,State,Country,Payment Medthod,Discount Code,Amount Paid".split(","))
        w.writerow("")
        for x in result:
            w.writerow(f"{x[4]}.,{x[0]},{x[1]},{x[5]},{x[11]},{x[8]},{x[2]},{x[6]},{x[7]},{x[9]},{x[10]},{x[3]}".split(","))
    global done
    done = Tk()
    done.title("Done!")
    done.geometry("210x90")
    Label(done,text="Done!",font=('Calibri',15)).pack()
    Button(done,text="Ok!",command=ex,font=('Calibri',15)).pack()

def ex():
    try:
        global done,showCus,searchCus
        done.destroy()
        showCus.destroy()
    except:
        pass
    try:
        searchCus.destroy()
    except:
        pass


def show():
    global showCus
    showCus = Tk()
    showCus.title("All Customers")
    showCus.iconbitmap("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\computer.ico")
    showCus.geometry("600x500")

    curr.execute("SELECT * FROM customers")
    res = curr.fetchall()
    i=1
    Label(showCus,text="\t\tList Customers",font=('Calibri',20)).grid(row=0,column=0,columnspan=3)
    for x in res:
        Label(showCus,text=f"\t{x[4]}. {x[0]} {x[1]}\n\t{x[5]} {x[11]}\n\t{x[8]} {x[2]} {x[6]} {x[7]}\n\t{x[9]} {x[10]} {x[3]}\n______________________________",font=('Calibri',15)).grid(row=1+i,column=1,columnspan=2)
        i+=1
    i+=1
    csvBtn = Button(showCus,text="Save as CSV!",command=lambda:writeToCSV(res),font=('Calibri',15))
    csvBtn.grid(row=i+1,column=2,pady=20)

def clear():
    fName_box.delete(0,END)
    lName_box.delete(0,END)
    add_box.delete(0,END)
    state_box.delete(0,END)
    country_box.delete(0,END)
    pin_box.delete(0,END)
    paymentMethod_box.delete(0,END)
    discountCode_box.delete(0,END)
    phone_box.delete(0,END)
    email_box.delete(0,END)
    amountpaid_box.delete(0,END)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "jenil"
)


curr =  db.cursor()
curr.execute("""CREATE TABLE IF NOT EXISTS customers(
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    pin INT(10),
    paid DECIMAL(10,2),
    user_id INT AUTO_INCREMENT PRIMARY KEY
)""")

# curr.execute("""ALTER TABLE customers ADD(
#     email VARCHAR(50),
#     state VARCHAR(50),
#     country VARCHAR(50),
#     address VARCHAR(100),
#     payment_method VARCHAR(50),
#     discount_code VARCHAR(50),
#     phone VARCHAR(20)
# )""")

# curr.execute("SELECT * FROM customers")
# a=[print(e) for e in curr.description]

title = Label(root,text="\tCustomer Database",font=('Calibri',20))
title.grid(row=0,column=0,columnspan=3)

fName_label = Label(root,text="First Name",font=('Calibri',15))
fName_label.grid(row=1,column=0,sticky=W,padx=40)
lName_label = Label(root,text="Last Name",font=('Calibri',15))
lName_label.grid(row=2,column=0,sticky=W,padx=40)
add_label = Label(root,text="Address",font=('Calibri',15))
add_label.grid(row=3,column=0,sticky=W,padx=40)
state_label = Label(root,text="State",font=('Calibri',15))
state_label.grid(row=4,column=0,sticky=W,padx=40)
country_label = Label(root,text="Country",font=('Calibri',15))
country_label.grid(row=5,column=0,sticky=W,padx=40)
pin_label = Label(root,text="Pincode",font=('Calibri',15))
pin_label.grid(row=6,column=0,sticky=W,padx=40)
paymentMethod_label = Label(root,text="Payment Medthod",font=('Calibri',15))
paymentMethod_label.grid(row=7,column=0,sticky=W,padx=40)
discountCode_label = Label(root,text="Discount Code",font=('Calibri',15)).grid(row=8,column=0,sticky=W,padx=40)
phone_label = Label(root,text="Phone",font=('Calibri',15))
phone_label.grid(row=9,column=0,sticky=W,padx=40)
email_label = Label(root,text="Email",font=('Calibri',15))
email_label.grid(row=10,column=0,sticky=W,padx=40)
amountpaid_label = Label(root,text="Amount Paid",font=('Calibri',15))
amountpaid_label.grid(row=11,column=0,sticky=W,padx=40)


global fName_box,lName_box,add_box,state_box,country_box,pin_box,paymentMethod_box,discountCode_box,phone_box,email_box,amountpaid_box
fName_box = Entry(root,font=('Calibri',15),width=25)
fName_box.grid(row=1,column=2)
lName_box = Entry(root,font=('Calibri',15),width=25)
lName_box.grid(row=2,column=2)
add_box = Entry(root,font=('Calibri',15),width=25)
add_box.grid(row=3,column=2)
state_box = Entry(root,font=('Calibri',15),width=25)
state_box.grid(row=4,column=2)
country_box = Entry(root,font=('Calibri',15),width=25)
country_box.grid(row=5,column=2)
pin_box = Entry(root,font=('Calibri',15),width=25)
pin_box.grid(row=6,column=2)
paymentMethod_box = Entry(root,font=('Calibri',15),width=25)
paymentMethod_box.grid(row=7,column=2)
discountCode_box = Entry(root,font=('Calibri',15),width=25)
discountCode_box.grid(row=8,column=2)
phone_box = Entry(root,font=('Calibri',15),width=25)
phone_box.grid(row=9,column=2)
email_box = Entry(root,font=('Calibri',15),width=25)
email_box.grid(row=10,column=2)
amountpaid_box = Entry(root,font=('Calibri',15),width=25)
amountpaid_box.grid(row=11,column=2)

submitBtn = Button(root,text="Submit!",font=('Calibri',15),command=add)
submitBtn.grid(row=12,column=0,pady=20)

clearBtn = Button(root,text="Clear!",font=('Calibri',15),command=clear)
clearBtn.grid(row=12,column=3)

listCus = Button(root,text="List Customers",font=('Calibri',14),command=show)
listCus.grid(row=13,column=0)

searchBtn = Button(root,text="Search\Edit Customers",font=('Calibri',15),command=search)
searchBtn.grid(row=13,column=3)
root.mainloop()