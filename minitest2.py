import requests
from datetime import datetime, timedelta

# Ganti dengan API key Anda
API_KEY = "ff4a16c174d6df14df88178c6289f25a"

# Endpoint URL untuk ramalan cuaca 5 hari ke depan di Jakarta
endpoint = f"http://api.openweathermap.org/data/2.5/forecast?q=Jakarta,id&units=metric&cnt=40&appid={API_KEY}"

response = requests.get(endpoint)

if response.status_code == 200:
    data = response.json()
    daily_temperatures = {}
    
    for entry in data['list']:
        timestamp = entry['dt']
        temperature = entry['main']['temp']
        date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
        
        if date not in daily_temperatures:
            daily_temperatures[date] = temperature
    
    print("Ramalan Cuaca Kota Jakarta untuk 5 hari ke depan:")
    for date, temperature in daily_temperatures.items():
        print(f"{date}: {temperature}°C")
else:
    print("Gagal mengambil data cuaca.")
