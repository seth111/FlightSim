import tkinter.messagebox as messagebox
from model.user_model import UserModel
from model.vol import Vol
from model.aeroport import Aeroport
from model.vehicule_aerien import VehiculeAerien

class AdminController:
    def __init__(self, view):
        self.view = view
        self.user_model = UserModel()
        self.vols = []
        self.aeroports = []
        self.vehicules_aeriens = []

    def create_pilot(self, first_name, last_name, email, password, license_number):
        if self.user_model.register(first_name, last_name, email, password, 'pilote'):
            self.user_model.users[email]['license_number'] = license_number
            self.user_model.save_users()
            messagebox.showinfo("Success", "Pilot created successfully")
        else:
            messagebox.showerror("Error", "Email already exists")

    def create_employee(self, first_name, last_name, email, password):
        if self.user_model.register(first_name, last_name, email, password, 'employé'):
            messagebox.showinfo("Success", "Employee created successfully")
        else:
            messagebox.showerror("Error", "Email already exists")

    def create_flight(self, compagnie, aeroport_depart, aeroport_arrivee, heure_depart, heure_arrivee, date_depart, date_arrivee, duree, prix):
        flight_id = f"F{len(self.vols) + 1:04d}"
        new_flight = Vol(flight_id, compagnie, aeroport_depart, aeroport_arrivee, heure_depart, heure_arrivee, date_depart, date_arrivee, duree, prix)
        self.vols.append(new_flight)
        messagebox.showinfo("Success", "Flight created successfully")

    def create_airport(self, nom, ville, rue, code_postal, nb_pistes, nb_portes_embarquement):
        airport_id = f"A{len(self.aeroports) + 1:04d}"
        new_airport = Aeroport(airport_id, nom, ville, rue, code_postal, nb_pistes, nb_portes_embarquement)
        self.aeroports.append(new_airport)
        messagebox.showinfo("Success", "Airport created successfully")

    def create_aircraft(self, type_vehicule, nb_places_premium, nb_places_classiques, nb_places_totales, poids_total):
        aircraft_id = f"V{len(self.vehicules_aeriens) + 1:04d}"
        new_aircraft = VehiculeAerien(aircraft_id, type_vehicule, nb_places_premium, nb_places_classiques, nb_places_totales, poids_total)
        self.vehicules_aeriens.append(new_aircraft)
        messagebox.showinfo("Success", "Aircraft created successfully")
