import tkinter as tk
from tkinter import ttk

class PilotView:
    def __init__(self, root):
        self.root = root
        self.root.title("Vue Pilote")
        self.root.geometry("1024x768")
        self.create_widgets()

    def create_widgets(self):
        # Background Image
        self.bg_image = tk.PhotoImage(file="assets/pilot.png")
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        # Profile Section
        self.profile_section = tk.LabelFrame(self.root, text="Profil du Pilote")
        self.profile_section.pack(pady=20, padx=20, fill="both", expand="yes")

        self.create_profile()

        # Flight Section
        self.flight_section = tk.LabelFrame(self.root, text="Vols")
        self.flight_section.pack(pady=20, padx=20, fill="both", expand="yes")

        self.create_flight_list()

    def create_profile(self):
        # Implementation to display pilot's profile
        pass

    def create_flight_list(self):
        # Implementation to display list of flights assigned to the pilot
        pass
