import os
import tkinter as tk
from tkinter import ttk, messagebox

class AdminView:
    def __init__(self, root):
        self.root = root
        self.root.title("Vue Administrateur")
        self.root.geometry("1024x768")
        self.create_widgets()

    def create_widgets(self):
        image_path = os.path.join("assets", "admin.png")
        if os.path.exists(image_path):
            self.bg_image = tk.PhotoImage(file=image_path)
            self.bg_label = tk.Label(self.root, image=self.bg_image)
            self.bg_label.place(relwidth=1, relheight=1)
        else:
            print(f"Image file not found: {image_path}")

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=20)

        self.create_pilot_button = tk.Button(self.buttons_frame, text="Créer Pilote", command=self.create_pilot)
        self.create_pilot_button.grid(row=0, column=0, padx=10)

        self.create_employee_button = tk.Button(self.buttons_frame, text="Créer Employé", command=self.create_employee)
        self.create_employee_button.grid(row=0, column=1, padx=10)

        self.create_client_button = tk.Button(self.buttons_frame, text="Créer Client", command=self.create_client)
        self.create_client_button.grid(row=0, column=2, padx=10)

        self.create_aircraft_button = tk.Button(self.buttons_frame, text="Créer Véhicule Aérien", command=self.create_aircraft)
        self.create_aircraft_button.grid(row=0, column=3, padx=10)

        self.create_flight_button = tk.Button(self.buttons_frame, text="Créer Vol", command=self.create_flight)
        self.create_flight_button.grid(row=0, column=4, padx=10)

        self.create_reservation_button = tk.Button(self.buttons_frame, text="Créer Réservation", command=self.create_reservation)
        self.create_reservation_button.grid(row=0, column=5, padx=10)

        self.create_itinerary_button = tk.Button(self.buttons_frame, text="Créer Itinéraire", command=self.create_itinerary)
        self.create_itinerary_button.grid(row=0, column=6, padx=10)

        self.view_pilots_button = tk.Button(self.buttons_frame, text="Voir Liste Pilote", command=self.view_pilots)
        self.view_pilots_button.grid(row=1, column=0, padx=10, pady=10)

        self.view_employees_button = tk.Button(self.buttons_frame, text="Voir Liste Employé", command=self.view_employees)
        self.view_employees_button.grid(row=1, column=1, padx=10, pady=10)

        self.view_clients_button = tk.Button(self.buttons_frame, text="Voir Liste Client", command=self.view_clients)
        self.view_clients_button.grid(row=1, column=2, padx=10, pady=10)

        self.view_aircrafts_button = tk.Button(self.buttons_frame, text="Voir Liste Véhicule Aérien", command=self.view_aircrafts)
        self.view_aircrafts_button.grid(row=1, column=3, padx=10, pady=10)

        self.view_flights_button = tk.Button(self.buttons_frame, text="Voir Liste Vol", command=self.view_flights)
        self.view_flights_button.grid(row=1, column=4, padx=10, pady=10)

        self.view_reservations_button = tk.Button(self.buttons_frame, text="Voir Réservation", command=self.view_reservations)
        self.view_reservations_button.grid(row=1, column=5, padx=10, pady=10)

    def create_form(self, title, fields, submit_command):
        form_window = tk.Toplevel(self.root)
        form_window.title(title)
        form_window.geometry("400x400")

        entries = {}
        for field in fields:
            tk.Label(form_window, text=field).pack(pady=5)
            entry = tk.Entry(form_window)
            entry.pack(pady=5)
            entries[field] = entry

        submit_button = tk.Button(form_window, text="Créer", command=lambda: self.submit_form(entries, form_window, submit_command))
        submit_button.pack(pady=20)

        return form_window, entries

    def submit_form(self, entries, form_window, submit_command):
        data = {field: entry.get() for field, entry in entries.items()}
        submit_command(data)
        form_window.destroy()

    def view_list(self, title, columns, data):
        list_window = tk.Toplevel(self.root)
        list_window.title(title)
        list_window.geometry("800x600")

        tree = ttk.Treeview(list_window, columns=columns, show='headings')
        for column in columns:
            tree.heading(column, text=column)
            tree.column(column, anchor='w')

        tree.pack(fill=tk.BOTH, expand=True)

        for item in data:
            tree.insert('', 'end', values=item)

    def create_pilot(self):
        self.create_form("Créer Pilote", ["Nom", "Prénom", "Email", "Mot de passe", "Licence"], self.handle_create_pilot)

    def handle_create_pilot(self, data):
        if data:
            user_data = {
                'user_id': 'P' + str(len(UserModel.load_users('data/users.json')) + 1).zfill(4),
                'first_name': data['Prénom'],
                'last_name': data['Nom'],
                'email': data['Email'],
                'password': data['Mot de passe'],
                'role': 'pilote',
                'nationality': '',
                'passport_number': '',
                'address': '',
                'licence': data['Licence']
            }
            users = UserModel.load_users('data/users.json')
            users.append(UserModel(**user_data))
            UserModel.save_users(users, 'data/users.json')
            messagebox.showinfo("Succès", "Pilote créé avec succès")

    def create_employee(self):
        self.create_form("Créer Employé", ["Nom", "Prénom", "Email", "Mot de passe"], self.handle_create_employee)

    def handle_create_employee(self, data):
        if data:
            user_data = {
                'user_id': 'E' + str(len(UserModel.load_users('data/users.json')) + 1).zfill(4),
                'first_name': data['Prénom'],
                'last_name': data['Nom'],
                'email': data['Email'],
                'password': data['Mot de passe'],
                'role': 'employé',
                'nationality': '',
                'passport_number': '',
                'address': ''
            }
            users = UserModel.load_users('data/users.json')
            users.append(UserModel(**user_data))
            UserModel.save_users(users, 'data/users.json')
            messagebox.showinfo("Succès", "Employé créé avec succès")

    def create_client(self):
        self.create_form("Créer Client", ["Nom", "Prénom", "Email", "Mot de passe", "Nationalité", "Numéro de passeport", "Adresse"], self.handle_create_client)

    def handle_create_client(self, data):
        if data:
            user_data = {
                'user_id': 'C' + str(len(UserModel.load_users('data/users.json')) + 1).zfill(4),
                'first_name': data['Prénom'],
                'last_name': data['Nom'],
                'email': data['Email'],
                'password': data['Mot de passe'],
                'role': 'client',
                'nationality': data['Nationalité'],
                'passport_number': data['Numéro de passeport'],
                'address': data['Adresse']
            }
            users = UserModel.load_users('data/users.json')
            users.append(UserModel(**user_data))
            UserModel.save_users(users, 'data/users.json')
            messagebox.showinfo("Succès", "Client créé avec succès")

    def create_aircraft(self):
        self.create_form("Créer Véhicule Aérien", ["Type", "Nom", "Nombre de places prémium", "Nombre de places classiques", "Nombre de places totales", "Poids total"], self.handle_create_aircraft)

    def handle_create_aircraft(self, data):
        if data:
            aircraft_data = {
                'aircraft_id': 'A' + str(len(Aircraft.load_aircrafts('data/aircrafts.json')) + 1).zfill(4),
                'type': data['Type'],
                'name': data['Nom'],
                'premium_seats': data['Nombre de places prémium'],
                'classic_seats': data['Nombre de places classiques'],
                'total_seats': data['Nombre de places totales'],
                'weight': data['Poids total']
            }
            aircrafts = Aircraft.load_aircrafts('data/aircrafts.json')
            aircrafts.append(Aircraft(**aircraft_data))
            Aircraft.save_aircrafts(aircrafts, 'data/aircrafts.json')
            messagebox.showinfo("Succès", "Véhicule aérien créé avec succès")

    def create_flight(self):
        self.create_form("Créer Vol", ["Numéro de vol", "Compagnie aérienne", "Aéroport de départ", "Aéroport d'arrivée", "Heure de départ", "Heure d'arrivée", "Date de départ", "Date d'arrivée", "Durée", "Prix classe économique", "Prix classe affaire"], self.handle_create_flight)

    def handle_create_flight(self, data):
        if data:
            flight_data = {
                'flight_id': 'F' + str(len(Flight.load_flights('data/flights.json')) + 1).zfill(4),
                'airline': data['Compagnie aérienne'],
                'departure_airport': data['Aéroport de départ'],
                'arrival_airport': data['Aéroport d\'arrivée'],
                'departure_time': data['Heure de départ'],
                'arrival_time': data['Heure d\'arrivée'],
                'departure_date': data['Date de départ'],
                'arrival_date': data['Date d\'arrivée'],
                'duration': data['Durée'],
                'price_economy': data['Prix classe économique'],
                'price_business': data['Prix classe affaire'],
                'stopover': ''
            }
            flights = Flight.load_flights('data/flights.json')
            flights.append(Flight(**flight_data))
            Flight.save_flights(flights, 'data/flights.json')
            messagebox.showinfo("Succès", "Vol créé avec succès")

    def create_reservation(self):
        self.create_form("Créer Réservation", ["Client", "Vol", "Date de réservation", "Statut"], self.handle_create_reservation)

    def handle_create_reservation(self, data):
        if data:
            reservation_data = {
                'reservation_id': 'R' + str(len(Reservation.load_reservations('data/reservations.json')) + 1).zfill(4),
                'client': data['Client'],
                'flight': data['Vol'],
                'reservation_date': data['Date de réservation'],
                'status': data['Statut']
            }
            reservations = Reservation.load_reservations('data/reservations.json')
            reservations.append(Reservation(**reservation_data))
            Reservation.save_reservations(reservations, 'data/reservations.json')
            messagebox.showinfo("Succès", "Réservation créée avec succès")

    def create_itinerary(self):
        self.create_form("Créer Itinéraire", ["Ville de départ", "Aéroport de départ", "Ville d'arrivée", "Aéroport d'arrivée", "Durée", "Escale"], self.handle_create_itinerary)

    def handle_create_itinerary(self, data):
        if data:
            itinerary_data = {
                'itinerary_id': 'I' + str(len(Itinerary.load_itineraries('data/itineraries.json')) + 1).zfill(4),
                'departure_city': data['Ville de départ'],
                'departure_airport': data['Aéroport de départ'],
                'arrival_city': data['Ville d\'arrivée'],
                'arrival_airport': data['Aéroport d\'arrivée'],
                'duration': data['Durée'],
                'stopover': data['Escale']
            }
            itineraries = Itinerary.load_itineraries('data/itineraries.json')
            itineraries.append(Itinerary(**itinerary_data))
            Itinerary.save_itineraries(itineraries, 'data/itineraries.json')
            messagebox.showinfo("Succès", "Itinéraire créé avec succès")

    def view_pilots(self):
        columns = ["ID", "Nom", "Prénom", "Email", "Licence"]
        pilots = UserModel.load_users('data/users.json')
        pilots = [p for p in pilots if p.role == 'pilote']
        data = [(p.user_id, p.last_name, p.first_name, p.email, p.licence) for p in pilots]
        self.view_list("Liste des Pilotes", columns, data)

    def view_employees(self):
        columns = ["ID", "Nom", "Prénom", "Email"]
        employees = UserModel.load_users('data/users.json')
        employees = [e for e in employees if e.role == 'employé']
        data = [(e.user_id, e.last_name, e.first_name, e.email) for e in employees]
        self.view_list("Liste des Employés", columns, data)

    def view_clients(self):
        columns = ["ID", "Nom", "Prénom", "Email", "Nationalité", "Numéro de passeport", "Adresse"]
        clients = UserModel.load_users('data/users.json')
        clients = [c for c in clients if c.role == 'client']
        data = [(c.user_id, c.last_name, c.first_name, c.email, c.nationality, c.passport_number, c.address) for c in clients]
        self.view_list("Liste des Clients", columns, data)

    def view_aircrafts(self):
        columns = ["ID", "Type", "Nom", "Nombre de places prémium", "Nombre de places classiques", "Nombre de places totales", "Poids total"]
        aircrafts = Aircraft.load_aircrafts('data/aircrafts.json')
        data = [(a.aircraft_id, a.type, a.name, a.premium_seats, a.classic_seats, a.total_seats, a.weight) for a in aircrafts]
        self.view_list("Liste des Véhicules Aériens", columns, data)

    def view_flights(self):
        columns = ["Numéro de vol", "Compagnie aérienne", "Aéroport de départ", "Aéroport d'arrivée", "Heure de départ", "Heure d'arrivée", "Date de départ", "Date d'arrivée", "Durée", "Prix classe économique", "Prix classe affaire"]
        flights = Flight.load_flights('data/flights.json')
        data = [(f.flight_id, f.airline, f.departure_airport, f.arrival_airport, f.departure_time, f.arrival_time, f.departure_date, f.arrival_date, f.duration, f.price_economy, f.price_business) for f in flights]
        self.view_list("Liste des Vols", columns, data)

    def view_reservations(self):
        columns = ["Client", "Vol", "Date de réservation", "Statut"]
        reservations = Reservation.load_reservations('data/reservations.json')
        data = [(r.client, r.flight, r.reservation_date, r.status) for r in reservations]
        self.view_list("Liste des Réservations", columns, data)

    def run(self):
        self.view.root.mainloop()
