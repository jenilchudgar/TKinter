from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# Define combo_box_selected function
def combo_box_selected(e):
    i = sizes.index(combo.get())
    color_combo.config(value=all_sizes[i])
    color_combo.current(0)

def list_box_selected(e):
    list_box_color.delete(0,END)
    i = sizes.index(list_box.get(ANCHOR))
    for i in all_sizes[i]:
        list_box_color.insert(END,i)

# Create a List of sizes
sizes = ["SMALL".capitalize(),"MEDIUM".capitalize(),"LARGE".capitalize()]

# Create a List of Colors
colors = ["RED","WHITE","YELLOW","ORANGE","PURPLE","GREY","BLUE","GREEN","BLACK"]


small_sizes = []
med_sizes = []
large_sizes = []
all_sizes = [small_sizes,med_sizes,large_sizes]

for i in range(0,3):
    for j in range(0,3):
        r = random.choice(colors)
        colors.pop(colors.index(r))
        all_sizes[j].append(r.capitalize())

# Create Combo Box
combo = ttk.Combobox(root,value=sizes,font=("Calibri",20))
combo.current(0)
combo.pack(pady=10)
combo.bind("<<ComboboxSelected>>",combo_box_selected)

# Create Color Combo Box
color_combo = ttk.Combobox(root,value=[""],font=("Calibri",20))
color_combo.current(0)
color_combo.pack(pady=10)

# Frame
frame = Frame(root)
frame.pack(pady=30)

# List Boxes
list_box = Listbox(frame)
list_box_color = Listbox(frame)

list_box.grid(row=0,column=0)
list_box_color.grid(row=0,column=1,padx=20)

for i in sizes:
    list_box.insert(END,i)

list_box.bind("<<ListboxSelect>>",list_box_selected)

root.mainloop()