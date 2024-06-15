import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from model.reservation_model import Reservation

class EmployeeView:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.root.title("Vue Employé")
        self.root.geometry("1024x768")
        self.create_widgets()

    def create_widgets(self):
        image_path = os.path.join("assets", "employee.jpg")
        if os.path.exists(image_path):
            self.bg_image = Image.open(image_path)
            self.bg_image = ImageTk.PhotoImage(self.bg_image)
            self.bg_label = tk.Label(self.root, image=self.bg_image)
            self.bg_label.place(relwidth=1, relheight=1)
        else:
            print(f"Image file not found: {image_path}")

        self.info_label = tk.Label(self.root, text=f"Bienvenue, {self.user.first_name} {self.user.last_name}", font=("Helvetica", 16))
        self.info_label.pack(pady=20)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=20)

        self.create_reservation_button = tk.Button(self.buttons_frame, text="Créer Réservation", command=self.create_reservation)
        self.create_reservation_button.grid(row=0, column=0, padx=10)

        self.view_reservations_button = tk.Button(self.buttons_frame, text="Voir Réservations", command=self.view_reservations)
        self.view_reservations_button.grid(row=0, column=1, padx=10)

    def create_reservation(self):
        self.create_form("Créer Réservation", ["Client", "Vol", "Date de réservation", "Statut"], self.handle_create_reservation)

    def handle_create_reservation(self, data):
        if data:
            reservation_data = {
                'reservation_id': 'R' + str(len(Reservation.load_reservations('data/reservations.json')) + 1).zfill(4),
                'client': data['Client'],
                'flight': data['Vol'],
                'reservation_date': data['Date de réservation'],
                'status': data['Statut']
            }
            reservations = Reservation.load_reservations('data/reservations.json')
            reservations.append(Reservation(**reservation_data))
            Reservation.save_reservations(reservations, 'data/reservations.json')
            messagebox.showinfo("Succès", "Réservation créée avec succès")

    def view_reservations(self):
        columns = ["Client", "Vol", "Date de réservation", "Statut"]
        reservations = Reservation.load_reservations('data/reservations.json')
        data = [(r.client, r.flight, r.reservation_date, r.status) for r in reservations]
        self.view_list("Liste des Réservations", columns, data)

    def create_form(self, title, fields, submit_command):
        form_window = tk.Toplevel(self.root)
        form_window.title(title)
        form_window.geometry("400x400")

        entries = {}
        for field in fields:
            tk.Label(form_window, text=field).pack(pady=5)
            entry = tk.Entry(form_window)
            entry.pack(pady=5)
            entries[field] = entry

        submit_button = tk.Button(form_window, text="Créer", command=lambda: self.submit_form(entries, form_window, submit_command))
        submit_button.pack(pady=20)

        return form_window, entries

    def submit_form(self, entries, form_window, submit_command):
        data = {field: entry.get() for field, entry in entries.items()}
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
