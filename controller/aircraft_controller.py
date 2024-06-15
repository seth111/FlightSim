from model.user_model import UserModel

class AircraftController:
    def __init__(self, view):
        self.view = view
        self.model = UserModel()

    def get_all_aircrafts(self):
        return self.model.aircrafts

    def modify_aircraft(self, aircraft_id, **kwargs):
        aircraft = next((a for a in self.model.aircrafts if a['id'] == aircraft_id), None)
        if aircraft:
            for key, value in kwargs.items():
                aircraft[key] = value
            self.model.save_aircrafts()

    def delete_aircraft(self, aircraft_id):
        self.model.aircrafts = [a for a in self.model.aircrafts if a['id'] != aircraft_id]
        self.model.save_aircrafts()
