from requests import get


class WeatherApi:
    def __init__(self):
        self._base_url = "https://api.open-meteo.com/v1"
        self._forecast_endpoint = "/forecast"

    def get_current_city_weater(self, latitude: float, longitude: float) -> dict[str, str] | bool:
        try:
            params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": ["temperature_2m", "relative_humidity_2m", "surface_pressure"]
            }

            response = get(
                url=f"{self._base_url}{self._forecast_endpoint}", params=params).json()

            return {
                "temperature": f'{response["current"]["temperature_2m"]} {response["current_units"]["temperature_2m"]}',
                "pressure": f'{response["current"]["surface_pressure"]} {response["current_units"]["surface_pressure"]}',
                "humidity": f'{response["current"]["relative_humidity_2m"]} {response["current_units"]["relative_humidity_2m"]}',
            }
        except:
            return False


weather_api = WeatherApi()
