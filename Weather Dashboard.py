import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city):
    # Make API call
    api_key = "YOUR_API_KEY"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        return weather_info
    else:
        return None

def show_weather():
    city = city_entry.get()
    weather_info = get_weather(city)
    
    if weather_info:
        temp_label.config(text=f"Temperature: {weather_info['temperature']}°C")
        humidity_label.config(text=f"Humidity: {weather_info['humidity']}%")
        description_label.config(text=f"Weather: {weather_info['description']}")
    else:
        messagebox.showerror("Error", "City not found. Please check the city name.")

# Set up GUI
root = tk.Tk()
root.title("Weather Dashboard")

# City input
city_label = tk.Label(root, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

search_button = tk.Button(root, text="Search", command=show_weather)
search_button.pack()

# Weather info labels
temp_label = tk.Label(root, text="Temperature: --°C")
temp_label.pack()

humidity_label = tk.Label(root, text="Humidity: --%")
humidity_label.pack()

description_label = tk.Label(root, text="Weather: --")
description_label.pack()

root.mainloop()
