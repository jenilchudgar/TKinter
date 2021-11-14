from tkinter import *

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# Delete Function
def delete():
    for i in reversed(listBox.curselection()):
        listBox.delete(i)

    label.config(text="")

# Select Function
def select():
    res = []
    for i in listBox.curselection():
        res.append(listBox.get(i))
    label.config(text=str(res))

# Delete All Function
def delete_all():
    listBox.delete(0,END)
    label.config(text="")

# Create a frame
listBox_frame = Frame(root)
scrollbar = Scrollbar(listBox_frame,orient=VERTICAL)

# Listbox
listBox = Listbox(listBox_frame,yscrollcommand=scrollbar.set,width=30,selectmode=MULTIPLE)

# Configure scrollbar
scrollbar.config(command=listBox.yview)

# Pack
scrollbar.pack(side=RIGHT,fill=Y)
listBox.pack(pady=20)
listBox_frame.pack()

# Add Items to Listbox
listBox.insert(END,"Jenil")
listBox.insert(END,"John")

myList = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen"]
for e in myList:
    listBox.insert(END,e)

btn_delete = Button(root,text="Delete",command=delete)
btn_delete.pack(pady=10)

btn_delete_all = Button(root,text="Delete All",command=delete_all)
btn_delete_all.pack(pady=10)

btn_select = Button(root,text="Select",command=select)
btn_select.pack(pady=10)

global label
label = Label(root,text="")
label.pack()

root.mainloop()