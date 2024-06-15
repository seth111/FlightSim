import json
from itinerary_model import itineraryModel
from itinerary_view import itineraryMap

class itineraryController:
    """
    The itineraryController class is responsible for managing the itinerary of flights.
    
    Attributes:
        airport_data_path (str): The path to the airport data file.
        itinerary_model (itineraryModel): An instance of the itineraryModel class.
        airports (list): A list of airports loaded from the airport data file.
        itinerary_map (itineraryMap): An instance of the itineraryMap class.
    """
    def __init__(self, airport_data_path):
        self.airport_data_path = airport_data_path
        self.itinerary_model = itineraryModel()
        self.airports = self.load_airports()
        self.itinerary_model.load_airports(self.airports)
        self.itinerary_map = itineraryMap()

    def load_airports(self):
        """
        Loads the airports from the airport data file.
        
        Returns:
            list: A list of airports.
        """
        with open(self.airport_data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['airports']

    def find_and_plot_route(self, start_airport_code, end_airport_code):
        """
        Finds the shortest route between two airports and plots it on the itinerary map.
        
        Args:
            start_airport_code (str): The IATA code of the starting airport.
            end_airport_code (str): The IATA code of the destination airport.
        """
        start_airport = next(airport for airport in self.airports if airport['IATA'] == start_airport_code)
        end_airport = next(airport for airport in self.airports if airport['IATA'] == end_airport_code)
        distance = self.itinerary_model.find_shortest_path(start_airport, end_airport)
        self.itinerary_map.plot_itinerary_route(start_airport, end_airport, distance)

    def show_map(self):
        """
        Displays the itinerary map.
        """

        self.itinerary_map.show()

def main():
    airport_data_path = "airports.json"
    controller = itineraryController(airport_data_path)
    start_airport_code = "ATL"  # Exemple de code de départ
    end_airport_code = "LAX"  # Exemple de code de destination
    controller.find_and_plot_route(start_airport_code, end_airport_code)
    controller.show_map()

if __name__ == "__main__":
    main()