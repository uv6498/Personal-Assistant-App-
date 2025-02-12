import speech_recognition as sr
import pyttsx3
import pywhatkit

def speak(text):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input and return the text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Which song would you like to play?")
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            song_name = recognizer.recognize_google(audio)
            print(f"You said:{song_name}")
            speak(f"Playing {song_name} on YouTube Music")
            return song_name
        except sr.UnknownValueError:
            speak("Sorry, I could not understand. Please try again.")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down. Please try again later.")
            return None

def play_song():
    """Listen for a song name and play it on YouTube Music."""
    song_name = listen()
    if song_name:
        pywhatkit.playonyt(song_name + " song")

if __name__ == "__main__":
    play_song()

