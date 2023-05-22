from tkinter import *
from bs4 import BeautifulSoup
from urllib import request
import urllib
from datetime import datetime
from urllib.request import Request, urlopen

# Get Time
global cur_time,now
now = datetime.now()
cur_time = now.strftime("%I:%M:%S %p")

root = Tk()
root.title("Python")
root.iconbitmap("computer.ico")
root.geometry("650x210")
root.config(bg="black")

global previous
previous = False

# Create A Frame
frame = Frame(root,bg="black")
frame.pack(pady=20)

# Create A Logo
logo = PhotoImage(file="img\\bitcoin.png")
logo_label = Label(frame,image=logo,bd=0)
logo_label.grid(row=0,column=0,rowspan=2)

# Add Bitcoin Price Label
bitcoin_label = Label(frame,text="TEST LOL",
                      font=("ComicSansMS",45),
                      bg="black",
                      fg="green",
                      bd="0"
                )
bitcoin_label.grid(row=0,column=1,padx=20,sticky=S)

# Latest Price -> Up/Down
latest_price = Label(frame,text="Unchanged",
                     font=("ComicSansMS",10),
                    bg="black",
                    fg="Grey",
                    bd=0
                )
latest_price.grid(row=1,column=1,sticky=N)

# Grab the Bitcoin
def Update():
    global previous
    
    req1 = Request(
        url='https://www.coindesk.com/price/bitcoin/', 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    page1 = urlopen(req1)

    req2 = Request(
        url='https://www.google.com/finance/quote/USD-INR', 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    page2 = urlopen(req2)


    # Grab Price
    html1 = BeautifulSoup(page1,"html.parser")
    price1 = html1.find(class_="currency-pricestyles__Price-sc-1rux8hj-0")
    price1 = str(price1)
    price1 = price1[62:71]
    price1 = price1.replace(",","")
    print(price1)

    # Grab Rupee
    html2 = BeautifulSoup(page2,"html.parser")
    price2 = html2.find(class_="fxKbKc")
    price2 = str(price2)
    price2 = price2[27:34]
    price2 = price2.replace(",","")
    print(price2)
    
    current = float(price1) * float(price2)

    # Update Label
    bitcoin_label.config(text=f"₹ {round(float(current),3)}")

    # Get Time
    global cur_time,now
    now = datetime.now()
    cur_time = now.strftime("%I:%M:%S %p")
    status_bar.config(text=f"Last Updated {cur_time}")

    if previous:
        if float(previous) > float(current):
            latest_price.config(text=f"Price Down {round(float(previous)-float(current),2)}",fg="red")
        elif float(previous) < float(current):
            latest_price.config(text=f"Price Up {round(float(current)-float(previous),2)}",fg="green")
        elif float(previous) == float(current):
            latest_price.config(text="Price Unchanged",fg="grey")
        else:
            previous = current 
            latest_price.config(text="Price Unchanged",fg="grey")

    # Set Timmer to 1/2 minute
    root.after(1000*30,Update)


# Create Status Bar
status_bar = Label(root,text=f"Last Updated {cur_time}",bd=0,anchor=E,bg="black",fg="grey")
status_bar.pack(fill=X,side=BOTTOM,ipadx=10)


# On Program Start
Update()

root.mainloop()