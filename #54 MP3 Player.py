from tkinter import *
import pygame

root = Tk()
root.title("MP3 Player")
root.iconbitmap("computer.ico")
root.geometry("600x400")

# Initialize Pygame Mixer
pygame.mixer.init()

# Create Playlist Box
song_box = Listbox(root,bg="black",fg="white",width=50)
song_box.pack(pady=20)

root.mainloop()