import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class MeteoMap:
    def __init__(self, map_image_path, airports):
        self.map_image_path = map_image_path
        self.airports = airports
        self.plot_map()

    def plot_map(self):
        fig, ax = plt.subplots(figsize=(15, 10))
        m = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=85, llcrnrlon=-180, urcrnrlon=180, resolution='c')
        m.drawcoastlines()
        m.drawcountries()
        m.fillcontinents(color='lightgray', lake_color='aqua')
        m.drawmapboundary(fill_color='aqua')

        for airport in self.airports:
            lon, lat = airport['lon'], airport['lat']
            x, y = m(lon, lat)
            m.plot(x, y, 'bo', markersize=5)

<<<<<<< HEAD
        plt.title('Airports on World Map')
        plt.show()
=======
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
    
    def on_resize(self, event):
        # Recalcule la taille et replace l'image sur le canvas
        self.update_canvas_size()
        self.canvas.coords(self.image_on_canvas, 0, 0)
        self.map_photo = ImageTk.PhotoImage(self.map_image)
        self.canvas.itemconfig(self.image_on_canvas, image=self.map_photo)
>>>>>>> dec27febc8a7d9aee959a49c232ba6cf00683519
