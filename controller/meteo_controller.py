import json
from model.Meteo_model import WeatherModel
from view.meteo_view import MeteoMap
class MeteoController:
    """Controller class for managing weather information of airports.

    This class provides methods to load airport data, fetch weather information for each airport,
    and plot the airports on a meteo map.

    Attributes:
        airport_data_path (str): The path to the JSON file containing airport data.
        airports (list): A list of airports loaded from the JSON file.
        weather_model (WeatherModel): An instance of the WeatherModel class for fetching weather information.

    Methods:
        __init__(self, airport_data_path): Initializes a new instance of the MeteoController class.
        load_airports(self): Load airports from a JSON file.
        get_airports_weather(self): Fetch weather information for each airport.
        plot_airports(self): Plot the airports on the meteo map.
    """

    def __init__(self, airport_data_path):
        """Initialize a new instance of the MeteoController class.

        Parameters:
            airport_data_path (str): The path to the JSON file containing airport data.
        """
        self.airport_data_path = airport_data_path
        self.airports = self.load_airports()
        self.weather_model = WeatherModel()

    def load_airports(self):
        """Load airports from a JSON file.

        This method reads the airport data from a JSON file and returns a list of airports.

        Returns:
            list: A list of airports.
        """
        with open(self.airport_data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['airports']

    def get_airports_weather(self):
        """Fetch weather information for each airport."""
        for airport in self.airports:
            lat = airport['lat']
            lon = airport['lon']
            weather_info = self.weather_model.get_weather_info(lat, lon)
            airport['weather'] = weather_info
            
    def plot_airports(self):
        """Plot the airports on the meteo map.

        This method retrieves the weather information for the airports and plots them on the meteo map.

        Parameters:
            None

        Returns:
            None
        """
        self.get_airports_weather()
        MeteoMap.plot_airports(self.airports)

def main():
    """Main function to run the program."""
    airport_data_path = "airports.json"
    controller = MeteoController(airport_data_path)
    controller.plot_airports_with_weather()
    

if __name__ == "__main__":
    main()
