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


def main():
    airports_filepath = 'airports.json'
    airports = load_airports(airports_filepath)
    plot_airports(airports)

if __name__ == "__main__":
    main()
