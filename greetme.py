import pyttsx3
import datetime

def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()

def welcome():
    current_hour = datetime.datetime.now().hour
    if 6 <= current_hour < 12:
        speak("Good morning")
    elif 12 <= current_hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    
    speak("Hello mam and all the faculty members and all the BTech final year students. I hope you all are doing well and are ready with your projects. I am Eeesha, nice to meet you all. How can I assist you today?")
