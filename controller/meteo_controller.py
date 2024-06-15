import json
from Meteo_model import WeatherModel
from meteo_view import MeteoMap

class MeteoController:
    """
    The MeteoController class is responsible for managing weather information for airports.

    Attributes:
        airport_data_path (str): The file path to the airport data.
        airports (list): A list of airports loaded from the airport data file.
        weather_model (WeatherModel): An instance of the WeatherModel class.

    Methods:
        __init__(self, airport_data_path): Initializes a new instance of the MeteoController class.
        load_airports(self): Loads the airports from the airport data file.
        get_airports_weather(self): Retrieves weather information for each airport.
        plot_airports(self): Plots the airports on a map.

    """

    def __init__(self, airport_data_path):
        """
        Initializes a new instance of the MeteoController class.

        Args:
            airport_data_path (str): The file path to the airport data.

        """
        self.airport_data_path = airport_data_path
        self.airports = self.load_airports()
        self.weather_model = WeatherModel()

    def load_airports(self):
        """
        Loads the airports from the airport data file.

        Returns:
            list: A list of airports loaded from the airport data file.

        """
        with open(self.airport_data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['airports']

    def get_airports_weather(self):
        """
        Retrieves weather information for each airport.

        """
        for airport in self.airports:
            lat = airport['lat']
            lon = airport['lon']
            weather_info = self.weather_model.get_weather_info(lat, lon)
            airport['weather'] = weather_info
            
    def plot_airports(self):
        """
        Plots the airports on a map.

        """
        self.get_airports_weather()
        MeteoMap.plot_airports(self.airports)

def main():
    airport_data_path = "Git_FlightSim/airports.json"
    controller = MeteoController(airport_data_path)
    controller.plot_airports()

if __name__ == "__main__":
    main()