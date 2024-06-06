import os
import json
import uuid

class UserModel:
    def __init__(self):
        self.users_file = os.path.join('data', 'users.json')
        self.users = self.load_users()
        if not self.users:
            self.register('Remond', 'Kamsu', 'rkamsu@poo.be', 'Administrateur', 'administrateur')

    def load_users(self):
        if not os.path.exists(self.users_file):
            os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
            return {}
        with open(self.users_file, 'r') as file:
            return json.load(file)
        
    def save_users(self):
        with open(self.users_file, 'w') as file:
            json.dump(self.users, file)

    def generate_user_id(self, role):
        prefix = {'administrateur': 'A', 'pilote': 'P', 'employé': 'E', 'client': 'C'}
        return f"{prefix[role]}{uuid.uuid4().hex[:4]}"

    def authenticate(self, email, password):
        user = self.users.get(email)
        return user and user['password'] == password

    def register(self, first_name, last_name, email, password, role):
        if email in self.users:
            return False
        user_id = self.generate_user_id(role)
        self.users[email] = {
            'id': user_id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'role': role
        }
        self.save_users()
        return True
