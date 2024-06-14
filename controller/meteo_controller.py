from view.meteo_view import MeteoMap
import json

class MeteoController:
    def __init__(self, map_image_path, airport_data_path):
        self.map_image_path = map_image_path
        self.airport_data_path = airport_data_path
        self.airports = self.load_airports()
        self.meteo_map = MeteoMap(self.map_image_path, self.airports)

    def load_airports(self):
        with open(self.airport_data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['airports']

def main():
    map_image_path = "assets/world-map.jpg"
    airport_data_path = "airports.json"
    controller = MeteoController(map_image_path, airport_data_path)

if __name__ == "__main__":
    main()
