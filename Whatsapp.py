import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr

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
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

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

def sendMessage():
    speak("Who do you want to message?")
    recipient = input("Enter the recipient's phone number with country code: ")
    speak("What's the message?")
    message = input("Enter the message: ")
    pywhatkit.sendwhatmsg(recipient, message, time_hour=datetime.datetime.now().hour, time_min=datetime.datetime.now().minute + 1)

if __name__ == "__main__":
    sendMessage()
