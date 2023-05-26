import requests
def get_weather(city):
    api_key = 'cd976dd2ac33cee5a1735a8405cf5de4'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if weather_data['cod'] == '404':
        print('City not found. Please try again.')
    else:
        print(f"Weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']}C")
        print(f"Description: {weather_data['weather'][0]['description']}")

def main():
    city = input("Enter a city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)

if __name__ == '__main__':
    main()