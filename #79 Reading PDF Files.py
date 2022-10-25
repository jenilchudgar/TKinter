from tkinter import *
from tkinter import filedialog
import PyPDF2

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

def clear():
    textbox.delete(1.0,END)

def open_file():
    f = filedialog.askopenfilename(title="Open PDF File",filetypes=(
        ("PDF Files","*.pdf"),
        ("All Files","*.*")
    ))

    if f:
        pdf_file = PyPDF2.PdfFileReader(f)
        for i in range(0,pdf_file.numPages):
            page = pdf_file.getPage(i)
            # Extract Content
            page_content = page.extractText()

            # Add Text to TextBox
            textbox.insert(1.0,f"Page: {i+1}\n{page_content}\n")


# Create Textbox
frame = Frame(root)
frame.pack(pady=20)

scroll_bar = Scrollbar(frame)
scroll_bar.pack(side=RIGHT,fill=Y)

textbox = Text(frame,height=40,width=40,yscrollcommand=scroll_bar.set,undo=True)
textbox.pack(pady=10)

scroll_bar.config(command=textbox.yview)

# Create A menu
menu = Menu(root)
root.config(menu=menu)

# File Menu
file_menu = Menu(menu,tearoff=False)
menu.add_cascade(menu=file_menu,label="File")
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Clear",command=clear)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

root.mainloop()