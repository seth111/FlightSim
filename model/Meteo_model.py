import requests

API_KEY = '42625c80eac0732a957e728cfdaf3d35'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

AIRPORTS = {
    'Heathrow': (51.470020, -0.454295),
    'JFK': (40.641311, -73.778139),
    'Narita': (35.771987, 140.392850),
    'Charles de Gaulle': (49.009690, 2.547924),
    'Sheremetyevo': (55.972642, 37.414589),
}

class WeatherModel:
    def get_weather_info(self, name, lat, lon):
        complete_url = f"{'http://api.openweathermap.org/data/2.5/weather?'}lat={lat}&lon={lon}&appid={'42625c80eac0732a957e728cfdaf3d35'}&units=metric"
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
