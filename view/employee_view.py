import tkinter as tk
from controller.employee_controller import EmployeeController

class EmployeeView:
    def __init__(self, root, user, main_controller):
        self.root = root
        self.user = user
        self.main_controller = main_controller
        self.controller = EmployeeController(self)

        self.frame = tk.Frame(root, bg="#2c3e50")
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text=f"Employee: {self.user['first_name']} {self.user['last_name']}", fg="white", bg="#2c3e50").pack(pady=20)

        self.create_reservation_button = tk.Button(self.frame, text="Create Reservation", command=self.create_reservation, bg="#3498db", fg="white", relief="flat")
        self.create_reservation_button.pack(pady=10)

        self.modify_reservation_button = tk.Button(self.frame, text="Modify Reservation", command=self.modify_reservation, bg="#3498db", fg="white", relief="flat")
        self.modify_reservation_button.pack(pady=10)

        self.assign_seat_button = tk.Button(self.frame, text="Assign Seat", command=self.assign_seat, bg="#3498db", fg="white", relief="flat")
        self.assign_seat_button.pack(pady=10)

        self.confirm_payment_button = tk.Button(self.frame, text="Confirm Payment", command=self.confirm_payment, bg="#3498db", fg="white", relief="flat")
        self.confirm_payment_button.pack(pady=10)

        self.delete_client_button = tk.Button(self.frame, text="Delete Client", command=self.delete_client, bg="#3498db", fg="white", relief="flat")
        self.delete_client_button.pack(pady=10)

        logout_btn = tk.Button(self.frame, text="Logout", command=self.logout, bg="#e74c3c", fg="white", relief="flat")
        logout_btn.pack(pady=20)

    def view_profile(self):
        self.clear_frame()
        tk.Label(self.frame, text="Profile", fg="white", bg="#2c3e50").pack(pady=20)
        tk.Label(self.frame, text=f"ID: {self.user['id']}", fg="white", bg="#2c3e50").pack(pady=5)
        tk.Label(self.frame, text=f"Name: {self.user['first_name']} {self.user['last_name']}", fg="white", bg="#2c3e50").pack(pady=5)
        tk.Label(self.frame, text=f"Email: {self.user['email']}", fg="white", bg="#2c3e50").pack(pady=5)
        tk.Label(self.frame, text=f"Role: {self.user['role']}", fg="white", bg="#2c3e50").pack(pady=5)

    def create_reservation(self):
        self.clear_frame()
        tk.Label(self.frame, text="Create Reservation", fg="white", bg="#2c3e50").pack(pady=20)
        # Implement logic to create reservation

    def modify_reservation(self):
        self.clear_frame()
        tk.Label(self.frame, text="Modify Reservation", fg="white", bg="#2c3e50").pack(pady=20)
        # Implement logic to modify reservation

    def assign_seat(self):
        self.clear_frame()
        tk.Label(self.frame, text="Assign Seat", fg="white", bg="#2c3e50").pack(pady=20)
        # Implement logic to assign seat

    def confirm_payment(self):
        self.clear_frame()
        tk.Label(self.frame, text="Confirm Payment", fg="white", bg="#2c3e50").pack(pady=20)
        # Implement logic to confirm payment

    def delete_client(self):
        self.clear_frame()
        tk.Label(self.frame, text="Delete Client", fg="white", bg="#2c3e50").pack(pady=20)
        # Implement logic to delete client

    def logout(self):
        self.main_controller.logout()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
