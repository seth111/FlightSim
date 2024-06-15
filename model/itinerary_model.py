import math

class itineraryModel:
    """Represents a model for flight itineraries.

    This class stores information about airports and aircrafts, and provides methods for loading airports,
    calculating distances between airports using the haversine formula, and finding the shortest path between
    two airports.

    Attributes:
        airports (list): A list of airports.
        aircrafts (dict): A dictionary containing information about different types of aircrafts.

    Methods:
        load_airports: Loads a list of airports into the model.
        haversine_distance: Calculates the distance between two sets of coordinates using the haversine formula.
        find_shortest_path: Finds the shortest path between two airports.

    """

    def __init__(self):
        self.airports = []
        self.aircrafts = {
            'plane': [
                {'name': 'Boeing 737', 'speed': 800},  # speed in km/h
                {'name': 'Airbus A320', 'speed': 830}
            ],
            'helicopter': [
                {'name': 'Bell 206', 'speed': 250},
                {'name': 'Eurocopter AS350', 'speed': 300}
            ]
        }

    def load_airports(self, airports):
        """Loads a list of airports into the model.

        Args:
            airports (list): A list of airports.

        """
        self.airports = airports

    def haversine_distance(self, lat1, lon1, lat2, lon2):
        """Calculates the distance between two sets of coordinates using the haversine formula.

        Args:
            lat1 (float): Latitude of the first point.
            lon1 (float): Longitude of the first point.
            lat2 (float): Latitude of the second point.
            lon2 (float): Longitude of the second point.

        Returns:
            float: The distance between the two points in kilometers.

        """
        R = 6371  # Earth radius in km
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance

    def find_shortest_path(self, start_airport, end_airport):
        """Finds the shortest path between two airports.

        Args:
            start_airport (dict): Information about the starting airport.
            end_airport (dict): Information about the destination airport.

        Returns:
            float: The shortest path distance between the two airports in kilometers.

        """
        start_coords = (start_airport['lat'], start_airport['lon'])
        end_coords = (end_airport['lat'], end_airport['lon'])
        distance = self.haversine_distance(*start_coords, *end_coords)
        print(f"La distance de vol entre LAX et ATL est de {distance:.2f} km.")
        return distance