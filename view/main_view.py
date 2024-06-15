import os
import tkinter as tk
from tkinter import ttk, messagebox

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Page d'accueil")
        self.root.geometry("1024x768")
        self.create_widgets()

    def create_widgets(self):
        # Vérifiez que le fichier image existe avant de l'utiliser
        image_path = os.path.join("assets", "accueil.png")
        if os.path.exists(image_path):
            self.bg_image = tk.PhotoImage(file=image_path)
            self.bg_label = tk.Label(self.root, image=self.bg_image)
            self.bg_label.place(relwidth=1, relheight=1)
        else:
            print(f"Image file not found: {image_path}")

        # Welcome Message
        self.welcome_msg = tk.Label(self.root, text="Bienvenue sur votre site de réservation de vols pour vos voyages dans l’Europe", font=("Helvetica", 20), bg="white")
        self.welcome_msg.pack(pady=20)

        # Buttons
        self.login_button = tk.Button(self.root, text="Se connecter", command=self.show_login_form)
        self.signup_button = tk.Button(self.root, text="Créer un compte", command=self.show_signup_form)
        self.login_button.pack(side=tk.RIGHT, padx=10)
        self.signup_button.pack(side=tk.RIGHT)

        # Flight Search Section
        self.search_section = tk.LabelFrame(self.root, text="Rechercher un vol")
        self.search_section.pack(pady=20, padx=20, fill="both", expand="yes")

        self.create_flight_search()

    def create_flight_search(self):
        tk.Label(self.search_section, text="Origine").grid(row=0, column=0, padx=10, pady=10)
        self.origin_entry = tk.Entry(self.search_section)
        self.origin_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.search_section, text="Destination").grid(row=0, column=2, padx=10, pady=10)
        self.destination_entry = tk.Entry(self.search_section)
        self.destination_entry.grid(row=0, column=3, padx=10, pady=10)

        tk.Label(self.search_section, text="Départ le").grid(row=1, column=0, padx=10, pady=10)
        self.departure_date = tk.Entry(self.search_section)
        self.departure_date.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.search_section, text="Retour le").grid(row=1, column=2, padx=10, pady=10)
        self.return_date = tk.Entry(self.search_section)
        self.return_date.grid(row=1, column=3, padx=10, pady=10)

        tk.Label(self.search_section, text="Nombre de passagers").grid(row=2, column=0, padx=10, pady=10)
        self.passenger_count = tk.Spinbox(self.search_section, from_=1, to=10)
        self.passenger_count.grid(row=2, column=1, padx=10, pady=10)

        self.search_button = tk.Button(self.search_section, text="Rechercher des vols", command=self.search_flights)
        self.search_button.grid(row=3, column=0, columnspan=4, pady=20)

    def show_login_form(self):
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Se connecter")
        self.login_window.geometry("300x200")

        tk.Label(self.login_window, text="Email").pack(pady=5)
        self.email_entry = tk.Entry(self.login_window)
        self.email_entry.pack(pady=5)

        tk.Label(self.login_window, text="Mot de passe").pack(pady=5)
        self.password_entry = tk.Entry(self.login_window, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.login_window, text="Se connecter", command=self.login).pack(pady=20)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.on_login(email, password)

    def show_signup_form(self):
        self.signup_window = tk.Toplevel(self.root)
        self.signup_window.title("Créer un compte")
        self.signup_window.geometry("400x400")

        fields = ["Nom", "Prénom", "Email", "Nationalité", "Numéro de passeport", "Adresse"]
        self.entries = {}
        for field in fields:
            tk.Label(self.signup_window, text=field).pack(pady=5)
            entry = tk.Entry(self.signup_window)
            entry.pack(pady=5)
            self.entries[field] = entry

        # Ajout du bouton "Créer" pour valider et enregistrer les données
        tk.Button(self.signup_window, text="Créer", command=self.signup).pack(pady=20)

    def signup(self):
        # Retrieve data from entries
        user_data = {
            'first_name': self.entries['Prénom'].get(),
            'last_name': self.entries['Nom'].get(),
            'email': self.entries['Email'].get(),
            'password': 'default_password',  # Vous devriez hacher le mot de passe dans une application réelle
            'role': 'client',
            'nationality': self.entries['Nationalité'].get(),
            'passport_number': self.entries['Numéro de passeport'].get(),
            'address': self.entries['Adresse'].get()
        }
        self.on_signup(user_data)

    def search_flights(self):
        # Retrieve search criteria from entries
        search_criteria = {
            'origin': self.origin_entry.get(),
            'destination': self.destination_entry.get(),
            'departure_date': self.departure_date.get(),
            'return_date': self.return_date.get(),
            'passenger_count': self.passenger_count.get()
        }
        self.on_search_flights(search_criteria)

    def on_signup(self, user_data):
        # À implémenter par le contrôleur
        pass

    def on_login(self, email, password):
        # À implémenter par le contrôleur
        pass

    def on_search_flights(self, search_criteria):
        # À implémenter par le contrôleur
        pass

    def show_success_message(self, message):
        messagebox.showinfo("Succès", message)

    def show_error_message(self, message):
        messagebox.showerror("Erreur", message)

    def show_flight_results(self, flights):
        results_window = tk.Toplevel(self.root)
        results_window.title("Résultats de la recherche de vols")
        results_window.geometry("800x600")

        tree = ttk.Treeview(results_window, columns=("Compagnie", "Origine", "Heure Départ", "Destination", "Heure Arrivée", "Escale", "Durée", "Prix Économique", "Prix Affaires"))
        tree.heading('#0', text='Numéro de Vol')
        tree.column('#0', anchor='w')
        tree.heading('Compagnie', text='Compagnie')
        tree.column('Compagnie', anchor='w')
        tree.heading('Origine', text='Origine')
        tree.column('Origine', anchor='w')
        tree.heading('Heure Départ', text='Heure Départ')
        tree.column('Heure Départ', anchor='w')
        tree.heading('Destination', text='Destination')
        tree.column('Destination', anchor='w')
        tree.heading('Heure Arrivée', text='Heure Arrivée')
        tree.column('Heure Arrivée', anchor='w')
        tree.heading('Escale', text='Escale')
        tree.column('Escale', anchor='w')
        tree.heading('Durée', text='Durée')
        tree.column('Durée', anchor='w')
        tree.heading('Prix Économique', text='Prix Économique')
        tree.column('Prix Économique', anchor='w')
        tree.heading('Prix Affaires', text='Prix Affaires')
        tree.column('Prix Affaires', anchor='w')

        tree.pack(fill=tk.BOTH, expand=True)

        for flight in flights:
            tree.insert('', 'end', text=flight.flight_id, values=(flight.airline, flight.departure_airport, flight.departure_time, flight.arrival_airport, flight.arrival_time, flight.stopover, flight.duration, flight.price_economy, flight.price_business))

        # Ajouter un bouton de réservation
        reserve_button = tk.Button(results_window, text="Réserver", command=lambda: self.reserve_flight(flights, tree))
        reserve_button.pack(pady=20)

    def reserve_flight(self, flights, tree):
        selected_item = tree.selection()
        if not selected_item:
            self.show_error_message("Veuillez sélectionner un vol à réserver")
            return

        selected_flight = None
        for flight in flights:
            if flight.flight_id == tree.item(selected_item)['text']:
                selected_flight = flight
                break

        if selected_flight:
            if self.is_client_logged_in():
                self.proceed_to_reservation(selected_flight)
            else:
                self.show_login_or_signup(selected_flight)

    def is_client_logged_in(self):
        # Placeholder: Implémentez la vérification de l'état de connexion du client
        return False

    def proceed_to_reservation(self, flight):
        # Placeholder: Implémentez la logique pour continuer à la page de réservation
        self.show_success_message(f"Réservation pour le vol {flight.flight_id} réussie")

    def show_login_or_signup(self, flight):
        choice_window = tk.Toplevel(self.root)
        choice_window.title("Connexion ou Création de compte")
        choice_window.geometry("300x200")

        tk.Label(choice_window, text="Veuillez vous connecter ou créer un compte pour réserver ce vol").pack(pady=20)

        tk.Button(choice_window, text="Se connecter", command=lambda: self.show_login_form()).pack(pady=5)
        tk.Button(choice_window, text="Créer un compte", command=lambda: self.show_signup_form()).pack(pady=5)
