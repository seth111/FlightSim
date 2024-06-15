import tkinter as tk
from tkinter import ttk

class ClientView:
    def __init__(self, root):
        self.root = root
        self.root.title("Vue Client")
        self.root.geometry("1024x768")
        self.create_widgets()

    def create_widgets(self):
        # Welcome Message
        self.welcome_msg = tk.Label(self.root, text="Bienvenue sur votre compte", font=("Helvetica", 16))
        self.welcome_msg.pack(pady=20)

        # Profile Section
        self.profile_section = tk.LabelFrame(self.root, text="Profil du Client")
        self.profile_section.pack(pady=20, padx=20, fill="both", expand="yes")

        self.create_profile()

        # Reservation Section
        self.reservation_section = tk.LabelFrame(self.root, text="Réservations")
        self.reservation_section.pack(pady=20, padx=20, fill="both", expand="yes")

        self.create_reservation_list()

    def create_profile(self):
        # Implementation to display client's profile
        pass

    def create_reservation_list(self):
        # Implementation to display list of reservations
        pass
