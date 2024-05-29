import os
import json

class UserModel:
    def __init__(self):
        self.users_file = 'users.json'
        self.users = self.load_users()
        
    def load_users(self):
        if not os.path.exists(self.users_file):
            return {}
        with open(self.users_file, 'r') as file:
            return json.load(file)
        
    def save_users(self):
        with open(self.users_file, 'w') as file:
            json.dump(self.users, file)
            
    def authenticate(self, username, password):
        user = self.users.get(username)
        return user and user['password'] == password
    
    def register(self, username, password):
        if username in self.users:
            return False
        self.users[username] = {'password': password}
        self.save_users()
        return True
