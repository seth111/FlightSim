import json

class Reservation:
    def __init__(self, reservation_id, client, flight, reservation_date, status):
        self.reservation_id = reservation_id
        self.client = client
        self.flight = flight
        self.reservation_date = reservation_date
        self.status = status

    @staticmethod
    def from_dict(data):
        return Reservation(
            data.get('reservation_id'),
            data.get('client'),
            data.get('flight'),
            data.get('reservation_date'),
            data.get('status')
        )

    @staticmethod
    def load_reservations(filepath):
        try:
            with open(filepath, 'r') as file:
                return [Reservation.from_dict(data) for data in json.load(file)]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_reservations(reservations, filepath):
        with open(filepath, 'w') as file:
            json.dump([reservation.__dict__ for reservation in reservations], file, indent=4)
