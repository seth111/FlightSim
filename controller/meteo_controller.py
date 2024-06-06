import json
from model.Meteo_model import WeatherModel
from view.meteo_view import MeteoMap

class MeteoController:
    def __init__(self, airport_data_path):
        self.airport_data_path = airport_data_path
        self.airports = self.load_airports()
        self.weather_model = WeatherModel()

    def load_airports(self):
        with open(self.airport_data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['airports']

    def get_airports_weather(self):
        for airport in self.airports:
            lat = airport['lat']
            lon = airport['lon']
            weather_info = self.weather_model.get_weather_info(lat, lon)
            airport['weather'] = weather_info
            
    def plot_airports(self):
        self.get_airports_weather()
        MeteoMap.plot_airports(self.airports)

def main():
    airport_data_path = "airports.json"
    controller = MeteoController(airport_data_path)
    controller.plot_airports_with_weather()
    

if __name__ == "__main__":
    main()
