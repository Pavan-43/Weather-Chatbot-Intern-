import openai
import requests

openai.api_key = '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'


API_KEY = 'a5568991395568d956b3fb0cd3313e1d'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return f"The weather in {city} is {weather}. Temperature: {temperature}°C. Humidity: {humidity}%"
    else:
        return f"Sorry, I couldn't fetch weather information for {city}."


def generate_response(prompt):
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7
    )
    return response.choices[0].text.strip()


def process_input(user_input):
    if 'weather' in user_input.lower():
        city = user_input.split('in', 1)[-1].strip()
        return get_weather(city)
    else:
        return generate_response(user_input)


def main():
    print("Welcome to the Weather Chatbot!")
    print("You can ask for weather information or ask any general question.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            break
        response = process_input(user_input)
        print("Chatbot:", response)


if __name__ == '__main__':
    main()
