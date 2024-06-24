import webbrowser
import wikipedia
from greetme import speak

def searchGoogle(query):
    speak("Searching Google")
    query = query.replace("google", "").strip()
    webbrowser.open(f"https://www.google.com/search?q={query}")

def searchYoutube(query):
    speak("Searching YouTube")
    query = query.replace("youtube", "").strip()
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def searchWikipedia(query):
    speak("Searching Wikipedia")
    query = query.replace("wikipedia", "").strip()
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        print(results)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There were multiple results for your query, please be more specific.")
        print(e.options)
    except wikipedia.exceptions.PageError:
        speak("No page found for your query.")
    except Exception as e:
        speak("An error occurred while searching Wikipedia.")
        print(e)
