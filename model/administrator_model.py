from model.user_model import UserModel
import os
import json

class AdministratorModel(UserModel):
    def __init__(self, id, name, lastname, email, password, function):
        super().__init__(id, name, lastname, email, password, function)
        self.administrator_file = 'administrator.json'
    
    def create(self, object, path):
        if os.path.exists(path):
            with open(path, 'r') as file:
                objects = json.load(file)
        else:
            objects = []

        objects.append(object.__dict__)

        with open(path, 'w') as file:
            json.dump(objects, file, indent=4) 

    def delete(self, object_id, path):
        if os.path.exists(path):
            with open(path, 'r') as file:
                objects = json.load(file)

            objects = [obj for obj in objects if obj['id'] != object_id]

            with open(path, 'w') as file:
                json.dump(objects, file, indent=4)

    def edit(self, object_id, new_details, path):
        if os.path.exists(path):
            with open(path, 'r') as file:
                objects = json.load(file)

            for obj in objects:
                if obj['id'] == object_id:
                    obj.update(new_details)

            with open(path, 'w') as file:
                json.dump(objects, file, indent=4)

    def see(self, path):
        if os.path.exists(path):
            with open(path, 'r') as file:
                objects = json.load(file)
            return objects
        return []

