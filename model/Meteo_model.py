import requests
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

API_KEY = '083fc7320895785e9e01400993070cd3'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

class WeatherModel:
    """A class that represents a weather model.

    This class provides methods to fetch weather information for given coordinates
    and cache the results for a specified duration.

    Attributes:
        cache (dict): A dictionary to store cached weather data.
        cache_duration (timedelta): The duration for which the weather data is cached.

    Methods:
        get_weather_info: Fetches weather information for given coordinates.

    """

    def __init__(self):
        self.cache = {}
        self.cache_duration = timedelta(minutes=30)  # Cache les résultats pour 30 minutes
        logging.info("WeatherModel initialized with cache duration of 30 minutes.")

    def get_weather_info(self, lat, lon):
        """Fetches weather information for given coordinates.

        Args:
            lat (float): The latitude of the location.
            lon (float): The longitude of the location.

        Returns:
            dict: A dictionary containing the weather information, including temperature,
                  wind speed, wind direction, and cloudiness.

        """
        logging.debug(f"Fetching weather info for coordinates: lat={lat}, lon={lon}")
        now = datetime.now()
        cache_key = (lat, lon)
        
        # Check cache first
        if cache_key in self.cache:
            cached_data, timestamp = self.cache[cache_key]
            if now - timestamp < self.cache_duration:
                logging.debug("Returning cached data.")
                return cached_data
        
        # Fetch data from API
        complete_url = f"{BASE_URL}lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        logging.debug(f"Complete URL for API request: {complete_url}")
        
        try:
            response = requests.get(complete_url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            data = response.json()
            logging.debug(f"API response data: {data}")
            
            if data['cod'] == 200:
                main = data.get('main', {})
                wind = data.get('wind', {})
                clouds = data.get('clouds', {})
                temp = main.get('temp', 'N/A')
                wind_speed = wind.get('speed', 'N/A')
                wind_deg = wind.get('deg', 'N/A')
                cloudiness = clouds.get('all', 'N/A')
                info = {
                    'temperature': temp,
                    'wind_speed': wind_speed,
                    'wind_direction': wind_deg,
                    'cloudiness': cloudiness
                }
                self.cache[cache_key] = (info, now)
                logging.info("Data fetched and cached successfully.")
                return info
            else:
                error_message = f"Error fetching data from API: {data.get('message', 'No message')}"
                logging.error(error_message)
                return {'error': error_message}
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            return {'error': str(e)}

# Example usage
if __name__ == "__main__":
    model = WeatherModel()
    result = model.get_weather_info(33.6407, -84.4277)
    print(result)