import tkinter as tk
from PIL import Image, ImageTk
import os
from controller.flight_controller import FlightController

class FlightView:
    def __init__(self, root, user, main_controller):
        self.root = root
        self.user = user
        self.main_controller = main_controller
        self.controller = FlightController(self)

        self.frame = tk.Frame(root, bg="#2c3e50")
        self.frame.pack(fill="both", expand=True)

        image_path = "assets/voyages.jpg"
        if os.path.exists(image_path):
            self.bg_image = Image.open(image_path)
        else:
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        self.bg_label = tk.Label(self.frame, bg="#2c3e50")
        self.bg_label.place(relwidth=1, relheight=1)
        self.root.bind("<Configure>", self.resize_background)

        tk.Label(self.frame, text="Flights", fg="white", bg="#2c3e50").pack(pady=20)

        flights = self.controller.get_all_flights()
        for flight in flights:
            self.display_flight_info(flight)

    def resize_background(self, event):
        new_width = event.width
        new_height = event.height
        resized_image = self.bg_image.resize((new_width, new_height), Image.LANCZOS)
        self.bg_image_tk = ImageTk.PhotoImage(resized_image)
        self.bg_label.config(image=self.bg_image_tk)

    def display_flight_info(self, flight):
        frame = tk.Frame(self.frame, bg="#2c3e50")
        frame.pack(fill="x", pady=5)

        tk.Label(frame, text=f"ID: {flight['id']}", fg="white", bg="#2c3e50").pack(side="left", padx=10)
        tk.Label(frame, text=f"{flight['compagnie']} from {flight['aeroport_depart']} to {flight['aeroport_arrivee']}", fg="white", bg="#2c3e50").pack(side="left", padx=10)

        tk.Button(frame, text="Modifier", command=lambda: self.modify_flight(flight), bg="#3498db", fg="white", relief="flat").pack(side="left", padx=5)
        tk.Button(frame, text="Supprimer", command=lambda: self.delete_flight(flight), bg="#e74c3c", fg="white", relief="flat").pack(side="left", padx=5)

    def modify_flight(self, flight):
        # Add code to modify flight details
        pass

    def delete_flight(self, flight):
        self.controller.delete_flight(flight['id'])
        self.view_flights()

    def view_flights(self):
        self.clear_frame()
        flights = self.controller.get_all_flights()
        for flight in flights:
            self.display_flight_info(flight)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
