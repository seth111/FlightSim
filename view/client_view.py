import tkinter as tk
from controller.client_controller import ClientController

class ClientView:
    def __init__(self, root, user, main_controller):
        self.root = root
        self.user = user
        self.main_controller = main_controller
        self.controller = ClientController(self)

        self.frame = tk.Frame(root, bg="#2c3e50")
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text=f"Client: {self.user['first_name']} {self.user['last_name']}", fg="white", bg="#2c3e50").pack(pady=20)

        self.view_flights_button = tk.Button(self.frame, text="View Available Flights", command=self.view_flights, bg="#3498db", fg="white", relief="flat")
        self.view_flights_button.pack(pady=10)

        self.book_flight_button = tk.Button(self.frame, text="Book a Flight", command=self.book_flight, bg="#3498db", fg="white", relief="flat")
        self.book_flight_button.pack(pady=10)

        self.view_reservations_button = tk.Button(self.frame, text="View Reservations", command=self.view_reservations, bg="#3498db", fg="white", relief="flat")
        self.view_reservations_button.pack(pady=10)

        self.update_profile_button = tk.Button(self.frame, text="Update Profile", command=self.update_profile, bg="#3498db", fg="white", relief="flat")
        self.update_profile_button.pack(pady=10)

        logout_btn = tk.Button(self.frame, text="Logout", command=self.logout, bg="#e74c3c", fg="white", relief="flat")
        logout_btn.pack(pady=20)

    def view_profile(self):
        self.clear_frame()
        tk.Label(self.frame, text="Profile", fg="white", bg="#2c3e50").pack(pady=20)
        tk.Label(self.frame, text=f"ID: {self.user['id']}", fg="white", bg="#2c3e50").pack(pady=5)
        tk.Label(self.frame, text=f"Name: {self.user['first_name']} {self.user['last_name']}", fg="white", bg="#2c3e50").pack(pady=5)
        tk.Label(self.frame, text=f"Email: {self.user['email']}", fg="white", bg="#2c3e50").pack(pady=5)
        tk.Label(self.frame, text=f"Role: {self.user['role']}", fg="white", bg="#2c3e50").pack(pady=5)

    def view_flights(self):
        self.clear_frame()
        tk.Label(self.frame, text="Available Flights", fg="white", bg="#2c3e50").pack(pady=20)
        # Add logic to list available flights

    def book_flight(self):
        self.clear_frame()
        tk.Label(self.frame, text="Book a Flight", fg="white", bg="#2c3e50").pack(pady=20)
        # Add logic to book a flight

    def view_reservations(self):
        self.clear_frame()
        tk.Label(self.frame, text="Reservations", fg="white", bg="#2c3e50").pack(pady=20)
        # Add logic to view reservations

    def update_profile(self):
        self.clear_frame()
        tk.Label(self.frame, text="Update Profile", fg="white", bg="#2c3e50").pack(pady=20)
        # Add logic to update profile

    def logout(self):
        self.main_controller.logout()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
