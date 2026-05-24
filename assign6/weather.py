# 1) Study the open weather API show more data in your API calling program
import os
import requests
from dotenv import load_dotenv

load_dotenv()

api= os.getenv("weatherapi_key")

city=input("Enter a city name: ")
url= f"http://api.weatherapi.com/v1/current.json?key={api}&q={city}&aqi=no"
response= requests.get(url)
data=response.json()
print(f"The data for the location{"location"} is as follows:")
print(data,"\n")
print(f"Temp in {city} in farenh is: {data["current"]["temp_f"]}")
print(f"Temp in {city} in celcius is: {data["current"]["temp_c"]}")
print(f"Last updated {data["current"]["last_updated"]}")
