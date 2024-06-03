from model.Meteo_model import WeatherModel
from view.meteo_view import MeteoMap
import tkinter as tk

class MeteoController:
    def __init__(self, root, map_image_path, airport_data):
        self.root = root
        self.weather_model = WeatherModel()
        self.meteo_map = MeteoMap(root, map_image_path)
        self.airport_data = airport_data

    def generate_zones(self):
        self.meteo_map.generate_zones_on_airports(self.airport_data, self.weather_model.get_weather_info)
