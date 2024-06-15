from model.user_model import UserModel

class FlightController:
    def __init__(self, view):
        self.view = view
        self.model = UserModel()

    def get_all_flights(self):
        return self.model.vols

    def modify_flight(self, flight_id, **kwargs):
        flight = next((f for f in self.model.vols if f['id'] == flight_id), None)
        if flight:
            for key, value in kwargs.items():
                flight[key] = value
            self.model.save_vols()

    def delete_flight(self, flight_id):
        self.model.vols = [f for f in self.model.vols if f['id'] != flight_id]
        self.model.save_vols()
