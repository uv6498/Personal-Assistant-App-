import speech_recognition as sr
import os
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak the response
def speak_response(response):
    engine.say(response)
    engine.runAndWait()

# Function to listen for a voice command
def listen_for_shutdown_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for shutdown command...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return None

# Function to check if the command matches "shutdown"
def execute_shutdown_command():
    command = listen_for_shutdown_command()
    if command and "shutdown" in command:
        speak_response("Shutting down the system now.")
        print("Shutting down...")
        if os.name == 'nt':  # For Windows
            os.system("shutdown /s /f /t 0")
        else:  # For Unix-based systems (Linux, macOS)
            os.system("shutdown -h now")
    else:
        speak_response("Shutdown command not recognized.")

if __name__ == "__main__":
    execute_shutdown_command()
