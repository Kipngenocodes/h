import json
from tkinter import *

import requests

main_window = Tk()
main_window.title("Working With  API")
main_window.geometry("500x500")


'''
https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=83605&distance=500&API_KEY=090F6EAB-9668-4F3A-8FC4-F0C60170C063
'''
try:
    api_req = requests.get(
        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=83605&distance=500&API_KEY=090F6EAB-9668-4F3A-8FC4-F0C60170C063")
    api = json.loads(api_req.content)
    Reportingarea = api[0]['ReportingArea']
    category = api[0]['Category']['Name']
    AQI = api[0]['AQI']

    if category == "Good":
        weather_color = "#00e400"
    elif category == "Moderate":
        weather_color = "#ffff00"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = "#ff7e00"
    elif category == "Unhealthy":
        weather_color = "#ff0000"
    elif category == "Very Unhealthy":
        weather_color = "#8f3f97"
    elif category == "Hazardous":
        weather_color = "#7e0023"
    main_window.config(background=weather_color)
except Exception as e:
    api = "Error occured while executing request"

myLabel = Label(main_window,
                text='City: ' + Reportingarea + '\n' + 'Category: ' + category + "\n" + "Air Quality: " + str(AQI),
                font=("Arial"), background=weather_color)
myLabel.pack()

main_window.mainloop()
