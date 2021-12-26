from tkinter import filedialog
from mutagen.mp3 import MP3
from tkinter import *
import pygame
import time

root = Tk()
root.title("MP3 Player")
root.iconbitmap("computer.ico")
root.geometry("500x400")

# Create Song Dictorinary
global song_dict,paused

song_dict = {}
paused = False

# Functions
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/',title="Choose a Song...",filetypes=(("mp3 Files","*.mp3"),("wav Files","*.wav")))

    # Remove Directory and replace file extensions with nothing
    song_new = song.split("/")[-1].replace(".mp3","").replace(".wav","")

    # Add song to song dict
    song_dict[song_new] = song

    # Add song to Listbox
    song_box.insert(END,song_new)

def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/',title="Choose Many Songs...",filetypes=(("mp3 Files","*.mp3"),("wav Files","*.wav")))

    for song in songs:
        # Remove Directory and replace file extensions with nothing
        song_new = song.split("/")[-1].replace(".mp3","").replace(".wav","")

        # Add song to song dict
        song_dict[song_new] = song

        # Add song to Listbox
        song_box.insert(END,song_new)

def play():
    global paused
    song = song_box.get(ACTIVE)
    pygame.mixer.music.load(song_dict[song])
    pygame.mixer.music.play(loops=0)

    play_time()

    paused = False

def stop():
    global paused
    song_box.selection_clear(0,END)
    pygame.mixer.music.stop()

    status_bar.config(text="")

    paused = True

def pause(is_paused):
    global paused

    paused = is_paused
    
    if paused:
        # Unpause
        pygame.mixer.music.unpause()
        paused = False

    else:
        # Pause
        pygame.mixer.music.pause()
        paused = True

def forward():
    global paused

    next_song = song_box.curselection()[0] + 1

    if song_box.size() == next_song:
        next_song = 0

    song_box.selection_clear(0,END)
    song_box.activate(next_song)
    song_box.selection_set(next_song)

    pygame.mixer.music.load(song_dict[song_box.get(next_song)])
    pygame.mixer.music.play(loops=0)

    play_time()

    paused = False

def back():
    global paused
    
    pre_song = song_box.curselection()[0] - 1

    if pre_song == 0-1:
        pre_song = song_box.size()-1

    song_box.selection_clear(0,END)
    song_box.activate(pre_song)
    song_box.selection_set(pre_song)

    pygame.mixer.music.load(song_dict[song_box.get(pre_song)])
    pygame.mixer.music.play(loops=0)

    play_time()

    paused = True

def delete():
    song_box.delete(ANCHOR)
    stop()

def delete_all():
    song_box.delete(0,END)
    stop()

def play_time():
    current_time = pygame.mixer.music.get_pos() / 1000

    converted_time = time.strftime("%M:%S",time.gmtime(current_time))

    # cur_song = song_box.curselection()
    song = song_dict[song_box.get(ACTIVE)]

    song_mut = MP3(song)
    song_len = song_mut.info.length

    converted_total_time = time.strftime("%M:%S",time.gmtime(song_len))
    print(current_time,song_len)
    if current_time == -0.001:
        status_bar.config(text="")
    elif current_time < song_len:
        status_bar.config(text=f"{converted_time} of {converted_total_time}")
        status_bar.after(1000,play_time)
    else:
        status_bar.config(text="")

# Initialize Pygame Mixer
pygame.mixer.init()

# Create Playlist Box
song_box = Listbox(root,bg="black",fg="yellow",width=50,font=('Calibri',12),selectbackground="silver",selectforeground="blue")
song_box.pack(pady=20)


# Define Player Control Images
back_img = PhotoImage(file="img/player/back.png")
forward_img = PhotoImage(file="img/player/forward.png")
play_img = PhotoImage(file="img/player/play.png")
pause_img = PhotoImage(file="img/player/pause.png")
stop_img = PhotoImage(file="img/player/stop.png")

# Create Player Control Frame
control_frame = Frame(root)
control_frame.pack()

# Create Player Control Buttons
back_btn = Button(control_frame,image=back_img,borderwidth=0,command=back)
play_btn = Button(control_frame,image=play_img,borderwidth=0,command=play)
pause_btn = Button(control_frame,image=pause_img,borderwidth=0,command=lambda: pause(paused))
stop_btn = Button(control_frame,image=stop_img,borderwidth=0,command=stop)
forward_btn = Button(control_frame,image=forward_img,borderwidth=0,command=forward)

back_btn.grid(row=0,column=0,padx=10)
play_btn.grid(row=0,column=1,padx=10)
pause_btn.grid(row=0,column=2,padx=10)
stop_btn.grid(row=0,column=3,padx=10)
forward_btn.grid(row=0,column=4,padx=10)

# Create Menu
main_menu = Menu(root)
root.config(menu=main_menu)

# Create Add Song Menu
add_song_menu = Menu(main_menu)
add_song_menu.add_command(label="Add One Song",command=add_song)
add_song_menu.add_command(label="Add Many Songs",command=add_many_songs)

# Create Delete Song Menu
delete_song_menu = Menu(main_menu)
delete_song_menu.add_command(label="Delete a Song",command=delete)
delete_song_menu.add_command(label="Delete all Songs",command=delete_all)

main_menu.add_cascade(label="Add Songs",menu=add_song_menu)
main_menu.add_cascade(label="Delete Songs",menu=delete_song_menu)

# Create Status Bar
status_bar = Label(root,text="",font=("Calibri",15),anchor=E,relief=SUNKEN,bd=1)
status_bar.pack(fill=X,side=BOTTOM,ipady=2)

root.mainloop()