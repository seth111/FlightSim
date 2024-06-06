import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from controller.main_controller import MainController
from view.admin_view import AdminView
from view.pilot_view import PilotView
from view.client_view import ClientView
from view.employee_view import EmployeeView

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Simulator")
        
        self.controller = MainController(self)

        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")

        self.bg_image = Image.open("assets/plane.png")
        self.bg_label = tk.Label(self.root, bg="#2c3e50")
        self.bg_label.place(relwidth=1, relheight=1)

        self.login_frame = tk.Frame(root, bg="#2c3e50")
        self.register_frame = tk.Frame(root, bg="#2c3e50")
        self.dashboard_frame = tk.Frame(root, bg="#2c3e50")

        self.root.bind("<Configure>", self.resize_background)

        self.create_login_frame()
        
    def resize_background(self, event):
        new_width = event.width
        new_height = event.height
        resized_image = self.bg_image.resize((new_width, new_height), Image.LANCZOS)
        self.bg_image_tk = ImageTk.PhotoImage(resized_image)
        self.bg_label.config(image=self.bg_image_tk)

    def create_login_frame(self):
        self.clear_frames()
        
        self.bg_label.place(relwidth=1, relheight=1)
        
        tk.Label(self.login_frame, text="Email", fg="white", bg="#2c3e50").grid(row=0, column=0, pady=10)
        tk.Label(self.login_frame, text="Password", fg="white", bg="#2c3e50").grid(row=1, column=0, pady=10)
        
        self.email_entry = tk.Entry(self.login_frame, bg="#ecf0f1")
        self.password_entry = tk.Entry(self.login_frame, show='*', bg="#ecf0f1")
        
        self.email_entry.grid(row=0, column=1, padx=10, pady=10)
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        
        login_btn = tk.Button(self.login_frame, text="Login", command=self.controller.login, bg="#3498db", fg="white", relief="flat")
        register_btn = tk.Button(self.login_frame, text="Register", command=self.create_register_frame, bg="#2ecc71", fg="white", relief="flat")
        
        login_btn.grid(row=2, column=0, padx=10, pady=20)
        register_btn.grid(row=2, column=1, padx=10, pady=20)
        
        self.login_frame.pack(fill="both", expand=True)
        
    def create_register_frame(self):
        self.clear_frames()
        
        tk.Label(self.register_frame, text="First Name", fg="white", bg="#2c3e50").grid(row=0, column=0, pady=10)
        tk.Label(self.register_frame, text="Last Name", fg="white", bg="#2c3e50").grid(row=1, column=0, pady=10)
        tk.Label(self.register_frame, text="Email", fg="white", bg="#2c3e50").grid(row=2, column=0, pady=10)
        tk.Label(self.register_frame, text="Password", fg="white", bg="#2c3e50").grid(row=3, column=0, pady=10)
        tk.Label(self.register_frame, text="Role", fg="white", bg="#2c3e50").grid(row=4, column=0, pady=10)
        
        self.first_name_entry = tk.Entry(self.register_frame, bg="#ecf0f1")
        self.last_name_entry = tk.Entry(self.register_frame, bg="#ecf0f1")
        self.email_entry = tk.Entry(self.register_frame, bg="#ecf0f1")
        self.password_entry = tk.Entry(self.register_frame, show='*', bg="#ecf0f1")
        self.role_var = tk.StringVar(value="client")
        self.role_option_menu = tk.OptionMenu(self.register_frame, self.role_var, "administrateur", "pilote", "employé", "client")
        self.role_option_menu.config(bg="#ecf0f1")
        
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)
        self.password_entry.grid(row=3, column=1, padx=10, pady=10)
        self.role_option_menu.grid(row=4, column=1, padx=10, pady=10)
        
        register_btn = tk.Button(self.register_frame, text="Register", command=self.controller.register, bg="#3498db", fg="white", relief="flat")
        back_btn = tk.Button(self.register_frame, text="Back", command=self.create_login_frame, bg="#e74c3c", fg="white", relief="flat")
        
        register_btn.grid(row=5, column=0, padx=10, pady=20)
        back_btn.grid(row=5, column=1, padx=10, pady=20)
        
        self.register_frame.pack(fill="both", expand=True)
        
    def show_dashboard(self, user):
        role = user['role']
        if role == 'administrateur':
            AdminView(self.root, user, self.controller)
        elif role == 'pilote':
            PilotView(self.root, user, self.controller)
        elif role == 'client':
            ClientView(self.root, user, self.controller)
        elif role == 'employé':
            EmployeeView(self.root, user, self.controller)
        
    def clear_frames(self):
        for frame in [self.login_frame, self.register_frame, self.dashboard_frame]:
            for widget in frame.winfo_children():
                widget.destroy()
            frame.pack_forget()
