from weather_api import weather_api

from constants import cities_coordinates


def main():
    # while True:

    print(print('\n'.join(cities_coordinates.keys())))
    city = input(
        "Enter the name of the city to display its weather: ").lower().strip()

    if not city.capitalize() in cities_coordinates:
        city = input("Incorrect city, pls try again! ").lower().strip()

    else:
        coordinates = cities_coordinates.get(city.capitalize())
        current_weather = weather_api.get_current_city_weather(
            latitude=coordinates["latitude"], longitude=coordinates["longitude"])

        if not current_weather:
            return print("Error, pls try later")

        print(f"Current weather for: {city.capitalize()}")
        for key, value in current_weather.items():
            print(f"{key.capitalize()} {value}")


if __name__ == "__main__":
    main()
