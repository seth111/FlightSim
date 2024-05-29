import tkinter.messagebox as messagebox
from model.user_model import UserModel

class MainController:
    def __init__(self, view):
        self.view = view
        self.model = UserModel()
        
    def login(self):
        username = self.view.username_entry.get()
        password = self.view.password_entry.get()
        if self.model.authenticate(username, password):
            self.view.show_dashboard(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            
    def register(self):
        username = self.view.new_username_entry.get()
        password = self.view.new_password_entry.get()
        if self.model.register(username, password):
            messagebox.showinfo("Registration Success", "You have been registered successfully")
            self.view.create_login_frame()
        else:
            messagebox.showerror("Registration Failed", "Username already exists")
            
    def search_flights(self):
        departure = self.view.departure_entry.get()
        arrival = self.view.arrival_entry.get()
        # Implement flight search logic
        messagebox.showinfo("Search", f"Searching flights from {departure} to {arrival}")
