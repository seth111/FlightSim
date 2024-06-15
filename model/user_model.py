import json

class UserModel:
    def __init__(self, user_id, first_name, last_name, email, password, role, nationality, passport_number, address, licence=None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role = role
        self.nationality = nationality
        self.passport_number = passport_number
        self.address = address
        self.licence = licence

    @staticmethod
    def from_dict(data):
        return UserModel(
            data.get('user_id'),
            data.get('first_name'),
            data.get('last_name'),
            data.get('email'),
            data.get('password'),
            data.get('role'),
            data.get('nationality'),
            data.get('passport_number'),
            data.get('address'),
            data.get('licence')
        )

    @staticmethod
    def load_users(filepath):
        try:
            with open(filepath, 'r') as file:
                return [UserModel.from_dict(data) for data in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def save_users(users, filepath):
        with open(filepath, 'w') as file:
            json.dump([user.__dict__ for user in users], file, indent=4)
