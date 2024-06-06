<<<<<<< HEAD
import json
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def load_airports(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data['airports']
    

def plot_airports(airports):
    fig, ax = plt.subplots(figsize=(15, 10))
    m = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=85, llcrnrlon=-180, urcrnrlon=180, resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    m.fillcontinents(color='lightgray', lake_color='aqua')
    m.drawmapboundary(fill_color='aqua')

    for airport in airports:
        lon, lat = airports['lon'], airports['lat']
        x, y = m(lon, lat)
        m.plot(x, y, 'bo', markersize=5)

    plt.title('Airports on World Map')
    plt.show()
    
def load_airports(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(data)  # Ajouter ceci pour voir la structure des données
        return data['airports']
=======
import os
import tkinter as tk
from view.main_view import MainView
from controller.meteo_controller import MeteoController
>>>>>>> dec27febc8a7d9aee959a49c232ba6cf00683519


def main():
<<<<<<< HEAD
    airports_filepath = 'airports.json'
    airports = load_airports(airports_filepath)
    plot_airports(airports)
=======
    root = tk.Tk()
    app = MainView(root)
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    
    map_image_path = os.path.join(os.path.dirname(__file__), "assets/world-map.jpg")  # Remplacez par le chemin de votre image de la carte du monde
    controller = MeteoController(root, map_image_path, AIRPORTS)
    controller.generate_zones()
    
    root.mainloop()
>>>>>>> dec27febc8a7d9aee959a49c232ba6cf00683519

if __name__ == "__main__":
    main()
