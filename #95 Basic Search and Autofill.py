from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("550x350")

# Update the Entrybox using selected
def fill_entry(event):
    # Clear Entry Box
    entry_box.delete(0,END)

    # Add Clicked List Item To Entry Box
    entry_box.insert(0,list_box.get(ACTIVE))

# Update The List
def update(data):
    # Clear The Listbox
    list_box.delete(0,END)

    # Add student in Listbox
    for i in data:
        list_box.insert(END,i)

# Check Entry Vs Listbox
def check_in_listbox(event):
    # Get Typed 
    typed = entry_box.get()
    print(typed)
    if typed == "":
        data = stds
    else:
        data = []
        for i in stds:
            if typed.lower() in i.lower():
                data.append(i)
                
    # Update the Listbox Using Updated and Sorted Data
    update(data)

title = Label(root,text="Search:-")
title.pack(pady=10)

entry_box = Entry(root,font=("Calibri",15),width=40)
entry_box.pack()

list_box = Listbox(root,width=80)
list_box.pack(pady=20)

# Create A List of Students in my Class
stds = ["Aaradhya Agrawal", "Aarav Sancheti", "Aarya Nahar", "Aditi Bhargava", "Advait Rana", "Akshita Nyati", "Ansh Agrawal", "Anshika Agarwal", "Argh Patni", "Arnav Agrawal", "Arnav Mehta", "Arnav Toshniwal", "Arv Nagar", "Aryan Sharma", "Daksh Airen", "Deshna Patodi", "Hemal Patel", "Ishi Bansal", "Kanishth Singh", "Jenil Chudgar","Khyati Garg", "Labdhi Jain", "Manas Khandelwal", "Mohana Bansal", "Nivedita Mehta", "Paavani Mokshmar", "Parth Bajaj", "Parth Kelwa", "Prashashti Jain", "Raunak Kinger", "Reva Agrawal", "Saanvi Vyas", "Saharsh Garg", "Sarthak Chaturvedi", "Sarva Misra", "Shiven Zalani", "Shreyasi Chelawat", "Veer Jain", "Yajat Khanna"]

update(stds)

# Create Binding on Listbox
list_box.bind("<<ListboxSelect>>",fill_entry)

# Create Binding on Entry
entry_box.bind("<KeyRelease>",check_in_listbox)

root.mainloop()