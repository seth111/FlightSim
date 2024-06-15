import json

class City:
    def __init__(self, city_id, name, postal_code, country):
        self.city_id = city_id
        self.name = name
        self.postal_code = postal_code
        self.country = country

    @classmethod
    def from_dict(cls, data):
        return cls(data['city_id'], data['name'], data['postal_code'], data['country'])

    @classmethod
    def load_cities(cls, filepath):
        with open(filepath, 'r') as file:
            cities_data = json.load(file)
        return [cls.from_dict(city) for city in cities_data]

    @classmethod
    def save_cities(cls, cities, filepath):
        with open(filepath, 'w') as file:
            json.dump([city.__dict__ for city in cities], file, indent=4)
