import os
import tkinter as tk
from view.main_view import MainView
from controller.meteo_controller import MeteoController

AIRPORTS = {
    'Heathrow': (51.470020, -0.454295),  # London
    'JFK': (40.641311, -73.778139),  # New York
    'Narita': (35.771987, 140.392850),  # Tokyo
    'Charles de Gaulle': (49.009690, 2.547924),  # Paris
    'Sheremetyevo': (55.972642, 37.414589),  # Moscow
}

def main():
    root = tk.Tk()
    app = MainView(root)
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    
    map_image_path = os.path.join(os.path.dirname(__file__), "assets/world-map.jpg")  # Remplacez par le chemin de votre image de la carte du monde
    controller = MeteoController(root, map_image_path, AIRPORTS)
    controller.generate_zones()
    
    root.mainloop()

if __name__ == "__main__":
    main()
