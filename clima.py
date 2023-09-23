import requests
import os
import json


api_key = os.getenv('WEATHER_API_KEY')


def get_clima(api_key, location):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': api_key,
        'q': location
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        current_weather = data['current']

        # Construct a dictionary with the weather details
        weather_details = {
            "location": location,
            "temperature": f"{current_weather['temp_c']}°C",
            "condition": current_weather['condition']['text'],
            "wind": f"{current_weather['wind_kph']} kph",
            "humidity": f"{current_weather['humidity']}%"
        }

        # Convert the dictionary to a JSON string and return
        return json.dumps(weather_details, indent=4)
    else:
        error_message = {
            "error": f"Error {response.status_code}",
            "message": response.text
        }
        return json.dumps(error_message, indent=4)
