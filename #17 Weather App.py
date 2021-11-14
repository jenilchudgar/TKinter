import requests
import json
from tkinter import *

root = Tk()
root.title("Weather App")
root.iconbitmap("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\weather_clear.ico")
root.geometry("250x250")

def sub():
    global l,f
    root.geometry("250x250")
    l.configure(fg="black")
    try:
        key = "1c5db216226498b1929fe76f2ed0f186"
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={entryBox.get()}&appid={key}"
        lat,lon = 0,0

        api = json.loads(requests.get(url).content)
        lat,lon = api[0]['lat'],api[0]['lon']
        name = api[0]['name']
        country = api[0]['country']

        
        url = f"https://restcountries.eu/rest/v2/alpha/{country}"
        api = json.loads(requests.get(url).content)
        country = api['name']

        url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid={key}"

        api = json.loads(requests.get(url).content)
        temp = f"{api['current']['temp']}°C"
        description = api['current']['weather'][0]['description']

        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={key}"

        indexes = {
            1:"Green",
            2:"Yellow",
            3:"Yellow",
            4:"Orange",
            5:"Red"
        }

        api = json.loads(requests.get(url).content)
        index = (api['list'][0]['main']['aqi'])
        root.configure(bg=indexes[index])
        if country=="United Kingdom of Great Britain and Northern Ireland":
            country = "United Kingdom of\nGreat Britain and\nNorthern Ireland"
            root.geometry("250x300")
        l.configure(text=f"{name} {country}\n{temp}\n{description.title()}\nAQI = {index}" if len(name+country)<20 else f"{name}\n{country}\n{temp}\n{description.title()}\nAQI = {index}",font=('Calibri',18))
        entryBox.delete(0,END)
        l.grid(row=2,column=0)
    
    except Exception as e:
        print(e)
        l.configure(text="Error!",fg="red",font=("Calibri",18))
        l.grid(row=2,column=0)


entryBox = Entry(root,font=("Calibri",16),width=22)
entryBox.grid(row=0,column=0)

sumbit = Button(root,text="Submit!",font=("Calibri",16),command=sub)
sumbit.grid(row=1,column=0)

global l,f
l = Label(root)
f = Label(root)
root.mainloop()