import os
import json

class UserModel:
    def __init__(self, id=None, name=None, lastname=None, email=None, password=None, function=None):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.function = function
        
        self.users_file = 'users.json'
        self.users = self.load_users()

    def save_users(self):
        with open(self.users_file, 'w') as file:
            json.dump(self.users, file, indent=4)
    
    def load_users(self):
        if not os.path.exists(self.users_file):
            return []
        with open(self.users_file, 'r') as file:
            return json.load(file)
    
    def authenticate(self, email, password):
        for user in self.users:
            if user['email'] == email and user['password'] == password:
                return True
        return False
    
    def register(self, name, lastname, email, password, function="Client"):
        # Check if the email already exists
        for user in self.users:
            if user['email'] == email:
                return False
        # Create a new user
        new_user = {
            "id": len(self.users) + 1,
            "name": name,
            "lastname": lastname,
            "email": email,
            "password": password,
            "function": function
        }
        self.users.append(new_user)
        self.save_users()
        return True

    def __str__(self):
        return f"{self.name} {self.lastname} - {self.email}"
