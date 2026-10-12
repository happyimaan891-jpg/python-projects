# Weather App in Python (Using OpenWeatherMap API)

import requests

def get_weather(city, api_key):
    # OpenWeatherMap API Endpoint URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            city_name = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_desc = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            print("\n==========================================")
            print(f"      WEATHER IN {city_name.upper()}, {country}")
            print("==========================================")
            print(f"Temperature : {temp}°C")
            print(f"Condition   : {weather_desc.capitalize()}")
            print(f"Humidity    : {humidity}%")
            print(f"Wind Speed  : {wind_speed} m/s")
            print("------------------------------------------")
        elif response.status_code == 404:
            print("\nCity not found! Please check the spelling.")
        else:
            print(f"\nFailed to retrieve weather data. (Error code: {response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"\nNetwork error occurred: {e}")

def main():
    print("==========================================")
    print("              WEATHER APP                 ")
    print("==========================================")
    
    # You can get a free API key from https://openweathermap.org/
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    
    if not api_key:
        print("API key cannot be empty!")
        return

    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ").strip()
        
        if city.lower() == 'exit':
            print("Thank you for using the Weather App. Goodbye!")
            break
        
        if city:
            get_weather(city, api_key)
        else:
            print("City name cannot be empty!")

if __name__ == "__main__":
    main()
