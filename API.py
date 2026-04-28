import requests #give python access to the internet

API_key = "831bcc60123e44bf868c2ae62826bcd7" #API key from the weather website

def get_weather(city):
  response requests.get('https://api.openweathermap.org/data/2.5/weather') # tell python to get the data from that URL

params={              #settings that we send to the API to tell it exactly what info we want"
  "q": city,          # q for query (request of info)
  "appid": API_key,   # inserting the API_key to show that we have permission
  "units": "metric"   # celsius
}

  

    





















def get_weather(city):
    """Fetch current weather for a given city from OpenWeatherMap API"""
    
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            "q": city,
            "appid": API_KEY,
            "units": "metric"  # gives Celsius
        }
    )
    
    if response.status_code == 200:
        raw = response.json()
        return {
            "temp": raw["main"]["temp"],
            "humidity": raw["main"]["humidity"],
            "description": raw["weather"][0]["description"],
            "wind_speed": raw["wind"]["speed"]
        }
    else:
        return None  # city not found or API error
