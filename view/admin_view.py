import tkinter as tk
from controller.admin_controller import AdminController

class AdminView:
    def __init__(self, root, user, main_controller):
        self.root = root
        self.user = user
        self.main_controller = main_controller
        self.controller = AdminController(self)

        self.frame = tk.Frame(root, bg="#2c3e50")
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text=f"Admin: {self.user['first_name']} {self.user['last_name']}", fg="white", bg="#2c3e50").pack(pady=20)

        tk.Button(self.frame, text="Create Pilot", command=self.create_pilot, bg="#3498db", fg="white", relief="flat").pack(pady=10)
        tk.Button(self.frame, text="Create Employee", command=self.create_employee, bg="#3498db", fg="white", relief="flat").pack(pady=10)
        tk.Button(self.frame, text="Create Flight", command=self.create_flight, bg="#3498db", fg="white", relief="flat").pack(pady=10)
        tk.Button(self.frame, text="Create Airport", command=self.create_airport, bg="#3498db", fg="white", relief="flat").pack(pady=10)
        tk.Button(self.frame, text="Create Aircraft", command=self.create_aircraft, bg="#3498db", fg="white", relief="flat").pack(pady=10)
        
        logout_btn = tk.Button(self.frame, text="Logout", command=self.logout, bg="#e74c3c", fg="white", relief="flat")
        logout_btn.pack(pady=20)

    def create_pilot(self):
        self.clear_frame()
        tk.Label(self.frame, text="First Name", fg="white", bg="#2c3e50").grid(row=0, column=0, pady=10)
        tk.Label(self.frame, text="Last Name", fg="white", bg="#2c3e50").grid(row=1, column=0, pady=10)
        tk.Label(self.frame, text="Email", fg="white", bg="#2c3e50").grid(row=2, column=0, pady=10)
        tk.Label(self.frame, text="Password", fg="white", bg="#2c3e50").grid(row=3, column=0, pady=10)
        tk.Label(self.frame, text="License Number", fg="white", bg="#2c3e50").grid(row=4, column=0, pady=10)

        first_name_entry = tk.Entry(self.frame, bg="#ecf0f1")
        last_name_entry = tk.Entry(self.frame, bg="#ecf0f1")
        email_entry = tk.Entry(self.frame, bg="#ecf0f1")
        password_entry = tk.Entry(self.frame, show='*', bg="#ecf0f1")
        license_entry = tk.Entry(self.frame, bg="#ecf0f1")

        first_name_entry.grid(row=0, column=1, padx=10, pady=10)
        last_name_entry.grid(row=1, column=1, padx=10, pady=10)
        email_entry.grid(row=2, column=1, padx=10, pady=10)
        password_entry.grid(row=3, column=1, padx=10, pady=10)
        license_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Button(self.frame, text="Create", command=lambda: self.controller.create_pilot(
            first_name_entry.get(),
            last_name_entry.get(),
            email_entry.get(),
            password_entry.get(),
            license_entry.get()
        ), bg="#3498db", fg="white", relief="flat").grid(row=5, column=0, columnspan=2, pady=10)

    def create_employee(self):
        self.clear_frame()
        tk.Label(self.frame, text="First Name", fg="white", bg="#2c3e50").grid(row=0, column=0, pady=10)
        tk.Label(self.frame, text="Last Name", fg="white", bg="#2c3e50").grid(row=1, column=0, pady=10)
        tk.Label(self.frame, text="Email", fg="white", bg="#2c3e50").grid(row=2, column=0, pady=10)
        tk.Label(self.frame, text="Password", fg="white", bg="#2c3e50").grid(row=3, column=0, pady=10)

        first_name_entry = tk.Entry(self.frame, bg="#ecf0f1")
        last_name_entry = tk.Entry(self.frame, bg="#ecf0f1")
        email_entry = tk.Entry(self.frame, bg="#ecf0f1")
        password_entry = tk.Entry(self.frame, show='*', bg="#ecf0f1")

        first_name_entry.grid(row=0, column=1, padx=10, pady=10)
        last_name_entry.grid(row=1, column=1, padx=10, pady=10)
        email_entry.grid(row=2, column=1, padx=10, pady=10)
        password_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self.frame, text="Create", command=lambda: self.controller.create_employee(
            first_name_entry.get(),
            last_name_entry.get(),
            email_entry.get(),
            password_entry.get()
        ), bg="#3498db", fg="white", relief="flat").grid(row=4, column=0, columnspan=2, pady=10)

    def create_flight(self):
        self.clear_frame()
        tk.Label(self.frame, text="Compagnie", fg="white", bg="#2c3e50").grid(row=0, column=0, pady=10)
        tk.Label(self.frame, text="Aéroport de Départ", fg="white", bg="#2c3e50").grid(row=1, column=0, pady=10)
        tk.Label(self.frame, text="Aéroport d'Arrivée", fg="white", bg="#2c3e50").grid(row=2, column=0, pady=10)
        tk.Label(self.frame, text="Heure de Départ", fg="white", bg="#2c3e50").grid(row=3, column=0, pady=10)
        tk.Label(self.frame, text="Heure d'Arrivée", fg="white", bg="#2c3e50").grid(row=4, column=0, pady=10)
        tk.Label(self.frame, text="Date de Départ", fg="white", bg="#2c3e50").grid(row=5, column=0, pady=10)
        tk.Label(self.frame, text="Date d'Arrivée", fg="white", bg="#2c3e50").grid(row=6, column=0, pady=10)
        tk.Label(self.frame, text="Durée", fg="white", bg="#2c3e50").grid(row=7, column=0, pady=10)
        tk.Label(self.frame, text="Prix", fg="white", bg="#2c3e50").grid(row=8, column=0, pady=10)

        compagnie_entry = tk.Entry(self.frame, bg="#ecf0f1")
        aeroport_depart_entry = tk.Entry(self.frame, bg="#ecf0f1")
        aeroport_arrivee_entry = tk.Entry(self.frame, bg="#ecf0f1")
        heure_depart_entry = tk.Entry(self.frame, bg="#ecf0f1")
        heure_arrivee_entry = tk.Entry(self.frame, bg="#ecf0f1")
        date_depart_entry = tk.Entry(self.frame, bg="#ecf0f1")
        date_arrivee_entry = tk.Entry(self.frame, bg="#ecf0f1")
        duree_entry = tk.Entry(self.frame, bg="#ecf0f1")
        prix_entry = tk.Entry(self.frame, bg="#ecf0f1")

        compagnie_entry.grid(row=0, column=1, padx=10, pady=10)
        aeroport_depart_entry.grid(row=1, column=1, padx=10, pady=10)
        aeroport_arrivee_entry.grid(row=2, column=1, padx=10, pady=10)
        heure_depart_entry.grid(row=3, column=1, padx=10, pady=10)
        heure_arrivee_entry.grid(row=4, column=1, padx=10, pady=10)
        date_depart_entry.grid(row=5, column=1, padx=10, pady=10)
        date_arrivee_entry.grid(row=6, column=1, padx=10, pady=10)
        duree_entry.grid(row=7, column=1, padx=10, pady=10)
        prix_entry.grid(row=8, column=1, padx=10, pady=10)

        tk.Button(self.frame, text="Create", command=lambda: self.controller.create_flight(
            compagnie_entry.get(),
            aeroport_depart_entry.get(),
            aeroport_arrivee_entry.get(),
            heure_depart_entry.get(),
            heure_arrivee_entry.get(),
            date_depart_entry.get(),
            date_arrivee_entry.get(),
            duree_entry.get(),
            prix_entry.get()
        ), bg="#3498db", fg="white", relief="flat").grid(row=9, column=0, columnspan=2, pady=10)

    def create_airport(self):
        self.clear_frame()
        tk.Label(self.frame, text="Nom", fg="white", bg="#2c3e50").grid(row=0, column=0, pady=10)
        tk.Label(self.frame, text="Ville", fg="white", bg="#2c3e50").grid(row=1, column=0, pady=10)
        tk.Label(self.frame, text="Rue", fg="white", bg="#2c3e50").grid(row=2, column=0, pady=10)
        tk.Label(self.frame, text="Code Postal", fg="white", bg="#2c3e50").grid(row=3, column=0, pady=10)
        tk.Label(self.frame, text="Nombre de Pistes", fg="white", bg="#2c3e50").grid(row=4, column=0, pady=10)
        tk.Label(self.frame, text="Nombre de Portes d'Embarquement", fg="white", bg="#2c3e50").grid(row=5, column=0, pady=10)

        nom_entry = tk.Entry(self.frame, bg="#ecf0f1")
        ville_entry = tk.Entry(self.frame, bg="#ecf0f1")
        rue_entry = tk.Entry(self.frame, bg="#ecf0f1")
        code_postal_entry = tk.Entry(self.frame, bg="#ecf0f1")
        nb_pistes_entry = tk.Entry(self.frame, bg="#ecf0f1")
        nb_portes_embarquement_entry = tk.Entry(self.frame, bg="#ecf0f1")

        nom_entry.grid(row=0, column=1, padx=10, pady=10)
        ville_entry.grid(row=1, column=1, padx=10, pady=10)
        rue_entry.grid(row=2, column=1, padx=10, pady=10)
        code_postal_entry.grid(row=3, column=1, padx=10, pady=10)
        nb_pistes_entry.grid(row=4, column=1, padx=10, pady=10)
        nb_portes_embarquement_entry.grid(row=5, column=1, padx=10, pady=10)

        tk.Button(self.frame, text="Create", command=lambda: self.controller.create_airport(
            nom_entry.get(),
            ville_entry.get(),
            rue_entry.get(),
            code_postal_entry.get(),
            nb_pistes_entry.get(),
            nb_portes_embarquement_entry.get()
        ), bg="#3498db", fg="white", relief="flat").grid(row=6, column=0, columnspan=2, pady=10)

    def create_aircraft(self):
        self.clear_frame()
        tk.Label(self.frame, text="Type de Véhicule", fg="white", bg="#2c3e50").grid(row=0, column=0, pady=10)
        tk.Label(self.frame, text="Nombre de Places Premium", fg="white", bg="#2c3e50").grid(row=1, column=0, pady=10)
        tk.Label(self.frame, text="Nombre de Places Classiques", fg="white", bg="#2c3e50").grid(row=2, column=0, pady=10)
        tk.Label(self.frame, text="Nombre de Places Totales", fg="white", bg="#2c3e50").grid(row=3, column=0, pady=10)
        tk.Label(self.frame, text="Poids Total", fg="white", bg="#2c3e50").grid(row=4, column=0, pady=10)

        type_vehicule_entry = tk.Entry(self.frame, bg="#ecf0f1")
        nb_places_premium_entry = tk.Entry(self.frame, bg="#ecf0f1")
        nb_places_classiques_entry = tk.Entry(self.frame, bg="#ecf0f1")
        nb_places_totales_entry = tk.Entry(self.frame, bg="#ecf0f1")
        poids_total_entry = tk.Entry(self.frame, bg="#ecf0f1")

        type_vehicule_entry.grid(row=0, column=1, padx=10, pady=10)
        nb_places_premium_entry.grid(row=1, column=1, padx=10, pady=10)
        nb_places_classiques_entry.grid(row=2, column=1, padx=10, pady=10)
        nb_places_totales_entry.grid(row=3, column=1, padx=10, pady=10)
        poids_total_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Button(self.frame, text="Create", command=lambda: self.controller.create_aircraft(
            type_vehicule_entry.get(),
            nb_places_premium_entry.get(),
            nb_places_classiques_entry.get(),
            nb_places_totales_entry.get(),
            poids_total_entry.get()
        ), bg="#3498db", fg="white", relief="flat").grid(row=5, column=0, columnspan=2, pady=10)

    def logout(self):
        self.main_controller.logout()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
