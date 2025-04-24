import requests # type: ignore

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_weather(self, city):
        url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"{city.title()}: {data['current']['temp_c']}°C, {data['current']['condition']['text']}"
        else:
            return f"Could not fetch weather for {city}."

class Logger:
    def __init__(self, filename="history.txt"):
        self.filename = filename

    def log(self, message):
        with open(self.filename, "a") as f:
            f.write(message + "\n")
