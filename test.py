from urllib import request, parse

# Пример данных
latitude = 55.7558
longitude = 37.6176

# Базовый URL и endpoint
base_url = "https://api.open-meteo.com"
forecast_endpoint = "/v1/forecast"

# Формируем параметры запроса
params = {
    "latitude": latitude,
    "longitude": longitude,
    # Параметры передаются одной строкой
    "current": "temperature_2m,relative_humidity_2m,surface_pressure"
}

# Кодируем параметры
query_string = parse.urlencode(params)

# Формируем полный URL
request_url = f"{base_url}{forecast_endpoint}?{query_string}"

# Выполняем запрос
with request.urlopen(url=request_url) as response:
    data = response.read()

print(data.decode("utf-8"))
