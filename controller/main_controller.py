import json
import os
import tkinter as tk
from view.main_view import MainView
from model.user_model import UserModel
from model.flight_model import Flight

class MainController:
    def __init__(self, root):
        self.root = root
        self.view = MainView(self.root)
        self.view.on_signup = self.handle_signup  # Connect the signup handler
        self.view.on_login = self.handle_login  # Connect the login handler
        self.view.on_search_flights = self.handle_flight_search  # Connect the flight search handler

    def run(self):
        self.root.mainloop()

    def handle_login(self, email, password):
        # Logic for handling login
        users = UserModel.load_users('data/users.json')
        user = next((u for u in users if u.email == email and u.password == password), None)
        if user:
            if user.role == 'administrateur':
                from view.admin_view import AdminView
                from controller.admin_controller import AdminController
                admin_root = tk.Toplevel(self.root)
                admin_view = AdminView(admin_root)
                admin_controller = AdminController(admin_view)
                admin_controller.run()
            elif user.role == 'pilote':
                from view.pilot_view import PilotView
                from controller.pilot_controller import PilotController
                pilot_root = tk.Toplevel(self.root)
                pilot_view = PilotView(pilot_root)
                pilot_controller = PilotController(pilot_view)
                pilot_controller.run()
            elif user.role == 'employé':
                from view.employee_view import EmployeeView
                from controller.employee_controller import EmployeeController
                employee_root = tk.Toplevel(self.root)
                employee_view = EmployeeView(employee_root)
                employee_controller = EmployeeController(employee_view)
                employee_controller.run()
            elif user.role == 'client':
                from view.client_view import ClientView
                from controller.client_controller import ClientController
                client_root = tk.Toplevel(self.root)
                client_view = ClientView(client_root)
                client_controller = ClientController(client_view, user)
                client_controller.run()
        else:
            self.view.show_error_message("Identifiant ou mot de passe incorrect")

    def handle_signup(self, user_data):
        # Generate unique user ID
        users = UserModel.load_users('data/users.json')
        user_data['user_id'] = 'C' + str(len(users) + 1).zfill(4)
        users.append(UserModel(**user_data))
        UserModel.save_users(users, 'data/users.json')
        self.view.show_success_message("Compte créé avec succès")

    def handle_flight_search(self, search_criteria):
        flights = Flight.load_flights('data/flights.json')
        matched_flights = [f for f in flights if f.departure_airport == search_criteria['origin'] and f.arrival_airport == search_criteria['destination'] and f.departure_date == search_criteria['departure_date']]
        if matched_flights:
            self.view.show_flight_results(matched_flights)
        else:
            self.view.show_error_message("Aucun vol trouvé pour les critères donnés")
