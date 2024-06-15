import plotly.graph_objects as go
from screeninfo import get_monitors

class ItineraryMap:
    """A class representing an itinerary map.

    This class provides methods to plot and display itinerary routes on a map.

    Attributes:
        fig (go.Figure): The figure object for the map.

    Methods:
        __init__(): Initializes the ItineraryMap object.
        plot_itinerary_route(start_airport, end_airport, distance): Plots an itinerary route on the map.
        show(): Displays the map.

    """

    def __init__(self):
        """Initializes the ItineraryMap object.

        This method initializes the ItineraryMap object by setting up the map figure.

        """
        monitor = get_monitors()[0]
        screen_width = monitor.width
        screen_height = monitor.height
        self.fig = go.Figure()
        self.fig.update_geos(
            projection_type="mercator",
            showcountries=True,
            showcoastlines=True,
            coastlinecolor="Black",
            showland=True,
            landcolor="lightgray",
            showocean=True,
            oceancolor="aqua"
        )
        self.fig.update_layout(
            title="Itinerary Routes",
            geo=dict(
                lataxis_showgrid=False,
                lonaxis_showgrid=False
            ),
            width=screen_width * 0.9,  # Utilise 90% de la largeur de l'écran
            height=screen_height * 0.9  # Utilise 90% de la hauteur de l'écran
        )

    def plot_itinerary_route(self, start_airport, end_airport, distance):
        """Plots an itinerary route on the map.

        This method plots an itinerary route on the map using the start and end airport coordinates,
        and the distance between them.

        Args:
            start_airport (dict): A dictionary containing the start airport details.
            end_airport (dict): A dictionary containing the end airport details.
            distance (float): The distance between the start and end airports in kilometers.

        """
        route = go.Scattergeo(
            lon=[start_airport['lon'], end_airport['lon']],
            lat=[start_airport['lat'], end_airport['lat']],
            mode='lines+markers+text',
            text=[start_airport['IATA'], end_airport['IATA']],
            textposition="top center",
            marker=dict(
                size=10,
                color=["green", "red"]
            ),
            line=dict(
                width=2,
                color='blue'
            )
        )
        self.fig.add_trace(route)
        self.fig.update_layout(
            title=f"Itinerary Route: {start_airport['name']} to {end_airport['name']} (Distance: {distance:.2f} km)"
        )
        
    def show(self):
        """Displays the map.

        This method displays the map with the plotted itinerary routes.

        """
        self.fig.show()

# Exemple d'utilisation
start_airport = {'lon': -0.4543, 'lat': 51.4700, 'IATA': 'LHR', 'name': 'London Heathrow'}
end_airport = {'lon': -73.7781, 'lat': 40.6413, 'IATA': 'JFK', 'name': 'John F. Kennedy'}
distance = 5540  # Exemple de distance en km

itinerary_map = ItineraryMap()
itinerary_map.plot_itinerary_route(start_airport, end_airport, distance)
itinerary_map.show()
