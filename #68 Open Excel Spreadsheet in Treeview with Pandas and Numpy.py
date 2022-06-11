from tkinter import ttk, filedialog
from tkinter import *
import pandas as pd

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("600x400")

# Define File Opening Function
def file_open():
    file_name = filedialog.askopenfilename(
        initialdir=r"C:\Users\sanja\Desktop\Coding\Python\TKinter",
        title="Open an Excel File",
        filetypes=(
            ("Excel Files","*.xlsx"),
        )
    )

    df = ""

    if file_name:
        try:
            file_name = r"{}".format(file_name)
            df = pd.read_excel(file_name)

        except Exception:
            print("An Error occured!")

    clear_tree()

    # Setup New Treeview
    tree["column"] = list(df.columns)
    tree["show"] = "headings"

    # Loop through columns list
    for col in tree["column"]:
        tree.heading(col,text=col)
    
    # Put Data in treeview
    df_rows = df.to_numpy().tolist()

    for row in df_rows:
        tree.insert(parent="",index=END,values=row)

    tree.pack()

def clear_tree():
    tree.delete(*tree.get_children())

# Create Frame
frame = Frame(root)
frame.pack(pady=20)

# Create Treeview
tree = ttk.Treeview(frame)

# Add Some Style
style = ttk.Style()

# Pick A Theame
style.theme_use("clam")

# Add a menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu,tearoff=False)
file_menu.add_command(label="Open",command=file_open)

my_menu.add_cascade(label="Spreadsheets",menu=file_menu)

root.mainloop()