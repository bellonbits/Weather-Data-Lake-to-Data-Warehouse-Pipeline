# scripts/fetch_weather.py
import requests, json, os
from datetime import datetime

API_KEY = "8f7c039d18fc20fade3dcca7a8fe1693"
CITY = "Nairobi"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

# Fix timestamp for filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"weather_{timestamp}.json"

# Ensure the directory exists
os.makedirs(".", exist_ok=True)

# Save the file
with open(filename, "w") as f:
    json.dump(data, f)

print(f"Saved weather data to {filename}")