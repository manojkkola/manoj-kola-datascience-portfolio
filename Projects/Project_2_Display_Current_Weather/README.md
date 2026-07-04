# Live Weather Lookup Tool

## Overview
A command-line Python application that connects to the OpenWeatherMap API to fetch and display real-time weather conditions. Users can look up weather by U.S. ZIP code or by city and state, with results shown in the temperature unit of their choice.

## Features
- **Two lookup methods**: 5-digit U.S. ZIP code, or city name + 2-letter state abbreviation
- **Unit conversion**: results displayed in Celsius, Fahrenheit, or Kelvin
- **Input validation**: catches invalid ZIP codes, invalid city/state input, and invalid unit selections, with clear error messages guiding the user to retry
- **Clean exit path**: a simple menu-driven loop that lets the user repeat lookups or exit

## How It Works
1. The user selects a lookup method (ZIP code, city/state, or exit) and enters the corresponding details.
2. The app calls the OpenWeatherMap Geocoding API to resolve the location into latitude/longitude coordinates.
3. It then queries the OpenWeatherMap Current Weather API using those coordinates.
4. The result is formatted and displayed in the user's chosen temperature unit.

## Contents
| File | Description |
|---|---|
| `Live_Weather_Prediction_Project.py` | Main application script |
| `Screenshot_for_Output_Celsius.jpg` | Example output in Celsius |
| `Screenshot_for_Output_Fahrenheit.jpg` | Example output in Fahrenheit |
| `Screenshot_Output_Kelvin.jpg` | Example output in Kelvin |
| `Screenshot_for_Invalid_City_Error.jpg` | Error handling for invalid city input |
| `Screenshot_for_Invalid_Zip_Error.jpg` | Error handling for invalid ZIP input |
| `Screenshot__Invalid_Units_Choice_Error.jpg` | Error handling for invalid unit selection |
| `Screenshot_for_Invalid_Choice_Error.jpg` | Error handling for invalid menu choice |
| `Screenshot_to_Exit.jpg` | Example of the exit flow |

## Tools & Methods
Python, REST API integration (OpenWeatherMap Geocoding + Current Weather APIs), input validation, error handling

## Note
The current script has an API key hardcoded directly in the source file. Since this repo is public, that key is exposed to anyone who views the file. It's worth regenerating the key on OpenWeatherMap and loading it via an environment variable (e.g., `os.environ["OWM_API_KEY"]`) instead of committing it directly.

## Author
Manoj Kumar Kola
