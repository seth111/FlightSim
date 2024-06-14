import tkinter.messagebox as messagebox
from model.user_model import UserModel
from view.admin_view import AdminView
from view.pilot_view import PilotView
from view.client_view import ClientView
from view.employee_view import EmployeeView

class MainController:
    def __init__(self, view):
        self.view = view
        self.model = UserModel()

    def login(self):
        email = self.view.email_entry.get()
        email = self.view.email_entry.get()
        password = self.view.password_entry.get()
        if self.model.authenticate(email, password):
            user = self.model.users[email]
            self.view.show_dashboard(user)
        else:
            messagebox.showerror("Login Failed", "Invalid email or password")
            
    def register(self):
        first_name = self.view.first_name_entry.get()
        last_name = self.view.last_name_entry.get()
        email = self.view.email_entry.get()
        password = self.view.password_entry.get()
        role = self.view.role_var.get()
        if self.model.register(first_name, last_name, email, password, role):
            messagebox.showinfo("Registration Success", "You have been registered successfully")
            self.view.create_login_frame()
        else:
            messagebox.showerror("Registration Failed", "Email already exists")

    def logout(self):
        self.view.create_login_frame()
            
    def search_flights(self):
        departure = self.view.departure_entry.get()
        arrival = self.view.arrival_entry.get()
        # Implement flight search logic
        messagebox.showinfo("Search", f"Searching flights from {departure} to {arrival}")
