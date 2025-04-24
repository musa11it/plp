from weather import WeatherFetcher, Logger

# Replace this with your real API key from weatherapi.com
API_KEY = "your_api_key_here"

def main():
    print("🌦️ Welcome to My Weather Dashboard!")
    wf = WeatherFetcher(API_KEY)
    logger = Logger()
    
    cities = []

    while True:
        print("\nMenu:\n1. Add City\n2. Show Weather\n3. Exit")
        choice = input("Choose: ")

        if choice == '1':
            city = input("Enter city name: ")
            cities.append(city)

        elif choice == '2':
            for city in cities:
                report = wf.fetch_weather(city)
                print(report)
                logger.log(report)

        elif choice == '3':
            print("👋 Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
