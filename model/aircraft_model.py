import json

class Aircraft:
    def __init__(self, aircraft_id, type, name, premium_seats, classic_seats, total_seats, weight):
        self.aircraft_id = aircraft_id
        self.type = type
        self.name = name
        self.premium_seats = premium_seats
        self.classic_seats = classic_seats
        self.total_seats = total_seats
        self.weight = weight

    @staticmethod
    def from_dict(data):
        return Aircraft(
            data.get('aircraft_id'),
            data.get('type'),
            data.get('name'),
            data.get('premium_seats'),
            data.get('classic_seats'),
            data.get('total_seats'),
            data.get('weight')
        )

    @staticmethod
    def load_aircrafts(filepath):
        try:
            with open(filepath, 'r') as file:
                return [Aircraft.from_dict(data) for data in json.load(file)]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_aircrafts(aircrafts, filepath):
        with open(filepath, 'w') as file:
            json.dump([aircraft.__dict__ for aircraft in aircrafts], file, indent=4)
