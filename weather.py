import requests
api="467286722ee449f9b8c35424262305"
city=input("Enter a city name: ")
url= f"http://api.weatherapi.com/v1/current.json?key={api}&q={city}&aqi=no"
response= requests.get(url)
data=response.json()
print(f"The data for the location{"location"} is as follows:")
print(data,"\n")
print(f"Temp in jaipur in farenh is: {data["current"]["temp_f"]}")
print(f"Temp in jaipur in celcius is: {data["current"]["temp_c"]}")
print(f"Last updated {data["current"]["last_updated"]}")
