from tkinter import *
import pygame

root = Tk()
root.title("MP3 Player")
root.iconbitmap("computer.ico")
root.geometry("500x400")

# Initialize Pygame Mixer
pygame.mixer.init()

# Create Playlist Box
song_box = Listbox(root,bg="black",fg="white",width=50)
song_box.pack(pady=20)


# Define Player Control Images
back_img = PhotoImage(file="img/player/previous.png")
forward_img = PhotoImage(file="img/player/forward.png")
play_img = PhotoImage(file="img/player/play.png")
pause_img = PhotoImage(file="img/player/pause.png")
stop_img = PhotoImage(file="img/player/stop.png")

# Create Player Control Frame
control_frame = Frame(root)
control_frame.pack()

# Create Player Control Buttons
back_btn = Button(control_frame,image=back_img,borderwidth=0)
play_btn = Button(control_frame,image=play_img,borderwidth=0)
pause_btn = Button(control_frame,image=pause_img,borderwidth=0)
stop_btn = Button(control_frame,image=stop_img,borderwidth=0)
forward_btn = Button(control_frame,image=forward_img,borderwidth=0)

forward_btn.grid(row=0,column=0,padx=10)
play_btn.grid(row=0,column=1,padx=10)
pause_btn.grid(row=0,column=2,padx=10)
stop_btn.grid(row=0,column=3,padx=10)
back_btn.grid(row=0,column=4,padx=10)

root.mainloop()