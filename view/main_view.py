import tkinter as tk
from tkinter import ttk

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Page d'accueil")
        self.root.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        # Background Image
        self.bg_image = tk.PhotoImage(file="assets/accueil.jpg")
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        # Welcome Message
        self.welcome_msg = tk.Label(self.root, text="Bienvenue sur votre site de réservation de vols pour vos voyages dans l’Europe", font=("Helvetica", 16), bg="white")
        self.welcome_msg.pack(pady=20)

        # Buttons
        self.login_button = tk.Button(self.root, text="Se connecter", command=self.show_login_form)
        self.signup_button = tk.Button(self.root, text="Créer un compte", command=self.show_signup_form)
        self.login_button.pack(side=tk.RIGHT, padx=10)
        self.signup_button.pack(side=tk.RIGHT)

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
        # Implementation for login
        pass

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

        tk.Button(self.signup_window, text="Créer", command=self.signup).pack(pady=20)

    def signup(self):
        # Implementation for signup
        pass

    def show_flight_search(self):
        # Implementation for flight search
        pass
