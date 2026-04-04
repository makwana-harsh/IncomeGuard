import requests

API_KEY = "your_api_key"

def get_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    rain = 0
    if "rain" in data:
        rain = data["rain"].get("1h", 0)

    temperature = data["main"]["temp"]

    return {
        "rain": rain,
        "temperature": temperature
    }