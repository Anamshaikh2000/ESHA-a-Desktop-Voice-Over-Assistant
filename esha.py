import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import os
import pygame
import datetime
import threading
import time
from email_util import send_email

try:
    from plyer import notification
except ImportError:
    os.system('pip install plyer')
    from plyer import notification

pygame.init()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 4000  # Increased energy threshold
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("No input detected. Please speak again.")
            return "None"

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except sr.UnknownValueError:
        print("Could not understand the audio, please try again.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        return "None"
    return query.lower()

def check_password():
    with open("password.txt", "r") as file:
        password = file.readline().strip()
    
    speak("Please say the password to continue.")
    while True:
        query = takeCommand()
        if query == password:
            break
        else:
            speak("Incorrect password. Please try again.")

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
    
    speak("Hello mam and all the faculty members and all the B.tech final year students. I hope you all are doing well and are ready with your projects. I am Esha, nice to meet you all. How can I assist you today?")

def set_alarm():
    speak("Sure, please specify the time for the alarm.")
    alarm_time = takeCommand()
    speak(f"Alarm set for {alarm_time}.")

    def alarm_thread():
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time == alarm_time:
                speak("Alarm! It's time to wake up!")
                break
            time.sleep(60)  # Check every minute

    threading.Thread(target=alarm_thread).start()

if __name__ == "__main__":
    check_password()
    welcome()
    while True:
        query = takeCommand()
        if query == "None":
            continue
        
        if "whatsapp" in query:
            from Whatsapp import sendMessage
            sendMessage()

        elif "google" in query:
            from SearchNow import searchGoogle
            searchGoogle(query)

        elif "youtube" in query:
            from SearchNow import searchYoutube
            searchYoutube(query)

        elif "wikipedia" in query:
            from SearchNow import searchWikipedia
            searchWikipedia(query)

        elif "temperature" in query or "weather" in query:
            search = "mam temperature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {search} is {temp}")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Mam, the time is {strTime}")

        elif "send email" in query:
            speak("Whom do you want to send the email to?")
            recipient_email = takeCommand().lower()
            speak("What is the subject of the email?")
            subject = takeCommand()
            speak("Please dictate the body of the email.")
            body = takeCommand()
            # Call send_email function
            send_email(subject, body, recipient_email) 

        elif "set up an alarm" in query:
            set_alarm()

        elif " sleep" in query:
            speak("Going to sleep, mam")
            break

        elif "shutdown the system" in query:
            speak("Are you sure you want to shutdown?")
            confirmation = takeCommand()
            if "yes" in confirmation:
                speak("Shutting down the system.")
                os.system("shutdown /s /t 1")
                break
            elif "no" in confirmation:
                speak("Shutdown cancelled.")
            else:
                speak("Sorry, I didn't get that. What else can I assist you with?")
