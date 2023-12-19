import requests
import json

def get_weather(api_key, location):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        return None

def display_weather(data):
    if data:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']} F")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather conditions: {data['weather'][0]['description']}")
    else:
        print("Weather data not available.")

def main():
    print("Command-Line Weather App")
    api_key = "3572eed4e27b3ba3d7f2187aaba38dc0"
    location = input("Enter the city or ZIP code: ")
    weather_data = get_weather(api_key, location)
    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
