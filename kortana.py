import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests
import os
import random
from apscheduler.schedulers.background import BackgroundScheduler
from plyer import notification

def speak(text):
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def greet():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good morning! How can I assist you today?")
    elif 12 <= hour < 18:
        speak("Good afternoon! How can I assist you today?")
    else:
        speak("Good evening! How can I assist you today?")

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def tell_date():
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today's date is {current_date}")

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query}")

def set_reminder(reminder_text, reminder_time):
    scheduler = BackgroundScheduler()
    scheduler.start()

    def job():
        speak(f"Reminder: {reminder_text}")
        notification.notify(
            title='Reminder',
            message=reminder_text,
            app_name='Voice Assistant',
            timeout=10
        )

    scheduler.add_job(job, 'date', run_date=reminder_time)
    speak(f"Reminder set for {reminder_time}")

def get_weather(city):
    api_key = '3572eed4e27b3ba3d7f2187aaba38dc0'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    
    response = requests.get(base_url)
    data = response.json()

    if data["cod"] != "404":
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        speak(f"The weather in {city} is {weather_description}. The temperature is {temperature} faranhiet.")
    else:
        speak(f"Sorry, I couldn't retrieve the weather information for {city}.")

def calculator():
    speak("Sure, what calculation would you like me to perform?")
    expression = listen()

    try:
        result = eval(expression)
        speak(f"The result of {expression} is {result}")
    except Exception as e:
        speak(f"Sorry, I encountered an error: {e}")

def open_website(website):
    speak(f"Opening {website}...")
    url = f"https://{website.lower()}.com"
    webbrowser.open(url)

def play_music():
    music_dir = 'path_to_your_music_directory'
    music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]

    if music_files:
        random_music = random.choice(music_files)
        os.startfile(os.path.join(music_dir, random_music))
        speak("Enjoy the music!")
    else:
        speak("No music files found in the specified directory.")

def main():
    greet()

    while True:
        command = listen()

        if "hello" in command:
            greet()
        elif "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "search" in command:
            speak("What do you want to search for?")
            search_query = listen()
            search_web(search_query)
        elif "weather" in command:
            speak("Sure, for which city?")
            city = listen()
            get_weather(city)
        elif "calculate" in command:
            calculator()
        elif "website" in command:
            speak("Which website would you like to open?")
            website_name = listen()
            open_website(website_name)
        elif "reminder" in command:
            speak("What would you like to set a reminder for?")
            reminder_text = listen()
            speak("When should I remind you?")
            reminder_time = listen()
            set_reminder(reminder_text, reminder_time)
        elif "music" in command:
            play_music()
        elif "exit" in command or "bye" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    main()
