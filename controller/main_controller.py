import tkinter.messagebox as messagebox
from model.user_model import UserModel

class MainController:
    def __init__(self, view):
        self.view = view
        self.model = UserModel()

    def login(self):
        email = self.view.email_entry.get()
        password = self.view.password_entry.get()
        user = self.model.authenticate(email, password)
        if user:
            if user['function'] == 'Admin':
                self.view.show_admin_dashboard(user['email'])
            else:
                self.view.show_dashboard(user['email'])
        else:
            messagebox.showerror("Login Failed", "Invalid email or password")
        

    def register(self, name, lastname, email, password):
        if self.model.register(name, lastname, email, password):
            messagebox.showinfo("Registration Success", "You have been registered successfully")
            self.view.create_login_frame()
        else:
            messagebox.showerror("Registration Failed", "Email already exists")

    def update_user(self, user_id, name, lastname, email, password, function):
        if self.model.update_user(user_id, name, lastname, email, password, function):
            messagebox.showinfo("Update Success", "User updated successfully")
        else:
            messagebox.showerror("Update Failed", "Failed to update user")

    def delete_user(self, user_id):
        if self.model.delete_user(user_id):
            messagebox.showinfo("Delete Success", "User deleted successfully")
        else:
            messagebox.showerror("Delete Failed", "Failed to delete user")

    def get_users(self):
        return self.model.get_users()
    
    def search_flights(self):
        departure = self.view.departure_entry.get()
        arrival = self.view.arrival_entry.get()
        # Implement flight search logic
        messagebox.showinfo("Search", f"Searching flights from {departure} to {arrival}")
