import tkinter as tk
from tkinter import ttk

class RegisterView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Créer un compte")
        self.geometry("400x400")
        self.setup_ui()

    def setup_ui(self):
        self.label = ttk.Label(self, text="Créer un compte", font=("Arial", 18))
        self.label.pack(pady=20)

        self.nom_label = ttk.Label(self, text="Nom")
        self.nom_label.pack(pady=5)
        self.nom_entry = ttk.Entry(self)
        self.nom_entry.pack(pady=5)

        self.prenom_label = ttk.Label(self, text="Prénom")
        self.prenom_label.pack(pady=5)
        self.prenom_entry = ttk.Entry(self)
        self.prenom_entry.pack(pady=5)

        self.email_label = ttk.Label(self, text="Email")
        self.email_label.pack(pady=5)
        self.email_entry = ttk.Entry(self)
        self.email_entry.pack(pady=5)

        self.password_label = ttk.Label(self, text="Mot de passe")
        self.password_label.pack(pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        self.register_button = ttk.Button(self, text="S'inscrire", command=self.register)
        self.register_button.pack(pady=20)

    def register(self):
        nom = self.nom_entry.get()
        prenom = self.prenom_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        # Add registration logic here
        self.controller.main_view.show_message(f"Compte créé pour {nom} {prenom}")
        self.destroy()

    def show(self):
        self.deiconify()
