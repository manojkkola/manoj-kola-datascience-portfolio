# ----------------------------------------------------------------------------------------------------------------------
# DSC 510
# Week 12
# Programming Assignment Week 12
# Author: Manoj Kumar Kola
# 05/26/2025

# Purpose: An application to interact with a web service to obtain weather data.

import requests

API_KEY="a6c059c29b01f84db321a0832e7ac41e"
geo_base_url = "http://api.openweathermap.org/geo/1.0/"
lat_long_base_url = "http://api.openweathermap.org/data/2.5/weather?"

"""Prompt user to choose lookup method and return location data."""
def get_user_input():

    while True:
        print("\nWeather Lookup Options:")
        print("1. ZIP Code")
        print("2. City and State")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            zip_code = input("Enter a valid 5-digit ZIP Code (US only): ").strip()
            if zip_code.isdigit() and len(zip_code) == 5:
                return {'type': 'zip', 'zip': zip_code}
            else:
                print("Invalid ZIP Code. Please enter a 5-digit number.")

        elif choice == '2':
            city = input("Enter the city name: ").strip()
            state = input("Enter the 2-letter state abbreviation (e.g., NJ): ").strip()
            if city and state.isalpha() and len(state) == 2:
                return {'type': 'city', 'city': city, 'state': state.upper()}
            else:
                print("Invalid city or state input. Please try again.")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


"""Perform GEO lookup using OpenWeather API to get latitude and longitude."""
def geo_lookup(location_data):

    if location_data['type'] == 'zip':
        url = f"{geo_base_url}zip?zip={location_data['zip']},US&appid={API_KEY}"
    else:
        city = location_data['city']
        state = location_data['state']
        url = f"{geo_base_url}direct?q={city},{state},US&appid={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list):
            data = data[0] if data else None
        if not data:
            raise ValueError("Location not found.")
        return data['lat'], data['lon'], data.get('name', 'Unknown City')

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred during GEO lookup: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Network error occurred during GEO lookup: {req_err}")
    except ValueError as e:
        print(f"Invalid location data: {e}")
    return None, None, None

"""Retrieve weather data for specified latitude and longitude."""
def get_weather(lat, lon, units="imperial"):
    weather_url = f"{lat_long_base_url}lat={lat}&lon={lon}&appid={API_KEY}&units={units}"
    try:
        response = requests.get(weather_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred during weather lookup: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Network error occurred during weather lookup: {req_err}")
    return None

"""Format and display weather information to the user."""
def display_weather(data, city_name, units):

    if not data:
        print("No weather data available to display.")
        return

    """defining Units"""
    #temp_unit = "°F" if units == "FH" else "°C"

    if units == "imperial":
        temp_unit = "°F"
    elif units == "metric":
        temp_unit = "°C"
    else:
        temp_unit = "°K"

    print(f"\nWeather Forecast for {city_name}:")
    print(f"Current Temperature: {data['main']['temp']}{temp_unit}")
    print(f"High Temperature: {data['main']['temp_max']}{temp_unit}")
    print(f"Low Temperature: {data['main']['temp_min']}{temp_unit}")
    print(f"Pressure: {data['main']['pressure']} hPa")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Cloud Coverage: {data['clouds']['all']}%")
    print(f"Weather Description: {data['weather'][0]['description'].capitalize()}")

# User option to choose temperature unit.
def choose_units():
    while True:
        print("\nChoose temperature unit:")
        print("1. Fahrenheit (default)")
        print("2. Celsius")
        print("3. Kelvin")
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            return "imperial"
        elif choice == '2':
            return "metric"
        elif choice == '3':
            return "standard"
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def main():
    # Main entry point for the application.
    print("Welcome to the Weather Forecast Lookup Tool!")

    while True:
        location_data = get_user_input()
        lat, lon, city_name = geo_lookup(location_data)
        if lat is None or lon is None:
            continue

        units = choose_units()
        weather_data = get_weather(lat, lon, units)
        display_weather(weather_data, city_name, units)

        re_check = input("\nWould you like to look up another location? (y/n): ").strip().lower()
        if re_check != 'y':
            print("Thanks for using the Weather Forecast Lookup Tool. Stay safe!")
            break

# Entry Point
if __name__ == '__main__':
    main()