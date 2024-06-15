import json

class Airport:
    def __init__(self, airport_id, name, city, street, postal_code, runways, gates):
        self.airport_id = airport_id
        self.name = name
        self.city = city
        self.street = street
        self.postal_code = postal_code
        self.runways = runways
        self.gates = gates

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['airport_id'], data['name'], data['city'], data['street'], 
            data['postal_code'], data['runways'], data['gates']
        )

    @classmethod
    def load_airports(cls, filepath):
        with open(filepath, 'r') as file:
            airports_data = json.load(file)
        return [cls.from_dict(airport) for airport in airports_data]

    @classmethod
    def save_airports(cls, airports, filepath):
        with open(filepath, 'w') as file:
            json.dump([airport.__dict__ for airport in airports], file, indent=4)
