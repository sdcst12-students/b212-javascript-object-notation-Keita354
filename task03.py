#Use the Weather API builder at https://open-meteo.com/en/docs
# to generate an API call for a city. We are going to make use 
#of the REQUESTS.Request method to retrieve this data and unpack 
#it with json.loads into a variable that we can use. Retrieve the 
#data and present it in a more organized format. You may use text
# output or a window using Tkinter.  Our goal is to format the
# result in a reasonably organized format.


from urllib.parse import urlparse, parse_qs
import requests
import json
import tkinter as tk

latitude = 49.2827
longitude = -123.1207
api_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&timezone=America%2FLos_Angeles'

def get_weather_data():
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = json.loads(response.text)
            result_label.config(text=f"Weather forecast for Vancouver:\n")  
            hourly_data = data.get('hourly', {})
            
            if hourly_data:
                time = hourly_data.get('time', [])
                temperatures = hourly_data.get('temperature_2m', [])
                
                if len(time) == len(temperatures):
                    weather_data = {}  
                    current_day = None
                    
                    for i in range(len(time)):
                        day, formatted_time = time[i].split("T")
                        if day not in weather_data:
                            weather_data[day] = []
                            current_day = day
                        weather_data[current_day].append(f"Time: {formatted_time}, Temperature: {temperatures[i]}°C")
                    

                    for day, data in weather_data.items():
                        day_button = tk.Button(window, text=f"Day {day}", command=lambda d=day: display_weather_data(d, weather_data))
                        day_button.pack()
                    
                else:
                    result_label.config(text="Mismatched data: time and temperature arrays have different lengths.")
            else:
                result_label.config(text="Hourly data not found in the response.")
        else:
            result_label.config(text=f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Request error: {e}")

def display_weather_data(day, weather_data):
    if day in weather_data:
        selected_data = "\n".join(weather_data[day])
        weather_textbox.config(state="normal")
        weather_textbox.delete(1.0, "end")
        weather_textbox.insert("end", selected_data)
        weather_textbox.config(state="disabled")

window = tk.Tk()
window.title("Vancouver")  # Set window title to "Vancouver"
window.title("Weather Forecast")

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

weather_textbox = tk.Text(window, wrap=tk.WORD, width=40, height=10, state="disabled")
weather_textbox.pack()

fetch_button = tk.Button(window, text="Fetch Weather Data", command=get_weather_data)
fetch_button.pack(pady=10)

window.mainloop()
