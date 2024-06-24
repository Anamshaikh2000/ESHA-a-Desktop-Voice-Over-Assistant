import pyttsx3
import speech_recognition as sr
import datetime
import time
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 4000
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

def parse_time(query):
    query = query.replace(" ", "")
    try:
        if "hours" in query or "minutes" in query:
            hours, minutes = 0, 0
            if "hours" in query:
                hours = int(query.split("hours")[0])
                if "minutes" in query:
                    minutes = int(query.split("hours")[1].split("minutes")[0])
            elif "minutes" in query:
                minutes = int(query.split("minutes")[0])
            return (datetime.datetime.now() + datetime.timedelta(hours=hours, minutes=minutes)).time()
        else:
            return datetime.datetime.strptime(query, "%H%M").time()
    except ValueError:
        return None

def set_alarm():
    speak("Please tell me the time to set the alarm. For example, say 'sixteen hours twenty minutes'.")
    while True:
        alarm_time = takeCommand()
        if alarm_time == "None":
            speak("I didn't catch that. Please try again.")
            continue

        alarm_time_obj = parse_time(alarm_time)
        if alarm_time_obj:
            speak(f"Alarm set for {alarm_time_obj.strftime('%H:%M')}")
            break
        else:
            speak("I couldn't understand the time format. Please say the time in HH:MM format.")

    while True:
        current_time = datetime.datetime.now().time()
        if current_time.hour == alarm_time_obj.hour and current_time.minute == alarm_time_obj.minute:
            break
        time.sleep(30)

    speak("Wake up! It's time!")
    # Replace the below line with any alarm sound you want
    os.system("start alarm_sound.mp3")

if __name__ == "__main__":
    set_alarm()
