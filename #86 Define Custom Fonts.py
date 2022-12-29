from tkinter import *
from tkinter.font import Font

NORMAL = "normal"
ROMAN = "roman"
BOLD   = "bold"
ITALIC = "italic"

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

bigFont = Font(
    family="Pacifico",
    size=40,
    weight=BOLD,
    underline=False,
    slant=ROMAN,
    overstrike=True,
)

hi = Label(root,text="LOL",font=bigFont)
hi.pack(pady=10)

root.mainloop()
