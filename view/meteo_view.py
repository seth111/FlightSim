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

        plt.title('Airports on World Map')
        plt.show()
