import os
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from PIL import Image, ImageTk
import json

class AdminView:
    def __init__(self, root):
        self.root = root
        self.root.title("Vue Administrateur")
        self.root.geometry("1024x768")
        self.create_widgets()

    def create_widgets(self):
        image_path = os.path.join("assets", "admin.jpg")
        if os.path.exists(image_path):
            self.bg_image = Image.open(image_path)
            self.bg_image = ImageTk.PhotoImage(self.bg_image)
            self.bg_label = tk.Label(self.root, image=self.bg_image)
            self.bg_label.place(relwidth=1, relheight=1)
        else:
            print(f"Image file not found: {image_path}")

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=20)

        self.create_pilot_button = tk.Button(self.buttons_frame, text="Créer Pilote", command=self.create_pilot)
        self.create_pilot_button.grid(row=0, column=0, padx=10)

        self.create_employee_button = tk.Button(self.buttons_frame, text="Créer Employé", command=self.create_employee)
        self.create_employee_button.grid(row=0, column=1, padx=10)

        self.create_client_button = tk.Button(self.buttons_frame, text="Créer Client", command=self.create_client)
        self.create_client_button.grid(row=0, column=2, padx=10)

        self.create_aircraft_button = tk.Button(self.buttons_frame, text="Créer Véhicule Aérien", command=self.create_aircraft)
        self.create_aircraft_button.grid(row=0, column=3, padx=10)

        self.create_flight_button = tk.Button(self.buttons_frame, text="Créer Vol", command=self.create_flight)
        self.create_flight_button.grid(row=0, column=4, padx=10)

        self.create_reservation_button = tk.Button(self.buttons_frame, text="Créer Réservation", command=self.create_reservation)
        self.create_reservation_button.grid(row=0, column=5, padx=10)

        self.create_itinerary_button = tk.Button(self.buttons_frame, text="Créer Itinéraire", command=self.create_itinerary)
        self.create_itinerary_button.grid(row=0, column=6, padx=10)

        self.view_pilots_button = tk.Button(self.buttons_frame, text="Voir Liste Pilote", command=self.view_pilots)
        self.view_pilots_button.grid(row=1, column=0, padx=10, pady=10)

        self.view_employees_button = tk.Button(self.buttons_frame, text="Voir Liste Employé", command=self.view_employees)
        self.view_employees_button.grid(row=1, column=1, padx=10, pady=10)

        self.view_clients_button = tk.Button(self.buttons_frame, text="Voir Liste Client", command=self.view_clients)
        self.view_clients_button.grid(row=1, column=2, padx=10, pady=10)

        self.view_aircrafts_button = tk.Button(self.buttons_frame, text="Voir Liste Véhicule Aérien", command=self.view_aircrafts)
        self.view_aircrafts_button.grid(row=1, column=3, padx=10, pady=10)

        self.view_flights_button = tk.Button(self.buttons_frame, text="Voir Liste Vol", command=self.view_flights)
        self.view_flights_button.grid(row=1, column=4, padx=10, pady=10)

        self.view_reservations_button = tk.Button(self.buttons_frame, text="Voir Réservation", command=self.view_reservations)
        self.view_reservations_button.grid(row=1, column=5, padx=10, pady=10)

    def create_form(self, title, fields, submit_command):
        form_window = tk.Toplevel(self.root)
        form_window.title(title)
        form_window.geometry("400x600")

        entries = {}
        for field in fields:
            tk.Label(form_window, text=field).pack(pady=5)
            if field in ["Date de départ", "Date d'arrivée"]:
                cal = Calendar(form_window, selectmode='day', date_pattern='yyyy-mm-dd')
                cal.pack(pady=5)
                entries[field] = cal
            elif field == "Compagnie aérienne":
                with open("data/airlines.json", "r") as file:
                    airlines = json.load(file)
                airline_names = [airline["name"] for airline in airlines]
                combobox = ttk.Combobox(form_window, values=airline_names)
                combobox.pack(pady=5)
                entries[field] = combobox
            else:
                entry = tk.Entry(form_window)
                entry.pack(pady=5)
                entries[field] = entry

        submit_button = tk.Button(form_window, text="Créer", command=lambda: self.submit_form(entries, form_window, submit_command))
        submit_button.pack(pady=20)

        return form_window, entries

    def submit_form(self, entries, form_window, submit_command):
        data = {}
        for field, widget in entries.items():
            if isinstance(widget, Calendar):
                data[field] = widget.get_date()
            elif isinstance(widget, ttk.Combobox):
                data[field] = widget.get()
            else:
                data[field] = widget.get()
        
        if "Heure de départ" in data and "Heure d'arrivée" in data:
            try:
                from datetime import datetime
                fmt = "%H:%M"
                tdelta = datetime.strptime(data["Heure d'arrivée"], fmt) - datetime.strptime(data["Heure de départ"], fmt)
                data["Durée"] = str(tdelta)
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur dans le calcul de la durée : {str(e)}")

        submit_command(data)
        form_window.destroy()

    def view_list(self, title, columns, data):
        list_window = tk.Toplevel(self.root)
        list_window.title(title)
        list_window.geometry("800x600")

        tree = ttk.Treeview(list_window, columns=columns, show='headings')
        for column in columns:
            tree.heading(column, text=column)
            tree.column(column, anchor='w')

        tree.pack(fill=tk.BOTH, expand=True)

        for item in data:
            tree.insert('', 'end', values=item)
