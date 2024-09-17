import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is " + Time)
    print("The current time is ", Time)
    
def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak(f"The current date is {day}/{month}/{year}")
    print(f"The current date is {day}/{month}/{year}")

def wishme():
    speak("Welcome back sir,how was your day!")
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 16:
        speak("Good Afternoon!")
    elif 16 <= hour < 24:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("How can I assist you today?")
    print("How can I assist you today?")

def screenshot():
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\ss.png")
    img.save(img_path)
    speak("Screenshot taken and saved to your Pictures folder.")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak("Sorry, I didn't get that. Can you please repeat?")
        return "None"
    return query.lower()
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand()

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            wb.open("youtube.com")
        elif "open google" in query:
            wb.open("google.com")
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = os.path.expanduser("~\\Music")
            songs = os.listdir(music_dir)
            song = random.choice(songs)
            os.startfile(os.path.join(music_dir, song))
        elif "screenshot" in query:
            screenshot()
        elif "offline" in query:
            speak("Going offline. Goodbye!")
            quit()
