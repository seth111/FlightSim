import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class ClientView:
    def init(self, root, user):
        self.root = root
        self.user = user
        self.root.title("Vue Client")
        self.root.geometry("1024x768")
        self.create_widgets()

    def create_widgets(self):
        image_path = os.path.join("assets", "client.jpg")
        if os.path.exists(image_path):
            self.bg_image = Image.open(image_path)
            self.bg_image = ImageTk.PhotoImage(self.bg_image)
            self.bg_label = tk.Label(self.root, image=self.bg_image)
            self.bg_label.place(relwidth=1, relheight=1)
        else:
            print(f"Image file not found: {image_path}")

        self.info_label = tk.Label(self.root, text=f"Bienvenue, {self.user.first_name} {self.user.last_name}", font=("Helvetica", 16))
        self.info_label.pack(pady=20)