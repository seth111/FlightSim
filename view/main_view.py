import tkinter as tk
from tkinter import PhotoImage, messagebox
from controller.main_controller import MainController

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Simulator")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")
        
        self.controller = MainController(self)
        
        # Création des frames pour les différentes vues
        self.login_frame = tk.Frame(self.root, bg="#2c3e50")
        self.dashboard_frame = tk.Frame(self.root, bg="#2c3e50")
        
        self.create_login_frame()
        
    def create_login_frame(self):
        self.clear_frames()
        
        # Image de fond
        self.bg_image = PhotoImage(file="assets/plane.png")
        self.bg_label = tk.Label(self.login_frame, image=self.bg_image, bg="#2c3e50")
        self.bg_label.place(relwidth=1, relheight=1)

        self.email_entry = self.create_label_entry(self.login_frame, "Email", 0)
        self.password_entry = self.create_label_entry(self.login_frame, "Mot de passe", 1, show='*')
        
        login_btn = tk.Button(self.login_frame, text="Se Connecter", command=self.controller.login, bg="#3498db", fg="white", relief="flat")
        register_btn = tk.Button(self.login_frame, text="Créer un Compte", command=self.create_register_frame, bg="#2ecc71", fg="white", relief="flat")
        
        login_btn.grid(row=2, column=0, padx=10, pady=20)
        register_btn.grid(row=2, column=1, padx=10, pady=20)
        
        self.login_frame.pack(fill="both", expand=True)
        
    def create_register_frame(self):
        RegisterView(self.root, self.controller)

    def show_dashboard(self, email):
        self.clear_frames()
        
        tk.Label(self.dashboard_frame, text=f"Bienvenue, {email}", fg="white", bg="#2c3e50").pack(pady=20)
        
        self.departure_entry = self.create_label_entry(self.dashboard_frame, "Aéroport de départ", 0)
        self.arrival_entry = self.create_label_entry(self.dashboard_frame, "Aéroport d'arrivée", 1)
        
        search_btn = tk.Button(self.dashboard_frame, text="Rechercher des vols", command=self.controller.search_flights, bg="#3498db", fg="white", relief="flat")
        search_btn.pack(pady=20)
        
        self.dashboard_frame.pack(fill="both", expand=True)
        
    def create_label_entry(self, frame, text, row, show=None):
        """Création d'une paire label/entrée pour éviter la redondance"""
        label = tk.Label(frame, text=text, fg="white", bg="#2c3e50")
        label.grid(row=row, column=0, pady=10)
        entry = tk.Entry(frame, bg="#ecf0f1", show=show)
        entry.grid(row=row, column=1, padx=10, pady=10)
        return entry
    
    def clear_frames(self):
        """Nettoyage des frames pour éviter la redondance"""
        for frame in [self.login_frame, self.dashboard_frame]:
            for widget in frame.winfo_children():
                widget.destroy()
            frame.pack_forget()


class RegisterView:
    def __init__(self, parent, controller):
        self.window = tk.Toplevel(parent)
        self.window.title("Créer un Compte")
        self.window.geometry("400x300")
        self.window.configure(bg="#2c3e50")
        
        self.controller = controller
        
        self.new_name_entry = self.create_label_entry("Nom", 0)
        self.new_lastname_entry = self.create_label_entry("Prénom", 1)
        self.new_email_entry = self.create_label_entry("Email", 2)
        self.new_password_entry = self.create_label_entry("Mot de passe", 3, show='*')
        
        register_btn = tk.Button(self.window, text="Créer Compte", command=self.creer_compte, bg="#3498db", fg="white", relief="flat")
        back_btn = tk.Button(self.window, text="Retour", command=self.window.destroy, bg="#e74c3c", fg="white", relief="flat")
        
        register_btn.grid(row=4, column=0, padx=10, pady=20)
        back_btn.grid(row=4, column=1, padx=10, pady=20)
    
    def create_label_entry(self, text, row, show=None):
        label = tk.Label(self.window, text=text, fg="white", bg="#2c3e50")
        label.grid(row=row, column=0, pady=10)
        entry = tk.Entry(self.window, bg="#ecf0f1", show=show)
        entry.grid(row=row, column=1, padx=10, pady=10)
        setattr(self, f"entry_{text.replace(' ', '_').lower()}", entry)
    
    def creer_compte(self):
        name = self.entry_nom.get()
        lastname = self.entry_prénom.get()
        email = self.entry_email.get()
        password = self.entry_mot_de_passe.get()
        function = "Client"  # Fonction est définie directement comme "Client"
        
        if self.controller.register(name, lastname, email, password):
            messagebox.showinfo("Succès", "Compte créé avec succès !")
            self.window.destroy()
        else:
            messagebox.showerror("Erreur", "Un compte avec cet email existe déjà")

