import tkinter as tk
from tkinter import PhotoImage
from controller.main_controller import MainController

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Simulator")
        
        self.controller = MainController(self)

        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")
        
        self.login_frame = tk.Frame(root, bg="#2c3e50")
        self.register_frame = tk.Frame(root, bg="#2c3e50")
        self.dashboard_frame = tk.Frame(root, bg="#2c3e50")
        
        self.create_login_frame()
        
    def create_login_frame(self):
        self.clear_frames()
        
        # Background image
        self.bg_image = PhotoImage(file="assets/plane.png")
        self.bg_label = tk.Label(self.login_frame, image=self.bg_image, bg="#2c3e50")
        self.bg_label.place(relwidth=1, relheight=1)

        tk.Label(self.login_frame, text="Nom Utilisateur", fg="white", bg="#2c3e50").grid(row=0, column=0, pady=10)
        tk.Label(self.login_frame, text="Mot de passe", fg="white", bg="#2c3e50").grid(row=1, column=0, pady=10)
        
        self.username_entry = tk.Entry(self.login_frame, bg="#ecf0f1")
        self.password_entry = tk.Entry(self.login_frame, show='*', bg="#ecf0f1")
        
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        
        login_btn = tk.Button(self.login_frame, text="Se Connecter", command=self.controller.login, bg="#3498db", fg="white", relief="flat")
        register_btn = tk.Button(self.login_frame, text="Créer un Compte", command=self.create_register_frame, bg="#2ecc71", fg="white", relief="flat")
        
        login_btn.grid(row=2, column=0, padx=10, pady=20)
        register_btn.grid(row=2, column=1, padx=10, pady=20)
        
        self.login_frame.pack(fill="both", expand=True)
        
    def create_register_frame(self):
        self.clear_frames()
        
        tk.Label(self.register_frame, text="Username", fg="white", bg="#2c3e50").grid(row=0, column=0, pady=10)
        tk.Label(self.register_frame, text="Password", fg="white", bg="#2c3e50").grid(row=1, column=0, pady=10)
        
        self.new_username_entry = tk.Entry(self.register_frame, bg="#ecf0f1")
        self.new_password_entry = tk.Entry(self.register_frame, show='*', bg="#ecf0f1")
        
        self.new_username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.new_password_entry.grid(row=1, column=1, padx=10, pady=10)
        
        register_btn = tk.Button(self.register_frame, text="Register", command=self.controller.register, bg="#3498db", fg="white", relief="flat")
        back_btn = tk.Button(self.register_frame, text="Back", command=self.create_login_frame, bg="#e74c3c", fg="white", relief="flat")
        
        register_btn.grid(row=2, column=0, padx=10, pady=20)
        back_btn.grid(row=2, column=1, padx=10, pady=20)
        
        self.register_frame.pack(fill="both", expand=True)
        
    def show_dashboard(self, username):
        self.clear_frames()
        
        tk.Label(self.dashboard_frame, text=f"Welcome, {username}", fg="white", bg="#2c3e50").pack(pady=20)
        
        tk.Label(self.dashboard_frame, text="Departure Airport", fg="white", bg="#2c3e50").pack(pady=10)
        self.departure_entry = tk.Entry(self.dashboard_frame, bg="#ecf0f1")
        self.departure_entry.pack(pady=5)
        
        tk.Label(self.dashboard_frame, text="Arrival Airport", fg="white", bg="#2c3e50").pack(pady=10)
        self.arrival_entry = tk.Entry(self.dashboard_frame, bg="#ecf0f1")
        self.arrival_entry.pack(pady=5)
        
        search_btn = tk.Button(self.dashboard_frame, text="Search Flights", command=self.controller.search_flights, bg="#3498db", fg="white", relief="flat")
        search_btn.pack(pady=20)
        
        self.dashboard_frame.pack(fill="both", expand=True)
        
    def clear_frames(self):
        for frame in [self.login_frame, self.register_frame, self.dashboard_frame]:
            for widget in frame.winfo_children():
                widget.destroy()
            frame.pack_forget()
