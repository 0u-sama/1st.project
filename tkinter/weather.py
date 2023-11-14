from tkinter import *
import requests
import json

# function zip_search


root = Tk()
root.title("weather")
root.geometry("400x100")

search_box = Entry(root)
search_box.grid(row=0, column=0)


# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=C5AEFA9C-5A75-4AC8-A597-E31E7A6377B7

def zip_search():
    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + search_box.get() + "&distance=25&API_KEY=C5AEFA9C-5A75-4AC8-A597-E31E7A6377B7")

        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = str(api[0]['AQI'])
        category = api[0]['Category']['Name']

        if category == "Good":
            app_color = "#0C0"
        elif category == "Moderate":
            app_color = "#FF0000"
        elif category == "Unhealthy for Sensitive Groups":
            app_color = "#ff9900"
        elif category == "Unhealthy":
            app_color = "#990066"
        elif category == "Hazardous":
            app_color = "#660000"
        Label(root, text="City: " + city + "\n" + "Air quality: " + quality + "\n" + category, font=("Helvetica", 10),
              background=app_color, padx=30).grid(row=1, column=1, columnspan=2)
        root.configure(background="white")
    except Exception as e:
        Label(root, text="error").grid(row=1, column=0, columnspan=2)


search_button = Button(root, text="search by zip_code", command=zip_search)
search_button.grid(row=0, column=1)


root.mainloop()
