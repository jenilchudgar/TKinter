from tkinter import *
import pygame

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("400x400")

pygame.mixer.init()

def play_sound():
    pygame.mixer.music.load("audio\cheer.mp3")    
    pygame.mixer.music.play(loops=0)

def stop_sound():
    pygame.mixer.music.stop()

play_btn = Button(root,text="Play Music!",command=play_sound,font=('Calibri',20))
play_btn.pack(pady=10)

stop_btn = Button(root,text="Stop Music!",command=stop_sound,font=('Calibri',20))
stop_btn.pack(pady=10)


root.mainloop()