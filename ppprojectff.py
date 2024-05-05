from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a7e8aa07d53269e41e4970d60d352021"
    response = requests.get(url)
    data = response.json()
    print(data)  # Print the API response to see its structure
    try:
        w_label1.config(text=data["weather"][0]["main"])
        wb_label1.config(text=data["weather"][0]["description"])
        temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)))
        per_label1.config(text=data["main"]["pressure"])
    except KeyError as e:
        print(f"KeyError: {e}")
        w_label1.config(text="Wrong City")
        wb_label1.config(text="Wrong City")
        temp_label1.config(text="Wrong City")
        per_label1.config(text="Wrong City")

win = Tk()
win.title("Weather")
win.config(bg="lightblue")
win.geometry("500x580")

# Creating app title
name_label = Label(win, text="Enter The City Name", font=("Courier new", 15, "bold"),bg="lightblue")
name_label.place(x=25, y=70, height=50, width=450)

city_name = StringVar()
# Creating list of city
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]
com = ttk.Combobox(win, text=" Weather App", values=list_name, font=("Calibri", 15, "normal"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

w_label = Label(win, text="Weather Climate", font=("times new Roman", 12, "bold"),bg="lightblue")
w_label.place(x=80, y=260, height=50, width=150)
w_label1 = Label(win, text="", font=("times new Roman", 12, "bold"))
w_label1.place(x=250, y=260, height=50, width=150)

wb_label = Label(win, text="Weather Description", font=("times new Roman", 12, "bold"),bg="lightblue")
wb_label.place(x=80, y=330, height=50, width=150)
wb_label1 = Label(win, text="", font=("times new Roman", 12, "bold"))
wb_label1.place(x=250, y=330, height=50, width=150)

temp_label = Label(win, text="Temperature", font=("times new Roman", 12, "bold"),bg="lightblue")
temp_label.place(x=80, y=400, height=50, width=150)
temp_label1 = Label(win, text="", font=("times new Roman", 12, "bold"))
temp_label1.place(x=250, y=400, height=50, width=150)

per_label = Label(win, text="Pressure", font=("times new Roman", 12, "bold"),bg="lightblue")
per_label.place(x=80, y=470, height=50, width=150)
per_label1 = Label(win, text="", font=("times new Roman", 12, "bold"))
per_label1.place(x=250, y=470, height=50, width=150)

# Creating Fetch button
done_button = Button(win, text="Get", font=("Courier new", 20, "bold"), bg="lightblue",command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()
