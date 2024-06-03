import tkinter as tk
from PIL import Image, ImageTk

class MeteoZone:
    def __init__(self, canvas, x, y, size, color, info):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.info = info
        self.draw_zone()
        self.add_hover_event()

    def draw_zone(self):
        self.zone_id = self.canvas.create_oval(
            self.x - self.size, self.y - self.size,
            self.x + self.size, self.y + self.size,
            fill=self.color, outline=""
        )
        self.text_id = self.canvas.create_text(
            self.x, self.y - self.size - 10, text=self.info, fill="black", state=tk.HIDDEN
        )

    def add_hover_event(self):
        self.canvas.tag_bind(self.zone_id, "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.zone_id, "<Leave>", self.on_leave)

    def on_enter(self, event):
        self.canvas.itemconfig(self.text_id, state=tk.NORMAL)

    def on_leave(self, event):
        self.canvas.itemconfig(self.text_id, state=tk.HIDDEN)

class MeteoMap:
    def __init__(self, root, map_image_path):
        self.root = root
        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Chargement de l'image
        self.map_image = Image.open(map_image_path)
        self.original_image = self.map_image.copy()
        self.map_photo = ImageTk.PhotoImage(self.map_image)
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.map_photo)

        self.zones = []

        # Gestion des événements de zoom et de redimensionnement
        self.canvas.bind("<MouseWheel>", self.zoom_with_mouse)
        self.canvas.bind("<Button-4>", self.zoom_with_mouse)
        self.canvas.bind("<Button-5>", self.zoom_with_mouse)
        self.root.bind("<Configure>", self.on_resize)
        self.canvas.focus_set()

        # Ajuster la taille de la fenêtre au démarrage
        self.update_canvas_size()

    def update_canvas_size(self):
        self.canvas.config(width=self.map_image.width, height=self.map_image.height)
        self.canvas.coords(self.image_on_canvas, 0, 0)

    def zoom_with_mouse(self, event):
        if event.delta > 0 or event.num == 4:  # Zoom avant
            self.zoom(1.1)
        elif event.delta < 0 or event.num == 5:  # Zoom arrière
            self.zoom(0.9)

    def zoom(self, factor):
        width, height = self.map_image.size
        new_size = (int(width * factor), int(height * factor))
        self.map_image = self.original_image.resize(new_size, Image.LANCZOS)
        self.map_photo = ImageTk.PhotoImage(self.map_image)
        self.canvas.itemconfig(self.image_on_canvas, image=self.map_photo)
        self.update_canvas_size()

    def latlon_to_xy(self, lat, lon):
        width, height = self.original_image.size
        x = (lon + 180) * (width / 360)
        y = (90 - lat) * (height / 180)
        return int(x), int(y)

    def generate_zones_on_airports(self, airport_data, get_weather_info):
        for airport, (lat, lon) in airport_data.items():
            x, y = self.latlon_to_xy(lat, lon)
            size = 5  # Taille fixe pour plus de précision
            color = 'blue'  # Couleur fixe pour plus de clarté
            info = get_weather_info(airport, lat, lon)
            zone = MeteoZone(self.canvas, x, y, size, color, info)
            self.zones.append(zone)
