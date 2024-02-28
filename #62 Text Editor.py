from tkinter import filedialog,font,messagebox,colorchooser
from tkinter import *
import win32api

root = Tk()
root.title("TKinter - Text Writer")
root.iconbitmap("img/editor/writing.ico")
root.geometry("1200x600")

global FILE
global EMPTY
global SELECTION

EMPTY = str()
FILE = EMPTY
SELECTION = False

# Functions
def new_file(e=None):
    global FILE
    text_box.delete(1.0,END)
    root.title("New File - Text Writer")
    status_bar.config(text="New File...\t")

    FILE = EMPTY

def open_file(e=None):
    global FILE
    text_box.delete(1.0,END)
    f = filedialog.askopenfilename(title="Open File",filetypes=(
        ("Text Files","*.txt"),
        ("Python Files","*.py"),
        ("HTML Files","*.html"),
        ("CSS Files","*.css"),
        ("C Files","*.c"),
        ("C++ Files","*.cpp"),
        ("JAVA Files","*.java"),
        ("All Files","*.*")
    ))
    status_bar.config(text=f)

    root.title(f"{f.split('/')[-1]} - Text Writer")
    
    FILE = f

    # Open The File
    if f:
        with open(f,"r") as file:
            text = file.read()
            text_box.insert(END,text)

def save_file(e=None):
    if FILE != EMPTY:
        with open(FILE,"w") as file:
            file.write(text_box.get(1.0,END))
        messagebox.showinfo("File Saved","The file was saved successfully!")
    else:
        save_as_file()

def save_as_file(e=None):
    f = filedialog.asksaveasfilename(defaultextension=".*",title="Save As",filetypes=(
        ("Text Files","*.txt"),
        ("Python Files","*.py"),
        ("HTML Files","*.html"),
        ("CSS Files","*.css"),
        ("C Files","*.c"),
        ("C++ Files","*.cpp"),
        ("JAVA Files","*.java"),
        ("All Files","*.*")
    ))

    if f:
        root.title(f"{f.split('/')[-1]} - Text Writer")
        status_bar.config(text=f)

        with open(f,"w") as file:
            file.write(text_box.get(1.0,END))
        messagebox.showinfo("File Saved","The file was saved successfully!")

def edit_cut(e=None):
    global SELECTION
    
    SELECTION = text_box.selection_get()

    if SELECTION:
        text_box.delete("sel.first","sel.last")

def edit_copy(e=None):
    global SELECTION

    SELECTION = text_box.selection_get()

def edit_paste(e=None):
    global SELECTION

    if e:
        SELECTION = root.clipboard_get()

    else:
        if SELECTION:
            pos = text_box.index(INSERT)
            text_box.insert(pos,SELECTION)

def text_styles_bold(e=None):
    cur_tags = text_box.tag_names("sel.first")
    bold_font = font.Font(text_box,text_box.cget("font"))
    bold_font.configure(weight=font.BOLD)

    text_box.tag_configure("bold",font=bold_font)

    if "bold" in cur_tags:
        text_box.tag_remove("bold","sel.first","sel.last")
    else:
        text_box.tag_add("bold","sel.first","sel.last")

def text_styles_italics(e=None):
    cur_tags = text_box.tag_names("sel.first")
    italics_font = font.Font(text_box,text_box.cget("font"))
    italics_font.configure(slant=font.ITALIC)

    text_box.tag_configure("italic",font=italics_font)

    if "italic" in cur_tags:
        text_box.tag_remove("italic","sel.first","sel.last")
    else:
        text_box.tag_add("italic","sel.first","sel.last")

def text_styles_text_color(e=None):
    color = colorchooser.askcolor()[1]

    if color:
        cur_tags = text_box.tag_names("sel.first")
        colors_font = font.Font(text_box,text_box.cget("font"))

        text_box.tag_configure("color",font=colors_font,foreground=color)

        if "color" in cur_tags:
            text_box.tag_remove("color","sel.first","sel.last")
        else:
            text_box.tag_add("color","sel.first","sel.last")

def text_styles_text_color_all(e=None):
    color = colorchooser.askcolor()[1]

    if color:
        text_box.config(foreground=color)

def text_styles_text_bg(e=None):
    background_color = colorchooser.askcolor()[1]

    if background_color:
        cur_tags = text_box.tag_names("sel.first")
        background_colors_font = font.Font(text_box,text_box.cget("font"))

        text_box.tag_configure("background_color",font=background_colors_font,background=background_color)

        if "background_color" in cur_tags:
            text_box.tag_remove("background_color","sel.first","sel.last")
        else:
            text_box.tag_add("background_color","sel.first","sel.last")

def text_styles_text_bg_all(e=None):
    background_color = colorchooser.askcolor()[1]

    if background_color:
        text_box.config(background=background_color)

def text_styles_font_size(e=None):
    top = Toplevel()
    top.title("Font Size")
    top.geometry("400x150")

    spin_box = Spinbox(top,from_=1,to=150,font=('Calibri',18))
    spin_box.pack(pady=20)

    def submit():
        text_box.config(font=("Calibri",int(spin_box.get())))

        top.destroy()
    
    submit_btn = Button(top,text="Submit!",command=submit)
    submit_btn.pack(pady=10)

def print_file(e=None):
    if FILE != EMPTY:
        save_file()
        win32api.ShellExecute(0,"print",FILE,None,".",0)

def select_all(e=None):
    text_box.tag_add("sel","1.0",END)

def night_mode(e=None):
    if is_night_mode.get():
        MAIN_COLOR = "black"
        SECOND_COLOR = "#373737"
        TEXT_COLOR = "white"

        root.config(bg=MAIN_COLOR)
        status_bar.config(bg=MAIN_COLOR,fg=TEXT_COLOR)
        text_box.config(bg=SECOND_COLOR,fg=TEXT_COLOR)

        file_menu.config(bg=SECOND_COLOR,fg=TEXT_COLOR)
        edit_menu.config(bg=SECOND_COLOR,fg=TEXT_COLOR)
        options_menu.config(bg=SECOND_COLOR,fg=TEXT_COLOR)
        text_styles_menu.config(bg=SECOND_COLOR,fg=TEXT_COLOR)
    else:
        MAIN_COLOR = "SystemButtonFace"
        SECOND_COLOR = "SystemButtonFace"
        TEXT_COLOR = "black"

        root.config(bg=MAIN_COLOR)
        status_bar.config(bg=MAIN_COLOR,fg=TEXT_COLOR)
        text_box.config(bg="white",fg=TEXT_COLOR)

        file_menu.config(bg=SECOND_COLOR,fg=TEXT_COLOR)
        edit_menu.config(bg=SECOND_COLOR,fg=TEXT_COLOR)
        options_menu.config(bg=SECOND_COLOR,fg=TEXT_COLOR)
        text_styles_menu.config(bg=SECOND_COLOR,fg=TEXT_COLOR)

# Create Main Frame
main_frame = Frame(root)
main_frame.pack(pady=5)

# Create Scroll Bar
scroll_bar = Scrollbar(main_frame)
scroll_bar.pack(side=RIGHT,fill=Y)

text_box = Text(main_frame,width=97,height=20,font=("Calibri",16),selectbackground="yellow",selectforeground="black",yscrollcommand=scroll_bar.set,undo=True)
text_box.pack()

scroll_bar.config(command=text_box.yview)

# Create Menu
menu = Menu(root)
root.config(menu=menu)

# Add File Menu
file_menu = Menu(menu,tearoff=False)
file_menu.add_command(label="New",command=new_file,accelerator="Ctrl+N")
file_menu.add_command(label="Open",command=open_file,accelerator="Ctrl+O")
file_menu.add_command(label="Save",command=save_file,accelerator="Ctrl+S")
file_menu.add_command(label="Save As",command=save_as_file,accelerator="Ctrl+Shift+S")
file_menu.add_separator()
file_menu.add_command(label="Print File",command=print_file,accelerator="Ctrl+P")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit,accelerator="Ctrl+Q")

# Add Edit Menu
edit_menu = Menu(menu,tearoff=False)
edit_menu.add_command(label="Cut",command=edit_cut,accelerator="Ctrl+X")
edit_menu.add_command(label="Copy",command=edit_copy,accelerator="Ctrl+C")
edit_menu.add_command(label="Paste",command=edit_paste,accelerator="Ctrl+V")

# Add Options Menu
horizontal_scroll_bar = BooleanVar()
horizontal_scroll_bar.set(False)

options_menu = Menu(menu,tearoff=False)

options_menu.add_command(label="Undo",command=text_box.edit_undo,accelerator="Ctrl+Z")
options_menu.add_command(label="Redo",command=text_box.edit_redo,accelerator="Ctrl+Y")

options_menu.add_separator()

options_menu.add_command(label="Select All",command=select_all,accelerator="Ctrl+A")
options_menu.add_command(label="Clear All",command=lambda e=None: text_box.delete(1.0,END),accelerator="Ctrl+Shift+C")

options_menu.add_separator()

is_night_mode = BooleanVar()
is_night_mode.set(False)

options_menu.add_checkbutton(label="Night Mode", onvalue=1, offvalue=0, variable=is_night_mode,command=night_mode)

# Add Text Styles
text_styles_menu = Menu(menu,tearoff=False)
text_styles_menu.add_command(label="Bold",command=text_styles_bold,accelerator="Ctrl+B")
text_styles_menu.add_command(label="Italics",command=text_styles_italics)

text_styles_menu.add_separator()

text_styles_menu.add_command(label="Change Font Size",command=text_styles_font_size,accelerator="Ctrl+F")

text_styles_menu.add_separator()

text_styles_menu.add_command(label="Text Color",command=text_styles_text_color,accelerator="Ctrl+T")
text_styles_menu.add_command(label="All Text Color",command=text_styles_text_color_all,accelerator="Ctrl+Shift+T")

text_styles_menu.add_separator()

text_styles_menu.add_command(label="Background Color",command=text_styles_text_bg,accelerator="Ctrl+G")
text_styles_menu.add_command(label="All Background Color",command=text_styles_text_bg_all,accelerator="Ctrl+Shift+G")

menu.add_cascade(label="File",menu=file_menu)
menu.add_cascade(label="Edit",menu=edit_menu)
menu.add_cascade(label="Options",menu=options_menu)
menu.add_cascade(label="Text Styles",menu=text_styles_menu)

# Add Status Bar
status_bar = Label(root,text="Ready...\t",anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=5)

# Key Bindings

# File
root.bind("<Control_L><n>",new_file)
root.bind("<Control_L><s>",save_file)
root.bind("<Control_L><Shift_L><s>",save_as_file)
root.bind("<Control_L><o>",open_file)
root.bind("<Control_L><q>",lambda e:root.quit())

# Edit
root.bind("<Control_L><c>",edit_copy)
root.bind("<Control_L><x>",edit_cut)
root.bind("<Control_L><v>",edit_paste)

# Options
root.bind("<Control_L><z>",text_box.edit_undo)
root.bind("<Control_L><y>",text_box.edit_redo)
root.bind("<Control_L><a>",select_all)
root.bind("<Control_L><Shift_L><c>",lambda e: text_box.delete(1.0,END))

# Text Styles
root.bind("<Control_L><b>",text_styles_bold)
root.bind("<Control_L><i>",text_styles_italics)

root.bind("<Control_L><f>",text_styles_font_size)

root.bind("<Control_L><t>",text_styles_text_color)
root.bind("<Control_L><Shift_L><t>",text_styles_text_color_all)

root.bind("<Control_L><g>",text_styles_text_bg)
root.bind("<Control_L><Shift_L><g>",text_styles_text_bg_all)

root.mainloop()