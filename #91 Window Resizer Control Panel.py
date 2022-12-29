from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x700")

def launch_win():
    global sec
    sec = Toplevel()

    sec.geometry("200x200")

# Change The Width
def width_slide(e):
    sec.geometry(f"{int(width_slider.get())}x{int(height_slider.get())}")

# Change The Height
def height_slide(e):
    sec.geometry(f"{int(width_slider.get())}x{int(height_slider.get())}")
# Change Botg
def both_slide(e):
    sec.geometry(f"{int(both_slider.get())}x{int(both_slider.get())}")
    pass



launch_btn = Button(root,text="Lauch New Window!",command=launch_win)
launch_btn.pack(pady=10)

# Create a Label Frame
width_frame = LabelFrame(root,text="Width")
width_frame.pack(pady=10)

height_frame = LabelFrame(root,text="Height")
height_frame.pack(pady=10)

both_frame = LabelFrame(root,text="Both")
both_frame.pack(pady=10)

# Create Some Slidders
width_slider = ttk.Scale(width_frame,from_=100,to=1000,orient=HORIZONTAL,length=200,command=width_slide,value=100)
width_slider.pack(pady=10,padx=10)

height_slider = ttk.Scale(height_frame,from_=100,to=1000,orient=VERTICAL,length=200,command=height_slide,value=100)
height_slider.pack(pady=10,padx=10)

both_slider = ttk.Scale(both_frame,from_=100,to=1000,orient=VERTICAL,length=200,command=both_slide,value=100)
both_slider.pack(pady=10,padx=10)

root.mainloop()