import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class MeteoMap:
    @staticmethod
    def plot_airports(airports):
        fig, ax = plt.subplots(figsize=(15, 10))
        m = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=85, llcrnrlon=-180, urcrnrlon=180, resolution='c')
        m.drawcoastlines()
        m.drawcountries()
        m.fillcontinents(color='lightgray', lake_color='aqua')
        m.drawmapboundary(fill_color='aqua')

        for airport in airports:
            lon, lat = airport['lon'], airport['lat']
            x, y = m(lon, lat)
            m.plot(x, y, 'bo', markersize=5)
            weather_info = airport.get('weather', {})
            temp = weather_info.get('temperature', 'N/A')
            wind_speed = weather_info.get('wind_speed', 'N/A')
            cloudiness = weather_info.get('cloudiness', 'N/A')
            plt.text(x, y, f"{airport['name']}\nTemp: {temp}°C\nWind: {wind_speed} m/s\nCloudiness: {cloudiness}%",
                     fontsize=9, ha='right', color='blue')

        plt.title('Airports on World Map with weather informations')
        plt.show()
