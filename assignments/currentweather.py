# Assignment:
# Using the URL below
# https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m
# Write a python program called currentweather.py that will print out the current temperature on the console (and only the temperature)
# I have set the lat/long to my location, you may use that or a different location.
# Last few marks, also print out wind direction (10m)


import requests
import json

url = 'https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m'
response = requests.get(url)
#print(response.json())

data = response.json()

current = data['current']
#print(current)
temperature = current['temperature_2m']

units = data['current_units']
degrees = units['temperature_2m']

print(temperature,degrees)

# Use this link for Wind speed: https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=wind_speed_10m&forecast_days=1
# Above link gives speed forecast for current day.
# Will need to get current time to get closest value.
