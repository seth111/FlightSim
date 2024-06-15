import tkinter as tk
from PIL import Image, ImageTk
import os
from controller.aircraft_controller import AircraftController

class AircraftView:
    def __init__(self, root, user, main_controller):
        self.root = root
        self.user = user
        self.main_controller = main_controller
        self.controller = AircraftController(self)

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

        tk.Label(self.frame, text="Aircrafts", fg="white", bg="#2c3e50").pack(pady=20)

        aircrafts = self.controller.get_all_aircrafts()
        for aircraft in aircrafts:
            self.display_aircraft_info(aircraft)

    def resize_background(self, event):
        new_width = event.width
        new_height = event.height
        resized_image = self.bg_image.resize((new_width, new_height), Image.LANCZOS)
        self.bg_image_tk = ImageTk.PhotoImage(resized_image)
        self.bg_label.config(image=self.bg_image_tk)

    def display_aircraft_info(self, aircraft):
        frame = tk.Frame(self.frame, bg="#2c3e50")
        frame.pack(fill="x", pady=5)

        tk.Label(frame, text=f"ID: {aircraft['id']}", fg="white", bg="#2c3e50").pack(side="left", padx=10)
        tk.Label(frame, text=f"Type: {aircraft['type_vehicule']} - Total Seats: {aircraft['nb_places_totales']}", fg="white", bg="#2c3e50").pack(side="left", padx=10)

        tk.Button(frame, text="Modifier", command=lambda: self.modify_aircraft(aircraft), bg="#3498db", fg="white", relief="flat").pack(side="left", padx=5)
        tk.Button(frame, text="Supprimer", command=lambda: self.delete_aircraft(aircraft), bg="#e74c3c", fg="white", relief="flat").pack(side="left", padx=5)

    def modify_aircraft(self, aircraft):
        # Add code to modify aircraft details
        pass

    def delete_aircraft(self, aircraft):
        self.controller.delete_aircraft(aircraft['id'])
        self.view_aircrafts()

    def view_aircrafts(self):
        self.clear_frame()
        aircrafts = self.controller.get_all_aircrafts()
        for aircraft in aircrafts:
            self.display_aircraft_info(aircraft)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
