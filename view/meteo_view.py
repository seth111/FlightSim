import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from PIL import Image
import tkinter as tk    
from PIL import ImageTk

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
    def __init__(self, map_image_path, airports, get_weather_info):
        self.map_image_path = map_image_path
        self.airports = airports
        self.get_weather_info = get_weather_info
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        self.plot_map()
        self.generate_zones_on_airports()
        self.root.mainloop()

    def plot_map(self):
        self.map_image = Image.open(self.map_image_path)
        self.original_image = self.map_image.copy()
        self.map_photo = ImageTk.PhotoImage(self.map_image)
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.map_photo)
        self.update_canvas_size()
        
    def update_canvas_size(self):
        self.canvas.config(width=self.map_image.width, height=self.map_image.height)
        self.canvas.coords(self.image_on_canvas, 0, 0)

    def latlon_to_xy(self, lat, lon):
        width, height = self.original_image.size
        x = (lon + 180) * (width / 360)
        y = (90 - lat) * (height / 180)
        return int(x), int(y)

    def generate_zones_on_airports(self):
        for airport in self.airports:
            lat, lon = airport['lat'], airport['lon']
            x, y = self.latlon_to_xy(lat, lon)
            size = 5  # Taille fixe pour plus de précision
            color = 'blue'  # Couleur fixe pour plus de clarté
            info = self.get_weather_info(airport['name'], lat, lon)
            zone = MeteoZone(self.canvas, x, y, size, color, info)
            self.canvas.tag_bind(zone.zone_id, "<Enter>", lambda e, zone=zone: zone.on_enter(e))
            self.canvas.tag_bind(zone.zone_id, "<Leave>", lambda e, zone=zone: zone.on_leave(e))

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
