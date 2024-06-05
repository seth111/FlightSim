import tkinter.messagebox as messagebox
from model.user_model import UserModel

class MainController:
    def __init__(self, view):
        self.view = view
        self.model = UserModel()

    def login(self):
        email = self.view.email_entry.get()
        password = self.view.password_entry.get()
        if self.model.authenticate(email, password):
            self.view.show_dashboard(email)
        else:
            messagebox.showerror("Login Failed", "Invalid email or password")

    def register(self, name, lastname, email, password):
        if self.model.register(name, lastname, email, password):
            messagebox.showinfo("Registration Success", "You have been registered successfully")
            self.view.create_login_frame()
        else:
            messagebox.showerror("Registration Failed", "Email already exists")

    def search_flights(self):
        departure = self.view.departure_entry.get()
        arrival = self.view.arrival_entry.get()
        # Implement flight search logic
        messagebox.showinfo("Search", f"Searching flights from {departure} to {arrival}")
