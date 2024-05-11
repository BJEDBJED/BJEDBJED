import requests
import json
import tkinter as tk
from tkinter import messagebox
import os

API_KEY = os.environ.get('API_KEY')

class JSONFabric:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return json.dumps(self.data)

class PlainFabric:
    def __init__(self, data):
        self.data = data

    def generate(self):
        weather_description = self.data.get('weather')[0].get('description')
        temperature = self.data.get('main').get('temp')
        humidity = self.data.get('main').get('humidity')
        wind_speed = self.data.get('wind').get('speed')

        report_text = (
            f"Weather: {weather_description}\n"
            f"Temperature: {temperature} °C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
        return report_text

class ReportFabric:
    def get_report(self, rtype, data):
        if rtype == 'JSON':
            return JSONFabric(data)
        elif rtype == 'Plain':
            return PlainFabric(data)
        else:
            return None

def get_weather_data(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    full_url = f"{url}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(full_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching weather data: {e}")
        return None

def generate_report(city, type_report, text_widget):
    data = get_weather_data(city)
    if data is not None:
        factory = ReportFabric()
        report = factory.get_report(type_report, data)
        generated_report = report.generate()
        text_widget.config(state=tk.NORMAL)
        text_widget.delete(1.0, tk.END)  # Clear previous content
        text_widget.insert(tk.END, f"Generated Report for {city}:\n\n{generated_report}")
        text_widget.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    root.title("Weather Report Generator")

    city_label = tk.Label(root, text="Enter city:")
    city_label.pack()

    city_entry = tk.Entry(root)
    city_entry.pack()

    type_label = tk.Label(root, text="Report type (JSON/Plain):")
    type_label.pack()

    type_entry = tk.Entry(root)
    type_entry.pack()

    report_text = tk.Text(root, height=15, width=50, state=tk.DISABLED)
    report_text.pack()

    generate_button = tk.Button(root, text="Generate Report",
                                command=lambda: generate_report(city_entry.get(), type_entry.get(), report_text))
    generate_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()