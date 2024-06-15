import json

class Itinerary:
    def __init__(self, itinerary_id, departure_city, departure_airport, arrival_city, arrival_airport, duration, stopover):
        self.itinerary_id = itinerary_id
        self.departure_city = departure_city
        self.departure_airport = departure_airport
        self.arrival_city = arrival_city
        self.arrival_airport = arrival_airport
        self.duration = duration
        self.stopover = stopover

    @staticmethod
    def from_dict(data):
        return Itinerary(
            data.get('itinerary_id'),
            data.get('departure_city'),
            data.get('departure_airport'),
            data.get('arrival_city'),
            data.get('arrival_airport'),
            data.get('duration'),
            data.get('stopover')
        )

    @staticmethod
    def load_itineraries(filepath):
        try:
            with open(filepath, 'r') as file:
                return [Itinerary.from_dict(data) for data in json.load(file)]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_itineraries(itineraries, filepath):
        with open(filepath, 'w') as file:
            json.dump([itinerary.__dict__ for itinerary in itineraries], file, indent=4)
