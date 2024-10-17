from urllib import (
    request,
    parse
)

import json


class WeatherApi:
    def __init__(self):
        self._base_url = "https://api.open-meteo.com"
        self._forecast_endpoint = "/v1/forecast"

    def get_current_city_weather(self, latitude: float, longitude: float) -> dict[str, str] | bool:
        try:
            params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,surface_pressure"
            }

            query_string = parse.urlencode(params)
            request_url = f"{self._base_url}{self._forecast_endpoint}?{query_string}"

            with request.urlopen(url=request_url) as response:
                data = response.read()

            json_data = json.loads(data.decode("utf-8"))

            return {
                "temperature": f'{json_data["current"]["temperature_2m"]} {json_data["current_units"]["temperature_2m"]}',
                "pressure": f'{json_data["current"]["surface_pressure"]} {json_data["current_units"]["surface_pressure"]}',
                "humidity": f'{json_data["current"]["relative_humidity_2m"]} {json_data["current_units"]["relative_humidity_2m"]}',
            }
        except:
            return False


weather_api = WeatherApi()
