import requests

# API key for OpenWeatherMap
api_key = '30d4741c779ba94c470ca1f63045390a'

# Prompt the user to enter a city
user_input = input("Enter city: ")

# Send a GET request to OpenWeatherMap API to fetch weather data
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# Check if the city was not found
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    # Extract weather information from the JSON response
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    # Print the weather and temperature for the specified city
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")
