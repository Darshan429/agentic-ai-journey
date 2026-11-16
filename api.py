import requests

def get_temprature(latitude,longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data['current']['temperature_2m']

paris_temp = get_temprature(48.85,2.35)
london_temp = get_temprature(51.50,0.12)
tokyo_temp = get_temprature(35.67,139.65)

print(f"Paris Temp: {paris_temp}°C")
print(f"London Temp: {london_temp}°C")
print(f"Tokyo Temp: {tokyo_temp}°C")