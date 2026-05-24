import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("cryptoapi_key")
cryptoname=(input("Enter crypto currency: ")).upper()

url = f"https://api.freecryptoapi.com/v1/getData?token={api_key}&symbol={cryptoname}"

response = requests.get(url)
data = response.json()

# print(data)
print(f"{cryptoname} last in USD was {data["symbols"][0]['last']}")
print(f"{cryptoname} lowest in USD was {data["symbols"][0]['lowest']}")
print(f"{cryptoname} highest in USD was {data["symbols"][0]['highest']}")
print(f"{cryptoname} source exchange was {data["symbols"][0]['source_exchange']}")
print(f"Timestamp: {data["symbols"][0]['date']}")