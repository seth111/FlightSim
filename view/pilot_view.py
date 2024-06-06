import tkinter as tk
from controller.pilot_controller import PilotController

class PilotView:
    def __init__(self, root, user, main_controller):
        self.root = root
        self.user = user
        self.main_controller = main_controller
        self.controller = PilotController(self)

        self.frame = tk.Frame(root, bg="#2c3e50")
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text=f"Pilot: {self.user['first_name']} {self.user['last_name']}", fg="white", bg="#2c3e50").pack(pady=20)

        self.profile_button = tk.Button(self.frame, text="View Profile", command=self.view_profile, bg="#3498db", fg="white", relief="flat")
        self.profile_button.pack(pady=10)

        self.flights_button = tk.Button(self.frame, text="View Flights", command=self.view_flights, bg="#3498db", fg="white", relief="flat")
        self.flights_button.pack(pady=10)

        self.notifications_button = tk.Button(self.frame, text="View Notifications", command=self.view_notifications, bg="#3498db", fg="white", relief="flat")
        self.notifications_button.pack(pady=10)

        logout_btn = tk.Button(self.frame, text="Logout", command=self.logout, bg="#e74c3c", fg="white", relief="flat")
        logout_btn.pack(pady=20)

    def view_profile(self):
        self.clear_frame()
        tk.Label(self.frame, text="Profile", fg="white", bg="#2c3e50").pack(pady=20)
        tk.Label(self.frame, text=f"ID: {self.user['id']}", fg="white", bg="#2c3e50").pack(pady=5)
        tk.Label(self.frame, text=f"Name: {self.user['first_name']} {self.user['last_name']}", fg="white", bg="#2c3e50").pack(pady=5)
        tk.Label(self.frame, text=f"Email: {self.user.get('email', 'N/A')}", fg="white", bg="#2c3e50").pack(pady=5)
        tk.Label(self.frame, text=f"Role: {self.user['role']}", fg="white", bg="#2c3e50").pack(pady=5)
        tk.Label(self.frame, text=f"License Number: {self.user.get('license_number', 'N/A')}", fg="white", bg="#2c3e50").pack(pady=5)

    def view_flights(self):
        self.clear_frame()
        tk.Label(self.frame, text="Flights", fg="white", bg="#2c3e50").pack(pady=20)
        # Add logic to list flights

    def view_notifications(self):
        self.clear_frame()
        tk.Label(self.frame, text="Notifications", fg="white", bg="#2c3e50").pack(pady=20)
        # Add logic to list notifications

    def logout(self):
        self.main_controller.logout()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
