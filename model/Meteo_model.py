import requests

API_KEY = '083fc7320895785e9e01400993070cd3'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

class WeatherModel:
    def get_weather_info(self, name, lat, lon):
        complete_url = f"{'http://api.openweathermap.org/data/2.5/weather?'}lat={lat}&lon={lon}&appid={'083fc7320895785e9e01400993070cd3'}&units=metric"
        response = requests.get(complete_url)
        data = response.json()
        if data['cod'] == 200:
            main = data.get('main', {})
            wind = data.get('wind', {})
            clouds = data.get('clouds', {})
            temp = main.get('temp', 'N/A')
            wind_speed = wind.get('speed', 'N/A')
            wind_deg = wind.get('deg', 'N/A')
            cloudiness = clouds.get('all', 'N/A')
            info = f"{name}\nTemp: {temp}°C\nWind: {wind_speed} m/s\nDirection: {wind_deg}°\nCloudiness: {cloudiness}%"
            return info
        else:
            print(f"Erreur : Impossible de récupérer les données pour {name}. Réponse API : {data}")
            return f"{name}\nData not available"
