import tkinter as tk
from tkinter import ttk

class LoginView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Connexion")
        self.geometry("400x300")
        self.setup_ui()

    def setup_ui(self):
        self.label = ttk.Label(self, text="Connexion", font=("Arial", 18))
        self.label.pack(pady=20)

        self.email_label = ttk.Label(self, text="Email")
        self.email_label.pack(pady=5)
        self.email_entry = ttk.Entry(self)
        self.email_entry.pack(pady=5)

        self.password_label = ttk.Label(self, text="Mot de passe")
        self.password_label.pack(pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = ttk.Button(self, text="Se connecter", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        # Add login logic here
        self.controller.main_view.show_message(f"Connexion réussie pour {email}")
        self.destroy()

    def show(self):
        self.deiconify()
