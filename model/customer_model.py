import user_model

class Customer(user_model):
    def __init__(self, id, name, lastname, email, password, num_card_eid, num_passport):
        super().__init__(id, name, lastname, email, password, function="Client")
        self.num_card_eid = num_card_eid
        self.num_passport = num_passport

    def create_flight(self, vol):
        # Logic to create a flight
        pass

    def edit_flight(self, vol):
        # Logic to modify a flight
        pass

    def delete_flight(self, vol):
        # Logic to cancel a flight
        pass

    def see_flight(self):
        # Logic to see the flight details
        pass

    def __str__(self):
        return f"Client {self.name} {self.lastname} - {self.email}"