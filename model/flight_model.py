import json

class Flight:
    def __init__(self, flight_id, airline, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, arrival_date, duration, price_economy, price_business, stopover):
        self.flight_id = flight_id
        self.airline = airline
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.duration = duration
        self.price_economy = price_economy
        self.price_business = price_business
        self.stopover = stopover

    @staticmethod
    def from_dict(data):
        return Flight(
            data.get('flight_id'),
            data.get('airline'),
            data.get('departure_airport'),
            data.get('arrival_airport'),
            data.get('departure_time'),
            data.get('arrival_time'),
            data.get('departure_date'),
            data.get('arrival_date'),
            data.get('duration'),
            data.get('price_economy'),
            data.get('price_business'),
            data.get('stopover')
        )

    @staticmethod
    def load_flights(filepath):
        try:
            with open(filepath, 'r') as file:
                return [Flight.from_dict(data) for data in json.load(file)]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_flights(flights, filepath):
        with open(filepath, 'w') as file:
            json.dump([flight.__dict__ for flight in flights], file, indent=4)
