import plotly.graph_objects as go

class MeteoMap:
    """
    A class for generating a map of airports with weather information.

    Methods:
        plot_airports: Plot the airports on a world map with weather information.
    """
    @staticmethod
    
    def plot_airports(airports):
        lats = [airport['lat'] for airport in airports]
        lons = [airport['lon'] for airport in airports]
        texts = []
        for airport in airports:
            weather_info = airport.get('weather', {})
            temp = weather_info.get('temperature', 'N/A')
            wind_speed = weather_info.get('wind_speed', 'N/A')
            cloudiness = weather_info.get('cloudiness', 'N/A')
            text = f"{airport['name']}<br>Temp: {temp}°C<br>Wind: {wind_speed} m/s<br>Cloudiness: {cloudiness}%"
            texts.append(text)

        fig = go.Figure(go.Scattergeo(
            lon = lons,
            lat = lats,
            text = texts,
            mode = 'markers',
            marker=dict(size=8, color='blue'),
            hoverinfo='text'
        ))

        fig.update_geos(
            projection_type="mercator",
            showcoastlines=True,
            coastlinecolor="black",
            showland=True,
            landcolor="lightgray",
            showocean=True,
            oceancolor="lightblue"
        )

        fig.update_layout(
            title = 'Airports on World Map with Weather Information',
            geo_scope='world',
        )

        fig.show()