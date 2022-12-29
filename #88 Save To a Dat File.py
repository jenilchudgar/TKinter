from tkinter import *
from tkinter import filedialog
import pickle
from tkinter import messagebox

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

# Create a List of sizes
sizes = ["SMALL".capitalize(),"MEDIUM".capitalize(),"LARGE".capitalize()]

text = Text(root,height=10,width=40)
text.pack(pady=10)

# Create A Button
def save_btn_func():
    # Grab text from text box
    text_to_save = text.get(1.0,END)

    # Define a filename
    f = filedialog.asksaveasfilename(title="Save As",filetypes=(("dat file","*.dat"),("All Files","*.*")))
    f=(f+".dat")

    # Open the file and save the data
    output_file = open(f"{f}","wb")
    pickle.dump(text_to_save,output_file)

    # Random Fun
    x = "/"

    # Conformation Message
    messagebox.showinfo(
        title="File Saved Successfully!",
        message=f"Your File {f.split(x)[-1]} has been saved successfully!"
    )

def open_btn_func():
    f = filedialog.askopenfilename(title="Save As",filetypes=(("dat file","*.dat"),("All Files","*.*")))

    # # Open the file and read the data
    input_file = open(f"{f}","rb")
    data = pickle.load(input_file)

    # Insert Text to Text Box
    text.insert(1.0,data)

save_btn = Button(root,text="Save!",command=save_btn_func)
save_btn.pack(pady=10)

open_btn = Button(root,text="Open!",command=open_btn_func)
open_btn.pack(pady=10)

root.mainloop()