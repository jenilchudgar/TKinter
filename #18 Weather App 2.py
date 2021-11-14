import requests
import json
from tkinter import *

root = Tk()
root.title("Weather App")
root.iconbitmap("C:\\Users\\sanja\\Desktop\\Extra\\Dowloads Folder\\weather_clear.ico")

def sub():
    global l
    url = f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={entryBox.get()}&distance=2&API_KEY=6641AD34-D311-464C-A707-31DB31A316E4"

    try:
        api = json.loads(requests.get(url).content)
        quality_dict = {
            1:'Green',
            2:'Yellow',
            3:'Yellow',
            4:'Orange',
            5:'Orange',
            6:'Red',
            7:'White'
        }

        area = api[0]['ReportingArea']
        print(api[0]['Category']['Number'])
        category = quality_dict[api[0]['Category']['Number']]
        category_name = api[0]['Category']['Name']
        quality = api[0]['AQI']

        l.configure(text=f"Area: {area}\tCategory: {category_name}\nQuality: {quality}",font=("Times",20),bg=category)
        l.grid(row=2,column=0)

    except:
        l.configure(text="Error",font=("Calibri",14),fg="Red",bg="white")
        l.grid(row=2,column=0)


entryBox = Entry(root,font=("Calibri",16))
entryBox.grid(row=0,column=0)

sumbit = Button(root,text="Submit!",font=("Calibri",16),command=sub)
sumbit.grid(row=1,column=0)

global l
l = Label(root)

root.mainloop()