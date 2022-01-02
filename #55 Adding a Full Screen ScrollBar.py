from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# Create Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH,expand=1)

# Create Canvas
canvas = Canvas(main_frame)
canvas.pack(side=LEFT,fill=BOTH,expand=1)

# Add Scrollbar to the Canvas
scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL,command=canvas.yview)
scrollbar.pack(side=RIGHT,fill=Y)

# Configure the Canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create ANOTHER Frame in the Canvas
sec_frame = Frame(canvas)

# Add that New Frame in a Window in the Canvas
canvas.create_window((0,0),window=sec_frame,anchor=NW)

for e in range(100):
    Button(sec_frame,text=f"Button {e}!").grid(row=e,column=0,pady=10)

root.mainloop()