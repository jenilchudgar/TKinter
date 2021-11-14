from tkinter import *
from PIL import ImageTk,Image
import os

def forward(no):
    global label,forwardBtn,BackwardsBtn

    statusBar = Label(root,text=f"Image {no} of {len(images)}",bd=1,anchor=E)
    statusBar.grid(row=2,column=0,columnspan=3,sticky=W+E,padx=10)

    label.grid_forget()
    label = Label(image=images[no-1])
    label.grid(row=0,column=0,columnspan=3)
    forwardBtn = Button(root,text=">>",fg="blue",command=lambda:forward(no+1))
    BackwardsBtn = Button(root,text="<<",fg="blue",command=lambda:backward(no-1))

    if no == len(images):
        forwardBtn = Button(root,text=">>",fg="blue",state=DISABLED)

    forwardBtn.grid(row=1,column=2)
    BackwardsBtn.grid(row=1,column=0)

def backward(no):
    global label,forwardBtn,BackwardsBtn

    statusBar = Label(root,text=f"Image {no} of {len(images)}",bd=1,anchor=E)
    statusBar.grid(row=2,column=0,columnspan=3,sticky=W+E,padx=10)

    label.grid_forget()
    
    label = Label(image=images[no-1])
    label.grid(row=0,column=0,columnspan=3)
    forwardBtn = Button(root,text=">>",fg="blue",command=lambda:forward(no+1))
    BackwardsBtn = Button(root,text="<<",fg="blue",command=lambda:backward(no-1))

    if no == 1:
        BackwardsBtn = Button(root,text="<<",fg="blue",state=DISABLED)

    forwardBtn.grid(row=1,column=2)
    BackwardsBtn.grid(row=1,column=0)

root = Tk()
root.title("Window")
root.iconbitmap("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\application-blue.ico")
val = os.listdir("C:\\Users\\sanja\\Pictures\\Jenil\\")
images=[]

i=0
while True:
    try:
        currentStr = val[i]
        if (currentStr.endswith(".png") or currentStr.endswith(".jpg") or currentStr.endswith(".jpeg") or currentStr.endswith(".JPG")):
            images.append(ImageTk.PhotoImage(Image.open("C:\\Users\\sanja\\Pictures\\Jenil\\"+currentStr)))
        i+=1
    except:
        break

statusBar = Label(root,text=f"Image 1 of {len(images)}",bd=1,anchor=E)
statusBar.grid(row=2,column=0,columnspan=3,sticky=W+E,padx=10)
label = Label(root,image=images[0])
label.grid(row=0,column=0,columnspan=3)

exitBtn = Button(root,text="Exit",fg="red",command=root.quit)
exitBtn.grid(row=1,column=1)
forwardBtn = Button(root,text=">>",fg="blue",command=lambda:forward(2))
forwardBtn.grid(row=1,column=2,pady=10)
BackwardsBtn = Button(root,text="<<",fg="blue",command=backward,state=DISABLED)
BackwardsBtn.grid(row=1,column=0)
root.mainloop()