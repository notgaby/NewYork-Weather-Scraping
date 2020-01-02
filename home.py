"""

Hello everu1! i am very bored, and  so i am going to *attempt* to make something cool

this is my explore nyc tool bc we r going to new york soon and i bored

features
A. Enter your location in new york
B. Random option - when ur bored

1) check weather
2) check very gud food places
3) local news (?)
4) tourist attraction

"""


#####################

import weather
import food

def getWeather():
    weather_Window = tk.Toplevel(master)
    weather_Window.title("Weather")

    #weather_Window.geometry("500x500")
    #weather_Window.configure(background = 'white')

    canvas = tk.Canvas(weather_Window, width = 500, height = 500, bg = '#B9D8D6')
    canvas.pack()

    canvas.create_text(250, 15, fill = "black", text = "DATE ★ WHEN ★ TEMP (HIGH/LOW) ★ PRECIPITATION (%) ★ HUMIDITY (%) ")

    xVal = 250
    yVal = 45

    for i in range(15):
        append = weather.get_dates()[i] + ' ★ ' + weather.get_days()[i] + ' ★ ' + weather.get_temps()[i] + ' ★ ' + weather.get_precip()[i] + ' ★ ' + weather.get_humidity()[i]
        canvas.create_text(xVal,yVal,fill = "black", text = append)
        yVal+= 30



"""




    for i in range(len(weather.get_dates())):
        print(weather.get_dates()[i])
        print(weather.get_days()[i])
        print(weather.get_temps()[i])


    h = 15
    w = 3
    for i in range(h):
        for j in range(w):
            b = tk.Entry(weather_Window,text="")
            b.grid(row=i, column=j)
"""



def getFood():
    food_Window = tk.Toplevel(master)
    food_Window.title("Food")

    food_Canvas = tk.Canvas(food_Window, width = 500, height = 500, bg = '#C9B9D8')
    food_Canvas.pack()

    listbox = tk.Listbox(food_Window)
    listbox.pack()

    places = ["New York", "Queens", "Manhattan", "Brooklyn", "Staten Island"]
    for item in places:
        listbox.insert(tk.END, item)



def getAttractions():
    attractions_Window = tk.Toplevel(master)
    attractions_Window.title("Attractions")

    attractions_Canvas = tk.Canvas(attractions_Window, width = 500, height = 500, bg = '#BFD8B9')
    attractions_Canvas.pack()

#####################

import tkinter as tk

master = tk.Tk()
master.title("New York")
master.geometry("300x250")
master.configure(background = '#D8B9D1')

#text = tk.Text(master, height = 0, width = 30)
#text.insert('1.0',"Explore New York")
explore = tk.Label(master, text = "Explore New York").place(x = 100, y = 0)

weatherBut = tk.Button(master, text = "Weather", command = getWeather).place(x = 100, y = 80)
food = tk.Button(master, text = "Food", command = getFood).place(x = 100, y = 110)
attractions = tk.Button(master, text = "Attractions", command = getAttractions).place(x = 100, y = 140)


#explore.pack()
master.mainloop()

